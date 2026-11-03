# 8.9. Manually updating the boot image on a platform none or external cluster

For `platform: None` and `platform: External` clusters, you can manually update the boot image for your cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to help ensure any new nodes can scale up properly. 

For these clusters, OpenShift Container Platform does not manage node provisioning or Red Hat Enterprise Linux CoreOS (RHCOS) boot images. These clusters do not use Machine API machine sets. 

Note

The standard boot image management feature is not supported for `platform: None` or `platform: External` clusters. 

The method for updating boot images depends on how nodes are added to your cluster as a day-2 operation. 

Method| Description  
---|---  
User-provisioned infrastructure clusters  |  Nodes are provisioned manually by a user-managed infrastructure.   
Red Hat Advanced Cluster Management (RHACM)-managed clusters  |  Nodes are added by using a discovery ISO managed by an `InfraEnv` object on the hub cluster.   
External provider clusters  |  Nodes are provisioned by using provider-specific tooling with a user-uploaded RHCOS image.   
Show more

User-provisioned infrastructure
    

For user-provisioned infrastructure clusters, you manage boot images as part of your infrastructure. To update the boot image, download the latest RHCOS image for your architecture from [mirror.openshift.com](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/) and update your infrastructure to serve the new image. 

For the full procedure, see the section for your platform in "Adding compute machines to clusters with user-provisioned infrastructure manually". 

RHACM-managed clusters
     For clusters managed by RHACM, the boot image used to generate the discovery ISO image is controlled by the `spec.osImageVersion` parameter in the `InfraEnv` object on the hub cluster. After an OpenShift Container Platform upgrade, you need to update the existing `InfraEnv` object to add or update `spec.osImageVersion` field, specifying the OpenShift Container Platform version of the new boot image. 
External provider clusters
     For clusters managed by an external infrastructure provider, such as Oracle Cloud Infrastructure (OCI), you must upload the new boot image to the provider’s image store and update your node provisioning configuration to reference the new image when creating new nodes. The exact steps are provider-specific. 

If boot image skew enforcement in your cluster is set to the manual mode, after updating the boot image, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".
