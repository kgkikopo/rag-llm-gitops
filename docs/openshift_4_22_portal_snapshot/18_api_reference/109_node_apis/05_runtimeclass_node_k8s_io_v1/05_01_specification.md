# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`handler` |  `string` |  handler specifies the underlying runtime and configuration that the CRI implementation will use to handle pods of this class. The possible values are specific to the node & CRI configuration. It is assumed that all handlers are available on every node, and handlers of the same name are equivalent on every node. For example, a handler called "runc" might specify that the runc OCI runtime (using native Linux containers) will be used to run the containers in a pod. The Handler must be lowercase, conform to the DNS Label (RFC 1123) requirements, and is immutable.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`overhead` |  `object` |  Overhead structure represents the resource overhead associated with running a pod.   
`scheduling` |  `object` |  Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass.   
Show more

## 5.1.1. .overhead

Description
     Overhead structure represents the resource overhead associated with running a pod. 
Type
     `object`

Property| Type| Description  
---|---|---  
`podFixed` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  podFixed represents the fixed resource overhead associated with running a pod.   
Show more

## 5.1.2. .scheduling

Description
     Scheduling specifies the scheduling constraints for nodes supporting a RuntimeClass. 
Type
     `object`

Property| Type| Description  
---|---|---  
`nodeSelector` |  `object (string)` |  nodeSelector lists labels that must be present on nodes that support this RuntimeClass. Pods using this RuntimeClass can only be scheduled to a node matched by this selector. The RuntimeClass nodeSelector is merged with a pod’s existing nodeSelector. Any conflicts will cause the pod to be rejected in admission.   
`tolerations` |  [`array (Toleration)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-Toleration) |  tolerations are appended (excluding duplicates) to pods running with this RuntimeClass during admission, effectively unioning the set of nodes tolerated by the pod and the RuntimeClass.   
Show more
