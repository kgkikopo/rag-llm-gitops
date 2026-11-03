# 7.4. Requirements for etcd, networking, and storage

Apply etcd, networking, and storage requirements for multisite clusters so etcd stays healthy and workloads remain reachable across sites. 

Consider the following requirements for clusters that span data centers. 

## 7.4.1. etcd requirements

There is a large list of factors and considerations that go into planning an etcd cluster deployment. When planning an OpenShift Container Platform cluster that spans data centers, you need to plan for situations that will likely stress or push etcd to the edge of its operational limits. 

See "Ensuring reliable etcd performance and scalability" for more details on how to maintain operational capabilities and reduce service-affecting events and instability of the cluster. 

## 7.4.2. Network requirements

The chosen network topology must yield direct IP connectivity between nodes. The lowest effective maximum transmission unit (MTU) across the infrastructure should be the maximum MTU used for the deployment. Using a lower MTU is acceptable. 

For more information, see "Understanding and Validating MTU setting with OpenShift Container Platform 4.x". The latency needs are ultimately defined by the services that use the network. See the sections related to etcd and storage for more details on requirements. 

In addition to the base networking requirements, you need to think about how applications will be accessed. A top-level Global Service Load Balancing (GSLB) method will be needed outside of OpenShift Container Platform to enable external traffic to connect to the OpenShift Container Platform control plane services and ingress controllers. 

## 7.4.3. Storage requirements

When you plan a cluster deployment that spans data centers, consider the selected storage integration to ensure that it also meets multisite requirements, as it pertains to accessibility from all sites, fault tolerance, high availability, and so on. 

An object storage solution should be used for the registry, and this storage solution needs to be in addition to any PV storage integration used for application volumes or workloads. This object storage solution should also have the same special considerations given to accessibility from all sites, fault tolerance, high availability, and so on. 

Because disk I/O is a critical factor in the health of etcd database, it is required that they are deployed on a high speed, low latency media. See etcd guidance on "How etcd peer round trip time affects performance" and "Determining the size of the etcd database and understanding its effects" for more details on the exact requirements to meet. 

**Additional resources**

  * [Ensuring reliable etcd performance and scalability](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/etcd-performance#etcd-leader-election-log-replication_etcd-performance "3.1. Leader election and log replication of etcd")
  * [Understanding and Validating MTU setting with OpenShift Container Platform 4.x (Red Hat Knowledgebase)](https://access.redhat.com/articles/7010220)
  * [How etcd peer round trip time affects performance](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/etcd-performance#etcd-peer-round-trip_etcd-performance "3.14. How etcd peer round-trip time affects performance")
  * [Determining the size of the etcd database and understanding its effects](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/etcd/etcd-performance#etcd-database-size_etcd-performance "3.10. Determine the size of the etcd database and understand its effects")
