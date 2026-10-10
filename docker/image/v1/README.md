# Docker Image Template

Scaffolds a minimal, non-root, OCI-labeled Docker image project with a Smith
manifest. One template covers both build-tool flavors — the choice is made at
scaffold time and baked into the project:

- **bake** — parameters in `docker-bake.hcl`, built by `docker buildx bake`;
  pairs with type `docker/bake/image@v1`
- **compose** — parameters in `compose.yaml` (defaults in `.env`), built by
  `docker compose build`; pairs with type `docker/compose/image@v1`

The unselected flavor's files are removed by `hooks/post_gen_project.py`, so
the project ships exactly one parameters file — the one its type drives.

Variation lives inside the template, not in the template path taxonomy:
`smith new docker/image` is always the command, and cookiecutter choices (+
the hook) do the branching.

```shell
smith new docker/image --version 1
```

```
docker/image/v1
├── cookiecutter.json
├── hooks/post_gen_project.py
└── {{cookiecutter.image_name}}/
    ├── Dockerfile
    ├── docker-bake.hcl        (bake flavor; removed by hook for compose)
    ├── compose.yaml           (compose flavor; removed by hook for bake)
    ├── dot_env                (compose flavor; renamed to .env by the hook)
    ├── .dockerignore
    ├── .gitignore
    ├── entrypoint.sh
    ├── smith.yml              (placeholder type — bind it by hand)
    └── README.md
```
