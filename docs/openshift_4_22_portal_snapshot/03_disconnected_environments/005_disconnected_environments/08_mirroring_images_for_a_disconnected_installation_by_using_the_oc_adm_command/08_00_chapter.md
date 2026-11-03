# Chapter 8. Mirroring images for a disconnected installation by using the oc adm command

You can ensure your clusters only use container images that satisfy your organizational controls on external content. Before you install a cluster on infrastructure that you provision in a restricted network, you must mirror the required container images into that environment. 

By using the `oc adm` command, you can mirror release and catalog images in OpenShift. To mirror container images, you must have a registry for mirroring. 

Important

  * The `oc adm release mirror` command is deprecated as of OpenShift Container Platform 4.22 and will be removed in a future release. As an alternative, use the oc-mirror plugin v2. 
  * You must have access to the internet to obtain the necessary container images. In this procedure, you place your mirror registry on a mirror host that has access to both your network and the internet. If you do not have access to a mirror host, use the "Mirroring Operator catalogs for use with disconnected clusters" procedure to copy images to a device you can move across network boundaries with. 



Note

When using the `oc adm release mirror` command, release image signatures are not automatically mirrored to the disconnected registry. Missing release signatures prevent cluster upgrades, as `ClusterImagePolicy` requires all release images to be verified. To ensure image signatures are correctly mirrored, it is recommended to use the oc-mirror v2 plugin.

- [8.1. Prerequisites for mirroring images with the oc adm command](08_01_prerequisites_for_mirroring_images_with_the_oc_adm_command.md)
- [8.2. Mirror registry](08_02_mirror_registry.md)
- [8.3. Preparing your mirror host](08_03_preparing_your_mirror_host.md)
- [8.4. Configure credentials that allow images to be mirrored](08_04_configure_credentials_that_allow_images_to_be_mirrored.md)
- [8.5. Mirror the OpenShift Container Platform image repository](08_05_mirror_the_openshift_container_platform_image_repository.md)
- [8.6. The Cluster Samples Operator in a disconnected environment](08_06_the_cluster_samples_operator_in_a_disconnected_environment.md)
- [8.7. Mirror Operator catalogs for use with disconnected clusters](08_07_mirror_operator_catalogs_for_use_with_disconnected_clusters.md)
- [8.8. Additional resources](08_08_additional_resources.md)
