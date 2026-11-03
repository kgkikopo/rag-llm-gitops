# 8.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`status` |  `object` |  SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user.   
Show more

## 8.1.1. .status

Description
     SelfSubjectReviewStatus is filled by the kube-apiserver and sent back to a user. 
Type
     `object`

Property| Type| Description  
---|---|---  
`userInfo` |  `object` |  UserInfo holds the information about the user needed to implement the user.Info interface.   
Show more

## 8.1.2. .status.userInfo

Description
     UserInfo holds the information about the user needed to implement the user.Info interface. 
Type
     `object`

Property| Type| Description  
---|---|---  
`extra` |  `object` |  Any additional information provided by the authenticator.   
`extra{}` |  `array (string)` |   
`groups` |  `array (string)` |  The names of groups this user is a part of.   
`uid` |  `string` |  A unique value that identifies this user across time. If this user is deleted and another user by the same name is added, they will have different UIDs.   
`username` |  `string` |  The name that uniquely identifies this user among all active users.   
Show more

## 8.1.3. .status.userInfo.extra

Description
     Any additional information provided by the authenticator. 
Type
     `object`
