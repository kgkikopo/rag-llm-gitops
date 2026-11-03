# 1.13. Installing RHCOS and starting the OpenShift Container Platform bootstrap process

To install OpenShift Container Platform on bare-metal infrastructure that you provision, install Red Hat Enterprise Linux CoreOS (RHCOS) by using the generated Ignition config files. Providing these files ensures the bootstrap process begins automatically after the machines reboot. 

If you have configured suitable networking, DNS, and load balancing infrastructure, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS machines have rebooted. 

To install RHCOS on the machines, follow either the steps to use an ISO image or network PXE booting. 

Note

The compute node deployment steps included in this installation document are RHCOS-specific. If you choose instead to deploy RHEL-based compute nodes, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. Only RHEL 8 compute machines are supported. 

You can configure RHCOS during ISO and PXE installations by using the following methods: 

  * Kernel arguments: You can use kernel arguments to provide installation-specific information. For example, you can specify the locations of the RHCOS installation files that you uploaded to your HTTP server and the location of the Ignition config file for the type of node you are installing. For a PXE installation, you can use the `APPEND` parameter to pass the arguments to the kernel of the live installer. For an ISO installation, you can interrupt the live installation boot process to add the kernel arguments. In both installation cases, you can use special `coreos.inst.*` arguments to direct the live installer, as well as standard installation boot arguments for turning standard kernel services on or off. 
  * Ignition configs: OpenShift Container Platform Ignition config files (`*.ign`) are specific to the type of node you are installing. You pass the location of a bootstrap, control plane, or compute node Ignition config file during the RHCOS installation so that it takes effect on first boot. In special cases, you can create a separate, limited Ignition config to pass to the live system. That Ignition config could do a certain set of tasks, such as reporting success to a provisioning system after completing installation. This special Ignition config is consumed by the `coreos-installer` to be applied on first boot of the installed system. Do not provide the standard control plane and compute node Ignition configs to the live ISO directly. 
  * `coreos-installer`: You can boot the live ISO installer to a shell prompt, which allows you to prepare the permanent system in a variety of ways before first boot. In particular, you can run the `coreos-installer` command to identify various artifacts to include, work with disk partitions, and set up networking. In some cases, you can configure features on the live system and copy them to the installed system. 

Note

As of version `0.17.0-3`, `coreos-installer` requires RHEL 9 or later to run the program. You can still use older versions of `coreos-installer` to customize RHCOS artifacts of newer OpenShift Container Platform releases and install metal images to disk. See "coreos-installer image mirror" to download older versions of the `coreos-installer` binary. 




Whether to use an ISO or PXE install depends on your situation. A PXE install requires an available DHCP service and more preparation, but can make the installation process more automated. An ISO install is a more manual process and can be inconvenient if you are setting up more than a few machines. 

**Additional resources**

  * [coreos-installer image mirror](https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/coreos-installer/)



## 1.13.1. Installing RHCOS by using an ISO image

To provision physical or virtual machines, install RHCOS by using a bootable ISO image. 

**Prerequisites**

  * You have created the Ignition config files for your cluster. 
  * You have configured a suitable network, DNS, and load balancing infrastructure. 
  * You have an HTTP server that can be accessed from your computer, and from the machines that you create. 
  * You have reviewed the _Advanced RHCOS installation configuration_ section for different ways to configure features, such as networking and disk partitioning. 



**Procedure**

  1. Obtain the SHA512 digest for each of your Ignition config files. For example, you can use the following on a system running Linux to get the SHA512 digest for your `bootstrap.ign` Ignition config file: 

```shell-session
$ sha512sum <installation_directory>/bootstrap.ign
```


The digests are provided to the `coreos-installer` in a later step to validate the authenticity of the Ignition config files on the cluster nodes. 

  2. Upload the bootstrap, control plane, and compute node Ignition config files that the installation program created to your HTTP server. Note the URLs of these files. 

Important

You can add or change configuration settings in your Ignition configs before saving them to your HTTP server. If you plan to add more compute machines to your cluster after you finish installation, do not delete these files. 

  3. From the installation host, validate that the Ignition config files are available on the URLs. The following example gets the Ignition config file for the bootstrap node: 

```shell-session
$ curl -k http://<HTTP_server>/bootstrap.ign
```


     * <HTTP_server>: Replace `bootstrap.ign` with `master.ign` or `worker.ign` in the command to validate that the Ignition config files for the control plane and compute nodes are also available. 

