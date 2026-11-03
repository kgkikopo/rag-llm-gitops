# 10.2. Adding an out-of-service taint manually for automatic volume detachment

After non-graceful shutdowns, to trigger automatic volume detachment and enable pod rescheduling, apply an out-of-service taint to the node. This recovers workloads faster than manually detaching volumes from failed nodes. 

**Prerequisites**

  * Access to the cluster with cluster-admin privileges. 



**Procedure**

  1. After a node is detected as unhealthy, shut down the worker node. 
  2. Ensure that the node is shutdown by running the following command and checking the status: 

```shell-session
$ oc get node <node_name>
```


     * Use the `<node_name>` to specify the node that shut down non-gracefully. 

Important

If the node is not completely shut down, do not proceed with tainting the node. If the node is still up and the taint is applied, filesystem corruption can occur. 

  3. Taint the corresponding node object by running the following command: 

Important

Tainting a node this way deletes all pods on that node. This also causes any pods that are backed by statefulsets to be evicted, and replacement pods to be created on a different node. 

```shell-session
$ oc adm taint node <node_name> node.kubernetes.io/out-of-service=nodeshutdown:NoExecute
```


     * Use the `<node_name>` to specify the node that shut down non-gracefully. 

After the taint is applied, the volumes detach from the shutdown node allowing their disks to be attached to a different node. 

The resulting YAML file resembles the following example file: 

**Example node YAML file with out-of-service taint applied**

```yaml
spec:
  taints:
  - effect: NoExecute
    key: node.kubernetes.io/out-of-service
    value: nodeshutdown
```


  4. Restart the node. 
  5. Remove the taint from the corresponding node object by running the following command: 

```shell-session
$ oc adm taint node <node_name> node.kubernetes.io/out-of-service=nodeshutdown:NoExecute-
```


     * Use the `<node_name>` to specify the node that shut down non-gracefully
