# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec is a required field that defines the desired state of the ClusterCatalog. The controller ensures that the catalog is unpacked and served over the catalog content HTTP server.   
`status` |  `object` |  status contains the following information about the state of the ClusterCatalog: - Whether the catalog contents are being served via the catalog content HTTP server - Whether the ClusterCatalog is progressing to a new state - A reference to the source from which the catalog contents were retrieved   
Show more

## 3.1.1. .spec

Description
     spec is a required field that defines the desired state of the ClusterCatalog. The controller ensures that the catalog is unpacked and served over the catalog content HTTP server. 
Type
     `object`
Required
    

  * `source`



Property| Type| Description  
---|---|---  
`availabilityMode` |  `string` |  availabilityMode is an optional field that defines how the ClusterCatalog is made available to clients on the cluster.  Allowed values are "Available", "Unavailable", or omitted.  When omitted, the default value is "Available".  When set to "Available", the catalog contents are unpacked and served over the catalog content HTTP server. Clients should consider this ClusterCatalog and its contents as usable.  When set to "Unavailable", the catalog contents are no longer served over the catalog content HTTP server. Treat this the same as if the ClusterCatalog does not exist. Use "Unavailable" when you want to keep the ClusterCatalog but treat it as if it doesn’t exist.   
`priority` |  `integer` |  priority is an optional field that defines a priority for this ClusterCatalog.  Clients use the ClusterCatalog priority as a tie-breaker between ClusterCatalogs that meet their requirements. Higher numbers mean higher priority.  Clients decide how to handle scenarios where multiple ClusterCatalogs with the same priority meet their requirements. Clients should prompt users for additional input to break the tie.  When omitted, the default priority is 0.  Use negative numbers to specify a priority lower than the default. Use positive numbers to specify a priority higher than the default.  The lowest possible value is -2147483648. The highest possible value is 2147483647.   
`source` |  `object` |  source is a required field that defines the source of a catalog. A catalog contains information on content that can be installed on a cluster. The catalog source makes catalog contents discoverable and usable by other on-cluster components. These components can present the content in a GUI dashboard or install content from the catalog on the cluster. The catalog source must contain catalog metadata in the File-Based Catalog (FBC) format. For more information on FBC, see <https://olm.operatorframework.io/docs/reference/file-based-catalogs/#docs>.  Below is a minimal example of a ClusterCatalogSpec that sources a catalog from an image:  source: type: Image image: ref: quay.io/operatorhubio/catalog:latest   
Show more

## 3.1.2. .spec.source

Description
    

source is a required field that defines the source of a catalog. A catalog contains information on content that can be installed on a cluster. The catalog source makes catalog contents discoverable and usable by other on-cluster components. These components can present the content in a GUI dashboard or install content from the catalog on the cluster. The catalog source must contain catalog metadata in the File-Based Catalog (FBC) format. For more information on FBC, see <https://olm.operatorframework.io/docs/reference/file-based-catalogs/#docs>. 

Below is a minimal example of a ClusterCatalogSpec that sources a catalog from an image: 

```plaintext
source:
  type: Image
  image:
    ref: quay.io/operatorhubio/catalog:latest
```


Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`image` |  `object` |  image configures how catalog contents are sourced from an OCI image. It is required when type is Image, and forbidden otherwise.   
`type` |  `string` |  type is a required field that specifies the type of source for the catalog.  The only allowed value is "Image".  When set to "Image", the ClusterCatalog content is sourced from an OCI image. When using an image source, the image field must be set and must be the only field defined for this type.   
Show more

## 3.1.3. .spec.source.image

Description
     image configures how catalog contents are sourced from an OCI image. It is required when type is Image, and forbidden otherwise. 
Type
     `object`
Required
    

  * `ref`



Property| Type| Description  
---|---|---  
`pollIntervalMinutes` |  `integer` |  pollIntervalMinutes is an optional field that sets the interval, in minutes, at which the image source is polled for new content. You cannot specify pollIntervalMinutes when ref is a digest-based reference.  When omitted, the image is not polled for new content.   
`ref` |  `string` |  ref is a required field that defines the reference to a container image containing catalog contents. It cannot be more than 1000 characters.  A reference has 3 parts: the domain, name, and identifier.  The domain is typically the registry where an image is located. It must be alphanumeric characters (lowercase and uppercase) separated by the "." character. Hyphenation is allowed, but the domain must start and end with alphanumeric characters. Specifying a port to use is also allowed by adding the ":" character followed by numeric values. The port must be the last value in the domain. Some examples of valid domain values are "registry.mydomain.io", "quay.io", "my-registry.io:8080".  The name is typically the repository in the registry where an image is located. It must contain lowercase alphanumeric characters separated only by the ".", "_", "\\__", "-" characters. Multiple names can be concatenated with the "/" character. The domain and name are combined using the "/" character. Some examples of valid name values are "operatorhubio/catalog", "catalog", "my-catalog.prod". An example of the domain and name parts of a reference being combined is "quay.io/operatorhubio/catalog".  The identifier is typically the tag or digest for an image reference and is present at the end of the reference. It starts with a separator character used to distinguish the end of the name and beginning of the identifier. For a digest-based reference, the "@" character is the separator. For a tag-based reference, the ":" character is the separator. An identifier is required in the reference.  Digest-based references must contain an algorithm reference immediately after the "@" separator. The algorithm reference must be followed by the ":" character and an encoded string. The algorithm must start with an uppercase or lowercase alpha character followed by alphanumeric characters and may contain the "-", "_", "+", and "." characters. Some examples of valid algorithm values are "sha256", "sha256+b64u", "multihash+base58". The encoded string following the algorithm must be hex digits (a-f, A-F, 0-9) and must be a minimum of 32 characters.  Tag-based references must begin with a word character (alphanumeric + "\\_") followed by word characters or ".", and "-" characters. The tag must not be longer than 127 characters.  An example of a valid digest-based image reference is "quay.io/operatorhubio/catalog@sha256:200d4ddb2a73594b91358fe6397424e975205bfbe44614f5846033cad64b3f05" An example of a valid tag-based image reference is "quay.io/operatorhubio/catalog:latest"   
Show more

