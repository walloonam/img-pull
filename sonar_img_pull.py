#!/usr/bin/python3

import os
import time

img_list = [
    "busybox:1.32",
    "docker.io/bitnami/postgresql:11.14.0-debian-10-r22",
    "sonarqube:10.6.0-community"
]

public_registry_list = [
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
