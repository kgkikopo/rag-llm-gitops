# 4.6. Telco RAN DU reference design components

The following sections describe the various OpenShift Container Platform components and configurations that you use to configure and deploy clusters to run RAN DU workloads. 

**Figure 4.2. Telco RAN DU reference design components**

![Diagram showing telco RAN DU RDS components](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/ac1ae4989cb764e66d14af4819724ce8/telco-ran-du-reference-design-components.png) ![Diagram showing telco RAN DU RDS components](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/ac1ae4989cb764e66d14af4819724ce8/telco-ran-du-reference-design-components.png)

Note

Ensure that additional components you include that are not specified in the telco RAN DU profile do not affect the CPU resources allocated to workload applications. 

Important

Out of tree drivers are not supported. 5G RAN application components are not included in the RAN DU profile and must be engineered against resources (CPU) allocated to applications. 

## 4.6.1. Host firmware tuning

Tune host firmware settings for optimal performance during initial cluster deployment. 

New in this release
    

  * No reference design updates in this release 



Description
    

Tune host firmware settings for optimal performance during initial cluster deployment. For more information, see "Recommended single-node OpenShift cluster configuration for vDU application workloads". Apply tuning settings in the host firmware during initial deployment. For more information, see "Managing host firmware settings with GitOps ZTP". The managed cluster host firmware settings are available on the hub cluster as individual `BareMetalHost` custom resources (CRs) that are created when you deploy the managed cluster with the `ClusterInstance` CR and GitOps ZTP. 

Note

Create the `ClusterInstance` CR based on the provided reference `example-sno.yaml` CR. 

Limits and requirements
    

  * You must enable Hyper-Threading in the host firmware settings 



Engineering considerations
    

  * Tune all firmware settings for maximum performance. 
  * All settings are expected to be for maximum performance unless tuned for power savings. 
  * You can tune host firmware for power savings at the expense of performance as required. 
  * Enable secure boot. When secure boot is enabled, only signed kernel modules are loaded by the kernel. Out-of-tree drivers are not supported. 



**Additional resources**

  * [Recommended single-node OpenShift cluster configuration for vDU application workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-reference-cluster-configuration-for-vdu)
  * [Managing host firmware settings with GitOps ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-configuring-host-firmware-with-gitops-ztp_ztp-deploying-far-edge-sites)
  * [Configuring host firmware for low latency and high performance](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-du-configuring-host-firmware-requirements_sno-configure-for-vdu)
  * [Provisioning real-time and low latency workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-provisioning-low-latency-workloads "Chapter 19. Provisioning real-time and low latency workloads")



## 4.6.2. Kubelet settings

Configure kubelet settings and sysctls for the telco RAN DU use model, including `systemReserved` and unsafe sysctl parameters. 

New in this release
    

  * No reference design updates in this release 



Some CNF workloads make use of sysctls which are not in the list of system-wide safe sysctls. Generally, network sysctls are namespaced and you can enable them using the `kubeletconfig.experimental` annotation in the `PerformanceProfile` Custom Resource (CR). 

Additionally, the `systemReserved` memory can be configured through the same `kubeletconfig.experimental` annotation to reserve memory for system daemons and kernel processes. 

An example setting of these parameters as a string of JSON is shown here: 

**Example snippet showing allowedUnsafeSysctls and systemReserved**

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: {{ .metadata.name }}
  annotations:
    # allowedUnsafeSysctls: some pods want the kernel stack to ignore IPv6 router Advertisement.
    # systemReserved: when used, it should be tailored for each environment.
    kubeletconfig.experimental: |
      {
       "allowedUnsafeSysctls":["net.ipv6.conf.all.accept_ra"],
       "systemReserved":{"memory":"11Gi"}
      }
