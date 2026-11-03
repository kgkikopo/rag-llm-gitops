# 9.1. Secrets management Operators in OpenShift Container Platform

OpenShift Container Platform offers supported Operators to secure and automate the management of sensitive data such as external credentials and digital certificates. 

The following Operators are available for secrets management: 

  * **Secrets Store CSI driver** : Enables Kubernetes to connect to external systems, and mount credentials from the external system into an application workload. 
  * **External Secrets Operator for Red Hat OpenShift** : Retrieves credentials stored in external management systems and makes them available within OpenShift Container Platform as standard Kubernetes Secrets. 
  * **cert-manager Operator for Red Hat OpenShift** : Manages the lifecycle of digital certificates that are used by applications running on OpenShift Container Platform by automating the process of issuance and renewal.
