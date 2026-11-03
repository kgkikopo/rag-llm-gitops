# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  BrokerTemplateInstanceSpec describes the state of a BrokerTemplateInstance.   
Show more

## 2.1.1. .spec

Description
     BrokerTemplateInstanceSpec describes the state of a BrokerTemplateInstance. 
Type
     `object`
Required
    

  * `templateInstance`
  * `secret`



Property| Type| Description  
---|---|---  
`bindingIDs` |  `array (string)` |  bindingIDs is a list of 'binding_id’s provided during successive bind calls to the template service broker.   
`secret` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  secret is a reference to a Secret object residing in a namespace, containing the necessary template parameters.   
`templateInstance` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  templateInstance is a reference to a TemplateInstance object residing in a namespace.   
Show more
