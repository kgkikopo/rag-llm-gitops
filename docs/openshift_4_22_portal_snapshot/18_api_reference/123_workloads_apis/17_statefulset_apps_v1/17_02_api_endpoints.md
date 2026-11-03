# 17.2. API endpoints

The following API endpoints are available: 

  * `/apis/apps/v1/statefulsets`

    * `GET`: list or watch objects of kind StatefulSet 

  * `/apis/apps/v1/watch/statefulsets`

    * `GET`: watch individual changes to a list of StatefulSet. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/apps/v1/namespaces/{namespace}/statefulsets`

    * `DELETE`: delete collection of StatefulSet 
    * `GET`: list or watch objects of kind StatefulSet 
    * `POST`: create a StatefulSet 

  * `/apis/apps/v1/watch/namespaces/{namespace}/statefulsets`

    * `GET`: watch individual changes to a list of StatefulSet. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/apps/v1/namespaces/{namespace}/statefulsets/{name}`

    * `DELETE`: delete a StatefulSet 
    * `GET`: read the specified StatefulSet 
    * `PATCH`: partially update the specified StatefulSet 
    * `PUT`: replace the specified StatefulSet 

  * `/apis/apps/v1/watch/namespaces/{namespace}/statefulsets/{name}`

    * `GET`: watch changes to an object of kind StatefulSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/apps/v1/namespaces/{namespace}/statefulsets/{name}/status`

    * `GET`: read status of the specified StatefulSet 
    * `PATCH`: partially update status of the specified StatefulSet 
    * `PUT`: replace status of the specified StatefulSet 




## 17.2.1. /apis/apps/v1/statefulsets

HTTP method
     `GET`
Description
     list or watch objects of kind StatefulSet 

Table 17.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`StatefulSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-apps-v1-StatefulSetList) schema   
401 - Unauthorized  |  Empty   
Show more

## 17.2.2. /apis/apps/v1/watch/statefulsets

HTTP method
     `GET`
Description
     watch individual changes to a list of StatefulSet. deprecated: use the 'watch' parameter with a list operation instead. 

Table 17.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 17.2.3. /apis/apps/v1/namespaces/{namespace}/statefulsets

HTTP method
     `DELETE`
Description
     delete collection of StatefulSet 

Table 17.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 17.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind StatefulSet 

Table 17.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`StatefulSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-apps-v1-StatefulSetList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a StatefulSet 

Table 17.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 17.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema  |   
Show more

Table 17.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
201 - Created  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
202 - Accepted  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 17.2.4. /apis/apps/v1/watch/namespaces/{namespace}/statefulsets

HTTP method
     `GET`
Description
     watch individual changes to a list of StatefulSet. deprecated: use the 'watch' parameter with a list operation instead. 

Table 17.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 17.2.5. /apis/apps/v1/namespaces/{namespace}/statefulsets/{name}

Table 17.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the StatefulSet   
Show more

HTTP method
     `DELETE`
Description
     delete a StatefulSet 

Table 17.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 17.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified StatefulSet 

Table 17.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified StatefulSet 

Table 17.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 17.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
201 - Created  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified StatefulSet 

Table 17.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 17.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema  |   
Show more

Table 17.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
201 - Created  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 17.2.6. /apis/apps/v1/watch/namespaces/{namespace}/statefulsets/{name}

Table 17.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the StatefulSet   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind StatefulSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 17.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 17.2.7. /apis/apps/v1/namespaces/{namespace}/statefulsets/{name}/status

Table 17.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the StatefulSet   
Show more

HTTP method
     `GET`
Description
     read status of the specified StatefulSet 

Table 17.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified StatefulSet 

Table 17.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 17.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
201 - Created  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified StatefulSet 

Table 17.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 17.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema  |   
Show more

Table 17.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
201 - Created  |  [`StatefulSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/statefulset-apps-v1 "Chapter 17. StatefulSet \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
