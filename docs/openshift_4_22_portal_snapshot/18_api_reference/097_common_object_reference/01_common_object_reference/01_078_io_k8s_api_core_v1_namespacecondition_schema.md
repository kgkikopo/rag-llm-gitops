# 1.78. io.k8s.api.core.v1.NamespaceCondition schema

Description
     NamespaceCondition contains details about state of namespace. 
Type
     `object`
Required
    

  * `type`
  * `status`



## 1.78.1. Schema

Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-apis-meta-v1-Time "1.145. io.k8s.apimachinery.pkg.apis.meta.v1.Time schema") |  Last time the condition transitioned from one status to another.   
`message` |  `string` |  Human-readable message indicating details about last transition.   
`reason` |  `string` |  Unique, one-word, CamelCase reason for the condition’s last transition.   
`status` |  `string` |  Status of the condition, one of True, False, Unknown.   
`type` |  `string` |  Type of namespace controller condition.   
Show more
