# Chapter 11. Installing a cluster into a shared VPC on Google Cloud using Infrastructure Manager templates

In OpenShift Container Platform version 4.22, you can install a cluster into a shared Virtual Private Cloud (VPC) on Google Cloud that uses infrastructure that you provide. In this context, a cluster installed into a shared VPC is a cluster that is configured to use a VPC from a project different from where the cluster is being deployed. 

A shared VPC enables an organization to connect resources from multiple projects to a common VPC network. You can communicate within the organization securely and efficiently by using internal IPs from that network. For more information about shared VPC, see "Shared VPC overview" in the Google Cloud documentation 

The steps for performing a user-provided infrastructure installation into a shared VPC are outlined here. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods. 

Important

The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods; the templates are just an example.

- [11.1. Prerequisites](11_01_prerequisites.md)
- [11.2. Certificate signing requests management](11_02_certificate_signing_requests_management.md)
- [11.3. Internet access for OpenShift Container Platform](11_03_internet_access_for_openshift_container_platform.md)
- [11.4. Configuring the Google Cloud project that hosts your cluster](11_04_configuring_the_google_cloud_project_that_hosts_your_cluster.md)
- [11.5. Requirements for a cluster with user-provisioned infrastructure](11_05_requirements_for_a_cluster_with_user_provisioned_infrastructure.md)
- [11.6. Configuring the Google Cloud project that hosts your shared VPC network](11_06_configuring_the_google_cloud_project_that_hosts_your_shared_vpc_network.md)
- [11.7. Creating the installation files for Google Cloud](11_07_creating_the_installation_files_for_google_cloud.md)
- [11.8. Extracting the infrastructure name](11_08_extracting_the_infrastructure_name.md)
- [11.9. Exporting common variables for Infrastructure Manager templates](11_09_exporting_common_variables_for_infrastructure_manager_templates.md)
- [11.10. Networking requirements for user-provisioned infrastructure](11_10_networking_requirements_for_user_provisioned_infrastructure.md)
- [11.11. Creating load balancers in Google Cloud](11_11_creating_load_balancers_in_google_cloud.md)
- [11.12. Creating a private DNS zone in Google Cloud](11_12_creating_a_private_dns_zone_in_google_cloud.md)
- [11.13. Creating firewall rules and IAM roles in Google Cloud](11_13_creating_firewall_rules_and_iam_roles_in_google_cloud.md)
- [11.14. Creating IAM policy bindings in Google Cloud](11_14_creating_iam_policy_bindings_in_google_cloud.md)
- [11.15. Creating the RHCOS cluster image for the Google Cloud infrastructure](11_15_creating_the_rhcos_cluster_image_for_the_google_cloud_infrastructure.md)
- [11.16. Creating the bootstrap machine in Google Cloud](11_16_creating_the_bootstrap_machine_in_google_cloud.md)
- [11.17. Creating the control plane machines in Google Cloud](11_17_creating_the_control_plane_machines_in_google_cloud.md)
- [11.18. Creating additional worker machines in Google Cloud](11_18_creating_additional_worker_machines_in_google_cloud.md)
- [11.19. Removing bootstrap resources in Google Cloud](11_19_removing_bootstrap_resources_in_google_cloud.md)
- [11.20. Install the OpenShift CLI on Linux](11_20_install_the_openshift_cli_on_linux.md)
- [11.21. Install the OpenShift CLI on Windows](11_21_install_the_openshift_cli_on_windows.md)
- [11.22. Install the OpenShift CLI on macOS](11_22_install_the_openshift_cli_on_macos.md)
- [11.23. Logging in to the cluster by using the CLI](11_23_logging_in_to_the_cluster_by_using_the_cli.md)
- [11.24. Approve the certificate signing requests for your machines](11_24_approve_the_certificate_signing_requests_for_your_machines.md)
- [11.25. Adding the ingress DNS records](11_25_adding_the_ingress_dns_records.md)
- [11.26. Adding ingress firewall rules](11_26_adding_ingress_firewall_rules.md)
- [11.27. Completing a Google Cloud installation on user-provisioned infrastructure](11_27_completing_a_google_cloud_installation_on_user_provisioned_infrastructure.md)
- [11.28. Telemetry access for OpenShift Container Platform](11_28_telemetry_access_for_openshift_container_platform.md)
- [11.29. Additional resources](11_29_additional_resources.md)
