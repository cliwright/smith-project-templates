# {{cookiecutter.image_name}}

{{cookiecutter.project_short_description}}

This directory is a Smith project. Bind it to a project type by editing
`type:` in `smith.yml` (see the comments there), then Smith owns the build:
`smith build {{cookiecutter.image_slug}}`.

## Building by hand

{% if cookiecutter.build_tool == "bake" -%}
Parameters live in `docker-bake.hcl` and are built with `docker buildx bake`:

```shell
docker buildx bake                    # build, tagged {{cookiecutter.registry}}/{{cookiecutter.image_name}}:dev
TAG=1.4.2 docker buildx bake          # override the tag (any variable in the file)
docker buildx bake --push             # build and push
```
{%- else -%}
Parameters live in `compose.yaml` with defaults in `.env`, and are built with
`docker compose build`:

```shell
docker compose build                  # build, tagged {{cookiecutter.registry}}/{{cookiecutter.image_name}}:dev
TAG=1.4.2 docker compose build        # override the tag (any variable in the file)
docker compose build --push           # build and push
```
{%- endif %}

## Customizing

- Replace `entrypoint.sh` with your application's startup command (the
  Dockerfile copies it with `--chmod=755`, so it need not be executable in
  git).
- The base image is a build arg (`--build-arg BASE_IMAGE=...`), but the
  user/group creation commands in the Dockerfile match the
  `base_image_family` chosen at scaffold time — switch family there, not just
  the arg.
- New build arguments need two coordinated edits: `ARG <name>` in the
  Dockerfile, and an entry in the parameters file.
