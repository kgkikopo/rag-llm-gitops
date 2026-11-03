# 24.2. API endpoints

The following API endpoints are available: 

  * `/apis/operator.openshift.io/v1/openshiftcontrollermanagers`

    * `DELETE`: delete collection of OpenShiftControllerManager 
    * `GET`: list objects of kind OpenShiftControllerManager 
    * `POST`: create an OpenShiftControllerManager 

  * `/apis/operator.openshift.io/v1/openshiftcontrollermanagers/{name}`

    * `DELETE`: delete an OpenShiftControllerManager 
    * `GET`: read the specified OpenShiftControllerManager 
    * `PATCH`: partially update the specified OpenShiftControllerManager 
    * `PUT`: replace the specified OpenShiftControllerManager 

  * `/apis/operator.openshift.io/v1/openshiftcontrollermanagers/{name}/status`

    * `GET`: read status of the specified OpenShiftControllerManager 
    * `PATCH`: partially update status of the specified OpenShiftControllerManager 
    * `PUT`: replace status of the specified OpenShiftControllerManager 




## 24.2.1. /apis/operator.openshift.io/v1/openshiftcontrollermanagers

HTTP method
     `DELETE`
Description
     delete collection of OpenShiftControllerManager 

Table 24.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind OpenShiftControllerManager 

Table 24.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OpenShiftControllerManagerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-operator-v1-OpenShiftControllerManagerList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an OpenShiftControllerManager 

Table 24.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 24.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema  |   
Show more

Table 24.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema   
202 - Accepted  |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 24.2.2. /apis/operator.openshift.io/v1/openshiftcontrollermanagers/{name}

Table 24.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OpenShiftControllerManager   
Show more

HTTP method
     `DELETE`
Description
     delete an OpenShiftControllerManager 

Table 24.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 24.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified OpenShiftControllerManager 

Table 24.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified OpenShiftControllerManager 

Table 24.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 24.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified OpenShiftControllerManager 

Table 24.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 24.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema  |   
Show more

Table 24.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 24.2.3. /apis/operator.openshift.io/v1/openshiftcontrollermanagers/{name}/status

Table 24.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OpenShiftControllerManager   
Show more

HTTP method
     `GET`
Description
     read status of the specified OpenShiftControllerManager 

Table 24.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified OpenShiftControllerManager 

Table 24.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 24.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified OpenShiftControllerManager 

Table 24.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 24.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema  |   
Show more

Table 24.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`OpenShiftControllerManager`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/openshiftcontrollermanager-operator-openshift-io-v1 "Chapter 24. OpenShiftControllerManager \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
