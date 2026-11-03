# 6.2. API endpoints

The following API endpoints are available: 

  * `/api/v1/persistentvolumeclaims`

    * `GET`: list or watch objects of kind PersistentVolumeClaim 

  * `/api/v1/watch/persistentvolumeclaims`

    * `GET`: watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/persistentvolumeclaims`

    * `DELETE`: delete collection of PersistentVolumeClaim 
    * `GET`: list or watch objects of kind PersistentVolumeClaim 
    * `POST`: create a PersistentVolumeClaim 

  * `/api/v1/watch/namespaces/{namespace}/persistentvolumeclaims`

    * `GET`: watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}`

    * `DELETE`: delete a PersistentVolumeClaim 
    * `GET`: read the specified PersistentVolumeClaim 
    * `PATCH`: partially update the specified PersistentVolumeClaim 
    * `PUT`: replace the specified PersistentVolumeClaim 

  * `/api/v1/watch/namespaces/{namespace}/persistentvolumeclaims/{name}`

    * `GET`: watch changes to an object of kind PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status`

    * `GET`: read status of the specified PersistentVolumeClaim 
    * `PATCH`: partially update status of the specified PersistentVolumeClaim 
    * `PUT`: replace status of the specified PersistentVolumeClaim 




## 6.2.1. /api/v1/persistentvolumeclaims

HTTP method
     `GET`
Description
     list or watch objects of kind PersistentVolumeClaim 

Table 6.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PersistentVolumeClaimList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PersistentVolumeClaimList) schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.2. /api/v1/watch/persistentvolumeclaims

HTTP method
     `GET`
Description
     watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead. 

Table 6.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.3. /api/v1/namespaces/{namespace}/persistentvolumeclaims

HTTP method
     `DELETE`
Description
     delete collection of PersistentVolumeClaim 

Table 6.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 6.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind PersistentVolumeClaim 

Table 6.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PersistentVolumeClaimList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PersistentVolumeClaimList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a PersistentVolumeClaim 

Table 6.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema  |   
Show more

Table 6.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
201 - Created  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
202 - Accepted  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.4. /api/v1/watch/namespaces/{namespace}/persistentvolumeclaims

HTTP method
     `GET`
Description
     watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead. 

Table 6.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.5. /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}

Table 6.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PersistentVolumeClaim   
Show more

HTTP method
     `DELETE`
Description
     delete a PersistentVolumeClaim 

Table 6.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 6.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
202 - Accepted  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified PersistentVolumeClaim 

Table 6.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified PersistentVolumeClaim 

Table 6.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
201 - Created  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified PersistentVolumeClaim 

Table 6.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema  |   
Show more

Table 6.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
201 - Created  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.6. /api/v1/watch/namespaces/{namespace}/persistentvolumeclaims/{name}

Table 6.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PersistentVolumeClaim   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 6.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.7. /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status

Table 6.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PersistentVolumeClaim   
Show more

HTTP method
     `GET`
Description
     read status of the specified PersistentVolumeClaim 

Table 6.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified PersistentVolumeClaim 

Table 6.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
201 - Created  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified PersistentVolumeClaim 

Table 6.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema  |   
Show more

Table 6.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
201 - Created  |  [`PersistentVolumeClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/persistentvolumeclaim-v1 "Chapter 6. PersistentVolumeClaim \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
