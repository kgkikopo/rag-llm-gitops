# 21.2. API endpoints

The following API endpoints are available: 

  * `/apis/operator.openshift.io/v1/machineconfigurations`

    * `DELETE`: delete collection of MachineConfiguration 
    * `GET`: list objects of kind MachineConfiguration 
    * `POST`: create a MachineConfiguration 

  * `/apis/operator.openshift.io/v1/machineconfigurations/{name}`

    * `DELETE`: delete a MachineConfiguration 
    * `GET`: read the specified MachineConfiguration 
    * `PATCH`: partially update the specified MachineConfiguration 
    * `PUT`: replace the specified MachineConfiguration 

  * `/apis/operator.openshift.io/v1/machineconfigurations/{name}/status`

    * `GET`: read status of the specified MachineConfiguration 
    * `PATCH`: partially update status of the specified MachineConfiguration 
    * `PUT`: replace status of the specified MachineConfiguration 




## 21.2.1. /apis/operator.openshift.io/v1/machineconfigurations

HTTP method
     `DELETE`
Description
     delete collection of MachineConfiguration 

Table 21.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind MachineConfiguration 

Table 21.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineConfigurationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-operator-v1-MachineConfigurationList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a MachineConfiguration 

Table 21.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 21.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema  |   
Show more

Table 21.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema   
202 - Accepted  |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 21.2.2. /apis/operator.openshift.io/v1/machineconfigurations/{name}

Table 21.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the MachineConfiguration   
Show more

HTTP method
     `DELETE`
Description
     delete a MachineConfiguration 

Table 21.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 21.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified MachineConfiguration 

Table 21.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified MachineConfiguration 

Table 21.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 21.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified MachineConfiguration 

Table 21.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 21.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema  |   
Show more

Table 21.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 21.2.3. /apis/operator.openshift.io/v1/machineconfigurations/{name}/status

Table 21.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the MachineConfiguration   
Show more

HTTP method
     `GET`
Description
     read status of the specified MachineConfiguration 

Table 21.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified MachineConfiguration 

Table 21.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 21.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified MachineConfiguration 

Table 21.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 21.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema  |   
Show more

Table 21.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema   
201 - Created  |  [`MachineConfiguration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/machineconfiguration-operator-openshift-io-v1 "Chapter 21. MachineConfiguration \[operator.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
