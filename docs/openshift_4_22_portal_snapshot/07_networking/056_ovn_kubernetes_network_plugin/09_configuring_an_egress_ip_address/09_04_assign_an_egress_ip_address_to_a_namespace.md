# 9.4. Assign an egress IP address to a namespace

You can assign one or more egress IP addresses to a namespace or to specific pods in a namespace. 

**Prerequisites**

  * The OpenShift CLI (`oc`) is installed. 
  * You are logged in to the cluster as a cluster administrator. 
  * At least one node is configured to host an egress IP address. 



**Procedure**

  1. Create an `EgressIP` object. 

     1. Create a `<egressips_name>.yaml` file where `<egressips_name>` is the name of the object. 
     2. In the file that you created, define an `EgressIP` object, as in the following example: 

```yaml
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egress-project1
spec:
  egressIPs:
  - 192.168.127.10
  - 192.168.127.11
  namespaceSelector:
    matchLabels:
      env: qa
# ...
```


  2. To create the object, enter the following command. 

```shell-session
$ oc apply -f <egressips_name>.yaml
```


where: 

`<egressips_name>`
     Replace `<egressips_name>` with the name of the object. 

**Example output**

```shell-session
egressips.k8s.ovn.org/<egressips_name> created
```


  3. Optional: Store the `<egressips_name>.yaml` file so that you can make changes later. 
  4. Add labels to the namespace that requires egress IP addresses. To add a label to the namespace of an `EgressIP` object defined in a previous step, run the following command: 

```shell-session
$ oc label ns <namespace> env=qa
```


where: 

`<namespace>`
     Replace `<namespace>` with the namespace that requires egress IP addresses. 




**Verification**

  * To show all egress IP addresses that are in use in your cluster, enter the following command: 

```shell-session
$ oc get egressip -o yaml
```


Note

The command `oc get egressip` only returns one egress IP address regardless of how many are configured. This is not a bug and is a limitation of Kubernetes. As a workaround, you can pass in the `-o yaml` or `-o json` flags to return all egress IPs addresses in use. 

**Example output**

```shell-session
# ...
spec:
  egressIPs:
  - 192.168.127.10
  - 192.168.127.11
# ...
```
