# Chapter 4. Configuring additional devices in an IBM Z or IBM LinuxONE environment

After installing OpenShift Container Platform, you can configure additional devices for your cluster in an IBM Z® or IBM® LinuxONE environment, which is installed with z/VM. 

The following devices can be configured: 

  * Fibre Channel Protocol (FCP) host 
  * FCP LUN 
  * DASD 
  * qeth 



You can configure devices by adding udev rules by using the Machine Config Operator (MCO) or you can configure devices manually. 

Note

The procedures described here apply only to z/VM installations. If you have installed your cluster with RHEL KVM on IBM Z® or IBM® LinuxONE infrastructure, no additional configuration is needed inside the KVM guest after the devices were added to the KVM guests. However, both in z/VM and RHEL KVM environments the next steps to configure the Local Storage Operator and Kubernetes NMState Operator need to be applied. 

**Additional resources**

  * [Machine configuration overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#machine-config-overview)

- [4.1. Configuring additional devices by using the Machine Config Operator](04_01_configuring_additional_devices_by_using_the_machine_config_operator.md)
- [4.2. Configuring additional devices manually](04_02_configuring_additional_devices_manually.md)
- [4.3. RoCE network cards](04_03_roce_network_cards.md)
- [4.4. Enabling multipathing for FCP LUNs](04_04_enabling_multipathing_for_fcp_luns.md)
