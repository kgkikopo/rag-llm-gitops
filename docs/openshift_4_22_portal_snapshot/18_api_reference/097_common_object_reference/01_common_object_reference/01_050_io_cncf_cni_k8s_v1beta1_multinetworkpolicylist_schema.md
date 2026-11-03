# 1.50. io.cncf.cni.k8s.v1beta1.MultiNetworkPolicyList schema

Description
     MultiNetworkPolicyList is a list of MultiNetworkPolicy 
Type
     `object`
Required
    

  * `items`



## 1.50.1. Schema

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`items` |  [`array (MultiNetworkPolicy)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#multinetworkpolicy-k8s-cni-cncf-io-v1beta1) |  List of multi-networkpolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ListMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") |  Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
Show more
