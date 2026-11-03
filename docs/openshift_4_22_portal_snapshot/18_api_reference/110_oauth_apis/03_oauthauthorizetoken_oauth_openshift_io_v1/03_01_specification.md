# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`clientName` |  `string` |  clientName references the client that created this token.   
`codeChallenge` |  `string` |  codeChallenge is the optional code_challenge associated with this authorization code, as described in rfc7636   
`codeChallengeMethod` |  `string` |  codeChallengeMethod is the optional code_challenge_method associated with this authorization code, as described in rfc7636   
`expiresIn` |  `integer` |  expiresIn is the seconds from CreationTime before this token expires.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`redirectURI` |  `string` |  redirectURI is the redirection associated with the token.   
`scopes` |  `array (string)` |  scopes is an array of the requested scopes.   
`state` |  `string` |  state data from request   
`userName` |  `string` |  userName is the user name associated with this token   
`userUID` |  `string` |  userUID is the unique UID associated with this token. UserUID and UserName must both match for this token to be valid.   
Show more
