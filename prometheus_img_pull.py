#!/usr/bin/python3

import os
import time

img_list = [
    "quay.io/prometheus/alertmanager:v0.27.0",
    "quay.io/prometheus/node-exporter:v1.8.2",
    "quay.io/prometheus-operator/prometheus-config-reloader:v0.76.0",
    "quay.io/prometheus/prometheus:v2.54.1",
    "quay.io/prometheus/pushgateway:v1.9.0",
    "registry.k8s.io/kube-state-metrics/kube-state-metrics:v2.13.0",
]

public_registry_list = [
    "quay.io",
    "registry.k8s.io",

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
