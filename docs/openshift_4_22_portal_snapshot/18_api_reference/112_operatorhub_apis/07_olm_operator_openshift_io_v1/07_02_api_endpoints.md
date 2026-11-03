# 7.2. API endpoints

The following API endpoints are available: 

  * `/apis/operator.openshift.io/v1/olms`

    * `DELETE`: delete collection of OLM 
    * `GET`: list objects of kind OLM 
    * `POST`: create an OLM 

  * `/apis/operator.openshift.io/v1/olms/{name}`

    * `DELETE`: delete an OLM 
    * `GET`: read the specified OLM 
    * `PATCH`: partially update the specified OLM 
    * `PUT`: replace the specified OLM 

  * `/apis/operator.openshift.io/v1/olms/{name}/status`

    * `GET`: read status of the specified OLM 
    * `PATCH`: partially update status of the specified OLM 
    * `PUT`: replace status of the specified OLM 




## 7.2.1. /apis/operator.openshift.io/v1/olms

HTTP method
     `DELETE`
Description
     delete collection of OLM 

Table 7.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind OLM 

Table 7.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLMList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-operator-v1-OLMList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an OLM 

Table 7.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema  |   
Show more

Table 7.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema   
202 - Accepted  |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.2. /apis/operator.openshift.io/v1/olms/{name}

Table 7.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OLM   
Show more

HTTP method
     `DELETE`
Description
     delete an OLM 

Table 7.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 7.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified OLM 

Table 7.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified OLM 

Table 7.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified OLM 

Table 7.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema  |   
Show more

Table 7.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.3. /apis/operator.openshift.io/v1/olms/{name}/status

Table 7.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OLM   
Show more

HTTP method
     `GET`
Description
     read status of the specified OLM 

Table 7.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified OLM 

Table 7.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified OLM 

Table 7.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema  |   
Show more

Table 7.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`OLM`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/olm-operator-openshift-io-v1 "Chapter 7. OLM \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
