# Chapter 1. Configuring system controls and interface attributes using the tuning plugin

To modify kernel parameters and interface attributes at runtime in OpenShift Container Platform, you can use the tuning Container Network Interface (CNI) meta plugin. The plugin operates in a chain with a main CNI plugin and allows you to change sysctls and interface attributes such as promiscuous mode, all-multicast mode, MTU, and MAC address. 

![CNI plugin](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Configuring_network_settings-en-US/images/af56fdca7a66f114406dd89fc4fb9ca9/264_OpenShift_CNI_plugin_chain_0722.png) ![CNI plugin](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Configuring_network_settings-en-US/images/af56fdca7a66f114406dd89fc4fb9ca9/264_OpenShift_CNI_plugin_chain_0722.png)

- [1.1. Configure system controls by using the tuning CNI](01_01_configure_system_controls_by_using_the_tuning_cni.md)
- [1.2. Enable all-multicast mode by using the tuning CNI](01_02_enable_all_multicast_mode_by_using_the_tuning_cni.md)
- [1.3. Additional resources](01_03_additional_resources.md)
