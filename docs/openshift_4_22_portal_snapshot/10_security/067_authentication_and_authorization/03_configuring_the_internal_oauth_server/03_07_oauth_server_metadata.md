# 3.7. OAuth server metadata

Applications running in the cluster can query the OAuth 2.0 Authorization Server Metadata endpoint to dynamically discover OAuth server endpoints, supported scopes, and grant types for automated client configuration. 

Any application running inside the cluster can issue a `GET` request to **_https://openshift.default.svc/.well-known/oauth-authorization-server_** to fetch the following information: 

```plaintext
{
  "issuer": "https://<namespace_route>",
  "authorization_endpoint": "https://<namespace_route>/oauth/authorize",
  "token_endpoint": "https://<namespace_route>/oauth/token",
  "scopes_supported": [
    "user:full",
    "user:info",
    "user:check-access",
    "user:list-scoped-projects",
    "user:list-projects"
  ],
  "response_types_supported": [
    "code",
    "token"
  ],
  "grant_types_supported": [
    "authorization_code",
    "implicit"
  ],
  "code_challenge_methods_supported": [
    "plain",
    "S256"
  ]
}
```


\+ where: 

`issuer`
     Specifies the authorization server’s issuer identifier, which is a URL that uses the `https` scheme and has no query or fragment components. This is the location where `.well-known` RFC 5785 resources containing information about the authorization server are published. 
`authorization_endpoint`
     Specifies the URL of the authorization server’s authorization endpoint. 
`token_endpoint`
     Specifies the URL of the authorization server’s token endpoint. 
`scopes_supported`
     Specifies a JSON array containing a list of the OAuth 2.0 RFC 6749 scope values that this authorization server supports. Note that not all supported scope values are advertised. 
`response_types_supported`
     Specifies a JSON array containing a list of the OAuth 2.0 `response_type` values that this authorization server supports. The array values used are the same as those used with the `response_types` parameter defined by OAuth 2.0 Dynamic Client Registration Protocol in RFC 7591. 
`grant_types_supported`
     Specifies a JSON array containing a list of the OAuth 2.0 grant type values that this authorization server supports. The array values used are the same as those used with the `grant_types` parameter defined by OAuth 2.0 Dynamic Client Registration Protocol in RFC 7591. 
`code_challenge_methods_supported`
     Specifies a JSON array containing a list of PKCE RFC 7636 code challenge methods supported by this authorization server. Code challenge method values are used in the `code_challenge_method` parameter defined in Section 4.3 of RFC 7636. The valid code challenge method values are those registered in the IANA PKCE Code Challenge Methods registry. 

**Additional resources**

  * [OAuth 2.0 Authorization Server Metadata](https://tools.ietf.org/html/draft-ietf-oauth-discovery-10)
  * [RFC 5785 - Defining Well-Known Uniform Resource Identifiers](https://tools.ietf.org/html/rfc5785)
  * [RFC 6749 - The OAuth 2.0 Authorization Framework](https://tools.ietf.org/html/rfc6749)
  * [RFC 7591 - OAuth 2.0 Dynamic Client Registration Protocol](https://tools.ietf.org/html/rfc7591)
  * [RFC 7636 - Proof Key for Code Exchange by OAuth Public Clients](https://tools.ietf.org/html/rfc7636)
  * [RFC 7636 Section 4.3 - Client Creates a Code Challenge](https://tools.ietf.org/html/rfc7636#section-4.3)
  * [IANA OAuth Parameters](http://www.iana.org/assignments/oauth-parameters)
