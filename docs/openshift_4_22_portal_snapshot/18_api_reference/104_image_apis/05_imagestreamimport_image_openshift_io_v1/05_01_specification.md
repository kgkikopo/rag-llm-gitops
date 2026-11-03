# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ImageStreamImportSpec defines what images should be imported.   
`status` |  `object` |  ImageStreamImportStatus contains information about the status of an image stream import.   
Show more

## 5.1.1. .spec

Description
     ImageStreamImportSpec defines what images should be imported. 
Type
     `object`
Required
    

  * `import`



Property| Type| Description  
---|---|---  
`images` |  `array` |  images are a list of individual images to import.   
`images[]` |  `object` |  ImageImportSpec describes a request to import a specific image.   
`import` |  `boolean` |  import indicates whether to perform an import - if so, the specified tags are set on the spec and status of the image stream defined by the type meta.   
`repository` |  `object` |  RepositoryImportSpec describes a request to import images from a container image repository.   
Show more

## 5.1.2. .spec.images

Description
     images are a list of individual images to import. 
Type
     `array`

## 5.1.3. .spec.images[]

Description
     ImageImportSpec describes a request to import a specific image. 
Type
     `object`
Required
    

  * `from`



Property| Type| Description  
---|---|---  
`from` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  from is the source of an image to import; only kind DockerImage is allowed   
`importPolicy` |  `object` |  TagImportPolicy controls how images related to this tag will be imported.   
`includeManifest` |  `boolean` |  includeManifest determines if the manifest for each image is returned in the response   
`referencePolicy` |  `object` |  TagReferencePolicy describes how pull-specs for images in this image stream tag are generated when image change triggers in deployment configs or builds are resolved. This allows the image stream author to control how images are accessed.   
`to` |  `LocalObjectReference` |  To is a tag in the current image stream to assign the imported image to, if name is not specified the default tag from from.name will be used   
Show more

## 5.1.4. .spec.images[].importPolicy

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

## 5.1.5. .spec.images[].referencePolicy

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

## 5.1.6. .spec.repository

Description
     RepositoryImportSpec describes a request to import images from a container image repository. 
Type
     `object`
Required
    

  * `from`



Property| Type| Description  
---|---|---  
`from` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  from is the source for the image repository to import; only kind DockerImage and a name of a container image repository is allowed   
`importPolicy` |  `object` |  TagImportPolicy controls how images related to this tag will be imported.   
`includeManifest` |  `boolean` |  includeManifest determines if the manifest for each image is returned in the response   
`referencePolicy` |  `object` |  TagReferencePolicy describes how pull-specs for images in this image stream tag are generated when image change triggers in deployment configs or builds are resolved. This allows the image stream author to control how images are accessed.   
Show more

## 5.1.7. .spec.repository.importPolicy

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

## 5.1.8. .spec.repository.referencePolicy

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

## 5.1.9. .status

Description
     ImageStreamImportStatus contains information about the status of an image stream import. 
Type
     `object`

Property| Type| Description  
---|---|---  
`images` |  `array` |  images is set with the result of importing spec.images   
`images[]` |  `object` |  ImageImportStatus describes the result of an image import.   
`import` |  `object` |  An ImageStream stores a mapping of tags to images, metadata overrides that are applied when images are tagged in a stream, and an optional reference to a container image repository on a registry. Users typically update the spec.tags field to point to external images which are imported from container registries using credentials in your namespace with the pull secret type, or to existing image stream tags and images which are immediately accessible for tagging or pulling. The history of images applied to a tag is visible in the status.tags field and any user who can view an image stream is allowed to tag that image into their own image streams. Access to pull images from the integrated registry is granted by having the "get imagestreams/layers" permission on a given image stream. Users may remove a tag by deleting the imagestreamtag resource, which causes both spec and status for that tag to be removed. Image stream history is retained until an administrator runs the prune operation, which removes references that are no longer in use. To preserve a historical image, ensure there is a tag in spec pointing to that image by its digest.  Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).   
`repository` |  `object` |  RepositoryImportStatus describes the result of an image repository import   
Show more

## 5.1.10. .status.images

Description
     images is set with the result of importing spec.images 
Type
     `array`

## 5.1.11. .status.images[]

Description
     ImageImportStatus describes the result of an image import. 
Type
     `object`
Required
    

  * `status`



