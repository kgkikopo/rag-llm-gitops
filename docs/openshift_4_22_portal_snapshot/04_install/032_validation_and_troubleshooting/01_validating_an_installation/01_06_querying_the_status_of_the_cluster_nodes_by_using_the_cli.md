# 1.6. Querying the status of the cluster nodes by using the CLI

You can verify the status of the cluster nodes after an installation. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. List the status of the cluster nodes by entering the following command: 

```shell-session
$ oc get nodes
```


  2. Verify that the output lists all of the expected control plane and compute nodes and that each node has a `Ready` status: 

**Example output**

```shell-session
NAME                          STATUS   ROLES    AGE   VERSION
compute-1.example.com         Ready    worker   33m   v1.35.4
control-plane-1.example.com   Ready    master   41m   v1.35.4
control-plane-2.example.com   Ready    master   45m   v1.35.4
compute-2.example.com         Ready    worker   38m   v1.35.4
compute-3.example.com         Ready    worker   33m   v1.35.4
control-plane-3.example.com   Ready    master   41m   v1.35.4
```


  3. Review CPU and memory resource availability for each cluster node: 

```shell-session
$ oc adm top nodes
```


**Example output**

```shell-session
NAME                          CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
compute-1.example.com         128m         8%     1132Mi          16%
control-plane-1.example.com   801m         22%    3471Mi          23%
control-plane-2.example.com   1718m        49%    6085Mi          40%
compute-2.example.com         935m         62%    5178Mi          75%
compute-3.example.com         111m         7%     1131Mi          16%
control-plane-3.example.com   942m         26%    4100Mi          27%
```


**Additional resources**

  * [Verifying node health](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#verifying-node-health)
