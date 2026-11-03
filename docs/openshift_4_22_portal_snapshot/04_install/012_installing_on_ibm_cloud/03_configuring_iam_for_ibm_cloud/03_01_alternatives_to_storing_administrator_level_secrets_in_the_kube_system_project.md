# 3.1. Alternatives to storing administrator-level secrets in the kube-system project

The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). You can configure the CCO to suit the security requirements of your organization by setting different values for the `credentialsMode` parameter in the `install-config.yaml` file. 

Storing an administrator-level credential secret in the cluster `kube-system` project is not supported for IBM Cloud®; therefore, you must set the `credentialsMode` parameter for the CCO to `Manual` when installing OpenShift Container Platform and manage your cloud credentials manually. 

Using manual mode allows each cluster component to have only the permissions it requires, without storing an administrator-level credential in the cluster. You can also use this mode if your environment does not have connectivity to the cloud provider public IAM endpoint. However, you must manually reconcile permissions with new release images for every upgrade. You must also manually supply credentials for every component that requests them. 

**Additional resources**

  * [About the Cloud Credential Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#about-cloud-credential-operator)
