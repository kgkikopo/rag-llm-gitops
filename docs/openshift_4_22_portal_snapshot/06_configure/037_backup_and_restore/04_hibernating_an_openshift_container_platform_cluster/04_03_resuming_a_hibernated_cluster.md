# 4.3. Resuming a hibernated cluster

Resume a hibernated cluster by starting the cluster virtual machines and approving certificate signing requests (CSRs) as needed. This process restores the cluster to a ready state within the supported 90-day window. 

It can take around 45 minutes for the cluster to resume, depending on the size of your cluster. 

**Prerequisites**

  * You hibernated your cluster less than 90 days ago. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Within 90 days of cluster hibernation, resume the cluster virtual machines: 

Use the tools native to the cloud environment of your cluster to resume the cluster virtual machines. 

  2. Wait about 5 minutes, depending on the number of nodes in your cluster. 
  3. Approve CSRs for the nodes: 

     1. Check that there is a CSR for each node in the `NotReady` state by running the following command: 

```shell-session
$ oc get csr
```


**Example output**

```shell-session
NAME       AGE  SIGNERNAME                                   REQUESTOR                                                                  REQUESTEDDURATION  CONDITION
csr-4dwsd  37m  kubernetes.io/kube-apiserver-client          system:node:ci-ln-812tb4k-72292-8bcj7-worker-c-q8mw2                       24h                Pending
csr-4vrbr  49m  kubernetes.io/kube-apiserver-client          system:node:ci-ln-812tb4k-72292-8bcj7-master-1                             24h                Pending
csr-4wk5x  51m  kubernetes.io/kubelet-serving                system:node:ci-ln-812tb4k-72292-8bcj7-master-1                             <none>             Pending
csr-84vb6  51m  kubernetes.io/kube-apiserver-client-kubelet  system:serviceaccount:openshift-machine-config-operator:node-bootstrapper  <none>             Pending
```


     2. Approve each valid CSR by running the following command: 

```shell-session
$ oc adm certificate approve <csr_name>
```


     3. Verify that all necessary CSRs were approved by running the following command: 

```shell-session
$ oc get csr
```


**Example output**

```shell-session
NAME       AGE  SIGNERNAME                                   REQUESTOR                                                                  REQUESTEDDURATION  CONDITION
csr-4dwsd  37m  kubernetes.io/kube-apiserver-client          system:node:ci-ln-812tb4k-72292-8bcj7-worker-c-q8mw2                       24h                Approved,Issued
csr-4vrbr  49m  kubernetes.io/kube-apiserver-client          system:node:ci-ln-812tb4k-72292-8bcj7-master-1                             24h                Approved,Issued
csr-4wk5x  51m  kubernetes.io/kubelet-serving                system:node:ci-ln-812tb4k-72292-8bcj7-master-1                             <none>             Approved,Issued
csr-84vb6  51m  kubernetes.io/kube-apiserver-client-kubelet  system:serviceaccount:openshift-machine-config-operator:node-bootstrapper  <none>             Approved,Issued
```


CSRs should show `Approved,Issued` in the `CONDITION` column. 

  4. Verify that all nodes now show as ready by running the following command: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME                                      STATUS  ROLES                 AGE   VERSION
ci-ln-812tb4k-72292-8bcj7-master-0        Ready	  control-plane,master  32m   v1.35.4
ci-ln-812tb4k-72292-8bcj7-master-1        Ready	  control-plane,master  32m   v1.35.4
ci-ln-812tb4k-72292-8bcj7-master-2        Ready	  control-plane,master  32m   v1.35.4
Ci-ln-812tb4k-72292-8bcj7-worker-a-zhdvk  Ready	  worker                19m   v1.35.4
ci-ln-812tb4k-72292-8bcj7-worker-b-9hrmv  Ready	  worker                19m   v1.35.4
ci-ln-812tb4k-72292-8bcj7-worker-c-q8mw2  Ready	  worker                19m   v1.35.4
```


All nodes should show `Ready` in the `STATUS` column. It might take a few minutes for all nodes to become ready after approving the CSRs. 

  5. Wait for cluster Operators to restart to load the new certificates. 

This might take 5 or 10 minutes. 

  6. Verify that all cluster Operators are in a good state by running the following command: 

```shell-session
$ oc get clusteroperators
```


**Example output**

```shell-session
NAME                      VERSION   AVAILABLE  PROGRESSING  DEGRADED  SINCE   MESSAGE
authentication            4.22.0-0  True       False        False     51m
baremetal                 4.22.0-0  True       False        False     72m
cloud-controller-manager  4.22.0-0  True       False        False     75m
cloud-credential          4.22.0-0  True       False        False     77m
cluster-api               4.22.0-0  True       False        False     42m
cluster-autoscaler        4.22.0-0  True       False        False     72m
config-operator           4.22.0-0  True       False        False     72m
console                   4.22.0-0  True       False        False     55m
...
```


All cluster Operators should show `AVAILABLE`=`True`, `PROGRESSING`=`False`, and `DEGRADED`=`False`.
