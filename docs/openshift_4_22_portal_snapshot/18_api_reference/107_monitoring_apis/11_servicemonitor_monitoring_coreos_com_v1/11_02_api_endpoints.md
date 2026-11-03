# 11.2. API endpoints

The following API endpoints are available: 

  * `/apis/monitoring.coreos.com/v1/servicemonitors`

    * `GET`: list objects of kind ServiceMonitor 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors`

    * `DELETE`: delete collection of ServiceMonitor 
    * `GET`: list objects of kind ServiceMonitor 
    * `POST`: create a ServiceMonitor 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors/{name}`

    * `DELETE`: delete a ServiceMonitor 
    * `GET`: read the specified ServiceMonitor 
    * `PATCH`: partially update the specified ServiceMonitor 
    * `PUT`: replace the specified ServiceMonitor 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors/{name}/status`

    * `GET`: read status of the specified ServiceMonitor 
    * `PATCH`: partially update status of the specified ServiceMonitor 
    * `PUT`: replace status of the specified ServiceMonitor 




## 11.2.1. /apis/monitoring.coreos.com/v1/servicemonitors

HTTP method
     `GET`
Description
     list objects of kind ServiceMonitor 

Table 11.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceMonitorList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-monitoring-v1-ServiceMonitorList) schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.2. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors

HTTP method
     `DELETE`
Description
     delete collection of ServiceMonitor 

Table 11.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind ServiceMonitor 

Table 11.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceMonitorList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-monitoring-v1-ServiceMonitorList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ServiceMonitor 

Table 11.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 11.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema   
202 - Accepted  |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.3. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors/{name}

Table 11.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ServiceMonitor   
Show more

HTTP method
     `DELETE`
Description
     delete a ServiceMonitor 

Table 11.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 11.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ServiceMonitor 

Table 11.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ServiceMonitor 

Table 11.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ServiceMonitor 

Table 11.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 11.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.4. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/servicemonitors/{name}/status

Table 11.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ServiceMonitor   
Show more

HTTP method
     `GET`
Description
     read status of the specified ServiceMonitor 

Table 11.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ServiceMonitor 

Table 11.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ServiceMonitor 

Table 11.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 11.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`ServiceMonitor`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/servicemonitor-monitoring-coreos-com-v1 "Chapter 11. ServiceMonitor \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
