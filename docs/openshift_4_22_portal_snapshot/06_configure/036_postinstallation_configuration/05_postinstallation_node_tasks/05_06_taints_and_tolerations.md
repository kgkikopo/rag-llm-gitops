# 5.6. Taints and tolerations

Understand and work with taints and tolerations to control which pods can be scheduled on specific nodes. 

## 5.6.1. Understanding taints and tolerations

You can use a _taint_ on a node to allow that node to refuse a pod to be scheduled unless that pod has a matching _toleration_. 

You apply taints to a node through the `Node` specification (`NodeSpec`) and apply tolerations to a pod through the `Pod` specification (`PodSpec`). When you apply a taint to a node, the scheduler cannot place a pod on that node unless the pod can tolerate the taint. 

**Example taint in a node specification**

```yaml
apiVersion: v1
kind: Node
metadata:
  name: my-node
#...
spec:
  taints:
  - effect: NoExecute
    key: key1
    value: value1
#...
```


**Example toleration in a`Pod` spec**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - key: "key1"
    operator: "Equal"
    value: "value1"
    effect: "NoExecute"
    tolerationSeconds: 3600
#...
```


Taints and tolerations consist of a key, value, and effect. 

Table 5.1. Taint and toleration componentsParameter| Description  
---|---  
`key` |  The `key` is any string, up to 253 characters. The key must begin with a letter or number, and may contain letters, numbers, hyphens, dots, and underscores.   
`value` |  The `value` is any string, up to 63 characters. The value must begin with a letter or number, and may contain letters, numbers, hyphens, dots, and underscores.   
`effect` |  The effect is one of the following:  |  `NoSchedule` [1] | 

  * New pods that do not match the taint are not scheduled onto that node. 
  * Existing pods on the node remain. 

  
---|---  
`PreferNoSchedule` | 

  * New pods that do not match the taint might be scheduled onto that node, but the scheduler tries not to. 
  * Existing pods on the node remain. 

  
`NoExecute` | 

  * New pods that do not match the taint cannot be scheduled onto that node. 
  * Existing pods on the node that do not have a matching toleration are removed. 

  
Show more  
  
`operator` |  |  `Equal` |  The `key`/`value`/`effect` parameters must match. This is the default.   
---|---  
`Exists` |  The `key`/`effect` parameters must match. You must leave a blank `value` parameter, which matches any.   
Show more  
  
Show more

  1. If you add a `NoSchedule` taint to a control plane node, the node must have the `node-role.kubernetes.io/master=:NoSchedule` taint, which is added by default. 

For example: 

```yaml
apiVersion: v1
kind: Node
metadata:
  annotations:
    machine.openshift.io/machine: openshift-machine-api/ci-ln-62s7gtb-f76d1-v8jxv-master-0
    machineconfiguration.openshift.io/currentConfig: rendered-master-cdc1ab7da414629332cc4c3926e6e59c
  name: my-node
#...
spec:
  taints:
  - effect: NoSchedule
    key: node-role.kubernetes.io/master
#...
```


A toleration matches a taint: 

  * If the `operator` parameter is set to `Equal`: 

    * the `key` parameters are the same; 
    * the `value` parameters are the same; 
    * the `effect` parameters are the same. 

  * If the `operator` parameter is set to `Exists`: 

    * the `key` parameters are the same; 
    * the `effect` parameters are the same. 




The following taints are built into OpenShift Container Platform: 

  * `node.kubernetes.io/not-ready`: The node is not ready. This corresponds to the node condition `Ready=False`. 
  * `node.kubernetes.io/unreachable`: The node is unreachable from the node controller. This corresponds to the node condition `Ready=Unknown`. 
  * `node.kubernetes.io/memory-pressure`: The node has memory pressure issues. This corresponds to the node condition `MemoryPressure=True`. 
  * `node.kubernetes.io/disk-pressure`: The node has disk pressure issues. This corresponds to the node condition `DiskPressure=True`. 
  * `node.kubernetes.io/network-unavailable`: The node network is unavailable. 
  * `node.kubernetes.io/unschedulable`: The node is unschedulable. 
  * `node.cloudprovider.kubernetes.io/uninitialized`: When the node controller is started with an external cloud provider, this taint is set on a node to mark it as unusable. After a controller from the cloud-controller-manager initializes this node, the kubelet removes this taint. 
  * `node.kubernetes.io/pid-pressure`: The node has pid pressure. This corresponds to the node condition `PIDPressure=True`. 

Important

OpenShift Container Platform does not set a default pid.available `evictionHard`. 




## 5.6.2. Add taints and tolerations

You can add tolerations to pods and taints to nodes to allow the node to control which pods should or should not be scheduled on that node. 

For existing pods and nodes, you should add the toleration to the pod first, then add the taint to the node to avoid pods being removed from the node before you can add the toleration. 

**Procedure**

  1. Add a toleration to a pod by editing the `Pod` spec to include a `tolerations` stanza: 

**Sample pod configuration file with an Equal operator**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - key: "key1"
    value: "value1"
    operator: "Equal"
    effect: "NoExecute"
    tolerationSeconds: 3600
#...
```


