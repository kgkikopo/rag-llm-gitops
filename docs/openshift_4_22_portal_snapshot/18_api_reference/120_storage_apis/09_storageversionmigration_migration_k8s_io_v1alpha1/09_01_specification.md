# 9.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Specification of the migration.   
`status` |  `object` |  Status of the migration.   
Show more

## 9.1.1. .spec

Description
     Specification of the migration. 
Type
     `object`
Required
    

  * `resource`



Property| Type| Description  
---|---|---  
`continueToken` |  `string` |  The token used in the list options to get the next chunk of objects to migrate. When the .status.conditions indicates the migration is "Running", users can use this token to check the progress of the migration.   
`resource` |  `object` |  The resource that is being migrated. The migrator sends requests to the endpoint serving the resource. Immutable.   
Show more

## 9.1.2. .spec.resource

Description
     The resource that is being migrated. The migrator sends requests to the endpoint serving the resource. Immutable. 
Type
     `object`

Property| Type| Description  
---|---|---  
`group` |  `string` |  The name of the group.   
`resource` |  `string` |  The name of the resource.   
`version` |  `string` |  The name of the version.   
Show more

## 9.1.3. .status

Description
     Status of the migration. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  The latest available observations of the migration’s current state.   
`conditions[]` |  `object` |  Describes the state of a migration at a certain point.   
Show more

## 9.1.4. .status.conditions

Description
     The latest available observations of the migration’s current state. 
Type
     `array`

## 9.1.5. .status.conditions[]

Description
     Describes the state of a migration at a certain point. 
Type
     `object`
Required
    

  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastUpdateTime` |  `string` |  The last time this condition was updated.   
`message` |  `string` |  A human readable message indicating details about the transition.   
`reason` |  `string` |  The reason for the condition’s last transition.   
`status` |  `string` |  Status of the condition, one of True, False, Unknown.   
`type` |  `string` |  Type of the condition.   
Show more
