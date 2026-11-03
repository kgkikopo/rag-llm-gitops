# 2.12. Installing single-node OpenShift with IBM Z and IBM LinuxONE

You can install a single-node OpenShift cluster with IBM Z and IBM LinuxONE by performing a user-provisioned installation. 

Installing a single-node cluster on IBM Z® and IBM® LinuxONE requires user-provisioned installation using one of the following procedures: 

  * "Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE" 
  * "Installing a cluster with RHEL KVM on IBM Z® and IBM® LinuxONE" 
  * "Installing a cluster in an LPAR on IBM Z® and IBM® LinuxONE" 



Note

Installing a single-node cluster on IBM Z® simplifies installation for development and test environments and requires less resource requirements at entry level. 

You must meet the following hardware requirements when installing a single-node cluster on IBM Z® and IBM® LinuxONE: 

  * The equivalent of two Integrated Facilities for Linux (IFL), which are SMT2 enabled, for each cluster. 
  * At least one network connection to both connect to the `LoadBalancer` service and to serve data for traffic outside the cluster. 



Note

You can use dedicated or shared IFLs to assign sufficient compute resources. Resource sharing is one of the key strengths of IBM Z®. However, you must adjust capacity correctly on each hypervisor layer and ensure sufficient resources for every OpenShift Container Platform cluster. 

**Additional resources**

  * [Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z)
  * [Installing a cluster with RHEL KVM on IBM Z® and IBM® LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z-kvm)
  * [Installing a cluster in an LPAR on IBM Z® and IBM® LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z-lpar)



## 2.12.1. Installing single-node OpenShift with z/VM on IBM Z and IBM LinuxONE

You can install single-node OpenShift with z/VM on IBM Z and IBM LinuxONE. 

**Prerequisites**

  * You have installed `podman`. 



**Procedure**

  1. Set the OpenShift Container Platform version by running the following command: 

```shell-session
$ OCP_VERSION=<ocp_version>
```


Replace `<ocp_version>` with the current version. For example, `latest-4.22`. 

  2. Set the host architecture by running the following command: 

```shell-session
$ ARCH=<architecture>
```


Replace `<architecture>` with the target host architecture `s390x`. 

  3. Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands: 

```shell-session
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-client-linux.tar.gz -o oc.tar.gz
```


```shell-session
$ tar zxf oc.tar.gz
```


```shell-session
$ chmod +x oc
```


  4. Download the OpenShift Container Platform installer and make it available for use by entering the following commands: 

```shell-session
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
```


```shell-session
$ tar zxvf openshift-install-linux.tar.gz
```


```shell-session
$ chmod +x openshift-install
```


  5. Prepare the `install-config.yaml` file: 

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

  6. Generate OpenShift Container Platform assets by running the following commands: 

```shell-session
$ mkdir ocp
```


```shell-session
$ cp install-config.yaml ocp
```


```shell-session
$ ./openshift-install --dir=ocp create single-node-ignition-config
```


  7. Obtain the RHEL `kernel`, `initramfs`, and `rootfs` artifacts from the "Product Downloads" page on the Red Hat Customer Portal or from the "RHCOS image mirror" page. 

Important

The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described in the following procedure. 

The file names contain the OpenShift Container Platform version number. They resemble the following examples: 

`kernel`
     `rhcos-<version>-live-kernel-<architecture>`
`initramfs`
     `rhcos-<version>-live-initramfs.<architecture>.img`
`rootfs`
    

`rhcos-<version>-live-rootfs.<architecture>.img`

Note

The `rootfs` image is the same for FCP and DASD. 

  8. Move the following artifacts and files to an HTTP or HTTPS server: 

     * Downloaded RHEL live `kernel`, `initramfs`, and `rootfs` artifacts 
     * Ignition files 

  9. Create parameter files for a particular virtual machine: 

**Example parameter file**

