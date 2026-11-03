# Chapter 10. Installing a cluster on user-provisioned infrastructure in Google Cloud by using Infrastructure Manager templates

In OpenShift Container Platform version 4.22, you can install a cluster on Google Cloud that uses infrastructure that you provide. 

The steps for performing a user-provided infrastructure install are outlined here. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods. 

Important

The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods; the templates are just an example.

- [10.1. Prerequisites](10_01_prerequisites.md)
- [10.2. Certificate signing requests management](10_02_certificate_signing_requests_management.md)
- [10.3. Internet access for OpenShift Container Platform](10_03_internet_access_for_openshift_container_platform.md)
- [10.4. Configuring your Google Cloud project](10_04_configuring_your_google_cloud_project.md)
- [10.5. Requirements for a cluster with user-provisioned infrastructure](10_05_requirements_for_a_cluster_with_user_provisioned_infrastructure.md)
- [10.6. Creating the installation files for Google Cloud](10_06_creating_the_installation_files_for_google_cloud.md)
- [10.7. Extracting the infrastructure name](10_07_extracting_the_infrastructure_name.md)
- [10.8. Exporting common variables for Infrastructure Manager templates](10_08_exporting_common_variables_for_infrastructure_manager_templates.md)
- [10.9. Creating a VPC in Google Cloud](10_09_creating_a_vpc_in_google_cloud.md)
- [10.10. Networking requirements for user-provisioned infrastructure](10_10_networking_requirements_for_user_provisioned_infrastructure.md)
- [10.11. Creating load balancers in Google Cloud](10_11_creating_load_balancers_in_google_cloud.md)
- [10.12. Creating a private DNS zone in Google Cloud](10_12_creating_a_private_dns_zone_in_google_cloud.md)
- [10.13. Creating firewall rules and IAM roles in Google Cloud](10_13_creating_firewall_rules_and_iam_roles_in_google_cloud.md)
- [10.14. Creating IAM policy bindings in Google Cloud](10_14_creating_iam_policy_bindings_in_google_cloud.md)
- [10.15. Creating the RHCOS cluster image for the Google Cloud infrastructure](10_15_creating_the_rhcos_cluster_image_for_the_google_cloud_infrastructure.md)
- [10.16. Creating the bootstrap machine in Google Cloud](10_16_creating_the_bootstrap_machine_in_google_cloud.md)
- [10.17. Creating the control plane machines in Google Cloud](10_17_creating_the_control_plane_machines_in_google_cloud.md)
- [10.18. Creating additional worker machines in Google Cloud](10_18_creating_additional_worker_machines_in_google_cloud.md)
- [10.19. Removing bootstrap resources in Google Cloud](10_19_removing_bootstrap_resources_in_google_cloud.md)
- [10.20. Install the OpenShift CLI on Linux](10_20_install_the_openshift_cli_on_linux.md)
- [10.21. Install the OpenShift CLI on Windows](10_21_install_the_openshift_cli_on_windows.md)
- [10.22. Install the OpenShift CLI on macOS](10_22_install_the_openshift_cli_on_macos.md)
- [10.23. Logging in to the cluster by using the CLI](10_23_logging_in_to_the_cluster_by_using_the_cli.md)
- [10.24. Approve the certificate signing requests for your machines](10_24_approve_the_certificate_signing_requests_for_your_machines.md)
- [10.25. Adding the ingress DNS records](10_25_adding_the_ingress_dns_records.md)
- [10.26. Completing a Google Cloud installation on user-provisioned infrastructure](10_26_completing_a_google_cloud_installation_on_user_provisioned_infrastructure.md)
- [10.27. Telemetry access for OpenShift Container Platform](10_27_telemetry_access_for_openshift_container_platform.md)
- [10.28. Additional resources](10_28_additional_resources.md)
