# 14.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec describes the configuration of this pinned image set.   
Show more

## 14.1.1. .spec

Description
     spec describes the configuration of this pinned image set. 
Type
     `object`
Required
    

  * `pinnedImages`



Property| Type| Description  
---|---|---  
`pinnedImages` |  `array` |  pinnedImages is a list of OCI Image referenced by digest that should be pinned and pre-loaded by the nodes of a MachineConfigPool. Translates into a new file inside the /etc/crio/crio.conf.d directory with content similar to this:  pinned_images = [ "quay.io/openshift-release-dev/ocp-release@sha256:…​", "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:…​", "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:…​", …​ ]  Image references must be by digest. A maximum of 500 images may be specified.   
`pinnedImages[]` |  `object` |  PinnedImageRef represents a reference to an OCI image   
Show more

## 14.1.2. .spec.pinnedImages

Description
    

pinnedImages is a list of OCI Image referenced by digest that should be pinned and pre-loaded by the nodes of a MachineConfigPool. Translates into a new file inside the /etc/crio/crio.conf.d directory with content similar to this: 

```plaintext
pinned_images = [
        "quay.io/openshift-release-dev/ocp-release@sha256:...",
        "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:...",
        "quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:...",
        ...
]
```


Image references must be by digest. A maximum of 500 images may be specified. 

Type
     `array`

## 14.1.3. .spec.pinnedImages[]

Description
     PinnedImageRef represents a reference to an OCI image 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is an OCI Image referenced by digest. The format of the image pull spec is: host[:port][/namespace]/name@sha256:<digest>, where the digest must be 64 characters long, and consist only of lowercase hexadecimal characters, a-f and 0-9. The length of the whole spec must be between 1 to 447 characters.   
Show more
