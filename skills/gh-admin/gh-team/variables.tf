variable "name" {
  description = "Display name for the GitHub team."
  type        = string
}

variable "description" {
  description = "Team description."
  type        = string
  default     = ""
}

variable "role" {
  description = "Org role for every member of this team: member or admin."
  type        = string
  default     = "member"

  validation {
    condition     = contains(["member", "admin"], var.role)
    error_message = "role must be \"member\" or \"admin\"."
  }
}

variable "members" {
  description = "GitHub usernames, alphabetical."
  type        = set(string)
}
