# Chapter 3. LocalSubjectAccessReview [authorization.openshift.io/v1]

Description
    

LocalSubjectAccessReview is an object for requesting information about whether a user or group can perform an action in a particular namespace 

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

- [3.1. Specification](03_01_specification.md)
- [3.2. API endpoints](03_02_api_endpoints.md)