```shell-session
cio_ignore=all,!condev rd.neednet=1 \
console=ttysclp0 \
ignition.firstboot ignition.platform.id=metal \
ignition.config.url=http://<http_server>:8080/ignition/bootstrap-in-place-for-live-iso.ign \
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \
ip=<ip>::<gateway>:<mask>:<hostname>::none nameserver=<dns> \
rd.znet=qeth,0.0.bdd0,0.0.bdd1,0.0.bdd2,layer2=1 \
rd.dasd=0.0.4411 \
rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \
zfcp.allow_lun_scan=0
```


     * For the `ignition.config.url=` parameter, specify the Ignition file for the machine role. Only HTTP and HTTPS protocols are supported. 
     * For the `coreos.live.rootfs_url=` artifact, specify the matching `rootfs` artifact for the `kernel`and `initramfs` you are booting. Only HTTP and HTTPS protocols are supported. 
     * For the `ip=` parameter, assign the IP address automatically using DHCP or manually as described in "Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE". 
     * For installations on DASD-type disks, use `rd.dasd=` to specify the DASD where RHCOS is to be installed. Omit this entry for FCP-type disks. 
     * For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where RHCOS is to be installed. Omit this entry for DASD-type disks. 

Leave all other parameters unchanged. 

  10. Transfer the following artifacts, files, and images to z/VM. For example by using FTP: 

     * `kernel` and `initramfs` artifacts 
     * Parameter files 
     * RHCOS images 

For details about how to transfer the files with FTP and boot from the virtual reader, see "Installing under Z/VM" in the RHCOS documentation. 

  11. Punch the files to the virtual reader of the z/VM guest virtual machine that is to become your bootstrap node. 
  12. Log in to CMS on the bootstrap machine. 
  13. IPL the bootstrap machine from the reader by running the following command: 

```plaintext
$ cp ipl c
```


  14. After the first reboot of the virtual machine, run the following commands directly after one another: 

     1. To boot a DASD device after first reboot, run the following commands: 

```shell-session
$ cp i <devno> clear loadparm prompt
```


Replace `<devno>` with the device number of the boot device as seen by the guest. 

```shell-session
$ cp vi vmsg 0 <kernel_parameters>
```


Replace `<kernel_parameters>` with a set of kernel parameters to be stored as system control program data (SCPDATA). When booting Linux, these kernel parameters are concatenated to the end of the existing kernel parameters that are used by your boot configuration. The combined parameter string must not exceed 896 characters. 

     2. To boot an FCP device after first reboot, run the following commands: 

```shell-session
$ cp set loaddev portname <wwpn> lun <lun>
```


Replace `<wwpn>` with the target port and `<lun>` with the logical unit in hexadecimal format. 

```shell-session
$ cp set loaddev bootprog <n>
```


Replace `<n>` with the kernel to be booted. 

```shell-session
$ cp set loaddev scpdata {APPEND|NEW} '<kernel_parameters>'
```


where: 

`<kernel_parameters>`
     Specifies a set of kernel parameters to be stored as system control program data (SCPDATA). When booting Linux, these kernel parameters are concatenated to the end of the existing kernel parameters that are used by your boot configuration. The combined parameter string must not exceed 896 characters. 
`<APPEND|NEW>`
     Optional: Specify `APPEND` to append kernel parameters to existing SCPDATA. This is the default. Specify `NEW` to replace existing SCPDATA. 

```shell-session
$ cp set loaddev scpdata 'rd.zfcp=0.0.8001,0x500507630a0350a4,0x4000409D00000000
ip=encbdd0:dhcp::02:00:00:02:34:02 rd.neednet=1'
```


To start the IPL and boot process, run the following command: 

```shell-session
$ cp i <devno>
```


Replace `<devno>` with the device number of the boot device as seen by the guest. 




