---
name: gh-admin
description: >-
  GitHub organization administration via OpenTofu — repos, teams, permissions,
  webhooks, and archival through the gh-repo and gh-team modules shipped with
  this skill. TRIGGER when: managing a GitHub org's repos, teams, or permissions
  declaratively; standing up an org's admin repo from nothing; adopting an org
  whose Terraform was written by someone else; or working in a repository named
  "admin". DO NOT TRIGGER for: GitLab group management, application code, or
  cloud-provider infrastructure-as-code.
---

# GitHub Org Admin (OpenTofu)

Manage a GitHub organization declaratively: repos, teams, permissions, archival.
The `gh-repo/` and `gh-team/` modules ship in this skill directory — copy them into
the org's admin repo. They are the shape everything below assumes.

## OpenTofu Only

This project uses **OpenTofu exclusively**. Never use the `terraform` CLI.

If the project still has Terraform artifacts (a `.terraform/` directory, `terraform`
in scripts or docs), migrate first:

1. Install OpenTofu: `brew install opentofu`
2. Run `tofu init` to re-initialize.
3. Replace `terraform` references in scripts, docs, and CI with `tofu`.
4. Verify with `tofu plan` that state is compatible.

## Find the starting rung

The axis is how far the existing `.tf` is from the shape below, not how many repos
it covers.

**No `.tf`** — greenfield. Run the init sequence.

**Someone else's structure** — repos declared as inline `github_repository`
resources, or under foreign modules, or named by another convention. The objects
are already in state; the addresses are wrong. Move them with `tofu state mv` into
`module.repo-<name>`, never re-import — importing on top of managed objects
duplicates them. Do one repo, get a clean plan, then batch the rest.

**Our shape, older keys** — a `gh-repo`/`gh-team` predating the modules here.
Reconcile against `gh-repo/variables.tf`; a missing key is a default nobody wrote
down, not a deliberate choice.

**Nothing in state** — declared but never applied, or state was lost. Import sweep.

**Clean plan** — maintained. Go to Workflow.

One convergence test on every rung: `tofu plan` reports no changes.

## Init sequence (greenfield)

The org must already exist on GitHub with at least one owner. Create the admin repo,
then:

1. Copy `gh-repo/` and `gh-team/` from this skill directory into the repo root.
2. Write `main.tf` (provider config) and `variables.tf` (`github_token`). Set up the
   secret files as **Secrets** describes. Ask the user to put the token value in
   `terraform.tfvars`. Never write the token yourself.
3. **Pin the provider to the current latest.** Check what that is rather than
   copying a number out of any document — `tofu init` reports the version it
   selects. Pin `~>` that minor, and let `.terraform.lock.hcl` freeze the exact
   build. Do the same for `required_version` against the installed `tofu version`.
4. Declare teams in `teams.tf` **before** repos in `repos.tf`. Repo modules consume
   `module.team-<name>.team_id`, so the teams must apply first. A one-member team is
   normal — declare the org's shape, not its current headcount.
5. Run `tofu plan`, then stop until the user explicitly approves the plan. Then run
   `tofu apply`, and commit `.tf`, `.terraform.lock.hcl`, and `terraform.tfstate`
   together.

Latest-at-init applies to **init only**. On any migration rung the existing pin and
lock file govern — never bump a provider major mid-migration, since
`integrations/github` majors carry breaking resource changes.

## Project Layout

```
main.tf              # GitHub provider configuration
repos.tf             # Active repository module declarations
teams.tf             # Team module declarations
archive-repos.tf     # Archived repository declarations (separate file)
variables.tf         # Provider-level variables (e.g. github_token)
terraform.tfvars     # GitHub token (see Secrets)
terraform.tfstate    # State, committed encrypted with git-crypt (see Secrets)
.gitattributes       # git-crypt patterns for the secret files
.gitignore           # .terraform/, terraform.tfstate*.backup
.terraform.lock.hcl  # Provider lock — COMMIT THIS
gh-repo/             # Reusable repository module
gh-team/             # Reusable team module
```

