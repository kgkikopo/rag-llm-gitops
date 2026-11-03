# Chapter 4. ResourceAccessReview [authorization.openshift.io/v1]

Description
    

ResourceAccessReview is a means to request a list of which users and groups are authorized to perform the action specified by spec 

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

- [4.1. Specification](04_01_specification.md)
- [4.2. API endpoints](04_02_api_endpoints.md)
