# 31.2. API endpoints

The following API endpoints are available: 

  * `/apis/route.openshift.io/v1/routes`

    * `GET`: list or watch objects of kind Route 

  * `/apis/route.openshift.io/v1/watch/routes`

    * `GET`: watch individual changes to a list of Route. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/route.openshift.io/v1/namespaces/{namespace}/routes`

    * `DELETE`: delete collection of Route 
    * `GET`: list or watch objects of kind Route 
    * `POST`: create a Route 

  * `/apis/route.openshift.io/v1/watch/namespaces/{namespace}/routes`

    * `GET`: watch individual changes to a list of Route. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/route.openshift.io/v1/namespaces/{namespace}/routes/{name}`

    * `DELETE`: delete a Route 
    * `GET`: read the specified Route 
    * `PATCH`: partially update the specified Route 
    * `PUT`: replace the specified Route 

  * `/apis/route.openshift.io/v1/watch/namespaces/{namespace}/routes/{name}`

    * `GET`: watch changes to an object of kind Route. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/route.openshift.io/v1/namespaces/{namespace}/routes/{name}/status`

    * `GET`: read status of the specified Route 
    * `PATCH`: partially update status of the specified Route 
    * `PUT`: replace status of the specified Route 




## 31.2.1. /apis/route.openshift.io/v1/routes

HTTP method
     `GET`
Description
     list or watch objects of kind Route 

Table 31.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RouteList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-route-v1-RouteList) schema   
401 - Unauthorized  |  Empty   
Show more

## 31.2.2. /apis/route.openshift.io/v1/watch/routes

HTTP method
     `GET`
Description
     watch individual changes to a list of Route. deprecated: use the 'watch' parameter with a list operation instead. 

Table 31.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 31.2.3. /apis/route.openshift.io/v1/namespaces/{namespace}/routes

HTTP method
     `DELETE`
Description
     delete collection of Route 

Table 31.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 31.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Route 

Table 31.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RouteList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-route-v1-RouteList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Route 

Table 31.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 31.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema  |   
Show more

Table 31.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
201 - Created  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
202 - Accepted  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 31.2.4. /apis/route.openshift.io/v1/watch/namespaces/{namespace}/routes

HTTP method
     `GET`
Description
     watch individual changes to a list of Route. deprecated: use the 'watch' parameter with a list operation instead. 

Table 31.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 31.2.5. /apis/route.openshift.io/v1/namespaces/{namespace}/routes/{name}

Table 31.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Route   
Show more

HTTP method
     `DELETE`
Description
     delete a Route 

Table 31.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 31.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Route 

Table 31.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Route 

Table 31.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 31.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
201 - Created  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Route 

Table 31.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 31.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema  |   
Show more

Table 31.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
201 - Created  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 31.2.6. /apis/route.openshift.io/v1/watch/namespaces/{namespace}/routes/{name}

Table 31.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Route   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Route. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 31.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 31.2.7. /apis/route.openshift.io/v1/namespaces/{namespace}/routes/{name}/status

Table 31.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Route   
Show more

HTTP method
     `GET`
Description
     read status of the specified Route 

Table 31.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Route 

Table 31.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 31.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
201 - Created  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Route 

Table 31.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 31.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema  |   
Show more

Table 31.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
201 - Created  |  [`Route`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/route-route-openshift-io-v1 "Chapter 31. Route \[route.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
