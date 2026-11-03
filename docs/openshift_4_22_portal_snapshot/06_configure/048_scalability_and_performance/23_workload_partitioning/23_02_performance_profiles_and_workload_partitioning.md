# 23.2. Performance profiles and workload partitioning

To enable workload partitioning, apply a performance profile. 

An appropriately configured performance profile specifies the `isolated` and `reserved` CPUs. Create a performance profile by using the Performance Profile Creator (PPC) tool. 

**Sample performance profile configuration**

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


Table 23.1. PerformanceProfile CR options for single-node OpenShift clustersPerformanceProfile CR field| Description  
---|---  
`metadata.name` |  Ensure that `name` matches the following fields set in related GitOps ZTP custom resources (CRs): 

  * `include=openshift-node-performance-${PerformanceProfile.metadata.name}` in `TunedPerformancePatch.yaml`
  * `name: 50-performance-${PerformanceProfile.metadata.name}` in `validatorCRs/informDuValidator.yaml`

  
`spec.additionalKernelArgs` |  `"efi=runtime"` Configures UEFI secure boot for the cluster host.   
`spec.cpu.isolated` |  Set the isolated CPUs. Ensure all of the Hyper-Threading pairs match.  Important The reserved and isolated CPU pools must not overlap and together must span all available cores. CPU cores that are not accounted for cause an undefined behaviour in the system.   
`spec.cpu.reserved` |  Set the reserved CPUs. When workload partitioning is enabled, system processes, kernel threads, and system container threads are restricted to these CPUs. All CPUs that are not isolated should be reserved.   
`spec.hugepages.pages` | 

  * Set the number of huge pages (`count`) 
  * Set the huge pages size (`size`). 
  * Set `node` to the NUMA node where the `hugepages` are allocated (`node`) 

  
`spec.realTimeKernel` |  Set `enabled` to `true` to use the realtime kernel.   
`spec.workloadHints` |  Use `workloadHints` to define the set of top level flags for different type of workloads. The example configuration configures the cluster for low latency and high performance.   
Show more

**Additional resources**

  * [About the Performance Profile Creator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile#cnf-about-the-profile-creator-tool_cnf-tuning-low-latency-nodes-with-perf-profile "17.1.1. About the Performance Profile Creator")
