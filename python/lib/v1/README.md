# Python Template

This template uses cookiecutter to generate a Python project with a basic structure and configuration.


```shell
/templates/python
├── cookiecutter.json
├── README.md
└── /{{cookiecutter.pypi_package_name}}
    ├── /docs
    │   ├── index.md
    │   └── installation.md
    ├── zensical.toml
    ├── pyproject.toml
    ├── README.md
    ├── /src
    │   └── /{{cookiecutter.project_slug}}
    │       ├── __init__.py
    │       ├── __main__.py
    │       └── / cli
    │           └── __init__.py
    ├── Taskfile.yml
    └── /tests
        ├── __init__.py
        ├── conftest.py
        └── test_{{cookiecutter.project_slug}}.py
```
