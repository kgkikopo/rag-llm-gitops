# 5.2. API endpoints

The following API endpoints are available: 

  * `/apis/monitoring.openshift.io/v1/alertingrules`

    * `GET`: list objects of kind AlertingRule 

  * `/apis/monitoring.openshift.io/v1/namespaces/{namespace}/alertingrules`

    * `DELETE`: delete collection of AlertingRule 
    * `GET`: list objects of kind AlertingRule 
    * `POST`: create an AlertingRule 

  * `/apis/monitoring.openshift.io/v1/namespaces/{namespace}/alertingrules/{name}`

    * `DELETE`: delete an AlertingRule 
    * `GET`: read the specified AlertingRule 
    * `PATCH`: partially update the specified AlertingRule 
    * `PUT`: replace the specified AlertingRule 

  * `/apis/monitoring.openshift.io/v1/namespaces/{namespace}/alertingrules/{name}/status`

    * `GET`: read status of the specified AlertingRule 
    * `PATCH`: partially update status of the specified AlertingRule 
    * `PUT`: replace status of the specified AlertingRule 




## 5.2.1. /apis/monitoring.openshift.io/v1/alertingrules

HTTP method
     `GET`
Description
     list objects of kind AlertingRule 

Table 5.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertingRuleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-monitoring-v1-AlertingRuleList) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.2. /apis/monitoring.openshift.io/v1/namespaces/{namespace}/alertingrules

HTTP method
     `DELETE`
Description
     delete collection of AlertingRule 

Table 5.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind AlertingRule 

Table 5.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertingRuleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-monitoring-v1-AlertingRuleList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an AlertingRule 

Table 5.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema  |   
Show more

Table 5.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema   
201 - Created  |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema   
202 - Accepted  |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.3. /apis/monitoring.openshift.io/v1/namespaces/{namespace}/alertingrules/{name}

Table 5.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the AlertingRule   
Show more

HTTP method
     `DELETE`
Description
     delete an AlertingRule 

Table 5.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified AlertingRule 

Table 5.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified AlertingRule 

Table 5.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified AlertingRule 

Table 5.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema  |   
Show more

Table 5.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema   
201 - Created  |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.4. /apis/monitoring.openshift.io/v1/namespaces/{namespace}/alertingrules/{name}/status

Table 5.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the AlertingRule   
Show more

HTTP method
     `GET`
Description
     read status of the specified AlertingRule 

Table 5.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified AlertingRule 

Table 5.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified AlertingRule 

Table 5.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema  |   
Show more

Table 5.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema   
201 - Created  |  [`AlertingRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertingrule-monitoring-openshift-io-v1 "Chapter 5. AlertingRule \[monitoring.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
