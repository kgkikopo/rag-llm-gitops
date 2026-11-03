# 1.114. io.k8s.api.rbac.v1.AggregationRule schema

Description
     AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole 
Type
     `object`

## 1.114.1. Schema

Property| Type| Description  
---|---|---  
`clusterRoleSelectors` |  `array (LabelSelector)` |  ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole’s permissions will be added   
Show more
