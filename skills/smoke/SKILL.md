---
name: smoke
description: >-
  Golden-file / snapshot smoke testing of shell-command output with the SMOKE CLI.
  Capture a command's observable output once, lock it into a *.lock.yml, and let later
  runs go UNCHANGED when output matches or CHANGED when it drifts. TRIGGER when: setting
  up snapshot or golden-file testing for a CLI tool or shell command, capturing command
  output as a baseline/golden, detecting output drift across runs, writing or editing a
  tests.yml / *.cue smoke spec, or interpreting SMOKE's UNCHANGED / CHANGED / NEW verdicts
  and 0 / 1 / 2 / 3 / 64 / 65 exit codes. Critical framing other tools get wrong: SMOKE
  detects DRIFT, not correctness — CHANGED is the expected "eyeball and re-commit" state,
  NOT a failing test; UNCHANGED means drift-free, NOT verified-correct. An agent must never
  chase output back to green or auto-commit a CHANGED result it did not read. DO NOT TRIGGER
  for assertion-based unit/integration frameworks (go test, pytest, jest), or test work that
  is not snapshot/golden-file based.
---

# SMOKE — golden-file smoke testing

SMOKE captures a command's observable output once and flags when it later drifts. It is a
**drift detector, not an assertion engine**: it answers *"does the output still match the
committed golden?"*, never *"is the behavior correct?"*. Treat it as `diff` against a
locked baseline, not as a pass/fail test runner.

Not a replacement for real tests — a fast drift tripwire for CLI output.

## Setup

Scaffold a spec, then fill it in:

```sh
smoke --init           # writes tests.yml (or: smoke --init=mytests.yml)
```

A spec is a tree of tests. The YAML root *is* the root test; `tests:` nests arbitrarily,
and subtests inherit the parent's `config`, `checks`, and `commands`.

```yaml
config:
  interpreter: /bin/sh   # commands are piped to `interpreter -s` via stdin
  timeout: 5s
checks:                  # what to observe and lock per command
  - exitcode
  - stdout
  - stderr
  - generated/*.go       # text file globs are also checks — locks file contents
                         #   (globs resolve relative to the test's workdir)
tests:
  - name: Greeting
    commands:
      - echo hello world
```

`.cue`, `.json`, `.jsonc`, and `.jsonl` specs work too; `.cue` gets schema validation
(typo'd fields fail closed). Lock files are `<spec>.lock.yml` (a `.yaml` spec locks to
`.lock.yaml`).

## Binary artifacts

SMOKE compares the **text lines** recorded in a lock. File-glob checks are suitable for
text-like files; do not use them to golden an opaque binary directly. Instead, make the
artifact's meaningful, deterministic projection a command that writes to `stdout`, and
snapshot it with `checks: [exitcode, stdout]`. Put the required projection tool in CI too.

Choose the projection for the property you need to watch:

| Artifact / question | Project to stdout | Detects / deliberately ignores |
| --- | --- | --- |
| PDF: did the readable document change? | `pdftotext -layout report.pdf -` | Text and coarse layout; not rendering or embedded-object bytes. |
| Image: did the pixels change, ignoring metadata? | normalized RGBA bytes plus dimensions, then a hash | Pixel/dimension drift; metadata and the original encoder's byte layout. |
| Image: need a reviewable pixel diff? | ImageMagick `txt:-` after normalization | Pixel values; can be very large. |
| Arbitrary binary: did these bytes change? | `xxd -g 1` or `od -An -v -tx1` | Exact selected bytes. |
| Archive: did its inventory change? | `tar -tvf` or `unzip -l` | Member names/sizes; not member payloads. |
| Office document: did the authored text change? | convert/extract text from DOCX/XLSX/PPTX | Semantic content chosen by the extractor, not ZIP-container bytes. |
| SQLite: did the logical database change? | `sqlite3 app.db '.dump'` | Schema/data dump; avoid volatile tables or values first. |
| Audio/video: did stream metadata change? | selected `ffprobe` output | Codec/stream metadata; not a perceptual media comparison. |
| Executable/object: did the ABI surface change? | `readelf`, `otool`, or `nm` with stable options | Selected headers/symbols; not nondeterministic build bytes. |

Examples:

