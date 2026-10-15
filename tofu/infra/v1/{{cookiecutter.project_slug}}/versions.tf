terraform {
  required_version = ">= {{ cookiecutter.tofu_version }}"

  required_providers {
{%- if cookiecutter.cloud_provider == "aws" %}
    aws = {
      source  = "hashicorp/aws"
      version = "~> {{ cookiecutter.provider_version }}"
    }
{%- elif cookiecutter.cloud_provider == "gcp" %}
    google = {
      source  = "hashicorp/google"
      version = "~> {{ cookiecutter.provider_version }}"
    }
{%- elif cookiecutter.cloud_provider == "azure" %}
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> {{ cookiecutter.provider_version }}"
    }
{%- endif %}
  }
}

{% if cookiecutter.cloud_provider == "aws" -%}
provider "aws" {
  region = var.region

  default_tags {
    tags = {
      Project     = "{{ cookiecutter.project_slug }}"
      Environment = var.environment
      ManagedBy   = "opentofu"
    }
  }
}
{%- elif cookiecutter.cloud_provider == "gcp" -%}
provider "google" {
  project = var.cloud_project
  region  = var.region
}
{%- elif cookiecutter.cloud_provider == "azure" -%}
provider "azurerm" {
  features {}
}
{%- endif %}
