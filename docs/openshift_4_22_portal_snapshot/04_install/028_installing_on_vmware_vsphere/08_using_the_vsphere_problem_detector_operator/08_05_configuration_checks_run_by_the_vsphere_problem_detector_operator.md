# 8.5. Configuration checks run by the vSphere Problem Detector Operator

The following tables identify the configuration checks that the vSphere Problem Detector Operator runs. Some checks verify the configuration of the cluster. Other checks verify the configuration of each node in the cluster. 

Table 8.1. Cluster configuration checksName| Description  
---|---  
`CheckDefaultDatastore` |  Verifies that the default datastore name in the VMware vSphere configuration is short enough for use with dynamic provisioning.  If this check fails, you can expect the following: 

  * `systemd` logs errors to the journal such as `Failed to set up mount unit: Invalid argument`. 
  * `systemd` does not unmount volumes if the virtual machine shuts down or reboots without draining all the pods from the node. 

If this check fails, reconfigure vSphere with a shorter name for the default datastore.   
`CheckFolderPermissions` |  Verifies the permission to list volumes in the default datastore. You must enable the permission to create volumes. The Operator verifies the permission by listing the `/` and `/kubevols` directories. When the Operator performs the check, the root directory must exist. The `/kubevols` directory might not exist at the time of the check. The creation of the `/kubevols` directory occurs when the datastore supports dynamic provisioning.  If this check fails, review the required permissions for the vCenter account that you specified during the OpenShift Container Platform installation.   
`CheckStorageClasses` |  Verifies the following: 

  * The fully qualified path to each persistent volume that the storage class provisions does not go lower than 255 characters. 
  * The storage class can use only one storage policy and the policy must be defined. 

  
`CheckTaskPermissions` |  Verifies the permission to list recent tasks and datastores.   
`ClusterInfo` |  Collects the cluster version and UUID from vSphere vCenter.   
Show more

Table 8.2. Node configuration checksName| Description  
---|---  
`CheckNodeDiskUUID` |  Verifies that all the vSphere virtual machines include the `disk.enableUUID=TRUE` configuration.  If this check fails, see the [How to check `disk.EnableUUID` parameter from VM in vSphere](https://access.redhat.com/solutions/4606201) Red Hat Knowledgebase solution.   
`CheckNodeProviderID` |  Verifies that all nodes have the `ProviderID` configuration from vSphere vCenter. This check fails when the output from the following command does not include a provider ID for each node.  `$ oc get nodes -o custom-columns=NAME:.metadata.name,PROVIDER_ID:.spec.providerID,UUID:.status.nodeInfo.systemUUID` If this check fails, reference the vSphere product documentation on how to set the provider ID for each node in the cluster.   
`CollectNodeESXiVersion` |  Reports the version of the ESXi hosts that run nodes.   
`CollectNodeHWVersion` |  Reports the virtual machine hardware version for a node.   
Show more