where: 

`spec.tolerations`
     Specifies the toleration parameters, as described in the **Taint and toleration components** table. 
`spec.tolerations.tolerationSeconds``
     Specifies how long a pod can remain bound to a node before being evicted. 

For example: 

**Sample pod configuration file with an Exists operator**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
   tolerations:
    - key: "key1"
      operator: "Exists"
      effect: "NoExecute"
      tolerationSeconds: 3600
#...
```


The `Exists` operator does not take a `value`. 

This example places a taint on `node1` that has key `key1`, value `value1`, and taint effect `NoExecute`. 

  2. Add a taint to a node by using the following command with the parameters described in the **Taint and toleration components** table: 

```shell-session
$ oc adm taint nodes <node_name> <key>=<value>:<effect>
```


For example: 

```shell-session
$ oc adm taint nodes node1 key1=value1:NoExecute
```


This command places a taint on `node1` that has key `key1`, value `value1`, and effect `NoExecute`. 

Note

If you add a `NoSchedule` taint to a control plane node, the node must have the `node-role.kubernetes.io/master=:NoSchedule` taint, which is added by default. 

For example: 

```yaml
apiVersion: v1
kind: Node
metadata:
  annotations:
    machine.openshift.io/machine: openshift-machine-api/ci-ln-62s7gtb-f76d1-v8jxv-master-0
    machineconfiguration.openshift.io/currentConfig: rendered-master-cdc1ab7da414629332cc4c3926e6e59c
  name: my-node
#...
spec:
  taints:
  - effect: NoSchedule
    key: node-role.kubernetes.io/master
#...
```


The tolerations on the pod match the taint on the node. A pod with either toleration can be scheduled onto `node1`. 




## 5.6.3. Add taints and tolerations using a compute machine set

You can add taints to groups of nodes by using a compute machine set. All nodes associated with the `MachineSet` object are updated with the taint. 

Tolerations respond to taints added by a compute machine set in the same manner as taints added directly to the nodes. 

**Procedure**

  1. Add a toleration to a pod by editing the `Pod` spec to include a `tolerations` stanza: 

**Sample pod configuration file with`Equal` operator**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - key: "key1"
    value: "value1"
    operator: "Equal"
    effect: "NoExecute"
    tolerationSeconds: 3600
#...
```


where: 

`spec.tolerations`
     Specifies the toleration parameters, as described in the **Taint and toleration components** table. 
`spec.tolerations.tolerationSeconds`
     Specifies how long a pod can remain bound to a node before being evicted. 

For example: 

**Sample pod configuration file with`Exists` operator**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - key: "key1"
    operator: "Exists"
    effect: "NoExecute"
    tolerationSeconds: 3600
#...
```


  2. Add the taint to the `MachineSet` object: 

     1. Edit the `MachineSet` YAML for the nodes you want to taint or you can create a new `MachineSet` object: 

```shell-session
$ oc edit machineset <machineset>
```


     2. Add the taint to the `spec.template.spec` section: 

**Example taint in a compute machine set specification**

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: my-machineset
#...
spec:
#...
  template:
