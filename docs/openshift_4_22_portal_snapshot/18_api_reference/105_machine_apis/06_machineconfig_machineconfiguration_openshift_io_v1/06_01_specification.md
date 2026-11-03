# 6.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  MachineConfigSpec is the spec for MachineConfig   
Show more

## 6.1.1. .spec

Description
     MachineConfigSpec is the spec for MachineConfig 
Type
     `object`

Property| Type| Description  
---|---|---  
`baseOSExtensionsContainerImage` |  `string` |  baseOSExtensionsContainerImage specifies the remote location that will be used to fetch the extensions container matching a new-format OS image   
`config` |  ``  |  config is a Ignition Config object.   
`extensions` |  `array (string)` |  extensions contains a list of additional features that can be enabled on host   
`fips` |  `boolean` |  fips controls FIPS mode   
`kernelArguments` |  ``  |  kernelArguments contains a list of kernel arguments to be added   
`kernelType` |  `string` |  kernelType contains which kernel we want to be running like default (traditional), realtime, 64k-pages (aarch64 only).   
`osImageURL` |  `string` |  osImageURL specifies the remote location that will be used to fetch the OS.   
Show more
