# 1.3. Choosing a method to install OpenShift Container Platform on Google Cloud

You can install OpenShift Container Platform on installer-provisioned or user-provisioned infrastructure. The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster. You can also install OpenShift Container Platform on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself. For more information about installer-provisioned and user-provisioned installation processes, see "Installation process". 

## 1.3.1. Installer-provisioned infrastructure installation methods

You can choose from several methods to install a cluster on Google Cloud by using installer-provisioned infrastructure, depending on your network requirements and environment constraints. 

You can install a cluster on Google Cloud infrastructure that is provisioned by the OpenShift Container Platform installation program, by using one of the following methods: 

  * **[Installing a cluster quickly on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-default "Chapter 3. Installing a cluster quickly on Google Cloud")** : You can install OpenShift Container Platform on Google Cloud infrastructure that is provisioned by the OpenShift Container Platform installation program. You can install a cluster quickly by using the default configuration options. 
  * **[Installing a customized cluster on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-customizations "Chapter 4. Installing a cluster on Google Cloud with customizations")** : You can install a customized cluster on Google Cloud infrastructure that the installation program provisions. You can customize your OpenShift Container Platform network configuration during installation, so that your cluster can coexist with your existing IP address allocations and adhere to your network requirements. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available postinstallation. 
  * **[Installing a cluster on Google Cloud in a restricted network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-restricted-networks-gcp-installer-provisioned "Chapter 5. Installing a cluster on Google Cloud in a disconnected environment")** : You can install OpenShift Container Platform on installer-provisioned infrastructure in Google Cloud by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. While you can install OpenShift Container Platform by using the mirrored content, your cluster still requires internet access to use the Google Cloud APIs. 
  * **[Installing a cluster into an existing Virtual Private Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-vpc "Chapter 6. Installing a cluster on Google Cloud into an existing VPC")** : You can install OpenShift Container Platform on an existing Google Cloud Virtual Private Cloud (VPC). You can use this installation method if you have constraints set by the guidelines of your company, such as limits on creating new accounts or infrastructure. 
  * **[Installing a private cluster on an existing VPC](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-private "Chapter 8. Installing a private cluster on Google Cloud")** : You can install a private cluster on an existing Google Cloud VPC. You can use this method to deploy OpenShift Container Platform on an internal network that is not visible to the internet. 



**Additional resources**

  * [Postinstallation configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#post-install-cluster-tasks)



## 1.3.2. User-provisioned infrastructure installation methods

You can choose from several methods to install a cluster on Google Cloud by using infrastructure that you provision, depending on your network requirements and environment constraints. 

You can install a cluster on Google Cloud infrastructure that you provision, by using one of the following methods: 

  * **[Installing a cluster on Google Cloud with user-provisioned infrastructure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-user-infra "Chapter 10. Installing a cluster on user-provisioned infrastructure in Google Cloud by using Infrastructure Manager templates")** : You can install OpenShift Container Platform on Google Cloud infrastructure that you provide. You can use the provided Infrastructure Manager templates to assist with the installation. 
  * **[Installing a cluster with shared VPC on user-provisioned infrastructure in Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-user-infra-vpc "Chapter 11. Installing a cluster into a shared VPC on Google Cloud using Infrastructure Manager templates")** : You can use the provided Infrastructure Manager templates to create Google Cloud resources in a shared VPC infrastructure. 
  * **[Installing a cluster on Google Cloud in a restricted network with user-provisioned infrastructure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-restricted-networks-gcp "Chapter 12. Installing a cluster on Google Cloud in a disconnected environment with user-provisioned infrastructure")** : You can install OpenShift Container Platform on Google Cloud in a restricted network with user-provisioned infrastructure. By creating an internal mirror of the installation release content, you can install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content. 



**Additional resources**

  * [Installation process](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#installation-process_architecture-installation)
