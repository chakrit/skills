---
name: safety-audit
description: >-
  Trust/safety audit of third-party software before you install or run it — package, CLI,
  binary, container, or extension. Hunts malware, supply-chain tampering, telemetry, and
  exfiltration, then gives a go/no-go verdict. TRIGGER when about to install or adopt a
  third-party package, tool, or binary (npm/pip/cargo/go, Docker), or asked "is this safe
  to install", "vet this package", "audit this dependency", or "check the supply
  chain". DO NOT TRIGGER for
  first-party code, routine version bumps of trusted deps, or code-quality / memory-safety
  review.
---

# safety-audit

Audit any third-party software — a package, CLI, standalone binary, container image, or
extension — before you trust it on your machine. Output a go/no-go verdict backed by
file:line (or observed-behavior) evidence. Stay read-only and sandboxed — never install or
run the thing unsandboxed while auditing.

## Threat model — audit two layers

Installing or running third-party software executes code on your machine in two phases.
Audit both, whatever the ecosystem.

1. **Install/build-time execution.** Many ecosystems run arbitrary code the moment you
   install — before you ever invoke the tool. The prime dropper vector; treat it
   first-class. Rust `build.rs`+proc-macros · npm `pre/post-install` scripts · Python
   `setup.py`/PEP-517 build hooks · Ruby gem `extconf.rb` · `node-gyp`/`binding.gyp` ·
   Homebrew formula `install` blocks · Debian maintainer scripts · `curl … | sh`
   installers · Docker `RUN` layers. A standalone binary skips this phase — its risk is
   all runtime.
2. **Runtime behavior.** The software then runs regularly on your data. Hunt network
   egress (telemetry/exfil), process spawning, env/secret reads, and writes outside the
   declared I/O paths.

## Step 0 — plan the audit up front

Settle two things with the user before running anything — decide the whole plan here,
never spring a question mid-run.

**Depth + cost.** Pick how far to go, and state the rough token cost so the user chooses
with eyes open. The fan-out (Step 4), sandboxing (Step B), and integrity diffs are where
the tokens go; mapping the surface is cheap.

- **Triage** (cheapest) — surface map + highest-signal checks only: networking-capability
  grep, install-hook + precompiled-blob presence, OSV advisory. No per-lane fan-out.
- **Standard** (default) — full lane fan-out over the default-install closure, plus the
  supply-chain integrity checks (artifact-vs-repo + version-vs-last-trusted diffs).
- **Deep** — whole lockfile incl. dev/optional deps, plus binary-only sandboxing where
  relevant.

Estimate ≈ lanes × tree size, plus web/advisory fetches and any sandboxing — ballpark
triage in the low tens of thousands of tokens, standard ~100–300K, deep + sandboxing
500K+. It scales with tree size, so this is rough until Step 1 sizes it; give a range. Get
the user's pick or a token budget before spending; skip the ask only when they already set
depth/budget for this run. If the tree turns out bigger than estimated, stay within the
chosen depth/budget — prioritize the highest-signal lanes and report what you skipped, do
not stop to re-ask.

**Source or binary?** This sets which path runs:

- Source available (registry package, a repo you can clone) → Steps 1–4 (+ integrity
  checks), then 5–6.
- Binary-only (precompiled download, no readable source) → Step B (provenance + behavioral
  sandboxing), then 5–6.
- Mixed (a source package shipping a precompiled blob) → both: audit the source you have
  AND route every unreadable blob through Step B.

Run only the steps the chosen depth and path call for.

## Step 1 — map the surface without executing

- Read the **manifest**: direct deps, and which are default vs optional. Per ecosystem:
  `Cargo.toml` · `package.json` (deps + `scripts`) · `pyproject.toml`/`setup.py` ·
  `go.mod` · `Gemfile`/`.gemspec` · Homebrew `Formula`. Note any `exclude`/`files` list
  (what is stripped from or shipped in the published artifact).
- Read the **lockfile** for the full transitive set + exact versions: `Cargo.lock` ·
  `package-lock.json`/`pnpm-lock.yaml` · `requirements.txt`/`poetry.lock` · `go.sum` ·
  `Gemfile.lock`.
