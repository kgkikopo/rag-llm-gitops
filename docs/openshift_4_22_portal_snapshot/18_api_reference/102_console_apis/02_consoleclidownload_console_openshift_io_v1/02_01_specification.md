# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ConsoleCLIDownloadSpec is the desired cli download configuration.   
Show more

## 2.1.1. .spec

Description
     ConsoleCLIDownloadSpec is the desired cli download configuration. 
Type
     `object`
Required
    

  * `description`
  * `displayName`
  * `links`



Property| Type| Description  
---|---|---  
`description` |  `string` |  description is the description of the CLI download (can include markdown).   
`displayName` |  `string` |  displayName is the display name of the CLI download.   
`links` |  `array` |  links is a list of objects that provide CLI download link details.   
`links[]` |  `object` |   
Show more

## 2.1.2. .spec.links

Description
     links is a list of objects that provide CLI download link details. 
Type
     `array`

## 2.1.3. .spec.links[]

Description
    
Type
     `object`
Required
    

  * `href`



Property| Type| Description  
---|---|---  
`href` |  `string` |  href is the absolute secure URL for the link (must use https)   
`text` |  `string` |  text is the display text for the link   
Show more
