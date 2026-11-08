output "name" {
  description = "Repository name as created."
  value       = github_repository.repo.name
}

output "full_name" {
  description = "Repository name qualified with its owner, e.g. acme/site-web."
  value       = github_repository.repo.full_name
}
