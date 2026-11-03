# 12.2. API endpoints

The following API endpoints are available: 

  * `/apis/resource.k8s.io/v1/resourceslices`

    * `DELETE`: delete collection of ResourceSlice 
    * `GET`: list or watch objects of kind ResourceSlice 
    * `POST`: create a ResourceSlice 

  * `/apis/resource.k8s.io/v1/watch/resourceslices`

    * `GET`: watch individual changes to a list of ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/resource.k8s.io/v1/resourceslices/{name}`

    * `DELETE`: delete a ResourceSlice 
    * `GET`: read the specified ResourceSlice 
    * `PATCH`: partially update the specified ResourceSlice 
    * `PUT`: replace the specified ResourceSlice 

  * `/apis/resource.k8s.io/v1/watch/resourceslices/{name}`

    * `GET`: watch changes to an object of kind ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 12.2.1. /apis/resource.k8s.io/v1/resourceslices

HTTP method
     `DELETE`
Description
     delete collection of ResourceSlice 

Table 12.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 12.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind ResourceSlice 

Table 12.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceSliceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-resource-v1-ResourceSliceList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ResourceSlice 

Table 12.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 12.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema  |   
Show more

Table 12.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema   
201 - Created  |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema   
202 - Accepted  |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 12.2.2. /apis/resource.k8s.io/v1/watch/resourceslices

HTTP method
     `GET`
Description
     watch individual changes to a list of ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead. 

Table 12.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 12.2.3. /apis/resource.k8s.io/v1/resourceslices/{name}

Table 12.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ResourceSlice   
Show more

HTTP method
     `DELETE`
Description
     delete a ResourceSlice 

Table 12.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 12.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema   
202 - Accepted  |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ResourceSlice 

Table 12.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ResourceSlice 

Table 12.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 12.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema   
201 - Created  |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ResourceSlice 

Table 12.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 12.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema  |   
Show more

Table 12.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema   
201 - Created  |  [`ResourceSlice`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceslice-resource-k8s-io-v1 "Chapter 12. ResourceSlice \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 12.2.4. /apis/resource.k8s.io/v1/watch/resourceslices/{name}

Table 12.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ResourceSlice   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 12.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
