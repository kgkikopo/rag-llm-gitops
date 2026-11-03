# Chapter 10. ImageTag [image.openshift.io/v1]

Description
    

ImageTag represents a single tag within an image stream and includes the spec, the status history, and the currently referenced image (if any) of the provided tag. This type replaces the ImageStreamTag by providing a full view of the tag. ImageTags are returned for every spec or status tag present on the image stream. If no tag exists in either form, a not found error will be returned by the API. A create operation will succeed if no spec tag has already been defined and the spec field is set. Delete will remove both spec and status elements from the image stream. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `spec`
  * `status`
  * `image`

- [10.1. Specification](10_01_specification.md)
- [10.2. API endpoints](10_02_api_endpoints.md)
