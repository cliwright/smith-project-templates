# Output values for {{ cookiecutter.project_short_description }}

# Identity output from the read-only data source in main.tf — confirms which
# account/project/subscription OpenTofu is authenticated against.
{%- if cookiecutter.cloud_provider == "aws" %}
output "aws_account_id" {
  description = "AWS account ID OpenTofu is authenticated against"
  value       = data.aws_caller_identity.current.account_id
}
{%- elif cookiecutter.cloud_provider == "gcp" %}
output "gcp_project_id" {
  description = "GCP project OpenTofu is authenticated against"
  value       = data.google_client_config.current.project
}
{%- elif cookiecutter.cloud_provider == "azure" %}
output "azure_subscription_id" {
  description = "Azure subscription OpenTofu is authenticated against"
  value       = data.azurerm_client_config.current.subscription_id
}
{%- endif %}