Property| Type| Description  
---|---|---  
`image` |  `object` |  Image is an immutable representation of a container image and its metadata at a point in time. Images are named by taking a hash of their contents (metadata and content) and any change in format, content, or metadata results in a new name. The images resource is primarily for use by cluster administrators and integrations like the cluster image registry - end users, instead, access images via the imagestreamtags or imagestreamimages resources. While image metadata is stored in the API, any integration that implements the container image registry API must provide its own storage for the raw manifest data, image config, and layer contents.  Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).   
`manifests` |  `array` |  manifests holds sub-manifests metadata when importing a manifest list   
`manifests[]` |  `object` |  Image is an immutable representation of a container image and its metadata at a point in time. Images are named by taking a hash of their contents (metadata and content) and any change in format, content, or metadata results in a new name. The images resource is primarily for use by cluster administrators and integrations like the cluster image registry - end users, instead, access images via the imagestreamtags or imagestreamimages resources. While image metadata is stored in the API, any integration that implements the container image registry API must provide its own storage for the raw manifest data, image config, and layer contents.  Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).   
`status` |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) |  status is the status of the image import, including errors encountered while retrieving the image   
`tag` |  `string` |  tag is the tag this image was located under, if any   
Show more

## 5.1.12. .status.images[].image

Description
    

Image is an immutable representation of a container image and its metadata at a point in time. Images are named by taking a hash of their contents (metadata and content) and any change in format, content, or metadata results in a new name. The images resource is primarily for use by cluster administrators and integrations like the cluster image registry - end users, instead, access images via the imagestreamtags or imagestreamimages resources. While image metadata is stored in the API, any integration that implements the container image registry API must provide its own storage for the raw manifest data, image config, and layer contents. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`dockerImageConfig` |  `string` |  dockerImageConfig is a JSON blob that the runtime uses to set up the container. This is a part of manifest schema v2. Will not be set when the image represents a manifest list.   
`dockerImageLayers` |  `array` |  dockerImageLayers represents the layers in the image. May not be set if the image does not define that data or if the image represents a manifest list.   
`dockerImageLayers[]` |  `object` |  ImageLayer represents a single layer of the image. Some images may have multiple layers. Some may have none.   
`dockerImageManifest` |  `string` |  dockerImageManifest is the raw JSON of the manifest   
`dockerImageManifestMediaType` |  `string` |  dockerImageManifestMediaType specifies the mediaType of manifest. This is a part of manifest schema v2.   
`dockerImageManifests` |  `array` |  dockerImageManifests holds information about sub-manifests when the image represents a manifest list. When this field is present, no DockerImageLayers should be specified.   
`dockerImageManifests[]` |  `object` |  ImageManifest represents sub-manifests of a manifest list. The Digest field points to a regular Image object.   
`dockerImageMetadata` |  [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) |  dockerImageMetadata contains metadata about this image   
`dockerImageMetadataVersion` |  `string` |  dockerImageMetadataVersion conveys the version of the object, which if empty defaults to "1.0"   
`dockerImageReference` |  `string` |  dockerImageReference is the string that can be used to pull this image.   
`dockerImageSignatures` |  `array (string)` |  dockerImageSignatures provides the signatures as opaque blobs. This is a part of manifest schema v1.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`signatures` |  `array` |  signatures holds all signatures of the image.   
`signatures[]` |  `object` |  ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose.  Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).   
Show more

## 5.1.13. .status.images[].image.dockerImageLayers

Description
     dockerImageLayers represents the layers in the image. May not be set if the image does not define that data or if the image represents a manifest list. 
Type
     `array`

## 5.1.14. .status.images[].image.dockerImageLayers[]

Description
     ImageLayer represents a single layer of the image. Some images may have multiple layers. Some may have none. 
Type
     `object`
Required
    

  * `name`
  * `size`
  * `mediaType`



Property| Type| Description  
---|---|---  
`mediaType` |  `string` |  mediaType of the referenced object.   
`name` |  `string` |  name of the layer as defined by the underlying store.   
`size` |  `integer` |  size of the layer in bytes as defined by the underlying store.   
Show more

## 5.1.15. .status.images[].image.dockerImageManifests

Description
     dockerImageManifests holds information about sub-manifests when the image represents a manifest list. When this field is present, no DockerImageLayers should be specified. 
Type
     `array`

## 5.1.16. .status.images[].image.dockerImageManifests[]

Description
     ImageManifest represents sub-manifests of a manifest list. The Digest field points to a regular Image object. 
Type
     `object`
Required
    

  * `digest`
  * `mediaType`
  * `manifestSize`
  * `architecture`
  * `os`



Property| Type| Description  
---|---|---  
`architecture` |  `string` |  architecture specifies the supported CPU architecture, for example `amd64` or `ppc64le`.   
`digest` |  `string` |  digest is the unique identifier for the manifest. It refers to an Image object.   
`manifestSize` |  `integer` |  manifestSize represents the size of the raw object contents, in bytes.   
`mediaType` |  `string` |  mediaType defines the type of the manifest, possible values are application/vnd.oci.image.manifest.v1+json, application/vnd.docker.distribution.manifest.v2+json or application/vnd.docker.distribution.manifest.v1+json.   
`os` |  `string` |  os specifies the operating system, for example `linux`.   
`variant` |  `string` |  variant is an optional field repreenting a variant of the CPU, for example v6 to specify a particular CPU variant of the ARM CPU.   
Show more

