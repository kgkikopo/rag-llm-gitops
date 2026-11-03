# 1.1. Choosing a method to install OpenShift Container Platform on IBM Z or IBM LinuxONE

OpenShift Container Platform supports many installation methods on IBM Z® and IBM® LinuxONE. The method you select depends on your network environment, the level of infrastructure control you require, and whether your deployment connects to the internet. 

The OpenShift Container Platform installation program offers the following methods for deploying a cluster on IBM Z®: 

  * **Interactive** : You can deploy a cluster with the web-based Assisted Installer. This method requires no setup for the installation program, and is ideal for connected environments such as IBM Z®. 
  * **Local Agent-based** : You can deploy a cluster locally with the Agent-based Installer. It provides many of the benefits of the Assisted Installer, but you must download and configure the Agent-based Installer first. You complete the configuration with a command-line interface (CLI). This approach is ideal for disconnected networks. 
  * **Full control** : You can deploy a cluster on infrastructure that you prepare and support, which provides maximum customizability. You can deploy clusters in connected or disconnected environments. 



Table 1.1. IBM Z(R) installation options | Assisted Installer| Agent-based Installer| User-provisioned installation| Installer-provisioned installation  
---|---|---|---|---  
IBM Z® with z/VM  |  ✓  |  ✓  |  ✓  |   
Restricted network IBM Z® with z/VM  |  |  ✓  |  ✓  |   
IBM Z® with RHEL KVM  |  ✓  |  ✓  |  ✓  |   
Restricted network IBM Z® with RHEL KVM  |  |  ✓  |  ✓  |   
IBM Z® in an LPAR  |  ✓  |  ✓  |  ✓  |   
Restricted network IBM Z® in an LPAR  |  |  ✓  |  ✓  |   
Show more

For more information about the installation process, see Installation process in the Additional resources section.
