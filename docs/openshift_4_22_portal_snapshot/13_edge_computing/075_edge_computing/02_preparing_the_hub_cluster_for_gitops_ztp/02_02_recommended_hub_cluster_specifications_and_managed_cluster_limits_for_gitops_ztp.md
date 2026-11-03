# 2.2. Recommended hub cluster specifications and managed cluster limits for GitOps ZTP

With GitOps Zero Touch Provisioning (ZTP), you can manage thousands of clusters in geographically dispersed regions and networks. 

The Red Hat Performance and Scale lab successfully created and managed 3500 virtual single-node OpenShift clusters with a reduced DU profile from a single Red Hat Advanced Cluster Management (RHACM) hub cluster in a lab environment. 

In real-world situations, the scaling limits for the number of clusters that you can manage will vary depending on various factors affecting the hub cluster. For example: 

Hub cluster resources
     Available hub cluster host resources (CPU, memory, storage) are an important factor in determining how many clusters the hub cluster can manage. The more resources allocated to the hub cluster, the more managed clusters it can accommodate. 
Hub cluster storage
     The hub cluster host storage IOPS rating and whether the hub cluster hosts use NVMe storage can affect hub cluster performance and the number of clusters it can manage. 
Network bandwidth and latency
     Slow or high-latency network connections between the hub cluster and managed clusters can impact how the hub cluster manages multiple clusters. 
Managed cluster size and complexity
     The size and complexity of the managed clusters also affects the capacity of the hub cluster. Larger managed clusters with more nodes, namespaces, and resources require additional processing and management resources. Similarly, clusters with complex configurations such as the RAN DU profile or diverse workloads can require more resources from the hub cluster. 
Number of managed policies
     The number of policies managed by the hub cluster scaled over the number of managed clusters bound to those policies is an important factor that determines how many clusters can be managed. 
Monitoring and management workloads
     RHACM continuously monitors and manages the managed clusters. The number and complexity of monitoring and management workloads running on the hub cluster can affect its capacity. Intensive monitoring or frequent reconciliation operations can require additional resources, potentially limiting the number of manageable clusters. 
RHACM version and configuration
     Different versions of RHACM can have varying performance characteristics and resource requirements. Additionally, the configuration settings of RHACM, such as the number of concurrent reconciliations or the frequency of health checks, can affect the managed cluster capacity of the hub cluster. 

Use the following representative configuration and network specifications to develop your own Hub cluster and network specifications. 

Important

The following guidelines are based on internal lab benchmark testing only and do not represent complete bare-metal host specifications. 

Table 2.2. Representative three-node hub cluster machine specificationsRequirement| Description  
---|---  
Server hardware  |  3 x Dell PowerEdge R650 rack servers   
NVMe hard disks  | 

  * 50 GB disk for `/var/lib/etcd`
  * 2.9 TB disk for `/var/lib/containers`

  
SSD hard disks  | 

  * 1 SSD split into 15 200GB thin-provisioned logical volumes provisioned as `PV` CRs 
  * 1 SSD serving as an extra large `PV` resource 

  
Number of applied DU profile policies  |  5   
Show more

Important

The following network specifications are representative of a typical real-world RAN network and were applied to the scale lab environment during testing. 

Table 2.3. Simulated lab environment network specificationsSpecification| Description  
---|---  
Round-trip time (RTT) latency  |  50 ms   
Packet loss  |  0.02% packet loss   
Network bandwidth limit  |  20 Mbps   
Show more

**Additional resources**

  * [Creating and managing single-node OpenShift clusters with RHACM](https://access.redhat.com/documentation/en-us/red_hat_advanced_cluster_management_for_kubernetes/2.7/html/install/installing#single-node)
