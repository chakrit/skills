variable "name" {
  description = "GitHub repository name."
  type        = string
}

variable "description" {
  description = "Repository description."
  type        = string
  default     = ""
}

variable "public" {
  description = "Public repository. Set true only for open-source repos and forks."
  type        = bool
  default     = false
}

variable "archived" {
  description = "CAREFUL! Archiving cannot be undone via the GitHub API."
  type        = bool
  default     = false
}

variable "has_issues" {
  description = "Enable the Issues tab."
  type        = bool
  default     = false
}

variable "admins" {
  description = "Team IDs granted admin permission."
  type        = set(string)
  default     = []
}

variable "pushers" {
  description = "Team IDs granted push permission."
  type        = set(string)
  default     = []
}

variable "pullers" {
  description = "Team IDs granted pull permission."
  type        = set(string)
  default     = []
}

variable "indv_pushers" {
  description = "Individual GitHub usernames granted push. Prefer team access."
  type        = set(string)
  default     = []
}

variable "indv_pullers" {
  description = "Individual GitHub usernames granted pull. Prefer team access."
  type        = set(string)
  default     = []
}
