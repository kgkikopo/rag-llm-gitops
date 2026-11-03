# 6.4. etcd key-value store

etcd is a consistent, distributed key-value store that holds small amounts of data that can fit entirely in memory. 

Although etcd is a core component of many projects, etcd is the primary data store for Kubernetes, which is the standard system for container orchestration. 

Benefits of using etcd
    

etcd provides the following benefits: 

  * Maintain consistent uptime for your cloud-native applications, and keep them working even if individual servers fail 
  * Store and replicate all cluster states for Kubernetes 
  * Distribute configuration data to provide redundancy and resiliency for the configuration of nodes 



How etcd works
    

To ensure a reliable approach to cluster configuration and management, etcd uses the etcd Operator. The Operator simplifies the use of etcd on a Kubernetes container platform like OpenShift Container Platform. With the etcd Operator, you can create or delete etcd members, resize clusters, perform backups, and upgrade etcd. 

The etcd Operator observes, analyzes, and acts: 

  1. It observes the cluster state by using the Kubernetes API. 
  2. It analyzes differences between the current state and the state that you want. 
  3. It fixes the differences through the etcd cluster management APIs, the Kubernetes API, or both. 

etcd holds the cluster state, which is constantly updated. etcd continuously persists this state, which leads to a high number of small changes at high frequency. As a result, you must back the etcd cluster member with fast, low-latency I/O. For more information about best practices for etcd, see "Recommended etcd practices". 




**Additional resources**

  * [Recommended etcd practices](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/etcd/#recommended-etcd-practices)
  * [Backing up etcd](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/backup_and_restore/#backing-up-etcd)
