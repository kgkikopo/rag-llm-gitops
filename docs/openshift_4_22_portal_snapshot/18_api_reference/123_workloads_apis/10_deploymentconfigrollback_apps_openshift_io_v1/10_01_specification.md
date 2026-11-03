# 10.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  name of the deployment config that will be rolled back.   
`spec` |  `object` |  DeploymentConfigRollbackSpec represents the options for rollback generation.   
`updatedAnnotations` |  `object (string)` |  updatedAnnotations is a set of new annotations that will be added in the deployment config.   
Show more

## 10.1.1. .spec

Description
     DeploymentConfigRollbackSpec represents the options for rollback generation. 
Type
     `object`
Required
    

  * `from`
  * `includeTriggers`
  * `includeTemplate`
  * `includeReplicationMeta`
  * `includeStrategy`



Property| Type| Description  
---|---|---  
`from` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  from points to a ReplicationController which is a deployment.   
`includeReplicationMeta` |  `boolean` |  includeReplicationMeta specifies whether to include the replica count and selector.   
`includeStrategy` |  `boolean` |  includeStrategy specifies whether to include the deployment Strategy.   
`includeTemplate` |  `boolean` |  includeTemplate specifies whether to include the PodTemplateSpec.   
`includeTriggers` |  `boolean` |  includeTriggers specifies whether to include config Triggers.   
`revision` |  `integer` |  revision to rollback to. If set to 0, rollback to the last revision.   
Show more
