# 1.27. com.github.openshift.api.image.v1.ImageTagList schema

Description
    

ImageTagList is a list of ImageTag objects. When listing image tags, the image field is not populated. Tags are returned in alphabetical order by image stream and then tag. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `items`



## 1.27.1. Schema

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`items` |  [`array (ImageTag)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagetag-image-openshift-io-v1) |  items is the list of image stream tags   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ListMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta "1.140. io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema") |  metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
Show more
