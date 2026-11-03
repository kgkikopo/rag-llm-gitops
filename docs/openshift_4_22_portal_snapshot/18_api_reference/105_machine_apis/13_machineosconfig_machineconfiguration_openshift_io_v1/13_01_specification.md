# 13.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec describes the configuration of the machineosconfig   
`status` |  `object` |  status describes the status of the machineosconfig   
Show more

## 13.1.1. .spec

Description
     spec describes the configuration of the machineosconfig 
Type
     `object`
Required
    

  * `imageBuilder`
  * `machineConfigPool`
  * `renderedImagePushSecret`
  * `renderedImagePushSpec`



Property| Type| Description  
---|---|---  
`baseImagePullSecret` |  `object` |  baseImagePullSecret is the secret used to pull the base image. Must live in the openshift-machine-config-operator namespace if provided. Defaults to using the cluster-wide pull secret if not specified. This is provided during install time of the cluster, and lives in the openshift-config namespace as a secret.   
`containerFile` |  `array` |  containerFile describes the custom data the user has specified to build into the image. This is also commonly called a Dockerfile and you can treat it as such. The content is the content of your Dockerfile. See <https://github.com/containers/common/blob/main/docs/Containerfile.5.md> for the spec reference. This is a list indexed by architecture name (e.g. AMD64), and allows specifying one containerFile per arch, up to 4.   
`containerFile[]` |  `object` |  MachineOSContainerfile contains all custom content the user wants built into the image   
`imageBuilder` |  `object` |  imageBuilder describes which image builder will be used in each build triggered by this MachineOSConfig. Currently supported type(s): Job   
`machineConfigPool` |  `object` |  machineConfigPool is the pool which the build is for. The Machine Config Operator will perform the build and roll out the built image to the specified pool.   
`renderedImagePushSecret` |  `object` |  renderedImagePushSecret is the secret used to connect to a user registry. The final image push and pull secrets should be separate and assume the principal of least privilege. The push secret with write privilege is only required to be present on the node hosting the MachineConfigController pod. The pull secret with read only privileges is required on all nodes. By separating the two secrets, the risk of write credentials becoming compromised is reduced.   
`renderedImagePushSpec` |  `string` |  renderedImagePushSpec describes the location of the final image. The MachineOSConfig object will use the in cluster image registry configuration. If you wish to use a mirror or any other settings specific to registries.conf, please specify those in the cluster wide registries.conf via the cluster image.config, ImageContentSourcePolicies, ImageDigestMirrorSet, or ImageTagMirrorSet objects. The format of the image push spec is: host[:port][/namespace]/name:<tag> or svc_name.namespace.svc[:port]/repository/name:<tag>. The length of the push spec must be between 1 to 447 characters.   
Show more

## 13.1.2. .spec.baseImagePullSecret

Description
     baseImagePullSecret is the secret used to pull the base image. Must live in the openshift-machine-config-operator namespace if provided. Defaults to using the cluster-wide pull secret if not specified. This is provided during install time of the cluster, and lives in the openshift-config namespace as a secret. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the secret used to push or pull this MachineOSConfig object. Must consist of lower case alphanumeric characters, '-' or '.', and must start and end with an alphanumeric character. This secret must be in the openshift-machine-config-operator namespace.   
Show more

## 13.1.3. .spec.containerFile

Description
     containerFile describes the custom data the user has specified to build into the image. This is also commonly called a Dockerfile and you can treat it as such. The content is the content of your Dockerfile. See <https://github.com/containers/common/blob/main/docs/Containerfile.5.md> for the spec reference. This is a list indexed by architecture name (e.g. AMD64), and allows specifying one containerFile per arch, up to 4. 
Type
     `array`

## 13.1.4. .spec.containerFile[]

Description
     MachineOSContainerfile contains all custom content the user wants built into the image 
Type
     `object`
Required
    

  * `content`



