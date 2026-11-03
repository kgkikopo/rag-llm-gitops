# 2.2. API endpoints

The following API endpoints are available: 

  * `/apis/apiregistration.k8s.io/v1/apiservices`

    * `DELETE`: delete collection of APIService 
    * `GET`: list or watch objects of kind APIService 
    * `POST`: create an APIService 

  * `/apis/apiregistration.k8s.io/v1/watch/apiservices`

    * `GET`: watch individual changes to a list of APIService. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/apiregistration.k8s.io/v1/apiservices/{name}`

    * `DELETE`: delete an APIService 
    * `GET`: read the specified APIService 
    * `PATCH`: partially update the specified APIService 
    * `PUT`: replace the specified APIService 

  * `/apis/apiregistration.k8s.io/v1/watch/apiservices/{name}`

    * `GET`: watch changes to an object of kind APIService. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/apiregistration.k8s.io/v1/apiservices/{name}/status`

    * `GET`: read status of the specified APIService 
    * `PATCH`: partially update status of the specified APIService 
    * `PUT`: replace status of the specified APIService 




## 2.2.1. /apis/apiregistration.k8s.io/v1/apiservices

HTTP method
     `DELETE`
Description
     delete collection of APIService 

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
     list or watch objects of kind APIService 

Table 2.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIServiceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-kube-aggregator-pkg-apis-apiregistration-v1-APIServiceList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an APIService 

Table 2.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema  |   
Show more

Table 2.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
201 - Created  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
202 - Accepted  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /apis/apiregistration.k8s.io/v1/watch/apiservices

HTTP method
     `GET`
Description
     watch individual changes to a list of APIService. deprecated: use the 'watch' parameter with a list operation instead. 

Table 2.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /apis/apiregistration.k8s.io/v1/apiservices/{name}

Table 2.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the APIService   
Show more

HTTP method
     `DELETE`
Description
     delete an APIService 

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
     read the specified APIService 

Table 2.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified APIService 

Table 2.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
201 - Created  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified APIService 

Table 2.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema  |   
Show more

Table 2.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
201 - Created  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.4. /apis/apiregistration.k8s.io/v1/watch/apiservices/{name}

Table 2.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the APIService   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind APIService. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 2.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.5. /apis/apiregistration.k8s.io/v1/apiservices/{name}/status

Table 2.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the APIService   
Show more

HTTP method
     `GET`
Description
     read status of the specified APIService 

Table 2.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified APIService 

Table 2.21. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
201 - Created  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified APIService 

Table 2.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.24. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema  |   
Show more

Table 2.25. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
201 - Created  |  [`APIService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/apiservice-apiregistration-k8s-io-v1 "Chapter 2. APIService \[apiregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