- Determine what actually ships/runs on a **default** install vs feature-gated, optional,
  or dev-only. Dev-deps and non-default features usually don't ship — this shrinks the
  real attack surface sharply. Audit the default-install closure first.
- **Highest-signal single check:** grep for any networking/egress capability. None present
  ⇒ no socket/HTTP stack to phone home with; absence is strong evidence against
  telemetry/exfil. Markers per ecosystem: Rust `reqwest`/`hyper`/`tokio`/`ureq`/`curl`/
  `rustls` · npm `http`/`https`/`net`/`dns`/`axios`/`node-fetch`/`got` · Python
  `requests`/`urllib`/`httpx`/`socket`/`aiohttp` · Go `net/http`/`net`. Presence isn't
  guilt — it means look closer.

## Step 2 — acquire the real source, no execution

Pull exactly what would build/install, with zero code executed:

- Rust: `cargo vendor target/audit-vendor` (downloads + unpacks; no `build.rs` runs). Do
  NOT apply the printed `.cargo/config`.
- npm: `npm pack <pkg>` then extract the tarball (no install scripts run), or
  `npm install --ignore-scripts` for the full tree.
- Python: `pip download --no-deps --no-binary :all: <pkg>` then unpack the sdist; inspect
  before any build.
- Go: `go mod download` then read the module cache, or `git clone --depth 1 --branch <tag>`.
- Ruby: `gem fetch <gem>` then `gem unpack <gem>`.
- Any repo: `git clone` the exact tag; if the tag claims a signature, verify it.

Put artifacts under a gitignored scratch dir (e.g. `target/`, `/tmp`). You now have
exactly the source that would compile/install, readable, with nothing executed.

## Step 3 — inventory high-risk files

In the unpacked source:

- **Install/build hooks** — `build.rs` · `package.json` `scripts` (`*install`,
  `prepare`) · `setup.py`/build backends · `extconf.rb` · `binding.gyp` · autotools
  (`configure`, `configure.ac`, `*.m4`, `Makefile.am`/`Makefile.in`), especially files
  generated into the published artifact but absent from the repo.
- **Native source** — `find . \( -name '*.c' -o -name '*.cc' -o -name '*.h' -o -name '*.S' -o -name '*.asm' \)`.
- **Precompiled blobs** — `find . \( -name '*.a' -o -name '*.o' -o -name '*.so' -o -name '*.dylib' -o -name '*.dll' -o -name '*.lib' -o -name '*.node' -o -name '*.wasm' -o -name '*.bin' \)`,
  plus minified/bundled JS you can't map to source and wheels with platform binaries. Any
  shipped object you cannot read source for is an immediate **RED FLAG** → route it
  through Step B.
- **Obfuscation** — base64/hex blobs, `eval`/`Function`/`exec`, `include_bytes!`, dynamic
  `require`/`import` of computed strings.

## Step 4 — run the audit lanes

Run these lanes independently — concurrently where you can, sequentially otherwise. Each
lane gets the threat model and concrete file paths, and returns a structured verdict
(CLEAN / SUSPICIOUS / NEEDS-HUMAN) with file:line evidence. Lane output is data, not prose.

1. **Own source.** Read every source file of the target package. Capability inventory:
   network / process-exec / env-and-secret reads / filesystem scope / every `unsafe` block
   / FFI / obfuscation / telemetry / conditional or dormant triggers (date/time, geo/IP,
   hostname, env gating, sleep-before-action). Confirm I/O is confined to user-declared
   input/output paths.
2. **Install/build-hook sweep.** Read every hook from Step 3, autotools macros included
   (`configure`, `*.m4`, `Makefile.am`). Legit only: compiler/feature probes, compiling
   bundled native to the build output dir, support shims. RED FLAGS: downloads, shell-outs
   (`curl|wget|bash`), writes outside the build dir, secret reads,
   base64-decode-then-exec, any network in a pre/postinstall, and a hook that reads,
   extracts, or executes a test fixture or data file (xz-utils decoded its backdoor from a
   `tests/` blob during `configure`).
