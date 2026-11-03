# 7.1. Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes. For more information, see "Installation and update". 
  * You read the documentation on selecting a cluster installation method and preparing it for users. For more information, see "Selecting a cluster installation method and preparing it for users". 
  * If you use a firewall, you configured it to allow the sites that your cluster requires access to. For more information, see "Configuring your firewall for OpenShift Container Platform". 
  * You configured a Google Cloud project to host the cluster. This project, known as the service project, must be attached to the host project. For more information, see "Configuring a Google Cloud project". 
  * You have a Google Cloud host project that contains a shared VPC network and that has a configured Cloud Router and Cloud NAT gateway, to ensure that internet access from the VPC is available. 
  * You have a Google Cloud service account that has the required Google Cloud permissions in both the host and service projects. For more information, see "Required Google Cloud permissions for shared VPC installations". 
  * If you want to provide your own private hosted zone, you must have created one in the service project with the DNS pattern `cluster-name.baseDomain.`, for example `testCluster.example.com.`. The private hosted zone must be bound to the VPC in the host project. If you do not provide a private hosted zone, the installation program provisions one automatically. 
  * If you manage your Google Cloud firewall rules, you configured the required firewall rules. For more information, see "Managing your own firewall rules". 



**Additional resources**

  * [Installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
  * [Selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing)
  * [Configuring your firewall for OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall)
  * [Configuring a Google Cloud project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-account "Chapter 2. Configuring a Google Cloud project")
  * [Attaching service projects](https://cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared)
  * [Cloud Router overview](https://cloud.google.com/network-connectivity/docs/router/concepts/overview)
  * [Cloud NAT overview](https://cloud.google.com/nat/docs/overview)
  * [Required Google Cloud permissions for shared VPC installations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-account#minimum-required-permissions-ipi-gcp-xpn_installing-gcp-account "2.5.3. Required Google Cloud permissions for shared VPC installations")
  * [Create a zone with cross-project binding](https://cloud.google.com/dns/docs/zones/cross-project-binding)
  * [Managing your own firewall rules](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-account#installation-gcp-user-managed-firewall-rules_installing-gcp-account "2.6. Managing your own firewall rules")
