# Chapter 4. Installing a cluster on OpenStack on your own infrastructure

In OpenShift Container Platform version 4.22, you can install a cluster on Red Hat OpenStack Platform (RHOSP) that runs on user-provisioned infrastructure. 

By using your own infrastructure, you can integrate your cluster with existing infrastructure and modifications. The process requires more effort on your part than installer-provisioned installations, because you must create all RHOSP resources, like Nova servers, Neutron ports, and security groups. However, Red Hat provides Ansible playbooks to help you in the deployment process. 

Ensure that you meet the following prerequisites: 

  * You reviewed details about the OpenShift Container Platform installation and update processes. 
  * You read the documentation on selecting a cluster installation method and preparing it for users. 
  * You verified that OpenShift Container Platform 4.22 is compatible with your RHOSP version by using the "Supported platforms for OpenShift Container Platform clusters" section. You can also compare platform support across different versions by viewing the OpenShift Container Platform on RHOSP support matrix. 
  * You have an RHOSP account where you want to install OpenShift Container Platform. 
  * You understand performance and scalability practices for cluster scaling, control plane sizing, and etcd. For more information, see "Recommended control plane practices". 
  * On the machine from which you run the installation program, you have: 

    * A single directory in which you can keep the files you create during the installation process 
    * Python 3 




You can complete the following configurations after you install a cluster on RHOSP on your own infrastructure: 

  * Customize your cluster. 
  * If necessary, you can use remote health reporting. 
  * If you need to enable external access to node ports, configure ingress cluster traffic by using a node port. 
  * If you did not configure RHOSP to accept application traffic over floating IP addresses, configure RHOSP access with floating IP addresses. 



**Additional resources**

  * [Installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
  * [Selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing)
  * [Supported platforms for OpenShift Container Platform clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#supported-platforms-for-openshift-clusters_architecture-installation)
  * [OpenShift Container Platform on RHOSP support matrix](https://access.redhat.com/articles/4679401)
  * [Recommended control plane practices](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#recommended-host-practices)
  * [Postinstallation cluster tasks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations)
  * [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting)
  * [Configuring ingress cluster traffic by using a NodePort](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ingress_and_load_balancing/#nw-using-nodeport_configuring-ingress-cluster-traffic-nodeport)
  * [Configuring network settings after installing RHOSP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_openstack/installing-openstack-network-config#installation-osp-configuring-api-floating-ip_installing-openstack-network-config "7.1. Configuring application access with floating IP addresses")

- [4.1. Internet access for OpenShift Container Platform](04_01_internet_access_for_openshift_container_platform.md)
- [4.2. Resource guidelines for installing OpenShift Container Platform on RHOSP](04_02_resource_guidelines_for_installing_openshift_container_platform_on_rhosp.md)
- [4.3. Downloading playbook dependencies](04_03_downloading_playbook_dependencies.md)
- [4.4. Downloading the installation playbooks](04_04_downloading_the_installation_playbooks.md)
- [4.5. Obtaining the installation program](04_05_obtaining_the_installation_program.md)
- [4.6. Generating a key pair for cluster node SSH access](04_06_generating_a_key_pair_for_cluster_node_ssh_access.md)
- [4.7. Creating the Red Hat Enterprise Linux CoreOS (RHCOS) image](04_07_creating_the_red_hat_enterprise_linux_coreos_rhcos_image.md)
- [4.8. Verifying external network access](04_08_verifying_external_network_access.md)
- [4.9. Access to the environment](04_09_access_to_the_environment.md)
- [4.10. Defining parameters for the installation program](04_10_defining_parameters_for_the_installation_program.md)
- [4.11. Creating network resources on RHOSP](04_11_creating_network_resources_on_rhosp.md)
- [4.12. Creating the installation configuration file](04_12_creating_the_installation_configuration_file.md)
- [4.13. Creating the Kubernetes manifest and Ignition config files](04_13_creating_the_kubernetes_manifest_and_ignition_config_files.md)
- [4.14. Preparing the bootstrap Ignition files](04_14_preparing_the_bootstrap_ignition_files.md)
- [4.15. Creating control plane Ignition config files on RHOSP](04_15_creating_control_plane_ignition_config_files_on_rhosp.md)
- [4.16. Updating network resources on RHOSP](04_16_updating_network_resources_on_rhosp.md)
- [4.17. Creating the bootstrap machine on RHOSP](04_17_creating_the_bootstrap_machine_on_rhosp.md)
- [4.18. Creating the control plane machines on RHOSP](04_18_creating_the_control_plane_machines_on_rhosp.md)
- [4.19. Logging in to the cluster by using the CLI](04_19_logging_in_to_the_cluster_by_using_the_cli.md)
- [4.20. Deleting bootstrap resources from RHOSP](04_20_deleting_bootstrap_resources_from_rhosp.md)
- [4.21. Creating compute machines on RHOSP](04_21_creating_compute_machines_on_rhosp.md)
- [4.22. Approve the certificate signing requests for your machines](04_22_approve_the_certificate_signing_requests_for_your_machines.md)
- [4.23. Verifying a successful installation](04_23_verifying_a_successful_installation.md)
- [4.24. Telemetry access for OpenShift Container Platform](04_24_telemetry_access_for_openshift_container_platform.md)
