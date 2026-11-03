# 3.4. Editing a network policy

As a cluster administrator, you can edit an existing network policy for a namespace. 

## 3.4.1. Edit a network policy

To modify existing policy configurations, you can edit a network policy in a namespace. Edit policies by modifying the policy file and applying it with `oc apply`, or by using the `oc edit` command directly. 

Note

If you log in with `cluster-admin` privileges, you can edit network policies in any namespace in the cluster. 

Note

If you log in with `cluster-admin` privileges, you can edit network policies in any namespace in the cluster. In the web console, you can edit policies directly in YAML or by using the **Actions** menu. 

**Prerequisites**

  * Your cluster uses a network plugin that supports `NetworkPolicy` objects, such as the OVN-Kubernetes network plugin, with `mode: NetworkPolicy` set. 
  * You installed the OpenShift CLI (`oc`). 
  * You are logged in to the cluster with a user with `admin` privileges. 
  * You are working in the namespace where the network policy exists. 



**Procedure**

  1. Optional: To list the network policy objects in a namespace, enter the following command: 

```shell-session
$ oc get network policy -n <namespace>
```


where: 

`<namespace>`
     Optional: Specifies the namespace if the object is defined in a different namespace than the current namespace. 

  2. Edit the network policy object. 

     1. If you saved the network policy definition in a file, edit the file and make any necessary changes, and then enter the following command. 

```shell-session
$ oc apply -n <namespace> -f <policy_file>.yaml
```


where: 

`<namespace>`
     Optional: Specifies the namespace if the object is defined in a different namespace than the current namespace. 
`<policy_file>`
     Specifies the name of the file containing the network policy. 

     2. If you need to update the network policy object directly, enter the following command: 

```shell-session
$ oc edit network policy <policy_name> -n <namespace>
```


where: 

`<policy_name>`
     Specifies the name of the network policy. 
`<namespace>`
     Optional: Specifies the namespace if the object is defined in a different namespace than the current namespace. 

  3. Confirm that the network policy object is updated. 

```shell-session
$ oc describe networkpolicy <policy_name> -n <namespace>
```


where: 

`<policy_name>`
     Specifies the name of the network policy. 
`<namespace>`
     Optional: Specifies the namespace if the object is defined in a different namespace than the current namespace. 




## 3.4.2. Example NetworkPolicy object

Reference the example `NetworkPolicy` object to understand how to configure this object. 

```yaml
kind: NetworkPolicy
apiVersion: networking.k8s.io/v1
metadata:
  name: allow-27107
spec:
  podSelector:
    matchLabels:
      app: mongodb
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: app
    ports:
    - protocol: TCP
      port: 27017
```


where: 

`name`
     The name of the NetworkPolicy object. 
`spec.podSelector`
     A selector that describes the pods to which the policy applies. The policy object can only select pods in the project that defines the NetworkPolicy object. 
`ingress.from.podSelector`
     A selector that matches the pods from which the policy object allows ingress traffic. The selector matches pods in the same namespace as the NetworkPolicy. 
`ingress.ports`
     A list of one or more destination ports on which to accept traffic. 

## 3.4.3. Additional resources

  * [Creating a network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_security/network-policy#creating-network-policy "3.2. Creating a network policy")