## 5.1.17. .status.images[].image.signatures

Description
     signatures holds all signatures of the image. 
Type
     `array`

## 5.1.18. .status.images[].image.signatures[]

Description
    

ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `type`
  * `content`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`conditions` |  `array` |  conditions represent the latest available observations of a signature’s current state.   
`conditions[]` |  `object` |  SignatureCondition describes an image signature condition of particular kind at particular probe time.   
`content` |  `string` |  Required: An opaque binary string which is an image’s signature.   
`created` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  If specified, it is the time of signature’s creation.   
`imageIdentity` |  `string` |  A human readable string representing image’s identity. It could be a product name and version, or an image pull spec (e.g. "registry.access.redhat.com/rhel7/rhel:7.2").   
`issuedBy` |  `object` |  SignatureIssuer holds information about an issuer of signing certificate or key.   
`issuedTo` |  `object` |  SignatureSubject holds information about a person or entity who created the signature.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`signedClaims` |  `object (string)` |  Contains claims from the signature.   
`type` |  `string` |  Required: Describes a type of stored blob.   
Show more

## 5.1.19. .status.images[].image.signatures[].conditions

Description
     conditions represent the latest available observations of a signature’s current state. 
Type
     `array`

## 5.1.20. .status.images[].image.signatures[].conditions[]

Description
     SignatureCondition describes an image signature condition of particular kind at particular probe time. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastProbeTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition was checked.   
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition transit from one status to another.   
`message` |  `string` |  Human readable message indicating details about last transition.   
`reason` |  `string` |  (brief) reason for the condition’s last transition.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of signature condition, Complete or Failed.   
Show more

## 5.1.21. .status.images[].image.signatures[].issuedBy

Description
     SignatureIssuer holds information about an issuer of signing certificate or key. 
Type
     `object`

Property| Type| Description  
---|---|---  
`commonName` |  `string` |  Common name (e.g. openshift-signing-service).   
`organization` |  `string` |  organization name.   
Show more

## 5.1.22. .status.images[].image.signatures[].issuedTo

Description
     SignatureSubject holds information about a person or entity who created the signature. 
Type
     `object`
Required
    

  * `publicKeyID`



Property| Type| Description  
---|---|---  
`commonName` |  `string` |  Common name (e.g. openshift-signing-service).   
`organization` |  `string` |  organization name.   
`publicKeyID` |  `string` |  If present, it is a human readable key id of public key belonging to the subject used to verify image signature. It should contain at least 64 lowest bits of public key’s fingerprint (e.g. 0x685ebe62bf278440).   
Show more

## 5.1.23. .status.images[].manifests

Description
     manifests holds sub-manifests metadata when importing a manifest list 
Type
     `array`

## 5.1.24. .status.images[].manifests[]

Description
    

Image is an immutable representation of a container image and its metadata at a point in time. Images are named by taking a hash of their contents (metadata and content) and any change in format, content, or metadata results in a new name. The images resource is primarily for use by cluster administrators and integrations like the cluster image registry - end users, instead, access images via the imagestreamtags or imagestreamimages resources. While image metadata is stored in the API, any integration that implements the container image registry API must provide its own storage for the raw manifest data, image config, and layer contents. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`dockerImageConfig` |  `string` |  dockerImageConfig is a JSON blob that the runtime uses to set up the container. This is a part of manifest schema v2. Will not be set when the image represents a manifest list.   
`dockerImageLayers` |  `array` |  dockerImageLayers represents the layers in the image. May not be set if the image does not define that data or if the image represents a manifest list.   
`dockerImageLayers[]` |  `object` |  ImageLayer represents a single layer of the image. Some images may have multiple layers. Some may have none.   
`dockerImageManifest` |  `string` |  dockerImageManifest is the raw JSON of the manifest   
`dockerImageManifestMediaType` |  `string` |  dockerImageManifestMediaType specifies the mediaType of manifest. This is a part of manifest schema v2.   
`dockerImageManifests` |  `array` |  dockerImageManifests holds information about sub-manifests when the image represents a manifest list. When this field is present, no DockerImageLayers should be specified.   
`dockerImageManifests[]` |  `object` |  ImageManifest represents sub-manifests of a manifest list. The Digest field points to a regular Image object.   
`dockerImageMetadata` |  [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) |  dockerImageMetadata contains metadata about this image   
`dockerImageMetadataVersion` |  `string` |  dockerImageMetadataVersion conveys the version of the object, which if empty defaults to "1.0"   
`dockerImageReference` |  `string` |  dockerImageReference is the string that can be used to pull this image.   
`dockerImageSignatures` |  `array (string)` |  dockerImageSignatures provides the signatures as opaque blobs. This is a part of manifest schema v1.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`signatures` |  `array` |  signatures holds all signatures of the image.   
`signatures[]` |  `object` |  ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose.  Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).   
Show more

