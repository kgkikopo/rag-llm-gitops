# 11.11. Network policy configuration for cert-manager Operator

The cert-manager Operator for Red Hat OpenShift provides predefined `NetworkPolicy` resources to enhance security by controlling the ingress and egress traffic for its components. By default, this feature is disabled to prevent connectivity issues or breaking changes during an upgrade. To use this feature, you must enable it in the `CertManager` custom resource (CR). 

After enabling the default policies, you must manually configure additional egress rules to allow outbound traffic. These rules are required for cert-manager Operator for Red Hat OpenShift to communicate with external services beyond the API server and internal DNS. 

The examples of services that require custom egress rules include the following: 

  * ACME servers, for example, Let’s Encrypt 
  * DNS-01 challenge providers, for example, AWS Route53 or Cloudflare 
  * External CAs, such as HashiCorp Vault 



Note

Network policies are expected to be enabled by default in a future release, which could cause connectivity failures during an upgrade. To prepare for this change, configure the required egress policies. 

## 11.11.1. Default ingress and egress rules

The default network policy applies the following ingress and egress rules to each component. 

Component| Ingress ports| Egress ports| Description  
---|---|---|---  
`cert-manager` |  9402  |  6443, 5353  |  Allows ingress traffic to metrics server and egress traffic to OpenShift API server.   
`cert-manager-webhook` |  9402, 10250  |  6443  |  Allows ingress traffic to metrics and webhook servers, and egress traffic to OpenShift API server and internal DNS server.   
`cert-manager-cainjector` |  9402  |  6443  |  Allows ingress traffic to metrics server and egress traffic to OpenShift API server.   
`istio-csr` |  6443, 9402  |  6443  |  Allows ingress traffic to the gRPC Istio certificate request API, metrics servers and egress traffic to OpenShift API server.   
Show more

## 11.11.2. Network policy configuration parameters

You can enable and configure network policies for the cert-manager Operator components by updating the `CertManager` custom resource (CR). The CR includes the following parameters for enabling default network policies and defining custom egress rules. 

Field| Type| Description  
---|---|---  
`spec.defaultNetworkPolicy` |  `boolean` |  Specifies whether to enable the default network policy for the cert-manager Operator components.  Important Once you enable default network policies, you cannot disable them. This restriction prevents accidental security degradation. Before enabling this setting, ensure that you plan the network policy requirements.   
`spec.networkPolicies` |  `object` |  Defines a list of custom network policy configuration. To apply the configuration, you must set `spec.defaultNetworkPolicy` to `true`.   
`spec.networkPolicies.componentName` |  `string` |  Specifies the component that this network policy targets. The only valid value is `CoreController`.   
`spec.networkPolicies.egress` |  `object` |  Defines the egress rules for the specified component. Set to `{}` to allow connections to all external providers.   
`spec.networkPolicies.egress.ports` |  `object` |  Defines a list of network ports and protocols for the specified providers.   
`spec.networkPolicies.name` |  `string` |  Specifies a unique name for the custom network policy, which is used to generate the `NetworkPolicy` resource name.   
Show more

## 11.11.3. Network policy configuration examples

To control traffic flow and enhance cluster security, enable network policies and custom rules for the cert-manager Operator for Red Hat OpenShift. 

To enable network policy and custom rules, see the following example: 

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: CertManager
metadata:
  name: cluster
spec:
  defaultNetworkPolicy: "true"
```


To allow egress access to all external issuer providers, see the following example: 

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: CertManager
metadata:
  name: cluster
spec:
  defaultNetworkPolicy: "true"
  networkPolicies:
  - name: allow-egress-to-all
    componentName: CoreController
    egress:
     - {}
```


To allow the cert-manager Operator controller to perform the ACME challenge self-check, see the following example. This process requires connections to the ACME provider, DNS API endpoints, and recursive DNS servers. 

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: CertManager
metadata:
  name: cluster
spec:
  defaultNetworkPolicy: "true"
  networkPolicies:
  - name: allow-egress-to-acme-server
    componentName: CoreController
    egress:
    - ports:
      - port: 80
        protocol: TCP
      - port: 443
        protocol: TCP
  - name: allow-egress-to-dns-service
    componentName: CoreController
    egress:
    - ports:
      - port: 53
        protocol: UDP
      - port: 53
        protocol: TCP
```


## 11.11.4. Verifying the network policy creation

You can verify that the default and custom `NetworkPolicy` resources are created. 

**Prerequisites**

  * You have enabled network policy for cert-manager Operator for Red Hat OpenShift in the `CertManager` custom resource. 



**Procedure**

  * Verify the list of `NetworkPolicy` resources in the `cert-manager` namespace by running the following command: 

```shell-session
$ oc get networkpolicy -n cert-manager
```


**Example output**

```shell-session
NAME                                             POD-SELECTOR                              AGE
cert-manager-allow-egress-to-api-server          app.kubernetes.io/instance=cert-manager   7s
cert-manager-allow-egress-to-dns                 app=cert-manager                          6s
cert-manager-allow-ingress-to-metrics            app.kubernetes.io/instance=cert-manager   7s
cert-manager-allow-ingress-to-webhook            app=webhook                               6s
cert-manager-deny-all                            app.kubernetes.io/instance=cert-manager   8s
cert-manager-user-allow-egress-to-acme-server    app=cert-manager                          8s
cert-manager-user-allow-egress-to-dns-service    app=cert-manager                          7s
```


The output lists the default policies and any custom policies that you created.
