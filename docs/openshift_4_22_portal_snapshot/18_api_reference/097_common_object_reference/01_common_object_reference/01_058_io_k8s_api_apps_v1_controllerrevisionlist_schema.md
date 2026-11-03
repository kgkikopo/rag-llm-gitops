# 1.58. io.k8s.api.apps.v1.ControllerRevisionList schema

Description
     ControllerRevisionList is a resource containing a list of ControllerRevision objects. 
Type
     `object`
Required
    

  * `items`



## 1.58.1. Schema

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`items` |  [`array (ControllerRevision)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#controllerrevision-apps-v1) |  Items is the list of ControllerRevisions   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ListMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") |  More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
Show more
