# Chapter 5. Installing a cluster on Google Cloud in a disconnected environment

In OpenShift Container Platform 4.22, you can install a cluster on Google Cloud in a restricted network by creating an internal mirror of the installation release content on an existing Google Virtual Private Cloud (VPC). 

Important

You can install an OpenShift Container Platform cluster by using mirrored installation release content, but your cluster will require internet access to use the Google Cloud APIs.

- [5.1. Prerequisites](05_01_prerequisites.md)
- [5.2. About installations in restricted networks](05_02_about_installations_in_restricted_networks.md)
- [5.3. Internet access for OpenShift Container Platform](05_03_internet_access_for_openshift_container_platform.md)
- [5.4. Generating a key pair for cluster node SSH access](05_04_generating_a_key_pair_for_cluster_node_ssh_access.md)
- [5.5. Creating the installation configuration file](05_05_creating_the_installation_configuration_file.md)
- [5.6. Install the OpenShift CLI on Linux](05_06_install_the_openshift_cli_on_linux.md)
- [5.7. Install the OpenShift CLI on Windows](05_07_install_the_openshift_cli_on_windows.md)
- [5.8. Install the OpenShift CLI on macOS](05_08_install_the_openshift_cli_on_macos.md)
- [5.9. Alternatives to storing administrator-level secrets in the kube-system project](05_09_alternatives_to_storing_administrator_level_secrets_in_the_kube_system_project.md)
- [5.10. Deploying the cluster](05_10_deploying_the_cluster.md)
- [5.11. Provisioning your own DNS records](05_11_provisioning_your_own_dns_records.md)
- [5.12. Logging in to the cluster by using the CLI](05_12_logging_in_to_the_cluster_by_using_the_cli.md)
- [5.13. Disabling the default software catalog sources](05_13_disabling_the_default_software_catalog_sources.md)
- [5.14. Telemetry access for OpenShift Container Platform](05_14_telemetry_access_for_openshift_container_platform.md)
- [5.15. Additional resources](05_15_additional_resources.md)
