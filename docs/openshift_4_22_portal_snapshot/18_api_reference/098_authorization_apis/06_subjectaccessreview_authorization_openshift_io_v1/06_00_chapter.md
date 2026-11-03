# Chapter 6. SubjectAccessReview [authorization.openshift.io/v1]

Description
    

SubjectAccessReview is an object for requesting information about whether a user or group can perform an action 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `namespace`
  * `verb`
  * `resourceAPIGroup`
  * `resourceAPIVersion`
  * `resource`
  * `resourceName`
  * `path`
  * `isNonResourceURL`
  * `user`
  * `groups`
  * `scopes`

- [6.1. Specification](06_01_specification.md)
- [6.2. API endpoints](06_02_api_endpoints.md)
