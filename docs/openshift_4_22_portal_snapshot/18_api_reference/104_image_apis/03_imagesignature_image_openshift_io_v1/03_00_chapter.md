# Chapter 3. ImageSignature [image.openshift.io/v1]

Description
    

ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `type`
  * `content`

- [3.1. Specification](03_01_specification.md)
- [3.2. API endpoints](03_02_api_endpoints.md)
