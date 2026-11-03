# Chapter 10. ResourceClaim [resource.k8s.io/v1]

Description
    

ResourceClaim describes a request for access to resources in the cluster, for use by workloads. For example, if a workload needs an accelerator device with specific properties, this is how that request is expressed. The status stanza tracks whether this claim has been satisfied and what specific resources have been allocated. 

This is an alpha type and requires enabling the DynamicResourceAllocation feature gate. 

Type
     `object`
Required
    

  * `spec`

- [10.1. Specification](10_01_specification.md)
- [10.2. API endpoints](10_02_api_endpoints.md)
