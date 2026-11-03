# 2.2. API endpoints

The following API endpoints are available: 

  * `/apis/config.openshift.io/v1/apiservers`

    * `DELETE`: delete collection of APIServer 
    * `GET`: list objects of kind APIServer 
    * `POST`: create an APIServer 

  * `/apis/config.openshift.io/v1/apiservers/{name}`

    * `DELETE`: delete an APIServer 
    * `GET`: read the specified APIServer 
    * `PATCH`: partially update the specified APIServer 
    * `PUT`: replace the specified APIServer 

  * `/apis/config.openshift.io/v1/apiservers/{name}/status`

    * `GET`: read status of the specified APIServer 
    * `PATCH`: partially update status of the specified APIServer 
    * `PUT`: replace status of the specified APIServer 




## 2.2.1. /apis/config.openshift.io/v1/apiservers

HTTP method
     `DELETE`
Description
     delete collection of APIServer 

Table 2.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind APIServer 

Table 2.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIServerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-APIServerList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an APIServer 

Table 2.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema  |   
Show more

Table 2.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema   
201 - Created  |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema   
202 - Accepted  |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /apis/config.openshift.io/v1/apiservers/{name}

Table 2.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the APIServer   
Show more

HTTP method
     `DELETE`
Description
     delete an APIServer 

Table 2.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified APIServer 

Table 2.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified APIServer 

Table 2.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified APIServer 

Table 2.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema  |   
Show more

Table 2.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema   
201 - Created  |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /apis/config.openshift.io/v1/apiservers/{name}/status

Table 2.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the APIServer   
Show more

HTTP method
     `GET`
Description
     read status of the specified APIServer 

Table 2.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified APIServer 

Table 2.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified APIServer 

Table 2.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema  |   
Show more

Table 2.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema   
201 - Created  |  [`APIServer`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/apiserver-config-openshift-io-v1 "Chapter 2. APIServer \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
