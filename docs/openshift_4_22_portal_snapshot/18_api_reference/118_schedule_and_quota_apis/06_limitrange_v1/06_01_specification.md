# 6.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  LimitRangeSpec defines a min/max usage limit for resources that match on kind.   
Show more

## 6.1.1. .spec

Description
     LimitRangeSpec defines a min/max usage limit for resources that match on kind. 
Type
     `object`
Required
    

  * `limits`



Property| Type| Description  
---|---|---  
`limits` |  `array` |  Limits is the list of LimitRangeItem objects that are enforced.   
`limits[]` |  `object` |  LimitRangeItem defines a min/max usage limit for any resource that matches on kind.   
Show more

## 6.1.2. .spec.limits

Description
     Limits is the list of LimitRangeItem objects that are enforced. 
Type
     `array`

## 6.1.3. .spec.limits[]

Description
     LimitRangeItem defines a min/max usage limit for any resource that matches on kind. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`default` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  Default resource requirement limit value by resource name if resource limit is omitted.   
`defaultRequest` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  DefaultRequest is the default resource requirement request value by resource name if resource request is omitted.   
`max` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  Max usage constraints on this kind by resource name.   
`maxLimitRequestRatio` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  MaxLimitRequestRatio if specified, the named resource must have a request and limit that are both non-zero where limit divided by request is less than or equal to the enumerated value; this represents the max burst for the named resource.   
`min` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  Min usage constraints on this kind by resource name.   
`type` |  `string` |  Type of resource that this limit applies to.   
Show more