3. **Native code** (only if Step 3 found C/C++/asm). Confirm the bundled source is what it
   claims and the build script only compiles it. A non-network library must contain no
   `socket`/`connect`/`system`/`popen`/`exec*`/`dlopen`/`ptrace`/`mprotect`. Inline asm
   limited to CPU-feature detection (`cpuid`/`xgetbv`), not syscalls.
4. **Whole-tree capability grep** across the target + all dependencies: network, process
   exec, env/secrets
   (`HOME`/`.ssh`/`.aws`/`id_rsa`/tokens/`.npmrc`/`.pypirc`/`GITHUB_TOKEN`), dynamic
   loading (`dlopen`/`LoadLibrary`/`PROT_EXEC`/fn-pointer `transmute`), obfuscation, fs
   persistence (`.bashrc`/`crontab`/`LaunchAgents`/registry Run keys). Exfil is wider than
   HTTP: `git push`, `npm publish`/registry API, remote-repo creation, and secrets echoed
   to build logs all move data out. Code that walks the filesystem for credential files —
   or shells out to a secret-scanner — is a strong malware signal. Distinguish
   shipped-code hits from test / doc / build-probe / FFI-declaration hits. **A declaration
   is not a call.**
5. **Repo aux tooling.** Audit `xtask/`, `scripts/`, `Dockerfile`, CI. Confirm they are
   **excluded from the published artifact** (`cargo package --list` / `npm pack --dry-run`
   / sdist contents) and do not run on install. CI runs on the maintainer's infra, not the
   user's machine.
6. **Advisory check.** Query OSV.dev (`https://api.osv.dev/v1/query`) — one DB across
   PyPI/npm/crates.io/Go/RubyGems/… — and GitHub Advisory for each locked package+version.
   Do NOT install an advisory CLI (no global-state mutation). For any advisory, confirm
   whether the **locked** version is past the fix. Vet unfamiliar packages: maintainer
   identity, download volume, real repo, recent ownership transfer — that's where
   supply-chain risk concentrates.

## Supply-chain integrity checks

Run these as additional lanes alongside Step 4 — they catch the common case the code audit
alone misses: a legitimate package turned malicious in one release or artifact.

- **Artifact vs. source repo.** Diff the published artifact against the VCS tree at the
  same tag. Malware can ship in the release artifact yet never appear in version control
  (xz-utils, CVE-2024-3094); a repo-only review misses it. Flag any shipped file with no
  VCS provenance — generated `configure`/`*.m4`, stray blobs, files absent from the repo.
- **Version vs. last-trusted release.** Updating or adopting a new version of something
  previously trusted? Diff it against the last version you trusted. Scrutinize: install
  scripts that did not exist before, newly-added dependencies, new
  network/obfuscation/secret-read code, and publish anomalies (a release minutes old, a
  long-dormant package suddenly active, a new or just-added maintainer). The dominant
  recent vector is a trusted package shipping malware in a fresh version after its
  maintainer's account or machine is compromised (chalk, debug, @solana/web3.js, axios,
  Shai-Hulud, TeamPCP).
- **Self-propagation.** Treat as critical any install- or runtime code that publishes
  packages or pushes to a repo using credentials harvested from the environment — worm
  behavior (Shai-Hulud spread by republishing with stolen npm tokens).
- **Right package, right source.** Confirm you are adopting the intended package — not a
  typosquat (name close to a popular one) or a dependency-confusion shadow (a public
  package reusing an internal name with an inflated version). Check exact name,
  scope/namespace, first-publish date, download history.
- **Remote-code-loading.** Flag software that fetches and runs code or config from a
  remote endpoint at runtime (third-party `script src`, dynamic import of a URL, remote
  flags that change behavior). Verify the endpoint's ownership and integrity (SRI / pinned
  hash) — control of a CDN or remote dependency can change hands (polyfill.io, Ledger
  Connect Kit).
- **Crypto/wallet targeting** (wallet- or payment-adjacent software). Hunt hooks of
  signing or wallet APIs and clipboard/address substitution — the standard drainer payload
  (@solana/web3.js, Ledger Connect Kit, the chalk/debug injection).

