# 8.1. Resources managed by quota

To limit aggregate resource consumption per project, define a `ResourceQuota` object. By using this object, you can restrict the number of created objects by type. You can also restrict the total amount of compute resources and storage consumed within the project. 

The following tables describe the set of compute resources and object types that a quota might manage. 

Note

A pod is in a terminal state if `status.phase` is `Failed` or `Succeeded`. 

Table 8.1. Compute resources managed by quotaResource Name| Description  
---|---  
`cpu` |  The sum of CPU requests across all pods in a non-terminal state cannot exceed this value. `cpu` and `requests.cpu` are the same value and can be used interchangeably.   
`memory` |  The sum of memory requests across all pods in a non-terminal state cannot exceed this value. `memory` and `requests.memory` are the same value and can be used interchangeably.   
`ephemeral-storage` |  The sum of local ephemeral storage requests across all pods in a non-terminal state cannot exceed this value. `ephemeral-storage` and `requests.ephemeral-storage` are the same value and can be used interchangeably. This resource is available only if you enabled the ephemeral storage technology preview. This feature is disabled by default.   
`requests.cpu` |  The sum of CPU requests across all pods in a non-terminal state cannot exceed this value. `cpu` and `requests.cpu` are the same value and can be used interchangeably.   
`requests.memory` |  The sum of memory requests across all pods in a non-terminal state cannot exceed this value. `memory` and `requests.memory` are the same value and can be used interchangeably.   
`requests.ephemeral-storage` |  The sum of ephemeral storage requests across all pods in a non-terminal state cannot exceed this value. `ephemeral-storage` and `requests.ephemeral-storage` are the same value and can be used interchangeably. This resource is available only if you enabled the ephemeral storage technology preview. This feature is disabled by default.   
`limits.cpu` |  The sum of CPU limits across all pods in a non-terminal state cannot exceed this value.   
`limits.memory` |  The sum of memory limits across all pods in a non-terminal state cannot exceed this value.   
`limits.ephemeral-storage` |  The sum of ephemeral storage limits across all pods in a non-terminal state cannot exceed this value. This resource is available only if you enabled the ephemeral storage technology preview. This feature is disabled by default.   
Show more

Table 8.2. Storage resources managed by quotaResource Name| Description  
---|---  
`requests.storage` |  The sum of storage requests across all persistent volume claims in any state cannot exceed this value.   
`persistentvolumeclaims` |  The total number of persistent volume claims that can exist in the project.   
`<storage-class-name>.storageclass.storage.k8s.io/requests.storage` |  The sum of storage requests across all persistent volume claims in any state that have a matching storage class, cannot exceed this value.   
`<storage-class-name>.storageclass.storage.k8s.io/persistentvolumeclaims` |  The total number of persistent volume claims with a matching storage class that can exist in the project.   
Show more

Table 8.3. Object counts managed by quotaResource Name| Description  
---|---  
`pods` |  The total number of pods in a non-terminal state that can exist in the project.   
`replicationcontrollers` |  The total number of replication controllers that can exist in the project.   
`resourcequotas` |  The total number of resource quotas that can exist in the project.   
`services` |  The total number of services that can exist in the project.   
`secrets` |  The total number of secrets that can exist in the project.   
`configmaps` |  The total number of `ConfigMap` objects that can exist in the project.   
`persistentvolumeclaims` |  The total number of persistent volume claims that can exist in the project.   
`openshift.io/imagestreams` |  The total number of image streams that can exist in the project.   
Show more

You can configure an object count quota for these standard namespaced resource types using the `count/<resource>.<group>` syntax. 

```shell-session
$ oc create quota <name> --hard=count/<resource>.<group>=<quota>
```


where: 

`<resource>`
     Specifies the name of the resource. 
`<group>`
     Specifies the API group, if applicable. You can use the `kubectl api-resources` command for a list of resources and their associated API groups.
