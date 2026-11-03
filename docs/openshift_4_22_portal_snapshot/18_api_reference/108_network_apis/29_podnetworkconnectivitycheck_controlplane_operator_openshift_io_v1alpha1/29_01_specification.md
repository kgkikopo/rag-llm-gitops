# 29.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec defines the source and target of the connectivity check   
`status` |  `object` |  status contains the observed status of the connectivity check   
Show more

## 29.1.1. .spec

Description
     spec defines the source and target of the connectivity check 
Type
     `object`
Required
    

  * `sourcePod`
  * `targetEndpoint`



Property| Type| Description  
---|---|---  
`sourcePod` |  `string` |  sourcePod names the pod from which the condition will be checked   
`targetEndpoint` |  `string` |  EndpointAddress to check. A TCP address of the form host:port. Note that if host is a DNS name, then the check would fail if the DNS name cannot be resolved. Specify an IP address for host to bypass DNS name lookup.   
`tlsClientCert` |  `object` |  TLSClientCert, if specified, references a kubernetes.io/tls type secret with 'tls.crt' and 'tls.key' entries containing an optional TLS client certificate and key to be used when checking endpoints that require a client certificate in order to gracefully preform the scan without causing excessive logging in the endpoint process. The secret must exist in the same namespace as this resource.   
Show more

## 29.1.2. .spec.tlsClientCert

Description
     TLSClientCert, if specified, references a kubernetes.io/tls type secret with 'tls.crt' and 'tls.key' entries containing an optional TLS client certificate and key to be used when checking endpoints that require a client certificate in order to gracefully preform the scan without causing excessive logging in the endpoint process. The secret must exist in the same namespace as this resource. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 29.1.3. .status

Description
     status contains the observed status of the connectivity check 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions summarize the status of the check   
`conditions[]` |  `object` |  PodNetworkConnectivityCheckCondition represents the overall status of the pod network connectivity.   
`failures` |  `array` |  failures contains logs of unsuccessful check actions   
`failures[]` |  `object` |  LogEntry records events   
`outages` |  `array` |  outages contains logs of time periods of outages   
`outages[]` |  `object` |  OutageEntry records time period of an outage   
`successes` |  `array` |  successes contains logs successful check actions   
`successes[]` |  `object` |  LogEntry records events   
Show more

## 29.1.4. .status.conditions

Description
     conditions summarize the status of the check 
Type
     `array`

## 29.1.5. .status.conditions[]

Description
     PodNetworkConnectivityCheckCondition represents the overall status of the pod network connectivity. 
Type
     `object`
Required
    

  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  ``  |  Last time the condition transitioned from one status to another.   
`message` |  `string` |  message indicating details about last transition in a human readable format.   
`reason` |  `string` |  reason for the condition’s last status transition in a machine readable format.   
`status` |  `string` |  status of the condition   
`type` |  `string` |  type of the condition   
Show more

## 29.1.6. .status.failures

Description
     failures contains logs of unsuccessful check actions 
Type
     `array`

## 29.1.7. .status.failures[]

Description
     LogEntry records events 
Type
     `object`
Required
    

  * `success`



Property| Type| Description  
---|---|---  
`latency` |  ``  |  latency records how long the action mentioned in the entry took.   
`message` |  `string` |  message explaining status in a human readable format.   
`reason` |  `string` |  reason for status in a machine readable format.   
`success` |  `boolean` |  success indicates if the log entry indicates a success or failure.   
`time` |  ``  |  Start time of check action.   
Show more

## 29.1.8. .status.outages

Description
     outages contains logs of time periods of outages 
Type
     `array`

## 29.1.9. .status.outages[]

Description
     OutageEntry records time period of an outage 
Type
     `object`

Property| Type| Description  
---|---|---  
`end` |  ``  |  end of outage detected   
`endLogs` |  `array` |  endLogs contains log entries related to the end of this outage. Should contain the success entry that resolved the outage and possibly a few of the failure log entries that preceded it.   
`endLogs[]` |  `object` |  LogEntry records events   
`message` |  `string` |  message summarizes outage details in a human readable format.   
`start` |  ``  |  start of outage detected   
`startLogs` |  `array` |  startLogs contains log entries related to the start of this outage. Should contain the original failure, any entries where the failure mode changed.   
`startLogs[]` |  `object` |  LogEntry records events   
Show more

## 29.1.10. .status.outages[].endLogs

Description
     endLogs contains log entries related to the end of this outage. Should contain the success entry that resolved the outage and possibly a few of the failure log entries that preceded it. 
Type
     `array`

## 29.1.11. .status.outages[].endLogs[]

Description
     LogEntry records events 
Type
     `object`
Required
    

  * `success`



Property| Type| Description  
---|---|---  
`latency` |  ``  |  latency records how long the action mentioned in the entry took.   
`message` |  `string` |  message explaining status in a human readable format.   
`reason` |  `string` |  reason for status in a machine readable format.   
`success` |  `boolean` |  success indicates if the log entry indicates a success or failure.   
`time` |  ``  |  Start time of check action.   
Show more

## 29.1.12. .status.outages[].startLogs

Description
     startLogs contains log entries related to the start of this outage. Should contain the original failure, any entries where the failure mode changed. 
Type
     `array`

## 29.1.13. .status.outages[].startLogs[]

Description
     LogEntry records events 
Type
     `object`
Required
    

  * `success`



Property| Type| Description  
---|---|---  
`latency` |  ``  |  latency records how long the action mentioned in the entry took.   
`message` |  `string` |  message explaining status in a human readable format.   
`reason` |  `string` |  reason for status in a machine readable format.   
`success` |  `boolean` |  success indicates if the log entry indicates a success or failure.   
`time` |  ``  |  Start time of check action.   
Show more

## 29.1.14. .status.successes

Description
     successes contains logs successful check actions 
Type
     `array`

## 29.1.15. .status.successes[]

Description
     LogEntry records events 
Type
     `object`
Required
    

  * `success`



Property| Type| Description  
---|---|---  
`latency` |  ``  |  latency records how long the action mentioned in the entry took.   
`message` |  `string` |  message explaining status in a human readable format.   
`reason` |  `string` |  reason for status in a machine readable format.   
`success` |  `boolean` |  success indicates if the log entry indicates a success or failure.   
`time` |  ``  |  Start time of check action.   
Show more
