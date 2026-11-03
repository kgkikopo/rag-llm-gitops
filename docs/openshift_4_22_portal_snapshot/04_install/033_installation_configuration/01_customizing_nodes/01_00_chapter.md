# Chapter 1. Customizing nodes

You can customize nodes both cluster-wide and per-machine configuration through Ignition, which allows arbitrary partitioning and file content changes to the operating system. 

If a configuration file is documented in Red Hat Enterprise Linux (RHEL), you can modify the file through Ignition. 

There are two ways to deploy machine config changes: 

  * Creating machine configs that are included in manifest files to start up a cluster during `openshift-install`. 
  * Creating machine configs that are passed to running OpenShift Container Platform nodes through the Machine Config Operator. 



Additionally, modifying the reference config, such as the Ignition config that is passed to `coreos-installer` when installing bare-metal nodes allows per-machine configuration. The Machine Config Operator cannot yet see these changes. 

The following sections describe features that you might want to configure on your nodes.

- [1.1. Create machine configs with Butane](01_01_create_machine_configs_with_butane.md)
- [1.2. Additional resources](01_02_additional_resources.md)
- [1.3. Adding day-1 kernel arguments](01_03_adding_day_1_kernel_arguments.md)
- [1.4. The addition of kernel modules to nodes](01_04_the_addition_of_kernel_modules_to_nodes.md)
- [1.5. Building and testing the kernel module container](01_05_building_and_testing_the_kernel_module_container.md)
- [1.6. Provisioning a kernel module to OpenShift Container Platform](01_06_provisioning_a_kernel_module_to_openshift_container_platform.md)
- [1.7. Boot disk encryption and mirroring during installation](01_07_boot_disk_encryption_and_mirroring_during_installation.md)
- [1.8. About disk mirroring](01_08_about_disk_mirroring.md)
- [1.9. Additional resources](01_09_additional_resources.md)
- [1.10. Configuring a RAID-enabled data volume](01_10_configuring_a_raid_enabled_data_volume.md)
- [1.11. Configuring an Intel® Virtual RAID on CPU (VROC) data volume](01_11_configuring_an_intel_virtual_raid_on_cpu_vroc_data_volume.md)
- [1.12. Configure chrony time service](01_12_configure_chrony_time_service.md)
