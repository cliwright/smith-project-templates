variable "region" {
  description = "Primary region (AWS/GCP) or location (Azure) for resources"
  type        = string
  default     = "{{ cookiecutter.region }}"
}

variable "cloud_project" {
  description = "Cloud project ID (GCP) or subscription scope; required for GCP, unused by AWS and Azure"
  type        = string
  default     = ""
{%- if cookiecutter.cloud_provider == "gcp" %}

  validation {
    condition     = var.cloud_project != ""
    error_message = "cloud_project (GCP project ID) must be set."
  }
{%- endif %}
}

variable "environment" {
  description = "Deployment environment; one of: {{ cookiecutter.environments }}"
  type        = string
  validation {
    condition     = contains([{% for e in cookiecutter.environments.split(",") %}"{{ e.strip() }}"{% if not loop.last %}, {% endif %}{% endfor %}], var.environment)
    error_message = "Environment must be one of: {{ cookiecutter.environments }}."
  }
}

# Add your custom variables here
# Example:
# variable "instance_type" {
#   description = "The instance type to use"
#   type        = string
#   default     = "t3.micro"
# }
