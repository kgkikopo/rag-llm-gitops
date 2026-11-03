# 9.2. API endpoints

The following API endpoints are available: 

  * `/api/v1/resourcequotas`

    * `GET`: list or watch objects of kind ResourceQuota 

  * `/api/v1/watch/resourcequotas`

    * `GET`: watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/resourcequotas`

    * `DELETE`: delete collection of ResourceQuota 
    * `GET`: list or watch objects of kind ResourceQuota 
    * `POST`: create a ResourceQuota 

  * `/api/v1/watch/namespaces/{namespace}/resourcequotas`

    * `GET`: watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/resourcequotas/{name}`

    * `DELETE`: delete a ResourceQuota 
    * `GET`: read the specified ResourceQuota 
    * `PATCH`: partially update the specified ResourceQuota 
    * `PUT`: replace the specified ResourceQuota 

  * `/api/v1/watch/namespaces/{namespace}/resourcequotas/{name}`

    * `GET`: watch changes to an object of kind ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/api/v1/namespaces/{namespace}/resourcequotas/{name}/status`

    * `GET`: read status of the specified ResourceQuota 
    * `PATCH`: partially update status of the specified ResourceQuota 
    * `PUT`: replace status of the specified ResourceQuota 




## 9.2.1. /api/v1/resourcequotas

HTTP method
     `GET`
Description
     list or watch objects of kind ResourceQuota 

Table 9.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceQuotaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ResourceQuotaList) schema   
401 - Unauthorized  |  Empty   
Show more

## 9.2.2. /api/v1/watch/resourcequotas

HTTP method
     `GET`
Description
     watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead. 

Table 9.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 9.2.3. /api/v1/namespaces/{namespace}/resourcequotas

HTTP method
     `DELETE`
Description
     delete collection of ResourceQuota 

Table 9.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 9.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind ResourceQuota 

Table 9.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceQuotaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ResourceQuotaList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ResourceQuota 

Table 9.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 9.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema  |   
Show more

Table 9.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
201 - Created  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
202 - Accepted  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 9.2.4. /api/v1/watch/namespaces/{namespace}/resourcequotas

HTTP method
     `GET`
Description
     watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead. 

Table 9.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 9.2.5. /api/v1/namespaces/{namespace}/resourcequotas/{name}

Table 9.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ResourceQuota   
Show more

HTTP method
     `DELETE`
Description
     delete a ResourceQuota 

Table 9.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 9.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
202 - Accepted  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ResourceQuota 

Table 9.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ResourceQuota 

Table 9.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 9.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
201 - Created  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ResourceQuota 

Table 9.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 9.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema  |   
Show more

Table 9.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
201 - Created  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 9.2.6. /api/v1/watch/namespaces/{namespace}/resourcequotas/{name}

Table 9.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ResourceQuota   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 9.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 9.2.7. /api/v1/namespaces/{namespace}/resourcequotas/{name}/status

Table 9.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ResourceQuota   
Show more

HTTP method
     `GET`
Description
     read status of the specified ResourceQuota 

Table 9.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ResourceQuota 

Table 9.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 9.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
201 - Created  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ResourceQuota 

Table 9.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 9.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema  |   
Show more

Table 9.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
201 - Created  |  [`ResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourcequota-v1 "Chapter 9. ResourceQuota \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
