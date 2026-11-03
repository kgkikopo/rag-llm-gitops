# 16.2. About Hyper-Threading for low latency and real-time applications

You can use Hyper-Threading, an Intel processor technology, to allow a physical CPU processor core to function as two logical cores, executing two independent threads simultaneously. 

Hyper-Threading allows for better system throughput for certain workload types where parallel processing is beneficial. The default OpenShift Container Platform configuration expects Hyper-Threading to be enabled. 

For telecommunications applications, design your application infrastructure to minimize latency as much as possible. Hyper-Threading can slow performance times and negatively affect throughput for compute-intensive workloads that require low latency. Disabling Hyper-Threading ensures predictable performance and can decrease processing times for these workloads. 

Note

Hyper-Threading implementation and configuration differs depending on the hardware you are running OpenShift Container Platform on. Consult the relevant host hardware tuning information for more details of the Hyper-Threading implementation specific to that hardware. Disabling Hyper-Threading can increase the cost per core of the cluster. 

**Additional resources**

  * [Configuring Hyper-Threading for a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile#cnf-configuring-hyperthreading-for-a-cluster_cnf-tuning-low-latency-nodes-with-perf-profile "17.9. Configure Hyper-Threading for a cluster")
