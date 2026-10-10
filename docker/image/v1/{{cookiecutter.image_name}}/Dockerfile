# syntax=docker/dockerfile:1

# Base image is fixed at scaffold time (see cookiecutter.json) but stays a
# build arg, so it can be overridden without editing the file:
#   docker build --build-arg BASE_IMAGE=debian:bookworm-slim ...
ARG BASE_IMAGE={{cookiecutter.base_image}}
FROM ${BASE_IMAGE}

# Non-root runtime user (numeric UID/GID 10001, family-agnostic). The
# creation commands differ per base-image family, chosen at scaffold time.
{% if cookiecutter.base_image_family == "alpine" -%}
RUN addgroup -S -g 10001 app && adduser -S -G app -u 10001 app
{%- else -%}
RUN groupadd --system --gid 10001 app && useradd --system --uid 10001 --gid app app
{%- endif %}

ARG IMAGE_VERSION=dev
LABEL org.opencontainers.image.title="{{cookiecutter.image_name}}" \
      org.opencontainers.image.description="{{cookiecutter.project_short_description}}" \
      org.opencontainers.image.version="${IMAGE_VERSION}" \
      org.opencontainers.image.source="https://github.com/{{cookiecutter.org}}/{{cookiecutter.image_name}}"

WORKDIR /app
COPY --chmod=755 entrypoint.sh /usr/local/bin/entrypoint.sh

USER app
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
