# Chapter 7. Configuring interface-level network sysctl settings and all-multicast mode for SR-IOV networks

As a cluster administrator, you can change interface-level network sysctls and several interface attributes such as promiscuous mode, all-multicast mode, MTU, and MAC address by using the tuning Container Network Interface (CNI) meta plugin for a pod connected to a SR-IOV network device. 

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

- [7.1. Label nodes with an SR-IOV enabled NIC](07_01_label_nodes_with_an_sr_iov_enabled_nic.md)
- [7.2. Set one sysctl flag](07_02_set_one_sysctl_flag.md)
- [7.3. Configure sysctl settings for pods associated with bonded SR-IOV interface flag](07_03_configure_sysctl_settings_for_pods_associated_with_bonded_sr_iov_interface_flag.md)
- [7.4. About all-multicast mode](07_04_about_all_multicast_mode.md)
