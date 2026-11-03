# Chapter 2. Converting a connected cluster to a disconnected cluster

You can convert your OpenShift Container Platform cluster from a connected cluster to a disconnected cluster. 

A disconnected cluster, also known as a restricted cluster, does not have an active connection to the internet. As such, you must mirror the contents of your registries and installation media. You can create this mirror registry on a host that can access both the internet and your closed network, or copy images to a device that you can move across network boundaries.

- [2.1. Mirror registry](02_01_mirror_registry.md)
- [2.2. Prerequisites for converting a connected cluster to a disconnected cluster](02_02_prerequisites_for_converting_a_connected_cluster_to_a_disconnected_cluster.md)
- [2.3. Prepare the cluster for mirroring](02_03_prepare_the_cluster_for_mirroring.md)
- [2.4. Mirror the images](02_04_mirror_the_images.md)
- [2.5. Configure the cluster for the mirror registry](02_05_configure_the_cluster_for_the_mirror_registry.md)
- [2.6. Ensure applications continue to work](02_06_ensure_applications_continue_to_work.md)
- [2.7. Disconnect the cluster from the network](02_07_disconnect_the_cluster_from_the_network.md)
- [2.8. Restoring a degraded Insights Operator](02_08_restoring_a_degraded_insights_operator.md)
- [2.9. Restoring the network](02_09_restoring_the_network.md)
