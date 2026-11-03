# Chapter 4. RoleBinding [rbac.authorization.k8s.io/v1]

Description
     RoleBinding references a role, but does not contain it. It can reference a Role in the same namespace or a ClusterRole in the global namespace. It adds who information via Subjects and namespace information by which namespace it exists in. RoleBindings in a given namespace only have effect in that namespace. 
Type
     `object`
Required
    

  * `roleRef`

- [4.1. Specification](04_01_specification.md)
- [4.2. API endpoints](04_02_api_endpoints.md)
