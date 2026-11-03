# 8.2. API endpoints

The following API endpoints are available: 

  * `/apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations`

    * `DELETE`: delete collection of PriorityLevelConfiguration 
    * `GET`: list or watch objects of kind PriorityLevelConfiguration 
    * `POST`: create a PriorityLevelConfiguration 

  * `/apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations`

    * `GET`: watch individual changes to a list of PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}`

    * `DELETE`: delete a PriorityLevelConfiguration 
    * `GET`: read the specified PriorityLevelConfiguration 
    * `PATCH`: partially update the specified PriorityLevelConfiguration 
    * `PUT`: replace the specified PriorityLevelConfiguration 

  * `/apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations/{name}`

    * `GET`: watch changes to an object of kind PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}/status`

    * `GET`: read status of the specified PriorityLevelConfiguration 
    * `PATCH`: partially update status of the specified PriorityLevelConfiguration 
    * `PUT`: replace status of the specified PriorityLevelConfiguration 




## 8.2.1. /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations

HTTP method
     `DELETE`
Description
     delete collection of PriorityLevelConfiguration 

Table 8.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 8.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind PriorityLevelConfiguration 

Table 8.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PriorityLevelConfigurationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-flowcontrol-v1-PriorityLevelConfigurationList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a PriorityLevelConfiguration 

Table 8.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema  |   
Show more

Table 8.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
201 - Created  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
202 - Accepted  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.2. /apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations

HTTP method
     `GET`
Description
     watch individual changes to a list of PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead. 

Table 8.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.3. /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}

Table 8.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PriorityLevelConfiguration   
Show more

HTTP method
     `DELETE`
Description
     delete a PriorityLevelConfiguration 

Table 8.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 8.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified PriorityLevelConfiguration 

Table 8.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified PriorityLevelConfiguration 

Table 8.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
201 - Created  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified PriorityLevelConfiguration 

Table 8.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema  |   
Show more

Table 8.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
201 - Created  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.4. /apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations/{name}

Table 8.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PriorityLevelConfiguration   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 8.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.5. /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}/status

Table 8.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PriorityLevelConfiguration   
Show more

HTTP method
     `GET`
Description
     read status of the specified PriorityLevelConfiguration 

Table 8.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified PriorityLevelConfiguration 

Table 8.21. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
201 - Created  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified PriorityLevelConfiguration 

Table 8.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.24. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema  |   
Show more

Table 8.25. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
201 - Created  |  [`PriorityLevelConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1 "Chapter 8. PriorityLevelConfiguration \[flowcontrol.apiserver.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
