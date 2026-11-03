# 4.2. Hibernating a cluster

Hibernate your cluster by verifying node and Operator health, then stopping the cluster virtual machines. This process pauses the cluster in a supported state so you can resume it later. 

**Prerequisites**

  * The cluster has been running for at least 24 hours to allow the first certificate rotation to complete. 
  * You created an etcd backup before hibernating the cluster. 

Important

Without a recent etcd backup, you might not be able to restore the cluster if hibernation or resume fails. 

  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Confirm that your cluster has been installed for at least 24 hours. 
  2. Ensure that all nodes are in a good state by running the following command: 

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


All nodes should show `Ready` in the `STATUS` column. 

  3. Ensure that all cluster Operators are in a good state by running the following command: 

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

  4. Ensure that all machine config pools are in a good state by running the following command: 

```shell-session
$ oc get mcp
```


**Example output**

```shell-session
NAME    CONFIG                                            UPDATED  UPDATING  DEGRADED  MACHINECOUNT  READYMACHINECOUNT  UPDATEDMACHINECOUNT  DEGRADEDMACHINECOUNT  AGE
master  rendered-master-87871f187930e67233c837e1d07f49c7  True     False     False     3             3                  3                    0                     96m
worker  rendered-worker-3c4c459dc5d90017983d7e72928b8aed  True     False     False     3             3                  3                    0                     96m
```


All machine config pools should show `UPDATING`=`False` and `DEGRADED`=`False`. 

  5. Stop the cluster virtual machines: 

Use the tools native to the cloud environment of your cluster to shut down the cluster virtual machines. 

Important

If you use a bastion virtual machine, do not shut down this virtual machine. 




**Additional resources**

  * [Backing up etcd](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/control-plane-backup-and-restore#backup-etcd "6.1. Backing up and restoring etcd data")
  * [Restoring to an earlier cluster state](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/control-plane-backup-and-restore#dr-restoring-cluster-state "6.4.3. Restoring to an earlier cluster state")
