# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`authorizeToken` |  `string` |  authorizeToken contains the token that authorized this token   
`clientName` |  `string` |  clientName references the client that created this token.   
`expiresIn` |  `integer` |  expiresIn is the seconds from CreationTime before this token expires.   
`inactivityTimeoutSeconds` |  `integer` |  inactivityTimeoutSeconds is the value in seconds, from the CreationTimestamp, after which this token can no longer be used. The value is automatically incremented when the token is used.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`redirectURI` |  `string` |  redirectURI is the redirection associated with the token.   
`refreshToken` |  `string` |  refreshToken is the value by which this token can be renewed. Can be blank.   
`scopes` |  `array (string)` |  scopes is an array of the requested scopes.   
`userName` |  `string` |  userName is the user name associated with this token   
`userUID` |  `string` |  userUID is the unique UID associated with this token   
Show more
