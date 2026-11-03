# 4.2. API endpoints

The following API endpoints are available: 

  * `/apis/machine.openshift.io/v1/controlplanemachinesets`

    * `GET`: list objects of kind ControlPlaneMachineSet 

  * `/apis/machine.openshift.io/v1/namespaces/{namespace}/controlplanemachinesets`

    * `DELETE`: delete collection of ControlPlaneMachineSet 
    * `GET`: list objects of kind ControlPlaneMachineSet 
    * `POST`: create a ControlPlaneMachineSet 

  * `/apis/machine.openshift.io/v1/namespaces/{namespace}/controlplanemachinesets/{name}`

    * `DELETE`: delete a ControlPlaneMachineSet 
    * `GET`: read the specified ControlPlaneMachineSet 
    * `PATCH`: partially update the specified ControlPlaneMachineSet 
    * `PUT`: replace the specified ControlPlaneMachineSet 

  * `/apis/machine.openshift.io/v1/namespaces/{namespace}/controlplanemachinesets/{name}/scale`

    * `GET`: read scale of the specified ControlPlaneMachineSet 
    * `PATCH`: partially update scale of the specified ControlPlaneMachineSet 
    * `PUT`: replace scale of the specified ControlPlaneMachineSet 

  * `/apis/machine.openshift.io/v1/namespaces/{namespace}/controlplanemachinesets/{name}/status`

    * `GET`: read status of the specified ControlPlaneMachineSet 
    * `PATCH`: partially update status of the specified ControlPlaneMachineSet 
    * `PUT`: replace status of the specified ControlPlaneMachineSet 




## 4.2.1. /apis/machine.openshift.io/v1/controlplanemachinesets

HTTP method
     `GET`
Description
     list objects of kind ControlPlaneMachineSet 

Table 4.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ControlPlaneMachineSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-machine-v1-ControlPlaneMachineSetList) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.2. /apis/machine.openshift.io/v1/namespaces/{namespace}/controlplanemachinesets

HTTP method
     `DELETE`
Description
     delete collection of ControlPlaneMachineSet 

Table 4.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind ControlPlaneMachineSet 

Table 4.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ControlPlaneMachineSetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-machine-v1-ControlPlaneMachineSetList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ControlPlaneMachineSet 

Table 4.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema  |   
Show more

Table 4.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema   
201 - Created  |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema   
202 - Accepted  |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.3. /apis/machine.openshift.io/v1/namespaces/{namespace}/controlplanemachinesets/{name}

Table 4.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ControlPlaneMachineSet   
Show more

HTTP method
     `DELETE`
Description
     delete a ControlPlaneMachineSet 

Table 4.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ControlPlaneMachineSet 

Table 4.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ControlPlaneMachineSet 

Table 4.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ControlPlaneMachineSet 

Table 4.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema  |   
Show more

Table 4.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema   
201 - Created  |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.4. /apis/machine.openshift.io/v1/namespaces/{namespace}/controlplanemachinesets/{name}/scale

Table 4.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ControlPlaneMachineSet   
Show more

HTTP method
     `GET`
Description
     read scale of the specified ControlPlaneMachineSet 

Table 4.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update scale of the specified ControlPlaneMachineSet 

Table 4.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace scale of the specified ControlPlaneMachineSet 

Table 4.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema  |   
Show more

Table 4.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.5. /apis/machine.openshift.io/v1/namespaces/{namespace}/controlplanemachinesets/{name}/status

Table 4.23. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ControlPlaneMachineSet   
Show more

HTTP method
     `GET`
Description
     read status of the specified ControlPlaneMachineSet 

Table 4.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ControlPlaneMachineSet 

Table 4.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.26. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ControlPlaneMachineSet 

Table 4.27. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.28. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema  |   
Show more

Table 4.29. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema   
201 - Created  |  [`ControlPlaneMachineSet`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_apis/controlplanemachineset-machine-openshift-io-v1 "Chapter 4. ControlPlaneMachineSet \[machine.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