**Example output**

```shell-session
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0{"ignition":{"version":"3.2.0"},"passwd":{"users":[{"name":"core","sshAuthorizedKeys":["ssh-rsa...
```


  4. Although it is possible to obtain the RHCOS images that are required for your preferred method of installing operating system instances from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/) page, the recommended way to obtain the correct version of your RHCOS images are from the output of `openshift-install` command: 

```shell-session
$ openshift-install coreos print-stream-json | grep '\.iso[^.]'
```


**Example output**

```shell-session
"location": "<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live.aarch64.iso",
"location": "<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live.ppc64le.iso",
"location": "<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live.s390x.iso",
"location": "<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live.x86_64.iso",
```


Important

The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Use the image versions that match your OpenShift Container Platform version if they are available. Use only ISO images for this procedure. RHCOS qcow2 images are not supported for this installation type. 

ISO file names resemble the following example: 

`rhcos-<version>-live.<architecture>.iso`

  5. Use the ISO to start the RHCOS installation. Use one of the following installation options: 

     * Burn the ISO image to a disk and boot it directly. 
     * Use ISO redirection by using a lights-out management (LOM) interface. 

  6. Boot the RHCOS ISO image without specifying any options or interrupting the live boot sequence. Wait for the installer to boot into a shell prompt in the RHCOS live environment. 

Note

It is possible to interrupt the RHCOS installation boot process to add kernel arguments. However, for this ISO procedure you should use the `coreos-installer` command as outlined in the following steps, instead of adding kernel arguments. 

  7. Run the `coreos-installer` command and specify the options that meet your installation requirements. At a minimum, you must specify the URL that points to the Ignition config file for the node type, and the device that you are installing to: 

```shell-session
$ sudo coreos-installer install --ignition-url=http://<HTTP_server>/<node_type>.ign <device> \
--ignition-hash=sha512-<digest>
```


     * `<device>`: You must run the `coreos-installer` command by using `sudo`, because the `core` user does not have the required root privileges to perform the installation. 
     * `<digest>`: The `--ignition-hash` option is required when the Ignition config file is obtained through an HTTP URL to validate the authenticity of the Ignition config file on the cluster node. `<digest>` is the Ignition config file SHA512 digest obtained in a preceding step. 

Note

If you want to provide your Ignition config files through an HTTPS server that uses TLS, you can add the internal certificate authority (CA) to the system trust store before running `coreos-installer`. 

The following example initializes a bootstrap node installation to the `/dev/sda` device. The Ignition config file for the bootstrap node is obtained from an HTTP web server with the IP address 192.168.1.2: 

```shell-session
$ sudo coreos-installer install --ignition-url=http://192.168.1.2:80/installation_directory/bootstrap.ign /dev/sda \
--ignition-hash=sha512-a5a2d43879223273c9b60af66b44202a1d1248fc01cf156c46d4a79f552b6bad47bc8cc78ddf0116e80c59d2ea9e32ba53bc807afbca581aa059311def2c3e3b
```


  8. Monitor the progress of the RHCOS installation on the console of the machine. 

Important

Be sure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of RHCOS installation issues that might arise. 

  9. After RHCOS installs, you must reboot the system. During the system reboot, it applies the Ignition config file that you specified. 
  10. Check the console output to verify that Ignition ran. 

**Example command**

```shell-session
Ignition: ran on 2022/03/14 14:48:33 UTC (this boot)
Ignition: user-provided config was applied
```


  11. Continue to create the other machines for your cluster. 

Important

You must create the bootstrap and control plane machines at this time. If the control plane machines are not made schedulable, also create at least two compute machines before you install OpenShift Container Platform. 

If the required network, DNS, and load balancer infrastructure are in place, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS nodes have rebooted. 

Note

RHCOS nodes do not include a default password for the `core` user. You can access the nodes by running `ssh core@<node>.<cluster_name>.<base_domain>` as a user with access to the SSH private key that is paired to the public key that you specified in your `install_config.yaml` file. OpenShift Container Platform 4 cluster nodes running RHCOS are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, when investigating installation issues, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on a target node, SSH access might be required for debugging or disaster recovery. 




## 1.13.2. Installing RHCOS by using PXE or iPXE booting

