import os
from kubernetes import client, config

# Set the Kubernetes namespace
namespace = "s4"

# Load the Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api = client.CoreV1Api()

def get_pods_in_namespace(namespace):
    try:
        pods = api.list_namespaced_pod(namespace=namespace)
        return pods.items
    except Exception as e:
        print(f"Error getting pods in namespace {namespace}: {e}")
        return []

if __name__ == "__main__":
    pods = get_pods_in_namespace(namespace)
    
    if pods:
        print("Pods in namespace:")
        for pod in pods:
            print(f"Pod Name: {pod.metadata.name}")
    else:
        print("No pods found in the specified namespace.")
