# 3.2. API endpoints

The following API endpoints are available: 

  * `/apis/policy/v1/poddisruptionbudgets`

    * `GET`: list or watch objects of kind PodDisruptionBudget 

  * `/apis/policy/v1/watch/poddisruptionbudgets`

    * `GET`: watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets`

    * `DELETE`: delete collection of PodDisruptionBudget 
    * `GET`: list or watch objects of kind PodDisruptionBudget 
    * `POST`: create a PodDisruptionBudget 

  * `/apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets`

    * `GET`: watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}`

    * `DELETE`: delete a PodDisruptionBudget 
    * `GET`: read the specified PodDisruptionBudget 
    * `PATCH`: partially update the specified PodDisruptionBudget 
    * `PUT`: replace the specified PodDisruptionBudget 

  * `/apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets/{name}`

    * `GET`: watch changes to an object of kind PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}/status`

    * `GET`: read status of the specified PodDisruptionBudget 
    * `PATCH`: partially update status of the specified PodDisruptionBudget 
    * `PUT`: replace status of the specified PodDisruptionBudget 




## 3.2.1. /apis/policy/v1/poddisruptionbudgets

HTTP method
     `GET`
Description
     list or watch objects of kind PodDisruptionBudget 

Table 3.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodDisruptionBudgetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-policy-v1-PodDisruptionBudgetList) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.2. /apis/policy/v1/watch/poddisruptionbudgets

HTTP method
     `GET`
Description
     watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead. 

Table 3.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.3. /apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets

HTTP method
     `DELETE`
Description
     delete collection of PodDisruptionBudget 

Table 3.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind PodDisruptionBudget 

Table 3.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodDisruptionBudgetList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-policy-v1-PodDisruptionBudgetList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a PodDisruptionBudget 

Table 3.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema  |   
Show more

Table 3.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
201 - Created  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
202 - Accepted  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.4. /apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets

HTTP method
     `GET`
Description
     watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead. 

Table 3.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.5. /apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}

Table 3.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PodDisruptionBudget   
Show more

HTTP method
     `DELETE`
Description
     delete a PodDisruptionBudget 

Table 3.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified PodDisruptionBudget 

Table 3.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified PodDisruptionBudget 

Table 3.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
201 - Created  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified PodDisruptionBudget 

Table 3.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema  |   
Show more

Table 3.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
201 - Created  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.6. /apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets/{name}

Table 3.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PodDisruptionBudget   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 3.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.7. /apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}/status

Table 3.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PodDisruptionBudget   
Show more

HTTP method
     `GET`
Description
     read status of the specified PodDisruptionBudget 

Table 3.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified PodDisruptionBudget 

Table 3.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
201 - Created  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified PodDisruptionBudget 

Table 3.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema  |   
Show more

Table 3.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
201 - Created  |  [`PodDisruptionBudget`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/policy_apis/poddisruptionbudget-policy-v1 "Chapter 3. PodDisruptionBudget \[policy/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
