# 15.2. API endpoints

The following API endpoints are available: 

  * `/api/v1/replicationcontrollers`

    * `GET`: list or watch objects of kind ReplicationController 

  * `/api/v1/watch/replicationcontrollers`

    * `GET`: watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/replicationcontrollers`

    * `DELETE`: delete collection of ReplicationController 
    * `GET`: list or watch objects of kind ReplicationController 
    * `POST`: create a ReplicationController 

  * `/api/v1/watch/namespaces/{namespace}/replicationcontrollers`

    * `GET`: watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/replicationcontrollers/{name}`

    * `DELETE`: delete a ReplicationController 
    * `GET`: read the specified ReplicationController 
    * `PATCH`: partially update the specified ReplicationController 
    * `PUT`: replace the specified ReplicationController 

  * `/api/v1/watch/namespaces/{namespace}/replicationcontrollers/{name}`

    * `GET`: watch changes to an object of kind ReplicationController. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status`

    * `GET`: read status of the specified ReplicationController 
    * `PATCH`: partially update status of the specified ReplicationController 
    * `PUT`: replace status of the specified ReplicationController 




## 15.2.1. /api/v1/replicationcontrollers

HTTP method
     `GET`
Description
     list or watch objects of kind ReplicationController 

Table 15.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicationControllerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ReplicationControllerList) schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.2. /api/v1/watch/replicationcontrollers

HTTP method
     `GET`
Description
     watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead. 

Table 15.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.3. /api/v1/namespaces/{namespace}/replicationcontrollers

HTTP method
     `DELETE`
Description
     delete collection of ReplicationController 

Table 15.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 15.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind ReplicationController 

Table 15.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicationControllerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ReplicationControllerList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ReplicationController 

Table 15.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema  |   
Show more

Table 15.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
201 - Created  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
202 - Accepted  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.4. /api/v1/watch/namespaces/{namespace}/replicationcontrollers

HTTP method
     `GET`
Description
     watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead. 

Table 15.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.5. /api/v1/namespaces/{namespace}/replicationcontrollers/{name}

Table 15.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ReplicationController   
Show more

HTTP method
     `DELETE`
Description
     delete a ReplicationController 

Table 15.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 15.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ReplicationController 

Table 15.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ReplicationController 

Table 15.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
201 - Created  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ReplicationController 

Table 15.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema  |   
Show more

Table 15.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
201 - Created  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.6. /api/v1/watch/namespaces/{namespace}/replicationcontrollers/{name}

Table 15.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ReplicationController   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind ReplicationController. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 15.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.7. /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status

Table 15.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ReplicationController   
Show more

HTTP method
     `GET`
Description
     read status of the specified ReplicationController 

Table 15.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ReplicationController 

Table 15.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
201 - Created  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ReplicationController 

Table 15.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema  |   
Show more

Table 15.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
201 - Created  |  [`ReplicationController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicationcontroller-v1 "Chapter 15. ReplicationController \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
