# 2.1. Prerequisites for installing a cluster on IBM Power

Before you install a OpenShift Container Platform cluster on IBM Power®, complete the prerequisite tasks to review installation details, provision storage, and configure your firewall. 

  * You reviewed details about the OpenShift Container Platform installation and update processes. 
  * You read the documentation on selecting a cluster installation method and preparing it for users. 
  * Before you begin the installation process, you must clean the installation directory. This ensures that the installation program creates and updates the required installation files. 
  * You provisioned persistent storage using OpenShift Data Foundation or other supported storage providers for your cluster. To deploy a private image registry, you must set up persistent storage with `ReadWriteMany` access. 
  * If you use a firewall, you configured it to allow the sites that your cluster requires access to. 

Note

Be sure to also review this site list if you are configuring a proxy. 




**Additional resources**

  * [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
  * [Selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing)
  * [Persistent storage using OpenShift Data Foundation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-ocs)
  * [Configuring your firewall](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall)
