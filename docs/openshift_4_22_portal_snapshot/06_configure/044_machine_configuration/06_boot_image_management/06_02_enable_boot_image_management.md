# 6.2. Enable boot image management

For supported platforms, the Machine Config Operator (MCO) can manage and update the boot image on each node to ensure the Red Hat Enterprise Linux CoreOS (RHCOS) version of the boot image matches the Red Hat Enterprise Linux CoreOS (RHCOS) version appropriate for your cluster. 

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

To enable the boot image management feature for control plane machine sets or to re-enable the boot image management feature for worker machine sets where it was disabled, edit the `MachineConfiguration` object. You can enable the feature for all of the machine sets in the cluster or specific machine sets. 

Note

Because the boot image management feature for worker nodes is default for the Google Cloud and AWS platforms, the `managedBootImages` configuration does not appear in the machine configuration object. To enable the feature for control plane machine sets without disabling the feature for worker machine sets, you must expressly add the configuration for both the control plane and worker machine sets, as shown in the following procedure. If you add only the configuration for control plane machine sets, due to default behavior, the Machine Config Operator (MCO) overwrites the configuration for the worker machine sets. 

Enabling the feature updates the boot image to the Red Hat Enterprise Linux CoreOS (RHCOS) boot image version appropriate for your cluster. If the cluster is again updated to a new OpenShift Container Platform version in the future, the boot image is updated again. New nodes created after enabling the feature use the updated boot image. This feature has no effect on existing nodes. 

When boot image management is enabled, the MCO automatically enables boot image skew enforcement to ensure that the boot image version is compliant for your cluster. For more information, see "Boot image skew enforcement". 

**Procedure**

  1. Edit the `MachineConfiguration` object, named `cluster`, by using the following command: 

```shell-session
$ oc edit MachineConfiguration cluster
```


  2. Enable the boot image management feature for some or all of your machine sets: 

     * Enable the boot image management feature for all machine sets: 

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
        mode: All
    - apiGroup: machine.openshift.io
      resource: machinesets
      selection:
        mode: All
```


where: 

`spec.managedBootImages`
     Configures the boot image management feature. 
`spec.managedBootImages.machineManagers.apiGroup`
     Specifies the API group. This must be `machine.openshift.io`. 
`spec.managedBootImages.machineManagers.resource`
    

Specifies the resource within the specified API group to apply the change. Use one or both of the following parameters. You must add the full stanza, as shown, if you want to enable the feature for control plane and worker machine sets. 

       * `controlplanemachinesets`: Enables boot image management for control plane machine sets. 
       * `machinesets`: Enables boot image management for worker machine sets. 

`spec.managedBootImages.machineManagers.selection.mode`
     Specifies that the feature is enabled for all machine sets in the cluster. 

     * Enable the boot image management feature for specific worker machine sets: 

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
        mode: Partial
        partial:
          machineResourceSelector:
            matchLabels:
              region: "east"
```


where: 

`spec.managedBootImages`
     Configures the boot image management feature. 
`spec.managedBootImages.machineManagers.apiGroup`
     Specifies the API group. This must be `machine.openshift.io`. 
`spec.managedBootImages.machineManagers.resource`
     Specifies the resource within the specified API group to apply the change. This must be `machinesets`. Partial boot image management for control plane machine sets is not supported. 
`spec.managedBootImages.machineManagers.selection.mode`
     Specifies that the feature is enabled for specific machine sets in the cluster. This must be `Partial`. 
`spec.managedBootImages.machineManagers.selection.partial`
     Specifies that the feature is enabled for machine sets with the specified label in their `MachineSet` object. 




**Verification**

  1. View the current state of the boot image management feature by using the following command to view the machine configuration object: 

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
        mode: All
    - apiGroup: machine.openshift.io
      resource: machinesets
      selection:
        mode: All
```


where: 

`status.managedBootImagesStatus.machineManagers.selection.mode`
     Specifies that the boot image management feature is enabled when set to `All`. 

  2. Scale a machine set to create a new node by using a command similar to the following. The boot image is updated only for new nodes. 

```shell-session
$ oc scale --replicas=2 machinesets.machine.openshift.io <machineset> -n openshift-machine-api
```


  3. If your cluster was using an older boot image version, you can see the new boot image version when the new node reaches the `READY` state. View the Red Hat Enterprise Linux CoreOS (RHCOS) version on a nodes: 

     1. Log in to the node by using a command similar to the following: 

```shell-session
$ oc debug node/<node_name>
```


     2. Set `/host` as the root directory within the debug shell by using the following command: 

```shell-session
sh-5.1# chroot /host
```


     3. View the `/sysroot/.coreos-aleph-version.json` file by using a command similar to the following: 

```shell-session
sh-5.1# cat /sysroot/.coreos-aleph-version.json
```


**Example output**

```yaml
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251015-1-ostree.x86_64.ociarchive",
    "version": "9.6.20251015-1"
}
```


where: 

`<version>`
     Specifies the boot image version. 




**Additional resources**

  * [Obtaining the installation program](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installation-obtaining-installer_ipi-aws-preparing-to-install)
