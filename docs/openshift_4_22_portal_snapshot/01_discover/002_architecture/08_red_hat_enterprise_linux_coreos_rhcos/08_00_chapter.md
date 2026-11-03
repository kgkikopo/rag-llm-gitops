# Chapter 8. Red Hat Enterprise Linux CoreOS (RHCOS)

Red Hat Enterprise Linux CoreOS (RHCOS) represents the next generation of single-purpose container operating system technology by providing the quality standards of Red Hat Enterprise Linux (RHEL) with automated, remote upgrade features. 

RHCOS is supported only as a component of OpenShift Container Platform 4.22 for all OpenShift Container Platform machines. RHCOS is the only supported operating system for all node types in OpenShift Container Platform. RHCOS is deployed in OpenShift Container Platform 4.22 in two general ways: 

  * If you install your cluster on infrastructure that the installation program provisions, RHCOS images are downloaded to the target platform during installation. Suitable Ignition config files, which control the RHCOS configuration, are also downloaded and used to deploy the machines. 
  * If you install your cluster on infrastructure that you manage, you must follow the installation documentation to obtain the RHCOS images, generate Ignition config files, and use the Ignition config files to provision your machines.

- [8.1. Key RHCOS features](08_01_key_rhcos_features.md)
- [8.2. View Ignition configuration files](08_02_view_ignition_configuration_files.md)
- [8.3. Change Ignition configs after installation](08_03_change_ignition_configs_after_installation.md)
