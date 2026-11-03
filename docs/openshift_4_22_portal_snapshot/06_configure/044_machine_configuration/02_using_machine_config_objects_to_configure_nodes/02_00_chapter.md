# Chapter 2. Using machine config objects to configure nodes

You can create `MachineConfig` custom resources (CR) that modify files, systemd unit files, and other operating system features running on OpenShift Container Platform nodes. By using `MachineConfig` objects, you can perform tasks such as disabling chronyd, adding kernel arguments, enabling multipathing, and adding RHCOS extensions. 

For more ideas on working with machine configs, see "How to update ssh keys after installation in OpenShift 4?", "Container image signatures", "Enabling SCTP in Openshift Container Platform 4", and "How to provide custom iSCSI initiatornames for nodes". 

OpenShift Container Platform supports Ignition specification version 3.5. For more information, see "Configuration Specification v3.5.0 (Ignition documentation)". You should base all new machine configs you create going forward on Ignition specification version 3.5. If you are upgrading your OpenShift Container Platform cluster, any existing machine configs with a previous Ignition specification will be translated automatically to specification version 3.5. 

There might be situations where the configuration on a node does not fully match what the currently-applied machine config specifies. This state is called _configuration drift_. The Machine Config Daemon (MCD) regularly checks the nodes for configuration drift. If the MCD detects configuration drift, the MCO marks the node `degraded` until an administrator corrects the node configuration. A degraded node is online and operational, but, it cannot be updated. For more information on configuration drift, see "Understanding configuration drift detection". 

Tip

Use the following "Configuring chrony time service" procedure as a model for how to go about adding other configuration files to OpenShift Container Platform nodes.

- [2.1. Configure chrony time service](02_01_configure_chrony_time_service.md)
- [2.2. Disable the chrony time service](02_02_disable_the_chrony_time_service.md)
- [2.3. Add kernel arguments to nodes](02_03_add_kernel_arguments_to_nodes.md)
- [2.4. Enable multipathing with kernel arguments on RHCOS](02_04_enable_multipathing_with_kernel_arguments_on_rhcos.md)
- [2.5. Add a real-time kernel to nodes](02_05_add_a_real_time_kernel_to_nodes.md)
- [2.6. Configure journald settings](02_06_configure_journald_settings.md)
- [2.7. Add extensions to RHCOS](02_07_add_extensions_to_rhcos.md)
- [2.8. Load custom firmware blobs in the machine config manifest](02_08_load_custom_firmware_blobs_in_the_machine_config_manifest.md)
- [2.9. Change the core user password for node access](02_09_change_the_core_user_password_for_node_access.md)
- [2.10. Override storage or partition setup](02_10_override_storage_or_partition_setup.md)
- [2.11. Additional resources](02_11_additional_resources.md)
