# 9.6. Advanced authentication field reference

The following table describes the advanced authentication configuration fields available as Technology Preview in OpenShift Container Platform. 

Table 9.1. Advanced oidcProviders configuration fieldsParameter| Description  
---|---  
`issuer.discoveryURL` |  Optional parameter. Custom OIDC discovery endpoint URL for retrieving identity provider metadata from a non-standard location.  Requirements: 

  * Must be a valid HTTPS URL 
  * Must differ from `issuer.issuerURL`

When not specified, OpenShift Container Platform constructs the discovery URL by using the standard OIDC format: `{issuerURL}/.well-known/openid-configuration`.  **Example:** `issuer: issuerURL: https://idp.example.com discoveryURL: https://custom-discovery.example.com/.well-known/openid-configuration`  
`claimValidationRules` |  Optional parameter. Array of validation rules for JWT token claims using Common Expression Language (CEL) expressions. All rules must evaluate to `true` for authentication to succeed (AND operation).  Each rule has: 

  * `type`: Set to `CEL` for CEL-based validation 
  * `cel`: Object with `expression` (must evaluate to `true`) and `message` (error text) 

CEL expressions access claims by using `claims` variable (for example, `claims.sub`).  **Example:** `claimValidationRules: - type: CEL cel: expression: 'claims.exp - claims.nbf <= 86400' message: 'Total token lifetime must not exceed 24 hours' - type: CEL cel: expression: 'has(claims.email) && claims.email.contains("@example.com")' message: 'Email claim must be present and from example.com domain'`  
`claimValidationRules[].type` |  Required. Validation rule type. Set to `CEL` for CEL-based validation. Requires `cel` field.   
`claimValidationRules[].cel` |  Required when `type` is `CEL`. Contains `expression` (CEL expression to evaluate) and `message` (error text).   
`claimValidationRules[].cel.expression` |  Required. CEL expression that validates token claims. Must evaluate to `true` for authentication to succeed.  Constraints: 1-1024 characters, must evaluate to boolean.  Access claims by using `claims` variable: `claims.sub`, `claims.foo.bar` (nested), `has(claims.email)` (existence check).  Note When using the `email` claim in CEL expressions, you must also validate the `email_verified` claim to ensure the email address has been verified by the identity provider. For example: `claims.email_verified && claims.email.endsWith("@example.com")`.   
`claimValidationRules[].cel.message` |  Required. Error message displayed when validation fails. Constraints: 1-256 characters.   
`userValidationRules` |  Optional parameter. Array of validation rules for user objects by using CEL expressions. All rules must evaluate to `true` for authentication to succeed (AND operation).  Each rule has `expression` (must evaluate to `true`) and `message` (error text).  CEL expressions access user object by using `user` variable: `user.username` (string), `user.groups` (array), `user.uid` (string), `user.extra` (map).  **Example:** `userValidationRules: - expression: "!user.username.startsWith('system:')" message: 'Username cannot use reserved system: prefix' - expression: "!user.groups.exists(g, g.startsWith('system:'))" message: 'Groups cannot use reserved system: prefix'`  
`userValidationRules[].expression` |  Required. CEL expression that validates the user object. Must evaluate to `true` for authentication to succeed.  Constraints: 1-1024 characters, must evaluate to boolean.  Access user fields: `user.username.startsWith('system:')`, `user.groups.exists(g, g == "admin")`, `user.extra["example.com/role"]`.   
`userValidationRules[].message` |  Required. Error message displayed when validation fails. Must not be empty.   
Show more

**Additional resources**

  * [Enabling direct authentication with an external OIDC identity provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/external-auth "Chapter 8. Enabling direct authentication with an external OIDC identity provider")
  * [Common Expression Language (CEL) specification](https://cel.dev/)
  * [Common Expression Language in Kubernetes](https://kubernetes.io/docs/reference/using-api/cel/)
