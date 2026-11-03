# Chapter 8. Installing a private cluster on Google Cloud

In OpenShift Container Platform version 4.22, you can install a private cluster into an existing VPC on Google Cloud with customizations by using installer-provisioned infrastructure. A private cluster keeps its endpoints internal, preventing direct internet exposure. 

You customize your cluster by modifying parameters in the `install-config.yaml` file before installation.

- [8.1. Prerequisites](08_01_prerequisites.md)
- [8.2. Private clusters](08_02_private_clusters.md)
- [8.3. About using a custom VPC](08_03_about_using_a_custom_vpc.md)
- [8.4. Internet access for OpenShift Container Platform](08_04_internet_access_for_openshift_container_platform.md)
- [8.5. Generating a key pair for cluster node SSH access](08_05_generating_a_key_pair_for_cluster_node_ssh_access.md)
- [8.6. Obtaining the installation program](08_06_obtaining_the_installation_program.md)
- [8.7. Manually creating the installation configuration file](08_07_manually_creating_the_installation_configuration_file.md)
- [8.8. Install the OpenShift CLI on Linux](08_08_install_the_openshift_cli_on_linux.md)
- [8.9. Install the OpenShift CLI on Windows](08_09_install_the_openshift_cli_on_windows.md)
- [8.10. Install the OpenShift CLI on macOS](08_10_install_the_openshift_cli_on_macos.md)
- [8.11. Alternatives to storing administrator-level secrets in the kube-system project](08_11_alternatives_to_storing_administrator_level_secrets_in_the_kube_system_project.md)
- [8.12. Deploying the cluster](08_12_deploying_the_cluster.md)
- [8.13. Provisioning your own DNS records](08_13_provisioning_your_own_dns_records.md)
- [8.14. Logging in to the cluster by using the CLI](08_14_logging_in_to_the_cluster_by_using_the_cli.md)
- [8.15. Telemetry access for OpenShift Container Platform](08_15_telemetry_access_for_openshift_container_platform.md)
- [8.16. Additional resources](08_16_additional_resources.md)
