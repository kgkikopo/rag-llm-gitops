# 4.2. Hardware, software, and operational requirements

Review the hardware, software, and operational requirements for OpenShift Virtualization, including CPU, OS, storage, cluster sizing, and live migration. 

## 4.2.1. CPU requirements

OpenShift Virtualization requires CPUs supported by Red Hat Enterprise Linux (RHEL) 9 with specific virtualization extensions enabled. 

CPU requirements for OpenShift Virtualization
    

  * Must be supported by Red Hat Enterprise Linux (RHEL) 9. See [Red Hat Ecosystem Catalog](https://catalog.redhat.com) for supported CPUs. 



Note

If your worker nodes have different CPUs, live migration failures might occur because different CPUs have different capabilities. You can mitigate this issue by ensuring that your worker nodes have CPUs with the appropriate capacity and by configuring node affinity rules for your virtual machines. 

For more information, see "Configuring a required node affinity rule" in the Additional resources section. 

  * Supports AMD64, Intel 64-bit (x86-64-v2), IBM Z® (`s390x`), or ARM64-based (`arm64` or `aarch64`) architectures and their respective CPU extensions. 
  * Intel VT-x, AMD-V, or ARM virtualization extensions are enabled, or `s390x` virtualization support is enabled. 
  * NX (no execute) flag is enabled. 
  * If you use `s390x` architecture, the default CPU model is set to `gen15b`. For more information, see "Configuring the default CPU model" in the Additional resources section. 



## 4.2.2. Operating system requirements

OpenShift Virtualization requires Red Hat Enterprise Linux CoreOS (RHCOS) on worker nodes. RHEL worker nodes are not supported. 

For more information, see "About RHCOS" in the Additional resources section. 

## 4.2.3. Storage requirements

OpenShift Virtualization requires OpenShift Container Platform-supported storage with specific configuration for VM workloads and snapshots. 

Storage requirements for OpenShift Virtualization
    

  * Storage must be supported by OpenShift Container Platform. For more information, see "Optimizing storage" in the Additional resources section. 
  * You must create a default OpenShift Virtualization or OpenShift Container Platform storage class. The purpose of this is to address the unique storage needs of VM workloads and offer optimized performance, reliability, and user experience. If both OpenShift Virtualization and OpenShift Container Platform default storage classes exist, the OpenShift Virtualization class takes precedence when creating VM disks. 

Note

To mark a storage class as the default for virtualization workloads, set the annotation `storageclass.kubevirt.io/is-default-virt-class` to `"true"`. 

  * If the storage provisioner supports snapshots, you must associate a `VolumeSnapshotClass` object with the default storage class. 



### 4.2.3.1. Storage I/O latency requirements for Windows virtual machines

Windows guest operating systems require consistently low storage I/O latency to remain stable. If the latency of the underlying storage exceeds the following thresholds, Windows VMs can become unstable or crash. 

Table 4.1. Storage I/O latency thresholds for Windows VMsStorage I/O latency| Impact  
---|---  
Less than 15 ms  |  Healthy. Storage performance is within the expected range for stable VM operation.   
15 ms to less than 100 ms  |  Unhealthy. Exceeding this threshold can eventually lead to workload instability and crashes.   
100 ms to less than 1,000 ms  |  Windows crashes are highly likely to occur.   
1,000 ms or more  |  Windows crashes are almost certain to occur.   
Show more

Note

If storage I/O latency exceeds 100 ms multiple times a day, prioritize identifying the root cause of the latency. Troubleshooting the affected workload is a secondary concern until you resolve the underlying latency issue. 

### 4.2.3.2. Volume and access modes for VM disks

If you use the storage API with known storage providers, the volume and access modes are selected automatically. However, if you use a storage class that does not have a storage profile, you must configure the volume and access mode. 

For a list of known storage providers for OpenShift Virtualization, see the [ Red Hat Ecosystem Catalog](https://catalog.redhat.com/search?searchType=software&badges_and_features=OpenShift+Virtualization&subcategories=Storage). 

For best results, use the `ReadWriteMany` (RWX) access mode and the `Block` volume mode. This is important for the following reasons: 

  * `ReadWriteMany` (RWX) access mode is required for live migration. 
  * The `Block` volume mode performs significantly better than the `Filesystem` volume mode. This is because the `Filesystem` volume mode uses more storage layers, including a file system layer and a disk image file. These layers are not necessary for VM disk storage. 

For example, if you use Red Hat OpenShift Data Foundation, Ceph RBD volumes are preferable to CephFS volumes. 




Important

You cannot live migrate virtual machines with the following configurations: 

  * Storage volume with `ReadWriteOnce` (RWO) access mode 
  * Passthrough features such as GPUs 



Set the `evictionStrategy` field to `None` for these virtual machines. The `None` strategy powers down VMs during node reboots. 

## 4.2.4. Physical resource overhead requirements

OpenShift Virtualization is an add-on to OpenShift Container Platform and imposes additional overhead that you must account for when planning a cluster. 

Each cluster machine must accommodate the following overhead requirements in addition to the OpenShift Container Platform requirements. Oversubscribing the physical resources in a cluster can affect performance. 

Important

The numbers noted in this documentation are based on Red Hat’s test methodology and setup. These numbers can vary based on your own individual setup and environments. 

### 4.2.4.1. Memory overhead

Calculate the memory overhead values for OpenShift Virtualization by using the equations below. 

Cluster memory overhead
    

```plaintext
Memory overhead per infrastructure node ≈ 150 MiB
```


```plaintext
Memory overhead per worker node ≈ 360 MiB
```


Additionally, OpenShift Virtualization environment resources require a total of 2179 MiB of RAM that is spread across all infrastructure nodes. 

Virtual machine memory overhead
    

```plaintext
Memory overhead per virtual machine ≈ (0.002 × requested memory) \
              + 218 MiB \
              + 8 MiB × (number of vCPUs) \
              + 16 MiB × (number of graphics devices) \
              + (additional memory overhead)
```


  * `218 MiB` is required for the processes that run in the `virt-launcher` pod. 
  * `8 MiB × (number of vCPUs)` refers to the number of virtual CPUs requested by the virtual machine. 
  * `16 MiB × (number of graphics devices)` refers to the number of virtual graphics cards requested by the virtual machine. 
  * Additional memory overhead: 

    * If your environment includes a Single Root I/O Virtualization (SR-IOV) network device or a Graphics Processing Unit (GPU), allocate 1 GiB additional memory overhead for each device. 
    * If Secure Encrypted Virtualization (SEV) is enabled, add 256 MiB. 
    * If Trusted Platform Module (TPM) is enabled, add 53 MiB. 




### 4.2.4.2. CPU overhead

Calculate the cluster processor overhead requirements for OpenShift Virtualization by using the equation below. The CPU overhead per virtual machine depends on your individual setup. 

Cluster CPU overhead
    

```plaintext
CPU overhead for infrastructure nodes ≈ 4 cores
```


OpenShift Virtualization increases the overall utilization of cluster level services such as logging, routing, and monitoring. To account for this workload, ensure that nodes that host infrastructure components have capacity allocated for 4 additional cores (4000 millicores) distributed across those nodes. 

```plaintext
CPU overhead for worker nodes ≈ 2 cores + CPU overhead per virtual machine
```


Each worker node that hosts virtual machines must have capacity for 2 additional cores (2000 millicores) for OpenShift Virtualization management workloads in addition to the CPUs required for virtual machine workloads. 

Virtual machine CPU overhead
     If dedicated CPUs are requested, there is a 1:1 impact on the cluster CPU overhead requirement. Otherwise, there are no specific rules about how many CPUs a virtual machine requires. 

### 4.2.4.3. Storage overhead

Use the guidelines below to estimate storage overhead requirements for your OpenShift Virtualization environment. 

Cluster storage overhead
    

```plaintext
Aggregated storage overhead per node ≈ 10 GiB
```


10 GiB is the estimated on-disk storage impact for each node in the cluster when you install OpenShift Virtualization. 

Virtual machine storage overhead
     Storage overhead per virtual machine depends on specific requests for resource allocation within the virtual machine. The request could be for ephemeral storage on the node or storage resources hosted elsewhere in the cluster. OpenShift Virtualization does not currently allocate any additional ephemeral storage for the running container itself. 
Example
     As a cluster administrator, if you plan to host 10 virtual machines in the cluster, each with 1 GiB of RAM and 2 vCPUs, the memory impact across the cluster is 11.68 GiB. The estimated on-disk storage impact for each node in the cluster is 10 GiB and the CPU impact for worker nodes that host virtual machine workloads is a minimum of 2 cores. 

## 4.2.5. Single-node OpenShift feature support

You can install OpenShift Virtualization on single-node OpenShift. The topology does not support high availability, pod disruption, live migration, or eviction strategies. 

However, you should be aware that Single-node OpenShift does not support the following features: 

  * High availability 
  * Pod disruption 
  * Live migration 
  * Virtual machines or templates that have an eviction strategy configured 



## 4.2.6. Object maximums

Consider tested object maximums for both OpenShift Container Platform and OpenShift Virtualization when planning your cluster. 

OpenShift Container Platform
     See "OpenShift Container Platform object maximums" in the Additional resources section. 
OpenShift Virtualization
     See "OpenShift Virtualization supported limits" in the Additional resources section. 

## 4.2.7. Live migration requirements

Live migration requires shared storage, sufficient resources, and compatible CPUs across nodes. 

Live migration requirements
    

  * Shared storage with `ReadWriteMany` (RWX) access mode. 
  * Sufficient RAM and network bandwidth. 

Note

You must ensure that there is enough memory request capacity in the cluster to support node drains that result in live migrations. You can determine the approximate required spare memory by using the following calculation: 

```plaintext
Product of (Maximum number of nodes that can drain in parallel) and (Highest total VM memory request allocations across nodes)
```


The default number of migrations that can run in parallel in the cluster is 5. For more information, see "Configuring live migration" in the Additional resources section. 

  * If the virtual machine uses a host model CPU, the nodes must support the virtual machine’s host model CPU. 



Note

A dedicated Multus network for live migration is highly recommended. For more information, see "Using a dedicated network for live migration" in the Additional resources section. A dedicated network minimizes the effects of network saturation on tenant workloads during migration. 

## 4.2.8. Cluster high availability options

Configure high availability (HA) for your cluster using installer-provisioned infrastructure (IPI), Node Health Check Operator, or manual monitoring. 

Methods of configuring HA
    

  * Automatic high availability for installer-provisioned infrastructure is available by deploying machine health checks. For more information, see "Installer-provisioned infrastructure installation overview" and "About machine health checks" in the Additional resources section. 



Note

In OpenShift Container Platform clusters installed using installer-provisioned infrastructure and with a properly configured `MachineHealthCheck` resource, if a node fails the machine health check and becomes unavailable to the cluster, it is recycled. What happens next with VMs that ran on the failed node depends on a series of conditions. See the "Run strategies" documentation for more detailed information about the potential outcomes and how run strategies affect those outcomes. 

Currently, installer-provisioned infrastructure is not supported on IBM Z®. 

  * Automatic high availability for both IPI and non-IPI is available by using the **Node Health Check Operator** on the OpenShift Container Platform cluster to deploy the `NodeHealthCheck` controller. The controller identifies unhealthy nodes and uses a remediation provider, such as the Self Node Remediation Operator or Fence Agents Remediation Operator, to remediate the unhealthy nodes. For more information on remediation, fencing, and maintaining nodes, see the [Workload Availability for Red Hat OpenShift](https://access.redhat.com/documentation/en-us/workload_availability_for_red_hat_openshift) documentation. 

Note

Fence Agents Remediation uses supported fencing agents to reset failed nodes faster than the Self Node Remediation Operator. This improves overall virtual machine high availability. For more information, see the [OpenShift Virtualization - Fencing and VM High Availability Guide](https://access.redhat.com/articles/7057929) knowledgebase article. 

  * High availability for any platform is available by using either a monitoring system or a qualified human to monitor node availability. When a node is lost, shut it down and run `oc delete node <lost_node>`. 

Note

Without an external monitoring system or a qualified human monitoring node health, virtual machines lose high availability. 




## 4.2.9. Additional resources

  * [Configuring a required node affinity rule](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-scheduler-node-affinity-configuring-required_nodes-scheduler-node-affinity)
  * [About RHCOS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#rhcos-about_architecture-rhcos)
  * [Optimizing storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#_optimizing-storage)
  * [Red Hat Ecosystem Catalog](https://catalog.redhat.com)
  * [Configuring live migration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/live-migration#virt-configuring-live-migration "11.2. Configuring live migration")
  * [Using a dedicated network for live migration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-dedicated-network-live-migration "9.16. Configuring a dedicated network for live migration")
  * [Run strategies](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/nodes#virt-runstrategies-vms_virt-eviction-strategies "12.2.3. Run strategies")
  * [OpenShift Container Platform object maximums](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#planning-your-environment-according-to-object-maximums)
  * [OpenShift Virtualization supported limits](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/about#virt-supported-limits "1.2. Supported limits")
  * [Installer-provisioned infrastructure installation overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#ipi-install-overview)
  * [About machine health checks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#machine-health-checks-about_deploying-machine-health-checks)
