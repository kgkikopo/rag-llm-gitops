# 32.2. API endpoints

The following API endpoints are available: 

  * `/api/v1/services`

    * `GET`: list or watch objects of kind Service 

  * `/api/v1/watch/services`

    * `GET`: watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/services`

    * `DELETE`: delete collection of Service 
    * `GET`: list or watch objects of kind Service 
    * `POST`: create a Service 

  * `/api/v1/watch/namespaces/{namespace}/services`

    * `GET`: watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/services/{name}`

    * `DELETE`: delete a Service 
    * `GET`: read the specified Service 
    * `PATCH`: partially update the specified Service 
    * `PUT`: replace the specified Service 

  * `/api/v1/watch/namespaces/{namespace}/services/{name}`

    * `GET`: watch changes to an object of kind Service. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/api/v1/namespaces/{namespace}/services/{name}/status`

    * `GET`: read status of the specified Service 
    * `PATCH`: partially update status of the specified Service 
    * `PUT`: replace status of the specified Service 




## 32.2.1. /api/v1/services

HTTP method
     `GET`
Description
     list or watch objects of kind Service 

Table 32.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ServiceList) schema   
401 - Unauthorized  |  Empty   
Show more

## 32.2.2. /api/v1/watch/services

HTTP method
     `GET`
Description
     watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead. 

Table 32.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 32.2.3. /api/v1/namespaces/{namespace}/services

HTTP method
     `DELETE`
Description
     delete collection of Service 

Table 32.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 32.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Service 

Table 32.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ServiceList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Service 

Table 32.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 32.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema  |   
Show more

Table 32.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
201 - Created  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
202 - Accepted  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 32.2.4. /api/v1/watch/namespaces/{namespace}/services

HTTP method
     `GET`
Description
     watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead. 

Table 32.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 32.2.5. /api/v1/namespaces/{namespace}/services/{name}

Table 32.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Service   
Show more

HTTP method
     `DELETE`
Description
     delete a Service 

Table 32.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 32.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
202 - Accepted  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Service 

Table 32.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Service 

Table 32.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 32.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
201 - Created  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Service 

Table 32.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 32.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema  |   
Show more

Table 32.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
201 - Created  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 32.2.6. /api/v1/watch/namespaces/{namespace}/services/{name}

Table 32.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Service   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Service. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 32.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 32.2.7. /api/v1/namespaces/{namespace}/services/{name}/status

Table 32.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Service   
Show more

HTTP method
     `GET`
Description
     read status of the specified Service 

Table 32.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Service 

Table 32.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 32.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
201 - Created  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Service 

Table 32.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 32.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema  |   
Show more

Table 32.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
201 - Created  |  [`Service`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/service-v1 "Chapter 32. Service \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
