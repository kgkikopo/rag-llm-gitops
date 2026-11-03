# 4.2. Overview of deploying managed clusters with GitOps ZTP

Red Hat Advanced Cluster Management (RHACM) uses GitOps Zero Touch Provisioning (ZTP) to deploy single-node OpenShift Container Platform clusters, three-node clusters, and standard clusters. You manage site configuration data as OpenShift Container Platform CRs in a Git repository. 

GitOps ZTP uses a declarative GitOps approach for a develop-once, deploy-anywhere model to deploy the managed clusters. 

The deployment of the clusters includes: 

  * Installing the host operating system (RHCOS) on a blank server 
  * Deploying OpenShift Container Platform 
  * Creating cluster policies and site subscriptions 
  * Making the necessary network configurations to the server operating system 
  * Deploying profile Operators and performing any needed software-related configuration, such as performance profile, PTP, and SR-IOV 



Note

To deploy clusters with virtualized control planes running on OpenShift Virtualization VMs instead of physical servers, you can use KubeVirt Redfish to expose VMs as Redfish endpoints. For more information, see "Virtualized control planes". 

**Additional resources**

  * [Understanding virtualized control planes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/virtualized_control_planes/#vcp-overview)
