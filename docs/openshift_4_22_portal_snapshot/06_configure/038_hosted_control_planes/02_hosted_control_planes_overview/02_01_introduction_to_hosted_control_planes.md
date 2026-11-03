# 2.1. Introduction to hosted control planes

Hosted control planes is available by using a supported version of multicluster engine for Kubernetes Operator on several platforms. 

You can deploy hosted control planes on the following platforms: 

  * Bare metal by using the Agent provider 
  * Non-bare-metal Agent machines, as a Technology Preview feature 
  * OpenShift Virtualization 
  * Amazon Web Services (AWS) 
  * IBM Z 
  * IBM Power 
  * Red Hat OpenStack Platform (RHOSP) 17.1, as a Technology Preview feature 



The hosted control planes feature is enabled by default. 

Note

The multicluster engine Operator is an integral part of Red Hat Advanced Cluster Management (RHACM) and is enabled by default with RHACM. However, you do not need RHACM to use hosted control planes. 

## 2.1.1. Architecture of hosted control planes

OpenShift Container Platform is often deployed in a coupled, or standalone, model, where a cluster consists of a control plane and a data plane. The control plane includes an API endpoint, a storage endpoint, a workload scheduler, and an actuator that ensures state. The data plane includes compute, storage, and networking where workloads and applications run. 

The standalone control plane is hosted by a dedicated group of nodes, which can be physical or virtual, with a minimum number to ensure quorum. The network stack is shared. Administrator access to a cluster offers visibility into the cluster’s control plane, machine management APIs, and other components that contribute to the state of a cluster. 

Although the standalone model works well, some situations require an architecture where the control plane and data plane are decoupled. In those cases, the data plane is on a separate network domain with a dedicated physical hosting environment. The control plane is hosted by using high-level primitives such as deployments and stateful sets that are native to Kubernetes. The control plane is treated as any other workload. 

![Diagram that compares the hosted control plane model against OpenShift with a coupled control plane and workers](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hosted_control_planes-en-US/images/01a511f42d82a6519a600b5c8e91724f/hosted-control-planes-diagram.png) ![Diagram that compares the hosted control plane model against OpenShift with a coupled control plane and workers](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hosted_control_planes-en-US/images/01a511f42d82a6519a600b5c8e91724f/hosted-control-planes-diagram.png)

## 2.1.2. Benefits of hosted control planes

With hosted control planes, you can pave the way for a true hybrid-cloud approach and enjoy several other benefits. 

  * The security boundaries between management and workloads are stronger because the control plane is decoupled and hosted on a dedicated hosting service cluster. As a result, you are less likely to leak credentials for clusters to other users. Because infrastructure secret account management is also decoupled, cluster infrastructure administrators cannot accidentally delete control plane infrastructure. 
  * With hosted control planes, you can run many control planes on fewer nodes. As a result, clusters are more affordable. 
  * Because the control planes consist of pods that are launched on OpenShift Container Platform, control planes start quickly. The same principles apply to control planes and workloads, such as monitoring, logging, and auto-scaling. 
  * From an infrastructure perspective, you can push registries, HAProxy, cluster monitoring, storage nodes, and other infrastructure components to the tenant’s cloud provider account, isolating usage to the tenant. 
  * From an operational perspective, multicluster management is more centralized, which results in fewer external factors that affect the cluster status and consistency. Site reliability engineers have a central place to debug issues and navigate to the cluster data plane, which can lead to shorter Time to Resolution (TTR) and greater productivity. 



**Additional resources**

  * [Cluster lifecycle with multicluster engine for Kubernetes Operator overview (Red Hat Advanced Cluster Management official documentation)](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.16/html/clusters/cluster_mce_overview#cluster_mce_overview)
