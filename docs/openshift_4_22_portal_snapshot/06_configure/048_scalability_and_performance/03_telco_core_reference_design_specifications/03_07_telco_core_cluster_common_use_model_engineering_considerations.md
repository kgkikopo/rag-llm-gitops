# 3.7. Telco core cluster common use model engineering considerations

The following engineering considerations apply to the telco core cluster common use model. 

  * Cluster workloads are detailed in "Application workloads". 
  * Worker nodes should run on either of the following CPUs: 

    * Intel 3rd Generation Xeon (IceLake) CPUs or better when supported by OpenShift Container Platform, or CPUs with the silicon security bug (Spectre and similar) mitigations turned off. Skylake and older CPUs can experience 40% transaction performance drops when Spectre and similar mitigations are enabled. 
    * AMD EPYC Zen 4 CPUs (Genoa, Bergamo) or AMD EPYC Zen 5 CPUs (Turin) when supported by OpenShift Container Platform. 
    * Intel Sierra Forest CPUs when supported by the OpenShift Container Platform. 
    * IRQ balancing is enabled on worker nodes. The `PerformanceProfile` CR sets the `globallyDisableIrqLoadBalancing` parameter to a value of `false`. Guaranteed QoS pods are annotated to ensure isolation as described in "CPU partitioning and performance tuning". 

  * All cluster nodes should have the following features: 

    * Have Hyper-Threading enabled 
    * Have x86_64 CPU architecture 
    * Have the stock (non-realtime) kernel enabled 
    * Are not configured for workload partitioning 

  * The balance between power management and maximum performance varies between machine config pools in the cluster. The following configurations should be consistent for all nodes in a machine config pools group. 

    * Cluster scaling. See "Scalability" for more information. 
    * Clusters should be able to scale to at least 120 nodes. 

  * CPU partitioning is configured using a `PerformanceProfile` CR and is applied to nodes on a per `MachineConfigPool` basis. See "CPU partitioning and performance tuning" for additional considerations. 
  * CPU requirements for OpenShift Container Platform depend on the configured feature set and application workload characteristics. For a cluster configured according to the reference configuration running a simulated workload of 3000 pods as created by the kube-burner node-density test, the following CPU requirements are validated: 

    * The minimum number of reserved CPUs for control plane and worker nodes is 2 CPUs (4 hyper-threads) per NUMA node. 
    * The NICs used for non-DPDK network traffic should be configured to use at most 32 RX/TX queues. 
    * Nodes with large numbers of pods or other resources might require additional reserved CPUs. The remaining CPUs are available for user workloads. 

Note

Variations in OpenShift Container Platform configuration, workload size, and workload characteristics require additional analysis to determine the effect on the number of required CPUs for the OpenShift platform. 




## 3.7.1. Application workloads

Application workloads running on telco core clusters can include a mix of high performance cloud-native network functions (CNFs) and traditional best-effort or burstable pod workloads. 

Guaranteed QoS scheduling is available to pods that require exclusive or dedicated use of CPUs due to performance or security requirements. Typically, pods that run high performance or latency sensitive CNFs by using user plane networking (for example, DPDK) require exclusive use of dedicated whole CPUs achieved through node tuning and guaranteed QoS scheduling. When creating pod configurations that require exclusive CPUs, be aware of the potential implications of hyper-threaded systems. Pods should request multiples of 2 CPUs when the entire core (2 hyper-threads) must be allocated to the pod. 

Pods running network functions that do not require high throughput or low latency networking should be scheduled with best-effort or burstable QoS pods and do not require dedicated or isolated CPU cores. 

Engineering considerations
    

Plan telco core workloads and cluster resources by using the following information: 

  * As of OpenShift Container Platform 4.19, `cgroup v1` is no longer supported and has been removed. All workloads must now be compatible with `cgroup v2`. For more information, see [Red Hat Enterprise Linux 9 changes in the context of Red Hat OpenShift workloads](https://www.redhat.com/en/blog/rhel-9-changes-context-red-hat-openshift-workloads). 
  * CNF applications should conform to the latest version of [Red Hat Best Practices for Kubernetes](https://redhat-best-practices-for-k8s.github.io/guide/). 
  * Use a mix of best-effort and burstable QoS pods as required by your applications. 

    * Use guaranteed QoS pods with proper configuration of reserved or isolated CPUs in the `PerformanceProfile` CR that configures the node. 
    * Guaranteed QoS Pods must include annotations for fully isolating CPUs. 
    * Best effort and burstable pods are not guaranteed exclusive CPU use. Workloads can be preempted by other workloads, operating system daemons, or kernel tasks. 

  * Use exec probes sparingly and only when no other suitable option is available. 

    * Do not use exec probes if a CNF uses CPU pinning. Use other probe implementations, for example, `httpGet` or `tcpSocket`. 
    * When you need to use exec probes, limit the exec probe frequency and quantity. The maximum number of exec probes must be kept below 10, and the frequency must not be set to less than 10 seconds. 
    * You can use startup probes, because they do not use significant resources at steady-state operation. The limitation on exec probes applies primarily to liveness and readiness probes. Exec probes cause much higher CPU usage on management cores compared to other probe types because they require process forking. 

  * Use pre-stop hooks to allow the application workload to perform required actions before pod disruption, such as during an upgrade or node maintenance. The hooks enable a pod to save state to persistent storage, offload traffic from a Service, or signal other Pods. 



## 3.7.2. Signaling workloads

Signaling workloads typically use SCTP, REST, gRPC, or similar TCP or UDP protocols and support hundreds of thousands of transactions per second (TPS) by using a secondary multus CNI configured as MACVLAN or SR-IOV. 

These workloads can run in pods with either guaranteed or burstable QoS.
