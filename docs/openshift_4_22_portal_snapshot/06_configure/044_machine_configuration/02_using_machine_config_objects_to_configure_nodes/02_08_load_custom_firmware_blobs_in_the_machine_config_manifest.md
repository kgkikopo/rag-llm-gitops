# 2.8. Load custom firmware blobs in the machine config manifest

You can load local firmware blobs that are not managed by RHCOS into the machine config manifest by updating the search path with a machine config. 

By default, the location for firmware blobs in `/usr/lib` is read-only. 

**Procedure**

  1. Create a Butane config file, `98-worker-firmware-blob.bu`, that updates the search path so that it is root-owned and writable to local storage. The following example places the custom blob file from your local workstation onto nodes under `/var/lib/firmware`. 

Note

The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.22.0`. See "Creating machine configs with Butane" for information about Butane. 

**Butane config file for custom firmware blob**

```yaml
variant: openshift
version: 4.22.0
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 98-worker-firmware-blob
storage:
  files:
  - path: /var/lib/firmware/<package_name>
    contents:
      local: <package_name>
    mode: 0644
openshift:
  kernel_arguments:
    - 'firmware_class.path=/var/lib/firmware'
```


where: 

`storage.files.path`
     Specifies the path on the node where the firmware package is copied to. 
`storage.files.contents.local`
     Specifies a file with contents that are read from a local file directory on the system running Butane. The path of the local file is relative to a `files-dir` directory, which must be specified by using the `--files-dir` option with Butane in a subsequent step. 
`storage.files.mode`
     Specifies the permissions for the file on the RHCOS node. Red Hat recommends setting `0644` permissions. 
`openshift.kernel_arguments`
     Specifies the kernel search path of where to look for the custom firmware blob that was copied from your local workstation onto the root file system of the node. This example uses `/var/lib/firmware` as the customized path. 

  2. Run Butane to generate a `MachineConfig` object file that uses a copy of the firmware blob on your local workstation named `98-worker-firmware-blob.yaml`. The firmware blob contains the configuration to be delivered to the nodes. The following example uses the `--files-dir` option to specify the directory on your workstation where the local file or files are located: 

```shell-session
$ butane 98-worker-firmware-blob.bu -o 98-worker-firmware-blob.yaml --files-dir <directory_including_package_name>
```


  3. Apply the configurations to the nodes in one of two ways: 

     * If the cluster is not running yet, after you generate manifest files, add the `MachineConfig` object file to the `<installation_directory>/openshift` directory, and then continue to create the cluster. 
     * If the cluster is already running, apply the file: 

```shell-session
$ oc apply -f 98-worker-firmware-blob.yaml
```


A `MachineConfig` object YAML file is created for you to finish configuring your machines. 

  4. Save the Butane config in case you need to update the `MachineConfig` object in the future.
