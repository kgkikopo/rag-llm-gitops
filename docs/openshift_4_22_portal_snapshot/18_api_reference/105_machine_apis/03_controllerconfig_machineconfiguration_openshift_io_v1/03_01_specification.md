# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec contains the desired controller config configuration.   
`status` |  `object` |  status contains observed information about the controller config.   
Show more

## 3.1.1. .spec

Description
     spec contains the desired controller config configuration. 
Type
     `object`
Required
    

  * `baseOSContainerImage`
  * `cloudProviderConfig`
  * `clusterDNSIP`
  * `images`
  * `ipFamilies`
  * `kubeAPIServerServingCAData`
  * `releaseImage`
  * `rootCAData`



Property| Type| Description  
---|---|---  
`additionalTrustBundle` |  ``  |  additionalTrustBundle is a certificate bundle that will be added to the nodes trusted certificate store.   
`baseOSContainerImage` |  `string` |  baseOSContainerImage is the new-format container image for operating system updates.   
`baseOSExtensionsContainerImage` |  `string` |  baseOSExtensionsContainerImage is the matching extensions container for the new-format container   
`cloudProviderCAData` |  ``  |  cloudProviderCAData specifies the cloud provider CA data   
`cloudProviderConfig` |  `string` |  cloudProviderConfig is the configuration for the given cloud provider   
`clusterDNSIP` |  `string` |  clusterDNSIP is the cluster DNS IP address   
`dns` |  `object` |  dns holds the cluster dns details   
`etcdDiscoveryDomain` |  `string` |  etcdDiscoveryDomain is deprecated, use Infra.Status.EtcdDiscoveryDomain instead   
`imageRegistryBundleData` |  `array` |  imageRegistryBundleData is the ImageRegistryData   
`imageRegistryBundleData[]` |  `object` |  ImageRegistryBundle contains information for writing image registry certificates   
`imageRegistryBundleUserData` |  `array` |  imageRegistryBundleUserData is Image Registry Data provided by the user   
`imageRegistryBundleUserData[]` |  `object` |  ImageRegistryBundle contains information for writing image registry certificates   
`images` |  `object (string)` |  images is map of images that are used by the controller to render templates under ./templates/   
`infra` |  `object` |  infra holds the infrastructure details   
`internalRegistryPullSecret` |  ``  |  internalRegistryPullSecret is the pull secret for the internal registry, used by rpm-ostree to pull images from the internal registry if present   
`ipFamilies` |  `string` |  ipFamilies indicates the IP families in use by the cluster network   
`kubeAPIServerServingCAData` |  `string` |  kubeAPIServerServingCAData managed Kubelet to API Server Cert…​ Rotated automatically   
`network` |  ``  |  network contains additional network related information   
`networkType` |  `string` |  networkType holds the type of network the cluster is using XXX: this is temporary and will be dropped as soon as possible in favor of a better support to start network related services the proper way. Nobody is also changing this once the cluster is up and running the first time, so, disallow regeneration if this changes.   
`osImageURL` |  `string` |  osImageURL is the old-format container image that contains the OS update payload.   
`platform` |  `string` |  platform is deprecated, use Infra.Status.PlatformStatus.Type instead   
`proxy` |  ``  |  proxy holds the current proxy configuration for the nodes   
`pullSecret` |  `object` |  pullSecret is the default pull secret that needs to be installed on all machines.   
`releaseImage` |  `string` |  releaseImage is the image used when installing the cluster   
`rootCAData` |  `string` |  rootCAData specifies the root CA data   
Show more

## 3.1.2. .spec.dns

Description
     dns holds the cluster dns details 
Type
     `object`
Required
    

  * `spec`
  * `kind`
  * `apiVersion`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  apiVersion defines the versioned schema of this representation of an object. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  kind is a string value representing the type of this object. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
Show more

## 3.1.3. .spec.imageRegistryBundleData

Description
     imageRegistryBundleData is the ImageRegistryData 
Type
     `array`

## 3.1.4. .spec.imageRegistryBundleData[]

Description
     ImageRegistryBundle contains information for writing image registry certificates 
Type
     `object`
Required
    

  * `data`
  * `file`



Property| Type| Description  
---|---|---  
`data` |  `string` |  data holds the contents of the bundle that will be written to the file location   
`file` |  `string` |  file holds the name of the file where the bundle will be written to disk   
Show more

## 3.1.5. .spec.imageRegistryBundleUserData

Description
     imageRegistryBundleUserData is Image Registry Data provided by the user 
Type
     `array`

## 3.1.6. .spec.imageRegistryBundleUserData[]

Description
     ImageRegistryBundle contains information for writing image registry certificates 
Type
     `object`
Required
    

  * `data`
  * `file`



Property| Type| Description  
---|---|---  
`data` |  `string` |  data holds the contents of the bundle that will be written to the file location   
`file` |  `string` |  file holds the name of the file where the bundle will be written to disk   
Show more

## 3.1.7. .spec.infra

Description
     infra holds the infrastructure details 
Type
     `object`
Required
    

  * `spec`
  * `kind`
  * `apiVersion`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  apiVersion defines the versioned schema of this representation of an object. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  kind is a string value representing the type of this object. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
Show more

## 3.1.8. .spec.pullSecret

Description
     pullSecret is the default pull secret that needs to be installed on all machines. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`fieldPath` |  `string` |  If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`namespace` |  `string` |  Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>  
`resourceVersion` |  `string` |  Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency>  
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids>  
Show more

## 3.1.9. .status

Description
     status contains observed information about the controller config. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions represents the latest available observations of current state.   
`conditions[]` |  `object` |  ControllerConfigStatusCondition contains condition information for ControllerConfigStatus   
`controllerCertificates` |  `array` |  controllerCertificates represents the latest available observations of the automatically rotating certificates in the MCO.   
`controllerCertificates[]` |  `object` |  ControllerCertificate contains info about a specific cert.   
`observedGeneration` |  `integer` |  observedGeneration represents the generation observed by the controller.   
Show more

## 3.1.10. .status.conditions

Description
     conditions represents the latest available observations of current state. 
Type
     `array`

## 3.1.11. .status.conditions[]

Description
     ControllerConfigStatusCondition contains condition information for ControllerConfigStatus 
Type
     `object`
Required
    

  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  ``  |  lastTransitionTime is the time of the last update to the current status object.   
`message` |  `string` |  message provides additional information about the current condition. This is only to be consumed by humans.   
`reason` |  `string` |  reason is the reason for the condition’s last transition. Reasons are PascalCase   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type specifies the state of the operator’s reconciliation functionality.   
Show more

## 3.1.12. .status.controllerCertificates

Description
     controllerCertificates represents the latest available observations of the automatically rotating certificates in the MCO. 
Type
     `array`

## 3.1.13. .status.controllerCertificates[]

Description
     ControllerCertificate contains info about a specific cert. 
Type
     `object`
Required
    

  * `bundleFile`
  * `signer`
  * `subject`



Property| Type| Description  
---|---|---  
`bundleFile` |  `string` |  bundleFile is the larger bundle a cert comes from   
`notAfter` |  `string` |  notAfter is the upper boundary for validity   
`notBefore` |  `string` |  notBefore is the lower boundary for validity   
`signer` |  `string` |  signer is the cert Issuer   
`subject` |  `string` |  subject is the cert subject   
Show more
