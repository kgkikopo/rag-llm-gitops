# 1.1. ClusterRoleBinding [authorization.openshift.io/v1]

Description
    

ClusterRoleBinding references a ClusterRole, but not contain it. It can reference any ClusterRole in the same namespace or in the global namespace. It adds who information via (Users and Groups) OR Subjects and namespace information by which namespace it exists in. ClusterRoleBindings in a given namespace only have effect in that namespace (excepting the master namespace which has power in all namespaces). 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
