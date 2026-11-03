# 6.5. Manually adding IBM Z agents

After creating the PXE assets, you can add IBM Z® agents. 

Only use this procedure for IBM Z® clusters. 

Depending on your IBM Z® environment, you can choose from the following options: 

  * Adding IBM Z® agents with z/VM 
  * Adding IBM Z® agents with RHEL KVM 
  * Adding IBM Z® agents with Logical Partition (LPAR) 



Note

Currently, ISO boot support on IBM Z® (`s390x`) is available only for Red Hat Enterprise Linux (RHEL) KVM, which provides the flexibility to choose either PXE or ISO-based installation. For installations with z/VM and Logical Partition (LPAR), only PXE boot is supported. 

## 6.5.1. Networking requirements for IBM Z

In IBM Z environments, advanced networking technologies such as Open Systems Adapter (OSA), HiperSockets, and Remote Direct Memory Access (RDMA) over Converged Ethernet (RoCE) require specific configurations that deviate from the standard network settings and those needs to be persisted for multiple boot scenarios that occur in the Agent-based Installation. 

To persist these parameters during boot, the `ai.ip_cfg_override=1` parameter is required in the `.parm` file. This parameter is used with the configured network cards to ensure a successful and efficient deployment on IBM Z. 

The following table lists the network devices that are supported on each hypervisor for the network configuration override functionality: 

Network device| z/VM| KVM| LPAR Classic| LPAR Dynamic Partition Manager (DPM)  
---|---|---|---|---  
Virtual Switch  |  Supported [1] |  Not applicable [2] |  Not applicable  |  Not applicable   
Direct attached Open Systems Adapter (OSA)  |  Supported  |  Not required [3] |  Supported  |  Not required   
RDMA over Converged Ethernet (RoCE)  |  Not required  |  Not required  |  Not required  |  Not required   
HiperSockets  |  Supported  |  Not required  |  Supported  |  Not required   
Show more

  1. Supported: When the `ai.ip_cfg_override` parameter is required for the installation procedure. 
  2. Not Applicable: When a network card is not applicable to be used on the hypervisor. 
  3. Not required: When the `ai.ip_cfg_override` parameter is not required for the installation procedure. 



## 6.5.2. Configuring network overrides in an IBM Z environment

You can specify a static IP address on IBM Z machines that use Logical Partition (LPAR) and z/VM. This is useful when the network devices do not have a static MAC address assigned to them. 

Note

If you are using an OSA network device in Processor Resource/Systems Manager (PR/SM) mode, the lack of persistent MAC addresses can lead to a dynamic assignment of roles for nodes. This means that the roles of individual nodes are not fixed and can change, as the system is unable to reliably associate specific MAC addresses with designated node roles. If MAC addresses are not persistent for any of the interfaces, roles for the nodes are assigned randomly during Agent-based installation. 

**Procedure**

  * If you have an existing `.parm` file, edit it to include the following entry: 

```shell-session
ai.ip_cfg_override=1
```


This parameter allows the file to add the network settings to the Red Hat Enterprise Linux CoreOS (RHCOS) installer. 

Note

The `override` parameter overrides the host’s network configuration settings. 

```shell-session
rd.neednet=1 cio_ignore=all,!condev
console=ttysclp0
coreos.live.rootfs_url=<coreos_url>
ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns>
rd.znet=qeth,<network_adaptor_range>,layer2=1
rd.<disk_type>=<adapter>
rd.zfcp=<adapter>,<wwpn>,<lun> random.trust_cpu=on
zfcp.allow_lun_scan=0
ai.ip_cfg_override=1
ignition.firstboot ignition.platform.id=metal
random.trust_cpu=on
```


    * For the `coreos.live.rootfs_url` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` that you are booting. Only HTTP and HTTPS protocols are supported. 
    * For installations on direct access storage devices (DASD) type disks, use `rd.` to specify the DASD where Red Hat Enterprise Linux CoreOS (RHCOS) is to be installed. For installations on Fibre Channel Protocol (FCP) disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where RHCOS is to be installed. 
    * Specify values for `<adapter>`, `<wwpn>`, and `<lun>` as in the following example: `rd.zfcp=0.0.8002,0x500507630400d1e3,0x4000404600000000`. 

Important

The `ip=` kernel parameter uses the following syntax: 

`ip=[IP]:[Gateway]:[Netmask]:[Hostname]:[Interface]:[None]:[DNS]`

For VLAN configurations: 

    * Define both the **base interface** and the **tagged VLAN interface** separately. 
    * The `vlan=` parameter links the tagged interface (for example, `encbdf0.300`) to the underlying physical interface (`encbdf0`). 

For bonded interfaces: 

    * No changes are required in the default kernel command-line parameters. 
    * To install nodes by using bonded interfaces, provide the appropriate bond configuration in the `agent-config` file. 




## 6.5.3. Adding IBM Z agents with z/VM

You can manually add IBM Z® agents with z/VM. Only use this procedure for IBM Z® clusters with z/VM. 

**Prerequisites**

  * You have a running file server with access to the guest virtual machines (VMs). 



**Procedure**

  1. Create a parameter file for the z/VM guest: 

```plaintext
rd.neednet=1 \
console=ttysclp0 \
coreos.live.rootfs_url=<rootfs_url> \
ip=172.18.78.2::172.18.78.1:255.255.255.0:::none nameserver=172.18.78.1 \
zfcp.allow_lun_scan=0 \
ai.ip_cfg_override=1 \
rd.znet=qeth,0.0.bdd0,0.0.bdd1,0.0.bdd2,layer2=1 \
rd.dasd=0.0.4411 \
rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \
fips=1 \
random.trust_cpu=on rd.luks.options=discard \
ignition.firstboot ignition.platform.id=metal \
console=tty1 console=ttyS1,115200n8 \
coreos.inst.persistent-kargs="console=tty1 console=ttyS1,115200n8"
```


     * For the `coreos.live.rootfs_url` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` that you are booting. Only HTTP and HTTPS protocols are supported. 
     * For the `ip` parameter, assign the IP address automatically using DHCP, or manually assign the IP address, as described in "Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE". 
     * The default for `zfcp.allow_lun_scan` is `1`. Omit this entry when using an OSA network adapter. 
     * For installations on DASD-type disks, use `rd.dasd` to specify the DASD where Red Hat Enterprise Linux CoreOS (RHCOS) is to be installed. Omit this entry for FCP-type disks. 
     * For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where RHCOS is to be installed. Omit this entry for DASD-type disks. 

