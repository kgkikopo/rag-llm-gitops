# 14.2. API endpoints

The following API endpoints are available: 

  * `/api/v1/pods`

    * `GET`: list or watch objects of kind Pod 

  * `/api/v1/watch/pods`

    * `GET`: watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/pods`

    * `DELETE`: delete collection of Pod 
    * `GET`: list or watch objects of kind Pod 
    * `POST`: create a Pod 

  * `/api/v1/watch/namespaces/{namespace}/pods`

    * `GET`: watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/pods/{name}`

    * `DELETE`: delete a Pod 
    * `GET`: read the specified Pod 
    * `PATCH`: partially update the specified Pod 
    * `PUT`: replace the specified Pod 

  * `/api/v1/namespaces/{namespace}/pods/{name}/log`

    * `GET`: read log of the specified Pod 

  * `/api/v1/watch/namespaces/{namespace}/pods/{name}`

    * `GET`: watch changes to an object of kind Pod. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/api/v1/namespaces/{namespace}/pods/{name}/resize`

    * `GET`: read resize of the specified Pod 
    * `PATCH`: partially update resize of the specified Pod 
    * `PUT`: replace resize of the specified Pod 

  * `/api/v1/namespaces/{namespace}/pods/{name}/status`

    * `GET`: read status of the specified Pod 
    * `PATCH`: partially update status of the specified Pod 
    * `PUT`: replace status of the specified Pod 

  * `/api/v1/namespaces/{namespace}/pods/{name}/ephemeralcontainers`

    * `GET`: read ephemeralcontainers of the specified Pod 
    * `PATCH`: partially update ephemeralcontainers of the specified Pod 
    * `PUT`: replace ephemeralcontainers of the specified Pod 




## 14.2.1. /api/v1/pods

HTTP method
     `GET`
Description
     list or watch objects of kind Pod 

Table 14.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodList) schema   
401 - Unauthorized  |  Empty   
Show more

## 14.2.2. /api/v1/watch/pods

HTTP method
     `GET`
Description
     watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead. 

Table 14.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 14.2.3. /api/v1/namespaces/{namespace}/pods

HTTP method
     `DELETE`
Description
     delete collection of Pod 

Table 14.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 14.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Pod 

Table 14.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Pod 

Table 14.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 14.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema  |   
Show more

Table 14.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
201 - Created  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
202 - Accepted  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 14.2.4. /api/v1/watch/namespaces/{namespace}/pods

HTTP method
     `GET`
Description
     watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead. 

Table 14.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 14.2.5. /api/v1/namespaces/{namespace}/pods/{name}

Table 14.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Pod   
Show more

HTTP method
     `DELETE`
Description
     delete a Pod 

Table 14.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 14.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
202 - Accepted  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Pod 

Table 14.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Pod 

Table 14.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 14.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
201 - Created  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Pod 

Table 14.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 14.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema  |   
Show more

Table 14.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
201 - Created  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 14.2.6. /api/v1/namespaces/{namespace}/pods/{name}/log

Table 14.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Pod   
Show more

HTTP method
     `GET`
Description
     read log of the specified Pod 

Table 14.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  `string`  
401 - Unauthorized  |  Empty   
Show more

## 14.2.7. /api/v1/watch/namespaces/{namespace}/pods/{name}

Table 14.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Pod   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Pod. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 14.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 14.2.8. /api/v1/namespaces/{namespace}/pods/{name}/resize

Table 14.23. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Pod   
Show more

HTTP method
     `GET`
Description
     read resize of the specified Pod 

Table 14.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update resize of the specified Pod 

Table 14.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 14.26. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
201 - Created  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace resize of the specified Pod 

Table 14.27. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 14.28. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema  |   
Show more

Table 14.29. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
201 - Created  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 14.2.9. /api/v1/namespaces/{namespace}/pods/{name}/status

Table 14.30. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Pod   
Show more

HTTP method
     `GET`
Description
     read status of the specified Pod 

Table 14.31. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Pod 

Table 14.32. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 14.33. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
201 - Created  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Pod 

Table 14.34. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 14.35. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema  |   
Show more

Table 14.36. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
201 - Created  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 14.2.10. /api/v1/namespaces/{namespace}/pods/{name}/ephemeralcontainers

Table 14.37. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Pod   
Show more

HTTP method
     `GET`
Description
     read ephemeralcontainers of the specified Pod 

Table 14.38. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update ephemeralcontainers of the specified Pod 

Table 14.39. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 14.40. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
201 - Created  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace ephemeralcontainers of the specified Pod 

Table 14.41. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 14.42. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema  |   
Show more

Table 14.43. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
201 - Created  |  [`Pod`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/pod-v1 "Chapter 14. Pod \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
