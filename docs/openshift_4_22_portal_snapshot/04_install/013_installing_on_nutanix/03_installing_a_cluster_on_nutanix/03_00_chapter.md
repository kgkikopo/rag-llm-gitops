# Chapter 3. Installing a cluster on Nutanix

In OpenShift Container Platform version 4.22, you can choose one of the following options to install a cluster on your Nutanix instance: 

**Using installer-provisioned infrastructure** : Use the procedures in the following sections to use installer-provisioned infrastructure. Installer-provisioned infrastructure is ideal for installing in connected or disconnected network environments. The installer-provisioned infrastructure includes an installation program that provisions the underlying infrastructure for the cluster. 

**Using the Assisted Installer** : The Assisted Installer is hosted at console.redhat.com. The Assisted Installer cannot be used in disconnected environments. The Assisted Installer does not provision the underlying infrastructure for the cluster, so you must provision the infrastructure before you run the Assisted Installer. Installing with the Assisted Installer also provides integration with Nutanix, enabling autoscaling. 

**Using user-provisioned infrastructure** : You provision the underlying infrastructure yourself and then complete the relevant installation steps. 

**Additional resources**

  * [Assisted Installer](https://access.redhat.com/documentation/en-us/assisted_installer_for_openshift_container_platform)
  * [Installing an on-premise cluster using the Assisted Installer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on-premise_with_assisted_installer/#installing-on-prem-assisted)
  * [Installing a cluster on any platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_any_platform/#installing-platform-agnostic)

- [3.1. Prerequisites](03_01_prerequisites.md)
- [3.2. Internet access for OpenShift Container Platform](03_02_internet_access_for_openshift_container_platform.md)
- [3.3. Internet access for Prism Central](03_03_internet_access_for_prism_central.md)
- [3.4. Generating a key pair for cluster node SSH access](03_04_generating_a_key_pair_for_cluster_node_ssh_access.md)
- [3.5. Obtaining the installation program](03_05_obtaining_the_installation_program.md)
- [3.6. Adding Nutanix root CA certificates to your system trust](03_06_adding_nutanix_root_ca_certificates_to_your_system_trust.md)
- [3.7. Creating the installation configuration file](03_07_creating_the_installation_configuration_file.md)
- [3.8. Install the OpenShift CLI on Linux](03_08_install_the_openshift_cli_on_linux.md)
- [3.9. Install the OpenShift CLI on Windows](03_09_install_the_openshift_cli_on_windows.md)
- [3.10. Install the OpenShift CLI on macOS](03_10_install_the_openshift_cli_on_macos.md)
- [3.11. Configuring IAM for Nutanix](03_11_configuring_iam_for_nutanix.md)
- [3.12. Adding config map and secret resources required for Nutanix CCM](03_12_adding_config_map_and_secret_resources_required_for_nutanix_ccm.md)
- [3.13. Services for a user-managed load balancer](03_13_services_for_a_user_managed_load_balancer.md)
- [3.14. Deploying the cluster](03_14_deploying_the_cluster.md)
- [3.15. Configuring the default storage container](03_15_configuring_the_default_storage_container.md)
- [3.16. Telemetry access for OpenShift Container Platform](03_16_telemetry_access_for_openshift_container_platform.md)
- [3.17. Additional resources](03_17_additional_resources.md)
