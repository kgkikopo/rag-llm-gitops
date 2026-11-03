# 3.2. API endpoints

The following API endpoints are available: 

  * `/apis/monitoring.coreos.com/v1beta1/alertmanagerconfigs`

    * `GET`: list objects of kind AlertmanagerConfig 

  * `/apis/monitoring.coreos.com/v1beta1/namespaces/{namespace}/alertmanagerconfigs`

    * `DELETE`: delete collection of AlertmanagerConfig 
    * `GET`: list objects of kind AlertmanagerConfig 
    * `POST`: create an AlertmanagerConfig 

  * `/apis/monitoring.coreos.com/v1beta1/namespaces/{namespace}/alertmanagerconfigs/{name}`

    * `DELETE`: delete an AlertmanagerConfig 
    * `GET`: read the specified AlertmanagerConfig 
    * `PATCH`: partially update the specified AlertmanagerConfig 
    * `PUT`: replace the specified AlertmanagerConfig 

  * `/apis/monitoring.coreos.com/v1beta1/namespaces/{namespace}/alertmanagerconfigs/{name}/status`

    * `GET`: read status of the specified AlertmanagerConfig 
    * `PATCH`: partially update status of the specified AlertmanagerConfig 
    * `PUT`: replace status of the specified AlertmanagerConfig 




## 3.2.1. /apis/monitoring.coreos.com/v1beta1/alertmanagerconfigs

HTTP method
     `GET`
Description
     list objects of kind AlertmanagerConfig 

Table 3.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertmanagerConfigList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-monitoring-v1beta1-AlertmanagerConfigList) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.2. /apis/monitoring.coreos.com/v1beta1/namespaces/{namespace}/alertmanagerconfigs

HTTP method
     `DELETE`
Description
     delete collection of AlertmanagerConfig 

Table 3.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind AlertmanagerConfig 

Table 3.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertmanagerConfigList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-monitoring-v1beta1-AlertmanagerConfigList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an AlertmanagerConfig 

Table 3.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema  |   
Show more

Table 3.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema   
201 - Created  |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema   
202 - Accepted  |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.3. /apis/monitoring.coreos.com/v1beta1/namespaces/{namespace}/alertmanagerconfigs/{name}

Table 3.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the AlertmanagerConfig   
Show more

HTTP method
     `DELETE`
Description
     delete an AlertmanagerConfig 

Table 3.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified AlertmanagerConfig 

Table 3.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified AlertmanagerConfig 

Table 3.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified AlertmanagerConfig 

Table 3.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema  |   
Show more

Table 3.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema   
201 - Created  |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.4. /apis/monitoring.coreos.com/v1beta1/namespaces/{namespace}/alertmanagerconfigs/{name}/status

Table 3.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the AlertmanagerConfig   
Show more

HTTP method
     `GET`
Description
     read status of the specified AlertmanagerConfig 

Table 3.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified AlertmanagerConfig 

Table 3.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified AlertmanagerConfig 

Table 3.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema  |   
Show more

Table 3.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema   
201 - Created  |  [`AlertmanagerConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1 "Chapter 3. AlertmanagerConfig \[monitoring.coreos.com/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more
