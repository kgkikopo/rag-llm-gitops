# 10.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Metal3RemediationSpec defines the desired state of Metal3Remediation.   
`status` |  `object` |  Metal3RemediationStatus defines the observed state of Metal3Remediation.   
Show more

## 10.1.1. .spec

Description
     Metal3RemediationSpec defines the desired state of Metal3Remediation. 
Type
     `object`

Property| Type| Description  
---|---|---  
`strategy` |  `object` |  Strategy field defines remediation strategy.   
Show more

## 10.1.2. .spec.strategy

Description
     Strategy field defines remediation strategy. 
Type
     `object`

Property| Type| Description  
---|---|---  
`retryLimit` |  `integer` |  Sets maximum number of remediation retries.   
`timeout` |  `string` |  Sets the timeout between remediation retries.   
`type` |  `string` |  Type of remediation.   
Show more

## 10.1.3. .status

Description
     Metal3RemediationStatus defines the observed state of Metal3Remediation. 
Type
     `object`

Property| Type| Description  
---|---|---  
`lastRemediated` |  `string` |  LastRemediated identifies when the host was last remediated   
`phase` |  `string` |  Phase represents the current phase of machine remediation. E.g. Pending, Running, Done etc.   
`retryCount` |  `integer` |  RetryCount can be used as a counter during the remediation. Field can hold number of reboots etc.   
Show more
