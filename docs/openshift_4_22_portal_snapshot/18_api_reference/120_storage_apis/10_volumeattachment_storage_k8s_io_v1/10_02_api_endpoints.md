# 10.2. API endpoints

The following API endpoints are available: 

  * `/apis/storage.k8s.io/v1/volumeattachments`

    * `DELETE`: delete collection of VolumeAttachment 
    * `GET`: list or watch objects of kind VolumeAttachment 
    * `POST`: create a VolumeAttachment 

  * `/apis/storage.k8s.io/v1/watch/volumeattachments`

    * `GET`: watch individual changes to a list of VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/storage.k8s.io/v1/volumeattachments/{name}`

    * `DELETE`: delete a VolumeAttachment 
    * `GET`: read the specified VolumeAttachment 
    * `PATCH`: partially update the specified VolumeAttachment 
    * `PUT`: replace the specified VolumeAttachment 

  * `/apis/storage.k8s.io/v1/watch/volumeattachments/{name}`

    * `GET`: watch changes to an object of kind VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/storage.k8s.io/v1/volumeattachments/{name}/status`

    * `GET`: read status of the specified VolumeAttachment 
    * `PATCH`: partially update status of the specified VolumeAttachment 
    * `PUT`: replace status of the specified VolumeAttachment 




## 10.2.1. /apis/storage.k8s.io/v1/volumeattachments

HTTP method
     `DELETE`
Description
     delete collection of VolumeAttachment 

Table 10.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 10.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind VolumeAttachment 

Table 10.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeAttachmentList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-storage-v1-VolumeAttachmentList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a VolumeAttachment 

Table 10.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema  |   
Show more

Table 10.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
202 - Accepted  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.2. /apis/storage.k8s.io/v1/watch/volumeattachments

HTTP method
     `GET`
Description
     watch individual changes to a list of VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead. 

Table 10.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.3. /apis/storage.k8s.io/v1/volumeattachments/{name}

Table 10.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the VolumeAttachment   
Show more

HTTP method
     `DELETE`
Description
     delete a VolumeAttachment 

Table 10.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 10.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
202 - Accepted  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified VolumeAttachment 

Table 10.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified VolumeAttachment 

Table 10.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified VolumeAttachment 

Table 10.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema  |   
Show more

Table 10.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.4. /apis/storage.k8s.io/v1/watch/volumeattachments/{name}

Table 10.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the VolumeAttachment   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 10.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.5. /apis/storage.k8s.io/v1/volumeattachments/{name}/status

Table 10.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the VolumeAttachment   
Show more

HTTP method
     `GET`
Description
     read status of the specified VolumeAttachment 

Table 10.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified VolumeAttachment 

Table 10.21. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified VolumeAttachment 

Table 10.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.24. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema  |   
Show more

Table 10.25. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
201 - Created  |  [`VolumeAttachment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage_apis/volumeattachment-storage-k8s-io-v1 "Chapter 10. VolumeAttachment \[storage.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
