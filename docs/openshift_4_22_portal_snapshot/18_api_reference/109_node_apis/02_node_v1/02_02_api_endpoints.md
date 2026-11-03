# 2.2. API endpoints

The following API endpoints are available: 

  * `/api/v1/nodes`

    * `DELETE`: delete collection of Node 
    * `GET`: list or watch objects of kind Node 
    * `POST`: create a Node 

  * `/api/v1/watch/nodes`

    * `GET`: watch individual changes to a list of Node. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/api/v1/nodes/{name}`

    * `DELETE`: delete a Node 
    * `GET`: read the specified Node 
    * `PATCH`: partially update the specified Node 
    * `PUT`: replace the specified Node 

  * `/api/v1/watch/nodes/{name}`

    * `GET`: watch changes to an object of kind Node. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/api/v1/nodes/{name}/status`

    * `GET`: read status of the specified Node 
    * `PATCH`: partially update status of the specified Node 
    * `PUT`: replace status of the specified Node 




## 2.2.1. /api/v1/nodes

HTTP method
     `DELETE`
Description
     delete collection of Node 

Table 2.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Node 

Table 2.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NodeList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-NodeList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Node 

Table 2.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema  |   
Show more

Table 2.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
201 - Created  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
202 - Accepted  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /api/v1/watch/nodes

HTTP method
     `GET`
Description
     watch individual changes to a list of Node. deprecated: use the 'watch' parameter with a list operation instead. 

Table 2.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /api/v1/nodes/{name}

Table 2.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Node   
Show more

HTTP method
     `DELETE`
Description
     delete a Node 

Table 2.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Node 

Table 2.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Node 

Table 2.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
201 - Created  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Node 

Table 2.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema  |   
Show more

Table 2.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
201 - Created  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.4. /api/v1/watch/nodes/{name}

Table 2.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Node   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Node. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 2.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.5. /api/v1/nodes/{name}/status

Table 2.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Node   
Show more

HTTP method
     `GET`
Description
     read status of the specified Node 

Table 2.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Node 

Table 2.21. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
201 - Created  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Node 

Table 2.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.24. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema  |   
Show more

Table 2.25. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
201 - Created  |  [`Node`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/node-v1 "Chapter 2. Node \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
