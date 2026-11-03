# Chapter 2. LocalResourceAccessReview [authorization.openshift.io/v1]

Description
    

LocalResourceAccessReview is a means to request a list of which users and groups are authorized to perform the action specified by spec in a particular namespace 

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

- [2.1. Specification](02_01_specification.md)
- [2.2. API endpoints](02_02_api_endpoints.md)
