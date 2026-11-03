# 10.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  NamespaceSpec describes the attributes on a Namespace.   
`status` |  `object` |  NamespaceStatus is information about the current status of a Namespace.   
Show more

## 10.1.1. .spec

Description
     NamespaceSpec describes the attributes on a Namespace. 
Type
     `object`

Property| Type| Description  
---|---|---  
`finalizers` |  `array (string)` |  Finalizers is an opaque list of values that must be empty to permanently remove object from storage. More info: <https://kubernetes.io/docs/tasks/administer-cluster/namespaces/>  
Show more

## 10.1.2. .status

Description
     NamespaceStatus is information about the current status of a Namespace. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  Represents the latest available observations of a namespace’s current state.   
`conditions[]` |  `object` |  NamespaceCondition contains details about state of namespace.   
`phase` |  `string` |  Phase is the current lifecycle phase of the namespace. More info: <https://kubernetes.io/docs/tasks/administer-cluster/namespaces/> Possible enum values: - `"Active"` means the namespace is available for use in the system - `"Terminating"` means the namespace is undergoing graceful termination   
Show more

## 10.1.3. .status.conditions

Description
     Represents the latest available observations of a namespace’s current state. 
Type
     `array`

## 10.1.4. .status.conditions[]

Description
     NamespaceCondition contains details about state of namespace. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition transitioned from one status to another.   
`message` |  `string` |  Human-readable message indicating details about last transition.   
`reason` |  `string` |  Unique, one-word, CamelCase reason for the condition’s last transition.   
`status` |  `string` |  Status of the condition, one of True, False, Unknown.   
`type` |  `string` |  Type of namespace controller condition.   
Show more
