# 4.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  PodSecurityPolicyReviewSpec defines specification for PodSecurityPolicyReview   
`status` |  `object` |  PodSecurityPolicyReviewStatus represents the status of PodSecurityPolicyReview.   
Show more

## 4.1.1. .spec

Description
     PodSecurityPolicyReviewSpec defines specification for PodSecurityPolicyReview 
Type
     `object`
Required
    

  * `template`



Property| Type| Description  
---|---|---  
`serviceAccountNames` |  `array (string)` |  serviceAccountNames is an optional set of ServiceAccounts to run the check with. If serviceAccountNames is empty, the template.spec.serviceAccountName is used, unless it’s empty, in which case "default" is used instead. If serviceAccountNames is specified, template.spec.serviceAccountName is ignored.   
`template` |  [`PodTemplateSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodTemplateSpec) |  template is the PodTemplateSpec to check. The template.spec.serviceAccountName field is used if serviceAccountNames is empty, unless the template.spec.serviceAccountName is empty, in which case "default" is used. If serviceAccountNames is specified, template.spec.serviceAccountName is ignored.   
Show more

## 4.1.2. .status

Description
     PodSecurityPolicyReviewStatus represents the status of PodSecurityPolicyReview. 
Type
     `object`

Property| Type| Description  
---|---|---  
`allowedServiceAccounts` |  `array` |  allowedServiceAccounts returns the list of service accounts in **this** namespace that have the power to create the PodTemplateSpec.   
`allowedServiceAccounts[]` |  `object` |  ServiceAccountPodSecurityPolicyReviewStatus represents ServiceAccount name and related review status   
Show more

## 4.1.3. .status.allowedServiceAccounts

Description
     allowedServiceAccounts returns the list of service accounts in **this** namespace that have the power to create the PodTemplateSpec. 
Type
     `array`

## 4.1.4. .status.allowedServiceAccounts[]

Description
     ServiceAccountPodSecurityPolicyReviewStatus represents ServiceAccount name and related review status 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`allowedBy` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  allowedBy is a reference to the rule that allows the PodTemplateSpec. A rule can be a SecurityContextConstraint or a PodSecurityPolicy A `nil`, indicates that it was denied.   
`name` |  `string` |  name contains the allowed and the denied ServiceAccount name   
`reason` |  `string` |  A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available.   
`template` |  [`PodTemplateSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodTemplateSpec) |  template is the PodTemplateSpec after the defaulting is applied.   
Show more
