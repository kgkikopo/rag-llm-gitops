# 10.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  TokenReviewSpec is a description of the token authentication request.   
`status` |  `object` |  TokenReviewStatus is the result of the token authentication request.   
Show more

## 10.1.1. .spec

Description
     TokenReviewSpec is a description of the token authentication request. 
Type
     `object`

Property| Type| Description  
---|---|---  
`audiences` |  `array (string)` |  Audiences is a list of the identifiers that the resource server presented with the token identifies as. Audience-aware token authenticators will verify that the token was intended for at least one of the audiences in this list. If no audiences are provided, the audience will default to the audience of the Kubernetes apiserver.   
`token` |  `string` |  Token is the opaque bearer token.   
Show more

## 10.1.2. .status

Description
     TokenReviewStatus is the result of the token authentication request. 
Type
     `object`

Property| Type| Description  
---|---|---  
`audiences` |  `array (string)` |  Audiences are audience identifiers chosen by the authenticator that are compatible with both the TokenReview and token. An identifier is any identifier in the intersection of the TokenReviewSpec audiences and the token’s audiences. A client of the TokenReview API that sets the spec.audiences field should validate that a compatible audience identifier is returned in the status.audiences field to ensure that the TokenReview server is audience aware. If a TokenReview returns an empty status.audience field where status.authenticated is "true", the token is valid against the audience of the Kubernetes API server.   
`authenticated` |  `boolean` |  Authenticated indicates that the token was associated with a known user.   
`error` |  `string` |  Error indicates that the token couldn’t be checked   
`user` |  `object` |  UserInfo holds the information about the user needed to implement the user.Info interface.   
Show more

## 10.1.3. .status.user

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

## 10.1.4. .status.user.extra

Description
     Any additional information provided by the authenticator. 
Type
     `object`
