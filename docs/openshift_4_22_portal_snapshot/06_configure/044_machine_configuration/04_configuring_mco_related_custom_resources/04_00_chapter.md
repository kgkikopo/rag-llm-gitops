# Chapter 4. Configuring MCO-related custom resources

In addition to `MachineConfig` objects, you can use `KubeletConfig` or `ContainerRuntimeConfig` custom resources to change node-level settings that impact how the kubelet and CRI-O container runtime services behave. 

The kubelet configuration is currently serialized as an Ignition configuration, so it can be directly edited. However, there is also a new `kubelet-config-controller` added to the Machine Config Controller (MCC). This lets you use a `KubeletConfig` custom resource (CR) to edit the kubelet parameters.

- [4.1. Create a KubeletConfig CR to edit kubelet parameters](04_01_create_a_kubeletconfig_cr_to_edit_kubelet_parameters.md)
- [4.2. Create a ContainerRuntimeConfig CR to edit CRI-O parameters](04_02_create_a_containerruntimeconfig_cr_to_edit_cri_o_parameters.md)
- [4.3. Configuring the container runtime](04_03_configuring_the_container_runtime.md)
- [4.4. Setting the default maximum container root partition size for Overlay with CRI-O](04_04_setting_the_default_maximum_container_root_partition_size_for_overlay_with_cri_o.md)
- [4.5. Creating a drop-in file for the default CRI-O capabilities](04_05_creating_a_drop_in_file_for_the_default_cri_o_capabilities.md)
- [4.6. Additional resources](04_06_additional_resources.md)