Note

For FCP multipath configurations, provide available multiple paths to the disk instead of a single path, and add `rd.multipath=default` to enable multipath during installation. 

```plaintext
rd.zfcp=<adapter1>,<wwpn1>,<lun1> \
rd.zfcp=<adapter2>,<wwpn2>,<lun2> \
rd.multipath=default
```


     * To enable FIPS mode, specify `fips=1`. This entry is required in addition to setting the `fips` parameter to `true` in the `install-config.yaml` file. 

Leave all other parameters unchanged. 

  2. Punch the `kernel.img`,`generic.parm`, and `initrd.img` files to the virtual reader of the z/VM guest virtual machine. 

For more information, see "PUNCH" in the IBM documentation. 

Tip

You can use the `CP PUNCH` command or, if you use Linux, the `vmur` command, to transfer files between two z/VM guest virtual machines. 

  3. Log in to the conversational monitor system (CMS) on the bootstrap machine. 
  4. IPL the bootstrap machine from the reader by running the following command: 

```shell-session
$ ipl c
```


For more information, see "IPL" in the IBM documentation. 




**Additional resources**

  * [PUNCH](https://www.ibm.com/docs/en/zvm/latest?topic=commands-punch)
  * [IPL](https://www.ibm.com/docs/en/zvm/latest?topic=commands-ipl)



**Additional resources**

  * [Installing a cluster with z/VM on IBM Z and IBM LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z)



## 6.5.4. Adding IBM Z agents with RHEL KVM

You can manually add IBM Z® agents with RHEL KVM. Only use this procedure for IBM Z® clusters with RHEL KVM. 

Note

The `nmstateconfig` parameter must be configured for the KVM boot. 

**Procedure**

  1. Boot your RHEL KVM machine. 
  2. To deploy the virtual server, run the `virt-install` command with the following parameters: 

```shell-session
$ virt-install \
   --name <vm_name> \
   --autostart \
   --ram=16384 \
   --cpu host \
   --vcpus=8 \
   --location <path_to_kernel_initrd_image>,kernel=kernel.img,initrd=initrd.img \
   --disk <qcow_image_path> \
   --network network:macvtap ,mac=<mac_address> \
   --graphics none \
   --noautoconsole \
   --wait=-1 \
   --extra-args "rd.neednet=1 nameserver=<nameserver>" \
   --extra-args "ip=<IP>::<nameserver>::<hostname>:enc1:none" \
   --extra-args "coreos.live.rootfs_url=http://<http_server>:8080/agent.s390x-rootfs.img" \
   --extra-args "random.trust_cpu=on rd.luks.options=discard" \
   --extra-args "ignition.firstboot ignition.platform.id=metal" \
   --extra-args "console=tty1 console=ttyS1,115200n8" \
   --extra-args "coreos.inst.persistent-kargs=console=tty1 console=ttyS1,115200n8" \
   --osinfo detect=on,require=off
```


For the `--location` parameter, specify the location of the `kernel` and `initrd` files. The location can be a local server path or a URL using HTTP or HTTPS. 

  3. Optional: Enable FIPS mode. 

To enable FIPS mode on IBM Z® clusters with RHEL KVM you must use PXE boot instead and run the `virt-install` command with the following parameters: 

**PXE boot**

```shell-session
$ virt-install \
   --name <vm_name> \
   --autostart \
   --ram=16384 \
   --cpu host \
   --vcpus=8 \
   --location <path_to_kernel_initrd_image>,kernel=kernel.img,initrd=initrd.img \
   --disk <qcow_image_path> \
   --network network:macvtap ,mac=<mac_address> \
   --graphics none \
   --noautoconsole \
   --wait=-1 \
   --extra-args "rd.neednet=1 nameserver=<nameserver>" \
   --extra-args "ip=<IP>::<nameserver>::<hostname>:enc1:none" \
   --extra-args "coreos.live.rootfs_url=http://<http_server>:8080/agent.s390x-rootfs.img" \
   --extra-args "random.trust_cpu=on rd.luks.options=discard" \
   --extra-args "ignition.firstboot ignition.platform.id=metal" \
   --extra-args "console=tty1 console=ttyS1,115200n8" \
   --extra-args "coreos.inst.persistent-kargs=console=tty1 console=ttyS1,115200n8" \
   --extra-args "fips=1" \
   --osinfo detect=on,require=off
```


where: 

`--location`
     Specifies the location of the kernel/initrd on the HTTP or HTTPS server. 
`--extra-args "fips=1"`
    

Specifies the enablement of FIPS mode. This entry is required in addition to setting the `fips` parameter to `true` in the `install-config.yaml` file. 

Note

     * For KVM-based installations using DASD devices on IBM Z, a partition (for example, `/dev/dasdb1`) must be created using the `fdasd` partitioning tool. 
     * Currently, only PXE boot is supported to enable FIPS mode on IBM Z®. 




**Additional resources**

  * [Installing a cluster with RHEL KVM on IBM Z and IBM LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z-kvm)



## 6.5.5. Adding IBM Z agents in a Logical Partition (LPAR)

You can manually add IBM Z® agents to your cluster that runs in an LPAR environment. 

Use this procedure only for IBM Z® clusters running in an LPAR. 

**Prerequisites**

  * You have Python 3 installed. 
  * You have a running file server with access to the Logical Partition (LPAR). 



**Procedure**

  1. Create a boot parameter file for the agents. 

```shell-session
rd.neednet=1 cio_ignore=all,!condev \
console=ttysclp0 \
ignition.firstboot ignition.platform.id=metal
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \
coreos.inst.persistent-kargs=console=ttysclp0 \
ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
rd.znet=qeth,<network_adaptor_range>,layer2=1
rd.<disk_type>=<adapter> \
fips=1 \
zfcp.allow_lun_scan=0 \
ai.ip_cfg_override=1 \
random.trust_cpu=on rd.luks.options=discard
```


     * For the `coreos.live.rootfs_url` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` that you are starting. Only HTTP and HTTPS protocols are supported. 
     * For the `ip` parameter, manually assign the IP address, as described in "Installing a cluster with z/VM on IBM Z and IBM LinuxONE". 
     * For installations on DASD-type disks, use `rd.dasd` to specify the DASD where Red Hat Enterprise Linux CoreOS (RHCOS) is to be installed. For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where RHCOS is to be installed. 

Note

For FCP multipath configurations, provide available multiple paths to the disk instead of a single path, and add `rd.multipath=default` to enable multipath during installation. 

**Example**

```shell-session
rd.zfcp=<adapter1>,<wwpn1>,<lun1> \
rd.zfcp=<adapter2>,<wwpn2>,<lun2> \
rd.multipath=default
```


     * To enable FIPS mode, specify `fips=1`. This entry is required in addition to setting the `fips` parameter to `true` in the `install-config.yaml` file. 

Note

The `.ins` and `initrd.img.addrsize` files are automatically generated for `s390x` architecture as part of boot-artifacts from the installation program and are only used when booting in an LPAR environment. 

**Example filesystem with LPAR boot**

```shell-session
boot-artifacts
    ├─ agent.s390x-generic.ins
    ├─ agent.s390x-initrd.addrsize
    ├─ agent.s390x-rootfs.img
    └─ agent.s390x-kernel.img
    └─ agent.s390x-rootfs.img
```


  2. Rename the `boot-artifacts` file present in the `generic.ins` parameter file to match the names of the `boot-artifacts` file generated by the installation program. 
  3. Transfer the `initrd`, `kernel`, `generic.ins`, and `initrd.img.addrsize` parameter files to the file server. For more information, see "Booting Linux in LPAR mode" in the IBM documentation. 
  4. Start the machine. 
  5. Repeat the procedure for all other machines in the cluster. 



**Additional resources**

  * [Booting Linux in LPAR mode](https://www.ibm.com/docs/en/linux-on-systems?topic=bl-booting-linux-in-lpar-mode)



**Additional resources**

  * [Installing a cluster in an LPAR on IBM Z and IBM LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z-lpar)
