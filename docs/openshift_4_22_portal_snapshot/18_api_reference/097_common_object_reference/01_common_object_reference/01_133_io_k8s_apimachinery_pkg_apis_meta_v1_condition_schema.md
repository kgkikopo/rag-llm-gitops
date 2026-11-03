# 1.133. io.k8s.apimachinery.pkg.apis.meta.v1.Condition schema

Description
     Condition contains details for one aspect of the current state of this API Resource. 
Type
     `object`
Required
    

  * `type`
  * `status`
  * `lastTransitionTime`
  * `reason`
  * `message`



## 1.133.1. Schema

Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-apis-meta-v1-Time "1.145. io.k8s.apimachinery.pkg.apis.meta.v1.Time schema") |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`message` |  `string` |  message is a human readable message indicating details about the transition. This may be an empty string.   
`observedGeneration` |  `integer` |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`reason` |  `string` |  reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase.   
Show more
