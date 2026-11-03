# Chapter 1. Machine configuration overview

You can make changes to the operating systems on OpenShift Container Platform nodes by creating `MachineConfig` objects, which are managed by the Machine Config Operator. For example, you can use the Machine Config Operator (MCO) and machine configs to manage systemd, CRI-O and kubelet, the kernel, Network Manager, and other system features. 

Tasks in this section describe how to use features of the Machine Config Operator to configure operating system features on OpenShift Container Platform nodes. 

Important

NetworkManager stores new network configurations to `/etc/NetworkManager/system-connections/` in a key file format. 

Previously, NetworkManager stored new network configurations to `/etc/sysconfig/network-scripts/` in the `ifcfg` format. Starting with RHEL 9.0, RHEL stores new network configurations at `/etc/NetworkManager/system-connections/` in a key file format. The connections configurations stored to `/etc/sysconfig/network-scripts/` in the old format still work uninterrupted. Modifications in existing profiles continue updating the older files.

- [1.1. About the Machine Config Operator](01_01_about_the_machine_config_operator.md)
- [1.2. Machine config overview](01_02_machine_config_overview.md)
- [1.3. Understanding the Machine Config Operator node drain behavior](01_03_understanding_the_machine_config_operator_node_drain_behavior.md)
- [1.4. Understanding configuration drift detection](01_04_understanding_configuration_drift_detection.md)
- [1.5. Check machine config pool status](01_05_check_machine_config_pool_status.md)
- [1.6. About node status during updates](01_06_about_node_status_during_updates.md)
- [1.7. View and interact with certificates](01_07_view_and_interact_with_certificates.md)
- [1.8. Additional resources](01_08_additional_resources.md)
