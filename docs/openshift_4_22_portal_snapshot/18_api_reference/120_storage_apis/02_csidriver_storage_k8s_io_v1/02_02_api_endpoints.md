# 2.2. API endpoints

The following API endpoints are available: 

  * `/apis/storage.k8s.io/v1/csidrivers`

    * `DELETE`: delete collection of CSIDriver 
    * `GET`: list or watch objects of kind CSIDriver 
    * `POST`: create a CSIDriver 

  * `/apis/storage.k8s.io/v1/watch/csidrivers`

    * `GET`: watch individual changes to a list of CSIDriver. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/storage.k8s.io/v1/csidrivers/{name}`

    * `DELETE`: delete a CSIDriver 
    * `GET`: read the specified CSIDriver 
    * `PATCH`: partially update the specified CSIDriver 
    * `PUT`: replace the specified CSIDriver 

  * `/apis/storage.k8s.io/v1/watch/csidrivers/{name}`

    * `GET`: watch changes to an object of kind CSIDriver. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 2.2.1. /apis/storage.k8s.io/v1/csidrivers

HTTP method
     `DELETE`
Description
     delete collection of CSIDriver 

Table 2.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind CSIDriver 

Table 2.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIDriverList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-CSIDriverList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a CSIDriver 

Table 2.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema  |   
Show more

Table 2.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema   
202 - Accepted  |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /apis/storage.k8s.io/v1/watch/csidrivers

HTTP method
     `GET`
Description
     watch individual changes to a list of CSIDriver. deprecated: use the 'watch' parameter with a list operation instead. 

Table 2.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /apis/storage.k8s.io/v1/csidrivers/{name}

Table 2.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CSIDriver   
Show more

HTTP method
     `DELETE`
Description
     delete a CSIDriver 

Table 2.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema   
202 - Accepted  |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified CSIDriver 

Table 2.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified CSIDriver 

Table 2.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified CSIDriver 

Table 2.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema  |   
Show more

Table 2.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`CSIDriver`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csidriver-storage-k8s-io-v1 "Chapter 2. CSIDriver \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.4. /apis/storage.k8s.io/v1/watch/csidrivers/{name}

Table 2.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CSIDriver   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind CSIDriver. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 2.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