# ...
```


Note

Although these sysctls are namespaced, they may allow a pod to consume memory or other resources beyond any limits specified in the pod description. You must ensure that these sysctls do not exhaust platform resources. 

For more information, see "Using sysctls in containers". 

**Additional resources**

  * [Using sysctls in containers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-containers-sysctls-about)



## 4.6.3. CPU partitioning and performance tuning

The RAN DU use model includes cluster performance tuning using `PerformanceProfile` CRs for low-latency performance, and a `TunedPerformancePatch` CR that adds additional RAN-specific tuning. 

New in this release
    

  * No reference design updates in this release 



Description
     The RAN DU use model includes cluster performance tuning using `PerformanceProfile` CRs for low-latency performance, and a `TunedPerformancePatch` CR that adds additional RAN-specific tuning. A reference `PerformanceProfile` is provided for both x86_64 and aarch64 CPU architectures. The single `TunedPerformancePatch` object provided automatically detects the CPU architecture and performs the required additional tuning. The RAN DU use case requires the cluster to be tuned for low-latency performance. The Node Tuning Operator reconciles the `PerformanceProfile` and `TunedPerformancePatch` CRs. 

For more information about node tuning with the `PerformanceProfile` CR, see "Tuning nodes for low latency with the performance profile". 

Limits and requirements
    

You must configure the following settings in the telco RAN DU profile `PerformanceProfile` CR: 

  * Set a reserved `cpuset` of 4 or more, equating to 4 hyper-threads (2 cores) on x86_64, or 4 cores on aarch64 for any of the following CPUs: 

    * Intel 3rd Generation Xeon (IceLake) 2.20 GHz, or newer, CPUs with host firmware tuned for maximum performance 
    * AMD EPYC Zen 4 CPUs (Genoa, Bergamo) 
    * ARM CPUs (Neoverse) 

Note

It is recommended to evaluate features, such as per-pod power management, to determine any potential impact on performance. 

  * x86_64: 

    * Set the reserved `cpuset` to include both hyper-thread siblings for each included core. Unreserved cores are available as allocatable CPU for scheduling workloads. 
    * Ensure that hyper-thread siblings are not split across reserved and isolated cores. 
    * Ensure that reserved and isolated CPUs include all the threads for all cores in the CPU. 
    * Include Core 0 for each NUMA node in the reserved CPU set. 
    * Set the hugepage size to 1G. 

  * aarch64: 

    * Use the first 4 cores for the reserved CPU set (or more). 
    * Set the hugepage size to 512M. 

  * Only pin OpenShift Container Platform pods that are by default configured as part of the management workload partition to reserved cores. 
  * When recommended by the hardware vendor, set the maximum CPU frequency for reserved and isolated CPUs using the `hardwareTuning` section. 



Engineering considerations
    

  * RealTime (RT) kernel 

    * Under x86_64, to reach the full performance metrics, you must use the RT kernel, which is the default in the `x86_64/PerformanceProfile.yaml` configuration. 

      * If required, you can select the non-RT kernel with corresponding impact to performance. 

    * Under aarch64, only the 64k-pagesize non-RT kernel is recommended for RAN DU use cases, which is the default in the `aarch64/PerformanceProfile.yaml` configuration. 

  * The number of hugepages you configure depends on application workload requirements. Variation in this parameter is expected and allowed. 
  * Variation is expected in the configuration of reserved and isolated CPU sets based on selected hardware and additional components in use on the system. The variation must still meet the specified limits. 
  * Hardware without IRQ affinity support affects isolated CPUs. To ensure that pods with guaranteed whole CPU QoS have full use of allocated CPUs, all hardware in the server must support IRQ affinity. 
  * To enable workload partitioning, set `cpuPartitioningMode` to `AllNodes` during deployment, and then use the `PerformanceProfile` CR to allocate enough CPUs to support the operating system, interrupts, and OpenShift Container Platform pods. 
  * Tailor `systemReserved` memory for each cluster based on its size and application workload. The minimum recommended value is 11Gi. 
  * Under x86_64, the `PerformanceProfile` may be customized with the following optional arguments in the `additionalKernelargs` list: 

    * The `vfio_pci` arguments support devices such as the FEC accelerator. You can omit them if they are not required for your workload. 
    * To enable the `acpi_idle` CPUIdle driver, for example, for Intel FlexRAN, add `intel_idle.max_cstate=0`

  * Under aarch64, the `PerformanceProfile` must be adjusted depending on the needs of the platform: 

    * For Grace Hopper systems, the following kernel commandline arguments are required: 

      * `acpi_power_meter.force_cap_on=y`
      * `module_blacklist=nouveau`
      * `pci=realloc=off`
      * `pci=pcie_bus_safe`

    * For other ARM platforms, you may need to enable `iommu.passthrough=1` or `pci=realloc`

  * Extending and augmenting `TunedPerformancePatch.yaml`: 

    * `TunedPerformancePatch.yaml` introduces a default top-level tuned profile named `ran-du-performance` and an architecture-aware RAN tuning profile named `ran-du-performance-architecture-common`, and additional archichitecture-specific child policies that are automatically selected by the common policy. 
    * By default, the `ran-du-performance` profile is set to `priority` level `18`, and it includes both the PerformanceProfile-created profile `openshift-node-performance-openshift-node-performance-profile` and `ran-du-performance-architecture-common`
    * If you have customized the name of the `PerformanceProfile` object, you must create a new tuned object that includes the name change of the tuned profile created by the `PerformanceProfile` CR, as well as the `ran-du-performance-architecture-common` RAN tuning profile. This must have a `priority` less than 18. For example, if the PerformanceProfile object is named `change-this-name`: 

```yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: custom-performance-profile-override
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
    - name: custom-performance-profile-x
      data: |
        [main]
        summary=Override of the default ran-du performance tuning to adjust for our renamed PerformanceProfile
        include=openshift-node-performance-change-this-name,ran-du-performance-architecture-common
  recommend:
    - machineConfigLabels:
        machineconfiguration.openshift.io/role: "master"
      priority: 15
      profile: custom-performance-profile-x
