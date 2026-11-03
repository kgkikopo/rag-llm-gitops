# 7.2. Recommended cluster host requirements for vDU application workloads

Running vDU application workloads requires a bare-metal host with sufficient resources to run OpenShift Container Platform services and production workloads. 

Table 7.1. Minimum resource requirementsProfile| vCPU| Memory| Storage  
---|---|---|---  
Minimum  |  4 vCPU  |  32 GB of RAM  |  120 GB   
Recommended  |  8 vCPU  |  32 GB of RAM  |  120 GB   
Show more

Important

Running single-node OpenShift on 4 vCPUs leaves very little headroom for vDU application workloads. With all cluster capabilities enabled, the platform alone can request over 2.5 vCPUs and consume over 2 vCPUs at idle, leaving minimal capacity for application workloads. 

To run on 4 vCPUs, you must minimize the cluster resource footprint: 

  * Set `baselineCapabilitySet` to `None` in the `install-config.yaml` file and use `additionalEnabledCapabilities` to enable only the capabilities that your workload requires, such as `Storage`, `Console`, and `Ingress`. For more information, see "Cluster capabilities". 
  * Use a performance profile to partition CPU resources between cluster housekeeping duties and application workloads, ensuring that your vDU containers run on isolated CPUs with minimal interruption. For more information, see "Tuning nodes for low latency with the performance profile". 



If your deployment does not require these optimizations, it is recommended to use at least 8 vCPUs.. 

Note

One vCPU equals one physical core. However, if you enable simultaneous multithreading (SMT), or Hyper-Threading, use the following formula to calculate the number of vCPUs that represent one physical core: 

  * (threads per core × cores) × sockets = vCPUs 



Important

The server must have a Baseboard Management Controller (BMC) when booting with virtual media. 

**Additional resources**

  * [Cluster capabilities](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#cluster-capabilities)
  * [Tuning nodes for low latency with the performance profile](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#cnf-tuning-low-latency-nodes-with-perf-profile)
