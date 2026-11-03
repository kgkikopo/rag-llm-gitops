# 5.2. API endpoints

The following API endpoints are available: 

  * `/apis/node.k8s.io/v1/runtimeclasses`

    * `DELETE`: delete collection of RuntimeClass 
    * `GET`: list or watch objects of kind RuntimeClass 
    * `POST`: create a RuntimeClass 

  * `/apis/node.k8s.io/v1/watch/runtimeclasses`

    * `GET`: watch individual changes to a list of RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/node.k8s.io/v1/runtimeclasses/{name}`

    * `DELETE`: delete a RuntimeClass 
    * `GET`: read the specified RuntimeClass 
    * `PATCH`: partially update the specified RuntimeClass 
    * `PUT`: replace the specified RuntimeClass 

  * `/apis/node.k8s.io/v1/watch/runtimeclasses/{name}`

    * `GET`: watch changes to an object of kind RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 5.2.1. /apis/node.k8s.io/v1/runtimeclasses

HTTP method
     `DELETE`
Description
     delete collection of RuntimeClass 

Table 5.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind RuntimeClass 

Table 5.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RuntimeClassList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-node-v1-RuntimeClassList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a RuntimeClass 

Table 5.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`RuntimeClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/runtimeclass-node-k8s-io-v1 "Chapter 5. RuntimeClass \[node.k8s.io/v1\]") schema  |   
Show more

Table 5.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RuntimeClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/runtimeclass-node-k8s-io-v1 "Chapter 5. RuntimeClass \[node.k8s.io/v1\]") schema   
201 - Created  |  [`RuntimeClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/runtimeclass-node-k8s-io-v1 "Chapter 5. RuntimeClass \[node.k8s.io/v1\]") schema   
202 - Accepted  |  [`RuntimeClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/runtimeclass-node-k8s-io-v1 "Chapter 5. RuntimeClass \[node.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.2. /apis/node.k8s.io/v1/watch/runtimeclasses

HTTP method
     `GET`
Description
     watch individual changes to a list of RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead. 

Table 5.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.3. /apis/node.k8s.io/v1/runtimeclasses/{name}

Table 5.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the RuntimeClass   
Show more

HTTP method
     `DELETE`
Description
     delete a RuntimeClass 

Table 5.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified RuntimeClass 

Table 5.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RuntimeClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/runtimeclass-node-k8s-io-v1 "Chapter 5. RuntimeClass \[node.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified RuntimeClass 

Table 5.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RuntimeClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/runtimeclass-node-k8s-io-v1 "Chapter 5. RuntimeClass \[node.k8s.io/v1\]") schema   
201 - Created  |  [`RuntimeClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/runtimeclass-node-k8s-io-v1 "Chapter 5. RuntimeClass \[node.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified RuntimeClass 

Table 5.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`RuntimeClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/runtimeclass-node-k8s-io-v1 "Chapter 5. RuntimeClass \[node.k8s.io/v1\]") schema  |   
Show more

Table 5.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RuntimeClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/runtimeclass-node-k8s-io-v1 "Chapter 5. RuntimeClass \[node.k8s.io/v1\]") schema   
201 - Created  |  [`RuntimeClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/runtimeclass-node-k8s-io-v1 "Chapter 5. RuntimeClass \[node.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.4. /apis/node.k8s.io/v1/watch/runtimeclasses/{name}

Table 5.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the RuntimeClass   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 5.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
