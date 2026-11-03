# Chapter 4. RoleBindingRestriction [authorization.openshift.io/v1]

Description
    

RoleBindingRestriction is an object that can be matched against a subject (user, group, or service account) to determine whether rolebindings on that subject are allowed in the namespace to which the RoleBindingRestriction belongs. If any one of those RoleBindingRestriction objects matches a subject, rolebindings on that subject in the namespace are allowed. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`

- [4.1. Specification](04_01_specification.md)
- [4.2. API endpoints](04_02_api_endpoints.md)
