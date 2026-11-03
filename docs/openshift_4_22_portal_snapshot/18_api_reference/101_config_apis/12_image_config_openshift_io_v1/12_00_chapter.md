# Chapter 12. Image [config.openshift.io/v1]

Description
    

Image governs policies related to imagestream imports and runtime configuration for external registries. It allows cluster admins to configure which registries OpenShift is allowed to import images from, extra CA trust bundles for external registries, and policies to block or allow registry hostnames. When exposing OpenShift’s image registry to the public, this also lets cluster admins specify the external hostname. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `spec`

- [12.1. Specification](12_01_specification.md)
- [12.2. API endpoints](12_02_api_endpoints.md)
