# 1.6. About node status during updates

If you make changes to a machine config pool (MCP) that results in a new machine config, for example by using a `MachineConfig` or `KubeletConfig` object, you can get detailed information about the progress of the node updates by using the machine config nodes custom resource. 

This information can be helpful if issues arise during the update and you need to troubleshoot a node. 

The `MachineConfigNode` custom resource allows you to monitor the progress of individual node updates as they move through the update phases. This information can be helpful with troubleshooting if one of the nodes has an issue during the update. The custom resource reports where in the update process the node is at the moment, the phases that have completed, and the phases that are remaining. 

The node update process consists of the following phases and subphases that are tracked by the machine config node custom resource, explained with more detail later in this section: 

  * **Update Prepared**. The MCO stops the configuration drift monitoring process and verifies that the newly-created machine config can be applied to a node. 
  * **Update Executed**. The MCO cordons and drains the node and applies the new machine config to the node files and operating system, as needed. It contains the following sub-phases: 

    * **Cordoned**. The MCO cordoned the node. 
    * **Drained**. The MCO drained the node. 
    * **AppliedFilesAndOS**. The MCO has updated the node files and operating system. 
    * **AppliedFiles**. The MCO has updated the node files. 
    * **AppliedOSImage**. The MCO has updated the operating system. 

In order to see **AppliedFiles** and **AppliedOSImage** in the output, you must enable the `TechPreviewNoUpgrade` feature set on the cluster. These conditions replace **AppliedFilesAndOS**. For more information, see "Enabling features using feature gates". 

Note

Enabling the `TechPreviewNoUpgrade` feature set cannot be undone and prevents minor version updates. These feature sets are not recommended on production clusters. 

Important

The `AppliedFiles` and `AppliedOSImage` condition is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

  * **PinnedImageSetsProgressing** The MCO is performing the steps needed to pin and pre-load container images. 
  * **PinnedImageSetsDegraded** The pinned image process failed. You can view the reason for the failure by using the `oc describe machineconfignode` command, as described later in this section. 
  * **NodeDegraded** The node update failed. You can view the reason for the failure by using the `oc describe machineconfignode` command, as described later in this section. 
  * **Update Post update action** The MCO is reloading CRI-O, as needed. 
  * **Rebooted Node** The MCO is rebooting the node, as needed. 
  * **Update Complete**. The MCO is uncordoning the node, updating the node state to the cluster, and resumes producing node metrics. It contains the following sub-phase: 

    * **Uncordoned**

  * **Updated** The MCO completed a node update and the current config version of the node is equal to the desired updated version. 
  * **Resumed**. The MCO restarted the config drift monitor process and the node returns to operational state. 
  * **ImagePulledFromRegistry**. The MCO has pulled the desired custom layered image. This condition applies only to nodes on which on-cluster image mode has been configured. 

In order to see **ImagePulledFromRegistry** in the output, you must enable the `TechPreviewNoUpgrade` feature set on the cluster. For more information, see "Enabling features using feature gates". 

Note

Enabling the `TechPreviewNoUpgrade` feature set cannot be undone and prevents minor version updates. These feature sets are not recommended on production clusters. 

Important

The `ImagePulledFromRegistry` condition is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 




As the update moves through these phases, you can query the `MachineConfigNode` custom resource, which reports one of the following conditions for each phase: 

  * `True`. The phase is complete on that node. 
  * `False`. The phase has not yet started or will not be executed on that node. 
  * `Unknown`. The phase is either being executed on that node or has an error. If the phase has an error, you can use the `oc describe machineconfignodes` command for more information, as described later in this section. 



For example, consider a cluster with a newly-created machine config: 

```shell-session
$ oc get machineconfig
```


**Example output**

