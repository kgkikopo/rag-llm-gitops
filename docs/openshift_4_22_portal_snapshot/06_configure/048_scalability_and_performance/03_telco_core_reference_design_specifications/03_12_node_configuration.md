# 3.12. Node Configuration

Node configuration for telco core clusters includes additional kernel modules, container mount namespace settings, and kdump configuration. 

New in this release
    

  * There are no reference design updates in this release. 



Limits and requirements
    

  * Analyze additional kernel modules to determine impact on CPU load, system performance, and ability to meet KPIs. 

Table 3.1. Additional kernel modulesFeature| Description  
---|---  
Additional kernel modules  |  Install the following kernel modules by using `MachineConfig` CRs to provide extended kernel functionality to CNFs. 
    * sctp 
    * ip_gre 
    * nf_tables 
    * nf_conntrack 
    * nft_ct 
    * nft_limit 
    * nft_log 
    * nft_nat 
    * nft_chain_nat 
    * nf_reject_ipv4 
    * nf_reject_ipv6 
    * nfnetlink_log   
Container mount namespace hiding  |  Reduce the frequency of kubelet housekeeping and eviction monitoring to reduce CPU usage. Creates a container mount namespace, visible to kubelet/CRI-O, to reduce system mount scanning overhead.   
Kdump enable  |  Optional configuration (enabled by default)   
Show more




**Additional resources**

  * [Automatic kernel crash dumps with kdump](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-sno-du-enabling-kdump_sno-configure-for-vdu)
  * [Optimizing CPU usage with mount namespace encapsulation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/scalability-and-performance-optimization#optimizing-cpu-usage "13.4. Optimizing CPU usage with mount namespace encapsulation")



## 3.12.1. Host firmware and boot loader configuration

Configure host firmware and boot loader settings to support telco core cluster requirements. 

New in this release
    

  * There are no reference design updates in this release. 



Engineering considerations
    

  * Enabling secure boot is the recommended configuration. 

Note

When secure boot is enabled, only signed kernel modules are loaded by the kernel. Out-of-tree drivers are not supported. 




## 3.12.2. Kubelet Settings

Some CNF workloads make use of sysctls which are not in the list of system-wide safe `sysctls`. Generally network sysctls are namespaced and can be enabled by using the `kubeletconfig.experimental` annotation in the PerformanceProfile as a string of JSON in the form `allowedUnsafeSysctls`. 

Additionally, the `systemReserved` memory can be configured through the same `kubeletconfig.experimental` annotation to reserve memory for system daemons and kernel processes. 

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
```


Note

Although these are namespaced they may allow a pod to consume memory or other resources beyond any limits specified in the pod description. You must ensure that these `sysctls` do not exhaust platform resources.
