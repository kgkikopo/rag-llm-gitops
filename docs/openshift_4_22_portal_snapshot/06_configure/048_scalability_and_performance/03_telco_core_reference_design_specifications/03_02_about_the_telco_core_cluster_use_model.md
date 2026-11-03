# 3.2. About the telco core cluster use model

The telco core cluster use model supports large-scale telco applications on commodity hardware, including control plane functions and centralized data plane functions such as 5G user plane functions (UPF). 

Control plane functions include signaling, aggregation, and session border controller (SBC). These functions require scalability, complex networking support, resilient software-defined storage, and performance requirements that are less stringent than far-edge RAN deployments. 

Networking requirements for telco core functions vary widely across a range of networking features and performance points. IPv6 is a requirement and dual-stack is common. Some functions need maximum throughput and transaction rate and require support for user-plane DPDK networking. Other functions use typical cloud-native patterns and can rely on OVN-Kubernetes, kernel networking, and load balancing. 

Telco core clusters are configured as standard with three control plane and one or more worker nodes configured with the stock (non-RT) kernel. In support of workloads with varying networking and performance requirements, you can segment worker nodes by using `MachineConfigPool` custom resources (CR), for example, for non-user data plane or high-throughput use cases. In support of required telco operational features, core clusters have a standard set of Day 2 OLM-managed Operators installed. 

**Figure 3.1. Telco core RDS cluster service-based architecture and networking topology**

![5G core cluster showing a service-based architecture with overlaid networking topology](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/5c9589733d4683bc9679a09ab907131e/openshift-5g-core-cluster-architecture-networking.png) ![5G core cluster showing a service-based architecture with overlaid networking topology](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/5c9589733d4683bc9679a09ab907131e/openshift-5g-core-cluster-architecture-networking.png)
