# 3.2. API endpoints

The following API endpoints are available: 

  * `/apis/quota.openshift.io/v1/clusterresourcequotas`

    * `DELETE`: delete collection of ClusterResourceQuota 
    * `GET`: list objects of kind ClusterResourceQuota 
    * `POST`: create a ClusterResourceQuota 

  * `/apis/quota.openshift.io/v1/watch/clusterresourcequotas`

    * `GET`: watch individual changes to a list of ClusterResourceQuota. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/quota.openshift.io/v1/clusterresourcequotas/{name}`

    * `DELETE`: delete a ClusterResourceQuota 
    * `GET`: read the specified ClusterResourceQuota 
    * `PATCH`: partially update the specified ClusterResourceQuota 
    * `PUT`: replace the specified ClusterResourceQuota 

  * `/apis/quota.openshift.io/v1/watch/clusterresourcequotas/{name}`

    * `GET`: watch changes to an object of kind ClusterResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/quota.openshift.io/v1/clusterresourcequotas/{name}/status`

    * `GET`: read status of the specified ClusterResourceQuota 
    * `PATCH`: partially update status of the specified ClusterResourceQuota 
    * `PUT`: replace status of the specified ClusterResourceQuota 




## 3.2.1. /apis/quota.openshift.io/v1/clusterresourcequotas

HTTP method
     `DELETE`
Description
     delete collection of ClusterResourceQuota 

Table 3.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind ClusterResourceQuota 

Table 3.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterResourceQuotaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-quota-v1-ClusterResourceQuotaList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ClusterResourceQuota 

Table 3.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema  |   
Show more

Table 3.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema   
201 - Created  |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema   
202 - Accepted  |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.2. /apis/quota.openshift.io/v1/watch/clusterresourcequotas

HTTP method
     `GET`
Description
     watch individual changes to a list of ClusterResourceQuota. deprecated: use the 'watch' parameter with a list operation instead. 

Table 3.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.3. /apis/quota.openshift.io/v1/clusterresourcequotas/{name}

Table 3.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ClusterResourceQuota   
Show more

HTTP method
     `DELETE`
Description
     delete a ClusterResourceQuota 

Table 3.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ClusterResourceQuota 

Table 3.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ClusterResourceQuota 

Table 3.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ClusterResourceQuota 

Table 3.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema  |   
Show more

Table 3.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema   
201 - Created  |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.4. /apis/quota.openshift.io/v1/watch/clusterresourcequotas/{name}

Table 3.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ClusterResourceQuota   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind ClusterResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 3.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.5. /apis/quota.openshift.io/v1/clusterresourcequotas/{name}/status

Table 3.18. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ClusterResourceQuota   
Show more

HTTP method
     `GET`
Description
     read status of the specified ClusterResourceQuota 

Table 3.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ClusterResourceQuota 

Table 3.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ClusterResourceQuota 

Table 3.22. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.23. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema  |   
Show more

Table 3.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema   
201 - Created  |  [`ClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1 "Chapter 3. ClusterResourceQuota \[quota.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