**Additional resources**

  * [Product Downloads](https://access.redhat.com/downloads/content/290)
  * [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/s390x/dependencies/rhcos/latest/)
  * [Installing under Z/VM](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/installation_guide/sect-installing-zvm-s390)



## 2.12.2. Installing single-node OpenShift with RHEL KVM on IBM Z and IBM LinuxONE

You can install single-node OpenShift with with RHEL KVM on IBM Z and IBM LinuxONE. 

**Prerequisites**

  * You have installed `podman`. 



**Procedure**

  1. Set the OpenShift Container Platform version by running the following command: 

```shell-session
$ OCP_VERSION=<ocp_version>
```


Replace `<ocp_version>` with the current version. For example, `latest-4.22`. 

  2. Set the host architecture by running the following command: 

```shell-session
$ ARCH=<architecture>
```


Replace `<architecture>` with the target host architecture `s390x`. 

  3. Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands: 

```shell-session
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-client-linux.tar.gz -o oc.tar.gz
```


```shell-session
$ tar zxf oc.tar.gz
```


```shell-session
$ chmod +x oc
```


  4. Download the OpenShift Container Platform installer and make it available for use by entering the following commands: 

```shell-session
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
```


```shell-session
$ tar zxvf openshift-install-linux.tar.gz
```


```shell-session
$ chmod +x openshift-install
```


  5. Prepare the `install-config.yaml` file: 

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

  6. Generate OpenShift Container Platform assets by running the following commands: 

```shell-session
$ mkdir ocp
```


```shell-session
$ cp install-config.yaml ocp
```


```shell-session
$ ./openshift-install --dir=ocp create single-node-ignition-config
```


  7. Obtain the RHEL `kernel`, `initramfs`, and `rootfs` artifacts from the [Product Downloads](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal or from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/s390x/dependencies/rhcos/latest/) page. 

Important

The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described in the following procedure. 

The file names contain the OpenShift Container Platform version number. They resemble the following examples: 

`kernel`
     `rhcos-<version>-live-kernel-<architecture>`
`initramfs`
     `rhcos-<version>-live-initramfs.<architecture>.img`
`rootfs`
     `rhcos-<version>-live-rootfs.<architecture>.img`

  8. Before you launch `virt-install`, move the following files and artifacts to an HTTP or HTTPS server: 

     * Downloaded RHEL live `kernel`, `initramfs`, and `rootfs` artifacts 
     * Ignition files 

  9. Create the KVM guest nodes by using the following components: 

     * RHEL `kernel` and `initramfs` artifacts 
     * Ignition files 
     * The new disk image 
     * Adjusted parm line arguments 

```shell-session
$ virt-install \
   --name <vm_name> \
   --autostart \
   --memory=<memory_mb> \
   --cpu host \
   --vcpus <vcpus> \
   --location <media_location>,kernel=<rhcos_kernel>,initrd=<rhcos_initrd> \
   --disk size=100 \
   --network network=<virt_network_parm> \
   --graphics none \
   --noautoconsole \
   --extra-args "rd.neednet=1 ignition.platform.id=metal ignition.firstboot" \
   --extra-args "ignition.config.url=http://<http_server>/bootstrap.ign" \
   --extra-args "coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img" \
   --extra-args "ip=<ip>::<gateway>:<mask>:<hostname>::none" \
   --extra-args "nameserver=<dns>" \
   --extra-args "console=ttysclp0" \
   --wait
```


     * For the `--location` parameter, specify the location of the kernel/initrd on the HTTP or HTTPS server. 
     * For the `ignition.config.url=` artifact, specify the location of the `bootstrap.ign` config file. Only HTTP and HTTPS protocols are supported. 
     * For the `coreos.live.rootfs_url=` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` you are booting. Only HTTP and HTTPS protocols are supported. 
     * For the `ip=` parameter, assign the IP address manually as described in "Installing a cluster with RHEL KVM on IBM Z® and IBM® LinuxONE". 




## 2.12.3. Installing single-node OpenShift in an LPAR on IBM Z and IBM LinuxONE

You can install single-node OpenShift in an LPAR on IBM Z and IBM LinuxONE. 

**Prerequisites**

  * If you are deploying a single-node cluster there are zero compute nodes, the Ingress Controller pods run on the control plane nodes. In single-node cluster deployments, you must configure your application ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. See the _Load balancing requirements for user-provisioned infrastructure_ section for more information. 



**Procedure**

  1. Set the OpenShift Container Platform version by running the following command: 

```shell-session
$ OCP_VERSION=<ocp_version>
```


Replace `<ocp_version>` with the current version. For example, `latest-4.22`. 

  2. Set the host architecture by running the following command: 

```shell-session
$ ARCH=<architecture>
```


Replace `<architecture>` with the target host architecture `s390x`. 

  3. Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands: 

```shell-session
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-client-linux.tar.gz -o oc.tar.gz
```


```shell-session
$ tar zxvf oc.tar.gz
```


```shell-session
$ chmod +x oc
```


  4. Download the OpenShift Container Platform installer and make it available for use by entering the following commands: 

```shell-session
$ curl -k https://mirror.openshift.com/pub/openshift-v4/${ARCH}/clients/ocp/${OCP_VERSION}/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
```


```shell-session
$ tar zxvf openshift-install-linux.tar.gz
```


```shell-session
$ chmod +x openshift-install
```


  5. Prepare the `install-config.yaml` file: 

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
`pullSecret`
     Specifies the `pullSecret` parameter. Copy the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) and add the contents to this configuration setting. 
`sshKey`
     Specifies the `sshKey` parameter. Add the public SSH key from the administration host so that you can log in to the cluster after installation. 

  6. Generate OpenShift Container Platform assets by running the following commands: 

```shell-session
$ mkdir ocp
```


```shell-session
$ cp install-config.yaml ocp
```


  7. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster: 

```shell-session
$ ./openshift-install create manifests --dir <installation_directory>
```


Replace `<installation_directory>` with the installation directory that contains the `install-config.yaml` file you created. 

  8. Check that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `true`. 

     1. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file. 
     2. Locate the `mastersSchedulable` parameter and ensure that it is set to `true` as shown in the following `spec` stanza: 

```yaml
spec:
  mastersSchedulable: true
status: {}
```


     3. Save and exit the file. 

  9. Create the Ignition configuration files by running the following command from the directory that contains the installation program: 

```shell-session
$ ./openshift-install create ignition-configs --dir <installation_directory>
```


Replace `<installation_directory>` with the same installation directory. 

  10. Obtain the RHEL `kernel`, `initramfs`, and `rootfs` artifacts from the [Product Downloads](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal or from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/s390x/dependencies/rhcos/latest/) page. 

Important

The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described in the following procedure. 

The file names contain the OpenShift Container Platform version number. They resemble the following examples: 

`kernel`
     `rhcos-<version>-live-kernel-<architecture>`
`initramfs`
     `rhcos-<version>-live-initramfs.<architecture>.img`
`rootfs`
    

`rhcos-<version>-live-rootfs.<architecture>.img`

Note

The `rootfs` image is the same for FCP and DASD. 

  11. Move the following artifacts and files to an HTTP or HTTPS server: 

     * Downloaded RHEL live `kernel`, `initramfs`, and `rootfs` artifacts 
     * Ignition files 

  12. Create a parameter file for the bootstrap in an LPAR: 

**Example parameter file for the bootstrap machine**

```shell-session
cio_ignore=all,!condev rd.neednet=1 \
console=ttysclp0 \
coreos.inst.install_dev=/dev/<block_device> \
coreos.inst.ignition_url=http://<http_server>/bootstrap.ign \
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \
ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
rd.znet=qeth,0.0.1140,0.0.1141,0.0.1142,layer2=1,portno=0 \
rd.dasd=0.0.4411 \
rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \
zfcp.allow_lun_scan=0
```


     * For the `coreos.inst.install_dev=` artifact, specify the block device on the system to install to. For installations on DASD-type disk use `dasda`, for installations on FCP-type disks use `sda`. 
     * For the `coreos.inst.ignition_url=` artifact, specify the location of the `bootstrap.ign` config file. Only HTTP and HTTPS protocols are supported. 
     * For the `coreos.live.rootfs_url=` artifact, specify the matching `rootfs` artifact for the `kernel`and `initramfs` you are booting. Only HTTP and HTTPS protocols are supported. 
     * For the `ip=` parameter, assign the IP address manually as described in "Installing a cluster in an LPAR on IBM Z® and IBM® LinuxONE". 
     * For installations on DASD-type disks, use `rd.dasd=` to specify the DASD where RHCOS is to be installed. Omit this entry for FCP-type disks. 
     * For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where RHCOS is to be installed. Omit this entry for DASD-type disks. 

You can adjust further parameters if required. 

  13. Create a parameter file for the control plane in an LPAR: 

**Example parameter file for the control plane machine**

```shell-session
cio_ignore=all,!condev rd.neednet=1 \
console=ttysclp0 \
coreos.inst.install_dev=/dev/<block_device> \
coreos.inst.ignition_url=http://<http_server>/master.ign \
coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \
ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
rd.znet=qeth,0.0.1140,0.0.1141,0.0.1142,layer2=1,portno=0 \
rd.dasd=0.0.4411 \
rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \
zfcp.allow_lun_scan=0
```


For the `coreos.inst.ignition_url=` artifact, specify the location of the `master.ign` config file. Only HTTP and HTTPS protocols are supported. 

  14. Transfer the following artifacts, files, and images to the LPAR. For example by using FTP: 

     * `kernel` and `initramfs` artifacts 
     * Parameter files 
     * RHCOS images 

For details about how to transfer the files with FTP and boot, see [Installing in an LPAR](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/performing_a_standard_rhel_9_installation/assembly_installing-on-64-bit-ibm-z_installing-rhel#installing-in-an-lpar_installing-in-an-lpar). 

  15. Boot the bootstrap machine. 
  16. Boot the control plane machine.
