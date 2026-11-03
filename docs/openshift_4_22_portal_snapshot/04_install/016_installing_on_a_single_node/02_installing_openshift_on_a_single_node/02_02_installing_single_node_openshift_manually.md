# 2.2. Installing single-node OpenShift manually

To install OpenShift Container Platform on a single node, first generate the installation ISO, and then boot the server from the ISO. You can monitor the installation using the `openshift-install` installation program. 

**Additional resources**

  * [Networking requirements for user-provisioned infrastructure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installation-network-user-infra_installing-bare-metal-network-customizations)
  * [User-provisioned DNS requirements](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installation-dns-user-infra_installing-bare-metal-network-customizations)
  * [Configuring DHCP or static IP addresses](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#configuring-dhcp-or-static-ip-addresses_installing-bare-metal-network-customizations)



## 2.2.1. Generating the installation ISO with coreos-installer

You can install OpenShift Container Platform on a single node by generating an installation ISO. 

**Prerequisites**

  * Install `podman`. 



Note

See "Requirements for installing OpenShift on a single node" for networking requirements, including DNS records. 

**Procedure**

  1. Set the OpenShift Container Platform version: 

```shell-session
$ export OCP_VERSION=<ocp_version>
```


Replace `<ocp_version>` with the current version, for example, `latest-4.22`

  2. Set the target cluster architecture: 

```shell-session
$ export ARCH=<architecture>
```


Replace `<architecture>` with the target host architecture, for example, `aarch64` or `x86_64`. 

  3. Set the installation host architecture: 

```shell-session
$ export HOST_ARCH=$(uname -m)
```


This command detects the architecture of the installation host. If the installation host architecture differs from the target cluster architecture, the downloaded binaries must match the installation host. For example, if you are installing an `aarch64` cluster from an `x86_64` bastion host, `HOST_ARCH` is `x86_64`. 

  4. Download the OpenShift Container Platform client (`oc`) and make it available for use by entering the following commands: 

```shell-session
$ curl -k https://mirror.openshift.com/pub/openshift-v4/$HOST_ARCH/clients/ocp/$OCP_VERSION/openshift-client-linux.tar.gz -o oc.tar.gz
```


```shell-session
$ tar zxf oc.tar.gz
```


```shell-session
$ chmod +x oc
```


  5. Download the OpenShift Container Platform installer and make it available for use by entering the following commands: 

```shell-session
$ curl -k https://mirror.openshift.com/pub/openshift-v4/$HOST_ARCH/clients/ocp/$OCP_VERSION/openshift-install-linux.tar.gz -o openshift-install-linux.tar.gz
```


```shell-session
$ tar zxvf openshift-install-linux.tar.gz
```


```shell-session
$ chmod +x openshift-install
```


  6. Retrieve the RHCOS ISO URL by running the following command: 

```shell-session
$ export ISO_URL=$(./openshift-install coreos print-stream-json | grep location | grep $ARCH | grep iso | cut -d\" -f4)
```


  7. Download the RHCOS ISO: 

```shell-session
$ curl -L $ISO_URL -o rhcos-live.iso
```


  8. Prepare the `install-config.yaml` file: 

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
     Specifies the value of `compute.replicas` as `0`. This makes the control plane node schedulable. 
`controlPlane.replicas`
     Specifies the value of `controlPlane.replicas` as `1`. In conjunction with the previous `compute` setting, this setting ensures the cluster runs on a single node. 
`metadata.name`
     Specifies the `metadata` name to the cluster name. 
`networking`
     Specifies the `networking` details. OVN-Kubernetes is the only allowed network plugin type for single-node clusters. 
`machineNetwork.cidr`
     Specifies the `cidr` value to match the subnet of the cluster. 
`installationDisk`
     Specifies the path to the installation disk drive, for example, `/dev/disk/by-id/wwn-0x64cd98f04fde100024684cf3034da5c2`. 
`pullSecret`
     Specifies the `pullSecret` parameter. Copy the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) and add the contents to this configuration setting. 
`sshKey`
     Specifies the `sshKey` parameter. Add the public SSH key from the administration host so that you can log in to the cluster after installation. 

  9. Generate OpenShift Container Platform assets by running the following commands: 

```shell-session
$ mkdir ocp
```


```shell-session
$ cp install-config.yaml ocp
```


```shell-session
$ ./openshift-install --dir=ocp create single-node-ignition-config
```


  10. Embed the ignition data into the RHCOS ISO by running the following commands: 

```shell-session
$ alias coreos-installer='podman run --privileged --pull always --rm \
        -v /dev:/dev -v /run/udev:/run/udev -v $PWD:/data \
        -w /data quay.io/coreos/coreos-installer:release'
```


```shell-session
$ coreos-installer iso ignition embed -fi ocp/bootstrap-in-place-for-live-iso.ign rhcos-live.iso
```


Important

The SSL certificates for the RHCOS ISO installation image are only valid for 24 hours. If you use the ISO image to install a node more than 24 hours after creating the image, the installation can fail. To re-create the image after 24 hours, delete the `ocp` directory and re-create the OpenShift Container Platform assets. 




**Additional resources**

  * [Requirements for installing OpenShift on a single node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_a_single_node/preparing-to-install-sno "Chapter 1. Preparing to install on a single node")
  * [Cluster capabilities](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#cluster-capabilities)
  * [Optional cluster capabilities in OpenShift Container Platform 4.22](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#explanation_of_capabilities_cluster-capabilities)



## 2.2.2. Monitoring the cluster installation using openshift-install

Use the `openshift-install` binary to monitor the progress of the single-node cluster installation. 

**Prerequisites**

  * Ensure that the boot drive order in the server BIOS settings defaults to booting the server from the target installation disk. 



**Procedure**

  1. Attach the discovery ISO image to the target host. 
  2. Boot the server from the discovery ISO image. The discovery ISO image writes the system configuration to the target installation disk and automatically triggers a server restart. 
  3. On the administration host, monitor the installation by running the following command: 

```shell-session
$ ./openshift-install --dir=ocp wait-for install-complete
```


  4. Optional: Remove the discovery ISO image. 

The server restarts several times while deploying the control plane. 




**Verification**

  * After the installation is complete, check the environment by running the following command: 

```shell-session
$ export KUBECONFIG=ocp/auth/kubeconfig
```


```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME                         STATUS   ROLES           AGE     VERSION
control-plane.example.com    Ready    master,worker   10m     v1.35.4
```


**Additional resources**

  * [Creating a bootable ISO image on a USB drive](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_a_single_node/install-sno-installing-sno#installing-with-usb-media_install-sno-installing-sno-with-the-assisted-installer "2.9. Creating a bootable ISO image on a USB drive")
  * [Booting from an HTTP-hosted ISO image using the Redfish API](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_a_single_node/install-sno-installing-sno#install-booting-from-an-iso-over-http-redfish_install-sno-installing-sno-with-the-assisted-installer "2.10. Booting from an HTTP-hosted ISO image using the Redfish API")
  * [Adding worker nodes to single-node OpenShift clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-sno-worker-nodes)
