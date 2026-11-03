# 2.10. Override storage or partition setup

You can use a `MachineConfig` object to change the disk partition schema, file systems, and RAID configurations that were established during the cluster installation. This allows you to make specific configuration changes that are different from the initial cluster state. 

If you specified storage and partition configuration upon cluster installation by using a Butane config, Ignition config, or machine config, those configurations become defaults within your cluster. If you create new nodes, those nodes automatically use those default configurations. 

You cannot change these components directly. By default, the Machine Config Operator (MCO) reviews changes in `MachineConfig` objects for specific fields and blocks some changes for security reasons. However, you can override this restriction for disk partition schema, file systems, and RAID configurations by adding the `irreconcilableValidationOverrides` parameter to the `MachineConfiguration` object. Then, you can create a new machine config to make the necessary changes for new nodes. 

Note

Configuration changes made through this process apply to new nodes only. 

For example, you might want to override your default storage configuration to add new hardware that uses a different storage partitioning schema or storage file system to your cluster. In this case, you can modify the storage configuration for any new nodes in your cluster. 

Or, if you used Ignition to modify the storage configuration as a post-installation task, your cluster might be reporting an `irreconcilableChanges` status in the `MachineConfigNode` object status fields. This messaging can alert you to these differences, so that you can determine if you want new hardware with the new configurations. 

Important

Overriding irreconcilable fields is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Prerequisites**

  * You enabled the required Technology Preview features for your cluster by adding the `TechPreviewNoUpgrade` feature set to the `FeatureGate` CR named `cluster`. For information about enabling Feature Gates, see _Enabling features using feature gates_. 

Warning

Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. This feature set allows you to enable these Technology Preview features on test clusters, where you can fully test them. Do not enable this feature set on production clusters. 




**Procedure**

  1. Edit the `MachineConfiguration` object by using the following command: 

```shell-session
$ oc edit machineconfiguration
```


  2. Add the `irreconcilableValidationOverrides` stanza to the `MachineConfiguration` object. 

```yaml
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
# ...
spec:
  irreconcilableValidationOverrides:
    storage:
    - Disks
    - Raid
    - FileSystems
# ...
```


where: 

`spec.irreconcilableValidationOverrides.storage.Disks`
     Allows you to modify the installed storage disk configuration to be used with new nodes. This field is optional. 
`spec.irreconcilableValidationOverrides.storage.Raid`
     Allows you to modify the installed RAID configuration to be used with new nodes. This field is optional. 
`spec.irreconcilableValidationOverrides.storage.FileSystems`
     Allows you to modify the installed file system configuration to be used with new nodes. This field is optional. 

  3. Create a YAML file for a `MachineConfig` object with the changes that you need, similar to the following: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: extra-disks
spec:
  config:
    ignition:
      version: "3.5.0"
    storage:
      disks:
      - device: "/dev/sdb"
        wipeTable: true
        partitions:
        - label: raid.1.1
          number: 1
          sizeMiB: 1024
          startMiB: 0
      - device: "/dev/sdc"
        wipeTable: true
        partitions:
        - label: raid.1.2
          number: 1
          sizeMiB: 1024
          startMiB: 0
      raid:
      - devices:
        - "/dev/disk/by-partlabel/raid.1.1"
        - "/dev/disk/by-partlabel/raid.1.2"
        level: stripe
        name: data
      filesystems:
      - device: "/dev/md/data"
        path: "/var/lib/data"
        format: ext4
        label: DATA
```


where: 

`spec.config.storage.disks`
     Specifies changes to the installed storage disk configuration in Ignition format. This field is optional. 
`spec.config.storage.raid`
     Specifies changes to the installed RAID configuration in Ignition format. This field is optional. 
`spec.config.storage.filesystems`
     Specifies changes to the installed file system configuration in Ignition format. This field is optional. 

  4. Create the `MachineConfig` object by using a command similar to the following: 

```shell-session
$ oc create -f <file_name>.yaml
```


When you create a new node from a machine set with the associated label, the new configurations are applied to the node.
