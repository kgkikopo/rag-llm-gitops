# 25.2. API endpoints

The following API endpoints are available: 

  * `/apis/network.operator.openshift.io/v1/operatorpkis`

    * `GET`: list objects of kind OperatorPKI 

  * `/apis/network.operator.openshift.io/v1/namespaces/{namespace}/operatorpkis`

    * `DELETE`: delete collection of OperatorPKI 
    * `GET`: list objects of kind OperatorPKI 
    * `POST`: create an OperatorPKI 

  * `/apis/network.operator.openshift.io/v1/namespaces/{namespace}/operatorpkis/{name}`

    * `DELETE`: delete an OperatorPKI 
    * `GET`: read the specified OperatorPKI 
    * `PATCH`: partially update the specified OperatorPKI 
    * `PUT`: replace the specified OperatorPKI 




## 25.2.1. /apis/network.operator.openshift.io/v1/operatorpkis

HTTP method
     `GET`
Description
     list objects of kind OperatorPKI 

Table 25.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorPKIList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-operator-network-v1-OperatorPKIList) schema   
401 - Unauthorized  |  Empty   
Show more

## 25.2.2. /apis/network.operator.openshift.io/v1/namespaces/{namespace}/operatorpkis

HTTP method
     `DELETE`
Description
     delete collection of OperatorPKI 

Table 25.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind OperatorPKI 

Table 25.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorPKIList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-operator-network-v1-OperatorPKIList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an OperatorPKI 

Table 25.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 25.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OperatorPKI`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/operatorpki-network-operator-openshift-io-v1 "Chapter 25. OperatorPKI \[network.operator.openshift.io/v1\]") schema  |   
Show more

Table 25.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorPKI`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/operatorpki-network-operator-openshift-io-v1 "Chapter 25. OperatorPKI \[network.operator.openshift.io/v1\]") schema   
201 - Created  |  [`OperatorPKI`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/operatorpki-network-operator-openshift-io-v1 "Chapter 25. OperatorPKI \[network.operator.openshift.io/v1\]") schema   
202 - Accepted  |  [`OperatorPKI`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/operatorpki-network-operator-openshift-io-v1 "Chapter 25. OperatorPKI \[network.operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 25.2.3. /apis/network.operator.openshift.io/v1/namespaces/{namespace}/operatorpkis/{name}

Table 25.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OperatorPKI   
Show more

HTTP method
     `DELETE`
Description
     delete an OperatorPKI 

Table 25.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 25.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified OperatorPKI 

Table 25.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorPKI`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/operatorpki-network-operator-openshift-io-v1 "Chapter 25. OperatorPKI \[network.operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified OperatorPKI 

Table 25.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 25.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorPKI`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/operatorpki-network-operator-openshift-io-v1 "Chapter 25. OperatorPKI \[network.operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified OperatorPKI 

Table 25.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 25.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OperatorPKI`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/operatorpki-network-operator-openshift-io-v1 "Chapter 25. OperatorPKI \[network.operator.openshift.io/v1\]") schema  |   
Show more

Table 25.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OperatorPKI`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/operatorpki-network-operator-openshift-io-v1 "Chapter 25. OperatorPKI \[network.operator.openshift.io/v1\]") schema   
201 - Created  |  [`OperatorPKI`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/operatorpki-network-operator-openshift-io-v1 "Chapter 25. OperatorPKI \[network.operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
