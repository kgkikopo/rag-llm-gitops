# Chapter 5. ImageStreamImport [image.openshift.io/v1]

Description
    

The image stream import resource provides an easy way for a user to find and import container images from other container image registries into the server. Individual images or an entire image repository may be imported, and users may choose to see the results of the import prior to tagging the resulting images into the specified image stream. 

This API is intended for end-user tools that need to see the metadata of the image prior to import (for instance, to generate an application from it). Clients that know the desired image can continue to create spec.tags directly into their image streams. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `spec`
  * `status`

- [5.1. Specification](05_01_specification.md)
- [5.2. API endpoints](05_02_api_endpoints.md)
