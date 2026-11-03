# 4.2. API endpoints

The following API endpoints are available: 

  * `/apis/storage.k8s.io/v1/csistoragecapacities`

    * `GET`: list or watch objects of kind CSIStorageCapacity 

  * `/apis/storage.k8s.io/v1/watch/csistoragecapacities`

    * `GET`: watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities`

    * `DELETE`: delete collection of CSIStorageCapacity 
    * `GET`: list or watch objects of kind CSIStorageCapacity 
    * `POST`: create a CSIStorageCapacity 

  * `/apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities`

    * `GET`: watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities/{name}`

    * `DELETE`: delete a CSIStorageCapacity 
    * `GET`: read the specified CSIStorageCapacity 
    * `PATCH`: partially update the specified CSIStorageCapacity 
    * `PUT`: replace the specified CSIStorageCapacity 

  * `/apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities/{name}`

    * `GET`: watch changes to an object of kind CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 4.2.1. /apis/storage.k8s.io/v1/csistoragecapacities

HTTP method
     `GET`
Description
     list or watch objects of kind CSIStorageCapacity 

Table 4.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIStorageCapacityList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-CSIStorageCapacityList) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.2. /apis/storage.k8s.io/v1/watch/csistoragecapacities

HTTP method
     `GET`
Description
     watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead. 

Table 4.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.3. /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities

HTTP method
     `DELETE`
Description
     delete collection of CSIStorageCapacity 

Table 4.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind CSIStorageCapacity 

Table 4.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIStorageCapacityList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-CSIStorageCapacityList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a CSIStorageCapacity 

Table 4.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CSIStorageCapacity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity \[storage.k8s.io/v1\]") schema  |   
Show more

Table 4.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIStorageCapacity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`CSIStorageCapacity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity \[storage.k8s.io/v1\]") schema   
202 - Accepted  |  [`CSIStorageCapacity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.4. /apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities

HTTP method
     `GET`
Description
     watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead. 

Table 4.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.5. /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities/{name}

Table 4.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CSIStorageCapacity   
Show more

HTTP method
     `DELETE`
Description
     delete a CSIStorageCapacity 

Table 4.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified CSIStorageCapacity 

Table 4.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIStorageCapacity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified CSIStorageCapacity 

Table 4.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIStorageCapacity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`CSIStorageCapacity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified CSIStorageCapacity 

Table 4.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CSIStorageCapacity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity \[storage.k8s.io/v1\]") schema  |   
Show more

Table 4.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CSIStorageCapacity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`CSIStorageCapacity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/csistoragecapacity-storage-k8s-io-v1 "Chapter 4. CSIStorageCapacity \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.6. /apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities/{name}

Table 4.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CSIStorageCapacity   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 4.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
