# 6.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  InstallPlanSpec defines a set of Application resources to be installed   
`status` |  `object` |  InstallPlanStatus represents the information about the status of steps required to complete installation.  Status may trail the actual state of a system.   
Show more

## 6.1.1. .spec

Description
     InstallPlanSpec defines a set of Application resources to be installed 
Type
     `object`
Required
    

  * `approval`
  * `approved`
  * `clusterServiceVersionNames`



Property| Type| Description  
---|---|---  
`approval` |  `string` |  Approval is the user approval policy for an InstallPlan. It must be one of "Automatic" or "Manual".   
`approved` |  `boolean` |   
`clusterServiceVersionNames` |  `array (string)` |   
`generation` |  `integer` |   
`source` |  `string` |   
`sourceNamespace` |  `string` |   
Show more

## 6.1.2. .status

Description
    

InstallPlanStatus represents the information about the status of steps required to complete installation. 

Status may trail the actual state of a system. 

Type
     `object`
Required
    

  * `catalogSources`
  * `phase`



Property| Type| Description  
---|---|---  
`attenuatedServiceAccountRef` |  `object` |  AttenuatedServiceAccountRef references the service account that is used to do scoped operator install.   
`bundleLookups` |  `array` |  BundleLookups is the set of in-progress requests to pull and unpackage bundle content to the cluster.   
`bundleLookups[]` |  `object` |  BundleLookup is a request to pull and unpackage the content of a bundle to the cluster.   
`catalogSources` |  `array (string)` |   
`conditions` |  `array` |   
`conditions[]` |  `object` |  InstallPlanCondition represents the overall status of the execution of an InstallPlan.   
`message` |  `string` |  Message is a human-readable message containing detailed information that may be important to understanding why the plan has its current status.   
`phase` |  `string` |  InstallPlanPhase is the current status of a InstallPlan as a whole.   
`plan` |  `array` |   
`plan[]` |  `object` |  Step represents the status of an individual step in an InstallPlan.   
`startTime` |  `string` |  StartTime is the time when the controller began applying the resources listed in the plan to the cluster.   
Show more

## 6.1.3. .status.attenuatedServiceAccountRef

Description
     AttenuatedServiceAccountRef references the service account that is used to do scoped operator install. 
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

## 6.1.4. .status.bundleLookups

Description
     BundleLookups is the set of in-progress requests to pull and unpackage bundle content to the cluster. 
Type
     `array`

## 6.1.5. .status.bundleLookups[]

Description
     BundleLookup is a request to pull and unpackage the content of a bundle to the cluster. 
Type
     `object`
Required
    

  * `catalogSourceRef`
  * `identifier`
  * `path`
  * `replaces`



Property| Type| Description  
---|---|---  
`catalogSourceRef` |  `object` |  CatalogSourceRef is a reference to the CatalogSource the bundle path was resolved from.   
`conditions` |  `array` |  Conditions represents the overall state of a BundleLookup.   
`conditions[]` |  `object` |   
`identifier` |  `string` |  Identifier is the catalog-unique name of the operator (the name of the CSV for bundles that contain CSVs)   
`path` |  `string` |  Path refers to the location of a bundle to pull. It’s typically an image reference.   
`properties` |  `string` |  The effective properties of the unpacked bundle.   
`replaces` |  `string` |  Replaces is the name of the bundle to replace with the one found at Path.   
Show more

## 6.1.6. .status.bundleLookups[].catalogSourceRef

Description
     CatalogSourceRef is a reference to the CatalogSource the bundle path was resolved from. 
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

## 6.1.7. .status.bundleLookups[].conditions

Description
     Conditions represents the overall state of a BundleLookup. 
Type
     `array`

## 6.1.8. .status.bundleLookups[].conditions[]

Description
    
Type
     `object`
Required
    

  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  Last time the condition transitioned from one status to another.   
`lastUpdateTime` |  `string` |  Last time the condition was probed.   
`message` |  `string` |  A human readable message indicating details about the transition.   
`reason` |  `string` |  The reason for the condition’s last transition.   
`status` |  `string` |  Status of the condition, one of True, False, Unknown.   
`type` |  `string` |  Type of condition.   
Show more

## 6.1.9. .status.conditions

Description
    
Type
     `array`

## 6.1.10. .status.conditions[]

Description
     InstallPlanCondition represents the overall status of the execution of an InstallPlan. 
Type
     `object`

Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |   
`lastUpdateTime` |  `string` |   
`message` |  `string` |   
`reason` |  `string` |  ConditionReason is a camelcased reason for the state transition.   
`status` |  `string` |   
`type` |  `string` |  InstallPlanConditionType describes the state of an InstallPlan at a certain point as a whole.   
Show more

## 6.1.11. .status.plan

Description
    
Type
     `array`

## 6.1.12. .status.plan[]

Description
     Step represents the status of an individual step in an InstallPlan. 
Type
     `object`
Required
    

  * `resolving`
  * `resource`
  * `status`



Property| Type| Description  
---|---|---  
`optional` |  `boolean` |   
`resolving` |  `string` |   
`resource` |  `object` |  StepResource represents the status of a resource to be tracked by an InstallPlan.   
`status` |  `string` |  StepStatus is the current status of a particular resource an in InstallPlan   
Show more

## 6.1.13. .status.plan[].resource

Description
     StepResource represents the status of a resource to be tracked by an InstallPlan. 
Type
     `object`
Required
    

  * `group`
  * `kind`
  * `name`
  * `sourceName`
  * `sourceNamespace`
  * `version`



Property| Type| Description  
---|---|---  
`group` |  `string` |   
`kind` |  `string` |   
`manifest` |  `string` |   
`name` |  `string` |   
`sourceName` |  `string` |   
`sourceNamespace` |  `string` |   
`version` |  `string` |   
Show more