Property| Type| Description  
---|---|---  
`containerfileArch` |  `string` |  containerfileArch describes the architecture this containerfile is to be built for. This arch is optional. If the user does not specify an architecture, it is assumed that the content can be applied to all architectures, or in a single arch cluster: the only architecture.   
`content` |  `string` |  content is an embedded Containerfile/Dockerfile that defines the contents to be built into your image. See <https://github.com/containers/common/blob/main/docs/Containerfile.5.md> for the spec reference. for example, this would add the tree package to your hosts: FROM configs AS final RUN rpm-ostree install tree && \ ostree container commit This is a required field and can have a maximum length of **4096** characters.   
Show more

## 13.1.5. .spec.imageBuilder

Description
     imageBuilder describes which image builder will be used in each build triggered by this MachineOSConfig. Currently supported type(s): Job 
Type
     `object`
Required
    

  * `imageBuilderType`



Property| Type| Description  
---|---|---  
`imageBuilderType` |  `string` |  imageBuilderType specifies the backend to be used to build the image. Valid options are: Job   
Show more

## 13.1.6. .spec.machineConfigPool

Description
     machineConfigPool is the pool which the build is for. The Machine Config Operator will perform the build and roll out the built image to the specified pool. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name of the MachineConfigPool object. This value should be at most 253 characters, and must contain only lowercase alphanumeric characters, hyphens and periods, and should start and end with an alphanumeric character.   
Show more

## 13.1.7. .spec.renderedImagePushSecret

Description
     renderedImagePushSecret is the secret used to connect to a user registry. The final image push and pull secrets should be separate and assume the principal of least privilege. The push secret with write privilege is only required to be present on the node hosting the MachineConfigController pod. The pull secret with read only privileges is required on all nodes. By separating the two secrets, the risk of write credentials becoming compromised is reduced. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the secret used to push or pull this MachineOSConfig object. Must consist of lower case alphanumeric characters, '-' or '.', and must start and end with an alphanumeric character. This secret must be in the openshift-machine-config-operator namespace.   
Show more

## 13.1.8. .status

Description
     status describes the status of the machineosconfig 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions are state related conditions for the object.   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
`currentImagePullSpec` |  `string` |  currentImagePullSpec is the fully qualified image pull spec used by the MCO to pull down the new OSImage. This includes the sha256 image digest. This is generated when the Machine Config Operator’s build controller successfully completes the build, and is populated from the corresponding MachineOSBuild object’s FinalImagePushSpec. This may change after completion in reaction to spec changes that would cause a new image build, but will not be removed. The format of the image pull spec is: host[:port][/namespace]/name@sha256:<digest>, where the digest must be 64 characters long, and consist only of lowercase hexadecimal characters, a-f and 0-9. The length of the whole spec must be between 1 to 447 characters.   
`machineOSBuild` |  `object` |  machineOSBuild is a reference to the MachineOSBuild object for this MachineOSConfig, which contains the status for the image build.   
`observedGeneration` |  `integer` |  observedGeneration represents the generation of the MachineOSConfig object observed by the Machine Config Operator’s build controller.   
Show more

## 13.1.9. .status.conditions

Description
     conditions are state related conditions for the object. 
Type
     `array`

## 13.1.10. .status.conditions[]

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

## 13.1.11. .status.machineOSBuild

Description
     machineOSBuild is a reference to the MachineOSBuild object for this MachineOSConfig, which contains the status for the image build. 
Type
     `object`
Required
    

  * `group`
  * `name`
  * `resource`



Property| Type| Description  
---|---|---  
`group` |  `string` |  group of the referent. The name must contain only lowercase alphanumeric characters, '-' or '.' and start/end with an alphanumeric character. Example: "", "apps", "build.openshift.io", etc.   
`name` |  `string` |  name of the referent. The name must contain only lowercase alphanumeric characters, '-' or '.' and start/end with an alphanumeric character.   
`namespace` |  `string` |  namespace of the referent. This value should consist of at most 63 characters, and of only lowercase alphanumeric characters and hyphens, and should start and end with an alphanumeric character.   
`resource` |  `string` |  resource of the referent. This value should consist of at most 63 characters, and of only lowercase alphanumeric characters and hyphens, and should start with an alphabetic character and end with an alphanumeric character. Example: "deployments", "deploymentconfigs", "pods", etc.   
Show more