## 5.1.25. .status.images[].manifests[].dockerImageLayers

Description
     dockerImageLayers represents the layers in the image. May not be set if the image does not define that data or if the image represents a manifest list. 
Type
     `array`

## 5.1.26. .status.images[].manifests[].dockerImageLayers[]

Description
     ImageLayer represents a single layer of the image. Some images may have multiple layers. Some may have none. 
Type
     `object`
Required
    

  * `name`
  * `size`
  * `mediaType`



Property| Type| Description  
---|---|---  
`mediaType` |  `string` |  mediaType of the referenced object.   
`name` |  `string` |  name of the layer as defined by the underlying store.   
`size` |  `integer` |  size of the layer in bytes as defined by the underlying store.   
Show more

## 5.1.27. .status.images[].manifests[].dockerImageManifests

Description
     dockerImageManifests holds information about sub-manifests when the image represents a manifest list. When this field is present, no DockerImageLayers should be specified. 
Type
     `array`

## 5.1.28. .status.images[].manifests[].dockerImageManifests[]

Description
     ImageManifest represents sub-manifests of a manifest list. The Digest field points to a regular Image object. 
Type
     `object`
Required
    

  * `digest`
  * `mediaType`
  * `manifestSize`
  * `architecture`
  * `os`



Property| Type| Description  
---|---|---  
`architecture` |  `string` |  architecture specifies the supported CPU architecture, for example `amd64` or `ppc64le`.   
`digest` |  `string` |  digest is the unique identifier for the manifest. It refers to an Image object.   
`manifestSize` |  `integer` |  manifestSize represents the size of the raw object contents, in bytes.   
`mediaType` |  `string` |  mediaType defines the type of the manifest, possible values are application/vnd.oci.image.manifest.v1+json, application/vnd.docker.distribution.manifest.v2+json or application/vnd.docker.distribution.manifest.v1+json.   
`os` |  `string` |  os specifies the operating system, for example `linux`.   
`variant` |  `string` |  variant is an optional field repreenting a variant of the CPU, for example v6 to specify a particular CPU variant of the ARM CPU.   
Show more

## 5.1.29. .status.images[].manifests[].signatures

Description
     signatures holds all signatures of the image. 
Type
     `array`

## 5.1.30. .status.images[].manifests[].signatures[]

Description
    

ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `type`
  * `content`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`conditions` |  `array` |  conditions represent the latest available observations of a signature’s current state.   
`conditions[]` |  `object` |  SignatureCondition describes an image signature condition of particular kind at particular probe time.   
`content` |  `string` |  Required: An opaque binary string which is an image’s signature.   
`created` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  If specified, it is the time of signature’s creation.   
`imageIdentity` |  `string` |  A human readable string representing image’s identity. It could be a product name and version, or an image pull spec (e.g. "registry.access.redhat.com/rhel7/rhel:7.2").   
`issuedBy` |  `object` |  SignatureIssuer holds information about an issuer of signing certificate or key.   
`issuedTo` |  `object` |  SignatureSubject holds information about a person or entity who created the signature.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`signedClaims` |  `object (string)` |  Contains claims from the signature.   
`type` |  `string` |  Required: Describes a type of stored blob.   
Show more

## 5.1.31. .status.images[].manifests[].signatures[].conditions

Description
     conditions represent the latest available observations of a signature’s current state. 
Type
     `array`

## 5.1.32. .status.images[].manifests[].signatures[].conditions[]

Description
     SignatureCondition describes an image signature condition of particular kind at particular probe time. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastProbeTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition was checked.   
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition transit from one status to another.   
`message` |  `string` |  Human readable message indicating details about last transition.   
`reason` |  `string` |  (brief) reason for the condition’s last transition.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of signature condition, Complete or Failed.   
Show more

## 5.1.33. .status.images[].manifests[].signatures[].issuedBy

Description
     SignatureIssuer holds information about an issuer of signing certificate or key. 
Type
     `object`

Property| Type| Description  
---|---|---  
`commonName` |  `string` |  Common name (e.g. openshift-signing-service).   
`organization` |  `string` |  organization name.   
Show more

## 5.1.34. .status.images[].manifests[].signatures[].issuedTo

Description
     SignatureSubject holds information about a person or entity who created the signature. 
