# 15.7. Pausing the reconciliation of a hosted cluster and hosted control plane

If you are a cluster instance administrator, you can pause the reconciliation of a hosted cluster and hosted control plane. You might want to pause reconciliation when you back up and restore an etcd database or when you need to debug problems with a hosted cluster or hosted control plane. 

**Procedure**

  1. To pause reconciliation for a hosted cluster and hosted control plane, populate the `pausedUntil` field of the `HostedCluster` resource. 

     * To pause the reconciliation until a specific time, enter the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  hostedclusters/<hosted_cluster_name> \
  -p '{"spec":{"pausedUntil":"<timestamp>"}}' \
  --type=merge
```


Replace `<timestamp>` with a timestamp in the RFC339 format; for example, `2024-03-03T03:28:48Z`. The reconciliation is paused until the specified time is passed. 

     * To pause the reconciliation indefinitely, enter the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  hostedclusters/<hosted_cluster_name> \
  -p '{"spec":{"pausedUntil":"true"}}' \
  --type=merge
```


The reconciliation is paused until you remove the field from the `HostedCluster` resource. 

When the pause reconciliation field is populated for the `HostedCluster` resource, the field is automatically added to the associated `HostedControlPlane` resource. 

  2. To remove the `pausedUntil` field, enter the following patch command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  hostedclusters/<hosted_cluster_name> \
  -p '{"spec":{"pausedUntil":null}}' \
  --type=merge
```
