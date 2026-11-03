# 3.3. Labeling the existing clusters

To ensure that existing clusters remain untouched by the tool updates, label all existing managed clusters with the `ztp-done` label. 

Note

This procedure only applies when updating clusters that were not provisioned with Topology Aware Lifecycle Manager (TALM). Clusters that you provision with TALM are automatically labeled with `ztp-done`. 

**Procedure**

  1. Find a label selector that lists the managed clusters that were deployed with GitOps Zero Touch Provisioning (ZTP), such as `local-cluster!=true`: 

```shell-session
$ oc get managedcluster -l 'local-cluster!=true'
```


  2. Ensure that the resulting list contains all the managed clusters that were deployed with GitOps ZTP, and then use that selector to add the `ztp-done` label: 

```shell-session
$ oc label managedcluster -l 'local-cluster!=true' ztp-done=
```
