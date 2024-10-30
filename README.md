
# 폐쇄망 환경에서의 K8s YAML 이미지 주소 업데이트 스크립트

이 Python 스크립트는 폐쇄망(air-gapped) 환경에서 Kubernetes YAML 파일 내의 공개 이미지 URL을 사설 레지스트리 URL로 변경하여, 제한된 네트워크 환경에서도 클러스터가 이미지에 접근할 수 있도록 합니다.

## 기능

- Kubernetes YAML 파일을 파싱하여 이미지 필드를 자동으로 찾아 업데이트합니다.
- `Deployment`, `DaemonSet`, `StatefulSet` 등 Kubernetes의 다양한 리소스 타입을 지원합니다.
- 공개 이미지 URL을 사설 레지스트리 주소로 일괄 변경할 수 있습니다.

## 요구 사항

- Python 3.x