Type
     `object`
Required
    

  * `publicKeyID`



Property| Type| Description  
---|---|---  
`commonName` |  `string` |  Common name (e.g. openshift-signing-service).   
`organization` |  `string` |  organization name.   
`publicKeyID` |  `string` |  If present, it is a human readable key id of public key belonging to the subject used to verify image signature. It should contain at least 64 lowest bits of public key’s fingerprint (e.g. 0x685ebe62bf278440).   
Show more

## 5.1.35. .status.import

Description
    

An ImageStream stores a mapping of tags to images, metadata overrides that are applied when images are tagged in a stream, and an optional reference to a container image repository on a registry. Users typically update the spec.tags field to point to external images which are imported from container registries using credentials in your namespace with the pull secret type, or to existing image stream tags and images which are immediately accessible for tagging or pulling. The history of images applied to a tag is visible in the status.tags field and any user who can view an image stream is allowed to tag that image into their own image streams. Access to pull images from the integrated registry is granted by having the "get imagestreams/layers" permission on a given image stream. Users may remove a tag by deleting the imagestreamtag resource, which causes both spec and status for that tag to be removed. Image stream history is retained until an administrator runs the prune operation, which removes references that are no longer in use. To preserve a historical image, ensure there is a tag in spec pointing to that image by its digest. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ImageStreamSpec represents options for ImageStreams.   
`status` |  `object` |  ImageStreamStatus contains information about the state of this image stream.   
Show more

## 5.1.36. .status.import.spec

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

## 5.1.37. .status.import.spec.lookupPolicy

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

## 5.1.38. .status.import.spec.tags

Description
     tags map arbitrary string values to specific image locators 
Type
     `array`

## 5.1.39. .status.import.spec.tags[]

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

## 5.1.40. .status.import.spec.tags[].importPolicy

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

## 5.1.41. .status.import.spec.tags[].referencePolicy

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

## 5.1.42. .status.import.status

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

## 5.1.43. .status.import.status.tags

Description
     tags are a historical record of images associated with each tag. The first entry in the TagEvent array is the currently tagged image. 
Type
     `array`

## 5.1.44. .status.import.status.tags[]

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

## 5.1.45. .status.import.status.tags[].conditions

Description
     conditions is an array of conditions that apply to the tag event list. 
Type
     `array`

## 5.1.46. .status.import.status.tags[].conditions[]

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

## 5.1.47. .status.import.status.tags[].items

Description
     Standard object’s metadata. 
Type
     `array`

## 5.1.48. .status.import.status.tags[].items[]

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

## 5.1.49. .status.repository

Description
     RepositoryImportStatus describes the result of an image repository import 
Type
     `object`

Property| Type| Description  
---|---|---  
`additionalTags` |  `array (string)` |  additionalTags are tags that exist in the repository but were not imported because a maximum limit of automatic imports was applied.   
`images` |  `array` |  images is a list of images successfully retrieved by the import of the repository.   
`images[]` |  `object` |  ImageImportStatus describes the result of an image import.   
`status` |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) |  status reflects whether any failure occurred during import   
Show more

## 5.1.50. .status.repository.images

Description
     images is a list of images successfully retrieved by the import of the repository. 
Type
     `array`

## 5.1.51. .status.repository.images[]

Description
     ImageImportStatus describes the result of an image import. 
Type
     `object`
Required
    

  * `status`



Property| Type| Description  
---|---|---  
`image` |  `object` |  Image is an immutable representation of a container image and its metadata at a point in time. Images are named by taking a hash of their contents (metadata and content) and any change in format, content, or metadata results in a new name. The images resource is primarily for use by cluster administrators and integrations like the cluster image registry - end users, instead, access images via the imagestreamtags or imagestreamimages resources. While image metadata is stored in the API, any integration that implements the container image registry API must provide its own storage for the raw manifest data, image config, and layer contents.  Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).   
`manifests` |  `array` |  manifests holds sub-manifests metadata when importing a manifest list   
`manifests[]` |  `object` |  Image is an immutable representation of a container image and its metadata at a point in time. Images are named by taking a hash of their contents (metadata and content) and any change in format, content, or metadata results in a new name. The images resource is primarily for use by cluster administrators and integrations like the cluster image registry - end users, instead, access images via the imagestreamtags or imagestreamimages resources. While image metadata is stored in the API, any integration that implements the container image registry API must provide its own storage for the raw manifest data, image config, and layer contents.  Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).   
`status` |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) |  status is the status of the image import, including errors encountered while retrieving the image   
`tag` |  `string` |  tag is the tag this image was located under, if any   
Show more

## 5.1.52. .status.repository.images[].image

Description
    

