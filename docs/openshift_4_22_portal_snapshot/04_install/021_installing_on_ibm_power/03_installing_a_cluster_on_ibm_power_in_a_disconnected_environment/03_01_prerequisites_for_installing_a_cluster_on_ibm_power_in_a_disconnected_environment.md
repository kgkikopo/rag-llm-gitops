# 3.1. Prerequisites for installing a cluster on IBM Power in a disconnected environment

Before you install a OpenShift Container Platform cluster on IBM Power® in a restricted network, complete the prerequisite tasks to mirror images and prepare your environment. 

  * You reviewed details about the OpenShift Container Platform installation and update processes. 
  * You read the documentation on selecting a cluster installation method and preparing it for users. 
  * You created a mirror registry for installation in a restricted network and obtained the `imageContentSources` data for your version of OpenShift Container Platform. 
  * Before you begin the installation process, you must move or remove any existing installation files. This ensures that the installation program creates and updates the required installation files. 

Important

Perform installation steps on a machine with access to the installation media. 

  * You provisioned persistent storage using OpenShift Data Foundation or other supported storage protocols for your cluster. To deploy a private image registry, you must set up persistent storage with `ReadWriteMany` access. 
  * If you use a firewall and plan to use the Telemetry service, you configured the firewall to allow the sites that your cluster requires access to. 

Note

Be sure to also review this site list if you are configuring a proxy. 




**Additional resources**

  * [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
  * [Selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing)
  * [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installing-mirroring-installation-images)
  * [Persistent storage using OpenShift Data Foundation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-ocs)
  * [Configuring your firewall](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall)
