# Chapter 4. PodSecurityPolicyReview [security.openshift.io/v1]

Description
    

PodSecurityPolicyReview checks which service accounts (not users, since that would be cluster-wide) can create the `PodTemplateSpec` in question. 

Compatibility level 2: Stable within a major release for a minimum of 9 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `spec`

- [4.1. Specification](04_01_specification.md)
- [4.2. API endpoints](04_02_api_endpoints.md)