```plaintext
NAME                                               GENERATEDBYCONTROLLER                      IGNITIONVERSION   AGE
# ...
rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   c00e2c941bc6e236b50e0bf3988e6c790cf2bbb2   3.5.0             6d15h
rendered-master-a386c2d1550b927d274054124f58be68   c00e2c941bc6e236b50e0bf3988e6c790cf2bbb2   3.5.0             7m26s
# ...
rendered-worker-01f27f752eb84eba917450e43636b210   c00e2c941bc6e236b50e0bf3988e6c790cf2bbb2   3.5.0             6d15h
rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   c00e2c941bc6e236b50e0bf3988e6c790cf2bbb2   3.5.0             7m26s
# ...
```


In this example, the current machine config for the worker nodes is listed before the newly-created machine config, which is being applied to the worker nodes. 

You can watch as the nodes are updated with the new machine config: 

```shell-session
$ oc get machineconfignodes
```


**Example output**

```plaintext
NAME                                       POOLNAME      DESIREDCONFIG                                      CURRENTCONFIG                                      UPDATED   AGE
ci-ln-ds73n5t-72292-9xsm9-master-0         master        rendered-master-a386c2d1550b927d274054124f58be68   rendered-master-a386c2d1550b927d274054124f58be68   True      27M
ci-ln-ds73n5t-72292-9xsm9-master-1         master        rendered-master-a386c2d1550b927d274054124f58be68   rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   False     27M
ci-ln-ds73n5t-72292-9xsm9-master-2         master        rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   True      27M
ci-ln-ds73n5t-72292-9xsm9-worker-a-2d8tz   worker-cnf    rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   True      20M
ci-ln-ds73n5t-72292-9xsm9-worker-b-gw5sd   worker        rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   rendered-worker-01f27f752eb84eba917450e43636b210   False     20M
ci-ln-ds73n5t-72292-9xsm9-worker-c-t227w   worker        rendered-worker-01f27f752eb84eba917450e43636b210   rendered-worker-01f27f752eb84eba917450e43636b210   True      19M
```


In this example, the `ci-ln-ds73n5t-72292-9xsm9-worker-a-2d8tz` node has been updated. The new machine config, `rendered-worker-f351f6947f15cd0380514f4b1c89f8f2`, is shown as the desired and current machine configs. 

The `ci-ln-ds73n5t-72292-9xsm9-worker-b-gw5sd` node is currently being updated to the new machine config. The previous and new machine configs are shown as the desired and current machine configs, respectively. 

The `ci-ln-ds73n5t-72292-9xsm9-worker-c-t227w` node has not yet been updated to the new machine config. The previous machine config is shown as the desired and current machine configs. 

Table 1.1. Basic machine config node fieldsField| Meaning  
---|---  
`NAME` |  The name of the node.   
`POOLNAME` |  The name of the machine config pool associated with that node.   
`DESIREDCONFIG` |  The name of the new machine config that the node updates to.   
`CURRENTCONFIG` |  The name of the current machine configuration on that node.   
`UPDATED` |  Indicates if the node has been updated by using one of the following conditions: 

  * If `False`, the node is being updated to the new machine configuration shown in the `DESIREDCONFIG` field. 
  * If `True`, and the `CURRENTCONFIG` matches the new machine configuration shown in the `DESIREDCONFIG` field, the node has been updated. 
  * If `True`, and the `CURRENTCONFIG` matches the old machine configuration shown in the `DESIREDCONFIG` field, that node has not been updated yet. 

  
`AGE` |  The age of the machine configuration node from when it was created. The age is not changed if the associated node is updated.   
Show more

You can use the `-o wide` flag to display additional information about the updates: 

```shell-session
$ oc get machineconfignodes -o wide
```


**Example output**

