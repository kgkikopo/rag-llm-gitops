# 12.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration   
`status` |  `object` |  status holds observed values from the cluster. They may not be overridden.   
Show more

## 12.1.1. .spec

Description
     spec holds user settable values for configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`additionalTrustedCA` |  `object` |  additionalTrustedCA is a reference to a ConfigMap containing additional CAs that should be trusted during imagestream import, pod image pull, build image pull, and imageregistry pullthrough. The namespace for this config map is openshift-config.   
`allowedRegistriesForImport` |  `array` |  allowedRegistriesForImport limits the container image registries that normal users may import images from. Set this list to the registries that you trust to contain valid Docker images and that you want applications to be able to import from. Users with permission to create Images or ImageStreamMappings via the API are not affected by this policy - typically only administrators or system integrations will have those permissions.   
`allowedRegistriesForImport[]` |  `object` |  RegistryLocation contains a location of the registry specified by the registry domain name. The domain name might include wildcards, like '*' or '??'.   
`externalRegistryHostnames` |  `array (string)` |  externalRegistryHostnames provides the hostnames for the default external image registry. The external hostname should be set only when the image registry is exposed externally. The first value is used in 'publicDockerImageRepository' field in ImageStreams. The value must be in "hostname[:port]" format.   
`imageStreamImportMode` |  `string` |  imageStreamImportMode controls the import mode behaviour of imagestreams. It can be set to `Legacy` or `PreserveOriginal` or the empty string. If this value is specified, this setting is applied to all newly created imagestreams which do not have the value set. `Legacy` indicates that the legacy behaviour should be used. For manifest lists, the legacy behaviour will discard the manifest list and import a single sub-manifest. In this case, the platform is chosen in the following order of priority: 1. tag annotations; 2. control plane arch/os; 3. linux/amd64; 4. the first manifest in the list. `PreserveOriginal` indicates that the original manifest will be preserved. For manifest lists, the manifest list and all its sub-manifests will be imported. When empty, the behaviour will be decided based on the payload type advertised by the ClusterVersion status, i.e single arch payload implies the import mode is Legacy and multi payload implies PreserveOriginal.   
`registrySources` |  `object` |  registrySources contains configuration that determines how the container runtime should treat individual registries when accessing images for builds+pods. (e.g. whether or not to allow insecure access). It does not contain configuration for the internal cluster registry.   
Show more

## 12.1.2. .spec.additionalTrustedCA

Description
     additionalTrustedCA is a reference to a ConfigMap containing additional CAs that should be trusted during imagestream import, pod image pull, build image pull, and imageregistry pullthrough. The namespace for this config map is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced config map   
Show more

## 12.1.3. .spec.allowedRegistriesForImport

Description
     allowedRegistriesForImport limits the container image registries that normal users may import images from. Set this list to the registries that you trust to contain valid Docker images and that you want applications to be able to import from. Users with permission to create Images or ImageStreamMappings via the API are not affected by this policy - typically only administrators or system integrations will have those permissions. 
Type
     `array`

## 12.1.4. .spec.allowedRegistriesForImport[]

Description
     RegistryLocation contains a location of the registry specified by the registry domain name. The domain name might include wildcards, like '*' or '??'. 
Type
     `object`

Property| Type| Description  
---|---|---  
`domainName` |  `string` |  domainName specifies a domain name for the registry In case the registry use non-standard (80 or 443) port, the port should be included in the domain name as well.   
`insecure` |  `boolean` |  insecure indicates whether the registry is secure (https) or insecure (http) By default (if not specified) the registry is assumed as secure.   
Show more

## 12.1.5. .spec.registrySources

Description
     registrySources contains configuration that determines how the container runtime should treat individual registries when accessing images for builds+pods. (e.g. whether or not to allow insecure access). It does not contain configuration for the internal cluster registry. 
Type
     `object`

Property| Type| Description  
---|---|---  
`allowedRegistries` |  `array (string)` |  allowedRegistries are the only registries permitted for image pull and push actions. All other registries are denied.  Only one of BlockedRegistries or AllowedRegistries may be set.   
`blockedRegistries` |  `array (string)` |  blockedRegistries cannot be used for image pull and push actions. All other registries are permitted.  Only one of BlockedRegistries or AllowedRegistries may be set.   
`containerRuntimeSearchRegistries` |  `array (string)` |  containerRuntimeSearchRegistries are registries that will be searched when pulling images that do not have fully qualified domains in their pull specs. Registries will be searched in the order provided in the list. Note: this search list only works with the container runtime, i.e CRI-O. Will NOT work with builds or imagestream imports.   
`insecureRegistries` |  `array (string)` |  insecureRegistries are registries which do not have a valid TLS certificates or only support HTTP connections.   
Show more

## 12.1.6. .status

Description
     status holds observed values from the cluster. They may not be overridden. 
Type
     `object`

Property| Type| Description  
---|---|---  
`externalRegistryHostnames` |  `array (string)` |  externalRegistryHostnames provides the hostnames for the default external image registry. The external hostname should be set only when the image registry is exposed externally. The first value is used in 'publicDockerImageRepository' field in ImageStreams. The value must be in "hostname[:port]" format.   
`imageStreamImportMode` |  `string` |  imageStreamImportMode controls the import mode behaviour of imagestreams. It can be `Legacy` or `PreserveOriginal`. `Legacy` indicates that the legacy behaviour should be used. For manifest lists, the legacy behaviour will discard the manifest list and import a single sub-manifest. In this case, the platform is chosen in the following order of priority: 1. tag annotations; 2. control plane arch/os; 3. linux/amd64; 4. the first manifest in the list. `PreserveOriginal` indicates that the original manifest will be preserved. For manifest lists, the manifest list and all its sub-manifests will be imported. This value will be reconciled based on either the spec value or if no spec value is specified, the image registry operator would look at the ClusterVersion status to determine the payload type and set the import mode accordingly, i.e single arch payload implies the import mode is Legacy and multi payload implies PreserveOriginal.   
`internalRegistryHostname` |  `string` |  internalRegistryHostname sets the hostname for the default internal image registry. The value must be in "hostname[:port]" format. This value is set by the image registry operator which controls the internal registry hostname.   
Show more
