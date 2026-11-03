# 9.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  TokenRequestSpec contains client provided parameters of a token request.   
`status` |  `object` |  TokenRequestStatus is the result of a token request.   
Show more

## 9.1.1. .spec

Description
     TokenRequestSpec contains client provided parameters of a token request. 
Type
     `object`
Required
    

  * `audiences`



Property| Type| Description  
---|---|---  
`audiences` |  `array (string)` |  Audiences are the intendend audiences of the token. A recipient of a token must identify themself with an identifier in the list of audiences of the token, and otherwise should reject the token. A token issued for multiple audiences may be used to authenticate against any of the audiences listed but implies a high degree of trust between the target audiences.   
`boundObjectRef` |  `object` |  BoundObjectReference is a reference to an object that a token is bound to.   
`expirationSeconds` |  `integer` |  ExpirationSeconds is the requested duration of validity of the request. The token issuer may return a token with a different validity duration so a client needs to check the 'expiration' field in a response.   
Show more

## 9.1.2. .spec.boundObjectRef

Description
     BoundObjectReference is a reference to an object that a token is bound to. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`kind` |  `string` |  Kind of the referent. Valid kinds are 'Pod' and 'Secret'.   
`name` |  `string` |  Name of the referent.   
`uid` |  `string` |  UID of the referent.   
Show more

## 9.1.3. .status

Description
     TokenRequestStatus is the result of a token request. 
Type
     `object`
Required
    

  * `token`
  * `expirationTimestamp`



Property| Type| Description  
---|---|---  
`expirationTimestamp` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  ExpirationTimestamp is the time of expiration of the returned token.   
`token` |  `string` |  Token is the opaque bearer token.   
Show more
