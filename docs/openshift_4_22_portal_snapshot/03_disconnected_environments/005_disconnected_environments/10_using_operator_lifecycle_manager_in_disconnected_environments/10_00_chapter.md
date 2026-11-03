# Chapter 10. Using Operator Lifecycle Manager in disconnected environments

For OpenShift Container Platform clusters in disconnected environments, Operator Lifecycle Manager (OLM) by default cannot access the Red Hat-provided software catalog sources hosted on remote registries because those remote sources require full internet connectivity. 

However, as a cluster administrator you can still enable your cluster to use OLM in a disconnected environment if you have a workstation that has full internet access. The workstation, which requires full internet access to pull the remote software catalog content, is used to prepare local mirrors of the remote sources, and push the content to a mirror registry. 

The mirror registry can be located on a bastion host, which requires connectivity to both your workstation and the disconnected cluster, or a completely disconnected, or _airgapped_ , host, which requires removable media to physically move the mirrored content to the disconnected environment. 

This guide describes the following process that is required to enable OLM in disconnected environments: 

  * Disable the default remote software catalog sources for OLM. 
  * Use a workstation with full internet access to create and push local mirrors of the software catalog content to a mirror registry. 
  * Configure OLM to install and manage Operators from local sources on the mirror registry instead of the default remote sources. 



After enabling OLM in a disconnected environment, you can continue to use your unrestricted workstation to keep your local software catalog sources updated as newer versions of Operators are released. 

Important

While OLM can manage Operators from local sources, the ability for a given Operator to run successfully in a disconnected environment still depends on the Operator itself meeting the following criteria: 

  * List any related images, or other container images that the Operator might require to perform their functions, in the `relatedImages` parameter of its `ClusterServiceVersion` (CSV) object. 
  * Reference all specified images by a digest (SHA) and not by a tag. 



You can search software on the Red Hat Ecosystem Catalog for a list of Red Hat Operators that support running in disconnected mode by filtering with the following selections: 

Type  |  Containerized application   
---|---  
Deployment method  |  Operator   
Infrastructure features  |  Disconnected   
  
For more information, see "Red Hat Ecosystem Catalog". 

**Additional resources**

  * [Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/search?p=1&deployed_as=Operator&type=Containerized%20application&badges_and_features=Disconnected)

- [10.1. Prerequisites](10_01_prerequisites.md)
- [10.2. Disabling the default software catalog sources](10_02_disabling_the_default_software_catalog_sources.md)
- [10.3. Mirror an Operator catalog](10_03_mirror_an_operator_catalog.md)
- [10.4. Add a catalog source to a cluster](10_04_add_a_catalog_source_to_a_cluster.md)
- [10.5. Additional resources](10_05_additional_resources.md)