Image is an immutable representation of a container image and its metadata at a point in time. Images are named by taking a hash of their contents (metadata and content) and any change in format, content, or metadata results in a new name. The images resource is primarily for use by cluster administrators and integrations like the cluster image registry - end users, instead, access images via the imagestreamtags or imagestreamimages resources. While image metadata is stored in the API, any integration that implements the container image registry API must provide its own storage for the raw manifest data, image config, and layer contents. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`dockerImageConfig` |  `string` |  dockerImageConfig is a JSON blob that the runtime uses to set up the container. This is a part of manifest schema v2. Will not be set when the image represents a manifest list.   
`dockerImageLayers` |  `array` |  dockerImageLayers represents the layers in the image. May not be set if the image does not define that data or if the image represents a manifest list.   
`dockerImageLayers[]` |  `object` |  ImageLayer represents a single layer of the image. Some images may have multiple layers. Some may have none.   
`dockerImageManifest` |  `string` |  dockerImageManifest is the raw JSON of the manifest   
`dockerImageManifestMediaType` |  `string` |  dockerImageManifestMediaType specifies the mediaType of manifest. This is a part of manifest schema v2.   
`dockerImageManifests` |  `array` |  dockerImageManifests holds information about sub-manifests when the image represents a manifest list. When this field is present, no DockerImageLayers should be specified.   
`dockerImageManifests[]` |  `object` |  ImageManifest represents sub-manifests of a manifest list. The Digest field points to a regular Image object.   
`dockerImageMetadata` |  [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) |  dockerImageMetadata contains metadata about this image   
`dockerImageMetadataVersion` |  `string` |  dockerImageMetadataVersion conveys the version of the object, which if empty defaults to "1.0"   
`dockerImageReference` |  `string` |  dockerImageReference is the string that can be used to pull this image.   
`dockerImageSignatures` |  `array (string)` |  dockerImageSignatures provides the signatures as opaque blobs. This is a part of manifest schema v1.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`signatures` |  `array` |  signatures holds all signatures of the image.   
`signatures[]` |  `object` |  ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose.  Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).   
Show more

## 5.1.53. .status.repository.images[].image.dockerImageLayers

Description
     dockerImageLayers represents the layers in the image. May not be set if the image does not define that data or if the image represents a manifest list. 
Type
     `array`

## 5.1.54. .status.repository.images[].image.dockerImageLayers[]

Description
     ImageLayer represents a single layer of the image. Some images may have multiple layers. Some may have none. 
Type
     `object`
Required
    

  * `name`
  * `size`
  * `mediaType`



Property| Type| Description  
---|---|---  
`mediaType` |  `string` |  mediaType of the referenced object.   
`name` |  `string` |  name of the layer as defined by the underlying store.   
`size` |  `integer` |  size of the layer in bytes as defined by the underlying store.   
Show more

## 5.1.55. .status.repository.images[].image.dockerImageManifests

Description
     dockerImageManifests holds information about sub-manifests when the image represents a manifest list. When this field is present, no DockerImageLayers should be specified. 
Type
     `array`

## 5.1.56. .status.repository.images[].image.dockerImageManifests[]

Description
     ImageManifest represents sub-manifests of a manifest list. The Digest field points to a regular Image object. 
Type
     `object`
Required
    

  * `digest`
  * `mediaType`
  * `manifestSize`
  * `architecture`
  * `os`



Property| Type| Description  
---|---|---  
`architecture` |  `string` |  architecture specifies the supported CPU architecture, for example `amd64` or `ppc64le`.   
`digest` |  `string` |  digest is the unique identifier for the manifest. It refers to an Image object.   
`manifestSize` |  `integer` |  manifestSize represents the size of the raw object contents, in bytes.   
`mediaType` |  `string` |  mediaType defines the type of the manifest, possible values are application/vnd.oci.image.manifest.v1+json, application/vnd.docker.distribution.manifest.v2+json or application/vnd.docker.distribution.manifest.v1+json.   
`os` |  `string` |  os specifies the operating system, for example `linux`.   
`variant` |  `string` |  variant is an optional field repreenting a variant of the CPU, for example v6 to specify a particular CPU variant of the ARM CPU.   
Show more

## 5.1.57. .status.repository.images[].image.signatures

Description
     signatures holds all signatures of the image. 
Type
     `array`

## 5.1.58. .status.repository.images[].image.signatures[]

Description
    

ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `type`
  * `content`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`conditions` |  `array` |  conditions represent the latest available observations of a signature’s current state.   
