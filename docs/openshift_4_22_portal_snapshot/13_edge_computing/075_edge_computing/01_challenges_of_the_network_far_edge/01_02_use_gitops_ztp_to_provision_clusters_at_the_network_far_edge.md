# 1.2. Use GitOps ZTP to provision clusters at the network far edge

Red Hat Advanced Cluster Management (RHACM) manages clusters in a hub-and-spoke architecture, where a single hub cluster manages many spoke clusters. 

Hub clusters running RHACM provision and deploy the managed clusters by using GitOps Zero Touch Provisioning (ZTP) and the assisted service that is deployed when you install RHACM. 

The assisted service handles provisioning of OpenShift Container Platform on single node clusters, three-node clusters, or standard clusters running on bare metal. 

A high-level overview of using GitOps ZTP to provision and maintain bare-metal hosts with OpenShift Container Platform is as follows: 

  * A hub cluster running RHACM manages an OpenShift image registry that mirrors the OpenShift Container Platform release images. RHACM uses the OpenShift image registry to provision the managed clusters. 
  * You manage the bare-metal hosts in a YAML format inventory file, versioned in a Git repository. 
  * You make the hosts ready for provisioning as managed clusters, and use RHACM and the assisted service to install the bare-metal hosts on site. 



Installing and deploying the clusters is a two-stage process, involving an initial installation phase, and a subsequent configuration and deployment phase. The following diagram illustrates this workflow: 

![Using GitOps and GitOps ZTP to install and deploy managed clusters](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Edge_computing-en-US/images/49638150ef1e67e49939ea47d170e45f/474_OpenShift_OpenShift_RAN_RDS_arch_updates_1023.png) ![Using GitOps and GitOps ZTP to install and deploy managed clusters](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Edge_computing-en-US/images/49638150ef1e67e49939ea47d170e45f/474_OpenShift_OpenShift_RAN_RDS_arch_updates_1023.png)
