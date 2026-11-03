# Chapter 9. ImageStreamTag [image.openshift.io/v1]

Description
    

ImageStreamTag represents an Image that is retrieved by tag name from an ImageStream. Use this resource to interact with the tags and images in an image stream by tag, or to see the image details for a particular tag. The image associated with this resource is the most recently successfully tagged, imported, or pushed image (as described in the image stream status.tags.items list for this tag). If an import is in progress or has failed the previous image will be shown. Deleting an image stream tag clears both the status and spec fields of an image stream. If no image can be retrieved for a given tag, a not found error will be returned. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `tag`
  * `generation`
  * `lookupPolicy`
  * `image`

- [9.1. Specification](09_01_specification.md)
- [9.2. API endpoints](09_02_api_endpoints.md)
