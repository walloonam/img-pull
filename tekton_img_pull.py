#!/usr/bin/python3

import os
import time

img_list = [
    "gcr.io/tekton-releases/github.com/tektoncd/dashboard/cmd/dashboard:v0.50.0@sha256:7f1591f311efab1bda7b1c7ce2a84aecb4a4792a15570683c5f3d09868a94f67",
    "gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/controller:v0.63.0@sha256:fd66b42c1076dec4430ab6767919e56c95b6a547c9696c40e06329c7b3b932ba",
    "gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/events:v0.63.0@sha256:709181f33f41654e39a74087194c61a20e515dcc530cbb99af8c8426f4ddc266",
    "gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/resolvers:v0.63.0@sha256:e3d170eb9bc04c6ee69306529c2f82e84296a52414e136ef16995ac179abcd12",
    "gcr.io/tekton-releases/github.com/tektoncd/pipeline/cmd/webhook:v0.63.0@sha256:66333eecff97acf5e5e0de9c104d51de9c507aa75361b0d94f5af583306ea18a",
    "gcr.io/tekton-releases/github.com/tektoncd/triggers/cmd/controller:v0.29.1@sha256:34aa909bd6de6b24c78004bbd5eac0d8d1f438bba4be5beb385b61b88977bffe",
    "gcr.io/tekton-releases/github.com/tektoncd/triggers/cmd/webhook:v0.29.1@sha256:6ec798175d57ad3fef752b6c2eddab78145d0d4e1472c79535bf4d9772cd1cca",
    "gcr.io/tekton-releases/github.com/tektoncd/triggers/cmd/interceptors:v0.29.1@sha256:8de2dd26b46ce62270597b1be6c2a102fcc8828128c186ccc97aa0570f0f8656",
]

public_registry_list = [
    "quay.io",
    "registry.k8s.io",
    "gcr.io/tekton-releases/github.com"
]

registry_path = "reg.inje-private.com"

harbor_project_name = "nnd002"

for var in img_list:
    os.system(f"docker pull {var}")

    image_without_sha = var.split('@')[0]                                            # tag시 sha 없애는 코드 추가

    for foo in public_registry_list:
        if image_without_sha.startswith(foo):
            private_img_path = image_without_sha.replace(foo, f"{registry_path}/{harbor_project_name}")
            break
        private_img_path = f"{registry_path}/{harbor_project_name}/{image_without_sha}"
#        else:                                                                 ljh 수정
#            private_img_path = f"{registry_path}/{harbor_project_name}/{var}"
    time.sleep(1)
#    os.system(f"echo {private_img_path}")
    os.system(f"docker tag {var} {private_img_path}")
    os.system(f"docker push {private_img_path}")
