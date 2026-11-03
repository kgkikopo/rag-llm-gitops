# 1.5. Bare-metal cluster installation requirements for OpenShift Virtualization

Configure your bare-metal cluster correctly during installation to support OpenShift Virtualization, as certain required settings cannot be changed after installation. 

## 1.5.1. High availability requirements for OpenShift Virtualization

When discussing high availability (HA) features in the context of OpenShift Virtualization, this refers only to the replication model of the core cluster components, determined by the `controlPlaneTopology` and `infrastructureTopology` fields in the `Infrastructure` custom resource (CR). Setting these fields to `HighlyAvailable` offers component redundancy, which is distinct from general cluster-wide application HA. Setting these fields to `SingleReplica` disables component redundancy, and therefore disables OpenShift Virtualization HA features. 

If you plan to use OpenShift Virtualization HA features, you must have three control plane nodes at the time of cluster installation. The `controlPlaneTopology` status in the `Infrastructure` CR for the cluster must be `HighlyAvailable`. 

Note

You can install OpenShift Virtualization on a single-node cluster, but single-node OpenShift does not support HA features. 

## 1.5.2. Live migration requirements for OpenShift Virtualization

  * If you plan to use live migration, you must have multiple worker nodes. The `infrastructureTopology` status in the `Infrastructure` CR for the cluster must be `HighlyAvailable`. A minimum of three worker nodes is recommended. 

Note

You can install OpenShift Virtualization on a single-node cluster, but single-node OpenShift does not support live migration. 

  * Live migration requires shared storage. Storage for OpenShift Virtualization must support and use the ReadWriteMany (RWX) access mode. 



## 1.5.3. SR-IOV requirements for OpenShift Virtualization

If you plan to use Single Root I/O Virtualization (SR-IOV), ensure that your network interface controllers (NICs) are supported by OpenShift Container Platform.
