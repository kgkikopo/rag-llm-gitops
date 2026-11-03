# 4.6. Disconnected environment support in OLM v1

Operator Lifecycle Manager (OLM) v1 supports cluster extension lifecycle management in internet-disconnected environments. This feature helps cluster administrators run mission-critical production workloads in high-security, disconnected clusters. 

## 4.6.1. About disconnected support and the oc-mirror plugin in OLM v1

After you use the oc-mirror plugin for the OpenShift CLI (`oc`) to mirror images to a mirror registry, OLM v1 relies on specific resource sets to function. 

Depending on your oc-mirror plugin version, OLM v1 uses one of the following resource sets: 

oc-mirror plugin v1
     Automatically generates `ImageContentSourcePolicy` resources and requires manually created `ClusterCatalog` resources. 
oc-mirror plugin v2
     Automatically generates `ImageDigestMirrorSet`, `ImageTagMirrorSet`, and `ClusterCatalog` resources. 

Note

The oc-mirror plugin v2 is the recommended version for mirroring. 

**Additional resources**

  * [Mirroring images for a disconnected installation using the oc-mirror plugin v1](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installing-mirroring-disconnected)
  * [Mirroring images for a disconnected installation using the oc-mirror plugin v2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#about-installing-oc-mirror-v2)