```plaintext
NAME                                       POOLNAME    DESIREDCONFIG                                      CURRENTCONFIG                                         UPDATED   AGE   UPDATEPREPARED   UPDATEEXECUTED   UPDATEPOSTACTIONCOMPLETE   UPDATECOMPLETE   RESUMED   UPDATEDFILESANDOS   CORDONEDNODE   DRAINEDNODE   REBOOTEDNODE   UNCORDONEDNODE
ci-ln-ds73n5t-72292-9xsm9-master-0         master      rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   rendered-master-23cf200e4ee97daa6e39fdce24c9fb67      True      27M   False            False            False                      False            False     False               False          False         False          False
ci-ln-ds73n5t-72292-9xsm9-master-1         master      rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   rendered-master-23cf200e4ee97daa6e39fdce24c9fb67      True      27M   False            False            False                      False            False     False               False          False         False          False
ci-ln-ds73n5t-72292-9xsm9-master-2         master      rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   rendered-master-23cf200e4ee97daa6e39fdce24c9fb67      True      27M   False            False            False                      False            False     False               False          False         False          False
ci-ln-ds73n5t-72292-9xsm9-worker-a-2d8tz   worker-cnf  rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   rendered-worker-f351f6947f15cd0380514f4b1c89f8f2      True      20M   False            False            False                      False            False     False               False          False         False          False
ci-ln-ds73n5t-72292-9xsm9-worker-b-gw5sd   worker      rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   rendered-worker-01f27f752eb84eba917450e43636b210      False     20M   True             True             Unknown                    False            False     True                True           True          Unknown        False
ci-ln-ds73n5t-72292-9xsm9-worker-c-t227w   worker      rendered-worker-01f27f752eb84eba917450e43636b210   rendered-worker-01f27f752eb84eba917450e43636b210      True      19M   False            False            False                      False            False     False               False          False         False          False
```


In addition to the fields defined in the previous table, the `-o wide` output displays the following fields: 

Table 1.2. Machine config node fields in the -o wide outputPhase Name| Definition  
---|---  
`UPDATEPREPARED` |  Indicates if the MCO is preparing to update the node.   
`UPDATEEXECUTED` |  Indicates if the MCO has completed the body of the update on the node.   
`UPDATEPOSTACTIONCOMPLETE` |  Indicates if the MCO has executed the post-update actions on the node.   
`UPDATECOMPLETE` |  Indicates if the MCO has completed the update on the node.   
`RESUMED` |  Indicates if the node has resumed normal processes.   
`UPDATEDFILESANDOS` |  Indicates if the MCO has updated the node files and operating system.   
`CORDONEDNODE` |  Indicates if the MCO has marked the node as not schedulable.   
`DRAINEDNODE` |  Indicates if the MCO has drained the node.   
`REBOOTEDNODE` |  Indicates if the MCO has restarted the node.   
`UNCORDONEDNODE` |  Indicates if the MCO has marked the node as schedulable.   
Show more

For more details on the update status, you can use the `oc describe machineconfignode` command: 

```shell-session
$ oc describe machineconfignode/<machine_config_node_name>
```


**Example output**

