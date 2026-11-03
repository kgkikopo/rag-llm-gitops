# 12.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |   
`spec` |  `object` |  PackageManifestSpec defines the desired state of PackageManifest   
`status` |  `object` |  PackageManifestStatus represents the current status of the PackageManifest   
Show more

## 12.1.1. .spec

Description
     PackageManifestSpec defines the desired state of PackageManifest 
Type
     `object`

## 12.1.2. .status

Description
     PackageManifestStatus represents the current status of the PackageManifest 
Type
     `object`
Required
    

  * `catalogSource`
  * `catalogSourceDisplayName`
  * `catalogSourcePublisher`
  * `catalogSourceNamespace`
  * `packageName`
  * `channels`
  * `defaultChannel`



Property| Type| Description  
---|---|---  
`catalogSource` |  `string` |  CatalogSource is the name of the CatalogSource this package belongs to   
`catalogSourceDisplayName` |  `string` |   
`catalogSourceNamespace` |  `string` |  CatalogSourceNamespace is the namespace of the owning CatalogSource   
`catalogSourcePublisher` |  `string` |   
`channels` |  `array` |  Channels are the declared channels for the package, ala `stable` or `alpha`.   
`channels[]` |  `object` |  PackageChannel defines a single channel under a package, pointing to a version of that package.   
`defaultChannel` |  `string` |  DefaultChannel is, if specified, the name of the default channel for the package. The default channel will be installed if no other channel is explicitly given. If the package has a single channel, then that channel is implicitly the default.   
`deprecation` |  `object` |  Deprecation conveys information regarding a deprecated resource.   
`packageName` |  `string` |  PackageName is the name of the overall package, ala `etcd`.   
`provider` |  `object` |  AppLink defines a link to an application   
Show more

## 12.1.3. .status.channels

Description
     Channels are the declared channels for the package, ala `stable` or `alpha`. 
Type
     `array`

## 12.1.4. .status.channels[]

Description
     PackageChannel defines a single channel under a package, pointing to a version of that package. 
Type
     `object`
Required
    

  * `name`
  * `currentCSV`
  * `entries`



Property| Type| Description  
---|---|---  
`currentCSV` |  `string` |  CurrentCSV defines a reference to the CSV holding the version of this package currently for the channel.   
`currentCSVDesc` |  `object` |  CSVDescription defines a description of a CSV   
`deprecation` |  `object` |  Deprecation conveys information regarding a deprecated resource.   
`entries` |  `array` |  Entries lists all CSVs in the channel, with their upgrade edges.   
`entries[]` |  `object` |  ChannelEntry defines a member of a package channel.   
`name` |  `string` |  Name is the name of the channel, e.g. `alpha` or `stable`  
Show more

## 12.1.5. .status.channels[].currentCSVDesc

Description
     CSVDescription defines a description of a CSV 
Type
     `object`

Property| Type| Description  
---|---|---  
`annotations` |  `object (string)` |   
`apiservicedefinitions` |  [`APIServiceDefinitions`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-operator-framework-api-pkg-operators-v1alpha1-APIServiceDefinitions) |   
`customresourcedefinitions` |  [`CustomResourceDefinitions`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-operator-framework-api-pkg-operators-v1alpha1-CustomResourceDefinitions) |   
`description` |  `string` |  LongDescription is the CSV’s description   
`displayName` |  `string` |  DisplayName is the CSV’s display name   
`icon` |  `array` |  Icon is the CSV’s base64 encoded icon   
`icon[]` |  `object` |  Icon defines a base64 encoded icon and media type   
`installModes` |  [`array (InstallMode)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-operator-framework-api-pkg-operators-v1alpha1-InstallMode) |  InstallModes specify supported installation types   
`keywords` |  `array (string)` |   
`links` |  `array` |   
`links[]` |  `object` |  AppLink defines a link to an application   
`maintainers` |  `array` |   
`maintainers[]` |  `object` |  Maintainer defines a project maintainer   
`maturity` |  `string` |   
`minKubeVersion` |  `string` |  Minimum Kubernetes version for operator installation   
`nativeApis` |  [`array (GroupVersionKind)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-GroupVersionKind) |   
`provider` |  `object` |  AppLink defines a link to an application   
`relatedImages` |  `array (string)` |  List of related images   
`version` |  [`OperatorVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-operator-framework-api-pkg-operators-lib-version-OperatorVersion) |  Version is the CSV’s semantic version   
Show more

## 12.1.6. .status.channels[].currentCSVDesc.icon

Description
     Icon is the CSV’s base64 encoded icon 
Type
     `array`

## 12.1.7. .status.channels[].currentCSVDesc.icon[]

Description
     Icon defines a base64 encoded icon and media type 
Type
     `object`

Property| Type| Description  
---|---|---  
`base64data` |  `string` |   
`mediatype` |  `string` |   
Show more

## 12.1.8. .status.channels[].currentCSVDesc.links

Description
    
Type
     `array`

## 12.1.9. .status.channels[].currentCSVDesc.links[]

Description
     AppLink defines a link to an application 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |   
`url` |  `string` |   
Show more

## 12.1.10. .status.channels[].currentCSVDesc.maintainers

Description
    
Type
     `array`

## 12.1.11. .status.channels[].currentCSVDesc.maintainers[]

Description
     Maintainer defines a project maintainer 
Type
     `object`

Property| Type| Description  
---|---|---  
`email` |  `string` |   
`name` |  `string` |   
Show more

## 12.1.12. .status.channels[].currentCSVDesc.provider

Description
     AppLink defines a link to an application 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |   
`url` |  `string` |   
Show more

## 12.1.13. .status.channels[].deprecation

Description
     Deprecation conveys information regarding a deprecated resource. 
Type
     `object`
Required
    

  * `message`



Property| Type| Description  
---|---|---  
`message` |  `string` |  Message is a human readable message describing the deprecation.   
Show more

## 12.1.14. .status.channels[].entries

Description
     Entries lists all CSVs in the channel, with their upgrade edges. 
Type
     `array`

## 12.1.15. .status.channels[].entries[]

Description
     ChannelEntry defines a member of a package channel. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`deprecation` |  `object` |  Deprecation conveys information regarding a deprecated resource.   
`name` |  `string` |  Name is the name of the bundle for this entry.   
`version` |  `string` |  Version is the version of the bundle for this entry.   
Show more

## 12.1.16. .status.channels[].entries[].deprecation

Description
     Deprecation conveys information regarding a deprecated resource. 
Type
     `object`
Required
    

  * `message`



Property| Type| Description  
---|---|---  
`message` |  `string` |  Message is a human readable message describing the deprecation.   
Show more

## 12.1.17. .status.deprecation

Description
     Deprecation conveys information regarding a deprecated resource. 
Type
     `object`
Required
    

  * `message`



Property| Type| Description  
---|---|---  
`message` |  `string` |  Message is a human readable message describing the deprecation.   
Show more

## 12.1.18. .status.provider

Description
     AppLink defines a link to an application 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |   
`url` |  `string` |   
Show more
