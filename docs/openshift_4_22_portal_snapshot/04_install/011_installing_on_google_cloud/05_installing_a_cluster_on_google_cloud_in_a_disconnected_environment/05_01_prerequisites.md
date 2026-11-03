# 5.1. Prerequisites

* You reviewed details about the OpenShift Container Platform installation and update processes. For more information, see "Installation and update". 
  * You read the documentation on selecting a cluster installation method and preparing it for users. For more information, see "Selecting a cluster installation method and preparing it for users". 
  * You configured a Google Cloud project to host the cluster. For more information, see "Configuring a Google Cloud project". 
  * You mirrored the images for a disconnected installation to your registry and obtained the `imageContentSources` data for your version of OpenShift Container Platform. For more information, see "Mirroring images for a disconnected installation". 

Important

Because the installation media is on the mirror host, you can use that computer to complete all installation steps. 

  * You have an existing VPC in Google Cloud. When you install a cluster in a restricted network by using installer-provisioned infrastructure, you cannot use the VPC that the installation program creates. You must use a user-provisioned VPC that satisfies one of the following requirements: 

    * Contains the mirror registry 
    * Has firewall rules or a peering connection to access the mirror registry hosted elsewhere 

  * If you use a firewall, you configured it to allow the sites that your cluster requires access to. You might need to grant access to more sites, but you must grant access to `*.googleapis.com` and `accounts.google.com`. For more information, see "Configuring your firewall for OpenShift Container Platform". 
  * If you are installing by using a Private Service Connect (PSC) endpoint, you must configure the endpoint in the same VPC where you install the cluster, as specified in the `install-config.yaml` file. For more information, see "Installing a cluster on Google Cloud into an existing VPC". 



**Additional resources**

  * [Installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
  * [Selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing)
  * [Configuring a Google Cloud project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-account "Chapter 2. Configuring a Google Cloud project")
  * [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installing-mirroring-installation-images)
  * [Configuring your firewall for OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall)
  * [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect)
  * [Installing a cluster on Google Cloud into an existing VPC](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-vpc "Chapter 6. Installing a cluster on Google Cloud into an existing VPC")
