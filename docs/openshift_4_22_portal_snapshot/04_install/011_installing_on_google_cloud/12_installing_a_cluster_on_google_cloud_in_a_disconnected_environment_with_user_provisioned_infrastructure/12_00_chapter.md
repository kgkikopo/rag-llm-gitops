# Chapter 12. Installing a cluster on Google Cloud in a disconnected environment with user-provisioned infrastructure

In OpenShift Container Platform version 4.22, you can install a cluster on Google Cloud that uses infrastructure that you provide and an internal mirror of the installation release content. 

Important

While you can install an OpenShift Container Platform cluster by using mirrored installation release content, your cluster still requires internet access to use the Google Cloud APIs. 

The steps for performing a user-provided infrastructure install are outlined here. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods. 

Important

The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods; the templates are just an example.

- [12.1. Prerequisites](12_01_prerequisites.md)
- [12.2. About installations in restricted networks](12_02_about_installations_in_restricted_networks.md)
- [12.3. Internet access for OpenShift Container Platform](12_03_internet_access_for_openshift_container_platform.md)
- [12.4. Configuring your Google Cloud project](12_04_configuring_your_google_cloud_project.md)
- [12.5. Requirements for a cluster with user-provisioned infrastructure](12_05_requirements_for_a_cluster_with_user_provisioned_infrastructure.md)
- [12.6. Creating the installation files for Google Cloud](12_06_creating_the_installation_files_for_google_cloud.md)
- [12.7. Extracting the infrastructure name](12_07_extracting_the_infrastructure_name.md)
- [12.8. Exporting common variables for Infrastructure Manager templates](12_08_exporting_common_variables_for_infrastructure_manager_templates.md)
- [12.9. Creating a VPC in Google Cloud](12_09_creating_a_vpc_in_google_cloud.md)
- [12.10. Networking requirements for user-provisioned infrastructure](12_10_networking_requirements_for_user_provisioned_infrastructure.md)
- [12.11. Creating load balancers in Google Cloud](12_11_creating_load_balancers_in_google_cloud.md)
- [12.12. Creating a private DNS zone in Google Cloud](12_12_creating_a_private_dns_zone_in_google_cloud.md)
- [12.13. Creating firewall rules and IAM roles in Google Cloud](12_13_creating_firewall_rules_and_iam_roles_in_google_cloud.md)
- [12.14. Creating IAM policy bindings in Google Cloud](12_14_creating_iam_policy_bindings_in_google_cloud.md)
- [12.15. Creating the RHCOS cluster image for the Google Cloud infrastructure](12_15_creating_the_rhcos_cluster_image_for_the_google_cloud_infrastructure.md)
- [12.16. Creating the bootstrap machine in Google Cloud](12_16_creating_the_bootstrap_machine_in_google_cloud.md)
- [12.17. Creating the control plane machines in Google Cloud](12_17_creating_the_control_plane_machines_in_google_cloud.md)
- [12.18. Creating additional worker machines in Google Cloud](12_18_creating_additional_worker_machines_in_google_cloud.md)
- [12.19. Removing bootstrap resources in Google Cloud](12_19_removing_bootstrap_resources_in_google_cloud.md)
- [12.20. Logging in to the cluster by using the CLI](12_20_logging_in_to_the_cluster_by_using_the_cli.md)
- [12.21. Disabling the default software catalog sources](12_21_disabling_the_default_software_catalog_sources.md)
- [12.22. Approve the certificate signing requests for your machines](12_22_approve_the_certificate_signing_requests_for_your_machines.md)
- [12.23. Adding the ingress DNS records](12_23_adding_the_ingress_dns_records.md)
- [12.24. Completing a Google Cloud installation on user-provisioned infrastructure](12_24_completing_a_google_cloud_installation_on_user_provisioned_infrastructure.md)
- [12.25. Telemetry access for OpenShift Container Platform](12_25_telemetry_access_for_openshift_container_platform.md)
- [12.26. Additional resources](12_26_additional_resources.md)
