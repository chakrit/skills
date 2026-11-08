output "team_id" {
  description = "Numeric team ID. This is what gh-repo permission sets take."
  value       = github_team.team.id
}

output "slug" {
  description = "URL slug for the team."
  value       = github_team.team.slug
}
