# 17.2. Reference performance profiles

Use the following reference performance profiles as the basis to develop your own custom profiles. 

## 17.2.1. Performance profile template for clusters that use OVS-DPDK on OpenStack

To maximize machine performance in a cluster that uses Open vSwitch with the Data Plane Development Kit (OVS-DPDK) on Red Hat OpenStack Platform (RHOSP), you can use a performance profile. 

You can use the following performance profile template to create a profile for your deployment. 

**Performance profile template for clusters that use OVS-DPDK**

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: cnf-performanceprofile
spec:
  additionalKernelArgs:
    - nmi_watchdog=0
    - audit=0
    - mce=off
    - processor.max_cstate=1
    - idle=poll
    - intel_idle.max_cstate=0
    - default_hugepagesz=1GB
    - hugepagesz=1G
    - intel_iommu=on
  cpu:
    isolated: <CPU_ISOLATED>
    reserved: <CPU_RESERVED>
  hugepages:
    defaultHugepagesSize: 1G
    pages:
      - count: <HUGEPAGES_COUNT>
        node: 0
        size: 1G
  nodeSelector:
    node-role.kubernetes.io/worker: ''
  realTimeKernel:
    enabled: false
    globallyDisableIrqLoadBalancing: true
```


Insert values that are appropriate for your configuration for the `CPU_ISOLATED`, `CPU_RESERVED`, and `HUGEPAGES_COUNT` keys. 

## 17.2.2. Telco RAN DU reference design performance profile

You can use a pre-configured design performance profile that configures node-level performance settings for OpenShift Container Platform clusters on commodity hardware to host telco RAN DU workloads. 

**Telco RAN DU reference design performance profile**

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  # if you change this name make sure the 'include' line in TunedPerformancePatch.yaml
  # matches this name: include=openshift-node-performance-${PerformanceProfile.metadata.name}
  # Also in file 'validatorCRs/informDuValidator.yaml':
  # name: 50-performance-${PerformanceProfile.metadata.name}
  name: openshift-node-performance-profile
  annotations:
    ran.openshift.io/reference-configuration: "ran-du.redhat.com"
spec:
  additionalKernelArgs:
    - "rcupdate.rcu_normal_after_boot=0"
    - "efi=runtime"
    - "vfio_pci.enable_sriov=1"
    - "vfio_pci.disable_idle_d3=1"
    - "module_blacklist=irdma"
  cpu:
    isolated: $isolated
    reserved: $reserved
  hugepages:
    defaultHugepagesSize: $defaultHugepagesSize
    pages:
      - size: $size
        count: $count
        node: $node
  machineConfigPoolSelector:
    pools.operator.machineconfiguration.openshift.io/$mcp: ""
  nodeSelector:
    node-role.kubernetes.io/$mcp: ''
  numa:
    topologyPolicy: "restricted"
  # To use the standard (non-realtime) kernel, set enabled to false
  realTimeKernel:
    enabled: true
  workloadHints:
    # WorkloadHints defines the set of upper level flags for different type of workloads.
    # See https://github.com/openshift/cluster-node-tuning-operator/blob/master/docs/performanceprofile/performance_profile.md#workloadhints
    # for detailed descriptions of each item.
    # The configuration below is set for a low latency, performance mode.
    realTime: true
    highPowerConsumption: false
    perPodPowerManagement: false
```


## 17.2.3. Telco core reference design performance profile

You can use a pre-configured design performance profile that configures node-level performance settings for OpenShift Container Platform clusters on commodity hardware to host telco core workloads. 

**Telco core reference design performance profile**

```yaml
# required
# count: 1
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: $name
  annotations:
    # Some pods want the kernel stack to ignore IPv6 router Advertisement.
    kubeletconfig.experimental: |
      {"allowedUnsafeSysctls":["net.ipv6.conf.all.accept_ra"]}
spec:
  cpu:
    # node0 CPUs: 0-17,36-53
    # node1 CPUs: 18-34,54-71
    # siblings: (0,36), (1,37)...
    # we want to reserve the first Core of each NUMA socket
    #
    # no CPU left behind! all-cpus == isolated + reserved
    isolated: $isolated # eg 1-17,19-35,37-53,55-71
    reserved: $reserved # eg 0,18,36,54
  # Guaranteed QoS pods will disable IRQ balancing for cores allocated to the pod.
  # default value of globallyDisableIrqLoadBalancing is false
  globallyDisableIrqLoadBalancing: false
  hugepages:
    defaultHugepagesSize: 1G
    pages:
      # 32GB per numa node
      - count: $count # eg 64
        size: 1G
  #machineConfigPoolSelector: {}
  #  pools.operator.machineconfiguration.openshift.io/worker: ''
  nodeSelector: {}
  #node-role.kubernetes.io/worker: ""
  workloadHints:
    realTime: false
    highPowerConsumption: false
    perPodPowerManagement: true
  realTimeKernel:
    enabled: false
  numa:
    # All guaranteed QoS containers get resources from a single NUMA node
    topologyPolicy: "single-numa-node"
  net:
    userLevelNetworking: false
```