`conditions[]` |  `object` |  SignatureCondition describes an image signature condition of particular kind at particular probe time.   
`content` |  `string` |  Required: An opaque binary string which is an image’s signature.   
`created` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  If specified, it is the time of signature’s creation.   
`imageIdentity` |  `string` |  A human readable string representing image’s identity. It could be a product name and version, or an image pull spec (e.g. "registry.access.redhat.com/rhel7/rhel:7.2").   
`issuedBy` |  `object` |  SignatureIssuer holds information about an issuer of signing certificate or key.   
`issuedTo` |  `object` |  SignatureSubject holds information about a person or entity who created the signature.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`signedClaims` |  `object (string)` |  Contains claims from the signature.   
`type` |  `string` |  Required: Describes a type of stored blob.   
Show more

## 5.1.59. .status.repository.images[].image.signatures[].conditions

Description
     conditions represent the latest available observations of a signature’s current state. 
Type
     `array`

## 5.1.60. .status.repository.images[].image.signatures[].conditions[]

Description
     SignatureCondition describes an image signature condition of particular kind at particular probe time. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastProbeTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition was checked.   
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition transit from one status to another.   
`message` |  `string` |  Human readable message indicating details about last transition.   
`reason` |  `string` |  (brief) reason for the condition’s last transition.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of signature condition, Complete or Failed.   
Show more

## 5.1.61. .status.repository.images[].image.signatures[].issuedBy

Description
     SignatureIssuer holds information about an issuer of signing certificate or key. 
Type
     `object`

Property| Type| Description  
---|---|---  
`commonName` |  `string` |  Common name (e.g. openshift-signing-service).   
`organization` |  `string` |  organization name.   
Show more

## 5.1.62. .status.repository.images[].image.signatures[].issuedTo

Description
     SignatureSubject holds information about a person or entity who created the signature. 
Type
     `object`
Required
    

  * `publicKeyID`



Property| Type| Description  
---|---|---  
`commonName` |  `string` |  Common name (e.g. openshift-signing-service).   
`organization` |  `string` |  organization name.   
`publicKeyID` |  `string` |  If present, it is a human readable key id of public key belonging to the subject used to verify image signature. It should contain at least 64 lowest bits of public key’s fingerprint (e.g. 0x685ebe62bf278440).   
Show more

## 5.1.63. .status.repository.images[].manifests

Description
     manifests holds sub-manifests metadata when importing a manifest list 
Type
     `array`

## 5.1.64. .status.repository.images[].manifests[]

Description
    

Image is an immutable representation of a container image and its metadata at a point in time. Images are named by taking a hash of their contents (metadata and content) and any change in format, content, or metadata results in a new name. The images resource is primarily for use by cluster administrators and integrations like the cluster image registry - end users, instead, access images via the imagestreamtags or imagestreamimages resources. While image metadata is stored in the API, any integration that implements the container image registry API must provide its own storage for the raw manifest data, image config, and layer contents. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`dockerImageConfig` |  `string` |  dockerImageConfig is a JSON blob that the runtime uses to set up the container. This is a part of manifest schema v2. Will not be set when the image represents a manifest list.   
`dockerImageLayers` |  `array` |  dockerImageLayers represents the layers in the image. May not be set if the image does not define that data or if the image represents a manifest list.   
`dockerImageLayers[]` |  `object` |  ImageLayer represents a single layer of the image. Some images may have multiple layers. Some may have none.   
`dockerImageManifest` |  `string` |  dockerImageManifest is the raw JSON of the manifest   
`dockerImageManifestMediaType` |  `string` |  dockerImageManifestMediaType specifies the mediaType of manifest. This is a part of manifest schema v2.   
`dockerImageManifests` |  `array` |  dockerImageManifests holds information about sub-manifests when the image represents a manifest list. When this field is present, no DockerImageLayers should be specified.   
`dockerImageManifests[]` |  `object` |  ImageManifest represents sub-manifests of a manifest list. The Digest field points to a regular Image object.   
`dockerImageMetadata` |  [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-runtime-RawExtension) |  dockerImageMetadata contains metadata about this image   
`dockerImageMetadataVersion` |  `string` |  dockerImageMetadataVersion conveys the version of the object, which if empty defaults to "1.0"   
`dockerImageReference` |  `string` |  dockerImageReference is the string that can be used to pull this image.   
`dockerImageSignatures` |  `array (string)` |  dockerImageSignatures provides the signatures as opaque blobs. This is a part of manifest schema v1.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`signatures` |  `array` |  signatures holds all signatures of the image.   
`signatures[]` |  `object` |  ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose.  Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).   
Show more

## 5.1.65. .status.repository.images[].manifests[].dockerImageLayers

Description
     dockerImageLayers represents the layers in the image. May not be set if the image does not define that data or if the image represents a manifest list. 
Type
     `array`

## 5.1.66. .status.repository.images[].manifests[].dockerImageLayers[]

Description
     ImageLayer represents a single layer of the image. Some images may have multiple layers. Some may have none. 
