import os
from kubernetes import client, config

# Set the Kubernetes namespace
namespace = "s4"

# Load the Kubernetes configuration with the specified namespace
config.load_kube_config(context=namespace)

# Define Kubernetes API client
api = client.CoreV1Api()

# Specify the PVC name
pvc_name = "my-pvc"

# Define the initial threshold (in GiB) for triggering auto-scaling
threshold_gib = 190  # Initial threshold (you can customize this)

# Retrieve the PVC size and calculate the maximum size
def get_pvc_status():
    try:
        pvc = api.read_namespaced_persistent_volume_claim(pvc_name, namespace)
        current_size = int(pvc.spec.resources.requests["storage"].replace("Gi", ""))
        max_size_gib = current_size + 5  # Add 5 GiB to the current size
        return current_size, max_size_gib
    except Exception as e:
        print(f"Error getting PVC: {e}")
        return None, None

def scale_pvc():
    current_size, max_size_gib = get_pvc_status()
    if current_size is not None:
        if current_size >= threshold_gib:
            print(f"Current PVC size: {current_size} GiB")
            print(f"Scaling PVC to {max_size_gib} GiB")
            
            # Update PVC size
            pvc = api.read_namespaced_persistent_volume_claim(pvc_name, namespace)
            pvc.spec.resources.requests["storage"] = f"{max_size_gib}Gi"
            api.patch_namespaced_persistent_volume_claim(pvc_name, namespace, pvc)
            print("PVC scaled successfully.")

if __name__ == "__main__":
    scale_pvc()
