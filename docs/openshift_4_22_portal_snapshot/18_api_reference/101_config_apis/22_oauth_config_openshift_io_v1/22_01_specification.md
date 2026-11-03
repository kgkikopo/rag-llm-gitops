# 22.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration   
`status` |  `object` |  status holds observed values from the cluster. They may not be overridden.   
Show more

## 22.1.1. .spec

Description
     spec holds user settable values for configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`identityProviders` |  `array` |  identityProviders is an ordered list of ways for a user to identify themselves. When this list is empty, no identities are provisioned for users.   
`identityProviders[]` |  `object` |  IdentityProvider provides identities for users authenticating using credentials   
`templates` |  `object` |  templates allow you to customize pages like the login page.   
`tokenConfig` |  `object` |  tokenConfig contains options for authorization and access tokens   
Show more

## 22.1.2. .spec.identityProviders

Description
     identityProviders is an ordered list of ways for a user to identify themselves. When this list is empty, no identities are provisioned for users. 
Type
     `array`

## 22.1.3. .spec.identityProviders[]

Description
     IdentityProvider provides identities for users authenticating using credentials 
Type
     `object`

Property| Type| Description  
---|---|---  
`basicAuth` |  `object` |  basicAuth contains configuration options for the BasicAuth IdP   
`github` |  `object` |  github enables user authentication using GitHub credentials   
`gitlab` |  `object` |  gitlab enables user authentication using GitLab credentials   
`google` |  `object` |  google enables user authentication using Google credentials   
`htpasswd` |  `object` |  htpasswd enables user authentication using an HTPasswd file to validate credentials   
`keystone` |  `object` |  keystone enables user authentication using keystone password credentials   
`ldap` |  `object` |  ldap enables user authentication using LDAP credentials   
`mappingMethod` |  `string` |  mappingMethod determines how identities from this provider are mapped to users Defaults to "claim"   
`name` |  `string` |  name is used to qualify the identities returned by this provider. - It MUST be unique and not shared by any other identity provider used - It MUST be a valid path segment: name cannot equal "." or ".." or contain "/" or "%" or ":" Ref: <https://godoc.org/github.com/openshift/origin/pkg/user/apis/user/validation#ValidateIdentityProviderName>  
`openID` |  `object` |  openID enables user authentication using OpenID credentials   
`requestHeader` |  `object` |  requestHeader enables user authentication using request header credentials   
`type` |  `string` |  type identifies the identity provider type for this entry.   
Show more

## 22.1.4. .spec.identityProviders[].basicAuth

Description
     basicAuth contains configuration options for the BasicAuth IdP 
Type
     `object`

Property| Type| Description  
---|---|---  
`ca` |  `object` |  ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config.   
`tlsClientCert` |  `object` |  tlsClientCert is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate to present when connecting to the server. The key "tls.crt" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config.   
`tlsClientKey` |  `object` |  tlsClientKey is an optional reference to a secret by name that contains the PEM-encoded TLS private key for the client certificate referenced in tlsClientCert. The key "tls.key" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config.   
`url` |  `string` |  url is the remote URL to connect to   
Show more

## 22.1.5. .spec.identityProviders[].basicAuth.ca

Description
     ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced config map   
Show more

## 22.1.6. .spec.identityProviders[].basicAuth.tlsClientCert

Description
     tlsClientCert is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate to present when connecting to the server. The key "tls.crt" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.7. .spec.identityProviders[].basicAuth.tlsClientKey

Description
     tlsClientKey is an optional reference to a secret by name that contains the PEM-encoded TLS private key for the client certificate referenced in tlsClientCert. The key "tls.key" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.8. .spec.identityProviders[].github

Description
     github enables user authentication using GitHub credentials 
Type
     `object`

Property| Type| Description  
---|---|---  
`ca` |  `object` |  ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. This can only be configured when hostname is set to a non-empty value. The namespace for this config map is openshift-config.   
`clientID` |  `string` |  clientID is the oauth client ID   
`clientSecret` |  `object` |  clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config.   
`hostname` |  `string` |  hostname is the optional domain (e.g. "mycompany.com") for use with a hosted instance of GitHub Enterprise. It must match the GitHub Enterprise settings value configured at /setup/settings#hostname.   
`organizations` |  `array (string)` |  organizations optionally restricts which organizations are allowed to log in   
`teams` |  `array (string)` |  teams optionally restricts which teams are allowed to log in. Format is <org>/<team>.   
Show more

