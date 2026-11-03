# 23.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  OperatorHubSpec defines the desired state of OperatorHub   
`status` |  `object` |  OperatorHubStatus defines the observed state of OperatorHub. The current state of the default hub sources will always be reflected here.   
Show more

## 23.1.1. .spec

Description
     OperatorHubSpec defines the desired state of OperatorHub 
Type
     `object`

Property| Type| Description  
---|---|---  
`disableAllDefaultSources` |  `boolean` |  disableAllDefaultSources allows you to disable all the default hub sources. If this is true, a specific entry in sources can be used to enable a default source. If this is false, a specific entry in sources can be used to disable or enable a default source.   
`sources` |  `array` |  sources is the list of default hub sources and their configuration. If the list is empty, it implies that the default hub sources are enabled on the cluster unless disableAllDefaultSources is true. If disableAllDefaultSources is true and sources is not empty, the configuration present in sources will take precedence. The list of default hub sources and their current state will always be reflected in the status block.   
`sources[]` |  `object` |  HubSource is used to specify the hub source and its configuration   
Show more

## 23.1.2. .spec.sources

Description
     sources is the list of default hub sources and their configuration. If the list is empty, it implies that the default hub sources are enabled on the cluster unless disableAllDefaultSources is true. If disableAllDefaultSources is true and sources is not empty, the configuration present in sources will take precedence. The list of default hub sources and their current state will always be reflected in the status block. 
Type
     `array`

## 23.1.3. .spec.sources[]

Description
     HubSource is used to specify the hub source and its configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`disabled` |  `boolean` |  disabled is used to disable a default hub source on cluster   
`name` |  `string` |  name is the name of one of the default hub sources   
Show more

## 23.1.4. .status

Description
     OperatorHubStatus defines the observed state of OperatorHub. The current state of the default hub sources will always be reflected here. 
Type
     `object`

Property| Type| Description  
---|---|---  
`sources` |  `array` |  sources encapsulates the result of applying the configuration for each hub source   
`sources[]` |  `object` |  HubSourceStatus is used to reflect the current state of applying the configuration to a default source   
Show more

## 23.1.5. .status.sources

Description
     sources encapsulates the result of applying the configuration for each hub source 
Type
     `array`

## 23.1.6. .status.sources[]

Description
     HubSourceStatus is used to reflect the current state of applying the configuration to a default source 
Type
     `object`

Property| Type| Description  
---|---|---  
`disabled` |  `boolean` |  disabled is used to disable a default hub source on cluster   
`message` |  `string` |  message provides more information regarding failures   
`name` |  `string` |  name is the name of one of the default hub sources   
`status` |  `string` |  status indicates success or failure in applying the configuration   
Show more
