# 2.1. Mirror registry

You must have access to the internet to obtain the necessary container images. Using an alternative registry means that you place the mirror registry on a mirror host that has access to both your network and the internet. 

You can mirror the images that are required for OpenShift Container Platform installation and subsequent product updates to a container mirror registry such as Red Hat Quay, JFrog Artifactory, Sonatype Nexus Repository, or Harbor. If you do not have access to a large-scale container registry, you can use the _mirror registry for Red Hat OpenShift_ , a small-scale container registry included with OpenShift Container Platform subscriptions. 

You can use any container registry that supports Docker v2-2, such as Red Hat Quay, the _mirror registry for Red Hat OpenShift_ , Artifactory, Sonatype Nexus Repository, or Harbor. Regardless of your chosen registry, the procedure to mirror content from Red Hat hosted sites on the internet to an isolated image registry is the same. After you mirror the content, you configure each cluster to retrieve this content from your mirror registry. 

Important

The OpenShift image registry cannot be used as the target registry because it does not support pushing without a tag, which is required during the mirroring process. 

If choosing a container registry that is not the _mirror registry for Red Hat OpenShift_ , it must be reachable by every machine in the clusters that you provision. If the registry is unreachable, installation, updating, or normal operations such as workload relocation might fail. For that reason, you must run mirror registries in a highly available way, and the mirror registries must at least match the production availability of your OpenShift Container Platform clusters. 

When you populate your mirror registry with OpenShift Container Platform images, you can follow two scenarios. If you have a host that can access both the internet and your mirror registry, but not your cluster nodes, you can directly mirror the content from that machine. This process is referred to as _connected mirroring_. If you have no such host, you must mirror the images to a file system and then bring that host or removable media into your restricted environment. This process is referred to as _disconnected mirroring_. 

For mirrored registries, to view the source of pulled images, you must review the `Trying to access` log entry in the CRI-O logs. Other methods to view the image pull source, such as using the `crictl images` command on a node, show the non-mirrored image name, even though the image is pulled from the mirrored location. 

Note

Red Hat does not test third party registries with OpenShift Container Platform.
