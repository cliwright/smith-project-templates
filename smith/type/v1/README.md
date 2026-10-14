# smith/type — project-type scaffold

Scaffolds a Smith **project type** source tree, ready to be smelt into an
ingot and published in a type registry. Invoked via:

```sh
smith new smith/type --version 1
```

The rendered tree is `<language>/<flavor>/<kind>/v<N>/project-type.json` —
the registry layout, with `name` and `version` in the file agreeing with the
path. `smith new` validates the result against the project-type schema and
the registry invariant after scaffolding and prints the `smith smelt --path`
command to pack it.

## Prompts

| prompt          | meaning                                                              |
|-----------------|----------------------------------------------------------------------|
| `language`      | type name segment 1 — the language namespace (`python`, `docker`, …) |
| `flavor`        | segment 2 — `std` when the language has a standard toolchain         |
| `kind`          | segment 3 — `lib`, `tool`, `image`, `module`, `workspace`, …         |
| `type_version`  | renders the `v<N>` directory and the file's `"version"`              |
| `description`   | one line: what projects of this type are                             |

`type_name` / `type_dir` are computed — leave them at their defaults.

## Authoring rule: Go templates vs. cookiecutter

`project-type.json` is a **cookiecutter template** whose output contains
**Go templates** (`{{.param}}` in steps and environment values). Cookiecutter
(Jinja) would eat the `{{...}}` expressions, so every Go-template expression
in the skeleton is wrapped in `{% raw %}…{% endraw %}`. Keep that wrapping
when you add steps, params, or environment values — otherwise the rendered
type silently loses its template expressions.

## After scaffolding

1. Edit `project-type.json`: real `tools`, real `targets`, drop the sample
   `params`/`environment` (or make them real). Add `scripts/` for long
   commands and `help/project.md` + `help/<target>.md` for CLI help.
2. `smith smelt --path <language>/<flavor>/<kind>/v<N>` — packs the ingot and
   its `.sha256` sidecar; re-run it after every edit.
3. Publish by copying the type tree into the registry repo and pushing; the
   registry's `task publish` re-smelts every type, and consumers pick the
   type up with `smith sync`.