You can use PXE or iPXE booting to install RHCOS on the machines. 

**Prerequisites**

  * You have created the Ignition config files for your cluster. 
  * You have configured a suitable network, DNS and load balancing infrastructure. 
  * You have configured suitable PXE or iPXE infrastructure. 
  * You have an HTTP server that can be accessed from your computer, and from the machines that you create. 
  * You have reviewed the _Advanced RHCOS installation configuration_ section for different ways to configure features, such as networking and disk partitioning. 



**Procedure**

  1. Upload the bootstrap, control plane, and compute node Ignition config files that the installation program created to your HTTP server. Note the URLs of these files. 

Important

You can add or change configuration settings in your Ignition configs before saving them to your HTTP server. If you plan to add more compute machines to your cluster after you finish installation, do not delete these files. 

  2. From the installation host, validate that the Ignition config files are available on the URLs. The following example gets the Ignition config file for the bootstrap node: 

```shell-session
$ curl -k http://<HTTP_server>/bootstrap.ign
```


     * `<HTTP_server>`: Replace `bootstrap.ign` with `master.ign` or `worker.ign` in the command to validate that the Ignition config files for the control plane and compute nodes are also available. 

**Example output**

```shell-session
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0{"ignition":{"version":"3.2.0"},"passwd":{"users":[{"name":"core","sshAuthorizedKeys":["ssh-rsa...
```


  3. Although it is possible to obtain the RHCOS `kernel`, `initramfs` and `rootfs` files that are required for your preferred method of installing operating system instances from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/) page, the recommended way to obtain the correct version of your RHCOS files are from the output of `openshift-install` command: 

```shell-session
$ openshift-install coreos print-stream-json | grep -Eo '"https.*(kernel-|initramfs.|rootfs.)\w+(\.img)?"'
```


**Example output**

```shell-session
"<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-kernel-aarch64"
"<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-initramfs.aarch64.img"
"<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-rootfs.aarch64.img"
"<url>/art/storage/releases/rhcos-4.22-ppc64le/49.84.202110081256-0/ppc64le/rhcos-<release>-live-kernel-ppc64le"
"<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live-initramfs.ppc64le.img"
"<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live-rootfs.ppc64le.img"
"<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-kernel-s390x"
"<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-initramfs.s390x.img"
"<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-rootfs.s390x.img"
"<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-kernel-x86_64"
"<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-initramfs.x86_64.img"
"<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-rootfs.x86_64.img"
```


Important

The RHCOS artifacts might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described below for this procedure. RHCOS QCOW2 images are not supported for this installation type. 

The file names contain the OpenShift Container Platform version number. They resemble the following examples: 

     * `kernel`: `rhcos-<version>-live-kernel-<architecture>`
     * `initramfs`: `rhcos-<version>-live-initramfs.<architecture>.img`
     * `rootfs`: `rhcos-<version>-live-rootfs.<architecture>.img`

  4. Upload the `rootfs`, `kernel`, and `initramfs` files to your HTTP server. 

Important

If you plan to add more compute machines to your cluster after you finish installation, do not delete these files. 

  5. Configure the network boot infrastructure so that the machines boot from their local disks after RHCOS is installed on them. 
  6. Configure PXE or iPXE installation for the RHCOS images and begin the installation. 
  7. Modify one of the following example menu entries for your environment and verify that the image and Ignition files are properly accessible: 

     * For PXE (`x86_64`): 

```plaintext
DEFAULT pxeboot
TIMEOUT 20
PROMPT 0
LABEL pxeboot
    KERNEL http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture>
    APPEND initrd=http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/bootstrap.ign
```


where: 

`kernel`
     Specify the location of the live `kernel` file that you uploaded to your HTTP server. The URL must be HTTP, TFTP, or FTP; HTTPS and NFS are not supported. 
`initrd=main`
    

If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC that is named `eno1`, set `ip=eno1:dhcp`. Specify the locations of the RHCOS files that you uploaded to your HTTP server. The `initrd` parameter value is the location of the `initramfs` file, the `coreos.live.rootfs_url` parameter value is the location of the `rootfs` file, and the `coreos.inst.ignition_url` parameter value is the location of the bootstrap Ignition config file. You can also add more kernel arguments to the `APPEND` line to configure networking or other boot options. 

Note

