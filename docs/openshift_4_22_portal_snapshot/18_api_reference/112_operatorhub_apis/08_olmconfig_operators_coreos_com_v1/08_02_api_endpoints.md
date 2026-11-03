# 8.2. API endpoints

The following API endpoints are available: 

  * `/apis/operators.coreos.com/v1/olmconfigs`

    * `DELETE`: delete collection of OLMConfig 
    * `GET`: list objects of kind OLMConfig 
    * `POST`: create an OLMConfig 

  * `/apis/operators.coreos.com/v1/olmconfigs/{name}`

    * `DELETE`: delete an OLMConfig 
    * `GET`: read the specified OLMConfig 
    * `PATCH`: partially update the specified OLMConfig 
    * `PUT`: replace the specified OLMConfig 

  * `/apis/operators.coreos.com/v1/olmconfigs/{name}/status`

    * `GET`: read status of the specified OLMConfig 
    * `PATCH`: partially update status of the specified OLMConfig 
    * `PUT`: replace status of the specified OLMConfig 




## 8.2.1. /apis/operators.coreos.com/v1/olmconfigs

HTTP method
     `DELETE`
Description
     delete collection of OLMConfig 

Table 8.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind OLMConfig 

Table 8.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLMConfigList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-operators-v1-OLMConfigList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an OLMConfig 

Table 8.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema  |   
Show more

Table 8.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema   
201 - Created  |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema   
202 - Accepted  |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.2. /apis/operators.coreos.com/v1/olmconfigs/{name}

Table 8.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OLMConfig   
Show more

HTTP method
     `DELETE`
Description
     delete an OLMConfig 

Table 8.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 8.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified OLMConfig 

Table 8.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified OLMConfig 

Table 8.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified OLMConfig 

Table 8.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema  |   
Show more

Table 8.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema   
201 - Created  |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.3. /apis/operators.coreos.com/v1/olmconfigs/{name}/status

Table 8.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OLMConfig   
Show more

HTTP method
     `GET`
Description
     read status of the specified OLMConfig 

Table 8.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified OLMConfig 

Table 8.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified OLMConfig 

Table 8.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema  |   
Show more

Table 8.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema   
201 - Created  |  [`OLMConfig`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olmconfig-operators-coreos-com-v1 "Chapter 8. OLMConfig \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
