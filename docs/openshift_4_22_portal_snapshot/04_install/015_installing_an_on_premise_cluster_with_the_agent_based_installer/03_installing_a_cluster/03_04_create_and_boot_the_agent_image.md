# 3.4. Create and boot the agent image

After you have prepared the configuration inputs for your installation, create the ISO image and boot it on your machines. 

**Prerequisites**

  * If you plan to boot the agent image from a USB drive, you have installed the `syslinux` package. 



**Procedure**

  1. Create the agent image by running the following command: 

```shell-session
$ openshift-install --dir <install_directory> agent create image
```


Note

Red Hat Enterprise Linux CoreOS (RHCOS) supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability. Multipathing is enabled by default in the agent ISO image, with a default `/etc/multipath.conf` configuration. 

  2. If you plan to boot the ISO image from a USB drive, add a master boot record to the image by running the following command: 

```shell-session
$ isohybrid --uefi <agent_iso_image>
```


**Example command**

```shell-session
$ isohybrid --uefi agent.x86_64.iso
```


  3. Boot the `agent.x86_64.iso`, `agent.aarch64.iso`, or `agent.s390x.iso` image on the bare-metal machines.
