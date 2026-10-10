"""Keep only the parameters files of the build tool chosen at scaffold time.

The template ships both flavors (docker-bake.hcl, and compose.yaml + .env);
`build_tool` picks exactly one. A Smith project should contain only the
parameters file its type actually drives. `.env` is shipped as `dot_env`
because dotfiles-by-that-name are awkward in template repos; it is renamed
into place here.
"""
import os
import sys

RENAME_WHEN = {
    "compose": [("dot_env", ".env")],
}

REMOVE_WHEN = {
    "bake": ["compose.yaml", "dot_env"],
    "compose": ["docker-bake.hcl"],
}


def main() -> int:
    tool = "{{ cookiecutter.build_tool }}"
    removed, renamed = [], []
    for src, dst in RENAME_WHEN.get(tool, []):
        if os.path.isfile(src):
            os.rename(src, dst)
            renamed.append("%s -> %s" % (src, dst))
    for path in REMOVE_WHEN[tool]:
        if os.path.isfile(path):
            os.remove(path)
            removed.append(path)
    if renamed:
        print("Renamed %s" % ", ".join(renamed))
    if removed:
        print("Removed unused %s parameters file(s): %s" % (tool, ", ".join(removed)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
