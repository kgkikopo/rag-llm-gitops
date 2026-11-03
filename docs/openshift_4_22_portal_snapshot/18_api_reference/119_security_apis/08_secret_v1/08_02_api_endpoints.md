# 8.2. API endpoints

The following API endpoints are available: 

  * `/api/v1/secrets`

    * `GET`: list or watch objects of kind Secret 

  * `/api/v1/watch/secrets`

    * `GET`: watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/secrets`

    * `DELETE`: delete collection of Secret 
    * `GET`: list or watch objects of kind Secret 
    * `POST`: create a Secret 

  * `/api/v1/watch/namespaces/{namespace}/secrets`

    * `GET`: watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/secrets/{name}`

    * `DELETE`: delete a Secret 
    * `GET`: read the specified Secret 
    * `PATCH`: partially update the specified Secret 
    * `PUT`: replace the specified Secret 

  * `/api/v1/watch/namespaces/{namespace}/secrets/{name}`

    * `GET`: watch changes to an object of kind Secret. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 8.2.1. /api/v1/secrets

HTTP method
     `GET`
Description
     list or watch objects of kind Secret 

Table 8.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SecretList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-SecretList) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.2. /api/v1/watch/secrets

HTTP method
     `GET`
Description
     watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead. 

Table 8.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.3. /api/v1/namespaces/{namespace}/secrets

HTTP method
     `DELETE`
Description
     delete collection of Secret 

Table 8.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 8.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Secret 

Table 8.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SecretList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-SecretList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Secret 

Table 8.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Secret`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/secret-v1 "Chapter 8. Secret \[v1\]") schema  |   
Show more

Table 8.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Secret`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/secret-v1 "Chapter 8. Secret \[v1\]") schema   
201 - Created  |  [`Secret`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/secret-v1 "Chapter 8. Secret \[v1\]") schema   
202 - Accepted  |  [`Secret`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/secret-v1 "Chapter 8. Secret \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.4. /api/v1/watch/namespaces/{namespace}/secrets

HTTP method
     `GET`
Description
     watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead. 

Table 8.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.5. /api/v1/namespaces/{namespace}/secrets/{name}

Table 8.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Secret   
Show more

HTTP method
     `DELETE`
Description
     delete a Secret 

Table 8.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 8.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Secret 

Table 8.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Secret`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/secret-v1 "Chapter 8. Secret \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Secret 

Table 8.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Secret`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/secret-v1 "Chapter 8. Secret \[v1\]") schema   
201 - Created  |  [`Secret`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/secret-v1 "Chapter 8. Secret \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Secret 

Table 8.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Secret`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/secret-v1 "Chapter 8. Secret \[v1\]") schema  |   
Show more

Table 8.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Secret`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/secret-v1 "Chapter 8. Secret \[v1\]") schema   
201 - Created  |  [`Secret`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/secret-v1 "Chapter 8. Secret \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.6. /api/v1/watch/namespaces/{namespace}/secrets/{name}

Table 8.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Secret   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Secret. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 8.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
