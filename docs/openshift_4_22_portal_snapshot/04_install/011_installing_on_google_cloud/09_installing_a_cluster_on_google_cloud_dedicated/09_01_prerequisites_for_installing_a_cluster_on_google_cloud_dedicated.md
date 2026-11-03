# 9.1. Prerequisites for installing a cluster on Google Cloud Dedicated

Installing OpenShift Container Platform on GCD requires a configured project with domain-scoped IDs, Workforce Identity Federation credentials, and network access to sovereign cloud API endpoints. 

  * You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes. 
  * You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing). 
  * You [configured a Google Cloud project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-account "Chapter 2. Configuring a Google Cloud project") to host the cluster. 
  * You have a credential file for a GCD service account that includes the `universe_domain` field for your sovereign cloud region. 
  * If you use a firewall, you [configured access to the sites](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall) that your cluster requires, including the GCD API endpoints for your region.
