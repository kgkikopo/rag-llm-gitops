# Chapter 4. ImageStreamImage [image.openshift.io/v1]

Description
    

ImageStreamImage represents an Image that is retrieved by image name from an ImageStream. User interfaces and regular users can use this resource to access the metadata details of a tagged image in the image stream history for viewing, since Image resources are not directly accessible to end users. A not found error will be returned if no such image is referenced by a tag within the ImageStream. Images are created when spec tags are set on an image stream that represent an image in an external registry, when pushing to the integrated registry, or when tagging an existing image from one image stream to another. The name of an image stream image is in the form "<STREAM>@<DIGEST>", where the digest is the content addressible identifier for the image (sha256:xxxxx…​). You can use ImageStreamImages as the from.kind of an image stream spec tag to reference an image exactly. The only operations supported on the imagestreamimage endpoint are retrieving the image. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `image`

- [4.1. Specification](04_01_specification.md)
- [4.2. API endpoints](04_02_api_endpoints.md)
