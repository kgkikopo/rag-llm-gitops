# 2.13. Installing single-node OpenShift with IBM Power

You can install a single-node OpenShift cluster with IBM Power by performing a user-provisioned installation. 

Installing a single-node cluster on IBM Power® requires user-provisioned installation using the "Installing a cluster with IBM Power®" procedure. 

Note

Installing a single-node cluster on IBM Power® simplifies installation for development and test environments and requires less resource requirements at entry level. 

You must meet the following hardware requirements when installing a single-node cluster on IBM Z® and IBM® LinuxONE: 

  * The equivalent of two Integrated Facilities for Linux (IFL), which are SMT2 enabled, for each cluster. 
  * At least one network connection to connect to the `LoadBalancer` service and to serve data for traffic outside of the cluster. 



Note

You can use dedicated or shared IFLs to assign sufficient compute resources. Resource sharing is one of the key strengths of IBM Power®. However, you must adjust capacity correctly on each hypervisor layer and ensure sufficient resources for every OpenShift Container Platform cluster. 

**Additional resources**

  * [Installing a cluster on IBM Power®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power/#installing-ibm-power)



## 2.13.1. Setting up bastion for single-node OpenShift with IBM Power

Before installing single-node OpenShift on IBM Power®, you must set up bastion. 

Setting up a bastion server for single-node OpenShift on IBM Power® requires the configuration of the following services: 

  * PXE is used for the single-node OpenShift cluster installation. PXE requires the following services to be configured and run: 

    * DNS to define api, api-int, and *.apps 
    * DHCP service to enable PXE and assign an IP address to single-node OpenShift node 
    * HTTP to provide ignition and RHCOS rootfs image 
    * TFTP to enable PXE 

  * You must install `dnsmasq` to support DNS, DHCP and PXE, httpd for HTTP. 



Use the following procedure to configure a bastion server that meets these requirements. 

**Procedure**

  1. Use the following command to install `grub2`, which is required to enable PXE for PowerVM: 

```shell-session
grub2-mknetdir --net-directory=/var/lib/tftpboot
```


**Example`/var/lib/tftpboot/boot/grub2/grub.cfg` file**

```shell-session
default=0
fallback=1
timeout=1
if [ ${net_default_mac} == fa:b0:45:27:43:20 ]; then
menuentry "CoreOS (BIOS)" {
   echo "Loading kernel"
   linux "/rhcos/kernel" ip=dhcp rd.neednet=1 ignition.platform.id=metal ignition.firstboot coreos.live.rootfs_url=http://192.168.10.5:8000/install/rootfs.img ignition.config.url=http://192.168.10.5:8000/ignition/sno.ign
   echo "Loading initrd"
   initrd  "/rhcos/initramfs.img"
}
fi
```


  2. Use the following commands to download RHCOS image files from the mirror repo for PXE. 

     1. Enter the following command to assign the `RHCOS_URL` variable the follow 4.12 URL: 

```shell-session
$ export RHCOS_URL=https://mirror.openshift.com/pub/openshift-v4/ppc64le/dependencies/rhcos/4.12/latest/
```


     2. Enter the following command to navigate to the `/var/lib/tftpboot/rhcos` directory: 

```shell-session
$ cd /var/lib/tftpboot/rhcos
```


     3. Enter the following command to download the specified RHCOS kernel file from the URL stored in the `RHCOS_URL` variable: 

```shell-session
$ wget ${RHCOS_URL}/rhcos-live-kernel-ppc64le -o kernel
```


     4. Enter the following command to download the RHCOS `initramfs` file from the URL stored in the `RHCOS_URL` variable: 

```shell-session
$ wget ${RHCOS_URL}/rhcos-live-initramfs.ppc64le.img -o initramfs.img
```


     5. Enter the following command to navigate to the `/var//var/www/html/install/` directory: 

```shell-session
$ cd /var//var/www/html/install/
```


     6. Enter the following command to download, and save, the RHCOS `root filesystem` image file from the URL stored in the `RHCOS_URL` variable: 

```shell-session
$ wget ${RHCOS_URL}/rhcos-live-rootfs.ppc64le.img -o rootfs.img
```


  3. To create the ignition file for a single-node OpenShift cluster, you must create the `install-config.yaml` file. 

     1. Enter the following command to create the work directory that holds the file: 

```shell-session
$ mkdir -p ~/sno-work
```


     2. Enter the following command to navigate to the `~/sno-work` directory: 

```shell-session
$ cd ~/sno-work
```


     3. Use the following sample file can to create the required `install-config.yaml` in the `~/sno-work` directory: 

```yaml
apiVersion: v1
baseDomain: <domain>
compute:
- name: worker
  replicas: 0
controlPlane:
  name: master
  replicas: 1
metadata:
  name: <name>
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
bootstrapInPlace:
  installationDisk: /dev/disk/by-id/<disk_id>
pullSecret: '<pull_secret>'
sshKey: |
  <ssh_key>
```


where: 

`baseDomain`
     Specifies the cluster domain name. 
`compute.replicas`
     Specifies the `compute` replicas to `0`. This makes the control plane node schedulable. 
`controlPlane.replicas`
     Specifies the `controlPlane` replicas to `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node. 
`metadata.name`
     Specifies the cluster name. 
`networking`
     Specifies the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters. 
`machineNetwork.cidr`
     Specifies the `cidr` value to match the subnet of the single-node OpenShift cluster. 
`bootstrapInPlace.installationDisk`
     Specifies the path to the installation disk drive, for example, `/dev/disk/by-id/wwn-0x64cd98f04fde100024684cf3034da5c2`. 
`pullSecret`
     Specifies the `pullSecret` parameter. Copy the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) and add the contents to this configuration setting. 
`sshKey`
     Specifies the `sshKey` parameter. Add the public SSH key from the administration host so that you can log in to the cluster after installation. 

  4. Download the `openshift-install` image to create the ignition file and copy it to the `http` directory. 

     1. Enter the following command to download the `openshift-install-linux-4.12.0` .tar file: 

```shell-session
$ wget https://mirror.openshift.com/pub/openshift-v4/ppc64le/clients/ocp/4.12.0/openshift-install-linux-4.12.0.tar.gz
```


     2. Enter the following command to unpack the `openshift-install-linux-4.12.0.tar.gz` archive: 

```shell-session
$ tar xzvf openshift-install-linux-4.12.0.tar.gz
```


     3. Enter the following command to 

```shell-session
$ ./openshift-install --dir=~/sno-work create create single-node-ignition-config
```


     4. Enter the following command to create the ignition file: 

```shell-session
$ cp ~/sno-work/single-node-ignition-config.ign /var/www/html/ignition/sno.ign
```


     5. Enter the following command to restore SELinux file for the `/var/www/html` directory: 

```shell-session
$ restorecon -vR /var/www/html || true
```


Bastion now has all the required files and is properly configured in order to install single-node OpenShift. 




## 2.13.2. Installing single-node OpenShift with IBM Power

You can install single-node OpenShift with IBM Power. 

There are two steps for the single-node OpenShift cluster installation. First the single-node OpenShift logical partition (LPAR) needs to boot up with PXE, then you need to monitor the installation progress. 

**Prerequisites**

  * You have set up bastion. 



**Procedure**

  1. Use the following command to boot powerVM with netboot: 

```shell-session
$ lpar_netboot -i -D -f -t ent -m <sno_mac> -s auto -d auto -S <server_ip> -C <sno_ip> -G <gateway> <lpar_name> default_profile <cec_name>
```


where: 

sno_mac
     Specifies the MAC address of the single-node OpenShift cluster. 
sno_ip
     Specifies the IP address of the single-node OpenShift cluster. 
server_ip
     Specifies the IP address of bastion (PXE server). 
gateway
     Specifies the Network’s gateway IP. 
lpar_name
     Specifies the single-node OpenShift lpar name in HMC. 
cec_name
     Specifies the System name where the sno_lpar resides 

  2. After the single-node OpenShift LPAR boots up with PXE, use the `openshift-install` command to monitor the progress of installation: 

     1. Run the following command after the bootstrap is complete: 

```shell-session
./openshift-install wait-for bootstrap-complete
```


     2. Run the following command after it returns successfully: 

```shell-session
./openshift-install wait-for install-complete
```