```plaintext
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigNode
metadata:
  creationTimestamp: "2025-04-28T18:40:29Z"
  generation: 3
  name: <machine_config_node_name>
# ...
spec:
  configVersion:
    desired: rendered-master-34f96af2e41acb615410b97ce1c819e6
  node:
    name: ci-ln-921r7qk-72292-kxv95-master-0
  pool:
    name: master
status:
  conditions:
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: All pinned image sets complete
    reason: AsExpected
    status: "False"
    type: PinnedImageSetsProgressing
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the UpdatePrepared phase
    reason: NotYetOccurred
    status: "False"
    type: UpdatePrepared
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the UpdateExecuted phase
    reason: NotYetOccurred
    status: "False"
    type: UpdateExecuted
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the UpdatePostActionComplete phase
    reason: NotYetOccurred
    status: "False"
    type: UpdatePostActionComplete
  - lastTransitionTime: "2025-04-28T18:42:08Z"
    message: 'Action during update to rendered-master-34f96af2e41acb615410b97ce1c819e6:
      Uncordoned Node as part of completing upgrade phase'
    reason: Uncordoned
    status: "False"
    type: UpdateComplete
  - lastTransitionTime: "2025-04-28T18:42:08Z"
    message: 'Action during update to rendered-master-34f96af2e41acb615410b97ce1c819e6:
      In desired config . Resumed normal operations.'
    reason: Resumed
    status: "False"
    type: Resumed
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the Drained phase
    reason: NotYetOccurred
    status: "False"
    type: Drained
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the AppliedFilesAndOS phase
    reason: NotYetOccurred
    status: "False"
    type: AppliedFilesAndOS
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the Cordoned phase
    reason: NotYetOccurred
    status: "False"
    type: Cordoned
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the RebootedNode phase
    reason: NotYetOccurred
    status: "False"
    type: RebootedNode
  - lastTransitionTime: "2025-04-28T18:42:08Z"
    message: Node ci-ln-921r7qk-72292-kxv95-master-0 Updated
    reason: Updated
    status: "True"
    type: Updated
  - lastTransitionTime: "2025-04-28T18:42:08Z"
    message: 'Action during update to rendered-master-34f96af2e41acb615410b97ce1c819e6:
      UnCordoned node. The node is reporting Unschedulable = false'
    reason: UpdateCompleteUncordoned
    status: "False"
    type: Uncordoned
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the NodeDegraded phase
    reason: NotYetOccurred
    status: "False"
    type: NodeDegraded
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: All is good
    reason: AsExpected
    status: "False"
    type: PinnedImageSetsDegraded
  configVersion:
    current: rendered-master-34f96af2e41acb615410b97ce1c819e6
    desired: rendered-master-34f96af2e41acb615410b97ce1c819e6
  observedGeneration: 4
```


where: 

`metadata.name`
     Specifies the `MachineConfigNode` object name. 
`spec.configVersion.desired`
     Specifies the new machine configuration. This field updates after the MCO validates the machine config in the `UPDATEPREPARED` phase, and then the status adds the new configuration. 
`status.configVersion.current`
     Specifies the current machine config on the node. 

For clusters configured with on-cluster image mode, the machine config node output also includes the name of the custom layered image that was applied to affected nodes. 

**Example machine config node output**

```shell-session
Name:         ip-10-0-14-86.us-west-1.compute.internal
API Version:  machineconfiguration.openshift.io/v1
Kind:         MachineConfigNode
# ...
Spec:
  Config Image:
    Desired Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
  Config Version:
    Desired:  rendered-worker-d63c7736923b60b8b82492ae9a1eef40
  Node:
    Name:  ip-10-0-14-86.us-west-1.compute.internal
  Pool:
    Name:  worker
# ...
Status:
  Conditions:
# ...
    Message:               Action during update to image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3: Successfully pulled OS image image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3 from registry
    Reason:                ImagePulledFromRegistry
    Status:                False
    Type:                  ImagePulledFromRegistry
# ...
  Config Image:
    Current Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
    Desired Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
# ...
```


The digested image pull spec for the new custom layered image is in the `Spec.Config Image.Desired Image` parameter. 

In order to see the custom layered image in the output, you must enable the `TechPreviewNoUpgrade` feature set on the cluster. For more information, see "Enabling features using feature gates". 

Note

Enabling the `TechPreviewNoUpgrade` feature set cannot be undone and prevents minor version updates. These feature sets are not recommended on production clusters. 

Important

The custom layered image output is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

## 1.6.1. Check node status during updates

During the update of a machine config pool (MCP), you can monitor the progress of all of the nodes in your cluster by using the `oc get machineconfignodes` and `oc describe machineconfignodes` commands. 

These commands provide information that can be helpful if issues arise during the update and you need to troubleshoot a node. 

For more information on the meaning of these fields, see "About checking machine config node status." 

**Prerequisites**

  * In order to see specific machine config node output, as described in "About checking machine config node status", you must enable the `TechPreviewNoUpgrade` feature set on the cluster. For more information, see "Enabling features using feature gates". 

Note

