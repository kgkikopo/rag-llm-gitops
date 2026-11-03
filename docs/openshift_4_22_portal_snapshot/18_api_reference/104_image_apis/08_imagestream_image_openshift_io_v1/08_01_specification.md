# 8.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ImageStreamSpec represents options for ImageStreams.   
`status` |  `object` |  ImageStreamStatus contains information about the state of this image stream.   
Show more

## 8.1.1. .spec

Description
     ImageStreamSpec represents options for ImageStreams. 
Type
     `object`

Property| Type| Description  
---|---|---  
`dockerImageRepository` |  `string` |  dockerImageRepository is optional, if specified this stream is backed by a container repository on this server Deprecated: This field is deprecated as of v3.7 and will be removed in a future release. Specify the source for the tags to be imported in each tag via the spec.tags.from reference instead.   
`lookupPolicy` |  `object` |  ImageLookupPolicy describes how an image stream can be used to override the image references used by pods, builds, and other resources in a namespace.   
`tags` |  `array` |  tags map arbitrary string values to specific image locators   
`tags[]` |  `object` |  TagReference specifies optional annotations for images using this tag and an optional reference to an ImageStreamTag, ImageStreamImage, or DockerImage this tag should track.   
Show more

## 8.1.2. .spec.lookupPolicy

Description
     ImageLookupPolicy describes how an image stream can be used to override the image references used by pods, builds, and other resources in a namespace. 
Type
     `object`
Required
    

  * `local`



Property| Type| Description  
---|---|---  
`local` |  `boolean` |  local will change the docker short image references (like "mysql" or "php:latest") on objects in this namespace to the image ID whenever they match this image stream, instead of reaching out to a remote registry. The name will be fully qualified to an image ID if found. The tag’s referencePolicy is taken into account on the replaced value. Only works within the current namespace.   
Show more

## 8.1.3. .spec.tags

Description
     tags map arbitrary string values to specific image locators 
Type
     `array`

## 8.1.4. .spec.tags[]

Description
     TagReference specifies optional annotations for images using this tag and an optional reference to an ImageStreamTag, ImageStreamImage, or DockerImage this tag should track. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`annotations` |  `object (string)` |  Optional; if specified, annotations that are applied to images retrieved via ImageStreamTags.   
`from` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  Optional; if specified, a reference to another image that this tag should point to. Valid values are ImageStreamTag, ImageStreamImage, and DockerImage. ImageStreamTag references can only reference a tag within this same ImageStream.   
`generation` |  `integer` |  generation is a counter that tracks mutations to the spec tag (user intent). When a tag reference is changed the generation is set to match the current stream generation (which is incremented every time spec is changed). Other processes in the system like the image importer observe that the generation of spec tag is newer than the generation recorded in the status and use that as a trigger to import the newest remote tag. To trigger a new import, clients may set this value to zero which will reset the generation to the latest stream generation. Legacy clients will send this value as nil which will be merged with the current tag generation.   
`importPolicy` |  `object` |  TagImportPolicy controls how images related to this tag will be imported.   
`name` |  `string` |  name of the tag   
`reference` |  `boolean` |  reference states if the tag will be imported. Default value is false, which means the tag will be imported.   
`referencePolicy` |  `object` |  TagReferencePolicy describes how pull-specs for images in this image stream tag are generated when image change triggers in deployment configs or builds are resolved. This allows the image stream author to control how images are accessed.   
Show more

## 8.1.5. .spec.tags[].importPolicy

Description
     TagImportPolicy controls how images related to this tag will be imported. 
Type
     `object`

Property| Type| Description  
---|---|---  
`importMode` |  `string` |  importMode describes how to import an image manifest.   
`insecure` |  `boolean` |  insecure is true if the server may bypass certificate verification or connect directly over HTTP during image import.   
`scheduled` |  `boolean` |  scheduled indicates to the server that this tag should be periodically checked to ensure it is up to date, and imported   
Show more

## 8.1.6. .spec.tags[].referencePolicy

Description
     TagReferencePolicy describes how pull-specs for images in this image stream tag are generated when image change triggers in deployment configs or builds are resolved. This allows the image stream author to control how images are accessed. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`type` |  `string` |  type determines how the image pull spec should be transformed when the image stream tag is used in deployment config triggers or new builds. The default value is `Source`, indicating the original location of the image should be used (if imported). The user may also specify `Local`, indicating that the pull spec should point to the integrated container image registry and leverage the registry’s ability to proxy the pull to an upstream registry. `Local` allows the credentials used to pull this image to be managed from the image stream’s namespace, so others on the platform can access a remote image but have no access to the remote secret. It also allows the image layers to be mirrored into the local registry which the images can still be pulled even if the upstream registry is unavailable.   
Show more

## 8.1.7. .status

Description
     ImageStreamStatus contains information about the state of this image stream. 
Type
     `object`

Property| Type| Description  
---|---|---  
`dockerImageRepository` |  `string` |  dockerImageRepository represents the effective location this stream may be accessed at. May be empty until the server determines where the repository is located   
`publicDockerImageRepository` |  `string` |  publicDockerImageRepository represents the public location from where the image can be pulled outside the cluster. This field may be empty if the administrator has not exposed the integrated registry externally.   
`tags` |  `array` |  tags are a historical record of images associated with each tag. The first entry in the TagEvent array is the currently tagged image.   
`tags[]` |  `object` |  NamedTagEventList relates a tag to its image history.   
Show more

## 8.1.8. .status.tags

Description
     tags are a historical record of images associated with each tag. The first entry in the TagEvent array is the currently tagged image. 
Type
     `array`

## 8.1.9. .status.tags[]

Description
     NamedTagEventList relates a tag to its image history. 
Type
     `object`
Required
    

  * `tag`
  * `items`



Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions is an array of conditions that apply to the tag event list.   
`conditions[]` |  `object` |  TagEventCondition contains condition information for a tag event.   
`items` |  `array` |  Standard object’s metadata.   
`items[]` |  `object` |  TagEvent is used by ImageStreamStatus to keep a historical record of images associated with a tag.   
`tag` |  `string` |  tag is the tag for which the history is recorded   
Show more

## 8.1.10. .status.tags[].conditions

Description
     conditions is an array of conditions that apply to the tag event list. 
Type
     `array`

## 8.1.11. .status.tags[].conditions[]

Description
     TagEventCondition contains condition information for a tag event. 
Type
     `object`
Required
    

  * `type`
  * `status`
  * `generation`



Property| Type| Description  
---|---|---  
`generation` |  `integer` |  generation is the spec tag generation that this status corresponds to   
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  lastTransitionTime is the time the condition transitioned from one status to another.   
`message` |  `string` |  message is a human readable description of the details about last transition, complementing reason.   
`reason` |  `string` |  reason is a brief machine readable explanation for the condition’s last transition.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of tag event condition, currently only ImportSuccess   
Show more

## 8.1.12. .status.tags[].items

Description
     Standard object’s metadata. 
Type
     `array`

## 8.1.13. .status.tags[].items[]

Description
     TagEvent is used by ImageStreamStatus to keep a historical record of images associated with a tag. 
Type
     `object`
Required
    

  * `created`
  * `dockerImageReference`
  * `image`
  * `generation`



Property| Type| Description  
---|---|---  
`created` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  created holds the time the TagEvent was created   
`dockerImageReference` |  `string` |  dockerImageReference is the string that can be used to pull this image   
`generation` |  `integer` |  generation is the spec tag generation that resulted in this tag being updated   
`image` |  `string` |  image is the image   
Show more
