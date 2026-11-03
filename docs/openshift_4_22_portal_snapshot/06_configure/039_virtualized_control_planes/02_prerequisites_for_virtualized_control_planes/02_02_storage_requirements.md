# 2.2. Storage requirements

The hosting cluster must have a storage solution that supports VM disk images and meets the latency requirements of `etcd`. 

The hosting cluster must have one of the following storage solutions: 

  * Red Hat OpenShift Data Foundation (ODF) provides VM live migration. When you install ODF on a cluster where OpenShift Virtualization is running, the `ocs-storagecluster-ceph-rbd-virtualization` storage class is created automatically. This storage class is optimized for KubeVirt workloads. 
  * Logical Volume Manager (LVM) Storage, backed by NVMe drives, provides predictable, low-latency disk I/O but does not support VM live migration. 



Consider the following when choosing a storage solution: 

  * ODF replicates data across multiple storage nodes for durability. This replication can cause unpredictable latency spikes during synchronization, which might affect `etcd` performance. Monitor `etcd` disk latency in production and ensure the underlying storage nodes use NVMe disks. 
  * LVM Storage writes directly to local disks without replication, providing consistent low latency. However, data is not replicated across nodes.
