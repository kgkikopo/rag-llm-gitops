# 27.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration   
`status` |  `object` |  status holds observed values from the cluster. They may not be overridden.   
Show more

## 27.1.1. .spec

Description
     spec holds user settable values for configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`defaultNodeSelector` |  `string` |  defaultNodeSelector helps set the cluster-wide default node selector to restrict pod placement to specific nodes. This is applied to the pods created in all namespaces and creates an intersection with any existing nodeSelectors already set on a pod, additionally constraining that pod’s selector. For example, defaultNodeSelector: "type=user-node,region=east" would set nodeSelector field in pod spec to "type=user-node,region=east" to all pods created in all namespaces. Namespaces having project-wide node selectors won’t be impacted even if this field is set. This adds an annotation section to the namespace. For example, if a new namespace is created with node-selector='type=user-node,region=east', the annotation openshift.io/node-selector: type=user-node,region=east gets added to the project. When the openshift.io/node-selector annotation is set on the project the value is used in preference to the value we are setting for defaultNodeSelector field. For instance, openshift.io/node-selector: "type=user-node,region=west" means that the default of "type=user-node,region=east" set in defaultNodeSelector would not be applied.   
`mastersSchedulable` |  `boolean` |  mastersSchedulable allows masters nodes to be schedulable. When this flag is turned on, all the master nodes in the cluster will be made schedulable, so that workload pods can run on them. The default value for this field is false, meaning none of the master nodes are schedulable. Important Note: Once the workload pods start running on the master nodes, extreme care must be taken to ensure that cluster-critical control plane components are not impacted. Please turn on this field after doing due diligence.   
`policy` |  `object` |  DEPRECATED: the scheduler Policy API has been deprecated and will be removed in a future release. policy is a reference to a ConfigMap containing scheduler policy which has user specified predicates and priorities. If this ConfigMap is not available scheduler will default to use DefaultAlgorithmProvider. The namespace for this configmap is openshift-config.   
`profile` |  `string` |  profile sets which scheduling profile should be set in order to configure scheduling decisions for new pods.  Valid values are "LowNodeUtilization", "HighNodeUtilization", "NoScoring" Defaults to "LowNodeUtilization"   
Show more

## 27.1.2. .spec.policy

Description
     DEPRECATED: the scheduler Policy API has been deprecated and will be removed in a future release. policy is a reference to a ConfigMap containing scheduler policy which has user specified predicates and priorities. If this ConfigMap is not available scheduler will default to use DefaultAlgorithmProvider. The namespace for this configmap is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced config map   
Show more

## 27.1.3. .status

Description
     status holds observed values from the cluster. They may not be overridden. 
Type
     `object`
