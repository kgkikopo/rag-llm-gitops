# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ProjectSpec describes the attributes on a Project   
`status` |  `object` |  ProjectStatus is information about the current status of a Project   
Show more

## 2.1.1. .spec

Description
     ProjectSpec describes the attributes on a Project 
Type
     `object`

Property| Type| Description  
---|---|---  
`finalizers` |  `array (string)` |  finalizers is an opaque list of values that must be empty to permanently remove object from storage   
Show more

## 2.1.2. .status

Description
     ProjectStatus is information about the current status of a Project 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  [`array (NamespaceCondition)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-NamespaceCondition) |  Represents the latest available observations of the project current state.   
`phase` |  `string` |  phase is the current lifecycle phase of the project  Possible enum values: - `"Active"` means the namespace is available for use in the system - `"Terminating"` means the namespace is undergoing graceful termination   
Show more
