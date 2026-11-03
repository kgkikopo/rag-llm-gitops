# 4.7. Adding IBM Z agents with RHEL KVM

You can manually add IBM Z® agents with RHEL KVM. Only use this procedure for IBM Z® clusters with RHEL KVM. 

Note

The `nmstateconfig` parameter must be configured for the KVM boot. 

**Procedure**

  1. Boot your RHEL KVM machine. 
  2. To deploy the virtual server, run the `virt-install` command with the following parameters: 

**ISO boot**

```shell-session
$ virt-install
    --name <vm_name> \
    --autostart \
    --memory=<memory> \
    --cpu host \
    --vcpus=<vcpus> \
    --cdrom \<path_to_image>/<agent_iso_image> \
    --disk pool=default,size=<disk_pool_size> \
    --network network:default,mac=<mac_address> \
    --graphics none \
    --noautoconsole \
    --os-variant rhel9.0 \
    --wait=-1
```


For the `--cdrom` parameter, specify the location of the ISO image on the local server, for example, `<path_to_image>/home/<image>.iso`. 

Note

For KVM-based installations using DASD devices on IBM Z, a partition (for example, `/dev/dasdb1`) must be created using the `fdasd` partitioning tool. 

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
