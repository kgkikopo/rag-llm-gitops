# 6.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  PodSecurityPolicySubjectReviewSpec defines specification for PodSecurityPolicySubjectReview   
`status` |  `object` |  PodSecurityPolicySubjectReviewStatus contains information/status for PodSecurityPolicySubjectReview.   
Show more

## 6.1.1. .spec

Description
     PodSecurityPolicySubjectReviewSpec defines specification for PodSecurityPolicySubjectReview 
Type
     `object`
Required
    

  * `template`



Property| Type| Description  
---|---|---  
`groups` |  `array (string)` |  groups is the groups you’re testing for.   
`template` |  [`PodTemplateSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodTemplateSpec) |  template is the PodTemplateSpec to check. If template.spec.serviceAccountName is empty it will not be defaulted. If its non-empty, it will be checked.   
`user` |  `string` |  user is the user you’re testing for. If you specify "user" but not "group", then is it interpreted as "What if user were not a member of any groups. If user and groups are empty, then the check is performed using **only** the serviceAccountName in the template.   
Show more

## 6.1.2. .status

Description
     PodSecurityPolicySubjectReviewStatus contains information/status for PodSecurityPolicySubjectReview. 
Type
     `object`

Property| Type| Description  
---|---|---  
`allowedBy` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  allowedBy is a reference to the rule that allows the PodTemplateSpec. A rule can be a SecurityContextConstraint or a PodSecurityPolicy A `nil`, indicates that it was denied.   
`reason` |  `string` |  A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available.   
`template` |  [`PodTemplateSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodTemplateSpec) |  template is the PodTemplateSpec after the defaulting is applied.   
Show more
