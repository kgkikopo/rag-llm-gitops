# 4.19. Customize upgrades for kernel modules

The Kernel Module Management (KMM) Operator periodically upgrades `Module` resources in the cluster, typically during a cluster upgrade. 

Use this procedure to upgrade the kernel module while running maintenance operations on the node, including rebooting the node, if needed. To minimize the impact on the workloads running in the cluster, run the kernel upgrade process sequentially, one node at a time. 

Note

This procedure requires knowledge of the workload using the kernel module and must be managed by the cluster administrator. 

**Prerequisites**

  * Before upgrading, set the `kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>=$moduleVersion` label on all the nodes that are used by the kernel module. 
  * End all user application workloads on the node or move them to another node. 
  * Unload the currently loaded kernel module. 
  * Ensure that the user workload (the application running in the cluster that is accessing kernel module) is not running on the node before the kernel module unloads and that the workload is back running on the node after the new kernel module version has been loaded. 



**Procedure**

  1. Ensure that the device plugin managed by KMM on the node is unloaded. 
  2. Update the following fields in the `Module` custom resource (CR): 

     * `containerImage` (to the appropriate kernel version) 
     * `version`

The update should be atomic; that is, both the `containerImage` and `version` fields must be updated simultaneously. 

  3. End any workload using the kernel module on the node being upgraded. 
  4. Remove the `kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>` label on the node. Run the following command to unload the kernel module from the node: 

```shell-session
$ oc label node/<node_name> kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>-
```


  5. If required, as the cluster administrator, perform any additional maintenance required on the node for the kernel module upgrade. 

If no additional upgrading is needed, you can skip Steps 3 through 6 by updating the `kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>` label value to the new `$moduleVersion` as set in the `Module`. 

  6. Run the following command to add the `kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>=$moduleVersion` label to the node. The `$moduleVersion` must be equal to the new value of the `version` field in the `Module` CR. 

```shell-session
$ oc label node/<node_name> kmm.node.kubernetes.io/version-module.<module_namespace>.<module_name>=<desired_version>
```


Note

Because of Kubernetes limitations in label names, the combined length of `Module` name and namespace must not exceed 39 characters. 

The Operator labels the node with a `version.ready` label to indicate that the new version of the kernel module is loaded and is ready to be used: 

**Example output**

```shell-session
`kmm.node.kubernetes.io/<module-namespace>.<module-name>.version.ready=<module-version>`
```


  7. Restore any workload that leverages the kernel module on the node. 
  8. Reload the device plugin managed by KMM on the node.
