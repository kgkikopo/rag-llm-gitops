# 14.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration   
Show more

## 14.1.1. .spec

Description
     spec holds user settable values for configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`repositoryDigestMirrors` |  `array` |  repositoryDigestMirrors allows images referenced by image digests in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in RepositoryDigestMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To pull image from mirrors by tags, should set the "allowMirrorByTags".  Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.  If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec.  When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified.   
`repositoryDigestMirrors[]` |  `object` |  RepositoryDigestMirrors holds cluster-wide information about how to handle mirrors in the registries config.   
Show more

## 14.1.2. .spec.repositoryDigestMirrors

Description
    

repositoryDigestMirrors allows images referenced by image digests in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in RepositoryDigestMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To pull image from mirrors by tags, should set the "allowMirrorByTags". 

Each “source” repository is treated independently; configurations for different “source” repositories don’t interact. 

If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec. 

When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified. 

Type
     `array`

## 14.1.3. .spec.repositoryDigestMirrors[]

Description
     RepositoryDigestMirrors holds cluster-wide information about how to handle mirrors in the registries config. 
Type
     `object`
Required
    

  * `source`



Property| Type| Description  
---|---|---  
`allowMirrorByTags` |  `boolean` |  allowMirrorByTags if true, the mirrors can be used to pull the images that are referenced by their tags. Default is false, the mirrors only work when pulling the images that are referenced by their digests. Pulling images by tag can potentially yield different images, depending on which endpoint we pull from. Forcing digest-pulls for mirrors avoids that issue.   
`mirrors` |  `array (string)` |  mirrors is zero or more repositories that may also contain the same images. If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec. No mirror will be configured. The order of mirrors in this list is treated as the user’s desired priority, while source is by default considered lower priority than all mirrors. Other cluster configuration, including (but not limited to) other repositoryDigestMirrors objects, may impact the exact order mirrors are contacted in, or some mirrors may be contacted in parallel, so this should be considered a preference rather than a guarantee of ordering.   
`source` |  `string` |  source is the repository that users refer to, e.g. in image pull specifications.   
Show more
