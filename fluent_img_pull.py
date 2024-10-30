#!/usr/bin/python3

import os
import time

img_list = [
    "busybox:latest",
    "cr.fluentbit.io/fluent/fluent-bit:3.1.7",
    "cr.fluentbit.io/fluent/fluent-bit:3.1.7-debug"
]

public_registry_list = [
    "quay.io",
    "registry.k8s.io",
    "cr.fluentbit.io"

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
