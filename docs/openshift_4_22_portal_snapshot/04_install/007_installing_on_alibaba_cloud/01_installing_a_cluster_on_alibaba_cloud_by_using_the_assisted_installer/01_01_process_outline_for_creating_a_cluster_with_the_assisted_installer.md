# 1.1. Process outline for creating a cluster with the Assisted Installer

You can install an OpenShift Container Platform cluster on Alibaba Cloud by using both the Assisted Installer and the Alibaba Cloud consoles. 

The main steps of the installation process are as follows: 

  1. Create the cluster with the Assisted Installer and download the generated image. 
  2. Convert the image to `QCOW2` format. For more information, see the following section. 
  3. Upload the image to the Object Storage Service bucket in Alibaba Cloud. 
  4. Import the image to the Elastic Compute Service in Alibaba Cloud. 
  5. Provision the Alibaba Cloud resources: 

     1. In the Virtual Private Cloud (VPC) console, set the networking configurations. 
     2. In the Alibaba Cloud DNS console, define the Domain Name System. 
     3. In the Elastic Compute Service (ECS) console, provision the compute instances. 

  6. Complete host discovery in the Assisted Installer. 
  7. Complete the network configurations in Alibaba Cloud. 
  8. Complete the cluster configuration and installation in the Assisted Installer. 



**Additional resources**

  * [Installing OpenShift Container Platform with the Assisted Installer](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025)
