# Backend settings live in environments/<env>.backend.tfvars (backend blocks
# cannot reference variables); pass them to tofu init:
#   tofu init -backend-config=environments/dev.backend.tfvars
terraform {
{%- if cookiecutter.cloud_provider == "aws" %}
  backend "s3" {}
{%- elif cookiecutter.cloud_provider == "gcp" %}
  backend "gcs" {}
{%- elif cookiecutter.cloud_provider == "azure" %}
  backend "azurerm" {}
{%- endif %}
}
