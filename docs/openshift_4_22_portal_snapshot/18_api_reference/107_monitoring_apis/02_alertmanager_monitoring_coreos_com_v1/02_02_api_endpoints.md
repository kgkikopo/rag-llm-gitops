# 2.2. API endpoints

The following API endpoints are available: 

  * `/apis/monitoring.coreos.com/v1/alertmanagers`

    * `GET`: list objects of kind Alertmanager 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/alertmanagers`

    * `DELETE`: delete collection of Alertmanager 
    * `GET`: list objects of kind Alertmanager 
    * `POST`: create an Alertmanager 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/alertmanagers/{name}`

    * `DELETE`: delete an Alertmanager 
    * `GET`: read the specified Alertmanager 
    * `PATCH`: partially update the specified Alertmanager 
    * `PUT`: replace the specified Alertmanager 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/alertmanagers/{name}/scale`

    * `GET`: read scale of the specified Alertmanager 
    * `PATCH`: partially update scale of the specified Alertmanager 
    * `PUT`: replace scale of the specified Alertmanager 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/alertmanagers/{name}/status`

    * `GET`: read status of the specified Alertmanager 
    * `PATCH`: partially update status of the specified Alertmanager 
    * `PUT`: replace status of the specified Alertmanager 




## 2.2.1. /apis/monitoring.coreos.com/v1/alertmanagers

HTTP method
     `GET`
Description
     list objects of kind Alertmanager 

Table 2.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertmanagerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-monitoring-v1-AlertmanagerList) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/alertmanagers

HTTP method
     `DELETE`
Description
     delete collection of Alertmanager 

Table 2.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind Alertmanager 

Table 2.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertmanagerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-monitoring-v1-AlertmanagerList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an Alertmanager 

Table 2.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 2.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema   
202 - Accepted  |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/alertmanagers/{name}

Table 2.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Alertmanager   
Show more

HTTP method
     `DELETE`
Description
     delete an Alertmanager 

Table 2.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Alertmanager 

Table 2.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Alertmanager 

Table 2.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Alertmanager 

Table 2.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 2.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.4. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/alertmanagers/{name}/scale

Table 2.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Alertmanager   
Show more

HTTP method
     `GET`
Description
     read scale of the specified Alertmanager 

Table 2.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update scale of the specified Alertmanager 

Table 2.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace scale of the specified Alertmanager 

Table 2.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema  |   
Show more

Table 2.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.5. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/alertmanagers/{name}/status

Table 2.23. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Alertmanager   
Show more

HTTP method
     `GET`
Description
     read status of the specified Alertmanager 

Table 2.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Alertmanager 

Table 2.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.26. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Alertmanager 

Table 2.27. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.28. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 2.29. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`Alertmanager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanager-monitoring-coreos-com-v1 "Chapter 2. Alertmanager \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
