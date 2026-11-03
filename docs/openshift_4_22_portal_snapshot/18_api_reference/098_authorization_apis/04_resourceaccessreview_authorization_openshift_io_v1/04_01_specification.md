# 4.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`content` |  [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) |  content is the actual content of the request for create and update   
`isNonResourceURL` |  `boolean` |  isNonResourceURL is true if this is a request for a non-resource URL (outside of the resource hierarchy)   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`namespace` |  `string` |  namespace is the namespace of the action being requested. Currently, there is no distinction between no namespace and all namespaces   
`path` |  `string` |  path is the path of a non resource URL   
`resource` |  `string` |  resource is one of the existing resource types   
`resourceAPIGroup` |  `string` |  Group is the API group of the resource Serialized as resourceAPIGroup to avoid confusion with the 'groups' field when inlined   
`resourceAPIVersion` |  `string` |  Version is the API version of the resource Serialized as resourceAPIVersion to avoid confusion with TypeMeta.apiVersion and ObjectMeta.resourceVersion when inlined   
`resourceName` |  `string` |  resourceName is the name of the resource being requested for a "get" or deleted for a "delete"   
`verb` |  `string` |  verb is one of: get, list, watch, create, update, delete   
Show more
