# 4.23. KMM firmware support

KMM firmware support copying firmware files from the kmod image to a node on OpenShift Container Platform before loading a kernel module. 

The contents of `.spec.moduleLoader.container.modprobe.firmwarePath` are copied into the `/var/lib/firmware` path on the node before running the `modprobe` command to insert the kernel module. 

All files and empty directories are removed from that location before running the `modprobe -r` command to unload the kernel module, when the pod is terminated. 

## 4.23.1. Configuring the lookup path on nodes

To add `/var/lib/firmware` to the kernel firmware lookup path on OpenShift Container Platform nodes, you can create a `MachineConfig` custom resource that sets the `firmware_class.path` kernel argument. 

On OpenShift Container Platform nodes, the set of default lookup paths for firmwares does not include the `/var/lib/firmware` path. 

**Procedure**

  1. Use the Machine Config Operator to create a `MachineConfig` custom resource (CR) that contains the `/var/lib/firmware` path: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 99-worker-kernel-args-firmware-path
spec:
  kernelArguments:
    - 'firmware_class.path=/var/lib/firmware'
```


You can configure the label based on your needs. In the case of single-node OpenShift, use either `control-pane` or `master` objects. 

  2. By applying the `MachineConfig` CR, the nodes are automatically rebooted. 



**Additional resources**

  * [Machine Config Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#machine-config-operator_machine-config-overview)



## 4.23.2. Building a kmod image

To build a kmod image with firmware support in OpenShift Container Platform, you can include the binary firmware in the builder image alongside the kernel module. 

**Procedure**

  * In addition to building the kernel module itself, include the binary firmware in the builder image: 

```plaintext
FROM registry.redhat.io/ubi9/ubi-minimal as builder

# Build the kmod

RUN ["mkdir", "/firmware"]
RUN ["curl", "-o", "/firmware/firmware.bin", "https://artifacts.example.com/firmware.bin"]

FROM registry.redhat.io/ubi9/ubi-minimal

# Copy the kmod, install modprobe, run depmod

COPY --from=builder /firmware /firmware
```


## 4.23.3. Tuning the Module resource

To configure firmware file paths for kernel modules on OpenShift Container Platform, you can set `.spec.moduleLoader.container.modprobe.firmwarePath` in the `Module` CR. 

**Procedure**

  * Set `.spec.moduleLoader.container.modprobe.firmwarePath` in the `Module` custom resource (CR): 

```yaml
apiVersion: kmm.sigs.x-k8s.io/v1beta1
kind: Module
metadata:
  name: my-kmod
spec:
  moduleLoader:
    container:
      modprobe:
        moduleName: my-kmod  # Required

        firmwarePath: /firmware
```


where: 

`spec.moduleLoader.container.modprobe.firmwarePath`
     Specifies that `/firmware/*` is copied into the files path `/var/lib/firmware/` on the node. This parameter is optional.
