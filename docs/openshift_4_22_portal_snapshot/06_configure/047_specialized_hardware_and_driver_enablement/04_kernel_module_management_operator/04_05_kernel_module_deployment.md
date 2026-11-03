# 4.5. Kernel module deployment

Kernel Module Management (KMM) monitors `Node` and `Module` resources on OpenShift Container Platform to load or unload kernel modules on eligible nodes. KMM creates worker pods on target nodes to reconcile the desired module state. 

To be eligible for a module, a node must contain the following: 

  * Labels that match the module’s `.spec.selector` field. 
  * A kernel version matching one of the items in the module’s `.spec.moduleLoader.container.kernelMappings` field. 
  * If ordered upgrade (`ordered_upgrade.md`) is configured in the module, a label that matches its `.spec.moduleLoader.container.version` field. 



When KMM reconciles nodes with the desired state as configured in the `Module` resource, it creates worker pods on the target nodes to run the necessary action. The KMM Operator monitors the outcome of the pods and records the information. The Operator uses this information to label the `Node` objects when the module is successfully loaded, and to run the device plugin, if configured. 

Worker pods run the KMM `worker` binary that performs the following tasks: 

  * Pulls the kmod image configured in the `Module` resource. Kmod images are standard OCI images that contain `.ko` files. 
  * Extracts the image in the pod’s filesystem. 
  * Runs `modprobe` with the specified arguments to perform the necessary action. 



## 4.5.1. The Module custom resource definition

The `Module` custom resource (CR) in OpenShift Container Platform represents a kernel module that can be loaded on all or select nodes in the cluster, through a kmod image. A `Module` CR specifies one or more kernel versions with which it is compatible, and a node selector. 

The compatible versions for a `Module` resource are listed under `.spec.moduleLoader.container.kernelMappings`. A kernel mapping can either match a `literal` version, or use `regexp` to match many of them at the same time. 

The reconciliation loop for the `Module` resource runs the following steps: 

  1. List all nodes matching `.spec.selector`. 
  2. Build a set of all kernel versions running on those nodes. 
  3. For each kernel version: 

     1. Go through `.spec.moduleLoader.container.kernelMappings` and find the appropriate container image name. If the kernel mapping has `build` or `sign` defined and the container image does not already exist, run the build, the signing pod, or both, as needed. 
     2. Create a worker pod to pull the container image determined in the previous step and run `modprobe`. 
     3. If `.spec.devicePlugin` is defined, create a device plugin daemon set using the configuration specified under `.spec.devicePlugin.container`. 

  4. Run `garbage-collect` on: 

     1. Obsolete device plugin `DaemonSets` that do not target any node. 
     2. Successful build pods. 
     3. Successful signing pods. 




## 4.5.2. Set soft dependencies between kernel modules

Soft dependencies require kernel modules to load in a specific order even when they do not share symbols. You can declare these dependencies in the `Module` CR with the `modulesLoadingOrder` field. 

The `depmod` utility does not recognize soft dependencies, and soft dependencies do not appear in the files it produces. For example, if `mod_a` has a soft dependency on `mod_b`, `modprobe mod_a` will not load `mod_b`. 

```yaml
# ...
spec:
  moduleLoader:
    container:
      modprobe:
        moduleName: mod_a
        dirName: /opt
        firmwarePath: /firmware
        parameters:
          - param=1
        modulesLoadingOrder:
          - mod_a
          - mod_b
```


In the configuration above, the worker pod will first try to unload the in-tree `mod_b` before loading `mod_a` from the kmod image. When the worker pod is terminated and `mod_a` is unloaded, `mod_b` will not be loaded again. 

Note

The first value in the list, to be loaded last, must be equivalent to the `moduleName`.
