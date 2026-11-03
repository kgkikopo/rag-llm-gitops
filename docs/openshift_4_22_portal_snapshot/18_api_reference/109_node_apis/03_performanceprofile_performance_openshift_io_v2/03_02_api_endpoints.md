# 3.2. API endpoints

The following API endpoints are available: 

  * `/apis/performance.openshift.io/v2/performanceprofiles`

    * `DELETE`: delete collection of PerformanceProfile 
    * `GET`: list objects of kind PerformanceProfile 
    * `POST`: create a PerformanceProfile 

  * `/apis/performance.openshift.io/v2/performanceprofiles/{name}`

    * `DELETE`: delete a PerformanceProfile 
    * `GET`: read the specified PerformanceProfile 
    * `PATCH`: partially update the specified PerformanceProfile 
    * `PUT`: replace the specified PerformanceProfile 

  * `/apis/performance.openshift.io/v2/performanceprofiles/{name}/status`

    * `GET`: read status of the specified PerformanceProfile 
    * `PATCH`: partially update status of the specified PerformanceProfile 
    * `PUT`: replace status of the specified PerformanceProfile 




## 3.2.1. /apis/performance.openshift.io/v2/performanceprofiles

HTTP method
     `DELETE`
Description
     delete collection of PerformanceProfile 

Table 3.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind PerformanceProfile 

Table 3.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PerformanceProfileList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-performance-v2-PerformanceProfileList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a PerformanceProfile 

Table 3.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema  |   
Show more

Table 3.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema   
201 - Created  |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema   
202 - Accepted  |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.2. /apis/performance.openshift.io/v2/performanceprofiles/{name}

Table 3.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PerformanceProfile   
Show more

HTTP method
     `DELETE`
Description
     delete a PerformanceProfile 

Table 3.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified PerformanceProfile 

Table 3.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified PerformanceProfile 

Table 3.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified PerformanceProfile 

Table 3.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema  |   
Show more

Table 3.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema   
201 - Created  |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.3. /apis/performance.openshift.io/v2/performanceprofiles/{name}/status

Table 3.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PerformanceProfile   
Show more

HTTP method
     `GET`
Description
     read status of the specified PerformanceProfile 

Table 3.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified PerformanceProfile 

Table 3.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified PerformanceProfile 

Table 3.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema  |   
Show more

Table 3.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema   
201 - Created  |  [`PerformanceProfile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/performanceprofile-performance-openshift-io-v2 "Chapter 3. PerformanceProfile \[performance.openshift.io/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more
