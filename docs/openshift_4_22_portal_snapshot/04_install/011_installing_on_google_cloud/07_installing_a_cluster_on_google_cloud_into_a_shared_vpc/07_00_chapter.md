# Chapter 7. Installing a cluster on Google Cloud into a shared VPC

In OpenShift Container Platform version 4.22, you can install a cluster into a shared Virtual Private Cloud (VPC) on Google Cloud. In this installation method, the cluster is configured to use a VPC from a different Google Cloud project. A shared VPC enables an organization to connect resources from multiple projects to a common VPC network. You can communicate within the organization securely and efficiently by using internal IP addresses from that network. 

The installation program provisions the rest of the required infrastructure, which you can further customize. To customize the installation, change parameters in the `install-config.yaml` file before you install the cluster. 

**Additional resources**

  * [Shared VPC overview](https://cloud.google.com/vpc/docs/shared-vpc)

- [7.1. Prerequisites](07_01_prerequisites.md)
- [7.2. Internet access for OpenShift Container Platform](07_02_internet_access_for_openshift_container_platform.md)
- [7.3. Generating a key pair for cluster node SSH access](07_03_generating_a_key_pair_for_cluster_node_ssh_access.md)
- [7.4. Obtaining the installation program](07_04_obtaining_the_installation_program.md)
- [7.5. Creating the installation files for Google Cloud](07_05_creating_the_installation_files_for_google_cloud.md)
- [7.6. Install the OpenShift CLI on Linux](07_06_install_the_openshift_cli_on_linux.md)
- [7.7. Install the OpenShift CLI on Windows](07_07_install_the_openshift_cli_on_windows.md)
- [7.8. Install the OpenShift CLI on macOS](07_08_install_the_openshift_cli_on_macos.md)
- [7.9. Alternatives to storing administrator-level secrets in the kube-system project](07_09_alternatives_to_storing_administrator_level_secrets_in_the_kube_system_project.md)
- [7.10. Deploying the cluster](07_10_deploying_the_cluster.md)
- [7.11. Provisioning your own DNS records](07_11_provisioning_your_own_dns_records.md)
- [7.12. Logging in to the cluster by using the CLI](07_12_logging_in_to_the_cluster_by_using_the_cli.md)
- [7.13. Telemetry access for OpenShift Container Platform](07_13_telemetry_access_for_openshift_container_platform.md)
- [7.14. Additional resources](07_14_additional_resources.md)