This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `APPEND` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information, see [How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?](https://access.redhat.com/articles/7212) and "Enabling the serial console for PXE and ISO installation" in the "Advanced RHCOS installation configuration" section. 

     * For iPXE (`x86_64` \+ `aarch64` ): 

```plaintext
kernel http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture> initrd=main coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/bootstrap.ign
initrd --name main http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img
boot
```


`kernel`
     Specify the locations of the RHCOS files that you uploaded to your HTTP server. The `kernel` parameter value is the location of the `kernel` file, the `initrd=main` argument is needed for booting on UEFI systems, the `coreos.live.rootfs_url` parameter value is the location of the `rootfs` file, and the `coreos.inst.ignition_url` parameter value is the location of the bootstrap Ignition config file. If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC that is named `eno1`, set `ip=eno1:dhcp`. 
`initrd`
    

Specify the location of the `initramfs` file that you uploaded to your HTTP server. 

Note

This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `kernel` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information, see [How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?](https://access.redhat.com/articles/7212) and "Enabling the serial console for PXE and ISO installation" in the "Advanced RHCOS installation configuration" section. 

Note

To network boot the CoreOS `kernel` on `aarch64` architecture, you need to use a version of iPXE build with the `IMAGE_GZIP` option enabled. See [`IMAGE_GZIP` option in iPXE](https://ipxe.org/buildcfg/image_gzip). 

     * For PXE (with UEFI and Grub as second stage) on `aarch64`: 

```plaintext
menuentry 'Install CoreOS' {
    linux rhcos-<version>-live-kernel-<architecture>  coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/bootstrap.ign
    initrd rhcos-<version>-live-initramfs.<architecture>.img
}
```


where: 

`coreos.live.rootfs_url`
     Specify the locations of the RHCOS files that you uploaded to your HTTP/TFTP server. 
`kernel`
     The `kernel` parameter value is the location of the `kernel` file on your TFTP server. The `coreos.live.rootfs_url` parameter value is the location of the `rootfs` file, and the `coreos.inst.ignition_url` parameter value is the location of the bootstrap Ignition config file on your HTTP Server. If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC that is named `eno1`, set `ip=eno1:dhcp`. 
`initrd rhcos`
     Specify the location of the `initramfs` file that you uploaded to your TFTP server. 

  8. Monitor the progress of the RHCOS installation on the console of the machine. 

Important

Be sure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of RHCOS installation issues that might arise. 

  9. After RHCOS installs, the system reboots. During reboot, the system applies the Ignition config file that you specified. 
  10. Check the console output to verify that Ignition ran. 

**Example command**

```shell-session
Ignition: ran on 2022/03/14 14:48:33 UTC (this boot)
Ignition: user-provided config was applied
```


  11. Continue to create the machines for your cluster. 

Important

You must create the bootstrap and control plane machines at this time. If the control plane machines are not made schedulable, also create at least two compute machines before you install the cluster. 

If the required network, DNS, and load balancer infrastructure are in place, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS nodes have rebooted. 

Note

RHCOS nodes do not include a default password for the `core` user. You can access the nodes by running `ssh core@<node>.<cluster_name>.<base_domain>` as a user with access to the SSH private key that is paired to the public key that you specified in your `install_config.yaml` file. OpenShift Container Platform 4 cluster nodes running RHCOS are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, when investigating installation issues, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on a target node, SSH access might be required for debugging or disaster recovery. 




## 1.13.3. Advanced RHCOS installation configuration

To apply advanced configurations unavailable through default installation methods, manually provision Red Hat Enterprise Linux CoreOS (RHCOS) nodes for OpenShift Container Platform. 

This approach enables granular control over the node infrastructure to meet specific deployment requirements. 

  * Passing kernel arguments to the live installer 
  * Running `coreos-installer` manually from the live system 
  * Customizing a live ISO or PXE boot image 



The advanced configuration topics for manual Red Hat Enterprise Linux CoreOS (RHCOS) installations detailed in this section relate to disk partitioning, networking, and configuring Ignition in different ways. 

## 1.13.4. Networking and bonding options for ISO installations

You can configure advanced options so that you can modify the Red Hat Enterprise Linux CoreOS (RHCOS) manual installation process. The subsequent sections show examples of networking options for an ISO installation. 

If you install RHCOS from an ISO image, you can add kernel arguments manually when you boot the image to configure networking for a node. If no networking arguments are specified, DHCP is activated in the initramfs when RHCOS detects that networking is required to fetch the Ignition config file. 

Important

When adding networking arguments manually, you must also add the `rd.neednet=1` kernel argument to bring the network up in the initramfs. 

The following information provides examples for configuring networking and bonding on your RHCOS nodes for ISO installations. The examples describe how to use the `ip=`, `nameserver=`, and `bond=` kernel arguments. 

Note

Ordering is important when adding the kernel arguments: `ip=`, `nameserver=`, and then `bond=`. 

The networking options are passed to the `dracut` tool during system boot. For more information about the networking options supported by `dracut`, see `dracut.cmdline` manual page. 

**Additional resources**

  * [`dracut.cmdline` manual page](https://www.man7.org/linux/man-pages/man7/dracut.cmdline.7.html)



### 1.13.4.1. Configuring DHCP or static IP addresses

You can configure an IP address by using either DHCP or an individual static IP address. If you set a static IP, you must then identify the DNS server IP address on each node. 

The configuration examples in the procedure, update the IP addresses for the following components: 

  * The node’s IP address to `10.10.10.2`
  * The gateway address to `10.10.10.254`
  * The netmask to `255.255.255.0`
  * The hostname to `core0.example.com`
  * The DNS server address to `4.4.4.41`
  * The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically. 



**Procedure**

  1. Enter a command like the following command to configure a static IP address: 

```shell-session
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
nameserver=4.4.4.41
```


  2. Enter a command like the following command to configure a DHCP IP address: 

```shell-session
ip=enp1s0:dhcp
```


Note

When you use DHCP to configure IP addressing for the RHCOS machines, the machines also obtain the DNS server information through DHCP. For DHCP-based deployments, you can define the DNS server address that is used by the RHCOS nodes through your DHCP server configuration. 

  3. If two or more network interfaces and only one interface exists, disable DHCP on a single interface. In the example, the `enp1s0` interface has a static networking configuration and DHCP is disabled for `enp2s0`, which is not used: 

```shell-session
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
ip=::::core0.example.com:enp2s0:none
```


  4. If you need to combine DHCP and static IP configurations on systems with multiple network interfaces, run the following example command: 

```shell-session
ip=enp1s0:dhcp
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
```


### 1.13.4.2. Configuring an IP address without a static hostname

You can configure an IP address without assigning a static hostname. If a static hostname is not set by the user, the static hostname gets picked up and automatically set by a reverse DNS lookup. 

The configuration examples in the procedure, update the IP addresses for the following components: 

  * The node’s IP address to `10.10.10.2`
  * The gateway address to `10.10.10.254`
  * The netmask to `255.255.255.0`
  * The DNS server address to `4.4.4.41`
  * The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically. 



**Procedure**

  * To configure an IP address without a static hostname, enter a command like the following command: 

```shell-session
ip=10.10.10.2::10.10.10.254:255.255.255.0::enp1s0:none
nameserver=4.4.4.41
```


### 1.13.4.3. Specifying multiple network interfaces and DNS servers

You can specify multiple network interfaces by setting multiple `ip=` entries. You can provide multiple DNS servers by adding a `nameserver=` entry for each server, 

**Procedure**

  * To specify multiple network interfaces for your interfaces, you can enter a command like the following command: 

```shell-session
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
ip=10.10.10.3::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
```


  * To provide multiple DNS servers by adding a `nameserver=` entry for each server, enter a command like the following command: 

```shell-session
nameserver=1.1.1.1
nameserver=8.8.8.8
```


### 1.13.4.4. Configuring default gateway and route

As an optional task, you can configure routes to additional networks by setting an `rd.route=` value. 

Note

When you configure one or multiple networks, one default gateway is required. If the additional network gateway is different from the primary network gateway, the default gateway must be the primary network gateway. 

**Procedure**

  * To configure the default gateway, enter the following command: 

```shell-session
ip=::10.10.10.254::::
```


  * To configure the route for an additional network, enter the following command: 

```shell-session
rd.route=20.20.20.0/24:20.20.20.254:enp2s0
```


### 1.13.4.5. Configuring VLANs on individual interfaces

As an optional task, you can configure VLANs on individual interfaces by using the `vlan=` parameter. 

**Procedure**

  * To configure a VLAN on a network interface and use a static IP address, run the following command: 

```shell-session
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0.100:none
vlan=enp2s0.100:enp2s0
```


  * To configure a VLAN on a network interface and to use DHCP, run the following command: 

```shell-session
ip=enp2s0.100:dhcp
vlan=enp2s0.100:enp2s0
```


### 1.13.4.6. Bonding multiple network interfaces to a single interface

As an optional task, you can bond multiple network interfaces to a single interface by using the `bond=` option. 

The following example demonstrates editing the `/etc/config/network` file and specifying the following syntax for bonding multiple network interfaces to a single interface: 

```shell-session
bond=<name>[:<network_interfaces>][:<options>]
```


  * `<name>`: Specifies the bonding device name, for example `bond0`. 
  * `<network_interfaces>`: Specifies a comma-separated list of physical (ethernet) interfaces, such as `em1,em2`. 
  * `<options>: Specifies a comma-separated list of bonding options. Enter the `modinfo bonding` command to see available options. 



When you create a bonded interface using the `bond=` command, you must specify how the IP address is assigned and other information for the bonded interface. 

**Procedure**

  * To configure the bonded interface to use DHCP, edit the `/etc/config/network` file by setting the IP address for the bond to `dhcp`. For example: 

```shell-session
ip=bond0:dhcp
```


  * To configure the bonded interface to use a static IP address, edit the `/etc/config/network` file entering the specific IP address you want and related information. For example: 

```shell-session
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
```


### 1.13.4.7. Bonding multiple SR-IOV network interfaces to a dual port NIC interface

You can bond multiple SR-IOV network interfaces to a dual port NIC interface by using the `bond=` option. Ensure you apply the procedure tasks to each node. 

**Procedure**

  1. Create the SR-IOV virtual functions (VFs) following the guidance in [Managing SR-IOV devices](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/managing-virtual-devices_configuring-and-managing-virtualization#managing-sr-iov-devices_managing-virtual-devices). Follow the procedure in the "Attaching SR-IOV networking devices to virtual machines" section. 
  2. Create the bond, attach the desired VFs to the bond and set the bond link state up following the guidance in [Configuring network bonding](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/configuring-network-bonding_configuring-and-managing-networking). Follow any of the described procedures to create the bond. 

The following examples illustrate the syntax you must use: 

     * The syntax for configuring a bonded interface is `bond=<name>[:<network_interfaces>][:options]`. 

`<name>` is the bonding device name (`bond0`), `<network_interfaces>` represents the virtual functions (VFs) by their known name in the kernel and shown in the output of the `ip link` command(`eno1f0`, `eno2f0`), and _options_ is a comma-separated list of bonding options. Enter `modinfo bonding` to see available options. 

     * When you create a bonded interface using `bond=`, you must specify how the IP address is assigned and other information for the bonded interface. 

       * To configure the bonded interface to use DHCP, set the bond’s IP address to `dhcp`. For example: 

```shell-session
bond=bond0:eno1f0,eno2f0:mode=active-backup
ip=bond0:dhcp::AA:BB:CC:DD:EE:FF
ip=eno1f0:none::AA:BB:CC:DD:EE:FF
ip=eno2f0:none::AA:BB:CC:DD:EE:FF
```


       * To configure the bonded interface to use a static IP address, enter the specific IP address you want and related information. For example: 

```shell-session
bond=bond0:eno1f0,eno2f0:mode=active-backup
ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
```


  3. Optional: You can use network teaming as an alternative to bonding by using the `team=` parameter. 

     * The syntax for configuring a team interface is: `team=name[:network_interfaces]`

_name_ is the team device name (`team0`) and _network_interfaces_ represents a comma-separated list of physical (ethernet) interfaces (`em1, em2`). 

Note

Teaming is planned to be deprecated when RHCOS switches to an upcoming version of RHEL. For more information, see this [Red Hat Knowledgebase Article](https://access.redhat.com/solutions/6509691). 

Use the following example to configure a network team: 

```shell-session
team=team0:em1,em2
ip=team0:dhcp
```


### 1.13.4.8. coreos-installer and boot options for ISO and PXE installations

You can install RHCOS by running `coreos-installer install <options> <device>` at the command prompt, after booting into the RHCOS live environment from an ISO image. 

The following table shows the subcommands, options, and arguments you can pass to the `coreos-installer` command. 

Table 1.8. coreos-installer subcommands, command-line options, and arguments **coreos-installer install subcommand**  
---  
**_Subcommand_** |  **_Description_**  
`$ coreos-installer install <options> <device>` |  Embed an Ignition config in an ISO image.   
**coreos-installer install subcommand options**  
**_Option_** |  **_Description_**  
`-u`, `--image-url <url>` |  Specify the image URL manually.   
`-f`, `--image-file <path>` |  Specify a local image file manually. Used for debugging.   
`-i,` `--ignition-file <path>` |  Embed an Ignition config from a file.   
`-I`, `--ignition-url <URL>` |  Embed an Ignition config from a URL.   
`--ignition-hash <digest>` |  Digest `type-value` of the Ignition config.   
`-p`, `--platform <name>` |  Override the Ignition platform ID for the installed system.   
`--console <spec>` |  Set the kernel and boot loader console for the installed system. For more information about the format of `<spec>`, see the [Linux kernel serial console](https://www.kernel.org/doc/html/latest/admin-guide/serial-console.html) documentation.   
`--append-karg <arg>…​` |  Append a default kernel argument to the installed system.   
`--delete-karg <arg>…​` |  Delete a default kernel argument from the installed system.   
`-n`, `--copy-network` |  Copy the network configuration from the install environment.  Important The `--copy-network` option only copies networking configuration found under `/etc/NetworkManager/system-connections`. In particular, it does not copy the system hostname.   
`--network-dir <path>` |  For use with `-n`. Default is `/etc/NetworkManager/system-connections/`.   
`--save-partlabel <lx>..` |  Save partitions with this label glob.   
`--save-partindex <id>…​` |  Save partitions with this number or range.   
`--insecure` |  Skip RHCOS image signature verification.   
`--insecure-ignition` |  Allow Ignition URL without HTTPS or hash.   
`--architecture <name>` |  Target CPU architecture. Valid values are `x86_64` and `aarch64`.   
`--preserve-on-error` |  Do not clear partition table on error.   
`-h`, `--help` |  Print help information.   
**coreos-installer install subcommand argument**  
**_Argument_** |  **_Description_**  
`<device>` |  The destination device.   
**coreos-installer ISO subcommands**  
**_Subcommand_** |  **_Description_**  
`$ coreos-installer iso customize <options> <ISO_image>` |  Customize a RHCOS live ISO image.   
`coreos-installer iso reset <options> <ISO_image>` |  Restore a RHCOS live ISO image to default settings.   
`coreos-installer iso ignition remove <options> <ISO_image>` |  Remove the embedded Ignition config from an ISO image.   
**coreos-installer ISO customize subcommand options**  
**_Option_** |  **_Description_**  
`--dest-ignition <path>` |  Merge the specified Ignition config file into a new configuration fragment for the destination system.   
`--dest-console <spec>` |  Specify the kernel and boot loader console for the destination system.   
`--dest-device <path>` |  Install and overwrite the specified destination device.   
`--dest-karg-append <arg>` |  Add a kernel argument to each boot of the destination system.   
`--dest-karg-delete <arg>` |  Delete a kernel argument from each boot of the destination system.   
`--network-keyfile <path>` |  Configure networking by using the specified NetworkManager keyfile for live and destination systems.   
`--ignition-ca <path>` |  Specify an additional TLS certificate authority to be trusted by Ignition.   
`--pre-install <path>` |  Run the specified script before installation.   
`--post-install <path>` |  Run the specified script after installation.   
`--installer-config <path>` |  Apply the specified installer configuration file.   
`--live-ignition <path>` |  Merge the specified Ignition config file into a new configuration fragment for the live environment.   
`--live-karg-append <arg>` |  Add a kernel argument to each boot of the live environment.   
`--live-karg-delete <arg>` |  Delete a kernel argument from each boot of the live environment.   
`--live-karg-replace <k=o=n>` |  Replace a kernel argument in each boot of the live environment, in the form `key=old=new`.   
`-f`, `--force` |  Overwrite an existing Ignition config.   
`-o`, `--output <path>` |  Write the ISO to a new output file.   
`-h`, `--help` |  Print help information.   
**coreos-installer PXE subcommands**  
**_Subcommand_** |  **_Description_**  
Note that not all of these options are accepted by all subcommands.   
`coreos-installer pxe customize <options> <path>` |  Customize a RHCOS live PXE boot config.   
`coreos-installer pxe ignition wrap <options>` |  Wrap an Ignition config in an image.   
`coreos-installer pxe ignition unwrap <options> <image_name>` |  Show the wrapped Ignition config in an image.   
**coreos-installer PXE customize subcommand options**  
**_Option_** |  **_Description_**  
Note that not all of these options are accepted by all subcommands.   
`--dest-ignition <path>` |  Merge the specified Ignition config file into a new configuration fragment for the destination system.   
`--dest-console <spec>` |  Specify the kernel and boot loader console for the destination system.   
`--dest-device <path>` |  Install and overwrite the specified destination device.   
`--network-keyfile <path>` |  Configure networking by using the specified NetworkManager keyfile for live and destination systems.   
`--ignition-ca <path>` |  Specify an additional TLS certificate authority to be trusted by Ignition.   
`--pre-install <path>` |  Run the specified script before installation.   
`post-install <path>` |  Run the specified script after installation.   
`--installer-config <path>` |  Apply the specified installer configuration file.   
`--live-ignition <path>` |  Merge the specified Ignition config file into a new configuration fragment for the live environment.   
`-o,` `--output <path>` |  Write the initramfs to a new output file.  Note This option is required for PXE environments.   
`-h`, `--help` |  Print help information.   
Show more

You can automatically start `coreos-installer` options at boot time by passing `coreos.inst` boot arguments to the RHCOS live installer. These are provided in addition to the standard boot arguments. 

  * For ISO installations, the `coreos.inst` options can be added by interrupting the automatic boot at the boot loader menu. You can interrupt the automatic boot by pressing `TAB` while the **RHEL CoreOS (Live)** menu option is highlighted. 
  * For PXE or iPXE installations, the `coreos.inst` options must be added to the `APPEND` line before the RHCOS live installer is booted. 



The following table shows the RHCOS live installer `coreos.inst` boot options for ISO and PXE installations. 

Table 1.9. coreos.inst boot optionsArgument| Description  
---|---  
`coreos.inst.install_dev` |  Required. The block device on the system to install to.  Note It is recommended to use the full path, such as `/dev/sda`, although `sda` is allowed.   
`coreos.inst.ignition_url` |  Optional: The URL of the Ignition config to embed into the installed system. If no URL is specified, no Ignition config is embedded. Only HTTP and HTTPS protocols are supported.   
`coreos.inst.save_partlabel` |  Optional: Comma-separated labels of partitions to preserve during the install. Glob-style wildcards are permitted. The specified partitions do not need to exist.   
`coreos.inst.save_partindex` |  Optional: Comma-separated indexes of partitions to preserve during the install. Ranges `m-n` are permitted, and either `m` or `n` can be omitted. The specified partitions do not need to exist.   
`coreos.inst.insecure` |  Optional: Permits the OS image that is specified by `coreos.inst.image_url` to be unsigned.   
`coreos.inst.image_url` |  Optional: Download and install the specified RHCOS image. 

  * This argument should not be used in production environments and is intended for debugging purposes only. 
  * While this argument can be used to install a version of RHCOS that does not match the live media, it is recommended that you instead use the media that matches the version you want to install. 
  * If you are using `coreos.inst.image_url`, you must also use `coreos.inst.insecure`. This is because the bare-metal media are not GPG-signed for OpenShift Container Platform. 
  * Only HTTP and HTTPS protocols are supported. 

  
`coreos.inst.skip_reboot` |  Optional: The system will not reboot after installing. After the install finishes, you will receive a prompt that allows you to inspect what is happening during installation. This argument should not be used in production environments and is intended for debugging purposes only.   
`coreos.inst.platform_id` |  Optional: The Ignition platform ID of the platform the RHCOS image is being installed on. Default is `metal`. This option determines whether or not to request an Ignition config from the cloud provider, such as VMware. For example: `coreos.inst.platform_id=vmware`.   
`ignition.config.url` |  Optional: The URL of the Ignition config for the live boot. For example, this can be used to customize how `coreos-installer` is invoked, or to run code before or after the installation. This is different from `coreos.inst.ignition_url`, which is the Ignition config for the installed system.   
Show more
