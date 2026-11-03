# 11.5. Requirements for a cluster with user-provisioned infrastructure

For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines. Reviewing these requirements before deployment helps you provision machines that meet the minimum resource needs of the cluster. 

## 11.5.1. Required machines for cluster installation

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails. 

The smallest OpenShift Container Platform clusters require the following hosts: 

Important

For a cluster that has user-provisioned infrastructure, you must deploy all of the required machines. 

Table 11.5. Minimum required hostsHosts| Description  
---|---  
One temporary bootstrap machine  |  The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster.   
Three control plane machines  |  The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane.   
At least two compute machines, which are also known as worker machines.  |  The workloads requested by OpenShift Container Platform users run on the compute machines.   
Show more

Important

To maintain high availability of your cluster, use separate physical hosts for these cluster machines. 

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. However, the compute machines can use Red Hat Enterprise Linux CoreOS (RHCOS), Red Hat Enterprise Linux (RHEL) 8.6 and later. 

RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.8 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits). 

## 11.5.2. Minimum resource requirements for cluster installation

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements. 

Table 11.6. Minimum resource requirementsMachine| Operating system| vCPU| Virtual RAM| Storage| Input/Output Per Second (IOPS)  
---|---|---|---|---|---  
Bootstrap  |  RHCOS  |  4  |  16 GB  |  100 GB  |  300   
Control plane  |  RHCOS  |  4  |  16 GB  |  100 GB  |  300   
Compute  |  RHCOS  |  2  |  8 GB  |  100 GB  |  300   
Show more

  * One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs. 
  * OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance. 
  * As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines. 



Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA): 

  * x86-64 architecture requires x86-64-v2 ISA 
  * ARM64 architecture requires ARMv8.0-A ISA 
  * ppc64le architecture requires IBM® Power9 ISA 
  * s390x architecture requires IBM® z14 ISA 



For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation. 

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform. 

**Additional resources**

  * [Optimizing storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#optimizing-storage)



## 11.5.3. Tested instance types for Google Cloud

OpenShift Container Platform supports specific Google Cloud instance types that have been validated for cluster deployment. 

Note

Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) (Google documentation). 

Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see [machine series support for Hyperdisk](https://cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in _Storage_. 

See the following machine series: 

  * `A2`
  * `A3`
  * `C2`
  * `C2D`
  * `C3`
  * `C3D`
  * `C4`
  * `E2`
  * `M1`
  * `N1`
  * `N2`
  * `N2D`
  * `N4`
  * `Tau T2D`



## 11.5.4. Using custom machine types

If the predefined Google Cloud machine types do not meet your workload requirements, you can configure a custom machine type in the `install-config.yaml` file during OpenShift Container Platform installation. 

Consider the following when using a custom machine type: 

  * Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation". 
  * The name of the custom machine type must adhere to the following syntax: 

`custom-<number_of_cpus>-<amount_of_memory_in_mb>`

For example, `custom-6-20480`.
