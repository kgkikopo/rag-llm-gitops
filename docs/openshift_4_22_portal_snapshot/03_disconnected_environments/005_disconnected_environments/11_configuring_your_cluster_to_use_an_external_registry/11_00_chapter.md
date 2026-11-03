# Chapter 11. Configuring your cluster to use an external registry

If your cluster was installed without an external registry, you can configure the cluster to use an external registry as a postinstallation task in order to use a mirroring workflow for your image management. 

Important

This configuration is applicable only to clusters installed using the method described in [Installing a cluster without an external registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#installing-ove). 

When you install a cluster using the method described in "Installing a cluster without an external registry", the cluster relies on images contained in the downloaded ISO for its lifecycle management. However, you might want to configure your cluster to use an external image registry and mirror images to the registry instead. To do this, you must set up an external registry, successfully complete an update using images from the external registry, and finally delete `InternalReleaseImage` custom resource, which maintains an internal image registry in the cluster. 

Important

Configuring your cluster to use an external registry is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

- [11.1. Pre-configuration tasks](11_01_pre_configuration_tasks.md)
- [11.2. Deleting the internal image registry](11_02_deleting_the_internal_image_registry.md)