Type
     `object`
Required
    

  * `name`
  * `size`
  * `mediaType`



Property| Type| Description  
---|---|---  
`mediaType` |  `string` |  mediaType of the referenced object.   
`name` |  `string` |  name of the layer as defined by the underlying store.   
`size` |  `integer` |  size of the layer in bytes as defined by the underlying store.   
Show more

## 5.1.67. .status.repository.images[].manifests[].dockerImageManifests

Description
     dockerImageManifests holds information about sub-manifests when the image represents a manifest list. When this field is present, no DockerImageLayers should be specified. 
Type
     `array`

## 5.1.68. .status.repository.images[].manifests[].dockerImageManifests[]

Description
     ImageManifest represents sub-manifests of a manifest list. The Digest field points to a regular Image object. 
Type
     `object`
Required
    

  * `digest`
  * `mediaType`
  * `manifestSize`
  * `architecture`
  * `os`



Property| Type| Description  
---|---|---  
`architecture` |  `string` |  architecture specifies the supported CPU architecture, for example `amd64` or `ppc64le`.   
`digest` |  `string` |  digest is the unique identifier for the manifest. It refers to an Image object.   
`manifestSize` |  `integer` |  manifestSize represents the size of the raw object contents, in bytes.   
`mediaType` |  `string` |  mediaType defines the type of the manifest, possible values are application/vnd.oci.image.manifest.v1+json, application/vnd.docker.distribution.manifest.v2+json or application/vnd.docker.distribution.manifest.v1+json.   
`os` |  `string` |  os specifies the operating system, for example `linux`.   
`variant` |  `string` |  variant is an optional field repreenting a variant of the CPU, for example v6 to specify a particular CPU variant of the ARM CPU.   
Show more

## 5.1.69. .status.repository.images[].manifests[].signatures

Description
     signatures holds all signatures of the image. 
Type
     `array`

## 5.1.70. .status.repository.images[].manifests[].signatures[]

Description
    

ImageSignature holds a signature of an image. It allows to verify image identity and possibly other claims as long as the signature is trusted. Based on this information it is possible to restrict runnable images to those matching cluster-wide policy. Mandatory fields should be parsed by clients doing image verification. The others are parsed from signature’s content by the server. They serve just an informative purpose. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `type`
  * `content`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`conditions` |  `array` |  conditions represent the latest available observations of a signature’s current state.   
`conditions[]` |  `object` |  SignatureCondition describes an image signature condition of particular kind at particular probe time.   
`content` |  `string` |  Required: An opaque binary string which is an image’s signature.   
`created` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  If specified, it is the time of signature’s creation.   
`imageIdentity` |  `string` |  A human readable string representing image’s identity. It could be a product name and version, or an image pull spec (e.g. "registry.access.redhat.com/rhel7/rhel:7.2").   
`issuedBy` |  `object` |  SignatureIssuer holds information about an issuer of signing certificate or key.   
`issuedTo` |  `object` |  SignatureSubject holds information about a person or entity who created the signature.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`signedClaims` |  `object (string)` |  Contains claims from the signature.   
`type` |  `string` |  Required: Describes a type of stored blob.   
Show more

## 5.1.71. .status.repository.images[].manifests[].signatures[].conditions

Description
     conditions represent the latest available observations of a signature’s current state. 
Type
     `array`

## 5.1.72. .status.repository.images[].manifests[].signatures[].conditions[]

Description
     SignatureCondition describes an image signature condition of particular kind at particular probe time. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastProbeTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition was checked.   
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition transit from one status to another.   
`message` |  `string` |  Human readable message indicating details about last transition.   
`reason` |  `string` |  (brief) reason for the condition’s last transition.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of signature condition, Complete or Failed.   
Show more

## 5.1.73. .status.repository.images[].manifests[].signatures[].issuedBy

Description
     SignatureIssuer holds information about an issuer of signing certificate or key. 
Type
     `object`

Property| Type| Description  
---|---|---  
`commonName` |  `string` |  Common name (e.g. openshift-signing-service).   
`organization` |  `string` |  organization name.   
Show more

## 5.1.74. .status.repository.images[].manifests[].signatures[].issuedTo

Description
     SignatureSubject holds information about a person or entity who created the signature. 
Type
     `object`
Required
    

  * `publicKeyID`



Property| Type| Description  
---|---|---  
`commonName` |  `string` |  Common name (e.g. openshift-signing-service).   
`organization` |  `string` |  organization name.   
`publicKeyID` |  `string` |  If present, it is a human readable key id of public key belonging to the subject used to verify image signature. It should contain at least 64 lowest bits of public key’s fingerprint (e.g. 0x685ebe62bf278440).   
Show more
