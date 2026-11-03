# 8.15. Use a virtual Trusted Platform Module (vTPM) device

To run Windows 11 or other workloads that require a Trusted Platform Module, you can add a virtual TPM (vTPM) to a new or existing virtual machine. Enable this by editing the `VirtualMachine` or `VirtualMachineInstance` manifest. 

Important

With OpenShift Virtualization 4.18 and newer, you can export virtual machines (VMs) with attached vTPM devices, create snapshots of these VMs, and restore VMs from these snapshots. However, cloning a VM with a vTPM device attached to it or creating a new VM from its snapshot is not supported. 

## 8.15.1. vTPM devices and state persistence

A virtual Trusted Platform Module (vTPM) device functions like a physical Trusted Platform Module (TPM) hardware chip. You can use a vTPM device with any operating system, but Windows 11 requires the presence of a TPM chip to install or boot. 

A vTPM device allows VMs created from a Windows 11 image to function without a physical TPM chip. 

OpenShift Virtualization supports persisting vTPM device state by using Persistent Volume Claims (PVCs) for VMs. If you do not specify the storage class for this PVC, OpenShift Virtualization uses the default storage class for virtualization workloads. If the default storage class for virtualization workloads is not set, OpenShift Virtualization uses the default storage class for the cluster. 

Note

The storage class that is marked as default for virtualization workloads has the annotation `storageclass.kubevirt.io/is-default-virt-class` set to "true". You can find this storage class by running the following command: 

```shell-session
$ oc get sc -o jsonpath='{range .items[?(.metadata.annotations.storageclass\.kubevirt\.io/is-default-virt-class=="true")]}{.metadata.name}{"\n"}{end}'
```


Similarly, the default storage class for the cluster has the annotation `storageclass.kubernetes.io/is-default-class` set to "true". To find this storage class, run the following command: 

```shell-session
$ oc get sc -o jsonpath='{range .items[?(.metadata.annotations.storageclass\.kubernetes\.io/is-default-class=="true")]}{.metadata.name}{"\n"}{end}'
```


To ensure consistent behavior, configure only one storage class as the default for virtualization workloads and for the cluster respectively. 

It is recommended that you specify the storage class explicitly by setting the `vmStateStorageClass` attribute in the `HyperConverged` custom resource (CR): 

```yaml
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
spec:
  vmStateStorageClass: <storage_class_name>

# ...
```


If you do not enable vTPM, then the VM does not recognize a TPM device, even if the node has one. 

## 8.15.2. Add a vTPM device to a virtual machine

Adding a virtual Trusted Platform Module (vTPM) device to a virtual machine (VM) allows you to run a VM created from a Windows 11 image without a physical TPM device. A vTPM device also stores secrets for that VM. 

Important

When you add a virtual Trusted Platform Module (vTPM) device to a Windows VM, it is important to make the vTPM device persistent. The BitLocker Drive is encrypted successfully and the encryption system check passes even if the vTPM device is not persistent. If the vTPM device is not persistent, it is discarded on shutdown. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Run the following command to update the VM configuration: 

```shell-session
$ oc edit vm <vm_name> -n <namespace>
```


  2. Edit the VM specification to add the vTPM device. For example: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
    name: example-vm
spec:
  template:
    spec:
      domain:
        devices:
          tpm:  
```


1

```yaml
            persistent: true 
```


2

```yaml
# ...
```


     * `spec.template.spec.domain.devices.tpm` specifies the vTPM device to add to the VM. 
     * `spec.template.spec.domain.devices.tpm.persistent` specifies that the vTPM device state persists after the VM is shut down. The default value is `false`. 

  3. To apply your changes, save and exit the editor. 
  4. Optional: If you edited a running virtual machine, you must restart it for the changes to take effect. 



## 8.15.3. Additional resources

  * [Exporting virtual machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-exporting-vms "8.12. Export a virtual machine")
  * [Creating a snapshot by using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/backup-and-restore#virt-creating-vm-snapshot-cli_virt-backup-restore-snapshots "15.1.4. Create a snapshot by using the CLI")
  * [Restoring a virtual machine from a snapshot by using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/backup-and-restore#virt-restoring-vm-from-snapshot-cli_virt-backup-restore-snapshots "15.1.7. Restore a VM from a snapshot by using the CLI")
