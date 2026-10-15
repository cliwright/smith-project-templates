# {{ cookiecutter.project_short_description }}
# Created using cookiecutter template on {{ cookiecutter.year }}

# Read-only identity data source: verifies provider authentication on the
# first plan and feeds the example output in outputs.tf.
{%- if cookiecutter.cloud_provider == "aws" %}
data "aws_caller_identity" "current" {}
{%- elif cookiecutter.cloud_provider == "gcp" %}
data "google_client_config" "current" {}
{%- elif cookiecutter.cloud_provider == "azure" %}
data "azurerm_client_config" "current" {}
{%- endif %}

# Add your resources here.
{% if cookiecutter.cloud_provider == "aws" -%}
# Example:
# resource "aws_s3_bucket" "example" {
#   bucket = "${var.environment}-{{ cookiecutter.project_slug }}-example"
# }
{%- endif %}
