# 3.8. Telco core RDS components

The following sections describe the various OpenShift Container Platform components and configurations that you use to configure and deploy clusters to run telco core workloads. 

## 3.8.1. CPU partitioning and performance tuning

CPU partitioning separates sensitive workloads from general-purpose tasks, interrupts, and driver work queues to improve performance and reduce latency. 

New in this release
    

  * There are no reference design updates in this release. 



Description
     CPU partitioning improves performance and reduces latency by separating sensitive workloads from general-purpose tasks, interrupts, and driver work queues. The CPUs allocated to those auxiliary processes are referred to as **reserved** in the following sections. In a system with Hyper-Threading enabled, a CPU is one hyper-thread. 
Limits and requirements
    

  * The operating system needs a certain amount of CPU to perform all the support tasks, including kernel networking. 

    * A system with just user plane networking applications (DPDK) needs at least one core (2 hyper-threads when enabled) reserved for the operating system and the infrastructure components. 

  * In a system with Hyper-Threading enabled, core sibling threads must always be in the same pool of CPUs. 
  * The set of reserved and isolated cores must include all CPU cores. 
  * Core 0 of each NUMA node must be included in the reserved CPU set. 
  * Low latency workloads require special configuration to avoid being affected by interrupts, kernel scheduler, or other parts of the platform. 



For more information, see "Creating a performance profile". 

