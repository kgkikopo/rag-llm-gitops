# Chapter 7. Guidance for clusters that span data centers

Evaluate considerations and metrics for OpenShift Container Platform clusters that span data centers so you can design supported, resilient multisite deployments. 

Red Hat strongly recommends a deployment model where OpenShift Container Platform clusters are deployed within a data center, but also acknowledges that there can be scenarios where a provider can use a deployment model where a cluster can span across data centers. This guidance outlines considerations when exploring the use of cluster deployments that span many data centers and describes important metrics that affect the supportability of such deployments. The design of such deployments must adhere to these guidelines for the product to function optimally and to ensure the highest quality of support with the appropriate product support subscriptions. 

Warning

A cluster deployment that spans many data centers extends the cluster as a single failure domain across locations and must not be considered a replacement for a disaster recovery plan. 

Clusters that span many data centers follow standard Red Hat OpenShift Container Platform support guidance. Review the "Red Hat OpenShift Container Platform Lifecycle" and "Red Hat Production Support Scope of Coverage" for more information. 

Do not deploy an OpenShift Container Platform cluster that spans many sites. If you need presence in many data centers or regions, deploy one cluster per region or site, and use tools such as Red Hat Advanced Cluster Management to manage those clusters and deployments. 

Some OpenShift Container Platform platforms support many data center deployments. Check the platform-specific product documentation and release notes for details. Other platforms can span data centers, depending on the quality of the network connectivity between nodes. For more information, see "Ensuring reliable etcd performance and scalability". 

When you implement a cluster deployment that spans many data centers, implement the practices in "Red Hat High Availability, and Recommended Practices". An alternative to multisite deployments is to deploy one OpenShift Container Platform cluster per site, managed by Red Hat Advanced Cluster Management.

- [7.1. Deployment caveats for spanned clusters](07_01_deployment_caveats_for_spanned_clusters.md)
- [7.2. Infrastructure as a Service (IaaS) and cloud provider considerations](07_02_infrastructure_as_a_service_iaas_and_cloud_provider_considerations.md)
- [7.3. Site recommendations for multisite clusters](07_03_site_recommendations_for_multisite_clusters.md)
- [7.4. Requirements for etcd, networking, and storage](07_04_requirements_for_etcd_networking_and_storage.md)
- [7.5. Workload placement considerations](07_05_workload_placement_considerations.md)
- [7.6. Additional resources](07_06_additional_resources.md)
