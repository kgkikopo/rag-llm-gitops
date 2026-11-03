# 1.89. io.k8s.api.core.v1.PodTemplateSpec schema

Description
     PodTemplateSpec describes the data a pod should have when created from a template 
Type
     `object`

## 1.89.1. Schema

Property| Type| Description  
---|---|---  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta "1.142. io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta schema") |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `PodSpec` |  Specification of the desired behavior of the pod. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>  
Show more
