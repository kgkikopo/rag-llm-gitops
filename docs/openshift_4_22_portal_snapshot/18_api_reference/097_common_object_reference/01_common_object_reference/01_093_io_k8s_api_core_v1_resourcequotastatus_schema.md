# 1.93. io.k8s.api.core.v1.ResourceQuotaStatus schema

Description
     ResourceQuotaStatus defines the enforced hard limits and observed use. 
Type
     `object`

## 1.93.1. Schema

Property| Type| Description  
---|---|---  
`hard` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") |  Hard is the set of enforced hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/>  
`used` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-api-resource-Quantity "1.132. io.k8s.apimachinery.pkg.api.resource.Quantity schema") |  Used is the current observed total usage of the resource in the namespace.   
Show more
