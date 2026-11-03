# 1.1. Security overview

It is important to understand how to properly secure various aspects of your OpenShift Container Platform cluster. 

## 1.1.1. Container security

A good starting point to understanding OpenShift Container Platform security is to review the concepts in [Understanding container security](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/container-security#security-understanding "2.1. Understanding container security"). This and subsequent sections provide a high-level walkthrough of the container security measures available in OpenShift Container Platform, including solutions for the host layer, the container and orchestration layer, and the build and application layer. These sections also include information on the following topics: 

  * Why container security is important and how it compares with existing security standards. 
  * Which container security measures are provided by the host (RHCOS and RHEL) layer and which are provided by OpenShift Container Platform. 
  * How to evaluate your container content and sources for vulnerabilities. 
  * How to design your build and deployment process to proactively check container content. 
  * How to control access to containers through authentication and authorization. 
  * How networking and attached storage are secured in OpenShift Container Platform. 
  * Containerized solutions for API management and SSO. 



## 1.1.2. Auditing

OpenShift Container Platform auditing provides a security-relevant chronological set of records documenting the sequence of activities that have affected the system by individual users, administrators, or other components of the system. Administrators can [configure the audit log policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/audit-log-policy-config "Chapter 15. Configuring the audit log policy") and [view audit logs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/audit-log-view "Chapter 14. Viewing audit logs"). 

## 1.1.3. Certificates

Certificates are used by various components to validate access to the cluster. Administrators can [replace the default ingress certificate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/configuring-certificates#replacing-default-ingress "3.1. Replacing the default ingress certificate"), [add API server certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/configuring-certificates#api-server-certificates "3.2. Adding API server certificates"), or [add a service certificate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/configuring-certificates#add-service-serving "3.3. Securing service traffic using service serving certificate secrets"). 

You can also review more details about the types of certificates used by the cluster: 

  * [User-provided certificates for the API server](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-user-provided-certificates-for-the-api-server "4.1. User-provided certificates for the API server")
  * [Proxy certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#proxy-certificates "4.2. Proxy certificates")
  * [Service CA certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-service-ca-certificates "4.3. Service CA certificates")
  * [Node certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-node-certificates "4.4. Node certificates")
  * [Bootstrap certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-bootstrap-certificates "4.5. Bootstrap certificates")
  * [etcd certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-etcd-certificates "4.6. etcd certificates")
  * [OLM certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-olm-certificates "4.7. OLM certificates")
  * [Aggregated API client certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-aggregated-api-client-certificates "4.8. Aggregated API client certificates")
  * [Machine Config Operator certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-machine-config-operator-certificates "4.9. Machine Config Operator certificates")
  * [User-provided certificates for default ingress](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-user-provided-certificates-for-default-ingress "4.10. User-provided certificates for default ingress")
  * [Ingress certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-ingress-certificates "4.11. Ingress certificates")
  * [Monitoring and cluster logging Operator component certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-monitoring-and-cluster-logging-operator-component-certificates "4.12. Monitoring and OpenShift Logging Operator component certificates")
  * [Control plane certificates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/certificate-types-and-descriptions#cert-types-control-plane-certificates "4.13. Control plane certificates")



## 1.1.4. Encrypting data

You can [enable etcd encryption](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/etcd/#etcd-encrypt) for your cluster to provide an additional layer of data security. For example, it can help protect the loss of sensitive data if an etcd backup is exposed to the incorrect parties. 

## 1.1.5. Vulnerability scanning

Administrators can use the Red Hat Quay Container Security Operator to run [vulnerability scans](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/pod-vulnerability-scan "Chapter 19. Scanning pods for vulnerabilities") and review information about detected vulnerabilities.
