# Chapter 4. Installing a cluster on Google Cloud with customizations

In OpenShift Container Platform version 4.22, you can install a cluster on Google Cloud with customizations by using installer-provisioned infrastructure. You customize the cluster to match your environment by modifying parameters in the `install-config.yaml` file before installation. 

By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations. 

You must set most of the network configuration parameters during installation, and you can modify only `kubeProxy` configuration parameters in a running cluster.

- [4.1. Prerequisites](04_01_prerequisites.md)
- [4.2. Internet access for OpenShift Container Platform](04_02_internet_access_for_openshift_container_platform.md)
- [4.3. Generating a key pair for cluster node SSH access](04_03_generating_a_key_pair_for_cluster_node_ssh_access.md)
- [4.4. Obtaining the installation program](04_04_obtaining_the_installation_program.md)
- [4.5. Creating the installation configuration file](04_05_creating_the_installation_configuration_file.md)
- [4.6. Managing user-defined labels and tags for Google Cloud](04_06_managing_user_defined_labels_and_tags_for_google_cloud.md)
- [4.7. Install the OpenShift CLI on Linux](04_07_install_the_openshift_cli_on_linux.md)
- [4.8. Install the OpenShift CLI on Windows](04_08_install_the_openshift_cli_on_windows.md)
- [4.9. Install the OpenShift CLI on macOS](04_09_install_the_openshift_cli_on_macos.md)
- [4.10. Alternatives to storing administrator-level secrets in the kube-system project](04_10_alternatives_to_storing_administrator_level_secrets_in_the_kube_system_project.md)
- [4.11. Using the Google Cloud Marketplace offering](04_11_using_the_google_cloud_marketplace_offering.md)
- [4.12. Network configuration phases](04_12_network_configuration_phases.md)
- [4.13. Specifying advanced network configuration](04_13_specifying_advanced_network_configuration.md)
- [4.14. Cluster Network Operator configuration](04_14_cluster_network_operator_configuration.md)
- [4.15. Deploying the cluster](04_15_deploying_the_cluster.md)
- [4.16. Provisioning your own DNS records](04_16_provisioning_your_own_dns_records.md)
- [4.17. Logging in to the cluster by using the CLI](04_17_logging_in_to_the_cluster_by_using_the_cli.md)
- [4.18. Telemetry access for OpenShift Container Platform](04_18_telemetry_access_for_openshift_container_platform.md)
- [4.19. Additional resources](04_19_additional_resources.md)
