# 10.2. API endpoints

The following API endpoints are available: 

  * `/apis/machine.openshift.io/v1beta1/machinesets`

    * `GET`: list objects of kind MachineSet 

  * `/apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets`

    * `DELETE`: delete collection of MachineSet 
    * `GET`: list objects of kind MachineSet 
    * `POST`: create a MachineSet 

  * `/apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}`

    * `DELETE`: delete a MachineSet 
    * `GET`: read the specified MachineSet 
    * `PATCH`: partially update the specified MachineSet 
    * `PUT`: replace the specified MachineSet 

  * `/apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}/scale`

    * `GET`: read scale of the specified MachineSet 
    * `PATCH`: partially update scale of the specified MachineSet 
    * `PUT`: replace scale of the specified MachineSet 

  * `/apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}/status`

    * `GET`: read status of the specified MachineSet 
    * `PATCH`: partially update status of the specified MachineSet 
    * `PUT`: replace status of the specified MachineSet 




## 10.2.1. /apis/machine.openshift.io/v1beta1/machinesets

HTTP method
     `GET`
Description
     list objects of kind MachineSet 

Table 10.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-machine-v1beta1-MachineSetList) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.2. /apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets

HTTP method
     `DELETE`
Description
     delete collection of MachineSet 

Table 10.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind MachineSet 

Table 10.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-machine-v1beta1-MachineSetList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a MachineSet 

Table 10.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema  |   
Show more

Table 10.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema   
201 - Created  |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema   
202 - Accepted  |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.3. /apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}

Table 10.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the MachineSet   
Show more

HTTP method
     `DELETE`
Description
     delete a MachineSet 

Table 10.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 10.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified MachineSet 

Table 10.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified MachineSet 

Table 10.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified MachineSet 

Table 10.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema  |   
Show more

Table 10.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema   
201 - Created  |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.4. /apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}/scale

Table 10.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the MachineSet   
Show more

HTTP method
     `GET`
Description
     read scale of the specified MachineSet 

Table 10.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update scale of the specified MachineSet 

Table 10.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace scale of the specified MachineSet 

Table 10.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema  |   
Show more

Table 10.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

## 10.2.5. /apis/machine.openshift.io/v1beta1/namespaces/{namespace}/machinesets/{name}/status

Table 10.23. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the MachineSet   
Show more

HTTP method
     `GET`
Description
     read status of the specified MachineSet 

Table 10.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified MachineSet 

Table 10.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.26. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified MachineSet 

Table 10.27. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 10.28. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema  |   
Show more

Table 10.29. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema   
201 - Created  |  [`MachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/machineset-machine-openshift-io-v1beta1 "Chapter 10. MachineSet \[machine.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more
