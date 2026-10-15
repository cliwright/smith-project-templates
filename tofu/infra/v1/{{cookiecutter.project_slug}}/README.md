# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Description

This smith OpenTofu project manages infrastructure for {{ cookiecutter.project_name }} on **{{ cookiecutter.cloud_provider | upper }}**.

## Prerequisites

- [OpenTofu](https://opentofu.org/) {{ cookiecutter.tofu_version }}+
{%- if cookiecutter.cloud_provider == "aws" %}
- AWS credentials — `aws configure`, or `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_SESSION_TOKEN` in the environment
{%- elif cookiecutter.cloud_provider == "gcp" %}
- [gcloud](https://cloud.google.com/sdk) with application-default credentials: `gcloud auth application-default login`
- A GCP project ID — set `cloud_project` in the environment tfvars
{%- elif cookiecutter.cloud_provider == "azure" %}
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/) — `az login`; the default subscription is used unless `ARM_SUBSCRIPTION_ID` is set
{%- endif %}

## State backend

State is stored in {%- if cookiecutter.cloud_provider == "aws" %} an S3 bucket. The bucket must exist before the first `tofu init` — create it by hand or with a small bootstrap stack. Fill the empty `bucket` in `environments/<env>.backend.tfvars`.
{%- elif cookiecutter.cloud_provider == "gcp" %} a GCS bucket, namespaced per environment via `prefix`. The bucket must exist before the first `tofu init`. Fill the empty `bucket` in `environments/<env>.backend.tfvars`.
{%- elif cookiecutter.cloud_provider == "azure" %} an Azure storage account. The resource group and storage account must exist before the first `tofu init`; the storage account name is globally unique (generated from the project slug — adjust if it is taken).
{%- endif %}

## Layout

- `versions.tf` — OpenTofu + provider pin, provider configuration
- `backend.tf` — empty `{{ {'aws': 's3', 'gcp': 'gcs', 'azure': 'azurerm'}[cookiecutter.cloud_provider] }}` backend block; settings come from `environments/<env>.backend.tfvars` (backend blocks cannot reference variables)
- `variables.tf` — `region`, `cloud_project`, `environment`
- `main.tf` / `outputs.tf` — read-only identity data source + output to verify authentication
- `environments/` — one `<env>.tfvars` + `<env>.backend.tfvars` pair per environment, generated at scaffold time

## Usage

```shell
tofu init -backend-config=environments/dev.backend.tfvars
tofu plan -var-file=environments/dev.tfvars
```

## Smith

This project ships a placeholder `smith.yml` (`type: missing/absent`). Bind it
by hand once your organization publishes tofu types — the intended ref is
`tofu/{{ cookiecutter.cloud_provider }}/infra@1` — then run `smith sync`.
