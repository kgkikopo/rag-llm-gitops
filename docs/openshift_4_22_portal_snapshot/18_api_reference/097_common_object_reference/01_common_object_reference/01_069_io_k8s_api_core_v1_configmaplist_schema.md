# 1.69. io.k8s.api.core.v1.ConfigMapList schema

Description
     ConfigMapList is a resource containing a list of ConfigMap objects. 
Type
     `object`
Required
    

  * `items`



## 1.69.1. Schema

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`items` |  [`array (ConfigMap)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#configmap-v1) |  Items is the list of ConfigMaps.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ListMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") |  More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
Show more