## 22.1.9. .spec.identityProviders[].github.ca

Description
     ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. This can only be configured when hostname is set to a non-empty value. The namespace for this config map is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced config map   
Show more

## 22.1.10. .spec.identityProviders[].github.clientSecret

Description
     clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.11. .spec.identityProviders[].gitlab

Description
     gitlab enables user authentication using GitLab credentials 
Type
     `object`

Property| Type| Description  
---|---|---  
`ca` |  `object` |  ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config.   
`clientID` |  `string` |  clientID is the oauth client ID   
`clientSecret` |  `object` |  clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config.   
`url` |  `string` |  url is the oauth server base URL   
Show more

## 22.1.12. .spec.identityProviders[].gitlab.ca

Description
     ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced config map   
Show more

## 22.1.13. .spec.identityProviders[].gitlab.clientSecret

Description
     clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.14. .spec.identityProviders[].google

Description
     google enables user authentication using Google credentials 
Type
     `object`

Property| Type| Description  
---|---|---  
`clientID` |  `string` |  clientID is the oauth client ID   
`clientSecret` |  `object` |  clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config.   
`hostedDomain` |  `string` |  hostedDomain is the optional Google App domain (e.g. "mycompany.com") to restrict logins to   
Show more

## 22.1.15. .spec.identityProviders[].google.clientSecret

Description
     clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.16. .spec.identityProviders[].htpasswd

Description
     htpasswd enables user authentication using an HTPasswd file to validate credentials 
Type
     `object`

Property| Type| Description  
---|---|---  
`fileData` |  `object` |  fileData is a required reference to a secret by name containing the data to use as the htpasswd file. The key "htpasswd" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. If the specified htpasswd data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config.   
Show more

## 22.1.17. .spec.identityProviders[].htpasswd.fileData

Description
     fileData is a required reference to a secret by name containing the data to use as the htpasswd file. The key "htpasswd" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. If the specified htpasswd data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.18. .spec.identityProviders[].keystone

Description
     keystone enables user authentication using keystone password credentials 
Type
     `object`

Property| Type| Description  
---|---|---  
`ca` |  `object` |  ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config.   
`domainName` |  `string` |  domainName is required for keystone v3   
`tlsClientCert` |  `object` |  tlsClientCert is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate to present when connecting to the server. The key "tls.crt" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config.   
`tlsClientKey` |  `object` |  tlsClientKey is an optional reference to a secret by name that contains the PEM-encoded TLS private key for the client certificate referenced in tlsClientCert. The key "tls.key" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config.   
`url` |  `string` |  url is the remote URL to connect to   
Show more

## 22.1.19. .spec.identityProviders[].keystone.ca

Description
     ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced config map   
Show more

## 22.1.20. .spec.identityProviders[].keystone.tlsClientCert

Description
     tlsClientCert is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate to present when connecting to the server. The key "tls.crt" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.21. .spec.identityProviders[].keystone.tlsClientKey

Description
     tlsClientKey is an optional reference to a secret by name that contains the PEM-encoded TLS private key for the client certificate referenced in tlsClientCert. The key "tls.key" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. If the specified certificate data is not valid, the identity provider is not honored. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.22. .spec.identityProviders[].ldap

Description
     ldap enables user authentication using LDAP credentials 
Type
     `object`

Property| Type| Description  
---|---|---  
`attributes` |  `object` |  attributes maps LDAP attributes to identities   
`bindDN` |  `string` |  bindDN is an optional DN to bind with during the search phase.   
`bindPassword` |  `object` |  bindPassword is an optional reference to a secret by name containing a password to bind with during the search phase. The key "bindPassword" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config.   
`ca` |  `object` |  ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config.   
`insecure` |  `boolean` |  insecure, if true, indicates the connection should not use TLS WARNING: Should not be set to `true` with the URL scheme "ldaps://" as "ldaps://" URLs always attempt to connect using TLS, even when `insecure` is set to `true` When `true`, "ldap://" URLS connect insecurely. When `false`, "ldap://" URLs are upgraded to a TLS connection using StartTLS as specified in <https://tools.ietf.org/html/rfc2830>.   
`url` |  `string` |  url is an RFC 2255 URL which specifies the LDAP search parameters to use. The syntax of the URL is: ldap://host:port/basedn?attribute?scope?filter   
Show more

