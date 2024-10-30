#!/usr/bin/python3

import os
import time

img_list = [
    "busybox:latest",
    "docker.io/bitnami/pgpool:4.5.2-debian-12-r2",
    "docker.io/bitnami/postgresql-repmgr:16.3.0-debian-12-r15",
    "docker.io/bitnami/redis-cluster:7.2.5-debian-12-r2",
    "gitea/gitea:1.22.1-rootless"
]

public_registry_list = [
    "quay.io",
    "registry.k8s.io",
    "docker.io"

]

registry_path = "reg.inje-private.com"

harbor_project_name = "nnd002"

for var in img_list:
    os.system(f"docker pull {var}")
    for foo in public_registry_list:
        if var.startswith(foo):
            private_img_path = var.replace(foo, f"{registry_path}/{harbor_project_name}")
            break
        private_img_path = f"{registry_path}/{harbor_project_name}/{var}"
#        else:                                                                 ljh 수정
#            private_img_path = f"{registry_path}/{harbor_project_name}/{var}"
    time.sleep(1)
#    os.system(f"echo {private_img_path}")
    os.system(f"docker tag {var} {private_img_path}")
    os.system(f"docker push {private_img_path}")
