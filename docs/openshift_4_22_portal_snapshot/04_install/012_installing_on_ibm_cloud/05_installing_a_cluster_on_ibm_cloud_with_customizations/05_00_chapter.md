# Chapter 5. Installing a cluster on IBM Cloud with customizations

In OpenShift Container Platform version 4.22, you can install a customized cluster on IBM Cloud® by using installer-provisioned infrastructure. Change parameters in the `install-config.yaml` file before you install the cluster. 

By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations. 

You must set most of the network configuration parameters during installation, and you can change only `kubeProxy` configuration parameters in a running cluster.

- [5.1. Prerequisites for installing a cluster on IBM Cloud(R)](05_01_prerequisites_for_installing_a_cluster_on_ibm_cloud_r.md)
- [5.2. Internet access for OpenShift Container Platform](05_02_internet_access_for_openshift_container_platform.md)
- [5.3. Generating a key pair for cluster node SSH access](05_03_generating_a_key_pair_for_cluster_node_ssh_access.md)
- [5.4. Obtaining the installation program](05_04_obtaining_the_installation_program.md)
- [5.5. Exporting the API key](05_05_exporting_the_api_key.md)
- [5.6. Creating the installation configuration file](05_06_creating_the_installation_configuration_file.md)
- [5.7. Manually creating IAM](05_07_manually_creating_iam.md)
- [5.8. Network configuration phases](05_08_network_configuration_phases.md)
- [5.9. Specifying advanced network configuration](05_09_specifying_advanced_network_configuration.md)
- [5.10. Cluster Network Operator configuration](05_10_cluster_network_operator_configuration.md)
- [5.11. Deploying the cluster](05_11_deploying_the_cluster.md)
- [5.12. Install the OpenShift CLI on Linux](05_12_install_the_openshift_cli_on_linux.md)
- [5.13. Install the OpenShift CLI on Windows](05_13_install_the_openshift_cli_on_windows.md)
- [5.14. Install the OpenShift CLI on macOS](05_14_install_the_openshift_cli_on_macos.md)
- [5.15. Logging in to the cluster by using the CLI](05_15_logging_in_to_the_cluster_by_using_the_cli.md)
- [5.16. Telemetry access for OpenShift Container Platform](05_16_telemetry_access_for_openshift_container_platform.md)
- [5.17. Additional resources](05_17_additional_resources.md)
