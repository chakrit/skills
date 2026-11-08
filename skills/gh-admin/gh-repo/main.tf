terraform {
  required_providers {
    github = {
      source = "integrations/github"
    }
  }
}

resource "github_repository" "repo" {
  name        = var.name
  description = var.description
  visibility  = var.public ? "public" : "private"
  archived    = var.archived

  is_template                 = false
  archive_on_destroy          = true
  web_commit_signoff_required = false # not enforced yet

  has_issues      = var.has_issues
  has_discussions = false
  has_projects    = false
  has_wiki        = false

  # Rebase-only. Merge commits and squash stay off.
  allow_merge_commit     = false
  allow_squash_merge     = false
  allow_rebase_merge     = true
  allow_auto_merge       = true
  delete_branch_on_merge = true

  lifecycle {
    # Deleting a module block must not destroy the repo, its issues, or its
    # history. Retire repos via `archived = true`, never by removing the block.
    # A genuine deletion means removing this block first, deliberately.
    prevent_destroy = true

    # GitHub reverts allow_auto_merge on its own every so often.
    ignore_changes = [allow_auto_merge]
  }
}

resource "github_actions_repository_permissions" "actions" {
  enabled    = false
  repository = github_repository.repo.name
}

resource "github_team_repository" "admins" {
  for_each   = var.admins
  repository = github_repository.repo.name
  team_id    = each.value
  permission = "admin"
}

resource "github_team_repository" "pushers" {
  for_each   = var.pushers
  repository = github_repository.repo.name
  team_id    = each.value
  permission = "push"
}

resource "github_team_repository" "pullers" {
  for_each   = var.pullers
  repository = github_repository.repo.name
  team_id    = each.value
  permission = "pull"
}

resource "github_repository_collaborator" "indv_pushers" {
  for_each   = var.indv_pushers
  repository = github_repository.repo.name
  permission = "push"
  username   = each.value
}

resource "github_repository_collaborator" "indv_pullers" {
  for_each   = var.indv_pullers
  repository = github_repository.repo.name
  permission = "pull"
  username   = each.value
}
