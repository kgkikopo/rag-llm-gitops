# 1.149. io.k8s.kube-aggregator.pkg.apis.apiregistration.v1.APIServiceList schema

Description
     APIServiceList is a list of APIService objects. 
Type
     `object`
Required
    

  * `items`



## 1.149.1. Schema

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`items` |  [`array (APIService)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#apiservice-apiregistration-k8s-io-v1) |  Items is the list of APIService   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ListMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") |  Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
Show more
