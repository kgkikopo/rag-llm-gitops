# 3.13. Disconnected environment

Telco core clusters are expected to be installed in networks without direct access to the internet. 

New in this release
    

  * Added requirement to use the `oc mirror` plugin v2 for mirroring image signatures in disconnected environments. 



Description
    

Telco core clusters are expected to be installed in networks without direct access to the internet. All container images needed to install, configure, and operate the cluster must be available in a disconnected registry. This includes OpenShift Container Platform images, Day 2 OLM Operator images, and application workload images. The use of a disconnected environment provides multiple benefits, including: 

  * Security - limiting access to the cluster 
  * Curated content - the registry is populated based on curated and approved updates for clusters 



Limits and requirements
    

  * A unique name is required for all custom `CatalogSource` resources. Do not reuse the default catalog names. 



Engineering considerations
    

  * A valid time source must be configured as part of cluster installation. 
  * In OpenShift Container Platform 4.22 and later, pulling OpenShift images from a disconnected mirror registry requires copying the image signatures into that registry during the mirroring process. The `oc adm mirror` command does not mirror signatures and must not be used. Instead, use the `oc mirror` plugin v2 to ensure signatures are properly mirrored. 



**Additional resources**

  * [Mirroring images for a disconnected installation by using the oc-mirror plugin v2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#about-installing-oc-mirror-v2)
  * [About cluster updates in a disconnected environment](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#about-disconnected-updates)
  * [Using sysctl in containers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-containers-sysctls)
