#!/bin/sh
# Placeholder entrypoint for {{cookiecutter.image_name}}.
# Replace this with your application's real startup command.
set -eu

echo "{{cookiecutter.image_name}}: {{cookiecutter.project_short_description}}"
echo "No application yet — replace entrypoint.sh with your real startup."

if [ "$#" -gt 0 ]; then
    exec "$@"
fi
