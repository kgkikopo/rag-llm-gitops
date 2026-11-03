# 4.10. User-provided certificates for default ingress

Review user-provided ingress certificates in OpenShift Container Platform, including transport layer security (TLS) secret storage, `IngressController` references, and replacing Operator-generated defaults. 

Use user-provided certificates for the default `IngressController` CR to complete the following tasks: 

  * Replace Operator-generated default certificates before production use. 
  * Store TLS secrets in the correct namespace. 
  * Reference the secret in the `IngressController` CR. 



## 4.10.1. User-provided certificates for default ingress reference

Use user-provided default ingress certificates to allow applications on the default apps domain to present a custom TLS certificate to clients, so clients do not need to have cluster-managed certificate authority (CA) certificates installed. 

### 4.10.1.1. Purpose

Applications are usually exposed at `<route_name>.apps.<cluster_name>.<base_domain>`. The `<cluster_name>` and `<base_domain>` come from the installation config file. `<route_name>` is the host field of the route, if specified, or the route name. For example, `hello-openshift-default.apps.username.devcluster.openshift.com`. `hello-openshift` is the name of the route and the route is in the default namespace. You might want clients to access the applications without distributing cluster-managed CA certificates to the clients. Cluster administrators must set a custom default certificate when serving application content. 

Warning

The Ingress Operator generates a default certificate for an `IngressController` CR to serve as a placeholder until you configure a custom default certificate. Do not use Operator-generated default certificates in production clusters. 

### 4.10.1.2. Location

Store user-provided certificates in a `tls` type `Secret` resource in the `openshift-ingress` namespace. Update the `IngressController` CR in the `openshift-ingress-operator` namespace to enable the use of the user-provided certificate. For more information, see "Setting a custom default certificate". 

### 4.10.1.3. Management

User-provided certificates are managed by the user. 

### 4.10.1.4. Expiration

Expiration and renewal are managed by the user. 

### 4.10.1.5. Services

Applications deployed on the cluster use user-provided certificates for default ingress. 

### 4.10.1.6. Customization

Update the secret containing the user-managed certificate as needed. 

## 4.10.2. Additional resources

  * [Replacing the default ingress certificate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/configuring-certificates#replacing-default-ingress "3.1. Replacing the default ingress certificate")
  * [Setting a custom default certificate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#nw-ingress-setting-a-custom-default-certificate_configuring-ingress)
