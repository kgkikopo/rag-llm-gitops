# 4.13. Control plane certificates

Review control plane certificate namespaces and automatic rotation in OpenShift Container Platform to plan maintenance and recover from expiration. 

## 4.13.1. Location

Control plane certificates are included in these namespaces: 

  * `openshift-config-managed`
  * `openshift-kube-apiserver`
  * `openshift-kube-apiserver-operator`
  * `openshift-kube-controller-manager`
  * `openshift-kube-controller-manager-operator`
  * `openshift-kube-scheduler`



## 4.13.2. Management

Control plane certificates are managed by the system and rotated automatically. 

If control plane certificates expire, see "Recovering from expired control plane certificates". 

## 4.13.3. Additional resources

  * [Recovering from expired control plane certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/backup_and_restore/#dr-recovering-expired-certs)
