# 12.2. API endpoints

The following API endpoints are available: 

  * `/api/v1/endpoints`

    * `GET`: list or watch objects of kind Endpoints 

  * `/api/v1/watch/endpoints`

    * `GET`: watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/endpoints`

    * `DELETE`: delete collection of Endpoints 
    * `GET`: list or watch objects of kind Endpoints 
    * `POST`: create Endpoints 

  * `/api/v1/watch/namespaces/{namespace}/endpoints`

    * `GET`: watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/endpoints/{name}`

    * `DELETE`: delete Endpoints 
    * `GET`: read the specified Endpoints 
    * `PATCH`: partially update the specified Endpoints 
    * `PUT`: replace the specified Endpoints 

  * `/api/v1/watch/namespaces/{namespace}/endpoints/{name}`

    * `GET`: watch changes to an object of kind Endpoints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 12.2.1. /api/v1/endpoints

HTTP method
     `GET`
Description
     list or watch objects of kind Endpoints 

Table 12.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EndpointsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-EndpointsList) schema   
401 - Unauthorized  |  Empty   
Show more

## 12.2.2. /api/v1/watch/endpoints

HTTP method
     `GET`
Description
     watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead. 

Table 12.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 12.2.3. /api/v1/namespaces/{namespace}/endpoints

HTTP method
     `DELETE`
Description
     delete collection of Endpoints 

Table 12.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 12.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Endpoints 

Table 12.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EndpointsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-EndpointsList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create Endpoints 

Table 12.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 12.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Endpoints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/endpoints-v1 "Chapter 12. Endpoints \[v1\]") schema  |   
Show more

Table 12.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Endpoints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/endpoints-v1 "Chapter 12. Endpoints \[v1\]") schema   
201 - Created  |  [`Endpoints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/endpoints-v1 "Chapter 12. Endpoints \[v1\]") schema   
202 - Accepted  |  [`Endpoints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/endpoints-v1 "Chapter 12. Endpoints \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 12.2.4. /api/v1/watch/namespaces/{namespace}/endpoints

HTTP method
     `GET`
Description
     watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead. 

Table 12.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 12.2.5. /api/v1/namespaces/{namespace}/endpoints/{name}

Table 12.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Endpoints   
Show more

HTTP method
     `DELETE`
Description
     delete Endpoints 

Table 12.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 12.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Endpoints 

Table 12.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Endpoints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/endpoints-v1 "Chapter 12. Endpoints \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Endpoints 

Table 12.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 12.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Endpoints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/endpoints-v1 "Chapter 12. Endpoints \[v1\]") schema   
201 - Created  |  [`Endpoints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/endpoints-v1 "Chapter 12. Endpoints \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Endpoints 

Table 12.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 12.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Endpoints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/endpoints-v1 "Chapter 12. Endpoints \[v1\]") schema  |   
Show more

Table 12.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Endpoints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/endpoints-v1 "Chapter 12. Endpoints \[v1\]") schema   
201 - Created  |  [`Endpoints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/endpoints-v1 "Chapter 12. Endpoints \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 12.2.6. /api/v1/watch/namespaces/{namespace}/endpoints/{name}

Table 12.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Endpoints   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Endpoints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 12.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
