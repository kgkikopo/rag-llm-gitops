# 7.2. API endpoints

The following API endpoints are available: 

  * `/apis/apps/v1/daemonsets`

    * `GET`: list or watch objects of kind DaemonSet 

  * `/apis/apps/v1/watch/daemonsets`

    * `GET`: watch individual changes to a list of DaemonSet. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/apps/v1/namespaces/{namespace}/daemonsets`

    * `DELETE`: delete collection of DaemonSet 
    * `GET`: list or watch objects of kind DaemonSet 
    * `POST`: create a DaemonSet 

  * `/apis/apps/v1/watch/namespaces/{namespace}/daemonsets`

    * `GET`: watch individual changes to a list of DaemonSet. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/apps/v1/namespaces/{namespace}/daemonsets/{name}`

    * `DELETE`: delete a DaemonSet 
    * `GET`: read the specified DaemonSet 
    * `PATCH`: partially update the specified DaemonSet 
    * `PUT`: replace the specified DaemonSet 

  * `/apis/apps/v1/watch/namespaces/{namespace}/daemonsets/{name}`

    * `GET`: watch changes to an object of kind DaemonSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/apps/v1/namespaces/{namespace}/daemonsets/{name}/status`

    * `GET`: read status of the specified DaemonSet 
    * `PATCH`: partially update status of the specified DaemonSet 
    * `PUT`: replace status of the specified DaemonSet 




## 7.2.1. /apis/apps/v1/daemonsets

HTTP method
     `GET`
Description
     list or watch objects of kind DaemonSet 

Table 7.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DaemonSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-apps-v1-DaemonSetList) schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.2. /apis/apps/v1/watch/daemonsets

HTTP method
     `GET`
Description
     watch individual changes to a list of DaemonSet. deprecated: use the 'watch' parameter with a list operation instead. 

Table 7.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.3. /apis/apps/v1/namespaces/{namespace}/daemonsets

HTTP method
     `DELETE`
Description
     delete collection of DaemonSet 

Table 7.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 7.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind DaemonSet 

Table 7.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DaemonSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-apps-v1-DaemonSetList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a DaemonSet 

Table 7.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema  |   
Show more

Table 7.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
201 - Created  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
202 - Accepted  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.4. /apis/apps/v1/watch/namespaces/{namespace}/daemonsets

HTTP method
     `GET`
Description
     watch individual changes to a list of DaemonSet. deprecated: use the 'watch' parameter with a list operation instead. 

Table 7.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.5. /apis/apps/v1/namespaces/{namespace}/daemonsets/{name}

Table 7.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the DaemonSet   
Show more

HTTP method
     `DELETE`
Description
     delete a DaemonSet 

Table 7.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 7.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified DaemonSet 

Table 7.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified DaemonSet 

Table 7.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
201 - Created  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified DaemonSet 

Table 7.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema  |   
Show more

Table 7.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
201 - Created  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.6. /apis/apps/v1/watch/namespaces/{namespace}/daemonsets/{name}

Table 7.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the DaemonSet   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind DaemonSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 7.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.7. /apis/apps/v1/namespaces/{namespace}/daemonsets/{name}/status

Table 7.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the DaemonSet   
Show more

HTTP method
     `GET`
Description
     read status of the specified DaemonSet 

Table 7.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified DaemonSet 

Table 7.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
201 - Created  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified DaemonSet 

Table 7.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema  |   
Show more

Table 7.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
201 - Created  |  [`DaemonSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/daemonset-apps-v1 "Chapter 7. DaemonSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
