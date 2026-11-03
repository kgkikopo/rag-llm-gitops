# Chapter 10. Using DPDK and RDMA

The containerized Data Plane Development Kit (DPDK) application is supported on OpenShift Container Platform. You can use Single Root I/O Virtualization (SR-IOV) network hardware with the Data Plane Development Kit (DPDK) and with remote direct memory access (RDMA). 

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

- [10.1. Example use of a virtual function in a pod](10_01_example_use_of_a_virtual_function_in_a_pod.md)
- [10.2. Use a virtual function in DPDK mode with an Intel NIC](10_02_use_a_virtual_function_in_dpdk_mode_with_an_intel_nic.md)
- [10.3. Use a virtual function in DPDK mode with a Mellanox NIC](10_03_use_a_virtual_function_in_dpdk_mode_with_a_mellanox_nic.md)
- [10.4. Use the TAP CNI to run a rootless DPDK workload with kernel access](10_04_use_the_tap_cni_to_run_a_rootless_dpdk_workload_with_kernel_access.md)
- [10.5. Overview of achieving a specific DPDK line rate](10_05_overview_of_achieving_a_specific_dpdk_line_rate.md)
- [10.6. Use SR-IOV and the Node Tuning Operator to achieve a DPDK line rate](10_06_use_sr_iov_and_the_node_tuning_operator_to_achieve_a_dpdk_line_rate.md)
- [10.7. Use a virtual function in RDMA mode with a Mellanox NIC](10_07_use_a_virtual_function_in_rdma_mode_with_a_mellanox_nic.md)
- [10.8. A test pod template for clusters that use OVS-DPDK on OpenStack](10_08_a_test_pod_template_for_clusters_that_use_ovs_dpdk_on_openstack.md)
- [10.9. Additional resources](10_09_additional_resources.md)
