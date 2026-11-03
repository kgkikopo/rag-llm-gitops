# 15.3. Deleting all destinations for network flows collectors

As a cluster administrator, you can configure the Cluster Network Operator (CNO) to stop sending network flows metadata to a network flows collector. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You are logged in to the cluster with a user with `cluster-admin` privileges. 



**Procedure**

  1. Remove all network flows collectors: 

```shell-session
$ oc patch network.operator cluster --type='json' \
    -p='[{"op":"remove", "path":"/spec/exportNetworkFlows"}]'
```


**Example output**

```shell-session
network.operator.openshift.io/cluster patched
```
