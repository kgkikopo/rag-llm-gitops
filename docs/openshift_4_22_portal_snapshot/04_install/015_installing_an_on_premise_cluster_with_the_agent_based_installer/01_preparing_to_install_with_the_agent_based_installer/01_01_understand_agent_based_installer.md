# 1.1. Understand Agent-based Installer

As an OpenShift Container Platform user, you can leverage the advantages of the Assisted Installer hosted service in disconnected environments. 

The Agent-based Installer uses a bootable ISO that contains the Assisted discovery agent and the Assisted Service. Both are required to perform the cluster installation, but the Assisted Service runs on only one of the hosts. 

Note

Currently, ISO boot support on IBM Z® (`s390x`) is available only for Red Hat Enterprise Linux (RHEL) KVM, which provides the flexibility to choose either PXE or ISO-based installation. For installations with z/VM and Logical Partition (LPAR), only PXE boot is supported. 

The `openshift-install agent create image` subcommand generates an ephemeral ISO based on the inputs that you provide. You can choose to provide inputs through the following manifests: 

Preferred manifests: 

  * `install-config.yaml`
  * `agent-config.yaml`



Optional ZTP manifests: 

  * `cluster-manifests/cluster-deployment.yaml`
  * `cluster-manifests/agent-cluster-install.yaml`
  * `cluster-manifests/pull-secret.yaml`
  * `cluster-manifests/infraenv.yaml`
  * `cluster-manifests/cluster-image-set.yaml`
  * `cluster-manifests/nmstateconfig.yaml`
  * `mirror/registries.conf`
  * `mirror/ca-bundle.crt`



## 1.1.1. Agent-based Installer workflow

One of the control plane hosts runs the Assisted Service at the start of the boot process and eventually becomes the bootstrap host. This node is called the **rendezvous host** (or node 0). 

The Assisted Service ensures that all the hosts meet the requirements and triggers an OpenShift Container Platform cluster deployment. All the nodes have the Red Hat Enterprise Linux (RHEL) image written to the disk. The non-bootstrap nodes reboot and initiate a cluster deployment. 

Once the nodes are rebooted, the rendezvous host reboots and joins the cluster. The bootstrapping is then complete and the cluster is deployed. 

**Figure 1.1. Node installation workflow**

![Agent-based installer workflow](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_an_on-premise_cluster_with_the_Agent-based_Installer-en-US/images/29ccc02b7fddfa90caec07c9f7e20421/agent-based-installer-workflow.png) ![Agent-based installer workflow](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_an_on-premise_cluster_with_the_Agent-based_Installer-en-US/images/29ccc02b7fddfa90caec07c9f7e20421/agent-based-installer-workflow.png)

You can install a disconnected OpenShift Container Platform cluster through the `openshift-install agent create image` subcommand for the following topologies: 

  * **A single-node OpenShift Container Platform cluster** : A node that is both a control plane and compute. 
  * **A three-node OpenShift Container Platform cluster** : A compact cluster that has three control plane nodes that are also compute nodes. 
  * **Highly available OpenShift Container Platform cluster (HA)** : Three control plane nodes with any number of compute nodes. 
  * **Two-node OpenShift Container Platform cluster with Arbiter** : Two control plane nodes with one local arbiter node. For more information, see "About a local arbiter node". 



## 1.1.2. Recommended resources for topologies

The following cluster resources are recommended for each topology: 

Table 1.2. Recommended cluster resourcesTopology| Number of control plane nodes| Number of compute nodes| vCPU| Memory| Storage  
---|---|---|---|---|---  
Single-node cluster  |  1  |  0  |  8 vCPUs  |  16 GB of RAM  |  120 GB   
Two-node OpenShift cluster with Arbiter  |  2 (control plane nodes)  |  0  |  4 vCPUs  |  16 GB of RAM  |  120 GB   
1 (arbiter node)  |  0  |  2 vCPUs  |  8 GB of RAM  |  50 GB   
Two-node OpenShift cluster with fencing (TNF)  |  2  |  0  |  4 vCPUs  |  16 GB of RAM  |  120 GB   
Compact cluster  |  3  |  0 or 1  |  8 vCPUs  |  16 GB of RAM  |  120 GB   
HA cluster  |  3 to 5  |  2 and above  |  8 vCPUs  |  16 GB of RAM  |  120 GB   
Show more

Note

You can use as few as 4 vCPUs for an single-node OpenShift cluster. 

However, running single-node OpenShift on 4 vCPUs leaves very little "headroom" for user applications, and creates a high risk of resource contention and performance degradation. 

To ensure cluster stability at this threshold, you must take steps to minimize the total resource footprint of the cluster, such as limiting the amount of workloads running on the cluster or limiting cluster capabilities. For more information, see "Cluster capabilities". 

Otherwise, it is recommended to provide more compute resources to the cluster. 

## 1.1.3. Supported platforms

In the `install-config.yaml` file, specify the platform on which to perform the installation. The following platforms are supported: 

  * `baremetal`
  * `vsphere`
  * `nutanix`
  * `external`
  * `none`



For a two-node OpenShift Container Platform cluster with fencing (TNF), only the following platforms are supported: 

  * `baremetal`
  * `external`
  * `none`

The `vsphere` and `nutanix` platforms are not supported for two-node clusters with fencing. 




Important

For platform `none`: 

  * The `none` option requires the provision of DNS name resolution and load balancing infrastructure in your cluster. See _Requirements for a cluster using the platform "none" option_ in the "Additional resources" section for more information. 
  * See "Deploying OpenShift 4.x on non-tested platforms using the bare metal install method" before you attempt to install an OpenShift Container Platform cluster in virtualized or cloud environments. 



For platform `vsphere`, or for platform `baremetal` on vSphere: 

  * You must set the `disk.EnableUUID` parameter to `TRUE` on all OpenShift Container Platform nodes. If this parameter is not enabled, the Agent-based Installer validation fails. 



**Additional resources**

  * [Cluster capabilities](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#cluster-capabilities)
  * [Deploying OpenShift 4.x on non-tested platforms using the bare metal install method (Red Hat Knowledgebase article)](https://access.redhat.com/articles/4207611)
  * [Requirements for a cluster using the platform "none" option](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_an_on-premise_cluster_with_the_agent-based_installer/preparing-to-install-with-agent-based-installer#installation-requirements-platform-none_preparing-to-install-with-agent-based-installer "1.6. Requirements for a cluster using the platform "none" option")
  * [Increase the network MTU](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#network-requirements-increase-mtu_ipi-install-prerequisites)
  * [Adding worker nodes to single-node OpenShift clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-sno-worker-nodes)
  * [About a local arbiter node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_an_on-premise_cluster_with_the_agent-based_installer/preparing-to-install-with-agent-based-installer#installing-ocp-agent-local-arbiter-node_preparing-to-install-with-agent-based-installer "1.7. About an arbiter node")
