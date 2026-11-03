# Chapter 5. Manually installing a single-node OpenShift cluster with GitOps ZTP

You can deploy a managed single-node OpenShift cluster by using Red Hat Advanced Cluster Management (RHACM) and the assisted service. 

Note

If you are creating multiple managed clusters, use the `ClusterInstance` method described in [Deploying far edge sites with ZTP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/ztp-deploying-far-edge-sites "Chapter 4. Installing managed clusters with RHACM and ClusterInstance resources"). 

Important

The target bare-metal host must meet the networking, firmware, and hardware requirements listed in [Recommended cluster configuration for vDU application workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/edge_computing/sno-configure-for-vdu "Chapter 7. Recommended single-node OpenShift cluster configuration for vDU application workloads").

- [5.1. Extracting reference and example CRs from the ztp-site-generate container](05_01_extracting_reference_and_example_crs_from_the_ztp_site_generate_container.md)
- [5.2. Create the managed bare-metal host secrets](05_02_create_the_managed_bare_metal_host_secrets.md)
- [5.3. Configuring Discovery ISO kernel arguments for manual installations using GitOps ZTP](05_03_configuring_discovery_iso_kernel_arguments_for_manual_installations_using_gitops_ztp.md)
- [5.4. Installing a single managed cluster](05_04_installing_a_single_managed_cluster.md)
- [5.5. Late binding for bare-metal host pools in GitOps ZTP deployments](05_05_late_binding_for_bare_metal_host_pools_in_gitops_ztp_deployments.md)
- [5.6. Bind bare-metal hosts to clusters using the cluster-reference annotation in GitOps ZTP deployments](05_06_bind_bare_metal_hosts_to_clusters_using_the_cluster_reference_annotation_in_gitops_ztp_deployments.md)
- [5.7. BareMetalHost cluster-reference annotation](05_07_baremetalhost_cluster_reference_annotation.md)
- [5.8. Monitoring the managed cluster installation status](05_08_monitoring_the_managed_cluster_installation_status.md)
- [5.9. Troubleshooting the managed cluster](05_09_troubleshooting_the_managed_cluster.md)
- [5.10. RHACM generated cluster installation CRs](05_10_rhacm_generated_cluster_installation_crs.md)
