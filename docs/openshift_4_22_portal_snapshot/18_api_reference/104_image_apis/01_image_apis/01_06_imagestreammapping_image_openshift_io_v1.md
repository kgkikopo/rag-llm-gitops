# 1.6. ImageStreamMapping [image.openshift.io/v1]

Description
    

ImageStreamMapping represents a mapping from a single image stream tag to a container image as well as the reference to the container image stream the image came from. This resource is used by privileged integrators to create an image resource and to associate it with an image stream in the status tags field. Creating an ImageStreamMapping will allow any user who can view the image stream to tag or pull that image, so only create mappings where the user has proven they have access to the image contents directly. The only operation supported for this resource is create and the metadata name and namespace should be set to the image stream containing the tag that should be updated. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
