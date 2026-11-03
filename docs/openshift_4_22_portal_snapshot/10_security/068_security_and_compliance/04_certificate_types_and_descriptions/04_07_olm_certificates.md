# 4.7. OLM certificates

Understand how Operator Lifecycle Manager (OLM) manages certificates for OLM components and creates and rotates certificates when installing Operators that include webhooks or API services. In proxy environments, you must manage Operator certificates yourself because OLM does not update them. 

## 4.7.1. Management

All certificates for Operator Lifecycle Manager (OLM) components, such as `olm-operator`, `catalog-operator`, `packageserver`, and `marketplace-operator`, are managed by the system. 

When installing Operators that include webhooks or API services in their `ClusterServiceVersion` (CSV) object, OLM creates and rotates the certificates for these resources. Certificates for resources in the `openshift-operator-lifecycle-manager` namespace are managed by OLM. 

OLM does not update the certificates of Operators that it manages in proxy environments. These certificates must be managed by the user using the subscription config. 

## 4.7.2. Additional resources

  * [Configuring proxy support in Operator Lifecycle Manager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-configuring-proxy-support)
  * [Proxy certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#proxy-certificates "4.2. Proxy certificates")
  * [Replacing the default ingress certificate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/configuring-certificates#replacing-default-ingress "3.1. Replacing the default ingress certificate")
  * [Updating the CA bundle](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/configuring-certificates#updating-ca-bundle "3.4. Updating the CA bundle")
