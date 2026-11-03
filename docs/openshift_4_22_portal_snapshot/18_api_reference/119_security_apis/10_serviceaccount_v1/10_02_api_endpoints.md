# 10.2. API endpoints

The following API endpoints are available: 

  * `/api/v1/serviceaccounts`

    * `GET`: list or watch objects of kind ServiceAccount 

  * `/api/v1/watch/serviceaccounts`

    * `GET`: watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/serviceaccounts`

    * `DELETE`: delete collection of ServiceAccount 
    * `GET`: list or watch objects of kind ServiceAccount 
    * `POST`: create a ServiceAccount 

  * `/api/v1/watch/namespaces/{namespace}/serviceaccounts`

    * `GET`: watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/serviceaccounts/{name}`

    * `DELETE`: delete a ServiceAccount 
    * `GET`: read the specified ServiceAccount 
    * `PATCH`: partially update the specified ServiceAccount 
    * `PUT`: replace the specified ServiceAccount 

  * `/api/v1/watch/namespaces/{namespace}/serviceaccounts/{name}`

    * `GET`: watch changes to an object of kind ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 10.2.1. /api/v1/serviceaccounts

HTTP method
     `GET`
Description
     list or watch objects of kind ServiceAccount 

Table 10.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceAccountList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ServiceAccountList) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.2. /api/v1/watch/serviceaccounts

HTTP method
     `GET`
Description
     watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead. 

Table 10.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.3. /api/v1/namespaces/{namespace}/serviceaccounts

HTTP method
     `DELETE`
Description
     delete collection of ServiceAccount 

Table 10.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 10.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind ServiceAccount 

Table 10.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceAccountList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ServiceAccountList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ServiceAccount 

Table 10.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema  |   
Show more

Table 10.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema   
201 - Created  |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema   
202 - Accepted  |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.4. /api/v1/watch/namespaces/{namespace}/serviceaccounts

HTTP method
     `GET`
Description
     watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead. 

Table 10.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.5. /api/v1/namespaces/{namespace}/serviceaccounts/{name}

Table 10.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ServiceAccount   
Show more

HTTP method
     `DELETE`
Description
     delete a ServiceAccount 

Table 10.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 10.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema   
202 - Accepted  |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ServiceAccount 

Table 10.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ServiceAccount 

Table 10.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema   
201 - Created  |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ServiceAccount 

Table 10.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema  |   
Show more

Table 10.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema   
201 - Created  |  [`ServiceAccount`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/serviceaccount-v1 "Chapter 10. ServiceAccount \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.6. /api/v1/watch/namespaces/{namespace}/serviceaccounts/{name}

Table 10.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ServiceAccount   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 10.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