## 22.1.23. .spec.identityProviders[].ldap.attributes

Description
     attributes maps LDAP attributes to identities 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `array (string)` |  email is the list of attributes whose values should be used as the email address. Optional. If unspecified, no email is set for the identity   
`id` |  `array (string)` |  id is the list of attributes whose values should be used as the user ID. Required. First non-empty attribute is used. At least one attribute is required. If none of the listed attribute have a value, authentication fails. LDAP standard identity attribute is "dn"   
`name` |  `array (string)` |  name is the list of attributes whose values should be used as the display name. Optional. If unspecified, no display name is set for the identity LDAP standard display name attribute is "cn"   
`preferredUsername` |  `array (string)` |  preferredUsername is the list of attributes whose values should be used as the preferred username. LDAP standard login attribute is "uid"   
Show more

## 22.1.24. .spec.identityProviders[].ldap.bindPassword

Description
     bindPassword is an optional reference to a secret by name containing a password to bind with during the search phase. The key "bindPassword" is used to locate the data. If specified and the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.25. .spec.identityProviders[].ldap.ca

Description
     ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced config map   
Show more

## 22.1.26. .spec.identityProviders[].openID

Description
     openID enables user authentication using OpenID credentials 
Type
     `object`

Property| Type| Description  
---|---|---  
`ca` |  `object` |  ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config.   
`claims` |  `object` |  claims mappings   
`clientID` |  `string` |  clientID is the oauth client ID   
`clientSecret` |  `object` |  clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config.   
`extraAuthorizeParameters` |  `object (string)` |  extraAuthorizeParameters are any custom parameters to add to the authorize request.   
`extraScopes` |  `array (string)` |  extraScopes are any scopes to request in addition to the standard "openid" scope.   
`issuer` |  `string` |  issuer is the URL that the OpenID Provider asserts as its Issuer Identifier. It must use the https scheme with no query or fragment component.   
Show more

## 22.1.27. .spec.identityProviders[].openID.ca

Description
     ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca.crt" is used to locate the data. If specified and the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. If empty, the default system roots are used. The namespace for this config map is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced config map   
Show more

## 22.1.28. .spec.identityProviders[].openID.claims

Description
     claims mappings 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `array (string)` |  email is the list of claims whose values should be used as the email address. Optional. If unspecified, no email is set for the identity   
`groups` |  `array (string)` |  groups is the list of claims value of which should be used to synchronize groups from the OIDC provider to OpenShift for the user. If multiple claims are specified, the first one with a non-empty value is used.   
`name` |  `array (string)` |  name is the list of claims whose values should be used as the display name. Optional. If unspecified, no display name is set for the identity   
`preferredUsername` |  `array (string)` |  preferredUsername is the list of claims whose values should be used as the preferred username. If unspecified, the preferred username is determined from the value of the sub claim   
Show more

## 22.1.29. .spec.identityProviders[].openID.clientSecret

Description
     clientSecret is a required reference to the secret by name containing the oauth client secret. The key "clientSecret" is used to locate the data. If the secret or expected key is not found, the identity provider is not honored. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.30. .spec.identityProviders[].requestHeader

Description
     requestHeader enables user authentication using request header credentials 
Type
     `object`

Property| Type| Description  
---|---|---  
`ca` |  `object` |  ca is a required reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. Specifically, it allows verification of incoming requests to prevent header spoofing. The key "ca.crt" is used to locate the data. If the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. The namespace for this config map is openshift-config.   
`challengeURL` |  `string` |  challengeURL is a URL to redirect unauthenticated /authorize requests to Unauthenticated requests from OAuth clients which expect WWW-Authenticate challenges will be redirected here. ${url} is replaced with the current URL, escaped to be safe in a query parameter <https://www.example.com/sso-login?then=${url}> ${query} is replaced with the current query string <https://www.example.com/auth-proxy/oauth/authorize?${query}> Required when challenge is set to true.   
`clientCommonNames` |  `array (string)` |  clientCommonNames is an optional list of common names to require a match from. If empty, any client certificate validated against the clientCA bundle is considered authoritative.   
`emailHeaders` |  `array (string)` |  emailHeaders is the set of headers to check for the email address   
`headers` |  `array (string)` |  headers is the set of headers to check for identity information   
`loginURL` |  `string` |  loginURL is a URL to redirect unauthenticated /authorize requests to Unauthenticated requests from OAuth clients which expect interactive logins will be redirected here ${url} is replaced with the current URL, escaped to be safe in a query parameter <https://www.example.com/sso-login?then=${url}> ${query} is replaced with the current query string <https://www.example.com/auth-proxy/oauth/authorize?${query}> Required when login is set to true.   
`nameHeaders` |  `array (string)` |  nameHeaders is the set of headers to check for the display name   
`preferredUsernameHeaders` |  `array (string)` |  preferredUsernameHeaders is the set of headers to check for the preferred username   
Show more

