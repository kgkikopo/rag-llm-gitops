# 2.2. API endpoints

The following API endpoints are available: 

  * `/apis/build.openshift.io/v1/buildconfigs`

    * `GET`: list or watch objects of kind BuildConfig 

  * `/apis/build.openshift.io/v1/watch/buildconfigs`

    * `GET`: watch individual changes to a list of BuildConfig. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs`

    * `DELETE`: delete collection of BuildConfig 
    * `GET`: list or watch objects of kind BuildConfig 
    * `POST`: create a BuildConfig 

  * `/apis/build.openshift.io/v1/watch/namespaces/{namespace}/buildconfigs`

    * `GET`: watch individual changes to a list of BuildConfig. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name}`

    * `DELETE`: delete a BuildConfig 
    * `GET`: read the specified BuildConfig 
    * `PATCH`: partially update the specified BuildConfig 
    * `PUT`: replace the specified BuildConfig 

  * `/apis/build.openshift.io/v1/watch/namespaces/{namespace}/buildconfigs/{name}`

    * `GET`: watch changes to an object of kind BuildConfig. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 2.2.1. /apis/build.openshift.io/v1/buildconfigs

HTTP method
     `GET`
Description
     list or watch objects of kind BuildConfig 

Table 2.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BuildConfigList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-build-v1-BuildConfigList) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /apis/build.openshift.io/v1/watch/buildconfigs

HTTP method
     `GET`
Description
     watch individual changes to a list of BuildConfig. deprecated: use the 'watch' parameter with a list operation instead. 

Table 2.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs

HTTP method
     `DELETE`
Description
     delete collection of BuildConfig 

Table 2.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind BuildConfig 

Table 2.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BuildConfigList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-build-v1-BuildConfigList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a BuildConfig 

Table 2.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BuildConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/buildconfig-build-openshift-io-v1 "Chapter 2. BuildConfig \[build.openshift.io/v1\]") schema  |   
Show more

Table 2.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BuildConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/buildconfig-build-openshift-io-v1 "Chapter 2. BuildConfig \[build.openshift.io/v1\]") schema   
201 - Created  |  [`BuildConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/buildconfig-build-openshift-io-v1 "Chapter 2. BuildConfig \[build.openshift.io/v1\]") schema   
202 - Accepted  |  [`BuildConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/buildconfig-build-openshift-io-v1 "Chapter 2. BuildConfig \[build.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.4. /apis/build.openshift.io/v1/watch/namespaces/{namespace}/buildconfigs

HTTP method
     `GET`
Description
     watch individual changes to a list of BuildConfig. deprecated: use the 'watch' parameter with a list operation instead. 

Table 2.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.5. /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name}

Table 2.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the BuildConfig   
Show more

HTTP method
     `DELETE`
Description
     delete a BuildConfig 

Table 2.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified BuildConfig 

Table 2.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BuildConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/buildconfig-build-openshift-io-v1 "Chapter 2. BuildConfig \[build.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified BuildConfig 

Table 2.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BuildConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/buildconfig-build-openshift-io-v1 "Chapter 2. BuildConfig \[build.openshift.io/v1\]") schema   
201 - Created  |  [`BuildConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/buildconfig-build-openshift-io-v1 "Chapter 2. BuildConfig \[build.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified BuildConfig 

Table 2.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BuildConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/buildconfig-build-openshift-io-v1 "Chapter 2. BuildConfig \[build.openshift.io/v1\]") schema  |   
Show more

Table 2.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BuildConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/buildconfig-build-openshift-io-v1 "Chapter 2. BuildConfig \[build.openshift.io/v1\]") schema   
201 - Created  |  [`BuildConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/buildconfig-build-openshift-io-v1 "Chapter 2. BuildConfig \[build.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.6. /apis/build.openshift.io/v1/watch/namespaces/{namespace}/buildconfigs/{name}

Table 2.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the BuildConfig   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind BuildConfig. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 2.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
