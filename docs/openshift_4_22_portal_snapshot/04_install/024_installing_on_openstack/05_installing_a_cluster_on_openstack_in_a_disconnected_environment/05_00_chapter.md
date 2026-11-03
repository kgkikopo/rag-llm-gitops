# Chapter 5. Installing a cluster on OpenStack in a disconnected environment

In OpenShift Container Platform 4.22, you can install a cluster on Red Hat OpenStack Platform (RHOSP) in a restricted network by creating an internal mirror of the installation release content. 

Ensure that you meet the following prerequisites: 

  * You reviewed details about the OpenShift Container Platform installation and update processes. 
  * You read the documentation on selecting a cluster installation method and preparing it for users. 
  * You verified that OpenShift Container Platform 4.22 is compatible with your RHOSP version. For more information, see "Supported platforms for OpenShift Container Platform clusters". You can also compare platform support across different versions by viewing the "OpenShift Container Platform on RHOSP support matrix". 
  * You created a registry on your mirror host and obtained the `imageContentSources` data for your version of OpenShift Container Platform. Because the installation media is on the mirror host, you can use that computer to complete all installation steps. 
  * You understand performance and scalability practices for cluster scaling, control plane sizing, and etcd. For more information, see "Recommended control plane practices". 
  * You have the metadata service enabled in RHOSP. 



You can complete the following configurations after you install a cluster on Red Hat OpenStack Platform (RHOSP) in a disconnected environment: 

  * Customize your cluster. 
  * If the mirror registry that you used to install your cluster has a trusted CA, add it to the cluster by configuring additional trust stores. 
  * Enable remote health reporting. 
  * Register your disconnected cluster. 
  * Configure image streams for the Cluster Samples Operator and the `must-gather` tool. 
  * Learn how to use Operator Lifecycle Manager in disconnected environments. 
  * If you did not configure RHOSP to accept application traffic over floating IP addresses, configure RHOSP access with floating IP addresses. 



**Additional resources**

  * [Installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
  * [Selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing)
  * [Supported platforms for OpenShift Container Platform clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#supported-platforms-for-openshift-clusters_architecture-installation)
  * [OpenShift Container Platform on RHOSP support matrix (Knowledgebase article)](https://access.redhat.com/articles/4679401)
  * [Mirroring images for a disconnected installation by using the `oc adm` command](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installing-mirroring-installation-images)
  * [Recommended control plane practices](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#recommended-host-practices)
  * [Postinstallation cluster tasks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations)
  * [Image configuration resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#images-configuration-cas_image-configuration)
  * [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting)
  * [Registering your disconnected cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#insights-operator-register-disconnected-cluster_remote-health-reporting)
  * [Using Operator Lifecycle Manager in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#olm-restricted-networks)
  * [Configuring network settings after installing RHOSP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_openstack/installing-openstack-network-config#installation-osp-configuring-api-floating-ip_installing-openstack-network-config "7.1. Configuring application access with floating IP addresses")

- [5.1. About installations in restricted networks](05_01_about_installations_in_restricted_networks.md)
- [5.2. Resource guidelines for installing OpenShift Container Platform on RHOSP](05_02_resource_guidelines_for_installing_openshift_container_platform_on_rhosp.md)
- [5.3. Internet access for OpenShift Container Platform](05_03_internet_access_for_openshift_container_platform.md)
- [5.4. Enabling Swift on RHOSP](05_04_enabling_swift_on_rhosp.md)
- [5.5. Defining parameters for the installation program](05_05_defining_parameters_for_the_installation_program.md)
- [5.6. Setting OpenStack Cloud Controller Manager options](05_06_setting_openstack_cloud_controller_manager_options.md)
- [5.7. Creating the RHCOS image for restricted network installations](05_07_creating_the_rhcos_image_for_restricted_network_installations.md)
- [5.8. Creating the installation configuration file](05_08_creating_the_installation_configuration_file.md)
- [5.9. Generating a key pair for cluster node SSH access](05_09_generating_a_key_pair_for_cluster_node_ssh_access.md)
- [5.10. Access to the environment](05_10_access_to_the_environment.md)
- [5.11. Deploying the cluster](05_11_deploying_the_cluster.md)
- [5.12. Verifying cluster status](05_12_verifying_cluster_status.md)
- [5.13. Logging in to the cluster by using the CLI](05_13_logging_in_to_the_cluster_by_using_the_cli.md)
- [5.14. Disabling the default software catalog sources](05_14_disabling_the_default_software_catalog_sources.md)
- [5.15. Telemetry access for OpenShift Container Platform](05_15_telemetry_access_for_openshift_container_platform.md)
