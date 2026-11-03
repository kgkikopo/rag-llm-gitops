# 16.2. API endpoints

The following API endpoints are available: 

  * `/apis/apps/v1/replicasets`

    * `GET`: list or watch objects of kind ReplicaSet 

  * `/apis/apps/v1/watch/replicasets`

    * `GET`: watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/apps/v1/namespaces/{namespace}/replicasets`

    * `DELETE`: delete collection of ReplicaSet 
    * `GET`: list or watch objects of kind ReplicaSet 
    * `POST`: create a ReplicaSet 

  * `/apis/apps/v1/watch/namespaces/{namespace}/replicasets`

    * `GET`: watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/apps/v1/namespaces/{namespace}/replicasets/{name}`

    * `DELETE`: delete a ReplicaSet 
    * `GET`: read the specified ReplicaSet 
    * `PATCH`: partially update the specified ReplicaSet 
    * `PUT`: replace the specified ReplicaSet 

  * `/apis/apps/v1/watch/namespaces/{namespace}/replicasets/{name}`

    * `GET`: watch changes to an object of kind ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/apps/v1/namespaces/{namespace}/replicasets/{name}/status`

    * `GET`: read status of the specified ReplicaSet 
    * `PATCH`: partially update status of the specified ReplicaSet 
    * `PUT`: replace status of the specified ReplicaSet 




## 16.2.1. /apis/apps/v1/replicasets

HTTP method
     `GET`
Description
     list or watch objects of kind ReplicaSet 

Table 16.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicaSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-apps-v1-ReplicaSetList) schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.2. /apis/apps/v1/watch/replicasets

HTTP method
     `GET`
Description
     watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead. 

Table 16.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.3. /apis/apps/v1/namespaces/{namespace}/replicasets

HTTP method
     `DELETE`
Description
     delete collection of ReplicaSet 

Table 16.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 16.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind ReplicaSet 

Table 16.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicaSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-apps-v1-ReplicaSetList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ReplicaSet 

Table 16.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema  |   
Show more

Table 16.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
201 - Created  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
202 - Accepted  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.4. /apis/apps/v1/watch/namespaces/{namespace}/replicasets

HTTP method
     `GET`
Description
     watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead. 

Table 16.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.5. /apis/apps/v1/namespaces/{namespace}/replicasets/{name}

Table 16.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ReplicaSet   
Show more

HTTP method
     `DELETE`
Description
     delete a ReplicaSet 

Table 16.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 16.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ReplicaSet 

Table 16.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ReplicaSet 

Table 16.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
201 - Created  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ReplicaSet 

Table 16.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema  |   
Show more

Table 16.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
201 - Created  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.6. /apis/apps/v1/watch/namespaces/{namespace}/replicasets/{name}

Table 16.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ReplicaSet   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 16.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.7. /apis/apps/v1/namespaces/{namespace}/replicasets/{name}/status

Table 16.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ReplicaSet   
Show more

HTTP method
     `GET`
Description
     read status of the specified ReplicaSet 

Table 16.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ReplicaSet 

Table 16.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
201 - Created  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ReplicaSet 

Table 16.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema  |   
Show more

Table 16.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
201 - Created  |  [`ReplicaSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/replicaset-apps-v1 "Chapter 16. ReplicaSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
