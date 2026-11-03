# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec defines the characteristics of the resource.   
`status` |  `object` |  status contains the observed state of the resource.   
Show more

## 2.1.1. .spec

Description
     spec defines the characteristics of the resource. 
Type
     `object`

Property| Type| Description  
---|---|---  
`numberOfUsersToReport` |  `integer` |  numberOfUsersToReport is the number of users to include in the report. If unspecified or zero, the default is ten. This is default is subject to change.   
Show more

## 2.1.2. .status

Description
     status contains the observed state of the resource. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions contains details of the current status of this API Resource.   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example, type FooStatus struct{ // Represents the observations of a foo’s current state. // Known .status.conditions.type are: "Available", "Progressing", and "Degraded" // +patchMergeKey=type // +patchStrategy=merge // +listType=map // +listMapKey=type Conditions []metav1.Condition `json:"conditions,omitempty" patchStrategy:"merge" patchMergeKey:"type" protobuf:"bytes,1,rep,name=conditions"` // other fields }   
`currentHour` |  `object` |  currentHour contains request history for the current hour. This is porcelain to make the API easier to read by humans seeing if they addressed a problem. This field is reset on the hour.   
`last24h` |  `array` |  last24h contains request history for the last 24 hours, indexed by the hour, so 12:00AM-12:59 is in index 0, 6am-6:59am is index 6, etc. The index of the current hour is updated live and then duplicated into the requestsLastHour field.   
`last24h[]` |  `object` |  PerResourceAPIRequestLog logs request for various nodes.   
`removedInRelease` |  `string` |  removedInRelease is when the API will be removed.   
`requestCount` |  `integer` |  requestCount is a sum of all requestCounts across all current hours, nodes, and users.   
Show more

## 2.1.3. .status.conditions

Description
     conditions contains details of the current status of this API Resource. 
Type
     `array`

## 2.1.4. .status.conditions[]

Description
     Condition contains details for one aspect of the current state of this API Resource. --- This struct is intended for direct use as an array at the field path .status.conditions. For example, type FooStatus struct{ // Represents the observations of a foo’s current state. // Known .status.conditions.type are: "Available", "Progressing", and "Degraded" // +patchMergeKey=type // +patchStrategy=merge // +listType=map // +listMapKey=type Conditions []metav1.Condition `json:"conditions,omitempty" patchStrategy:"merge" patchMergeKey:"type" protobuf:"bytes,1,rep,name=conditions"` // other fields } 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `message`
  * `reason`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`message` |  `string` |  message is a human readable message indicating details about the transition. This may be an empty string.   
`observedGeneration` |  `integer` |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`reason` |  `string` |  reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase. --- Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important. The regex it matches is (dns1123SubdomainFmt/)?(qualifiedNameFmt)   
Show more

## 2.1.5. .status.currentHour

Description
     currentHour contains request history for the current hour. This is porcelain to make the API easier to read by humans seeing if they addressed a problem. This field is reset on the hour. 
Type
     `object`

Property| Type| Description  
---|---|---  
`byNode` |  `array` |  byNode contains logs of requests per node.   
`byNode[]` |  `object` |  PerNodeAPIRequestLog contains logs of requests to a certain node.   
`requestCount` |  `integer` |  requestCount is a sum of all requestCounts across nodes.   
Show more

## 2.1.6. .status.currentHour.byNode

Description
     byNode contains logs of requests per node. 
Type
     `array`

## 2.1.7. .status.currentHour.byNode[]

Description
     PerNodeAPIRequestLog contains logs of requests to a certain node. 
Type
     `object`

Property| Type| Description  
---|---|---  
`byUser` |  `array` |  byUser contains request details by top .spec.numberOfUsersToReport users. Note that because in the case of an apiserver, restart the list of top users is determined on a best-effort basis, the list might be imprecise. In addition, some system users may be explicitly included in the list.   
`byUser[]` |  `object` |  PerUserAPIRequestCount contains logs of a user’s requests.   
`nodeName` |  `string` |  nodeName where the request are being handled.   
`requestCount` |  `integer` |  requestCount is a sum of all requestCounts across all users, even those outside of the top 10 users.   
Show more

## 2.1.8. .status.currentHour.byNode[].byUser

Description
     byUser contains request details by top .spec.numberOfUsersToReport users. Note that because in the case of an apiserver, restart the list of top users is determined on a best-effort basis, the list might be imprecise. In addition, some system users may be explicitly included in the list. 
Type
     `array`

## 2.1.9. .status.currentHour.byNode[].byUser[]

Description
     PerUserAPIRequestCount contains logs of a user’s requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`byVerb` |  `array` |  byVerb details by verb.   
`byVerb[]` |  `object` |  PerVerbAPIRequestCount requestCounts requests by API request verb.   
`requestCount` |  `integer` |  requestCount of requests by the user across all verbs.   
`userAgent` |  `string` |  userAgent that made the request. The same user often has multiple binaries which connect (pods with many containers). The different binaries will have different userAgents, but the same user. In addition, we have userAgents with version information embedded and the userName isn’t likely to change.   
`username` |  `string` |  userName that made the request.   
Show more

## 2.1.10. .status.currentHour.byNode[].byUser[].byVerb

Description
     byVerb details by verb. 
Type
     `array`

## 2.1.11. .status.currentHour.byNode[].byUser[].byVerb[]

Description
     PerVerbAPIRequestCount requestCounts requests by API request verb. 
Type
     `object`

Property| Type| Description  
---|---|---  
`requestCount` |  `integer` |  requestCount of requests for verb.   
`verb` |  `string` |  verb of API request (get, list, create, etc…​)   
Show more

## 2.1.12. .status.last24h

Description
     last24h contains request history for the last 24 hours, indexed by the hour, so 12:00AM-12:59 is in index 0, 6am-6:59am is index 6, etc. The index of the current hour is updated live and then duplicated into the requestsLastHour field. 
Type
     `array`

## 2.1.13. .status.last24h[]

Description
     PerResourceAPIRequestLog logs request for various nodes. 
Type
     `object`

Property| Type| Description  
---|---|---  
`byNode` |  `array` |  byNode contains logs of requests per node.   
`byNode[]` |  `object` |  PerNodeAPIRequestLog contains logs of requests to a certain node.   
`requestCount` |  `integer` |  requestCount is a sum of all requestCounts across nodes.   
Show more

## 2.1.14. .status.last24h[].byNode

Description
     byNode contains logs of requests per node. 
Type
     `array`

## 2.1.15. .status.last24h[].byNode[]

Description
     PerNodeAPIRequestLog contains logs of requests to a certain node. 
Type
     `object`

Property| Type| Description  
---|---|---  
`byUser` |  `array` |  byUser contains request details by top .spec.numberOfUsersToReport users. Note that because in the case of an apiserver, restart the list of top users is determined on a best-effort basis, the list might be imprecise. In addition, some system users may be explicitly included in the list.   
`byUser[]` |  `object` |  PerUserAPIRequestCount contains logs of a user’s requests.   
`nodeName` |  `string` |  nodeName where the request are being handled.   
`requestCount` |  `integer` |  requestCount is a sum of all requestCounts across all users, even those outside of the top 10 users.   
Show more

## 2.1.16. .status.last24h[].byNode[].byUser

Description
     byUser contains request details by top .spec.numberOfUsersToReport users. Note that because in the case of an apiserver, restart the list of top users is determined on a best-effort basis, the list might be imprecise. In addition, some system users may be explicitly included in the list. 
Type
     `array`

## 2.1.17. .status.last24h[].byNode[].byUser[]

Description
     PerUserAPIRequestCount contains logs of a user’s requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`byVerb` |  `array` |  byVerb details by verb.   
`byVerb[]` |  `object` |  PerVerbAPIRequestCount requestCounts requests by API request verb.   
`requestCount` |  `integer` |  requestCount of requests by the user across all verbs.   
`userAgent` |  `string` |  userAgent that made the request. The same user often has multiple binaries which connect (pods with many containers). The different binaries will have different userAgents, but the same user. In addition, we have userAgents with version information embedded and the userName isn’t likely to change.   
`username` |  `string` |  userName that made the request.   
Show more

## 2.1.18. .status.last24h[].byNode[].byUser[].byVerb

Description
     byVerb details by verb. 
Type
     `array`

## 2.1.19. .status.last24h[].byNode[].byUser[].byVerb[]

Description
     PerVerbAPIRequestCount requestCounts requests by API request verb. 
Type
     `object`

Property| Type| Description  
---|---|---  
`requestCount` |  `integer` |  requestCount of requests for verb.   
`verb` |  `string` |  verb of API request (get, list, create, etc…​)   
Show more
