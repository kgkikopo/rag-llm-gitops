# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ConsoleNotificationSpec is the desired console notification configuration.   
Show more

## 5.1.1. .spec

Description
     ConsoleNotificationSpec is the desired console notification configuration. 
Type
     `object`
Required
    

  * `text`



Property| Type| Description  
---|---|---  
`backgroundColor` |  `string` |  backgroundColor is the color of the background for the notification as CSS data type color.   
`color` |  `string` |  color is the color of the text for the notification as CSS data type color.   
`link` |  `object` |  link is an object that holds notification link details.   
`location` |  `string` |  location is the location of the notification in the console. Valid values are: "BannerTop", "BannerBottom", "BannerTopBottom".   
`text` |  `string` |  text is the visible text of the notification.   
Show more

## 5.1.2. .spec.link

Description
     link is an object that holds notification link details. 
Type
     `object`
Required
    

  * `href`
  * `text`



Property| Type| Description  
---|---|---  
`href` |  `string` |  href is the absolute URL for the link. Must use https:// for web URLs or mailto: for email links.   
`text` |  `string` |  text is the display text for the link   
Show more
