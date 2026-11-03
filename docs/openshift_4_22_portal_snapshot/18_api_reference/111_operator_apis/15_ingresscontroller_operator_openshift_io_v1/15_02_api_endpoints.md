# 15.2. API endpoints

The following API endpoints are available: 

  * `/apis/operator.openshift.io/v1/ingresscontrollers`

    * `GET`: list objects of kind IngressController 

  * `/apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers`

    * `DELETE`: delete collection of IngressController 
    * `GET`: list objects of kind IngressController 
    * `POST`: create an IngressController 

  * `/apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}`

    * `DELETE`: delete an IngressController 
    * `GET`: read the specified IngressController 
    * `PATCH`: partially update the specified IngressController 
    * `PUT`: replace the specified IngressController 

  * `/apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}/scale`

    * `GET`: read scale of the specified IngressController 
    * `PATCH`: partially update scale of the specified IngressController 
    * `PUT`: replace scale of the specified IngressController 

  * `/apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}/status`

    * `GET`: read status of the specified IngressController 
    * `PATCH`: partially update status of the specified IngressController 
    * `PUT`: replace status of the specified IngressController 




## 15.2.1. /apis/operator.openshift.io/v1/ingresscontrollers

HTTP method
     `GET`
Description
     list objects of kind IngressController 

Table 15.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IngressControllerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-operator-v1-IngressControllerList) schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.2. /apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers

HTTP method
     `DELETE`
Description
     delete collection of IngressController 

Table 15.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind IngressController 

Table 15.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IngressControllerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-operator-v1-IngressControllerList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an IngressController 

Table 15.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema  |   
Show more

Table 15.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema   
202 - Accepted  |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.3. /apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}

Table 15.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the IngressController   
Show more

HTTP method
     `DELETE`
Description
     delete an IngressController 

Table 15.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 15.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified IngressController 

Table 15.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified IngressController 

Table 15.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified IngressController 

Table 15.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema  |   
Show more

Table 15.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.4. /apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}/scale

Table 15.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the IngressController   
Show more

HTTP method
     `GET`
Description
     read scale of the specified IngressController 

Table 15.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update scale of the specified IngressController 

Table 15.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace scale of the specified IngressController 

Table 15.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema  |   
Show more

Table 15.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.5. /apis/operator.openshift.io/v1/namespaces/{namespace}/ingresscontrollers/{name}/status

Table 15.23. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the IngressController   
Show more

HTTP method
     `GET`
Description
     read status of the specified IngressController 

Table 15.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified IngressController 

Table 15.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.26. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified IngressController 

Table 15.27. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.28. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema  |   
Show more

Table 15.29. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`IngressController`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/ingresscontroller-operator-openshift-io-v1 "Chapter 15. IngressController \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