## Secrets

`terraform.tfvars` holds the GitHub token, and `terraform.tfstate` holds secret values
too.

- **`terraform.tfstate`:** commit it, encrypted with git-crypt.
- **`terraform.tfvars`:** whether to commit it depends on the repo. Follow the repo's
  existing practice; in a new repo, ask the user. If it is committed, encrypt it with
  git-crypt. If not, list it in `.gitignore`.
- Pass the token only through `terraform.tfvars`, never through environment variables.

Set up git-crypt when the repo has none: run `git-crypt init`, then add each encrypted
file to `.gitattributes` before its first commit:

```
terraform.tfstate filter=git-crypt diff=git-crypt
terraform.tfvars filter=git-crypt diff=git-crypt
```

Leave out the `terraform.tfvars` line when that file is gitignored. Before every commit
of a secret file, run `git-crypt status` and confirm the file shows as encrypted. If a
secret file was ever committed in plaintext, tell the user: encrypting it now does not
remove the plaintext from history.

If the repo's secret files are encrypted and the checkout is locked, ask the user to
unlock it (`git-crypt unlock`) before running `tofu`.

## Workflow

1. Edit `.tf` files to declare desired state.
2. Run `tofu fmt` to format changed files, then `tofu fmt -check` and `tofu validate`.
3. Run `tofu plan` to preview changes.
4. Stop until the user explicitly approves the plan. Then run `tofu apply`.
5. Commit `.tf` changes AND `terraform.tfstate` together, encrypted as **Secrets**
   describes.

Run every state-mutating command (`tofu import`, `tofu apply`, `tofu state rm`/`mv`) in a
plain foreground shell — backgrounded or wrapped invocations lose the state write. Verify
`terraform.tfstate` actually changed before committing.

## Adding a Repository

Add to `repos.tf` under the appropriate section comment: Main Application, Open Source,
or Supporting. Follow the existing naming and spacing conventions exactly.

```hcl
module "repo-<name>" {
  source = "./gh-repo"
  name   = "<name>"

  admins = [module.team-managers.team_id]
  pushers = [
    module.team-robots.team_id,
    module.team-engineers.team_id,
  ]
}
```

Module instance name: `repo-<name>` (matching the repository name).

### gh-repo Variables

| Variable       | Type        | Default | Notes                                   |
|----------------|-------------|---------|-----------------------------------------|
| `name`         | string      | —       | GitHub repo name                        |
| `description`  | string      | ""      | Repository description                  |
| `public`       | bool        | false   | Set true only for open-source and forks |
| `archived`     | bool        | false   | CAREFUL: cannot unarchive via API       |
| `has_issues`   | bool        | false   | Enable the Issues tab                   |
| `admins`       | set(string) | []      | Team IDs with admin permission          |
| `pushers`      | set(string) | []      | Team IDs with push permission           |
| `pullers`      | set(string) | []      | Team IDs with pull permission           |
| `indv_pullers` | set(string) | []      | Individual usernames, pull access       |
| `indv_pushers` | set(string) | []      | Individual usernames, push access       |

Permission sets take `team_id`, never `slug` — both exist as outputs and mixing them
across call sites produces grants that look declared but don't apply.

### Permission Patterns

Start here and grow from it — this is the smallest team shape that covers most orgs.

- `admins` — `module.team-managers.team_id`.
- `pushers` — `team-robots` + `team-engineers`. Add `team-projects` and `team-ops` on
  repos those teams ship.
- `pullers` — read-only access, rarely needed; mostly infra repos other teams must inspect.
- `indv_*` — individual collaborators. Prefer a team.

When uncertain which teams to assign, match the closest existing repo in `repos.tf`.

## Importing Existing Repos

Import the whole org, not one repo. List first, then import each:

```sh
gh api "orgs/<org>/repos?per_page=100" --jq '.[]|"\(.name)\t\(.private)\t\(.archived)"'
```

Declare a module block per repo, then import each:

```sh
tofu import "module.repo-<name>.github_repository.repo" "<name>"
```

