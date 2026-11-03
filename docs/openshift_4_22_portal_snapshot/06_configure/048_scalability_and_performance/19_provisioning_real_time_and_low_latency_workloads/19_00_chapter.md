# Chapter 19. Provisioning real-time and low latency workloads

If your organization needs high performance computing and low, predictable latency, especially in the financial and telecommunications industries, you can use the Node Tuning Operator to implement automatic tuning to achieve low latency performance and consistent response time for OpenShift Container Platform applications. 

You use the performance profile configuration to make these changes. 

You can update the kernel to kernel-rt, reserve CPUs for cluster and operating system housekeeping duties, including pod infra containers, isolate CPUs for application containers to run the workloads, and disable unused CPUs to reduce power consumption. 

Note

When writing your applications, follow the general recommendations described in [RHEL for Real Time processes and threads](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_for_real_time/9/html-single/understanding_rhel_for_real_time/index#assembly_rhel-for-real-time-processes-and-threads_understanding-RHEL-for-Real-Time-core-concepts). 

**Additional resources**

  * [Creating a performance profile](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile#cnf-create-performance-profiles_cnf-tuning-low-latency-nodes-with-perf-profile "17.1. Creating a performance profile")

- [19.1. Schedule a low latency workload onto a compute node](19_01_schedule_a_low_latency_workload_onto_a_compute_node.md)
- [19.2. Create a pod with a guaranteed QoS class](19_02_create_a_pod_with_a_guaranteed_qos_class.md)
- [19.3. Disabling CPU load balancing in a Pod](19_03_disabling_cpu_load_balancing_in_a_pod.md)
- [19.4. Disable power saving mode for high priority pods](19_04_disable_power_saving_mode_for_high_priority_pods.md)
- [19.5. CPU quota annotation for pods](19_05_cpu_quota_annotation_for_pods.md)
- [19.6. Configure interrupt processing for individual pods](19_06_configure_interrupt_processing_for_individual_pods.md)
