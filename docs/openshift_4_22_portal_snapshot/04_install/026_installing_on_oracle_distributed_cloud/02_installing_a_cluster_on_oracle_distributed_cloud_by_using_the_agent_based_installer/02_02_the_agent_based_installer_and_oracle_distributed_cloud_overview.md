# 2.2. The Agent-based Installer and Oracle Distributed Cloud overview

You can install an OpenShift Container Platform cluster on Oracle® Distributed Cloud by using the Agent-based Installer. Red Hat and Oracle test, validate, and support running Oracle Distributed Cloud workloads in an OpenShift Container Platform cluster. 

The Agent-based Installer provides the ease of use of the Assisted Installation service, but with the capability to install a cluster in either a connected or disconnected environment. 

The following diagrams show workflows for connected and disconnected environments: 

**Figure 2.1. Workflow for using the Agent-based installer in a connected environment to install a cluster on Oracle Cloud Infrastructure (OCI)**

![Image of a high-level workflow for using the Agent-based installer in a connected environment to install a cluster on OCI](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_Oracle_Distributed_Cloud-en-US/images/aa0c5d62501e4948cd292f93d8acae75/684_OpenShift_Installing_on_OCI_0624-connected.png) ![Image of a high-level workflow for using the Agent-based installer in a connected environment to install a cluster on OCI](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_Oracle_Distributed_Cloud-en-US/images/aa0c5d62501e4948cd292f93d8acae75/684_OpenShift_Installing_on_OCI_0624-connected.png)

**Figure 2.2. Workflow for using the Agent-based installer in a disconnected environment to install a cluster on OCI**

![Image of a high-level workflow for using the Agent-based installer in a disconnected environment to install a cluster on OCI](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_Oracle_Distributed_Cloud-en-US/images/aaae40f3f4a784d98c7015f481533446/684_OpenShift_Installing_on_OCI_0624-disconnected.png) ![Image of a high-level workflow for using the Agent-based installer in a disconnected environment to install a cluster on OCI](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_Oracle_Distributed_Cloud-en-US/images/aaae40f3f4a784d98c7015f481533446/684_OpenShift_Installing_on_OCI_0624-disconnected.png)

Oracle Distributed Cloud provides services that can meet your regulatory compliance, performance, and cost-effectiveness needs. Oracle Distributed Cloud supports 64-bit `x86` instances and 64-bit `ARM` instances. 

Note

Consider selecting a nonvolatile memory express (NVMe) drive or a solid-state drive (SSD) for your boot disk, because these drives offer low latency and high throughput capabilities for your boot disk. 

By running your OpenShift Container Platform cluster on Oracle Distributed Cloud, you can access the following capabilities: 

  * Compute flexible shapes, where you can customize the number of Oracle® CPUs (OCPUs) and memory resources for your VM. With access to this capability, a cluster’s workload can perform operations in a resource-balanced environment. You can find all RHEL-certified OCI shapes by going to the Oracle page on the Red Hat Ecosystem Catalog portal. 
  * Block Volume storage, where you can configure scaling and auto-tuning settings for your storage volume, so that the Block Volume service automatically adjusts the performance level to optimize performance. 



Important

To ensure the best performance conditions for your cluster workloads that operate on Oracle Distributed Cloud and on the OCVS service, ensure volume performance units (VPUs) for your block volume is sized for your workloads. The following list provides some guidance in selecting the VPUs needed for specific performance needs: 

  * Test or proof of concept environment: 100 GB, and 20 to 30 VPUs. 
  * Basic environment: 500 GB, and 60 VPUs. 
  * Heavy production environment: More than 500 GB, and 100 or more VPUs. 



Consider reserving additional VPUs to provide sufficient capacity for updates and scaling activities. For more information about VPUs, see Volume Performance Units (Oracle documentation). 

**Additional resources**

  * [Installation process](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#installation-process_architecture-installation)
  * [Internet access for OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_any_platform/#cluster-entitlements_installing-platform-agnostic)
  * [Understanding the Agent-based Installer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#understanding-agent-install_preparing-to-install-with-agent-based-installer)
  * [Overview of the Compute Service (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm)
  * [Volume Performance Units (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#vpus)
  * [Instance Sizing Recommendations for OpenShift Container Platform Nodes (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/installing-agent-about-instance-configurations.htm)