#...
    spec:
      taints:
      - effect: NoExecute
        key: key1
        value: value1
#...
```


This example places a taint that has the key `key1`, value `value1`, and taint effect `NoExecute` on the nodes. 

     3. Scale down the compute machine set to 0: 

```shell-session
$ oc scale --replicas=0 machineset <machineset> -n openshift-machine-api
```


Tip

You can alternatively apply the following YAML to scale the compute machine set: 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  name: <machineset>
  namespace: openshift-machine-api
spec:
  replicas: 0
```


Wait for the machines to be removed. 

     4. Scale up the compute machine set as needed: 

```shell-session
$ oc scale --replicas=2 machineset <machineset> -n openshift-machine-api
```


Or: 

```shell-session
$ oc edit machineset <machineset> -n openshift-machine-api
```


Wait for the machines to start. The taint is added to the nodes associated with the `MachineSet` object. 




## 5.6.4. Bind a user to a node using taints and tolerations

You can use taints and tolerations to dedicate a set of nodes for exclusive use by a particular set of users. 

First, add a toleration to their pods. Then, add a corresponding taint to those nodes. The pods with the tolerations are allowed to use the tainted nodes or any other nodes in the cluster. 

If you want ensure the pods are scheduled to only those tainted nodes, also add a label to the same set of nodes and add a node affinity to the pods so that the pods can only be scheduled onto nodes with that label. 

Use the following procedure to configure a node so that users can use only that node. 

**Procedure**

  1. Add a corresponding taint to those nodes: 

For example: 

```shell-session
$ oc adm taint nodes node1 dedicated=groupName:NoSchedule
```


Tip

You can alternatively apply the following YAML to add the taint: 

```yaml
kind: Node
apiVersion: v1
metadata:
  name: my-node
#...
spec:
  taints:
    - key: dedicated
      value: groupName
      effect: NoSchedule
#...
```


  2. Add a toleration to the pods by writing a custom admission controller. 



## 5.6.5. Control nodes with special hardware using taints and tolerations

In a cluster that has specialized hardware, you can use taints and tolerations to either keep pods that do not need the specialized hardware off of those nodes or require pods that need specialized hardware to use specific nodes. 

You can achieve this by adding a toleration to pods that need the special hardware and tainting the nodes that have the specialized hardware. 

Use the following procedure to ensure nodes with specialized hardware are reserved for specific pods. 

**Procedure**

  1. Add a toleration to pods that need the special hardware. 

For example: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
    - key: "disktype"
      value: "ssd"
      operator: "Equal"
      effect: "NoSchedule"
      tolerationSeconds: 3600
#...
```


  2. Taint the nodes that have the specialized hardware using one of the following commands: 

```shell-session
$ oc adm taint nodes <node-name> disktype=ssd:NoSchedule
```


Or: 

```shell-session
$ oc adm taint nodes <node-name> disktype=ssd:PreferNoSchedule
```


Tip

You can alternatively apply the following YAML to add the taint: 

```yaml
kind: Node
apiVersion: v1
metadata:
  name: my_node
#...
spec:
  taints:
    - key: disktype
      value: ssd
      effect: PreferNoSchedule
#...
```


## 5.6.6. Remove taints and tolerations

You can remove taints from nodes and tolerations from pods as needed if you no longer want the scheduling behavior. 

You should add the toleration to the pod first, then add the taint to the node to avoid pods being removed from the node before you can add the toleration. 

Use the following procedure to remove taints and tolerations. 

**Procedure**

  1. To remove a taint from a node: 

```shell-session
$ oc adm taint nodes <node-name> <key>-
```


For example: 

```shell-session
$ oc adm taint nodes ip-10-0-132-248.ec2.internal key1-
```


**Example output**

```shell-session
node/ip-10-0-132-248.ec2.internal untainted
```


  2. To remove a toleration from a pod, edit the `Pod` spec to remove the toleration: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
#...
spec:
  tolerations:
  - key: "key2"
    operator: "Exists"
    effect: "NoExecute"
    tolerationSeconds: 3600
#...
```
