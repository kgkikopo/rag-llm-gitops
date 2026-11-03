# 9.11. Hot plugging secondary network interfaces

You can add or remove secondary network interfaces without stopping your virtual machine (VM). OpenShift Virtualization supports hot plugging and hot unplugging for secondary interfaces that use bridge binding and the VirtIO device driver. 

OpenShift Virtualization also supports hot plugging secondary interfaces that use SR-IOV binding. To hot plug or hot unplug a secondary interface, you must have permission to create and list `VirtualMachineInstanceMigration` objects. 

Note

Hot unplugging is not supported for Single Root I/O Virtualization (SR-IOV) interfaces. 

## 9.11.1. VirtIO limitations

Each VirtIO interface uses one of the limited Peripheral Connect Interface (PCI) slots in the VM. There are a total of 32 slots available. The PCI slots are also used by other devices and must be reserved in advance, therefore slots might not be available on-demand. 

OpenShift Virtualization reserves up to six slots for hot plugging interfaces. 

Note

The actual number of slots available for hot plugging also depends on the machine type. For example, the default PCI topology for the q35 machine type supports hot plugging one additional PCIe device. For more information on PCI topology and hot plug support, see the [libvirt documentation](https://libvirt.org/pci-hotplug.html). 

If you restart the VM after hot plugging an interface, that interface becomes part of the standard network interfaces. 

## 9.11.2. Hot plug a secondary network interface by using the CLI

You can hot plug a secondary network interface to a virtual machine (VM) while the VM is running. 

**Prerequisites**

  * A network attachment definition is configured in the same namespace as your VM. 
  * The VM to which you want to hot plug the network interface is running. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Use your preferred text editor to edit the `VirtualMachine` manifest, as shown in the following example: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm-fedora
template:
  spec:
    domain:
      devices:
        interfaces:
        - name: defaultnetwork
          masquerade: {}
        # new interface
        - name: <secondary_nic>
          bridge: {}
    networks:
    - name: defaultnetwork
      pod: {}
    # new network
    - name: <secondary_nic>
      multus:
        networkName: <nad_name>
# ...
```


     * `spec.template.spec.domain.devices.interfaces.name` specifies the name of the new network interface. 
     * `spec.template.spec.networks.name` specifies the name of the network. This must be the same as the `name` of the new network interface that you defined in the `template.spec.domain.devices.interfaces` list. 
     * `spec.template.spec.networks.multus.networkName` specifies the name of the `NetworkAttachmentDefinition` object. 

  2. Save your changes and exit the editor. 
  3. For the new configuration to take effect, apply the changes by running the following command. Applying the changes triggers automatic VM live migration and attaches the network interface to the running VM. 

```shell-session
$ oc apply -f <filename>.yaml
```


where: 

<filename>
     Specifies the name of your `VirtualMachine` manifest YAML file. 




**Verification**

  1. Verify that the VM live migration is successful by using the following command: 

```shell-session
$ oc get VirtualMachineInstanceMigration -w
```


Example output: 

```shell-session
NAME                        PHASE             VMI
kubevirt-migrate-vm-lj62q   Scheduling        vm-fedora
kubevirt-migrate-vm-lj62q   Scheduled         vm-fedora
kubevirt-migrate-vm-lj62q   PreparingTarget   vm-fedora
kubevirt-migrate-vm-lj62q   TargetReady       vm-fedora
kubevirt-migrate-vm-lj62q   Running           vm-fedora
kubevirt-migrate-vm-lj62q   Succeeded         vm-fedora
```


  2. Verify that the new interface is added to the VM by checking the status of the virtual machine instance (VMI): 

```shell-session
$ oc get vmi vm-fedora -ojsonpath="{ @.status.interfaces }"
```


Example output: 

```plaintext
[
  {
    "infoSource": "domain, guest-agent",
    "interfaceName": "eth0",
    "ipAddress": "10.130.0.195",
    "ipAddresses": [
      "10.130.0.195",
      "fd02:0:0:3::43c"
    ],
    "mac": "52:54:00:0e:ab:25",
    "name": "default",
    "queueCount": 1
  },
  {
    "infoSource": "domain, guest-agent, multus-status",
    "interfaceName": "eth1",
    "mac": "02:d8:b8:00:00:2a",
    "name": "bridge-interface",
    "queueCount": 1
  }
]
```


The hot plugged interface appears in the VMI status. 




## 9.11.3. Hot unplug a secondary network interface by using the CLI

You can remove a secondary network interface from a running virtual machine (VM). 

Note

Hot unplugging is not supported for Single Root I/O Virtualization (SR-IOV) interfaces. 

**Prerequisites**

  * Your VM must be running. 
  * The VM must be created on a cluster running OpenShift Virtualization 4.14 or later. 
  * The VM must have a bridge network interface attached. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Using your preferred text editor, edit the `VirtualMachine` manifest file and set the interface state to `absent`. Setting the interface state to `absent` detaches the network interface from the guest, but the interface still exists in the pod. 

Example VM configuration: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm-fedora
template:
  spec:
    domain:
      devices:
        interfaces:
          - name: defaultnetwork
            masquerade: {}
          # set the interface state to absent
          - name: <secondary_nic>
            state: absent
            bridge: {}
    networks:
      - name: defaultnetwork
        pod: {}
      - name: <secondary_nic>
        multus:
          networkName: <nad_name>
# ...
```


Set the interface state to `absent` to detach it from the running VM. Removing the interface details from the VM specification does not hot unplug the secondary network interface. 

  2. Save your changes and exit the editor. 
  3. For the new configuration to take effect, apply the changes by running the following command. Applying the changes triggers automatic VM live migration and removes the interface from the pod. 

```shell-session
$ oc apply -f <filename>.yaml
```


where: 

<filename>
     Specifies the name of your `VirtualMachine` manifest YAML file. 




## 9.11.4. Additional resources

  * [Installing virtctl](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/getting-started#virt-installing-virtctl-binary_virt-using-the-cli-tools "3.2.1. Install the virtctl binary")
  * [About live migration permissions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/live-migration#virt-about-live-migration-permissions_virt-about-live-migration "11.1.2. Live migration permissions")
  * [Creating a Linux bridge network attachment definition](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-connecting-vm-to-linux-bridge "9.7. Connecting a virtual machine to a Linux bridge network")
  * [Creating an SR-IOV network attachment definition](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#nw-sriov-additional-network_virt-connecting-vm-to-sriov "9.8.2. Configuring SR-IOV additional network")
  * [Connect a VM to an SR-IOV network by using the CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-attaching-vm-to-sriov-network_virt-connecting-vm-to-sriov "9.8.3. Connect a VM to an SR-IOV network by using the CLI")
