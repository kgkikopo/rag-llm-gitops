# 2.11. Understanding DNS management policies

As a cluster administrator, when you create an Ingress Controller, the Operator manages the DNS records automatically. 

This approach has some limitations when the required DNS zone is different from the cluster DNS zone or when the DNS zone is hosted outside the cloud provider. 

The following list details key aspects for a managed DNS management policy: 

  * The Managed DNS management policy for Ingress Controllers ensures that the lifecycle of the wildcard DNS record on the cloud provider is automatically managed by the Operator. This is the default behavior. 
  * When you change an Ingress Controller from `Managed` to `Unmanaged` DNS management policy, the Operator does not clean up the previous wildcard DNS record provisioned on the cloud. 
  * When you change an Ingress Controller from `Unmanaged` to `Managed` DNS management policy, the Operator attempts to create the DNS record on the cloud provider if it does not exist or updates the DNS record if it already exists. 
  * The Unmanaged DNS management policy for Ingress Controllers ensures that the lifecycle of the wildcard DNS record on the cloud provider is not automatically managed; instead, it becomes the responsibility of the cluster administrator. 

Note

For Google Cloud installations, you can use a custom DNS solution. Refer to the `DNSRecord` CR for information on what you need to include in the DNS record. For more information, see [Enabling a user-managed DNS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installation-gcp-enabling-user-managed-DNS_installing-gcp-customizations) and [Provisioning your own DNS records](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installation-gcp-provisioning-own-dns-records_installing-gcp-customizations). 




## 2.11.1. Creating an Ingress Controller for manual DNS management

As a cluster administrator, you can create a new custom Ingress Controller with the Unmanaged DNS management policy. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You are logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Create an `IngressController` custom resource (CR) file named `sample-ingress.yaml` with the following content: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  namespace: openshift-ingress-operator
  name: <name>
spec:
  domain: <domain>
  endpointPublishingStrategy:
    type: LoadBalancerService
    loadBalancer:
      scope: External
      dnsManagementPolicy: Unmanaged
```


where: 

`metadata.name`
     Specify the `<name>` with a name for the `IngressController` object. 
`spec.domain`
     Specify the `domain` based on the DNS record that was created as a prerequisite. 
`loadBalancer.scope`
     Specify the `scope` as `External` to expose the load balancer externally. `loadBalancer.dnsManagementPolicy`: Specifies if the Ingress Controller is managing the lifecycle of the wildcard DNS record associated with the load balancer. The valid values are `Managed` and `Unmanaged`. The default value is `Managed`. 

  2. Apply the manifest to create the `IngressController` object: 

```shell-session
$ oc apply -f sample-ingress.yaml
```


  3. Verify that the Ingress Controller was created with the correct policy by running the following command: 

```shell-session
$ oc get ingresscontroller <name> -n openshift-ingress-operator -o=jsonpath={.spec.endpointPublishingStrategy.loadBalancer}
```


Inspect the output and confirm that `dnsManagementPolicy` is set to `Unmanaged`. 




## 2.11.2. Modifying an existing Ingress Controller for manual DNS management

As a cluster administrator, you can modify an existing Ingress Controller to manually manage the DNS record lifecycle. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You are logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Modify the chosen Ingress Controller to set the `dnsManagementPolicy` parameter: 

```shell-session
$ SCOPE=$(oc -n openshift-ingress-operator get ingresscontroller <name> -o=jsonpath="{.status.endpointPublishingStrategy.loadBalancer.scope}")
```


```shell-session
$ oc -n openshift-ingress-operator patch ingresscontrollers/default --type=merge --patch="{\"spec\":{\"endpointPublishingStrategy\":{\"type\":\"LoadBalancerService\",\"loadBalancer\":{\"dnsManagementPolicy\":\"Unmanaged\", \"scope\":\"${SCOPE}\"}}}}"
ingresscontroller.operator.openshift.io/default patched
```


  2. Verify that the Ingress Controller was modified correctly by running the following command: 

```shell-session
$ oc get ingresscontroller <name> -n openshift-ingress-operator -o=jsonpath={.spec.endpointPublishingStrategy.loadBalancer}
```


Inspect the output and confirm that `dnsManagementPolicy` is set to `Unmanaged`. 




## 2.11.3. Additional resources

  * [Ingress Controller configuration parameters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#nw-ingress-controller-configuration-parameters_configuring-ingress)
