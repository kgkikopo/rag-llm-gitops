# 5.2. API endpoints

The following API endpoints are available: 

  * `/apis/operators.coreos.com/v1alpha1/clusterserviceversions`

    * `GET`: list objects of kind ClusterServiceVersion 

  * `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions`

    * `DELETE`: delete collection of ClusterServiceVersion 
    * `GET`: list objects of kind ClusterServiceVersion 
    * `POST`: create a ClusterServiceVersion 

  * `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions/{name}`

    * `DELETE`: delete a ClusterServiceVersion 
    * `GET`: read the specified ClusterServiceVersion 
    * `PATCH`: partially update the specified ClusterServiceVersion 
    * `PUT`: replace the specified ClusterServiceVersion 

  * `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions/{name}/status`

    * `GET`: read status of the specified ClusterServiceVersion 
    * `PATCH`: partially update status of the specified ClusterServiceVersion 
    * `PUT`: replace status of the specified ClusterServiceVersion 




## 5.2.1. /apis/operators.coreos.com/v1alpha1/clusterserviceversions

HTTP method
     `GET`
Description
     list objects of kind ClusterServiceVersion 

Table 5.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterServiceVersionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-operators-v1alpha1-ClusterServiceVersionList) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.2. /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions

HTTP method
     `DELETE`
Description
     delete collection of ClusterServiceVersion 

Table 5.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind ClusterServiceVersion 

Table 5.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterServiceVersionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-operators-v1alpha1-ClusterServiceVersionList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ClusterServiceVersion 

Table 5.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema  |   
Show more

Table 5.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema   
201 - Created  |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema   
202 - Accepted  |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.3. /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions/{name}

Table 5.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ClusterServiceVersion   
Show more

HTTP method
     `DELETE`
Description
     delete a ClusterServiceVersion 

Table 5.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ClusterServiceVersion 

Table 5.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ClusterServiceVersion 

Table 5.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ClusterServiceVersion 

Table 5.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema  |   
Show more

Table 5.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema   
201 - Created  |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.4. /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/clusterserviceversions/{name}/status

Table 5.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ClusterServiceVersion   
Show more

HTTP method
     `GET`
Description
     read status of the specified ClusterServiceVersion 

Table 5.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ClusterServiceVersion 

Table 5.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ClusterServiceVersion 

Table 5.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema  |   
Show more

Table 5.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema   
201 - Created  |  [`ClusterServiceVersion`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1 "Chapter 5. ClusterServiceVersion \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
