# 1.94. io.k8s.api.core.v1.ResourceRequirements schema

Description
     ResourceRequirements describes the compute resource requirements. 
Type
     `object`

## 1.94.1. Schema

Property| Type| Description  
---|---|---  
`claims` |  `array (ResourceClaim)` |  Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This field depends on the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers.   
`limits` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") |  Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
`requests` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") |  Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
Show more
