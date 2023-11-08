 kubectl config use-context context-cu44zaiaeoq
 kubectl config use-context gke_s4-project-202316_us-central1-c_prod-cluster

 kubectl get ns 

 kubectl get all -n cert-manager

 kubectl get secrets -n cert-manager

 kubectl get ingress -n cert-manager

kubectl describe clusterissuer letsencrypt-cluster-issuer

// existing s4
certmanager.k8s.io/cluster-issuer: s4-ssl
secretName: certificate-s4

kubectl get ingress -n joveo 

certmanager.k8s.io/cluster-issuer: joveo-ssl-certificate
secretName: joveo-certificate

Godaddy
-------------
dev.succcess4.us
auth.dev.success4.us
dev.minio.succcess4.us

-------------
demo.succcess4.us
auth.demo.success4.us
demo.minio.succcess4.us



creditunion-ssl --issure secret opaque
creditunion-certificate -- tls


SSL Certificate for K8s
---------------------------

Step1 : New Cluster

    Create Cert-Manager
    https://cert-manager.io/docs/installation/kubectl/
    kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.1/cert-manager.yaml

Step2 : kubectl get pods --namespace cert-manager

NAME                                       READY   STATUS    RESTARTS   AGE
cert-manager-5c6866597-zw7kh               1/1     Running   0          2m
cert-manager-cainjector-577f6d9fd7-tr77l   1/1     Running   0          2m
cert-manager-webhook-787858fcdb-nlzsq      1/1     Running   0          2m


Step3: kubectl apply -f cert-issuer.yaml


Step4: kubectl apply -f certificate.yaml

Step5: kubectl edit ingress csapi -n namspace


apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  annotations:
    certmanager.k8s.io/cluster-issuer: cert-issuer.yaml(name/secert/opaque)

 tls:
  - hosts:
    - demo.decisionminds.com (domainname)
    - auth.demo.decisionminds.com
    secretName: certificate.yaml (name/tls)

