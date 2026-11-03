# 6.2. Cloud Credential Operator

The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). 

The CCO syncs on `CredentialsRequest` custom resources (CRs) to allow OpenShift Container Platform components to request cloud provider credentials with the specific permissions that are required for the cluster to run. 

By setting different values for the `credentialsMode` parameter in the `install-config.yaml` file, the CCO can be configured to operate in several different modes. If no mode is specified, or the `credentialsMode` parameter is set to an empty string (`""`), the CCO operates in its default mode. 

CRDs
    

  * `credentialsrequests.cloudcredential.openshift.io`

    * Scope: Namespaced 
    * CR: `CredentialsRequest`
    * Validation: Yes 




Configuration objects
     No configuration required. 

**Additional resources**

  * [About the Cloud Credential Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#about-cloud-credential-operator)
  * [`CredentialsRequest` custom resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#credentialsrequest-cloudcredential-openshift-io-v1)
  * [openshift-cloud-credential-operator](https://github.com/openshift/cloud-credential-operator)
