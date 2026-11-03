# 12.1. Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes. For more information, see "Installation and update". 
  * You read the documentation on selecting a cluster installation method and preparing it for users. For more information, see "Selecting a cluster installation method and preparing it for users". 
  * You created a registry on your mirror host and obtained the `imageContentSources` data for your version of OpenShift Container Platform. For more information, see "Mirroring images for a disconnected installation". 

Important

Because the installation media is on the mirror host, you can use that computer to complete all installation steps. 

  * If you use a firewall, you configured it to allow the sites that your cluster requires access to. While you might need to grant access to more sites, you must grant access to `*.googleapis.com` and `accounts.google.com`. For more information, see "Configuring your firewall for OpenShift Container Platform". 
  * If the cloud identity and access management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, you can manually create and maintain long-term credentials. For more information, see "Manually creating long-term credentials". 



**Additional resources**

  * [Installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
  * [Selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing)
  * [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installing-mirroring-installation-images)
  * [Configuring your firewall for OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall)
  * [Manually creating long-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-customizations#manually-create-iam_installing-gcp-customizations "4.10.1. Manually creating long-term credentials")