## 3.1.4. .status

Description
     status contains the following information about the state of the ClusterCatalog: - Whether the catalog contents are being served via the catalog content HTTP server - Whether the ClusterCatalog is progressing to a new state - A reference to the source from which the catalog contents were retrieved 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions represents the current state of this ClusterCatalog.  The current condition types are Serving and Progressing.  The Serving condition represents whether the catalog contents are being served via the HTTP(S) web server: - When status is True and reason is Available, the catalog contents are being served. - When status is False and reason is Unavailable, the catalog contents are not being served because the contents are not yet available. - When status is False and reason is UserSpecifiedUnavailable, the catalog contents are not being served because the catalog has been intentionally marked as unavailable.  The Progressing condition represents whether the ClusterCatalog is progressing or is ready to progress towards a new state: - When status is True and reason is Retrying, an error occurred that may be resolved on subsequent reconciliation attempts. - When status is True and reason is Succeeded, the ClusterCatalog has successfully progressed to a new state and is ready to continue progressing. - When status is False and reason is Blocked, an error occurred that requires manual intervention for recovery.  If the system initially fetched contents and polling identifies updates, both conditions can be active simultaneously: - The Serving condition remains True with reason Available because the previous contents are still served via the HTTP(S) web server. - The Progressing condition is True with reason Retrying because the system is working to serve the new version.   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
`lastUnpacked` |  `string` |  lastUnpacked represents the last time the catalog contents were extracted from their source format. For example, when using an Image source, the OCI image is pulled and image layers are written to a file-system backed cache. This extraction from the source format is called "unpacking".   
`resolvedSource` |  `object` |  resolvedSource contains information about the resolved source based on the source type.   
`urls` |  `object` |  urls contains the URLs that can be used to access the catalog.   
Show more

## 3.1.5. .status.conditions

Description
    

conditions represents the current state of this ClusterCatalog. 

The current condition types are Serving and Progressing. 

The Serving condition represents whether the catalog contents are being served via the HTTP(S) web server: - When status is True and reason is Available, the catalog contents are being served. - When status is False and reason is Unavailable, the catalog contents are not being served because the contents are not yet available. - When status is False and reason is UserSpecifiedUnavailable, the catalog contents are not being served because the catalog has been intentionally marked as unavailable. 

The Progressing condition represents whether the ClusterCatalog is progressing or is ready to progress towards a new state: - When status is True and reason is Retrying, an error occurred that may be resolved on subsequent reconciliation attempts. - When status is True and reason is Succeeded, the ClusterCatalog has successfully progressed to a new state and is ready to continue progressing. - When status is False and reason is Blocked, an error occurred that requires manual intervention for recovery. 

If the system initially fetched contents and polling identifies updates, both conditions can be active simultaneously: - The Serving condition remains True with reason Available because the previous contents are still served via the HTTP(S) web server. - The Progressing condition is True with reason Retrying because the system is working to serve the new version. 

Type
     `array`

## 3.1.6. .status.conditions[]

Description
     Condition contains details for one aspect of the current state of this API Resource. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `message`
  * `reason`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`message` |  `string` |  message is a human readable message indicating details about the transition. This may be an empty string.   
`observedGeneration` |  `integer` |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`reason` |  `string` |  reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase.   
Show more

## 3.1.7. .status.resolvedSource

Description
     resolvedSource contains information about the resolved source based on the source type. 
Type
     `object`
Required
    

  * `image`
  * `type`



Property| Type| Description  
---|---|---  
`image` |  `object` |  image contains resolution information for a catalog sourced from an image. It must be set when type is Image, and forbidden otherwise.   
`type` |  `string` |  type is a required field that specifies the type of source for the catalog.  The only allowed value is "Image".  When set to "Image", information about the resolved image source is set in the image field.   
Show more

## 3.1.8. .status.resolvedSource.image

Description
     image contains resolution information for a catalog sourced from an image. It must be set when type is Image, and forbidden otherwise. 
Type
     `object`
Required
    

  * `ref`



Property| Type| Description  
---|---|---  
`ref` |  `string` |  ref contains the resolved image digest-based reference. The digest format allows you to use other tooling to fetch the exact OCI manifests that were used to extract the catalog contents.   
Show more

## 3.1.9. .status.urls

Description
     urls contains the URLs that can be used to access the catalog. 
Type
     `object`
Required
    

  * `base`



Property| Type| Description  
---|---|---  
`base` |  `string` |  base is a cluster-internal URL that provides endpoints for accessing the catalog content.  Clients should append the path for the endpoint they want to access.  Currently, only a single endpoint is served and is accessible at the path /api/v1.  The endpoints served for the v1 API are: - /all - this endpoint returns the entire catalog contents in the FBC format  New endpoints may be added as needs evolve.   
Show more
