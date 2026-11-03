# 13.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration   
`status` |  `object` |  status contains the observed state of the resource.   
Show more

## 13.1.1. .spec

Description
     spec holds user settable values for configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`imageDigestMirrors` |  `array` |  imageDigestMirrors allows images referenced by image digests in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in imageDigestMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To use mirrors to pull images using tag specification, users should configure a list of mirrors using "ImageTagMirrorSet" CRD.  If the image pull specification matches the repository of "source" in multiple imagedigestmirrorset objects, only the objects which define the most specific namespace match will be used. For example, if there are objects using quay.io/libpod and quay.io/libpod/busybox as the "source", only the objects using quay.io/libpod/busybox are going to apply for pull specification quay.io/libpod/busybox. Each “source” repository is treated independently; configurations for different “source” repositories don’t interact.  If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec.  When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified. Users who want to use a specific order of mirrors, should configure them into one list of mirrors using the expected order.   
`imageDigestMirrors[]` |  `object` |  ImageDigestMirrors holds cluster-wide information about how to handle mirrors in the registries config.   
Show more

## 13.1.2. .spec.imageDigestMirrors

Description
    

imageDigestMirrors allows images referenced by image digests in pods to be pulled from alternative mirrored repository locations. The image pull specification provided to the pod will be compared to the source locations described in imageDigestMirrors and the image may be pulled down from any of the mirrors in the list instead of the specified repository allowing administrators to choose a potentially faster mirror. To use mirrors to pull images using tag specification, users should configure a list of mirrors using "ImageTagMirrorSet" CRD. 

If the image pull specification matches the repository of "source" in multiple imagedigestmirrorset objects, only the objects which define the most specific namespace match will be used. For example, if there are objects using quay.io/libpod and quay.io/libpod/busybox as the "source", only the objects using quay.io/libpod/busybox are going to apply for pull specification quay.io/libpod/busybox. Each “source” repository is treated independently; configurations for different “source” repositories don’t interact. 

If the "mirrors" is not specified, the image will continue to be pulled from the specified repository in the pull spec. 

When multiple policies are defined for the same “source” repository, the sets of defined mirrors will be merged together, preserving the relative order of the mirrors, if possible. For example, if policy A has mirrors `a, b, c` and policy B has mirrors `c, d, e`, the mirrors will be used in the order `a, b, c, d, e`. If the orders of mirror entries conflict (e.g. `a, b` vs. `b, a`) the configuration is not rejected but the resulting order is unspecified. Users who want to use a specific order of mirrors, should configure them into one list of mirrors using the expected order. 

Type
     `array`

## 13.1.3. .spec.imageDigestMirrors[]

Description
     ImageDigestMirrors holds cluster-wide information about how to handle mirrors in the registries config. 
Type
     `object`
Required
    

  * `source`



Property| Type| Description  
---|---|---  
`mirrorSourcePolicy` |  `string` |  mirrorSourcePolicy defines the fallback policy if fails to pull image from the mirrors. If unset, the image will continue to be pulled from the the repository in the pull spec. sourcePolicy is valid configuration only when one or more mirrors are in the mirror list.   
`mirrors` |  `array (string)` |  mirrors is zero or more locations that may also contain the same images. No mirror will be configured if not specified. Images can be pulled from these mirrors only if they are referenced by their digests. The mirrored location is obtained by replacing the part of the input reference that matches source by the mirrors entry, e.g. for registry.redhat.io/product/repo reference, a (source, mirror) pair *.redhat.io, mirror.local/redhat causes a mirror.local/redhat/product/repo repository to be used. The order of mirrors in this list is treated as the user’s desired priority, while source is by default considered lower priority than all mirrors. If no mirror is specified or all image pulls from the mirror list fail, the image will continue to be pulled from the repository in the pull spec unless explicitly prohibited by "mirrorSourcePolicy" Other cluster configuration, including (but not limited to) other imageDigestMirrors objects, may impact the exact order mirrors are contacted in, or some mirrors may be contacted in parallel, so this should be considered a preference rather than a guarantee of ordering. "mirrors" uses one of the following formats: host[:port] host[:port]/namespace[/namespace…] host[:port]/namespace[/namespace…]/repo for more information about the format, see the document about the location field: <https://github.com/containers/image/blob/main/docs/containers-registries.conf.5.md#choosing-a-registry-toml-table>  
`source` |  `string` |  source matches the repository that users refer to, e.g. in image pull specifications. Setting source to a registry hostname e.g. docker.io. quay.io, or registry.redhat.io, will match the image pull specification of corressponding registry. "source" uses one of the following formats: host[:port] host[:port]/namespace[/namespace…] host[:port]/namespace[/namespace…]/repo [*.]host for more information about the format, see the document about the location field: <https://github.com/containers/image/blob/main/docs/containers-registries.conf.5.md#choosing-a-registry-toml-table>  
Show more

## 13.1.4. .status

Description
     status contains the observed state of the resource. 
Type
     `object`
