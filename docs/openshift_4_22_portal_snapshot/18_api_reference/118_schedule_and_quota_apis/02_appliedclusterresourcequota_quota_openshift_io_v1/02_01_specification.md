# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  metadata is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ClusterResourceQuotaSpec defines the desired quota restrictions   
`status` |  `object` |  ClusterResourceQuotaStatus defines the actual enforced quota and its current usage   
Show more

## 2.1.1. .spec

Description
     ClusterResourceQuotaSpec defines the desired quota restrictions 
Type
     `object`
Required
    

  * `selector`
  * `quota`



Property| Type| Description  
---|---|---  
`quota` |  [`ResourceQuotaSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ResourceQuotaSpec) |  quota defines the desired quota   
`selector` |  `object` |  ClusterResourceQuotaSelector is used to select projects. At least one of LabelSelector or AnnotationSelector must present. If only one is present, it is the only selection criteria. If both are specified, the project must match both restrictions.   
Show more

## 2.1.2. .spec.selector

Description
     ClusterResourceQuotaSelector is used to select projects. At least one of LabelSelector or AnnotationSelector must present. If only one is present, it is the only selection criteria. If both are specified, the project must match both restrictions. 
Type
     `object`

Property| Type| Description  
---|---|---  
`annotations` |  `object (string)` |  AnnotationSelector is used to select projects by annotation.   
`labels` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  LabelSelector is used to select projects by label.   
Show more

## 2.1.3. .status

Description
     ClusterResourceQuotaStatus defines the actual enforced quota and its current usage 
Type
     `object`
Required
    

  * `total`



Property| Type| Description  
---|---|---  
`namespaces` |  `array` |  namespaces slices the usage by project. This division allows for quick resolution of deletion reconciliation inside of a single project without requiring a recalculation across all projects. This can be used to pull the deltas for a given project.   
`namespaces[]` |  `object` |  ResourceQuotaStatusByNamespace gives status for a particular project   
`total` |  [`ResourceQuotaStatus`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ResourceQuotaStatus) |  total defines the actual enforced quota and its current usage across all projects   
Show more

## 2.1.4. .status.namespaces

Description
     namespaces slices the usage by project. This division allows for quick resolution of deletion reconciliation inside of a single project without requiring a recalculation across all projects. This can be used to pull the deltas for a given project. 
Type
     `array`

## 2.1.5. .status.namespaces[]

Description
     ResourceQuotaStatusByNamespace gives status for a particular project 
Type
     `object`
Required
    

  * `namespace`
  * `status`



Property| Type| Description  
---|---|---  
`namespace` |  `string` |  namespace the project this status applies to   
`status` |  [`ResourceQuotaStatus`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ResourceQuotaStatus) |  status indicates how many resources have been consumed by this project   
Show more
