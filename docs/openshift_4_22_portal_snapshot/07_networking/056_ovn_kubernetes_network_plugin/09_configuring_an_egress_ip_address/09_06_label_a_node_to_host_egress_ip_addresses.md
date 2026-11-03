# 9.6. Label a node to host egress IP addresses

You can apply the `k8s.ovn.org/egress-assignable=""` label to a node in your cluster so that OpenShift Container Platform can assign one or more egress IP addresses to the node. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You logged in to the cluster as a cluster administrator. 



**Procedure**

  * To label a node so that it can host one or more egress IP addresses, enter the following command: 

```shell-session
$ oc label nodes <node_name> k8s.ovn.org/egress-assignable=""
```


`<node_name>`
    

Specifies the name of the node to label. 

Tip

You can alternatively apply the following YAML to add the label to a node: 

```yaml
apiVersion: v1
kind: Node
metadata:
  labels:
    k8s.ovn.org/egress-assignable: ""
  name: <node_name>
```
