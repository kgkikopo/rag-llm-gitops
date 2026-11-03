# 1.47. com.github.operator-framework.operator-lifecycle-manager.pkg.package-server.apis.operators.v1.PackageManifestList schema

Description
     PackageManifestList is a list of PackageManifest objects. 
Type
     `object`
Required
    

  * `items`



## 1.47.1. Schema

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`items` |  [`array (PackageManifest)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#packagemanifest-packages-operators-coreos-com-v1) |   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ListMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") |   
Show more
