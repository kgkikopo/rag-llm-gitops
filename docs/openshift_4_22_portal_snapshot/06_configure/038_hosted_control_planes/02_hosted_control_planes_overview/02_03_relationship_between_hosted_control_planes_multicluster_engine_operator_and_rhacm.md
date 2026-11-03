# 2.3. Relationship between hosted control planes, multicluster engine Operator, and RHACM

Configure hosted control planes by using the multicluster engine for Kubernetes Operator. The multicluster engine Operator cluster lifecycle defines the process that creates, imports, manages, and destroys Kubernetes clusters across cloud providers, private clouds, and on-premises data centers. 

Note

The multicluster engine Operator is an integral part of Red Hat Advanced Cluster Management and is enabled by default with RHACM. However, you do not need Red Hat Advanced Cluster Management to use hosted control planes. 

The multicluster engine Operator is the cluster lifecycle Operator that provides cluster management capabilities for OpenShift Container Platform and RHACM hub clusters. The multicluster engine Operator enhances cluster fleet management and supports OpenShift Container Platform cluster lifecycle management across clouds and data centers. 

**Figure 2.1. Cluster life cycle and foundation**

![Cluster life cycle and foundation](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hosted_control_planes-en-US/images/d108794b685b4c4a1fab3f28a72b29fe/acm-mce-intro-diagram.png) ![Cluster life cycle and foundation](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hosted_control_planes-en-US/images/d108794b685b4c4a1fab3f28a72b29fe/acm-mce-intro-diagram.png)

You can use the multicluster engine Operator with OpenShift Container Platform as a standalone cluster manager or as part of a RHACM hub cluster. 

Tip

A management cluster is also known as the hosting cluster. 

You can deploy OpenShift Container Platform clusters by using two different control plane configurations: standalone or hosted control planes. The standalone configuration uses dedicated virtual machines or physical machines to host the control plane. With hosted control planes for OpenShift Container Platform, you create control planes as pods on a management cluster without the need for dedicated virtual or physical machines for each control plane. 

**Figure 2.2. RHACM and the multicluster engine Operator introduction diagram**

![RHACM and the multicluster engine Operator introduction diagram](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hosted_control_planes-en-US/images/07887a81ea24c16fc01e40922a15c7d8/rhacm-flow.png) ![RHACM and the multicluster engine Operator introduction diagram](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Hosted_control_planes-en-US/images/07887a81ea24c16fc01e40922a15c7d8/rhacm-flow.png)

## 2.3.1. Hosted clusters in Red Hat Advanced Cluster Management

You can bring hosted clusters to a Red Hat Advanced Cluster Management hub cluster to manage them with Red Hat Advanced Cluster Management management components. 

For more information, see "Discovering multicluster engine Operator hosted clusters in Red Hat Advanced Cluster Management". 

**Additional resources**

  * [Discovering multicluster engine Operator hosted clusters in Red Hat Advanced Cluster Management (Red Hat Advanced Cluster Management official documentation)](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.11/html/clusters/cluster_mce_overview#discover-hosted-acm)
