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