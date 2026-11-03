# Chapter 5. RoleBinding [authorization.openshift.io/v1]

Description
    

RoleBinding references a Role, but not contain it. It can reference any Role in the same namespace or in the global namespace. It adds who information via (Users and Groups) OR Subjects and namespace information by which namespace it exists in. RoleBindings in a given namespace only have effect in that namespace (excepting the master namespace which has power in all namespaces). 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `subjects`
  * `roleRef`

- [5.1. Specification](05_01_specification.md)
- [5.2. API endpoints](05_02_api_endpoints.md)
