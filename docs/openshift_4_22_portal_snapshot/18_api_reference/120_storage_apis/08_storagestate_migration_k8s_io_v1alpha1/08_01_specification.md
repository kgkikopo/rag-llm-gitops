# 8.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Specification of the storage state.   
`status` |  `object` |  Status of the storage state.   
Show more

## 8.1.1. .spec

Description
     Specification of the storage state. 
Type
     `object`

Property| Type| Description  
---|---|---  
`resource` |  `object` |  The resource this storageState is about.   
Show more

## 8.1.2. .spec.resource

Description
     The resource this storageState is about. 
Type
     `object`

Property| Type| Description  
---|---|---  
`group` |  `string` |  The name of the group.   
`resource` |  `string` |  The name of the resource.   
Show more

## 8.1.3. .status

Description
     Status of the storage state. 
Type
     `object`

Property| Type| Description  
---|---|---  
`currentStorageVersionHash` |  `string` |  The hash value of the current storage version, as shown in the discovery document served by the API server. Storage Version is the version to which objects are converted to before persisted.   
`lastHeartbeatTime` |  `string` |  LastHeartbeatTime is the last time the storage migration triggering controller checks the storage version hash of this resource in the discovery document and updates this field.   
`persistedStorageVersionHashes` |  `array (string)` |  The hash values of storage versions that persisted instances of spec.resource might still be encoded in. "Unknown" is a valid value in the list, and is the default value. It is not safe to upgrade or downgrade to an apiserver binary that does not support all versions listed in this field, or if "Unknown" is listed. Once the storage version migration for this resource has completed, the value of this field is refined to only contain the currentStorageVersionHash. Once the apiserver has changed the storage version, the new storage version is appended to the list.   
Show more
