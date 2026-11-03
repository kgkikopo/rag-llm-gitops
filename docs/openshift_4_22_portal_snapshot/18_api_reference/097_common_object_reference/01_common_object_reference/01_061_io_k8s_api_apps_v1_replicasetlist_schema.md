# 1.61. io.k8s.api.apps.v1.ReplicaSetList schema

Description
     ReplicaSetList is a collection of ReplicaSets. 
Type
     `object`
Required
    

  * `items`



## 1.61.1. Schema

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`items` |  [`array (ReplicaSet)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#replicaset-apps-v1) |  List of ReplicaSets. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ListMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") |  Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
Show more
