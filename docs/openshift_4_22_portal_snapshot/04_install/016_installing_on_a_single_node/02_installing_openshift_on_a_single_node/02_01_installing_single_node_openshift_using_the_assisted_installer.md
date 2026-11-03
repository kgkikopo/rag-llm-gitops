# 2.1. Installing single-node OpenShift using the Assisted Installer

To install OpenShift Container Platform on a single node, use the web-based Assisted Installer wizard to guide you through the process and manage the installation. 

See "Installing OpenShift Container Platform with the Assisted Installer" for details and configuration options. 

**Additional resources**

  * [Installing OpenShift Container Platform with the Assisted Installer](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2026/html/installing_openshift_container_platform_with_the_assisted_installer/index)



## 2.1.1. Generating the discovery ISO with the Assisted Installer

Installing OpenShift Container Platform on a single node requires a discovery ISO, which the Assisted Installer can generate. 

**Procedure**

  1. On the administration host, open a browser and navigate to [Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/assisted-installer/clusters). 
  2. Click **Create New Cluster** to create a new cluster. 
  3. In the **Cluster name** field, enter a name for the cluster. 
  4. In the **Base domain** field, enter a base domain. For example: 

```plaintext
example.com
```


All DNS records must be subdomains of this base domain and include the cluster name, for example: 

```plaintext
<cluster_name>.example.com
```


Note

You cannot change the base domain or cluster name after cluster installation. 

  5. Select **Install single node OpenShift (SNO)** and complete the rest of the wizard steps. Download the discovery ISO. 
  6. Complete the remaining Assisted Installer wizard steps. 

Important

Ensure that you take note of the discovery ISO URL for installing with virtual media. 

If you enable OpenShift Virtualization during this process, you must have a second local storage device of at least 50GiB for your virtual machines. 




**Additional resources**

  * [Persistent storage using logical volume manager storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-lvms_logical-volume-manager-storage)
  * [OpenShift Virtualization capabilities](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/virtualization/#virt-what-you-can-do-with-virt_about-virt)



## 2.1.2. Installing single-node OpenShift with the Assisted Installer

Use the Assisted Installer to install the single-node cluster. 

**Prerequisites**

  * Ensure that the boot drive order in the server BIOS settings defaults to booting the server from the target installation disk. 



**Procedure**

  1. Attach the discovery ISO image to the target host. 
  2. Boot the server from the discovery ISO image. The discovery ISO image writes the system configuration to the target installation disk and automatically triggers a server restart. 
  3. On the administration host, return to the browser. Wait for the host to appear in the list of discovered hosts. If necessary, reload the [**Assisted Clusters**](https://console.redhat.com/openshift/assisted-installer/clusters) page and select the cluster name. 
  4. Complete the install wizard steps. Add networking details, including a subnet from the available subnets. Add the SSH public key if necessary. 
  5. Monitor the installation’s progress. Watch the cluster events. After the installation process finishes writing the operating system image to the server’s hard disk, the server restarts. 
  6. Optional: Remove the discovery ISO image. 

The server restarts several times automatically, deploying the control plane. 




**Additional resources**

  * [Creating a bootable ISO image on a USB drive](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_a_single_node/install-sno-installing-sno#installing-with-usb-media_install-sno-installing-sno-with-the-assisted-installer "2.9. Creating a bootable ISO image on a USB drive")
  * [Booting from an HTTP-hosted ISO image using the Redfish API](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_a_single_node/install-sno-installing-sno#install-booting-from-an-iso-over-http-redfish_install-sno-installing-sno-with-the-assisted-installer "2.10. Booting from an HTTP-hosted ISO image using the Redfish API")
  * [Adding worker nodes to single-node OpenShift clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-sno-worker-nodes)
