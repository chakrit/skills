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
file:line (or observed-behavior) evidence.

## Operations

- **Static audit:** map, acquire and inspect artifacts with Steps 0–5; recommend in Step 6.
- **Behavioral audit:** add Step B.4 only when execution is authorized and isolated.

During static phases, never invoke the target's hooks, build backends, entry points,
or repository-selected helpers. Use trusted, already-installed inspection tools with
controlled per-run configuration. Do not change global settings or install audit tools.
Keep downloads, extraction, caches and reports in designated scratch storage; do not
modify the target checkout or install the target. Inspection tools still parse hostile
input: use an isolated environment and do not claim that parsing is risk-free.

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

Settle depth and acquisition path before acquisition. Reuse existing authorization for
this run. If a later step requires new authority or cannot meet its safety prerequisites,
stop that branch and report the limitation; ask only when the user's decision is needed.

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
- Binary-only (precompiled download, no readable source) → Step 2, then Step B and 5–6;
  behavioral execution is conditional on Step B.4's prerequisites.
- Mixed (a source package shipping a precompiled blob) → both: audit the source you have
  AND route every unreadable blob through Step B.

Run only the steps the chosen depth and path call for. Record whether authorization
covers behavioral execution; depth alone does not authorize running the target.

## Step 1 — map the surface without executing

- Read the **manifest**: direct deps, and which are default vs optional. Per ecosystem:
  `Cargo.toml` · `package.json` (deps + `scripts`) · `pyproject.toml`/`setup.py` ·
  `go.mod` · `Gemfile`/`.gemspec` · Homebrew `Formula`. Note any `exclude`/`files` list
  (what is stripped from or shipped in the published artifact).
- Read the **lockfile** for the full transitive set + exact versions: `Cargo.lock` ·
  `package-lock.json`/`pnpm-lock.yaml` · `requirements.txt`/`poetry.lock` · `go.sum` ·
  `Gemfile.lock`. `go.sum` records checksums, not the selected dependency graph; read
  `go.mod` and applicable workspace inputs to establish Go module selection.
- Determine what actually ships/runs on a **default** install vs feature-gated, optional,
  or dev-only. Dev-deps and non-default features usually don't ship — this shrinks the
  real attack surface sharply. Audit the default-install closure first.
- **Highest-signal single check:** grep for any networking/egress capability. None present
  ⇒ no socket/HTTP stack to phone home with; absence is strong evidence against
  telemetry/exfil. Markers per ecosystem: Rust `reqwest`/`hyper`/`tokio`/`ureq`/`curl`/
  `rustls` · npm `http`/`https`/`net`/`dns`/`axios`/`node-fetch`/`got` · Python
  `requests`/`urllib`/`httpx`/`socket`/`aiohttp` · Go `net/http`/`net`. Presence isn't
  guilt — it means look closer.

## Step 2 — acquire artifacts without invoking target code

**2.1. Identify the input.** Distinguish a published registry artifact, repository source,
local directory, or binary download. Record the exact package name, version, platform,
origin URL, expected digest and resolved commit where applicable. Preserve private
registry selection; never substitute a public package with the same name.

**2.2. Download or copy as data.** Run acquisition from an isolated scratch workspace,
with trusted configuration and tools. Do not inherit target-controlled configuration,
plugins, toolchain selectors, credential helpers or executable hooks. If those conditions
cannot be established, use direct artifact downloads or report acquisition incomplete.
Apply 2.3's extraction boundary to every tool below that unpacks during acquisition;
if the tool cannot enforce it, download the archive directly for constrained extraction.

