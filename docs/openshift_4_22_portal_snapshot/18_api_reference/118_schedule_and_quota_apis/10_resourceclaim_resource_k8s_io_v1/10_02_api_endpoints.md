# 10.2. API endpoints

The following API endpoints are available: 

  * `/apis/resource.k8s.io/v1/resourceclaims`

    * `GET`: list or watch objects of kind ResourceClaim 

  * `/apis/resource.k8s.io/v1/watch/resourceclaims`

    * `GET`: watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims`

    * `DELETE`: delete collection of ResourceClaim 
    * `GET`: list or watch objects of kind ResourceClaim 
    * `POST`: create a ResourceClaim 

  * `/apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims`

    * `GET`: watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}`

    * `DELETE`: delete a ResourceClaim 
    * `GET`: read the specified ResourceClaim 
    * `PATCH`: partially update the specified ResourceClaim 
    * `PUT`: replace the specified ResourceClaim 

  * `/apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims/{name}`

    * `GET`: watch changes to an object of kind ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}/status`

    * `GET`: read status of the specified ResourceClaim 
    * `PATCH`: partially update status of the specified ResourceClaim 
    * `PUT`: replace status of the specified ResourceClaim 




## 10.2.1. /apis/resource.k8s.io/v1/resourceclaims

HTTP method
     `GET`
Description
     list or watch objects of kind ResourceClaim 

Table 10.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaimList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-resource-v1-ResourceClaimList) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.2. /apis/resource.k8s.io/v1/watch/resourceclaims

HTTP method
     `GET`
Description
     watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead. 

Table 10.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.3. /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims

HTTP method
     `DELETE`
Description
     delete collection of ResourceClaim 

Table 10.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 10.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind ResourceClaim 

Table 10.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaimList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-resource-v1-ResourceClaimList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ResourceClaim 

Table 10.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema  |   
Show more

Table 10.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
201 - Created  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
202 - Accepted  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.4. /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims

HTTP method
     `GET`
Description
     watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead. 

Table 10.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.5. /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}

Table 10.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ResourceClaim   
Show more

HTTP method
     `DELETE`
Description
     delete a ResourceClaim 

Table 10.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 10.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
202 - Accepted  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ResourceClaim 

Table 10.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ResourceClaim 

Table 10.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
201 - Created  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ResourceClaim 

Table 10.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema  |   
Show more

Table 10.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
201 - Created  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.6. /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaims/{name}

Table 10.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ResourceClaim   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 10.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.7. /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaims/{name}/status

Table 10.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ResourceClaim   
Show more

HTTP method
     `GET`
Description
     read status of the specified ResourceClaim 

Table 10.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ResourceClaim 

Table 10.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
201 - Created  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ResourceClaim 

Table 10.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema  |   
Show more

Table 10.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
201 - Created  |  [`ResourceClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaim-resource-k8s-io-v1 "Chapter 10. ResourceClaim \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
