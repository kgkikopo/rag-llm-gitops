# 6.4. Creating the PXE assets

Create the assets and optional script to implement in your PXE infrastructure. 

**Procedure**

  1. Create the PXE assets by running the following command: 

```shell-session
$ openshift-install agent create pxe-files
```


The generated PXE assets and optional iPXE script can be found in the `boot-artifacts` directory. 

**Example filesystem with PXE assets and optional iPXE script**

```shell-session
boot-artifacts
    ├─ agent.x86_64-initrd.img
    ├─ agent.x86_64.ipxe
    ├─ agent.x86_64-rootfs.img
    └─ agent.x86_64-vmlinuz
```


Important

The contents of the `boot-artifacts` directory vary depending on the specified architecture. 

Note

Red Hat Enterprise Linux CoreOS (RHCOS) supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability. Multipathing is enabled by default in the Agent ISO image, with a default `/etc/multipath.conf` configuration. 

  2. Upload the PXE assets and optional script to your infrastructure where they will be accessible during the boot process. 

Note

If you generated an iPXE script, the location of the assets must match the `bootArtifactsBaseURL` value you added to the `agent-config.yaml` file.