Re-run `tofu plan` until it reports no changes — that convergence, not the import
count, is the signal the sweep is complete.

Collaborators need care:

- List direct grants with `affiliation=direct`
  (`gh api "repos/{org}/{repo}/collaborators?affiliation=direct"`). The unfiltered
  collaborator listing returns team-*effective* roles, so imports capture phantom direct
  grants that duplicate team access.
- Declare only grants a team doesn't already cover; delete redundant direct grants via
  the API (OpenTofu won't remove undeclared collaborators).
- After any team or grant change, verify effective access per user with
  `gh api "repos/{org}/{repo}/collaborators/{user}/permission"`.
- Individual roles above push (`maintain`, direct `admin`) have no module variable —
  demote to team-based access or `indv_pushers`, and flag the cut to the user.

## Adding a Team Member

Edit `teams.tf`. Add the GitHub username string to the `members` set of the target module,
maintaining alphabetical order within the list.

```hcl
module "team-engineers" {
  source  = "./gh-team"
  name    = "Engineers"
  members = [
    "existinguser",
    "newuser",    # <-- add here, alphabetically
  ]
}
```

### gh-team Variables

| Variable      | Type        | Default  | Notes                            |
|---------------|-------------|----------|----------------------------------|
| `name`        | string      | —        | Display name for the GitHub team |
| `description` | string      | ""       | Team description                 |
| `role`        | string      | "member" | Org role: "member" or "admin"    |
| `members`     | set(string) | —        | GitHub usernames                 |

## Deleting a Team

Before destroying a team module, check its `github_membership` instances in state. If
another team module also manages a member's org membership, `tofu state rm` the
duplicates first — destroying them removes the user from the organization, not just the
team. Keep each person's org membership managed by exactly one team module.

## Archiving a Repository

Archival is how repos retire. `gh-repo` carries `prevent_destroy`, so removing a module
block fails the plan instead of destroying the repository and its issues.

1. Move the module block from `repos.tf` to `archive-repos.tf`. Keep the same module
   name — no state migration is needed since the module identity doesn't change.
2. Add `archived = true` to the module arguments.
3. Keep existing permission assignments intact.
4. Verify with `tofu plan` — it should show only `archived` changing to `true`.
5. Warn the user: archiving via the GitHub API is **irreversible**.

Genuinely deleting a repo means removing the `prevent_destroy` block first, as a separate
deliberate edit. If that feels like too much friction, archive instead.

## Webhooks

- Declare package-event hooks at the **org level**, as a single
  `github_organization_webhook`. Org-owned GHCR package events deliver to org-level
  webhooks only, never repo hooks — so a per-repo webhook variable is the wrong shape
  and a fresh publishing repo needs no hook of its own.
- Name the CD system as a per-org fact, in the org's own `main.tf`. It is not a
  `gh-repo` variable.
- GitHub silently throttles delivery — send a lot of events in a short window and the
  next webhook may arrive late. Treat a missing delivery as possibly delayed, not lost,
  before chasing it as a bug.

## Key Rules

- Never modify `gh-repo/` or `gh-team/` module internals for repo-specific needs. Use the
  module variables instead.
- Keep `repos.tf` organized by section: Main Application, Open Source, and
  Supporting.
- Archived repos live in `archive-repos.tf`, never in `repos.tf`.
- Trailing commas on the last list item are preferred (HCL style).
- Commit `.terraform.lock.hcl`. It pins provider checksums and is what makes `tofu init`
  reproducible on another machine.
- `terraform.tfstate` must be committed, encrypted, alongside `.tf` changes — it is the
  source of truth for drift detection.
- Gitignore `terraform.tfstate.backup`; never commit it. If it is already tracked, run
  `git rm --cached terraform.tfstate.backup` and commit the removal with the
  `.gitignore` entry.
- Commit `terraform.tfvars` only encrypted, and only when the repo commits it (Secrets).
- Default repo settings: issues/wiki/projects/discussions disabled, Actions disabled,
  rebase-only merges, branch deletion on merge.
