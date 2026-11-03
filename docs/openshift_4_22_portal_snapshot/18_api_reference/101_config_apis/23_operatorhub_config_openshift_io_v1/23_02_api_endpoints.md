# 23.2. API endpoints

The following API endpoints are available: 

  * `/apis/config.openshift.io/v1/operatorhubs`

    * `DELETE`: delete collection of OperatorHub 
    * `GET`: list objects of kind OperatorHub 
    * `POST`: create an OperatorHub 

  * `/apis/config.openshift.io/v1/operatorhubs/{name}`

    * `DELETE`: delete an OperatorHub 
    * `GET`: read the specified OperatorHub 
    * `PATCH`: partially update the specified OperatorHub 
    * `PUT`: replace the specified OperatorHub 

  * `/apis/config.openshift.io/v1/operatorhubs/{name}/status`

    * `GET`: read status of the specified OperatorHub 
    * `PATCH`: partially update status of the specified OperatorHub 
    * `PUT`: replace status of the specified OperatorHub 




## 23.2.1. /apis/config.openshift.io/v1/operatorhubs

HTTP method
     `DELETE`
Description
     delete collection of OperatorHub 

Table 23.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind OperatorHub 

Table 23.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorHubList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-OperatorHubList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an OperatorHub 

Table 23.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 23.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema  |   
Show more

Table 23.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema   
201 - Created  |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema   
202 - Accepted  |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 23.2.2. /apis/config.openshift.io/v1/operatorhubs/{name}

Table 23.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OperatorHub   
Show more

HTTP method
     `DELETE`
Description
     delete an OperatorHub 

Table 23.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 23.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified OperatorHub 

Table 23.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified OperatorHub 

Table 23.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 23.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified OperatorHub 

Table 23.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 23.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema  |   
Show more

Table 23.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema   
201 - Created  |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 23.2.3. /apis/config.openshift.io/v1/operatorhubs/{name}/status

Table 23.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OperatorHub   
Show more

HTTP method
     `GET`
Description
     read status of the specified OperatorHub 

Table 23.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified OperatorHub 

Table 23.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 23.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified OperatorHub 

Table 23.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 23.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema  |   
Show more

Table 23.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema   
201 - Created  |  [`OperatorHub`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/operatorhub-config-openshift-io-v1 "Chapter 23. OperatorHub \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
