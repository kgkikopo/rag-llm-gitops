# 9.2. Secrets management use cases

You can integrate secrets management Operators with other OpenShift Container Platform components to securely manage, automate, and consume credentials across infrastructure and application workflows. 

## 9.2.1. External Secrets Operator for Red Hat OpenShift use cases

You can integrate the External Secrets Operator with other OpenShift Container Platform components to securely manage and inject credentials. Learn how to apply External Secrets Operator in real-world deployment strategies, by reviewing the following example. 

Securing Red Hat OpenShift GitOps by using External Secrets Operator short-lived tokens
     To reduce the security risk of compromised credentials, you can configure the External Secrets Operator to generate short-lived tokens. Red Hat OpenShift GitOps can then use these temporary tokens to securely authenticate when accessing GitHub repositories. You can refer to an example of the integration in the External Secrets Operator and GitOps demonstration. 

**Additional resources**

  * [External Secrets Operator and GitOps demonstration](https://interact.redhat.com/share/tcwyXElfYLWTvHl5dJ5n)
  * [Zero trust GitOps: Build a secure, secretless GitOps pipeline](https://developers.redhat.com/articles/2026/03/13/zero-trust-gitops-build-secure-secretless-gitops-pipeline)



**Additional resources**

  * [Secrets Store Container Storage Interface Driver Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-secrets-store)
  * [External Secrets Operator for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/external-secrets-operator-for-red-hat-openshift#external-secrets-operator-about "13.1. External Secrets Operator for Red Hat OpenShift overview")
  * [cert-manager Operator for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/cert-manager-operator-for-red-hat-openshift#cert-manager-operator-about "11.1. cert-manager Operator for Red Hat OpenShift overview")
