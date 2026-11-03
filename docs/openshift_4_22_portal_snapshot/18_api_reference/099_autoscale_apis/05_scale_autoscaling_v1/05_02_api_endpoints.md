# 5.2. API endpoints

The following API endpoints are available: 

  * `/apis/apps/v1/namespaces/{namespace}/deployments/{name}/scale`

    * `GET`: read scale of the specified Deployment 
    * `PATCH`: partially update scale of the specified Deployment 
    * `PUT`: replace scale of the specified Deployment 

  * `/apis/apps/v1/namespaces/{namespace}/replicasets/{name}/scale`

    * `GET`: read scale of the specified ReplicaSet 
    * `PATCH`: partially update scale of the specified ReplicaSet 
    * `PUT`: replace scale of the specified ReplicaSet 

  * `/apis/apps/v1/namespaces/{namespace}/statefulsets/{name}/scale`

    * `GET`: read scale of the specified StatefulSet 
    * `PATCH`: partially update scale of the specified StatefulSet 
    * `PUT`: replace scale of the specified StatefulSet 

  * `/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale`

    * `GET`: read scale of the specified ReplicationController 
    * `PATCH`: partially update scale of the specified ReplicationController 
    * `PUT`: replace scale of the specified ReplicationController 




## 5.2.1. /apis/apps/v1/namespaces/{namespace}/deployments/{name}/scale

Table 5.1. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Scale   
Show more

HTTP method
     `GET`
Description
     read scale of the specified Deployment 

Table 5.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update scale of the specified Deployment 

Table 5.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace scale of the specified Deployment 

Table 5.5. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.6. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema  |   
Show more

Table 5.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.2. /apis/apps/v1/namespaces/{namespace}/replicasets/{name}/scale

Table 5.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Scale   
Show more

HTTP method
     `GET`
Description
     read scale of the specified ReplicaSet 

Table 5.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update scale of the specified ReplicaSet 

Table 5.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace scale of the specified ReplicaSet 

Table 5.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema  |   
Show more

Table 5.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.3. /apis/apps/v1/namespaces/{namespace}/statefulsets/{name}/scale

Table 5.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Scale   
Show more

HTTP method
     `GET`
Description
     read scale of the specified StatefulSet 

Table 5.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update scale of the specified StatefulSet 

Table 5.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace scale of the specified StatefulSet 

Table 5.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema  |   
Show more

Table 5.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.4. /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale

Table 5.22. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Scale   
Show more

HTTP method
     `GET`
Description
     read scale of the specified ReplicationController 

Table 5.23. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update scale of the specified ReplicationController 

Table 5.24. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.25. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace scale of the specified ReplicationController 

Table 5.26. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.27. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema  |   
Show more

Table 5.28. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
201 - Created  |  [`Scale`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/scale-autoscaling-v1 "Chapter 5. Scale \[autoscaling/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
