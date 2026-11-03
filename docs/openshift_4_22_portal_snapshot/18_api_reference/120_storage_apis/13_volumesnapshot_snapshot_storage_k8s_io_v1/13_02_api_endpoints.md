# 13.2. API endpoints

The following API endpoints are available: 

  * `/apis/snapshot.storage.k8s.io/v1/volumesnapshots`

    * `GET`: list objects of kind VolumeSnapshot 

  * `/apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots`

    * `DELETE`: delete collection of VolumeSnapshot 
    * `GET`: list objects of kind VolumeSnapshot 
    * `POST`: create a VolumeSnapshot 

  * `/apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}`

    * `DELETE`: delete a VolumeSnapshot 
    * `GET`: read the specified VolumeSnapshot 
    * `PATCH`: partially update the specified VolumeSnapshot 
    * `PUT`: replace the specified VolumeSnapshot 

  * `/apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}/status`

    * `GET`: read status of the specified VolumeSnapshot 
    * `PATCH`: partially update status of the specified VolumeSnapshot 
    * `PUT`: replace status of the specified VolumeSnapshot 




## 13.2.1. /apis/snapshot.storage.k8s.io/v1/volumesnapshots

HTTP method
     `GET`
Description
     list objects of kind VolumeSnapshot 

Table 13.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeSnapshotList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-storage-snapshot-v1-VolumeSnapshotList) schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.2. /apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots

HTTP method
     `DELETE`
Description
     delete collection of VolumeSnapshot 

Table 13.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind VolumeSnapshot 

Table 13.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeSnapshotList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-storage-snapshot-v1-VolumeSnapshotList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a VolumeSnapshot 

Table 13.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema  |   
Show more

Table 13.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema   
201 - Created  |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema   
202 - Accepted  |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.3. /apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}

Table 13.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the VolumeSnapshot   
Show more

HTTP method
     `DELETE`
Description
     delete a VolumeSnapshot 

Table 13.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 13.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified VolumeSnapshot 

Table 13.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified VolumeSnapshot 

Table 13.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified VolumeSnapshot 

Table 13.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema  |   
Show more

Table 13.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema   
201 - Created  |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.4. /apis/snapshot.storage.k8s.io/v1/namespaces/{namespace}/volumesnapshots/{name}/status

Table 13.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the VolumeSnapshot   
Show more

HTTP method
     `GET`
Description
     read status of the specified VolumeSnapshot 

Table 13.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified VolumeSnapshot 

Table 13.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified VolumeSnapshot 

Table 13.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema  |   
Show more

Table 13.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema   
201 - Created  |  [`VolumeSnapshot`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1 "Chapter 13. VolumeSnapshot \[snapshot.storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