```yaml
checks: [exitcode, stdout]
commands:
  # PDF text, rather than the volatile PDF container.
  - pdftotext -layout report.pdf -

  # First 256 bytes, or the byte interval [0x100, 0x1100), as readable hex.
  - xxd -g 1 -l 256 firmware.bin
  - xxd -g 1 -s 0x100 -l 4096 firmware.bin

  # Equivalent portable-style hex range where `od` is available.
  - LC_ALL=C od -An -v -tx1 -j 256 -N 4096 firmware.bin

  # Pixel semantic snapshot: metadata stripped, dimensions preserved, pixels hashed.
  - 'magick image.png -strip -format "%w %h\n" info:'
  - magick image.png -strip -depth 8 rgba:- | shasum -a 256

  # Archive inventory or a logical database dump.
  - unzip -l release.zip
  - sqlite3 app.db '.dump'
```

Use a byte range only when the format layout is known: PNG metadata can move between
chunks, so fixed offsets are brittle. For images where metadata should not matter, prefer
the normalized pixel projection above. A hash tells you that something changed but not
what; use a textual pixel dump when the review needs the latter. `base64 artifact.bin` is
a lossless last resort, but it produces large locks and poor diffs; prefer a semantic
projection or hex range whenever possible.

## The loop: run → eyeball → commit

This three-step cadence is the whole workflow. The eyeball step is load-bearing — skipping
it defeats the tool.

1. **Run** — `smoke tests.yml`. First run reports `NEW` (no lock yet).
2. **Eyeball** — read the output. Is it what the command *should* produce?
3. **Commit** — if correct, `smoke -c tests.yml` writes the `.lock.yml` golden.

Check the `.lock.yml` into source control so teammates and CI compare against the same
baseline.

On later runs: `UNCHANGED` (exit 0) means output matched. When you change behavior that
*should* move output, you get `CHANGED` (exit 1) — eyeball the diff, then `smoke -c` to
re-bless the golden. Re-running the run→eyeball→commit loop on an intended change is
correct, not a workaround.

## Exit codes

Branch on the exit code — never parse the human text or colors. Full contract:
[`docs/spec/exit-codes.md`](https://github.com/chakrit/smoke/blob/main/docs/spec/exit-codes.md).

| Code | State       | Meaning                                                        |
| ---- | ----------- | -------------------------------------------------------------- |
| 0    | `UNCHANGED` | Output matched the lock. *Not* "tests passed."                 |
| 1    | `CHANGED`   | Drift — output moved (includes `MISSING`, timeout). Review it. |
| 2    | —           | Operational error: SMOKE itself broke (runner crash, I/O).     |
| 3    | `NEW`       | No lock yet; first run is unreviewed.                          |
| 64   | —           | Usage error: bad flags or argv.                                |
| 65   | —           | Data error: a spec or lock file is malformed.                  |

`0` is the only clean pass for a CI gate; "fail on any nonzero" works. `2` /`64`/`65` mean
*stop* — none is drift.

## The three traps (the framing every test-trained consumer gets wrong)

Full guidance: [`docs/guides/using-smoke-in-tdd.md`](https://github.com/chakrit/smoke/blob/main/docs/guides/using-smoke-in-tdd.md).

- **`CHANGED` is not a failing test.** Exit 1 during an intentional change is *expected* —
  eyeball, then re-commit. Never pattern-match it as a red test and edit code to chase the
  output back to `UNCHANGED`. Re-commit; don't revert.
- **`UNCHANGED` is not "correct".** Exit 0 means the output didn't move, not that the
  behavior is right — the change may be in an unobserved surface, or the golden may have
  locked in a bug. Treat it as "no drift to review," never as verification.
- **Re-committing can hide a regression.** `smoke -c` is right only when you *intended*
  the change and read the new output. Auto-committing every `CHANGED` blesses regressions
  as the new golden — that turns SMOKE off.

## For an agent driving SMOKE

- Branch on `$?`, not output text. `0` = no drift (continue, not a verification pass); `1`
  = drift (surface the diff, re-commit only if intended and checked); `3` = first run
  (review, commit the initial lock); `2` /`64`/`65` = stop.
- Use `--json` (compare mode only) for a machine-readable mirror: top-level `status`
  (`unchanged`/`changed`/`new`) + `exitCode`, plus a per-node `matched`
  /`changed`/`missing` tree. It is the only thing on stdout at default verbosity.
- The mode flags — `--init`, `--list`, `--print`, `--commit`, `--show-expected` — each
  select the run's one action and are mutually exclusive; `--json` pairs only with the
  default compare mode. Any conflicting combination is rejected up front with exit `64`,
  before any work runs.
- Coloring auto-disables when stdout isn't a terminal, so piped/captured output is already
  plain; `--no-color` forces it off even on a TTY. Never rely on color either way — branch
  on `$?`.
- Never auto-chase green. A drift you did not cause is a signal to surface, not to fix.
