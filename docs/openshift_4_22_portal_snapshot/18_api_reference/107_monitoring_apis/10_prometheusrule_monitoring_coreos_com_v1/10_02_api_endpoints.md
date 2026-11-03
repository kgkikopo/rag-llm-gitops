# 10.2. API endpoints

The following API endpoints are available: 

  * `/apis/monitoring.coreos.com/v1/prometheusrules`

    * `GET`: list objects of kind PrometheusRule 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules`

    * `DELETE`: delete collection of PrometheusRule 
    * `GET`: list objects of kind PrometheusRule 
    * `POST`: create a PrometheusRule 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules/{name}`

    * `DELETE`: delete a PrometheusRule 
    * `GET`: read the specified PrometheusRule 
    * `PATCH`: partially update the specified PrometheusRule 
    * `PUT`: replace the specified PrometheusRule 

  * `/apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules/{name}/status`

    * `GET`: read status of the specified PrometheusRule 
    * `PATCH`: partially update status of the specified PrometheusRule 
    * `PUT`: replace status of the specified PrometheusRule 




## 10.2.1. /apis/monitoring.coreos.com/v1/prometheusrules

HTTP method
     `GET`
Description
     list objects of kind PrometheusRule 

Table 10.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PrometheusRuleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-monitoring-v1-PrometheusRuleList) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.2. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules

HTTP method
     `DELETE`
Description
     delete collection of PrometheusRule 

Table 10.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind PrometheusRule 

Table 10.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PrometheusRuleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-monitoring-v1-PrometheusRuleList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a PrometheusRule 

Table 10.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 10.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema   
202 - Accepted  |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.3. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules/{name}

Table 10.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PrometheusRule   
Show more

HTTP method
     `DELETE`
Description
     delete a PrometheusRule 

Table 10.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 10.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified PrometheusRule 

Table 10.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified PrometheusRule 

Table 10.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified PrometheusRule 

Table 10.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 10.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.4. /apis/monitoring.coreos.com/v1/namespaces/{namespace}/prometheusrules/{name}/status

Table 10.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PrometheusRule   
Show more

HTTP method
     `GET`
Description
     read status of the specified PrometheusRule 

Table 10.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified PrometheusRule 

Table 10.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified PrometheusRule 

Table 10.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema  |   
Show more

Table 10.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema   
201 - Created  |  [`PrometheusRule`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/prometheusrule-monitoring-coreos-com-v1 "Chapter 10. PrometheusRule \[monitoring.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
