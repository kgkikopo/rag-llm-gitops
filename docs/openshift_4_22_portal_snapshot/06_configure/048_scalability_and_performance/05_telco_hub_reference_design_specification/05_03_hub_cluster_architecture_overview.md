# 5.3. Hub cluster architecture overview

Use the features and components running on the management hub cluster to manage many other clusters in a hub-and-spoke topology. The hub cluster provides a highly available and centralized interface for managing the configuration, lifecycle, and observability of the fleet of deployed clusters. 

Note

All management hub functionality can be deployed on a dedicated OpenShift Container Platform cluster or as applications that are co-resident on an existing cluster. 

Managed cluster lifecycle
     Using a combination of Day 2 Operators, the hub cluster provides the necessary infrastructure to deploy and configure the fleet of clusters by using a GitOps methodology. Over the lifetime of the deployed clusters, further management of upgrades, scaling the number of clusters, node replacement, and other lifecycle management functions can be declaratively defined and rolled out. You can control the timing and progression of the rollout across the fleet. 
Monitoring
     The hub cluster provides monitoring and status reporting for the managed clusters through the Observability pillar of the RHACM Operator. This includes aggregated metrics, alerts, and compliance monitoring through the Governance policy framework. 

The telco management hub reference design specification (RDS) and the associated reference custom resources (CRs) describe the telco engineering and QE validated method for deploying, configuring and managing the lifecycle of telco managed cluster infrastructure. The reference configuration includes the installation and configuration of the hub cluster components on top of OpenShift Container Platform. 

**Figure 5.1. Hub cluster reference design components**

![telco hub cluster reference design components](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/e3f13b66c7c0d1d5cbc56a3a25f19db6/telco-hub-cluster-reference-design-components.png) ![telco hub cluster reference design components](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/e3f13b66c7c0d1d5cbc56a3a25f19db6/telco-hub-cluster-reference-design-components.png)

**Figure 5.2. Hub cluster reference design architecture**

![telco hub cluster rds architecture](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/b99320fdbc83f79efb2ca7cb6bc0e018/telco-hub-cluster-rds-architecture.png) ![telco hub cluster rds architecture](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/b99320fdbc83f79efb2ca7cb6bc0e018/telco-hub-cluster-rds-architecture.png)