Enabling the `TechPreviewNoUpgrade` feature set cannot be undone and prevents minor version updates. These feature sets are not recommended on production clusters. 

Important

The custom layered image output is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 




**Procedure**

  * View the update status of all nodes in the cluster, including the current and desired machine configurations, by running the following command: 

```shell-session
$ oc get machineconfignodes
```


**Example output**

```plaintext
NAME                                       POOLNAME   DESIREDCONFIG                                      CURRENTCONFIG                                      UPDATED   AGE
ci-ln-mdb23yt-72292-kzdsg-master-0         master     rendered-master-f21b093d20f68a7c06f922ed3ea5fbc8   rendered-master-1abc053eec29e6c945670f39d6dc8afa   False     27M
ci-ln-mdb23yt-72292-kzdsg-master-1         master     rendered-master-1abc053eec29e6c945670f39d6dc8afa   rendered-master-1abc053eec29e6c945670f39d6dc8afa   True      27M
ci-ln-mdb23yt-72292-kzdsg-master-2         master     rendered-master-1abc053eec29e6c945670f39d6dc8afa   rendered-master-1abc053eec29e6c945670f39d6dc8afa   True      27M
ci-ln-mdb23yt-72292-kzdsg-worker-a-gfqjr   worker     rendered-worker-d0130cd74e9e576d7ba78ce166272bfb   rendered-worker-8f61bf839898a4487c3b5263a430e94a   False     20M
ci-ln-mdb23yt-72292-kzdsg-worker-b-gknq4   worker     rendered-worker-8f61bf839898a4487c3b5263a430e94a   rendered-worker-8f61bf839898a4487c3b5263a430e94a   True      20M
ci-ln-mdb23yt-72292-kzdsg-worker-c-mffrx   worker     rendered-worker-8f61bf839898a4487c3b5263a430e94a   rendered-worker-8f61bf839898a4487c3b5263a430e94a   True      19M
```


  * View of all machine config node status fields for the nodes in your cluster by running the following command: 

```shell-session
$ oc get machineconfignodes -o wide
```


**Example output**

```plaintext
NAME                                       POOLNAME   DESIREDCONFIG                                      CURRENTCONFIG                                      UPDATED   AGE   UPDATEPREPARED   UPDATEEXECUTED   UPDATEPOSTACTIONCOMPLETE   UPDATECOMPLETE   RESUMED   UPDATEDFILESANDOS   CORDONEDNODE   DRAINEDNODE   REBOOTEDNODE   UNCORDONEDNODE
ci-ln-g6dr34b-72292-g9btv-master-0         master     rendered-master-d4e122320b351cdbe1df59ddb63ddcfc   rendered-master-6f2064fcb36d2a914de5b0c660dc49ff   False     27M   True             Unknown          False                      False            False     Unknown             False          False         False          False
ci-ln-g6dr34b-72292-g9btv-master-1         master     rendered-master-6f2064fcb36d2a914de5b0c660dc49ff   rendered-master-6f2064fcb36d2a914de5b0c660dc49ff   True      27M   False            False            False                      False            False     False               False          False         False          False
ci-ln-g6dr34b-72292-g9btv-master-2         master     rendered-master-6f2064fcb36d2a914de5b0c660dc49ff   rendered-master-6f2064fcb36d2a914de5b0c660dc49ff   True      27M   False            False            False                      False            False     False               False          False         False          False
ci-ln-g6dr34b-72292-g9btv-worker-a-sjh5r   worker     rendered-worker-671b88c8c569fa3f60dc1a27cf9c91f2   rendered-worker-d5534cb730e5e108905fc285c2a42b6c   False     20M   True             Unknown          False                      False            False     Unknown             False          False         False          False
ci-ln-g6dr34b-72292-g9btv-worker-b-xthbz   worker     rendered-worker-d5534cb730e5e108905fc285c2a42b6c   rendered-worker-d5534cb730e5e108905fc285c2a42b6c   True      20M   False            False            False                      False            False     False               False          False         False          False
ci-ln-g6dr34b-72292-g9btv-worker-c-gnpd6   worker     rendered-worker-d5534cb730e5e108905fc285c2a42b6c   rendered-worker-d5534cb730e5e108905fc285c2a42b6c   True      19M   False            False            False                      False            False     False               False          False         False          False
```


  * Check the update status of nodes in a specific machine config pool by running the following command: 

