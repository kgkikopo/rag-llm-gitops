# Chapter 2. AppliedClusterResourceQuota [quota.openshift.io/v1]

Description
    

AppliedClusterResourceQuota mirrors ClusterResourceQuota at a project scope, for projection into a project. It allows a project-admin to know which ClusterResourceQuotas are applied to his project and their associated usage. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `metadata`
  * `spec`

- [2.1. Specification](02_01_specification.md)
- [2.2. API endpoints](02_02_api_endpoints.md)
