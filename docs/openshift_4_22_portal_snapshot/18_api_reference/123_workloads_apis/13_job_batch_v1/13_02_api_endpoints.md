# 13.2. API endpoints

The following API endpoints are available: 

  * `/apis/batch/v1/jobs`

    * `GET`: list or watch objects of kind Job 

  * `/apis/batch/v1/watch/jobs`

    * `GET`: watch individual changes to a list of Job. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/batch/v1/namespaces/{namespace}/jobs`

    * `DELETE`: delete collection of Job 
    * `GET`: list or watch objects of kind Job 
    * `POST`: create a Job 

  * `/apis/batch/v1/watch/namespaces/{namespace}/jobs`

    * `GET`: watch individual changes to a list of Job. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/batch/v1/namespaces/{namespace}/jobs/{name}`

    * `DELETE`: delete a Job 
    * `GET`: read the specified Job 
    * `PATCH`: partially update the specified Job 
    * `PUT`: replace the specified Job 

  * `/apis/batch/v1/watch/namespaces/{namespace}/jobs/{name}`

    * `GET`: watch changes to an object of kind Job. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/batch/v1/namespaces/{namespace}/jobs/{name}/status`

    * `GET`: read status of the specified Job 
    * `PATCH`: partially update status of the specified Job 
    * `PUT`: replace status of the specified Job 




## 13.2.1. /apis/batch/v1/jobs

HTTP method
     `GET`
Description
     list or watch objects of kind Job 

Table 13.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`JobList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-batch-v1-JobList) schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.2. /apis/batch/v1/watch/jobs

HTTP method
     `GET`
Description
     watch individual changes to a list of Job. deprecated: use the 'watch' parameter with a list operation instead. 

Table 13.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.3. /apis/batch/v1/namespaces/{namespace}/jobs

HTTP method
     `DELETE`
Description
     delete collection of Job 

Table 13.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 13.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Job 

Table 13.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`JobList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-batch-v1-JobList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Job 

Table 13.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema  |   
Show more

Table 13.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
201 - Created  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
202 - Accepted  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.4. /apis/batch/v1/watch/namespaces/{namespace}/jobs

HTTP method
     `GET`
Description
     watch individual changes to a list of Job. deprecated: use the 'watch' parameter with a list operation instead. 

Table 13.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.5. /apis/batch/v1/namespaces/{namespace}/jobs/{name}

Table 13.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Job   
Show more

HTTP method
     `DELETE`
Description
     delete a Job 

Table 13.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 13.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Job 

Table 13.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Job 

Table 13.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
201 - Created  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Job 

Table 13.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema  |   
Show more

Table 13.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
201 - Created  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.6. /apis/batch/v1/watch/namespaces/{namespace}/jobs/{name}

Table 13.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Job   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Job. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 13.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.7. /apis/batch/v1/namespaces/{namespace}/jobs/{name}/status

Table 13.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Job   
Show more

HTTP method
     `GET`
Description
     read status of the specified Job 

Table 13.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Job 

Table 13.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
201 - Created  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Job 

Table 13.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema  |   
Show more

Table 13.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
201 - Created  |  [`Job`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/job-batch-v1 "Chapter 13. Job \[batch/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