- **Python registry:** fetch version-specific metadata, such as
  `https://pypi.org/pypi/<pkg>/<version>/json`, or the selected private registry's
  equivalent. Download the intended wheel or sdist URL directly and verify its SHA-256
  against the metadata. Do not use `pip download` for source acquisition: metadata
  generation can invoke build hooks, even with `--no-deps --no-binary :all:`.
  See [PyPI metadata](https://docs.pypi.org/api/json/) and
  [pip build hooks](https://pip.pypa.io/en/stable/reference/build-system/).
- **npm registry:** fetch the exact version's tarball URL and integrity metadata from
  the selected registry, then download and verify the tarball directly. For local
  directories, inspect files as data; for Git inputs, use the repository branch below.
  Do not use packing or installation to acquire these inputs. `npm pack` can run
  lifecycle hooks; `--dry-run` is not a general script-suppression guarantee.
  See [npm lifecycle scripts](https://docs.npmjs.com/cli/v11/using-npm/scripts/).
- **Rust:** acquire the target's published `.crate` separately. For dependency sources,
  use `cargo vendor --locked <fresh-destination>` from a controlled scratch copy with
  an existing lockfile and trusted installed toolchain. Vendoring does not run
  `build.rs`; it does not acquire the target artifact or prove complete build coverage.
  Do not apply the printed configuration. If the lockfile is missing or would change,
  report unresolved versions rather than silently resolving a different audit set.
  See [cargo vendor](https://doc.rust-lang.org/cargo/commands/cargo-vendor.html).
- **Go:** use `GOTOOLCHAIN=local go mod download <module>@<version>` with controlled
  configuration and scratch caches. Do not build or generate code. If the installed
  toolchain is incompatible, report the missing prerequisite instead of switching or
  downloading toolchains. Enumerate dependencies from the selected module graph;
  downloading one module does not establish complete coverage.
  See [Go toolchains](https://go.dev/doc/toolchain) and
  [module downloads](https://go.dev/ref/mod#go-mod-download).
- **Ruby:** use `gem fetch <gem> --version <version> --platform <platform>` with trusted
  RubyGems configuration, then `gem unpack <downloaded-file.gem>` in scratch storage.
  Read `.gemspec` files as text; do not evaluate them or build/install the gem.
  See [RubyGems commands](https://guides.rubygems.org/command-reference/).
- **Repository:** acquire the resolved commit without checkout, using
  `git clone --no-checkout` with controlled Git configuration, transport and templates.
  Inspect raw tree objects without filters, text conversion or external diff helpers;
  do not initialize submodules or invoke repository tooling. Record missing submodule
  and large-file contents. Verify claimed tag signatures and record the resolved commit.
  Checkout can invoke locally configured filters selected by repository attributes.
  See [Git clone](https://git-scm.com/docs/git-clone) and
  [Git attributes](https://git-scm.com/docs/gitattributes).
- **Local source:** inspect without running packaging commands or evaluating manifests.
  Record its identity and changes; do not describe it as the published artifact.
- **Binary or container:** download the exact artifact or image manifest and layers by
  digest without launching, installing or building them; continue through Step B.

**2.3. Verify and extract within bounds.** Stop using an artifact on digest mismatch.
A registry digest proves agreement with registry metadata, not trustworthiness or
equivalence to the source repository. List archive members before extraction; use a
trusted extractor that confines writes to a fresh isolated destination. Reject escaping
paths, unsafe links and special files. Bound expanded size and file count within existing
resource limits. Do not weaken extraction filters when an archive is rejected.
See [archive extraction guidance](https://docs.python.org/3/library/tarfile.html#extraction-filters).

**2.4. Record coverage.** List acquired artifacts and missing dependencies, including
build requirements. If metadata requires executing a backend, leave it unresolved in
the static phase. Report unavailable artifacts, dynamic requirements and incompatible
tools as coverage gaps; do not claim an exact install closure from a partial download.

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
5. **Repo aux tooling.** Audit `xtask/`, `scripts/`, `Dockerfile`, CI. Inspect the acquired
   archive's actual members to establish what ships, then trace whether install/build
   hooks consume those files. Do not repack or build to discover archive contents.
   `cargo package --list` under Step 2's tool/configuration constraints can supplement
   the inventory; it predicts local package contents, not published contents. Plain
   `cargo package` normally performs a verification build. CI configuration alone does
   not establish execution on the user's machine.
   See [Cargo packaging modes](https://doc.rust-lang.org/cargo/commands/cargo-package.html).
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
   symbol/import tables (`nm` / `otool -L` / `objdump -p` / `readelf -d`) for network,
   crypto, and process APIs; macOS entitlements (`codesign -d --entitlements -`). Never
   use `ldd` on an untrusted executable: it can execute code. ELF dependency declarations
   do not expose the complete dependency tree or every runtime-loaded library.
   See the [ldd security warning](https://www.man7.org/linux/man-pages/man1/ldd.1.html).
   Inspect acquired container layers as data using existing trusted tools; image history
   is supplemental metadata, not proof of file contents or behavior. Do not build or
   run an image for static inspection.
4. **Behavioral, sandboxed — last, never first.** Require authorization covering target
   execution and a disposable environment with no real credentials, host mounts,
   privileged access or host container socket. Establish isolation, resource limits and
   network policy before execution; default to blocked egress and authorize any required
   destinations. If authority is missing, ask and wait before execution. If adequate
   isolation is unavailable, skip execution and report incomplete behavioral evidence.
   Never substitute a host run. In the authorized environment, monitor network
   (`tcpdump` or equivalent), syscalls (`dtruss`/`strace`/`dtrace`), filesystem and
   persistence writes. Compare observed egress
   against what the tool legitimately needs. A clean session is not a clean bill —
   payloads gate on date/time, geo/IP, hostname, or env, or sleep before acting (the
   @solana/web3.js backdoor fired only in a ~5-hour window; SUNBURST lay dormant ~2
   weeks). Read the source for trigger conditions too; never rely on the sandbox alone.

## Step 5 — synthesize

- Roll the lane verdicts into one scoped recommendation. If missing artifacts or required
  checks prevent a supported go/no-go, report insufficient evidence and name the gap.
- State honest caveats explicitly: static-source + advisory-DB review is **not**
  cryptographic proof the published artifact byte-matches the public repo; advisory DBs
  lag days; behavioral sandboxing shows only what ran in that session; obscure-project
  trust rests on reputation, not a line-by-line review.
- Write the report as a deliverable file. Auditing something you don't own → leave it
  uncommitted.

## Step 6 — recommend a pinned, verified install

Recommend the exact audited artifact and version, with integrity verification. Do not
install it or modify a project from an audit request. Installation requires separate
authority; reuse it if already granted for this exact action. With insufficient evidence,
state the prerequisites instead of recommending installation.

- Rust: `cargo install <crate> --version <X.Y.Z> --locked`
- npm: pin the exact version, commit the lockfile, `npm ci` (not `install`); add
  `--ignore-scripts` if hooks were the only concern.
- Python: pin `==X.Y.Z` with `--require-hashes`; prefer the audited wheel/sdist.
- Go: rely on `go.sum`; pin the exact version/pseudo-version.
- Binary: install only the checksum/signature-verified artifact from the official origin.

A lockfile or hash pin constrains dependency selection; it does not constrain arbitrary
downloads made by build hooks. Include required build dependencies in the audited set
and report any unresolved inputs. Pin to an **immutable digest**
(content hash, git commit SHA, image digest) wherever the ecosystem allows — tags,
branches, and version ranges are mutable and can be re-pointed at malicious code after you
audit.

## High-signal heuristics

- Audit the **default-install closure**, not the whole lockfile — optional features and
  dev-deps shrink the real surface.
- **No networking/egress capability anywhere** is the strongest single anti-telemetry
  signal.
- Install/build-time hooks are the dropper vector — never skip them.
- Acquire artifacts as data under Step 2's input and configuration constraints; command
  names such as vendor, pack or download do not establish safety or complete coverage.
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

## Completion evidence

Deliver a report containing artifact identities and digests, selected depth, acquired
and missing dependencies, checks performed, file:line findings, and scoped verdict.
Record whether target code ran, its authorization and isolation when applicable, and
behavioral checks skipped. Distinguish registry integrity, source comparison and observed
behavior. An unresolved prerequisite completes an assessment with an explicit limitation;
it does not permit executing the target or claiming a complete audit. End with a pinned
recommendation only when the evidence supports one.