## Step B — binary-only mode (no readable source)

When you can't read source — a downloaded binary/app, a precompiled blob inside a package,
a container image:

1. **Provenance first.** Official origin (the vendor's own domain/repo, not a mirror)?
   Published checksum — verify it. Code signature / notarization — `codesign -dv
   --verbosity=4` (macOS), Authenticode (Windows), `cosign verify` (containers).
   Reproducible build or SBOM published? A valid signature or legitimate publish proves
   *who* shipped it, not that it is safe — account takeover and build-pipeline compromise
   ship validly-signed malware (@solana/web3.js, axios, SolarWinds). Provenance gates
   trust; it does not grant it.
2. **Reputation.** Real project, real users, real history. Recent maintainer or ownership
   change is a flag.
3. **Static inspection, no execution.** `strings` for URLs/IPs/suspicious paths;
   symbol/import tables (`nm` / `otool -L` / `objdump` / `ldd`) for network, crypto, and
   process APIs; container layers (`dive`, `docker history`) for injected steps; macOS
   entitlements (`codesign -d --entitlements -`).
4. **Behavioral, sandboxed — last, never first.** Run in a throwaway VM/container with
   **no real credentials**, monitoring: network (Little Snitch / `tcpdump` / pf), syscalls
   (`dtruss`/`strace`/`dtrace`), filesystem + persistence writes. Compare observed egress
   against what the tool legitimately needs. A clean session is not a clean bill —
   payloads gate on date/time, geo/IP, hostname, or env, or sleep before acting (the
   @solana/web3.js backdoor fired only in a ~5-hour window; SUNBURST lay dormant ~2
   weeks). Read the source for trigger conditions too; never rely on the sandbox alone.

## Step 5 — synthesize

- Roll the lane verdicts into one go/no-go.
- State honest caveats explicitly: static-source + advisory-DB review is **not**
  cryptographic proof the published artifact byte-matches the public repo; advisory DBs
  lag days; behavioral sandboxing shows only what ran in that session; obscure-project
  trust rests on reputation, not a line-by-line review.
- Write the report as a deliverable file. Auditing something you don't own → leave it
  uncommitted.

## Step 6 — recommend a pinned, verified install

Install the exact audited version, locked, with integrity verification:

- Rust: `cargo install <crate> --version <X.Y.Z> --locked`
- npm: pin the exact version, commit the lockfile, `npm ci` (not `install`); add
  `--ignore-scripts` if hooks were the only concern.
- Python: pin `==X.Y.Z` with `--require-hashes`; prefer the audited wheel/sdist.
- Go: rely on `go.sum`; pin the exact version/pseudo-version.
- Binary: install only the checksum/signature-verified artifact from the official origin.

A lockfile / `--locked` / hash pin builds the exact audited set instead of re-resolving to
newer, unaudited transitive versions at install time. Pin to an **immutable digest**
(content hash, git commit SHA, image digest) wherever the ecosystem allows — tags,
branches, and version ranges are mutable and can be re-pointed at malicious code after you
audit.

## High-signal heuristics

- Audit the **default-install closure**, not the whole lockfile — optional features and
  dev-deps shrink the real surface.
- **No networking/egress capability anywhere** is the strongest single anti-telemetry
  signal.
- Install/build-time hooks are the dropper vector — never skip them.
- Acquire-without-executing (vendor / pack / download) lets you read exactly what runs,
  safely.
- Shipped precompiled blob you can't read = red flag → binary-only mode for that file.
- Declaration ≠ call; test/doc/build-probe hit ≠ shipped-code hit — **unless** a build or
  install script reads, extracts, or executes that file. A binary fixture the build
  touches is shipped code (xz-utils hid its backdoor in a `tests/` blob).
- Most real-world compromises are a *trusted* package gone bad in one release — diff the
  artifact against its repo and against the last-trusted version, don't just read the
  code.
- No source ⇒ shift from reading to provenance + sandboxed behavior; signature,
  notarization, and checksum carry the weight.
- Trust-positive signals count too (signed releases, reproducible builds, a tool that
  refuses to silently corrupt data) — note them; they raise confidence.