Engineering considerations
    

  * As of OpenShift 4.19, `cgroup v1` is no longer supported and has been removed. All workloads must now be compatible with `cgroup v2`. For more information, see [Red Hat Enterprise Linux 9 changes in the context of Red Hat OpenShift workloads](https://www.redhat.com/en/blog/rhel-9-changes-context-red-hat-openshift-workloads). 
  * The minimum reserved capacity (`systemReserved`) required can be found by following the guidance in [Which amount of CPU and memory are recommended to reserve for the system in OCP 4 nodes?](https://access.redhat.com/solutions/5843241). 

    * The specific values must be custom-tuned for each cluster based on its size and application workload. 
    * The minimum recommended `systemReserved` memory is 11Gi for worker nodes and 30Gi for control plane nodes. 

  * For schedulable control planes, the minimum recommended reserved capacity is at least 16 CPUs. 
  * The actual required reserved CPU capacity depends on the cluster configuration and workload attributes. 
  * The reserved CPU value must be rounded up to a full core (2 hyper-threads) alignment. 
  * Changes to CPU partitioning cause the nodes contained in the relevant machine config pool to be drained and rebooted. 
  * The reserved CPUs reduce the pod density, because the reserved CPUs are removed from the allocatable capacity of the OpenShift Container Platform node. 
  * The real-time workload hint should be enabled for real-time capable workloads. 

    * Applying the real-time `workloadHint` setting results in the `nohz_full` kernel command line parameter being applied to improve performance of high performance applications. 

  * Hardware without IRQ affinity support affects isolated CPUs. All server hardware must support IRQ affinity to ensure that pods with guaranteed CPU QoS can fully use allocated CPUs. 
  * OVS dynamically manages its `cpuset` entry to adapt to network traffic needs. You do not need to reserve an additional CPU for handling high network throughput on the primary CNI. 
  * If workloads running on the cluster use kernel level networking, the RX/TX queue count for the participating NICs should be set to 16 or 32 queues if the hardware permits it. Be aware of the default queue count. With no configuration, the default queue count is one RX/TX queue per online CPU; which can result in too many interrupts being allocated. 
  * The irdma kernel module might result in the allocation of too many interrupt vectors on systems with high core counts. To prevent this condition the reference configuration excludes this kernel module from loading through a kernel commandline argument in the `PerformanceProfile` resource. Typically Core workloads do not require this kernel module. 
  * To enable the `acpi_idle` CPUIdle driver, for example for Intel FlexRAN workloads, add `intel_idle.max_cstate=0` to the `additionalKernelArgs` list in the `PerformanceProfile` resource. 
  * The `TunedPerformancePatch.yaml` file in the reference configures the `kernel.panic_on_unrecovered_nmi` sysctl parameter to enable triggering a kernel panic through BMC Non-Maskable Interrupt (NMI) on x86_64 architures. This provides a mechanism to force a kernel panic for system recovery and diagnostic purposes when nodes become unresponsive. 

Note

Some drivers do not deallocate the interrupts even after reducing the queue count. 




## 3.8.2. Workloads on schedulable control planes

You can enable schedulable control planes to run workloads on control plane nodes, utilizing idle CPU capacity on bare-metal machines. 

Enabling workloads on control plane nodes
    

You can enable schedulable control planes to run workloads on control plane nodes, utilizing idle CPU capacity on bare-metal machines for potential cost savings. This feature is only applicable to clusters with bare-metal control plane nodes. 

There are two distinct parts to this functionality: 

  1. Allowing workloads on control plane nodes: This feature can be configured after initial cluster installation, allowing you to enable it when you need to run workloads on those nodes. 
  2. Enabling workload partitioning: This is a critical isolation measure that protects the control plane from interference by regular workloads, ensuring cluster stability and reliability. Workload partitioning must be configured during the initial "day zero" cluster installation and cannot be enabled later. 



If you plan to run workloads on your control plane nodes, you must first enable workload partitioning during the initial setup. You can then enable the schedulable control plane feature at a later time. 

Workload characterization and limitations
    

You must test and verify workloads to ensure that applications do not interfere with core cluster functions. It is recommended that you start with lightweight containers that do not heavily load the CPU or networking. 

Certain workloads are not permitted on control plane nodes due to the risk to cluster stability. This includes any workload that reconfigures kernel arguments or system global `sysctls`, as this can lead to unpredictable outcomes for the cluster. 

To ensure stability, you must adhere to the following: 

  * Make sure all non-trivial workloads have memory limits defined. This protects the control plane in case of a memory leak. 
  * Avoid excessively loading reserved CPUs, for example, by heavy use of exec probes. 
  * Avoid heavy kernel-based networking usage, as it can increase reserved CPU load through software networking components like OVS. 



NUMA Resources Operator support
     As part of this enablement, the NUMA Resources Operator is supported on control plane nodes. The functional behavior of the NUMA Resources Operator remains the same, but its use on control plane nodes is explicitly permitted. 

**Additional resources**

  * [Creating a performance profile](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile#cnf-create-performance-profiles_cnf-tuning-low-latency-nodes-with-perf-profile "17.1. Creating a performance profile")
  * [Configuring host firmware for low latency and high performance](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-du-configuring-host-firmware-requirements_sno-configure-for-vdu)



## 3.8.3. Service Mesh

Telco core cloud-native functions (CNFs) typically require a Service Mesh implementation. 

Description
     Telco core cloud-native functions (CNFs) typically require a Service Mesh implementation. Specific Service Mesh features and performance requirements are dependent on the application. The selection of Service Mesh implementation and configuration is outside the scope of this documentation. The implementation must account for the impact of Service Mesh on cluster resource usage and performance, including additional latency introduced in pod networking. 

**Additional resources**

  * [About OpenShift Service Mesh](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/service_mesh/#ossm-about)



## 3.8.4. Networking

The following diagram describes the telco core reference design networking configuration. 

**Figure 3.2. Telco core reference design networking configuration**

![Overview of the telco core reference design networking configuration](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/2fd8e40cc6e45fbe288dcbae353e9d23/openshift-telco-core-rds-networking.png) ![Overview of the telco core reference design networking configuration](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/2fd8e40cc6e45fbe288dcbae353e9d23/openshift-telco-core-rds-networking.png)

Note

The diagram shows the recommended network topology, where bonding uses ports from the same dual-port NIC. Bonding ports across different NICs is not recommended. 

New in this release
    

  * Per-interface IP forwarding 
  * Support for alt-names on network interfaces 
  * Host firewall rules for multi-node clusters 
  * MetalLB `ConfigurationStatus` CRD 
  * Extended BGP/L2 advertisements with service selectors 
  * Support for Intel E830 Jasper Beach in telco core 



Note

If you have custom `FRRConfiguration` CRs in the `metallb-system` namespace, you must move them under the `openshift-network-operator` namespace. 

Description
    

  * The cluster is configured for dual-stack IP (IPv4 and IPv6). 
  * The validated physical network configuration consists of two dual-port NICs. One NIC is shared among the primary CNI (OVN-Kubernetes) and IPVLAN and MACVLAN traffic, while the second one is dedicated to SR-IOV VF-based pod traffic. 
  * A Linux bonding interface (`bond0`) is created in active-active IEEE 802.3ad LACP mode with the two NIC ports attached. The top-of-rack networking equipment must support and be configured for multi-chassis link aggregation (mLAG) technology. 
  * VLAN interfaces are created on top of `bond0`, including for the primary CNI. 
  * Bond and VLAN interfaces are created at cluster install time during the network configuration stage of the installation. Except for the `vlan0` VLAN used by the primary CNI, all other VLANs can be created during Day 2 activities with the Kubernetes NMstate Operator. 
  * MACVLAN and IPVLAN interfaces are created with their corresponding CNIs. They do not share the same base interface. For more information, see "Cluster Network Operator". 
  * SR-IOV VFs are managed by the SR-IOV Network Operator. 
  * To ensure consistent source IP addresses for pods behind a LoadBalancer Service, configure an `EgressIP` CR and specify the `podSelector` parameter. EgressIP is further discussed in the "Cluster Network Operator" section. 
  * You can implement service traffic separation by doing the following: 

    1. Configure VLAN interfaces and specific kernel IP routes on the nodes using `NodeNetworkConfigurationPolicy` CRs. 
    2. Create a MetalLB `BGPPeer` CR for each VLAN to establish peering with the remote BGP router. 
    3. Define a MetalLB `BGPAdvertisement` CR to specify which IP address pools should be advertised to a selected list of `BGPPeer` resources. The following diagram illustrates how specific service IP addresses are advertised externally through specific VLAN interfaces. Services routes are defined in `BGPAdvertisement` CRs and configured with values for `IPAddressPool1` and `BGPPeer1` fields. 

  * Host-level per-interface IP forwarding can be enabled or disabled by using `net.ipv4.conf.<interface>.forwarding` through the install network configuration (Day 1) or the Kubernetes NMState Operator (Day 2). 



**Figure 3.3. Telco core reference design MetalLB service separation**

![Telco core reference design MetalLB service separation](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/421ac907f335f30fbbe88a4cfe0d8cfc/openshift-telco-core-rds-metallb-service-separation.png) ![Telco core reference design MetalLB service separation](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/421ac907f335f30fbbe88a4cfe0d8cfc/openshift-telco-core-rds-metallb-service-separation.png)

**Additional resources**

  * [Understanding networking](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_overview/#understanding-networking)



### 3.8.4.1. Cluster Network Operator

The Cluster Network Operator (CNO) deploys and manages the cluster network components including the default OVN-Kubernetes network plugin during cluster installation. 

New in this release
    

  * There are no reference design updates in this release. 



Description
    

The Cluster Network Operator (CNO) deploys and manages the cluster network components including the default OVN-Kubernetes network plugin during cluster installation. The CNO allows configuration of primary interface MTU settings, OVN gateway modes to use node routing tables for pod egress, and additional secondary networks such as MACVLAN. 

In support of network traffic separation, multiple network interfaces are configured through the CNO. Traffic steering to these interfaces is configured through static routes applied by using the NMState Operator. To ensure that pod traffic is properly routed, OVN-K is configured with the `routingViaHost` option enabled. This setting uses the kernel routing table and the applied static routes rather than OVN for pod egress traffic. 

The Whereabouts CNI plugin is used to provide dynamic IPv4 and IPv6 addressing for additional pod network interfaces without the use of a DHCP server. 

Limits and requirements
    

  * OVN-Kubernetes is required for IPv6 support. 
  * Large MTU cluster support requires connected network equipment to be set to the same or larger value. MTU size up to 8900 is supported. 
  * MACVLAN and IPVLAN cannot co-locate on the same main interface due to their reliance on the same underlying kernel mechanism, specifically the `rx_handler`. This handler allows a third-party module to process incoming packets before the host processes them, and only one such handler can be registered per network interface. Since both MACVLAN and IPVLAN need to register their own `rx_handler` to function, they conflict and cannot coexist on the same interface. Review the source code for more details: 

    * [linux/v6.10.2/source/drivers/net/ipvlan/ipvlan_main.c#L82](https://elixir.bootlin.com/linux/v6.10.2/source/drivers/net/ipvlan/ipvlan_main.c#L82)
    * [linux/v6.10.2/source/drivers/net/macvlan.c#L1260](https://elixir.bootlin.com/linux/v6.10.2/source/drivers/net/macvlan.c#L1260)

  * Alternative NIC configurations include splitting the shared NIC into multiple NICs or using a single dual-port NIC, though they have not been tested and validated. 
  * Clusters with single-stack IP configuration are not validated. 
  * EgressIP 

    * EgressIP failover time depends on the `reachabilityTotalTimeoutSeconds` parameter in the `Network` CR. This parameter determines the frequency of probes used to detect when the selected egress node is unreachable. The recommended value of this parameter is `1` second. 
    * When EgressIP is configured with multiple egress nodes, the failover time is expected to be on the order of seconds or longer. 
    * On nodes with additional network interfaces EgressIP traffic will egress through the interface on which the EgressIP address has been assigned. For more information, see "Configuring an egress IP address". 

  * Pod-level SR-IOV bonding mode must be set to `active-backup` and a value in `miimon` must be set (`100` is recommended). 



Engineering considerations
    

  * Pod egress traffic is managed by kernel routing table using the `routingViaHost` option. Appropriate static routes must be configured in the host. 



**Additional resources**

  * [Cluster Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#nw-cluster-network-operator_cluster-network-operator)
  * [Configuring an egress IP address](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#configuring-egress-ips-ovn)



### 3.8.4.2. Load balancer

MetalLB is a load-balancer implementation for bare metal Kubernetes clusters that uses standard routing protocols. 

New in this release
    

  * There are no reference design updates in this release. 



Important

If you have custom `FRRConfiguration` CRs in the `metallb-system` namespace, you must move them under the `openshift-network-operator` namespace. 

Description
     MetalLB is a load-balancer implementation for bare metal Kubernetes clusters that uses standard routing protocols. It enables a Kubernetes service to get an external IP address which is also added to the host network for the cluster. The MetalLB Operator deploys and manages the lifecycle of a MetalLB instance in a cluster. Some use cases might require features not available in MetalLB, such as stateful load balancing. Where necessary, you can use an external third party load balancer. Selection and configuration of an external load balancer is outside the scope of this specification. When an external third-party load balancer is used, the integration effort must include enough analysis to ensure all performance and resource utilization requirements are met. 
Limits and requirements
    

  * Stateful load balancing is not supported by MetalLB. An alternate load balancer implementation must be used if this is a requirement for workload CNFs. 
  * You must ensure that the external IP address is routable from clients to the host network for the cluster. 



Engineering considerations
    

  * MetalLB is used in BGP mode only for telco core use models. 
  * For telco core use models, MetalLB is supported only with the OVN-Kubernetes network provider used in local gateway mode. See `routingViaHost` in "Cluster Network Operator". 
  * BGP configuration in MetalLB is expected to vary depending on the requirements of the network and peers. 

    * You can configure address pools with variations in addresses, aggregation length, auto assignment, and so on. 
    * MetalLB uses BGP for announcing routes only. Only the `transmitInterval` and `minimumTtl` parameters are relevant in this mode. Other parameters in the BFD profile should remain close to the defaults as shorter values can lead to false negatives and affect performance. 




**Additional resources**

  * [When to use MetalLB](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#nw-metallb-when-metallb_about-metallb-and-metallb-operator)



### 3.8.4.3. SR-IOV

SR-IOV enables physical functions (PFs) to be divided into multiple virtual functions (VFs) for higher throughput performance while keeping pods isolated. 

New in this release
    

  * There are no reference design updates in this release. 



Description
     SR-IOV enables physical functions (PFs) to be divided into multiple virtual functions (VFs). VFs can then be assigned to multiple pods to achieve higher throughput performance while keeping the pods isolated. The SR-IOV Network Operator provisions and manages SR-IOV CNI, network device plugin, and other components of the SR-IOV stack. 
Limits and requirements
    

  * Only certain network interfaces are supported. See "Supported devices" for more information. 
  * Enabling SR-IOV and IOMMU: the SR-IOV Network Operator automatically enables IOMMU on the kernel command line. 
  * SR-IOV VFs do not receive link state updates from the PF. If a link down detection is required, it must be done at the protocol level. 
  * `MultiNetworkPolicy` CRs can be applied to `netdevice` networks only. This is because the implementation uses iptables, which cannot manage vfio interfaces. 



Engineering considerations
    

  * SR-IOV interfaces in `vfio` mode are typically used to enable additional secondary networks for applications that require high throughput or low latency. 
  * The `SriovOperatorConfig` CR must be explicitly created. This CR is included in the reference configuration policies, which causes it to be created during initial deployment. 
  * NICs that do not support firmware updates with UEFI secure boot or kernel lockdown must be preconfigured with sufficient virtual functions (VFs) enabled to support the number of VFs required by the application workload. For Mellanox NICs, you must disable the Mellanox vendor plugin in the SR-IOV Network Operator. For more information see, "Configuring an SR-IOV network device". 
  * To change the MTU value of a VF after the pod has started, do not configure the `SriovNetworkNodePolicy` MTU field. Instead, use the Kubernetes NMState Operator to set the MTU of the related PF. 



**Additional resources**

  * [About Single Root I/O Virtualization (SR-IOV) hardware networks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/#about-sriov)
  * [Red Hat certified hardware (Red Hat Ecosystem Catalog)](https://catalog.redhat.com/en/hardware)
  * [Configuring the SR-IOV Network Operator on Mellanox cards when Secure Boot is enabled](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/#nw-sriov-nic-mlx-secure-boot_configuring-sriov-device)



### 3.8.4.4. NMState Operator

The Kubernetes NMState Operator provides a Kubernetes API for performing state-driven network configuration across cluster nodes. 

New in this release
    

  * There are no reference design updates in this release. 



Description
     The Kubernetes NMState Operator provides a Kubernetes API for performing state-driven network configuration across cluster nodes. It enables network interface configurations, static IPs and DNS, VLANs, trunks, bonding, static routes, MTU, and enabling promiscuous mode on the secondary interfaces. The cluster nodes periodically report on the state of each node’s network interfaces to the API server. 
Limits and requirements
     Not applicable 
Engineering considerations
    

  * Initial networking configuration is applied using `NMStateConfig` content in the installation CRs. The NMState Operator is used only when required for network updates. 
  * When SR-IOV virtual functions are used for host networking, the NMState Operator (via `nodeNetworkConfigurationPolicy` CRs) is used to configure VF interfaces, such as VLANs and MTU. 



**Additional resources**

  * [Kubernetes NMState Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#k8s-nmstate-about-the-k8s-nmstate-operator)



## 3.8.5. Logging

The Cluster Logging Operator enables collection and shipping of logs off the node for remote archival and analysis. 

New in this release
    

  * There are no reference design updates in this release. 



Description
     The Cluster Logging Operator enables collection and shipping of logs off the node for remote archival and analysis. The reference configuration uses Kafka to ship audit and infrastructure logs to a remote archive. 
Limits and requirements
     Not applicable 
Engineering considerations
    

  * The impact of cluster CPU use is based on the number or size of logs generated and the amount of log filtering configured. 
  * The reference configuration does not include shipping of application logs. The inclusion of application logs in the configuration requires you to evaluate the application logging rate and have sufficient additional CPU resources allocated to the reserved set. 



**Additional resources**

  * [Logging 6.0](https://docs.openshift.com/container-platform/4.17/observability/logging/logging-6.0/log6x-about.html)



## 3.8.6. Power Management

Use the performance profile to configure clusters with high power mode, low power mode, or mixed mode depending on workload latency sensitivity. 

New in this release
    

  * There are no reference design updates in this release. 



Description
     Use the Performance profile to configure clusters with high power mode, low power mode, or mixed mode. The choice of power mode depends on the characteristics of the workloads running on the cluster, particularly how sensitive they are to latency. Configure the maximum latency for a low-latency pod by using the per-pod power management C-states feature. 
Limits and requirements
    

  * Power configuration relies on appropriate BIOS configuration, for example, enabling C-states and P-states. Configuration varies between hardware vendors. 



Engineering considerations
    

  * Latency: To ensure that latency-sensitive workloads meet requirements, you require a high-power or a per-pod power management configuration. Per-pod power management is only available for Guaranteed QoS pods with dedicated pinned CPUs. 



**Additional resources**

  * [performance.openshift.io/v2 API reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/node_apis/#spec-workloadhints)
  * [Configuring power saving for nodes that run colocated high and low priority workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile#cnf-configuring-power-saving-for-nodes_cnf-tuning-low-latency-nodes-with-perf-profile "17.5. Configure power saving for nodes that run colocated high and low priority workloads")



## 3.8.7. Storage

Cloud native storage services can be provided by OpenShift Data Foundation or other third-party solutions for telco core clusters. 

New in this release
    

  * There are no reference design updates in this release. 



Description
    

Cloud native storage services can be provided by OpenShift Data Foundation or other third-party solutions. 

OpenShift Data Foundation is a Red Hat Ceph Storage based software-defined storage solution for containers. It provides block storage, file system storage, and on-premise object storage, which can be dynamically provisioned for both persistent and non-persistent data requirements. Telco core applications require persistent storage. 

Note

All storage data might not be encrypted in flight. To reduce risk, isolate the storage network from other cluster networks. The storage network must not be reachable, or routable, from other cluster networks. Only nodes directly attached to the storage network should be allowed to gain access to it. 

**Additional resources**

  * [Red Hat OpenShift Data Foundation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#red-hat-openshift-data-foundation)



### 3.8.7.1. OpenShift Data Foundation

OpenShift Data Foundation is a software-defined storage service for containers that provides block storage, file system storage, and on-premise object storage. 

New in this release
    

  * There are no reference design updates in this release. 



Description
    

OpenShift Data Foundation is a software-defined storage service for containers. OpenShift Data Foundation can be deployed in one of two modes: 

  * Internal mode, where OpenShift Data Foundation software components are deployed as software containers directly on the OpenShift cluster nodes, together with other containerized applications. 
  * External mode, where OpenShift Data Foundation is deployed on a dedicated storage cluster, which is usually a separate Red Hat Ceph Storage cluster running on Red Hat Enterprise Linux. These storage services are running externally to the application workload cluster. 



For telco core clusters, storage support is provided by OpenShift Data Foundation storage services running in external mode, for several reasons: 

  * Separating dependencies between OpenShift Container Platform and Ceph operations allows for independent OpenShift Container Platform and OpenShift Data Foundation updates. 
  * Separation of operations functions for the Storage and OpenShift Container Platform infrastructure layers, is a typical customer requirement for telco core use cases. 
  * External Red Hat Ceph Storage clusters can be re-used by multiple OpenShift Container Platform clusters deployed in the same region. 



OpenShift Data Foundation supports separation of storage traffic using secondary CNI networks. 

Limits and requirements
    

  * In an IPv4/IPv6 dual-stack networking environment, OpenShift Data Foundation uses IPv4 addressing. For more information, see [IPv6 support](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/latest/html/planning_your_deployment/network-requirements_rhodf#ipv6-support_rhodf). 



Engineering considerations
    

  * OpenShift Data Foundation network traffic should be isolated from other traffic on a dedicated network, for example, by using VLAN isolation. 
  * Workload requirements must be scoped before attaching multiple OpenShift Container Platform clusters to an external OpenShift Data Foundation cluster to ensure enough throughput, bandwidth, and performance KPIs. 



### 3.8.7.2. Additional storage solutions

You can use other storage solutions to provide persistent storage for telco core clusters. The configuration and integration of these solutions is outside the scope of the reference design specifications (RDS). 

Integration of the storage solution into the telco core cluster must include proper sizing and performance analysis to ensure the storage meets overall performance and resource usage requirements.