```shell-session
$ oc get machineconfignodes $(oc get machineconfignodes -o json | jq -r '.items[]|select(.spec.pool.name=="<pool_name>")|.metadata.name') 
```


1

```shell-session

```


where: 

`<pool_name>`
    

Specifies the name of the machine config pool. 

**Example output**

```plaintext
NAME                                       POOLNAME   DESIREDCONFIG                                      CURRENTCONFIG                                      UPDATED   AGE
ci-ln-g6dr34b-72292-g9btv-worker-a-sjh5r   worker     rendered-worker-d5534cb730e5e108905fc285c2a42b6c   rendered-worker-d5534cb730e5e108905fc285c2a42b6c   True      20M
ci-ln-g6dr34b-72292-g9btv-worker-b-xthbz   worker     rendered-worker-d5534cb730e5e108905fc285c2a42b6c   rendered-worker-faf6b50218a8bbce21f1370866283de5   False     20M
ci-ln-g6dr34b-72292-g9btv-worker-c-gnpd6   worker     rendered-worker-faf6b50218a8bbce21f1370866283de5   rendered-worker-faf6b50218a8bbce21f1370866283de5   True      19M
```


  * Check the update status of an individual node by running the following command: 

```shell-session
$ oc describe machineconfignode/<node_name>
```


**Example output**

```plaintext
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigNode
metadata:
  creationTimestamp: "2025-04-28T18:52:16Z"
  generation: 3
  name: ci-ln-921r7qk-72292-kxv95-worker-a-zmxrr
  ownerReferences:
  - apiVersion: v1
    kind: Node
    name: ci-ln-921r7qk-72292-kxv95-worker-a-zmxrr
    uid: e548a8d1-4f16-42cd-9234-87ac5aede6c1
  resourceVersion: "62331"
  uid: 11d96e07-582d-4569-a84a-9d8c5229a551
spec:
  configVersion:
    desired: rendered-worker-1930ca7433b7f0153286a3f04e4cb57b
  node:
    name: ci-ln-921r7qk-72292-kxv95-worker-a-zmxrr
  pool:
    name: worker
status:
  conditions:
# ...
    lastTransitionTime: 2025-04-23T14:55:31Z
    message: Update Compatible. Post Cfg Actions: [] Drain Required: true
    reason: UpdatePrepared
    status: True
    type: UpdatePrepared
# ...
    lastTransitionTime: 2025-04-23T14:55:31Z
    message: Draining node. The drain will not be complete until desired drainer drain-rendered-worker-1930ca7433b7f0153286a3f04e4cb57b
      matches current drainer uncordon-rendered-worker-a9673968884f1ea42c26edcd914af907
    reason: UpdateExecutedDrained
    status: True
    type: Drained
# ...
    lastTransitionTime: 2025-04-23T14:55:31Z
    message: Cordoned node. The node is reporting Unschedulable = true
    reason: UpdateExecutedCordoned
    status: True
    type: Cordoned
# ...
  - lastTransitionTime: "2025-04-28T18:52:16Z"
    message: This node has not yet entered the NodeDegraded phase
    reason: NotYetOccurred
    status: "False"
    type: NodeDegraded
# ...
  configversion:
    current: rendered-worker-8110974a5cea69dff5b263237b58abd8
    desired: rendered-worker-1930ca7433b7f0153286a3f04e4cb57b
  observedgeneration:  4
  pinnedImageSets:
  - desiredGeneration: 1
    name: worker-pinned-images
# ...
```
