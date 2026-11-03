# 1.138. io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector schema

Description
     A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects. 
Type
     `object`

## 1.138.1. Schema

Property| Type| Description  
---|---|---  
`matchExpressions` |  [`array (LabelSelectorRequirement)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelectorRequirement "1.139. io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelectorRequirement schema") |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more
