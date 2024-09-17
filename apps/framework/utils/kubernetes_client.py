import yaml
from kubernetes import client, config

from core.components.kubernetes import KUBE_CONFIG_FILE


class KubernetesClient:
    def __init__(self, namespace: str = "default"):
        """
        :param namespace: 操作的目标NameSpace
        :param kube_config_file: 目标KubeConfig，不填写则获取默认配置文件路径
        """
        self.namespace = namespace
        if KUBE_CONFIG_FILE:
            config.load_kube_config(config_file=KUBE_CONFIG_FILE)
        else:
            config.load_incluster_config()

        self.core_api = client.CoreV1Api()
        self.app_api = client.AppsV1Api()
        self.storage_api = client.StorageV1Api()
        self.custom_object_api = client.CustomObjectsApi()
        self.batch_api = client.BatchV1Api()
        self.traefik_resource_group = "traefik.containo.us"

        self.argo_resource_group = "argoproj.io"
        self.argo_resource_version = "v1alpha1"
