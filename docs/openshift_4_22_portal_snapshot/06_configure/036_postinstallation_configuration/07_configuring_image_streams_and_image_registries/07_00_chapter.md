# Chapter 7. Configuring image streams and image registries

You can configure image streams, image registries, and pull secrets after installation to control how your cluster accesses, imports, and stores container images. 

You can update the global pull secret for your cluster by either replacing the current pull secret or appending a new pull secret. The procedure is required when users use a separate registry to store images than the registry used during installation. For more information, see "Using image pull secrets". 

For information about images and configuring image streams or image registries, see the following documentation: 

  * Overview of images 
  * Image Registry Operator in OpenShift Container Platform 
  * Configuring image registry settings

- [7.1. Configuring image streams for a disconnected cluster](07_01_configuring_image_streams_for_a_disconnected_cluster.md)
- [7.2. Configuring periodic importing of Cluster Sample Operator image stream tags](07_02_configuring_periodic_importing_of_cluster_sample_operator_image_stream_tags.md)
- [7.3. Additional resources](07_03_additional_resources.md)
