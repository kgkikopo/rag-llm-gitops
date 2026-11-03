# 8.2. API endpoints

The following API endpoints are available: 

  * `/apis/monitoring.coreos.com/v1/probes`

    * `GET`: list objects of kind Probe 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes`

    * `DELETE`: delete collection of Probe 
    * `GET`: list objects of kind Probe 
    * `POST`: create a Probe 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes/{name}`

    * `DELETE`: delete a Probe 
    * `GET`: read the specified Probe 
    * `PATCH`: partially update the specified Probe 
    * `PUT`: replace the specified Probe 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes/{name}/status`

    * `GET`: read status of the specified Probe 
    * `PATCH`: partially update status of the specified Probe 
    * `PUT`: replace status of the specified Probe 




## 8.2.1. /apis/monitoring.coreos.com/v1/probes

HTTP method
     `GET`
Description
     list objects of kind Probe 

Table 8.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ProbeList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-monitoring-v1-ProbeList) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.2. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes

HTTP method
     `DELETE`
Description
     delete collection of Probe 

Table 8.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind Probe 

Table 8.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ProbeList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-monitoring-v1-ProbeList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Probe 

Table 8.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 8.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema   
202 - Accepted  |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.3. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes/{name}

Table 8.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Probe   
Show more

HTTP method
     `DELETE`
Description
     delete a Probe 

Table 8.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 8.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Probe 

Table 8.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Probe 

Table 8.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Probe 

Table 8.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 8.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.4. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/probes/{name}/status

Table 8.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Probe   
Show more

HTTP method
     `GET`
Description
     read status of the specified Probe 

Table 8.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Probe 

Table 8.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Probe 

Table 8.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 8.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`Probe`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/probe-monitoring-coreos-com-v1 "Chapter 8. Probe \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
