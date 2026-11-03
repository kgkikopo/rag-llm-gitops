# Chapter 3. Installing a cluster on OpenStack with customizations

In OpenShift Container Platform version 4.22, you can install a customized cluster on Red Hat OpenStack Platform (RHOSP). To customize the installation, modify parameters in the `install-config.yaml` before you install the cluster. 

Ensure that you meet the following prerequisites: 

  * You reviewed details about the OpenShift Container Platform installation and update processes. 
  * You read the documentation on selecting a cluster installation method and preparing it for users. 
  * You verified that OpenShift Container Platform 4.22 is compatible with your RHOSP version by using the supported platforms for OpenShift Container Platform clusters section. You can also compare platform support across different versions by viewing the OpenShift Container Platform on RHOSP support matrix. 
  * You have a storage service installed in RHOSP, such as block storage (Cinder) or object storage (Swift). Object storage is the recommended storage technology for OpenShift Container Platform registry cluster deployment. For more information, see "Optimizing storage". 
  * You understand performance and scalability practices for cluster scaling, control plane sizing, and etcd. For more information, see "Recommended practices for scaling the cluster". 
  * You have the metadata service enabled in RHOSP. 



You can complete the following configurations after you install a cluster on RHOSP with customizations: 

  * Customize your cluster. 
  * Enable remote health reporting. 
  * Configure ingress cluster traffic by using a node port. 
  * If you did not configure RHOSP to accept application traffic over floating IP addresses, configure RHOSP access with floating IP addresses. 



**Additional resources**

  * [Installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
  * [Selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing)
  * [Supported platforms for OpenShift Container Platform clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#supported-platforms-for-openshift-clusters_architecture-installation)
  * [OpenShift Container Platform on RHOSP support matrix (Red Hat Knowledgebase)](https://access.redhat.com/articles/4679401)
  * [Optimizing storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#optimizing-storage)
  * [Recommended practices for scaling the cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#recommended-host-practices)

- [3.1. Resource guidelines for installing OpenShift Container Platform on RHOSP](03_01_resource_guidelines_for_installing_openshift_container_platform_on_rhosp.md)
- [3.2. Internet access for OpenShift Container Platform](03_02_internet_access_for_openshift_container_platform.md)
- [3.3. Enabling Swift on RHOSP](03_03_enabling_swift_on_rhosp.md)
- [3.4. Configuring an image registry with custom storage on clusters that run on RHOSP](03_04_configuring_an_image_registry_with_custom_storage_on_clusters_that_run_on_rhosp.md)
- [3.5. Verifying external network access](03_05_verifying_external_network_access.md)
- [3.6. Defining parameters for the installation program](03_06_defining_parameters_for_the_installation_program.md)
- [3.7. Setting OpenStack Cloud Controller Manager options](03_07_setting_openstack_cloud_controller_manager_options.md)
- [3.8. Obtaining the installation program](03_08_obtaining_the_installation_program.md)
- [3.9. Creating the installation configuration file](03_09_creating_the_installation_configuration_file.md)
- [3.10. Generating a key pair for cluster node SSH access](03_10_generating_a_key_pair_for_cluster_node_ssh_access.md)
- [3.11. Access to the environment](03_11_access_to_the_environment.md)
- [3.12. Deploying the cluster](03_12_deploying_the_cluster.md)
- [3.13. Verifying cluster status](03_13_verifying_cluster_status.md)
- [3.14. Logging in to the cluster by using the CLI](03_14_logging_in_to_the_cluster_by_using_the_cli.md)
- [3.15. Telemetry access for OpenShift Container Platform](03_15_telemetry_access_for_openshift_container_platform.md)
- [3.16. Additional resources](03_16_additional_resources.md)
