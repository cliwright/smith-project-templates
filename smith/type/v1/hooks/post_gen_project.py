"""Validate the rendered type tree before the scaffold counts as done.

Runs inside the generated project directory (the rendered type_dir).
Enforces the segment patterns the smith schemas require so a bad prompt
answer fails the scaffold loudly instead of leaving an unsmeltable tree
behind, and verifies the rendered project-type.json parses as JSON (the
smith-side post-check does the full schema + registry-layout validation).
"""
import json
import re
import sys

SEGMENT = re.compile(r"^[a-z][a-z0-9-]*$")


def main() -> int:
    segments = [
        ("language", "{{ cookiecutter.language }}"),
        ("flavor", "{{ cookiecutter.flavor }}"),
        ("kind", "{{ cookiecutter.kind }}"),
    ]
    version = "{{ cookiecutter.type_version }}"
    errors = []
    for label, value in segments:
        if not SEGMENT.match(value):
            errors.append("%s segment %r must match %s" % (label, value, SEGMENT.pattern))
    if not re.match(r"^[0-9]+$", version):
        errors.append("type_version %r must be digits only (the directory is v<N>)" % version)
    try:
        with open("project-type.json", encoding="utf-8") as fh:
            doc = json.load(fh)
    except (OSError, ValueError) as exc:
        errors.append("project-type.json does not parse as JSON: %s" % exc)
    else:
        if doc.get("name") != "{{ cookiecutter.type_name }}":
            errors.append('project-type.json "name" does not match the type directory')
        if doc.get("version") != int(version or 0):
            errors.append('project-type.json "version" does not match the v<N> directory')
    if errors:
        for error in errors:
            print("smith/type scaffold: %s" % error, file=sys.stderr)
        return 1
    print("Rendered {{ cookiecutter.type_name }}@{{ cookiecutter.type_version }} at {{ cookiecutter.type_dir }}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
