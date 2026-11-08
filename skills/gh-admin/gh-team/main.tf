terraform {
  required_providers {
    github = {
      source = "integrations/github"
    }
  }
}

resource "github_team" "team" {
  name        = var.name
  description = var.description
  privacy     = "secret"
}

# Org membership. Each person's org membership must be managed by exactly one
# team module — destroying a duplicate removes them from the organization, not
# just the team.
resource "github_membership" "memberships" {
  for_each = var.members
  username = each.value
  role     = var.role
}

resource "github_team_membership" "team-memberships" {
  for_each = var.members
  team_id  = github_team.team.id
  username = each.value
  role     = var.role == "member" ? "member" : "maintainer"
}
