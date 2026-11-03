# 1.1. Overcome the challenges of the network far edge

Today, service providers want to deploy their infrastructure at the edge of the network. This presents significant challenges: 

  * How do you handle deployments of many edge sites in parallel? 
  * What happens when you need to deploy sites in disconnected environments? 
  * How do you manage the lifecycle of large fleets of clusters? 



GitOps Zero Touch Provisioning (ZTP) and _GitOps_ meets these challenges by allowing you to provision remote edge sites at scale with declarative site definitions and configurations for bare-metal equipment. Template or overlay configurations install OpenShift Container Platform features that are required for CNF workloads. The full lifecycle of installation and upgrades is handled through the GitOps ZTP pipeline. 

GitOps ZTP uses GitOps for infrastructure deployments. With GitOps, you use declarative YAML files and other defined patterns stored in Git repositories. Red Hat Advanced Cluster Management (RHACM) uses your Git repositories to drive the deployment of your infrastructure. 

GitOps provides traceability, role-based access control (RBAC), and a single source of truth for the desired state of each site. Scalability issues are addressed by Git methodologies and event driven operations through webhooks. 

You start the GitOps ZTP workflow by creating declarative site definition and configuration custom resources (CRs) that the GitOps ZTP pipeline delivers to the edge nodes. 

The following diagram shows how GitOps ZTP works within the far edge framework. 

![GitOps ZTP at the network far edge](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Edge_computing-en-US/images/e01c06c618b6911917ac01992c4d7163/217_OpenShift_Zero_Touch_Provisioning_updates_1022_1.png) ![GitOps ZTP at the network far edge](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Edge_computing-en-US/images/e01c06c618b6911917ac01992c4d7163/217_OpenShift_Zero_Touch_Provisioning_updates_1022_1.png)
