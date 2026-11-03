# 3.2. API endpoints

The following API endpoints are available: 

  * `/apis/build.openshift.io/v1/builds`

    * `GET`: list or watch objects of kind Build 

  * `/apis/build.openshift.io/v1/watch/builds`

    * `GET`: watch individual changes to a list of Build. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/build.openshift.io/v1/namespaces/{namespace}/builds`

    * `DELETE`: delete collection of Build 
    * `GET`: list or watch objects of kind Build 
    * `POST`: create a Build 

  * `/apis/build.openshift.io/v1/watch/namespaces/{namespace}/builds`

    * `GET`: watch individual changes to a list of Build. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name}`

    * `DELETE`: delete a Build 
    * `GET`: read the specified Build 
    * `PATCH`: partially update the specified Build 
    * `PUT`: replace the specified Build 

  * `/apis/build.openshift.io/v1/watch/namespaces/{namespace}/builds/{name}`

    * `GET`: watch changes to an object of kind Build. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name}/details`

    * `PUT`: replace details of the specified Build 

  * `/apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks`

    * `POST`: connect POST requests to webhooks of BuildConfig 

  * `/apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks/{path}`

    * `POST`: connect POST requests to webhooks of BuildConfig 




## 3.2.1. /apis/build.openshift.io/v1/builds

HTTP method
     `GET`
Description
     list or watch objects of kind Build 

Table 3.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BuildList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-build-v1-BuildList) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.2. /apis/build.openshift.io/v1/watch/builds

HTTP method
     `GET`
Description
     watch individual changes to a list of Build. deprecated: use the 'watch' parameter with a list operation instead. 

Table 3.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.3. /apis/build.openshift.io/v1/namespaces/{namespace}/builds

HTTP method
     `DELETE`
Description
     delete collection of Build 

Table 3.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Build 

Table 3.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BuildList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-build-v1-BuildList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Build 

Table 3.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema  |   
Show more

Table 3.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema   
201 - Created  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema   
202 - Accepted  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.4. /apis/build.openshift.io/v1/watch/namespaces/{namespace}/builds

HTTP method
     `GET`
Description
     watch individual changes to a list of Build. deprecated: use the 'watch' parameter with a list operation instead. 

Table 3.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.5. /apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name}

Table 3.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Build   
Show more

HTTP method
     `DELETE`
Description
     delete a Build 

Table 3.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Build 

Table 3.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Build 

Table 3.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema   
201 - Created  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Build 

Table 3.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema  |   
Show more

Table 3.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema   
201 - Created  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.6. /apis/build.openshift.io/v1/watch/namespaces/{namespace}/builds/{name}

Table 3.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Build   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Build. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 3.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.7. /apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name}/details

Table 3.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Build   
Show more

Table 3.22. Global query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

HTTP method
     `PUT`
Description
     replace details of the specified Build 

Table 3.23. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema  |   
Show more

Table 3.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema   
201 - Created  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/build-build-openshift-io-v1 "Chapter 3. Build \[build.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.8. /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks

Table 3.25. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Build   
Show more

HTTP method
     `POST`
Description
     connect POST requests to webhooks of BuildConfig 

Table 3.26. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  `string`  
401 - Unauthorized  |  Empty   
Show more

## 3.2.9. /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks/{path}

Table 3.27. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Build   
Show more

HTTP method
     `POST`
Description
     connect POST requests to webhooks of BuildConfig 

Table 3.28. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  `string`  
401 - Unauthorized  |  Empty   
Show more
