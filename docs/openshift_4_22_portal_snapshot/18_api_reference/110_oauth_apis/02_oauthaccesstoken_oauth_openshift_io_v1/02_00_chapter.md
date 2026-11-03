# Chapter 2. OAuthAccessToken [oauth.openshift.io/v1]

Description
    

OAuthAccessToken describes an OAuth access token. The name of a token must be prefixed with a `sha256~` string, must not contain "/" or "%" characters and must be at least 32 characters long. 

The name of the token is constructed from the actual token by sha256-hashing it and using URL-safe unpadded base64-encoding (as described in RFC4648) on the hashed result. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`

- [2.1. Specification](02_01_specification.md)
- [2.2. API endpoints](02_02_api_endpoints.md)
