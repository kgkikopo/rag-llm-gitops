# 7.2. API endpoints

The following API endpoints are available: 

  * `/apis/security.openshift.io/v1/rangeallocations`

    * `DELETE`: delete collection of RangeAllocation 
    * `GET`: list or watch objects of kind RangeAllocation 
    * `POST`: create a RangeAllocation 

  * `/apis/security.openshift.io/v1/watch/rangeallocations`

    * `GET`: watch individual changes to a list of RangeAllocation. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/security.openshift.io/v1/rangeallocations/{name}`

    * `DELETE`: delete a RangeAllocation 
    * `GET`: read the specified RangeAllocation 
    * `PATCH`: partially update the specified RangeAllocation 
    * `PUT`: replace the specified RangeAllocation 

  * `/apis/security.openshift.io/v1/watch/rangeallocations/{name}`

    * `GET`: watch changes to an object of kind RangeAllocation. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 7.2.1. /apis/security.openshift.io/v1/rangeallocations

HTTP method
     `DELETE`
Description
     delete collection of RangeAllocation 

Table 7.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 7.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind RangeAllocation 

Table 7.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RangeAllocationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-security-v1-RangeAllocationList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a RangeAllocation 

Table 7.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`RangeAllocation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/rangeallocation-security-openshift-io-v1 "Chapter 7. RangeAllocation \[security.openshift.io/v1\]") schema  |   
Show more

Table 7.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RangeAllocation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/rangeallocation-security-openshift-io-v1 "Chapter 7. RangeAllocation \[security.openshift.io/v1\]") schema   
201 - Created  |  [`RangeAllocation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/rangeallocation-security-openshift-io-v1 "Chapter 7. RangeAllocation \[security.openshift.io/v1\]") schema   
202 - Accepted  |  [`RangeAllocation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/rangeallocation-security-openshift-io-v1 "Chapter 7. RangeAllocation \[security.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.2. /apis/security.openshift.io/v1/watch/rangeallocations

HTTP method
     `GET`
Description
     watch individual changes to a list of RangeAllocation. deprecated: use the 'watch' parameter with a list operation instead. 

Table 7.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.3. /apis/security.openshift.io/v1/rangeallocations/{name}

Table 7.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the RangeAllocation   
Show more

HTTP method
     `DELETE`
Description
     delete a RangeAllocation 

Table 7.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 7.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified RangeAllocation 

Table 7.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RangeAllocation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/rangeallocation-security-openshift-io-v1 "Chapter 7. RangeAllocation \[security.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified RangeAllocation 

Table 7.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RangeAllocation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/rangeallocation-security-openshift-io-v1 "Chapter 7. RangeAllocation \[security.openshift.io/v1\]") schema   
201 - Created  |  [`RangeAllocation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/rangeallocation-security-openshift-io-v1 "Chapter 7. RangeAllocation \[security.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified RangeAllocation 

Table 7.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`RangeAllocation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/rangeallocation-security-openshift-io-v1 "Chapter 7. RangeAllocation \[security.openshift.io/v1\]") schema  |   
Show more

Table 7.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RangeAllocation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/rangeallocation-security-openshift-io-v1 "Chapter 7. RangeAllocation \[security.openshift.io/v1\]") schema   
201 - Created  |  [`RangeAllocation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/rangeallocation-security-openshift-io-v1 "Chapter 7. RangeAllocation \[security.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.4. /apis/security.openshift.io/v1/watch/rangeallocations/{name}

Table 7.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the RangeAllocation   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind RangeAllocation. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 7.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
