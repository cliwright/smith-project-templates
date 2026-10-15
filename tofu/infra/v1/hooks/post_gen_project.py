"""Generate per-environment tfvars and backend-tfvars files.

The set of environments is a prompt answer, so the environments/ files are
generated here rather than shipped statically: one "<env>.tfvars" and one
"<env>.backend.tfvars" per comma-separated entry. Backend fields match the
cloud provider chosen at scaffold time (backend blocks cannot reference
variables, so backend settings live in these files and are passed to
`tofu init -backend-config=environments/<env>.backend.tfvars`).
"""
import os
import sys

SLUG = "{{ cookiecutter.project_slug }}"
PROVIDER = "{{ cookiecutter.cloud_provider }}"
REGION = "{{ cookiecutter.region }}"
ENVIRONMENTS = [e.strip() for e in "{{ cookiecutter.environments }}".split(",") if e.strip()]


def tfvars(env):
    lines = ['environment = "%s"' % env]
    if PROVIDER == "gcp":
        lines.extend(["", "# GCP project ID", 'cloud_project = ""'])
    lines.append("")
    lines.append("# Add environment-specific variables here")
    return "\n".join(lines) + "\n"


def backend_tfvars(env):
    state_key = "%s/%s/terraform.tfstate" % (SLUG, env)
    if PROVIDER == "aws":
        lines = [
            "# The state bucket must exist before the first `tofu init` (create it",
            "# by hand or with a small bootstrap stack).",
            'bucket  = ""',
            'key     = "%s"' % state_key,
            'region  = "%s"' % REGION,
            "encrypt = true",
        ]
    elif PROVIDER == "gcp":
        lines = [
            "# The GCS state bucket must exist before the first `tofu init`.",
            'bucket = ""',
            'prefix = "%s/%s"' % (SLUG, env),
        ]
    else:
        lines = [
            "# The resource group and storage account must exist before the first",
            "# `tofu init`; the storage account name must be globally unique.",
            'resource_group_name  = "%s-tfstate"' % SLUG,
            'storage_account_name = "%s"' % ((SLUG.replace("-", "") + "tfstate")[:24]),
            'container_name       = "tfstate"',
            'key                  = "%s"' % state_key,
        ]
    return "\n".join(lines) + "\n"


def main() -> int:
    if not ENVIRONMENTS:
        print("tofu/infra scaffold: environments list is empty", file=sys.stderr)
        return 1
    os.makedirs("environments", exist_ok=True)
    written = []
    for env in ENVIRONMENTS:
        for name, content in (
            ("%s.tfvars" % env, tfvars(env)),
            ("%s.backend.tfvars" % env, backend_tfvars(env)),
        ):
            path = os.path.join("environments", name)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(content)
            written.append(path)
    print("Generated %d environment file(s) for provider %s: %s" % (len(written), PROVIDER, ", ".join(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
