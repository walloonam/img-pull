#!/usr/bin/python3

import os
import time

img_list = [
    "goharbor/harbor-core:v2.9.1",
    "goharbor/harbor-db:v2.9.1",    
    "goharbor/harbor-jobservice:v2.9.1",
    "goharbor/harbor-portal:v2.9.1",
    "goharbor/harbor-registryctl:v2.9.1",
    "goharbor/redis-photon:v2.9.1",
    "goharbor/registry-photon:v2.9.1",
    "goharbor/trivy-adapter-photon:v2.9.1"

]

public_registry_list = [
    "docker.io",
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