## 22.1.31. .spec.identityProviders[].requestHeader.ca

Description
     ca is a required reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. Specifically, it allows verification of incoming requests to prevent header spoofing. The key "ca.crt" is used to locate the data. If the config map or expected key is not found, the identity provider is not honored. If the specified ca data is not valid, the identity provider is not honored. The namespace for this config map is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced config map   
Show more

## 22.1.32. .spec.templates

Description
     templates allow you to customize pages like the login page. 
Type
     `object`

Property| Type| Description  
---|---|---  
`error` |  `object` |  error is the name of a secret that specifies a go template to use to render error pages during the authentication or grant flow. The key "errors.html" is used to locate the template data. If specified and the secret or expected key is not found, the default error page is used. If the specified template is not valid, the default error page is used. If unspecified, the default error page is used. The namespace for this secret is openshift-config.   
`login` |  `object` |  login is the name of a secret that specifies a go template to use to render the login page. The key "login.html" is used to locate the template data. If specified and the secret or expected key is not found, the default login page is used. If the specified template is not valid, the default login page is used. If unspecified, the default login page is used. The namespace for this secret is openshift-config.   
`providerSelection` |  `object` |  providerSelection is the name of a secret that specifies a go template to use to render the provider selection page. The key "providers.html" is used to locate the template data. If specified and the secret or expected key is not found, the default provider selection page is used. If the specified template is not valid, the default provider selection page is used. If unspecified, the default provider selection page is used. The namespace for this secret is openshift-config.   
Show more

## 22.1.33. .spec.templates.error

Description
     error is the name of a secret that specifies a go template to use to render error pages during the authentication or grant flow. The key "errors.html" is used to locate the template data. If specified and the secret or expected key is not found, the default error page is used. If the specified template is not valid, the default error page is used. If unspecified, the default error page is used. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.34. .spec.templates.login

Description
     login is the name of a secret that specifies a go template to use to render the login page. The key "login.html" is used to locate the template data. If specified and the secret or expected key is not found, the default login page is used. If the specified template is not valid, the default login page is used. If unspecified, the default login page is used. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.35. .spec.templates.providerSelection

Description
     providerSelection is the name of a secret that specifies a go template to use to render the provider selection page. The key "providers.html" is used to locate the template data. If specified and the secret or expected key is not found, the default provider selection page is used. If the specified template is not valid, the default provider selection page is used. If unspecified, the default provider selection page is used. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 22.1.36. .spec.tokenConfig

Description
     tokenConfig contains options for authorization and access tokens 
Type
     `object`

Property| Type| Description  
---|---|---  
`accessTokenInactivityTimeout` |  `string` |  accessTokenInactivityTimeout defines the token inactivity timeout for tokens granted by any client. The value represents the maximum amount of time that can occur between consecutive uses of the token. Tokens become invalid if they are not used within this temporal window. The user will need to acquire a new token to regain access once a token times out. Takes valid time duration string such as "5m", "1.5h" or "2h45m". The minimum allowed value for duration is 300s (5 minutes). If the timeout is configured per client, then that value takes precedence. If the timeout value is not specified and the client does not override the value, then tokens are valid until their lifetime.  WARNING: existing tokens' timeout will not be affected (lowered) by changing this value   
`accessTokenInactivityTimeoutSeconds` |  `integer` |  accessTokenInactivityTimeoutSeconds - DEPRECATED: setting this field has no effect.   
`accessTokenMaxAgeSeconds` |  `integer` |  accessTokenMaxAgeSeconds defines the maximum age of access tokens   
Show more

## 22.1.37. .status

Description
     status holds observed values from the cluster. They may not be overridden. 
Type
     `object`
