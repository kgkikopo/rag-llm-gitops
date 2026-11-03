# 1.5. About Red Hat Enterprise Linux CoreOS (RHCOS) and Ignition

Red Hat Enterprise Linux CoreOS (RHCOS) is a single-purpose container operating system that uses Ignition for initial configuration during cluster deployment. 

As a cluster administrator, you can perform the following Red Hat Enterprise Linux CoreOS (RHCOS) tasks: 

  * Learn about the next generation of single-purpose container operating system technology. 
  * Choose how to configure Red Hat Enterprise Linux CoreOS (RHCOS) 
  * Choose how to deploy Red Hat Enterprise Linux CoreOS (RHCOS): 

    * Installer-provisioned deployment 
    * User-provisioned deployment 




The OpenShift Container Platform installation program creates the Ignition configuration files that you need to deploy your cluster. Red Hat Enterprise Linux CoreOS (RHCOS) uses Ignition during the initial configuration to perform common disk tasks, such as partitioning, formatting, writing files, and configuring users. During the first boot, Ignition reads its configuration from the installation media or the location that you specify and applies the configuration to the machines. 

You can learn how Ignition works, the process for a Red Hat Enterprise Linux CoreOS (RHCOS) machine in an OpenShift Container Platform cluster, view Ignition configuration files, and change Ignition configuration after an installation.
