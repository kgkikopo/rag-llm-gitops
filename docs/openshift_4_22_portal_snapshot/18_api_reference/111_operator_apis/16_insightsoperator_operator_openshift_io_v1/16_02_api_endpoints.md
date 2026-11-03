# 16.2. API endpoints

The following API endpoints are available: 

  * `/apis/operator.openshift.io/v1/insightsoperators`

    * `DELETE`: delete collection of InsightsOperator 
    * `GET`: list objects of kind InsightsOperator 
    * `POST`: create an InsightsOperator 

  * `/apis/operator.openshift.io/v1/insightsoperators/{name}`

    * `DELETE`: delete an InsightsOperator 
    * `GET`: read the specified InsightsOperator 
    * `PATCH`: partially update the specified InsightsOperator 
    * `PUT`: replace the specified InsightsOperator 

  * `/apis/operator.openshift.io/v1/insightsoperators/{name}/scale`

    * `GET`: read scale of the specified InsightsOperator 
    * `PATCH`: partially update scale of the specified InsightsOperator 
    * `PUT`: replace scale of the specified InsightsOperator 

  * `/apis/operator.openshift.io/v1/insightsoperators/{name}/status`

    * `GET`: read status of the specified InsightsOperator 
    * `PATCH`: partially update status of the specified InsightsOperator 
    * `PUT`: replace status of the specified InsightsOperator 




## 16.2.1. /apis/operator.openshift.io/v1/insightsoperators

HTTP method
     `DELETE`
Description
     delete collection of InsightsOperator 

Table 16.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind InsightsOperator 

Table 16.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`InsightsOperatorList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-operator-v1-InsightsOperatorList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an InsightsOperator 

Table 16.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema  |   
Show more

Table 16.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema   
202 - Accepted  |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.2. /apis/operator.openshift.io/v1/insightsoperators/{name}

Table 16.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the InsightsOperator   
Show more

HTTP method
     `DELETE`
Description
     delete an InsightsOperator 

Table 16.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 16.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified InsightsOperator 

Table 16.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified InsightsOperator 

Table 16.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified InsightsOperator 

Table 16.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema  |   
Show more

Table 16.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.3. /apis/operator.openshift.io/v1/insightsoperators/{name}/scale

Table 16.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the InsightsOperator   
Show more

HTTP method
     `GET`
Description
     read scale of the specified InsightsOperator 

Table 16.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update scale of the specified InsightsOperator 

Table 16.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace scale of the specified InsightsOperator 

Table 16.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema  |   
Show more

Table 16.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.4. /apis/operator.openshift.io/v1/insightsoperators/{name}/status

Table 16.22. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the InsightsOperator   
Show more

HTTP method
     `GET`
Description
     read status of the specified InsightsOperator 

Table 16.23. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified InsightsOperator 

Table 16.24. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.25. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified InsightsOperator 

Table 16.26. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.27. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema  |   
Show more

Table 16.28. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`InsightsOperator`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/insightsoperator-operator-openshift-io-v1 "Chapter 16. InsightsOperator \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
