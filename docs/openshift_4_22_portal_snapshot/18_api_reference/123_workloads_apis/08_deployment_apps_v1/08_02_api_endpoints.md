# 8.2. API endpoints

The following API endpoints are available: 

  * `/apis/apps/v1/deployments`

    * `GET`: list or watch objects of kind Deployment 

  * `/apis/apps/v1/watch/deployments`

    * `GET`: watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/apps/v1/namespaces/{namespace}/deployments`

    * `DELETE`: delete collection of Deployment 
    * `GET`: list or watch objects of kind Deployment 
    * `POST`: create a Deployment 

  * `/apis/apps/v1/watch/namespaces/{namespace}/deployments`

    * `GET`: watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/apps/v1/namespaces/{namespace}/deployments/{name}`

    * `DELETE`: delete a Deployment 
    * `GET`: read the specified Deployment 
    * `PATCH`: partially update the specified Deployment 
    * `PUT`: replace the specified Deployment 

  * `/apis/apps/v1/watch/namespaces/{namespace}/deployments/{name}`

    * `GET`: watch changes to an object of kind Deployment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/apps/v1/namespaces/{namespace}/deployments/{name}/status`

    * `GET`: read status of the specified Deployment 
    * `PATCH`: partially update status of the specified Deployment 
    * `PUT`: replace status of the specified Deployment 




## 8.2.1. /apis/apps/v1/deployments

HTTP method
     `GET`
Description
     list or watch objects of kind Deployment 

Table 8.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DeploymentList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-apps-v1-DeploymentList) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.2. /apis/apps/v1/watch/deployments

HTTP method
     `GET`
Description
     watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead. 

Table 8.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.3. /apis/apps/v1/namespaces/{namespace}/deployments

HTTP method
     `DELETE`
Description
     delete collection of Deployment 

Table 8.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 8.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Deployment 

Table 8.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DeploymentList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-apps-v1-DeploymentList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Deployment 

Table 8.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema  |   
Show more

Table 8.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
201 - Created  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
202 - Accepted  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.4. /apis/apps/v1/watch/namespaces/{namespace}/deployments

HTTP method
     `GET`
Description
     watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead. 

Table 8.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.5. /apis/apps/v1/namespaces/{namespace}/deployments/{name}

Table 8.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Deployment   
Show more

HTTP method
     `DELETE`
Description
     delete a Deployment 

Table 8.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 8.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Deployment 

Table 8.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Deployment 

Table 8.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
201 - Created  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Deployment 

Table 8.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema  |   
Show more

Table 8.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
201 - Created  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.6. /apis/apps/v1/watch/namespaces/{namespace}/deployments/{name}

Table 8.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Deployment   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Deployment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 8.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.7. /apis/apps/v1/namespaces/{namespace}/deployments/{name}/status

Table 8.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Deployment   
Show more

HTTP method
     `GET`
Description
     read status of the specified Deployment 

Table 8.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Deployment 

Table 8.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
201 - Created  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Deployment 

Table 8.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema  |   
Show more

Table 8.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
201 - Created  |  [`Deployment`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deployment-apps-v1 "Chapter 8. Deployment \[apps/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
