# 11.8. Configuring certificates with an issuer

By using the cert-manager Operator for Red Hat OpenShift, you can manage certificates, handling tasks such as renewal and issuance, for workloads within the cluster, as well as components interacting externally to the cluster. 

## 11.8.1. Create certificates for user workloads

To secure communications for your applications, create and manage TLS certificates for your workloads by using the cert-manager Operator for Red Hat OpenShift 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have installed the cert-manager Operator for Red Hat OpenShift. 



**Procedure**

  1. Create an issuer. For more information, see "Configuring an issuer" in the "Additional resources" section. 
  2. Create a certificate: 

     1. Create a YAML file, for example, `certificate.yaml`, that defines the `Certificate` object: 

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: <tls_cert>
  namespace: <issuer_namespace>
spec:
  isCA: false
  commonName: '<common_name>'
  secretName: <secret_name>
  dnsNames:
  - "<domain_name>"
  issuerRef:
    name: <issuer_name>
    kind: Issuer
```


where: 

`<tls_cert>`
     Specifies a name for the certificate. 
`<issuer_namespace>`
     Specifies the namespace of the issuer. 
`<common_name>`
     Specifies the common name (CN). 
`<secret_name>`
     Specifies the name of the secret to create that contains the certificate. 
`<domain_name>`
     Specifies the domain name. 
`<issuer_name>`
     Specifies the name of the issuer. 

     2. Create the `Certificate` object by running the following command: 

```shell-session
$ oc create -f certificate.yaml
```


**Verification**

  * Verify that the certificate is created and ready to use by running the following command: 

```shell-session
$ oc get certificate -w -n <issuer_namespace>
```


Once certificate is in `Ready` status, workloads on your cluster can start using the generated certificate secret. 




## 11.8.2. Create certificates for the API server

To secure interactions with the cluster control plane, create TLS certificates for the API server by using the cert-manager Operator for Red Hat OpenShift. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have installed version 1.13.0 or later of the cert-manager Operator for Red Hat OpenShift. 



**Procedure**

  1. Create an issuer. For more information, see "Configuring an issuer" in the "Additional resources" section. 
  2. Create a certificate: 

     1. Create a YAML file, for example, `certificate.yaml`, that defines the `Certificate` object: 

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: <tls_cert>
  namespace: openshift-config
spec:
  isCA: false
  commonName: "api.<cluster_base_domain>"
  secretName: <secret_name>
  dnsNames:
  - "api.<cluster_base_domain>"
  issuerRef:
    name: <issuer_name>
    kind: Issuer
```


where: 

`<tls_cert>`
     Specifies a name for the certificate. 
`<cluster_base_domain>`
     Specifies the common name (CN). 
`<secret_name>`
     Specifies the name of the secret to create that contains the certificate. 
`<issuer_name>`
     Specifies the name of the issuer. 

     2. Create the `Certificate` object by running the following command: 

```shell-session
$ oc create -f certificate.yaml
```


  3. Add the API server named certificate. For more information, see "Adding an API server named certificate" section in the "Additional resources" section. 

Note

To ensure the certificates are updated, run the `oc login` command again after the certificate is created. 




**Verification**

  * Verify that the certificate is created and ready to use by running the following command: 

```shell-session
$ oc get certificate -w -n openshift-config
```


Once certificate is in `Ready` status, API server on your cluster can start using the generated certificate secret. 




## 11.8.3. Create certificates for the Ingress Controller

You can create a certificate for the Ingress Controller and then replace bootstrapped default self-signed certificates with cert-manager-managed external certificates. 

Note

Before using the procedure, ensure you understand the following Ingress Controller behaviors: 

  * When certificates are renewed or rotated by using the cert-manager Operator, only the contents of the secret, such as the certificate and key, are updated. The secret name remains unchanged. Kubelet automatically propagates these updates to the mounted volume, allowing the router to detect the file changes and hot-reload the new certificate and key. As a result, no rolling update of the router deployment is triggered or required. 
  * The secret name is referenced in the Ingress Controller configuration. If you want to replace the default ingress certificate or use different secret name in Ingress Controller configuration, you must patch or edit the configuration to apply the change. This operation triggers a rolling update for router pods where new router pods load the new cert/key pair. 



**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have installed version 1.13.0 or later of the cert-manager Operator for Red Hat OpenShift. 



**Procedure**

  1. Create an issuer. For more information, see "Configuring an issuer" in the "Additional resources" section. 
  2. Create a certificate: 

     1. Create a YAML file, for example, `certificate.yaml`, that defines the `Certificate` object: 

**Example`certificate.yaml` file**

```yaml
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: <tls_cert>
  namespace: openshift-ingress
spec:
  isCA: false
  commonName: "apps.<cluster_base_domain>"
  secretName: <secret_name>
  dnsNames:
  - "apps.<cluster_base_domain>"
  - "\*.apps.<cluster_base_domain>"
  issuerRef:
    name: <issuer_name>
    kind: Issuer
```


where: 

`<tls_cert>`
     Specifies the name for the certificate. 
`<cluster_base_domain>`
     Specifies the common name (CN). 
`<secret_name>`
     Specifies the name of the secret to create that contains the certificate. 
`<cluster_base_domain>`
     Specifies the DNS name of the ingress. 
`<issuer_name>`
     Specifies the name of the issuer. 

     2. Create the `Certificate` object by running the following command: 

```shell-session
$ oc create -f certificate.yaml
```


  3. Replace the default ingress certificate. For more information, see "Replacing the default ingress certificate" section in the "Additional resources" section. 



**Verification**

  1. Verify that the certificate is created and ready to use by running the following command: 

```shell-session
$ oc get certificate -n openshift-ingress
```


  2. Verify the definition and content of the secret object by running the following command: 

```shell-session
$ oc get secret <secretName> -n openshift-ingress
```


  3. Verify that the default TLS certificate has the correct configuration details for the Ingress Controller by running the following command: 

```shell-session
$ oc get ingresscontroller default -n openshift-ingress-operator -o yaml | grep -A2 defaultCertificate
```


After the certificate is in `Ready` status, the Ingress Controller on your cluster can start using the generated certificate secret. 




**Additional resources**

  * [Red Hat Knowledgebase solution](https://access.redhat.com/solutions/4542531)



## 11.8.4. Additional resources

  * [Supported issuer types](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/cert-manager-operator-for-red-hat-openshift#cert-manager-issuer-types_cert-manager-operator-about "11.1.2. cert-manager Operator for Red Hat OpenShift issuer providers")
  * [Configuring an ACME issuer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/cert-manager-operator-for-red-hat-openshift#cert-manager-operator-issuer-acme "11.7. Configuring an ACME issuer")
  * [Adding an API server named certificate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/configuring-certificates#customize-certificates-api-add-named_api-server-certificates "3.2.1. Add an API server named certificate for the first time")
  * [Replacing the default ingress certificate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/configuring-certificates#replacing-default-ingress "3.1. Replacing the default ingress certificate")
