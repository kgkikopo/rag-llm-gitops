# 3.2. API endpoints

The following API endpoints are available: 

  * `/apis/storage.k8s.io/v1/csinodes`

    * `DELETE`: delete collection of CSINode 
    * `GET`: list or watch objects of kind CSINode 
    * `POST`: create a CSINode 

  * `/apis/storage.k8s.io/v1/watch/csinodes`

    * `GET`: watch individual changes to a list of CSINode. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/storage.k8s.io/v1/csinodes/{name}`

    * `DELETE`: delete a CSINode 
    * `GET`: read the specified CSINode 
    * `PATCH`: partially update the specified CSINode 
    * `PUT`: replace the specified CSINode 

  * `/apis/storage.k8s.io/v1/watch/csinodes/{name}`

    * `GET`: watch changes to an object of kind CSINode. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 3.2.1. /apis/storage.k8s.io/v1/csinodes

HTTP method
     `DELETE`
Description
     delete collection of CSINode 

Table 3.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind CSINode 

Table 3.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSINodeList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-CSINodeList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a CSINode 

Table 3.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema  |   
Show more

Table 3.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema   
202 - Accepted  |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.2. /apis/storage.k8s.io/v1/watch/csinodes

HTTP method
     `GET`
Description
     watch individual changes to a list of CSINode. deprecated: use the 'watch' parameter with a list operation instead. 

Table 3.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.3. /apis/storage.k8s.io/v1/csinodes/{name}

Table 3.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CSINode   
Show more

HTTP method
     `DELETE`
Description
     delete a CSINode 

Table 3.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema   
202 - Accepted  |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified CSINode 

Table 3.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified CSINode 

Table 3.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified CSINode 

Table 3.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema  |   
Show more

Table 3.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`CSINode`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csinode-storage-k8s-io-v1 "Chapter 3. CSINode \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.4. /apis/storage.k8s.io/v1/watch/csinodes/{name}

Table 3.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CSINode   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind CSINode. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 3.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
