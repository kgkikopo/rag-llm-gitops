# 9.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ConsoleYAMLSampleSpec is the desired YAML sample configuration. Samples will appear with their descriptions in a samples sidebar when creating a resources in the web console.   
Show more

## 9.1.1. .spec

Description
     ConsoleYAMLSampleSpec is the desired YAML sample configuration. Samples will appear with their descriptions in a samples sidebar when creating a resources in the web console. 
Type
     `object`
Required
    

  * `description`
  * `targetResource`
  * `title`
  * `yaml`



Property| Type| Description  
---|---|---  
`description` |  `string` |  description of the YAML sample.   
`snippet` |  `boolean` |  snippet indicates that the YAML sample is not the full YAML resource definition, but a fragment that can be inserted into the existing YAML document at the user’s cursor.   
`targetResource` |  `object` |  targetResource contains apiVersion and kind of the resource YAML sample is representating.   
`title` |  `string` |  title of the YAML sample.   
`yaml` |  `string` |  yaml is the YAML sample to display.   
Show more

## 9.1.2. .spec.targetResource

Description
     targetResource contains apiVersion and kind of the resource YAML sample is representating. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
Show more
