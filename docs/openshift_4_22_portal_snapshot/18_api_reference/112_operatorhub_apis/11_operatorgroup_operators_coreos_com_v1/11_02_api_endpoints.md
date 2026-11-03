# 11.2. API endpoints

The following API endpoints are available: 

  * `/apis/operators.coreos.com/v1/operatorgroups`

    * `GET`: list objects of kind OperatorGroup 

  * `/apis/operators.coreos.com/v1/namespaces/{namespace}/operatorgroups`

    * `DELETE`: delete collection of OperatorGroup 
    * `GET`: list objects of kind OperatorGroup 
    * `POST`: create an OperatorGroup 

  * `/apis/operators.coreos.com/v1/namespaces/{namespace}/operatorgroups/{name}`

    * `DELETE`: delete an OperatorGroup 
    * `GET`: read the specified OperatorGroup 
    * `PATCH`: partially update the specified OperatorGroup 
    * `PUT`: replace the specified OperatorGroup 

  * `/apis/operators.coreos.com/v1/namespaces/{namespace}/operatorgroups/{name}/status`

    * `GET`: read status of the specified OperatorGroup 
    * `PATCH`: partially update status of the specified OperatorGroup 
    * `PUT`: replace status of the specified OperatorGroup 




## 11.2.1. /apis/operators.coreos.com/v1/operatorgroups

HTTP method
     `GET`
Description
     list objects of kind OperatorGroup 

Table 11.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorGroupList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-operators-v1-OperatorGroupList) schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.2. /apis/operators.coreos.com/v1/namespaces/{namespace}/operatorgroups

HTTP method
     `DELETE`
Description
     delete collection of OperatorGroup 

Table 11.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind OperatorGroup 

Table 11.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorGroupList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-operators-v1-OperatorGroupList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an OperatorGroup 

Table 11.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema  |   
Show more

Table 11.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema   
201 - Created  |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema   
202 - Accepted  |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.3. /apis/operators.coreos.com/v1/namespaces/{namespace}/operatorgroups/{name}

Table 11.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OperatorGroup   
Show more

HTTP method
     `DELETE`
Description
     delete an OperatorGroup 

Table 11.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 11.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified OperatorGroup 

Table 11.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified OperatorGroup 

Table 11.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified OperatorGroup 

Table 11.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema  |   
Show more

Table 11.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema   
201 - Created  |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.4. /apis/operators.coreos.com/v1/namespaces/{namespace}/operatorgroups/{name}/status

Table 11.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OperatorGroup   
Show more

HTTP method
     `GET`
Description
     read status of the specified OperatorGroup 

Table 11.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified OperatorGroup 

Table 11.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified OperatorGroup 

Table 11.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema  |   
Show more

Table 11.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema   
201 - Created  |  [`OperatorGroup`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/operatorgroup-operators-coreos-com-v1 "Chapter 11. OperatorGroup \[operators.coreos.com/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
