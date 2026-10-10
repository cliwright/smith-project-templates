// docker-bake.hcl — build parameters for {{cookiecutter.image_name}}.
//
// Single source of truth for how the image is built: tags, build args,
// platforms, cache. Smith's docker/bake/image type builds with
// `docker buildx bake`, which reads this file; anything declared here is
// picked up automatically.
//
// Variables are overridable from the environment at invocation time:
//   TAG=1.4.2 docker buildx bake
//   REGISTRY=localhost:5000/mine docker buildx bake --push

variable "REGISTRY" {
  default = "{{cookiecutter.registry}}"
}

variable "IMAGE" {
  default = "{{cookiecutter.image_name}}"
}

variable "TAG" {
  default = "dev"
}

target "image" {
  context    = "."
  dockerfile = "Dockerfile"
  tags       = ["${REGISTRY}/${IMAGE}:${TAG}"]
  args = {
    IMAGE_VERSION = "${TAG}"
  }
  // Multi-arch: add platforms and push — a local docker store only holds one
  // platform's image at a time:
  //   platforms = ["linux/amd64", "linux/arm64"]
}
