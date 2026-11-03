# 1.3. Adding day-1 kernel arguments

You can add kernel arguments to all control plane and compute nodes during initial cluster installation. This approach ensures the arguments take effect before the first boot operation of the system. You can also modify kernel arguments as a day-2 activity. 

The following list details reasons why you might want to add kernel arguments during cluster installation: 

  * You need to do some low-level network configuration before the systems start. 
  * You want to disable a feature, such as SELinux, so it has no impact on the systems when they first come up. 



Warning

Disabling SELinux on RHCOS in production is not supported. Re-provision any node with disabled SELinux before including the node in a production cluster. 

To add kernel arguments to control plane or compute nodes, you can create a `MachineConfig` object. You can then inject the object into the set of manifest files used by Ignition during cluster setup. 

For a listing of arguments you can pass to a RHEL 8 kernel at boot time, see "Kernel.org kernel parameters" in the _Additional resources_ section. Add kernel arguments before installation only if they are required to complete the initial OpenShift Container Platform installation. 

**Procedure**

  1. Change to the directory that contains the installation program and generate the Kubernetes manifests for the cluster: 

```shell-session
$ ./openshift-install create manifests --dir <installation_directory>
```


  2. Determine if you want to add kernel arguments to compute or control plane nodes, or both. 
  3. In the `openshift` directory, create a file, such as `99-openshift-machineconfig-master-kargs.yaml`, to define a `MachineConfig` object. Add the kernel settings to this file. The example adds a `loglevel=7` kernel argument to control plane nodes. 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 99-openshift-machineconfig-master-kargs
spec:
  kernelArguments:
    - loglevel=7
# ...
```


You can change `master` to `worker` to add kernel arguments to compute nodes instead. Create a separate YAML file to add to both control plane and compute nodes. 




**Additional resources**

  * [Kernel.org kernel parameters](https://www.kernel.org/doc/Documentation/admin-guide/kernel-parameters.txt)