```


    * To further override, the optional `TunedPowerCustom.yaml` config file exemplifies how to extend the provided `TunedPerformancePatch.yaml` without needing to overlay or edit it directly. Creating an additional tuned profile which includes the top-level tuned profile named `ran-du-performance` and has a lower `priority` number in the `recommend` section allows adding additional settings easily. 
    * For additional information on the Node Tuning Operator, see "Using the Node Tuning Operator". 




**Additional resources**

  * [Finding the effective IRQ affinity setting for a node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile#about_irq_affinity_setting_cnf-tuning-low-latency-nodes-with-perf-profile "17.11.1. Finding the effective IRQ affinity setting for a node")
  * [Tuning nodes for low latency with the performance profile](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile "Chapter 17. Tuning nodes for low latency with the performance profile")
  * [Using the Node Tuning Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/using-node-tuning-operator "Chapter 10. Using the Node Tuning Operator")



## 4.6.4. PTP Operator

Configure Precision Time Protocol (PTP) in cluster nodes to ensure precise timing and reliability in the RAN environment. 

New in this release
    

  * Support for PTP boundary clock without holdover on GNR-D hardware. 



Description
     Configure PTP in cluster nodes. PTP ensures precise timing and reliability in the RAN environment, compared to other clock synchronization protocols, like NTP. 
Support includes
    

  * Grandmaster clock (T-GM): use GPS to sync the local clock and provide time synchronization to other devices 
  * Boundary clock (T-BC): receive time from another PTP source and redistribute it to other devices 
  * Ordinary clock (T-TSC): synchronize the local clock from another PTP time provider 



Configuration variations allow for multiple NIC configurations for greater time distribution and high availability (HA), and optional fast event notification over HTTP. 

Limits and requirements
    

  * Supports the PTP G.8275.1 profile for the following telco use-cases: 

    * T-GM use-case: 

      * Limited to a maximum of 3 Westport channel NICs 

        * Requires GNSS input to one NIC card, with SMA connections to synchronize additional NICs 

      * HA support N/A 
      * GNR-D is not supported for T-GM. 

    * T-BC use-case: 

      * Limited to a maximum of 2 NICs 
      * System clock HA support is optional in 2-NIC configuration. 
      * GNR-D is not supported for T-BC. 

    * T-TSC use-case: 

      * Limited to single NIC only 
      * System clock HA support is optional in active/standby 2-port configuration. 
      * GNR-D is not supported for T-TSC. 

    * T-BC without holdover use-case: 

      * GNR-D hardware with 0, 1, or 2 additional Carter Flats, e830 NICs 
      * Time receiver port must be one of the onboard NAC ports. 
      * Time transmitters may be configured to any combination of NAC and Carter Flats ports, up to a total of 23. 
      * Holdover is not enabled, so any failure of the Time receiver will enter `FREERUN` state immediately. 

  * Log reduction must be enabled with `true` or `enhanced`. 



Engineering considerations
    

  * Example RAN DU RDS configurations are provided for: 

    * T-GM, T-BC, T-TSC, and BC-without-holdover 
    * Variations with and without HA 
    * Variations with and without fast event notification 

  * PTP fast event notifications use `ConfigMap` CRs to persist subscriber details. 
  * Hierarchical event subscription as described in the O-RAN specification is not supported for PTP events. 
  * Cluster nodes must have proper NTP configuration to ensure correct time prior to PTP operator taking ownership of node timing. 



## 4.6.5. SR-IOV Operator

The SR-IOV Operator provisions and configures the SR-IOV CNI and device plugins. 

New in this release
    

  * No reference design updates in this release 



Description
     The SR-IOV Operator provisions and configures the SR-IOV CNI and device plugins. Both `netdevice` (kernel VFs) and `vfio` (DPDK) devices are supported and applicable to the RAN DU use models. 
Limits and requirements
    

  * Use devices that are supported for OpenShift Container Platform. For more information, see "Supported devices". 
  * SR-IOV and IOMMU enablement in host firmware settings: The SR-IOV Network Operator automatically enables IOMMU on the kernel command line. 
  * SR-IOV VFs do not receive link state updates from the PF. If link down detection is required you must configure this at the protocol level. 



Engineering considerations
    

  * SR-IOV interfaces with the `vfio` driver type are typically used to enable additional secondary networks for applications that require high throughput or low latency. 
  * Customer variation on the configuration and number of `SriovNetwork` and `SriovNetworkNodePolicy` custom resources (CRs) is expected. 
  * IOMMU kernel command line settings are applied with a `MachineConfig` CR at install time. This ensures that the `SriovOperator` CR does not cause a reboot of the node when adding them. 
  * SR-IOV support for draining nodes in parallel is not applicable in a single-node OpenShift cluster. 
  * You must include the `SriovOperatorConfig` CR in your deployment; the CR is not created automatically. This CR is included in the reference configuration policies which are applied during initial deployment. 
  * In scenarios where you pin or restrict workloads to specific nodes, the SR-IOV parallel node drain feature will not result in the rescheduling of pods. In these scenarios, the SR-IOV Operator disables the parallel node drain functionality. 
  * You must pre-configure NICs which do not support firmware updates under secure boot or kernel lockdown with sufficient virtual functions (VFs) to support the number of VFs needed by the application workload. For Mellanox NICs, you must disable the Mellanox vendor plugin in the SR-IOV Network Operator. For more information, see "Configuring the SR-IOV Network Operator on Mellanox cards when Secure Boot is enabled". 
  * To change the MTU value of a virtual function after the pod has started, do not configure the MTU field in the `SriovNetworkNodePolicy` CR. Instead, configure the Network Manager or use a custom `systemd` script to set the MTU of the physical function to an appropriate value. For example: 

```shell-session
# ip link set dev <physical_function> mtu 9000
```


**Additional resources**

  * [Red Hat certified hardware (Red Hat Ecosystem Catalog)](https://catalog.redhat.com/en/hardware)
  * [Configuring QinQ support for SR-IOV enabled workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/#configuring-qinq-support)



## 4.6.6. Logging

Use logging to collect logs from the far edge node for remote analysis. 

New in this release
    

  * No reference design updates in this release 



Description
     Use logging to collect logs from the far edge node for remote analysis. The recommended log collector is Vector. 
Engineering considerations
    

  * Handling logs beyond the infrastructure and audit logs, for example, from the application workload requires additional CPU and network bandwidth based on additional logging rate. 
  * As of OpenShift Container Platform 4.14, Vector is the reference log collector. Use of fluentd in the RAN use models is deprecated. 



**Additional resources**

  * [About OpenShift logging](https://docs.redhat.com/en/documentation/red_hat_openshift_logging/6.2/html/about_openshift_logging/index)



## 4.6.7. SRIOV-FEC Operator

SRIOV-FEC Operator is an optional 3rd party Certified Operator supporting FEC accelerator hardware. 

New in this release
    

  * No reference design updates in this release 



Description
     SRIOV-FEC Operator is an optional 3rd party Certified Operator supporting FEC accelerator hardware. 
Limits and requirements
    

  * Starting with FEC Operator v2.7.0: 

    * Secure boot is supported 
    * `vfio` drivers for PFs require the usage of a `vfio-token` that is injected into the pods. Applications in the pod can pass the VF token to DPDK by using EAL parameter `--vfio-vf-token`. 




Engineering considerations
    

  * The SRIOV-FEC Operator uses CPU cores from the isolated CPU set. 
  * You can validate FEC readiness as part of the pre-checks for application deployment, for example, by extending the validation policy. 



**Additional resources**

  * [SRIOV-FEC Operator for Intel® vRAN Dedicated Accelerator manager container](https://catalog.redhat.com/software/containers/intel/sriov-fec-operator/6017de1669aea3122e6fa15f)



## 4.6.8. Lifecycle Agent

The Lifecycle Agent provides local lifecycle management services for image-based upgrade of single-node OpenShift clusters. 

New in this release
    

  * No reference design updates in this release 



Description
     The Lifecycle Agent provides local lifecycle management services for image-based upgrade of single-node OpenShift clusters. Image-based upgrade is the recommended upgrade method for single-node OpenShift clusters. 
Limits and requirements
    

  * The Lifecycle Agent is not applicable in multi-node clusters or single-node OpenShift clusters with an additional worker. 
  * The Lifecycle Agent requires a persistent volume that you create when installing the cluster. 



For more information about partition requirements, see "Configuring a shared container directory between ostree stateroots when using GitOps ZTP". 

**Additional resources**

  * [Understanding the image-based upgrade for single-node OpenShift clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#cnf-understanding-image-based-upgrade)
  * [Configuring a shared container directory between ostree stateroots when using GitOps ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-image-based-upgrade-shared-container-partition_shared-container-partition)



## 4.6.9. Local Storage Operator

You can create persistent volumes that can be used as `PVC` resources by applications with the Local Storage Operator. 

New in this release
    

  * No reference design updates in this release 



Description
     You can create persistent volumes that can be used as `PVC` resources by applications with the Local Storage Operator. The number and type of `PV` resources that you create depends on your requirements. 
Engineering considerations
    

  * Create backing storage for `PV` CRs before creating the `PV`. This can be a partition, a local volume, LVM volume, or full disk. 
  * Refer to the device listing in `LocalVolume` CRs by the hardware path used to access each device to ensure correct allocation of disks and partitions, for example, `/dev/disk/by-path/<id>`. Logical names (for example, `/dev/sda`) are not guaranteed to be consistent across node reboots. 



## 4.6.10. Logical Volume Manager Storage

Logical Volume Manager (LVM) Storage provides dynamic provisioning of block and file storage by creating logical volumes from local devices that can be consumed as persistent volume claim (PVC) resources by applications. 

New in this release
    

  * No reference design updates in this release 



Description
     Logical Volume Manager (LVM) Storage is an optional component. It provides dynamic provisioning of both block and file storage by creating logical volumes from local devices that can be consumed as persistent volume claim (PVC) resources by applications. Volume expansion and snapshots are also possible. An example configuration is provided in the RDS with the `StorageLVMCluster.yaml` file. 
Limits and requirements
    

  * In single-node OpenShift clusters, persistent storage must be provided by either LVM Storage or local storage, not both. 
  * Volume snapshots are excluded from the reference configuration. 



Engineering considerations
    

  * LVM Storage can be used as the local storage implementation for the RAN DU use case. When LVM Storage is used as the storage solution, it replaces the Local Storage Operator, and the CPU required is assigned to the management partition as platform overhead. The reference configuration must include one of these storage solutions but not both. 
  * Ensure that sufficient disks or partitions are available for storage requirements. 



## 4.6.11. Workload partitioning

Workload partitioning pins OpenShift Container Platform and Day 2 Operator pods that are part of the DU profile to the reserved CPU set and removes the reserved CPU from node accounting. 

New in this release
    

  * No reference design updates in this release 



Description
     Workload partitioning pins OpenShift Container Platform and Day 2 Operator pods that are part of the DU profile to the reserved CPU set and removes the reserved CPU from node accounting. This leaves all unreserved CPU cores available for user workloads. This leaves all non-reserved CPU cores available for user workloads. Workload partitioning is enabled through a capability set in installation parameters: `cpuPartitioningMode: AllNodes`. The set of management partition cores are set with the reserved CPU set that you configure in the `PerformanceProfile` CR. 
Limits and requirements
    

  * `Namespace` and `Pod` CRs must be annotated to allow the pod to be applied to the management partition 
  * Pods with CPU limits cannot be allocated to the partition. This is because mutation can change the pod QoS. 
  * For more information about the minimum number of CPUs that can be allocated to the management partition, see "Node Tuning Operator". 



Engineering considerations
    

  * Workload partitioning pins all management pods to reserved cores. A sufficient number of cores must be allocated to the reserved set to account for operating system, management pods, and expected spikes in CPU use that occur when the workload starts, the node reboots, or other system events happen. 



**Additional resources**

  * [Workload partitioning](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/enabling-workload-partitioning "Chapter 23. Workload partitioning")



## 4.6.12. Cluster tuning

Configure cluster tuning settings including cluster capabilities and monitoring for the telco RAN DU reference design. 

New in this release
    

  * OLM profile collection is removed in OpenShift Container Platform 4.22. The `DisableOLMPprof` CR compliance type is now set to `mustnothave` to remove the previously applied configuration from clusters. 



Description
     For a full list of components that you can disable using the cluster capabilities feature, see "Cluster capabilities". 
Limits and requirements
    

  * Cluster capabilities are not available for installer-provisioned installation methods. 



The following table lists the required platform tuning configurations: 

Table 4.4. Cluster capabilities configurationsFeature| Description  
---|---  
Remove optional cluster capabilities  |  Reduce the OpenShift Container Platform footprint by disabling optional cluster Operators on single-node OpenShift clusters only. 

  * Remove all optional Operators except the Node Tuning Operator, Operator Lifecycle Manager, and the Ingress Operator. 

  
Configure cluster monitoring  |  Configure the monitoring stack for reduced footprint by doing the following: 

  * Disable the local `alertmanager` and `telemeter` components. 
  * If you use RHACM observability, the CR must be augmented with appropriate `additionalAlertManagerConfigs` CRs to forward alerts to the hub cluster. 
  * RHACM observability combines its default data values with the monitoring configuration `ConfigMap` CR provided as part of the cluster tuning reference CRs. This merge results in the policy becoming non-compliant. To ensure that the provided configuration is not overwritten or merged with RHACM data values, you can disable the RHACM management of this `ConfigMap` CR . This keeps the policy compliant. For more information, see the Observability section of Telco hub reference design specifications. 
  * Reduce the `Prometheus` retention period to 24h. Note The RHACM hub cluster aggregates managed cluster metrics. 

  
Disable networking diagnostics  |  Disable networking diagnostics for single-node OpenShift because they are not required.   
Configure a single OperatorHub catalog source  |  Configure the cluster to use a single catalog source that contains only the Operators required for a RAN DU deployment. Each catalog source increases the CPU use on the cluster. Using a single `CatalogSource` fits within the platform CPU budget.   
Disable the Console Operator  |  If the cluster was deployed with the console disabled, the `Console` CR (`ConsoleOperatorDisable.yaml`) is not needed. If the cluster was deployed with the console enabled, you must apply the `Console` CR.   
Show more

Engineering considerations
    

  * As of OpenShift Container Platform 4.19, cgroup v1 is no longer supported and has been removed. All workloads must now be compatible with cgroup v2. For more information, see [Red Hat Enterprise Linux 9 changes in the context of Red Hat OpenShift workloads](https://www.redhat.com/en/blog/rhel-9-changes-context-red-hat-openshift-workloads). 



**Additional resources**

  * [Cluster capabilities](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#cluster-capabilities)
  * [Observability](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/telco-hub-ref-design-specs#telco-hub-observability_telco-hub "5.14. Observability")



## 4.6.13. Machine configuration

Configure machine configuration settings for container runtime, kubelet, SCTP, kdump, and other system-level components in the telco RAN DU reference design. 

New in this release
    

  * No reference design updates in this release 



Limits and requirements
    

  * To ensure images are static, except during scheduled maintenance in defined maintenance windows, do not set the pod `imagePullPolicy` field to `Always`. 
  * The configuration CRs in this table are required components unless otherwise noted. 



Table 4.5. Machine configuration optionsFeature| Description  
---|---  
Container Runtime  |  Sets the container runtime to `crun` for all node roles.   
Kubelet config and container mount namespace hiding  |  Reduces the frequency of kubelet housekeeping and eviction monitoring, which reduces CPU usage   
SCTP  |  Optional configuration (enabled by default)   
Kdump  |  Optional configuration (enabled by default) Enables kdump to capture debug information when a kernel panic occurs. The reference CRs that enable kdump have an increased memory reservation based on the set of drivers and kernel modules included in the reference configuration.   
SR-IOV-related kernel arguments  |  Include additional SR-IOV-related arguments in the kernel command line   
Set RCU Normal  |  Systemd service that sets `rcu_normal` after the system finishes startup   
One-shot time sync  |  Replaces `chrony-wait.service` with a one-time NTP system time synchronization job for control plane or worker nodes. This MachineConfig is required for nodes running PTP and should not be included for nodes which use NTP for time synchronization.   
Show more

**Additional resources**

  * [Recommended cluster install manifests](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-sno-install-time-cluster-config)
