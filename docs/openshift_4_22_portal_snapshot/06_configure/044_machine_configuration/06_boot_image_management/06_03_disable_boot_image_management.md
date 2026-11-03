# 6.3. Disable boot image management

You can disable the boot image management feature so that the Machine Config Operator (MCO) no longer manages or updates the boot image in the affected machine sets. For example, you could disable this feature for the worker nodes in order to use a custom boot image that you do not want changed. 

Note

If you are updating an Microsoft Azure or VMware vSphere cluster from OpenShift Container Platform 4.21 to 4.22, and you have not configured the `managedBootImages` parameter, the update is blocked with the message: `This cluster is Azure or vSphere but lacks a boot image configuration`. The update is intentionally blocked on Azure or vSphere clusters in order to alert you that the default boot image management behavior is changing between version 4.21 and 4.22 in order to enable boot images management by default on those platforms. 

To allow the update, perform one of the following tasks: 

  * If you want to allow the feature to be enabled, acknowledge that you are aware of the change in the default behavior by patching the `admin-acks` config map by running the following command: 

```shell-session
$ oc -n openshift-config patch cm admin-acks --patch '{"data":{"ack-4.21-boot-image-opt-out-in-4.22":"true"}}' --type=merge
```


  * If you do not want the boot image management feature enabled, explicitly disable the feature for worker machine sets by using the following procedure. 



You disable the boot image management feature for the control plane or worker machine sets in your cluster by editing the `MachineConfiguration` object. 

Note

The following table lists the platforms on which boot image management is available: 

Platform| Worker machine sets| Control plane machine sets  
---|---|---  
Google Cloud  |  Enabled by default  |  Disabled by default   
Amazon Web Services (AWS)  |  Enabled by default  |  Disabled by default   
Microsoft Azure  |  Enabled by default  |  Disabled by default   
VMware vSphere  |  Enabled by default  |  Not supported   
Show more

For all other platforms, the MCO does not automatically update the boot image with each cluster update. Images from the Google Cloud Marketplace or AWS Marketplace are not automatically updated. 

For clusters where automatic updates are disabled or not supported, you can manually update the boot image on your cluster. See "Manually updating the boot image" for information. The method to update or specify the image varies by platform. 

Disabling this feature does not rollback the nodes or machine sets to the originally-installed boot image. The machine sets retain the boot image version that was present when the feature was disabled and is not updated if the cluster is upgraded to a new OpenShift Container Platform version in the future. This feature has no effect on existing nodes. 

If boot image management is disabled, you must update the boot image version that is used by the boot image skew enforcement feature to ensure that the boot image is current for your cluster. For more information, see "Boot image skew enforcement". 

After disabling the feature, you can re-enable the feature at any time. For more information, see "Enabling updated boot images". 

**Procedure**

  1. Edit the `MachineConfiguration` object, named `cluster`, by using the following command:: 

```shell-session
$ oc edit MachineConfiguration cluster
```


  2. Disable the feature for some or all of your machine sets by making one or both of the following changes: 

     * Disable the feature for nodes in the worker machine sets by adding the following parameters: 

```yaml
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
spec:
# ...
  managedBootImages:
    machineManagers:
    - apiGroup: machine.openshift.io
      resource: machinesets
      selection:
        mode: None
```


where: 

`spec.managedBootImages`
     Specifies the parameters for the boot image management feature. 
`spec.managedBootImages.machineManagers.apiGroup`
     Specifies the API group. This must be `machine.openshift.io`. 
`spec.managedBootImages.machineManagers.resource`
     Specifies that the `selection.mode` parameter applies to worker nodes when a value of `machinesets` is set. 
`spec.managedBootImages.machineManagers.selection.mode`
     When `None`, specifies that the feature is disabled for the specified machine sets. 

     * Disable the feature for nodes in the control plane machine sets by adding the following parameters: 

```yaml
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
spec:
# ...
  managedBootImages:
    machineManagers:
    - apiGroup: machine.openshift.io
      resource: controlplanemachinesets
      selection:
        mode: None
```


where: 

`spec.managedBootImages`
     Specifies the parameters for the boot image management feature. 
`spec.managedBootImages.machineManagers.apiGroup`
     Specifies the API group. This must be `machine.openshift.io`. 
`spec.managedBootImages.machineManagers.resource`
     Specifies that the `selection.mode` parameter applies to control plane nodes when a value of `controlplanemachinesets` is set. 
`spec.managedBootImages.machineManagers.selection.mode`
     When `None`, specifies that the feature is disabled for the specified machine sets. 




**Verification**

  * View the current state of the boot image management feature by using the following command to view the machine configuration object: 

```shell-session
$ oc get machineconfiguration cluster -o yaml
```


**Example machine set with the boot image reference**

```yaml
kind: MachineConfiguration
metadata:
  name: cluster
# ...
status:
  conditions:
  - lastTransitionTime: "2025-05-01T20:11:49Z"
    message: Reconciled 2 of 4 MAPI MachineSets | Reconciled 0 of 0 CAPI MachineSets
      | Reconciled 0 of 0 CAPI MachineDeployments
    reason: BootImageUpdateConfigurationUpdated
    status: "True"
    type: BootImageUpdateProgressing
  - lastTransitionTime: "2025-05-01T19:30:13Z"
    message: 0 Degraded MAPI MachineSets | 0 Degraded CAPI MachineSets | 0 CAPI MachineDeployments
    reason: BootImageUpdateConfigurationUpdated
    status: "False"
    type: BootImageUpdateDegraded
  managedBootImagesStatus:
    machineManagers:
    - apiGroup: machine.openshift.io
      resource: controlplanemachinesets
      selection:
        mode: None
    - apiGroup: machine.openshift.io
      resource: machinesets
      selection:
        mode: All
```


where: 

`status.managedBootImagesStatus.machineManagers.selection.mode`
     Specifies that the boot image management feature is disabled when set to `None`. In this example, the boot image management feature is disabled for control plane machine sets and enabled for worker machine sets.
