# 8.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration   
`status` |  `object` |  status holds observed values from the cluster. They may not be overridden.   
Show more

## 8.1.1. .spec

Description
     spec holds user settable values for configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`authentication` |  `object` |  ConsoleAuthentication defines a list of optional configuration for console authentication.   
Show more

## 8.1.2. .spec.authentication

Description
     ConsoleAuthentication defines a list of optional configuration for console authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`logoutRedirect` |  `string` |  An optional, absolute URL to redirect web browsers to after logging out of the console. If not specified, it will redirect to the default login page. This is required when using an identity provider that supports single sign-on (SSO) such as: - OpenID (Keycloak, Azure) - RequestHeader (GSSAPI, SSPI, SAML) - OAuth (GitHub, GitLab, Google) Logging out of the console will destroy the user’s token. The logoutRedirect provides the user the option to perform single logout (SLO) through the identity provider to destroy their single sign-on session.   
Show more

## 8.1.3. .status

Description
     status holds observed values from the cluster. They may not be overridden. 
Type
     `object`

Property| Type| Description  
---|---|---  
`consoleURL` |  `string` |  The URL for the console. This will be derived from the host for the route that is created for the console.   
Show more
