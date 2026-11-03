# Chapter 22. OAuth [config.openshift.io/v1]

Description
    

OAuth holds cluster-wide information about OAuth. The canonical name is `cluster`. It is used to configure the integrated OAuth server. This configuration is only honored when the top level Authentication config has type set to IntegratedOAuth. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `spec`

- [22.1. Specification](22_01_specification.md)
- [22.2. API endpoints](22_02_api_endpoints.md)
