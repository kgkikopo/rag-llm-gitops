# 27.2. API endpoints

The following API endpoints are available: 

  * `/apis/config.openshift.io/v1/schedulers`

    * `DELETE`: delete collection of Scheduler 
    * `GET`: list objects of kind Scheduler 
    * `POST`: create a Scheduler 

  * `/apis/config.openshift.io/v1/schedulers/{name}`

    * `DELETE`: delete a Scheduler 
    * `GET`: read the specified Scheduler 
    * `PATCH`: partially update the specified Scheduler 
    * `PUT`: replace the specified Scheduler 

  * `/apis/config.openshift.io/v1/schedulers/{name}/status`

    * `GET`: read status of the specified Scheduler 
    * `PATCH`: partially update status of the specified Scheduler 
    * `PUT`: replace status of the specified Scheduler 




## 27.2.1. /apis/config.openshift.io/v1/schedulers

HTTP method
     `DELETE`
Description
     delete collection of Scheduler 

Table 27.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind Scheduler 

Table 27.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SchedulerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-SchedulerList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Scheduler 

Table 27.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 27.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema  |   
Show more

Table 27.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema   
201 - Created  |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema   
202 - Accepted  |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 27.2.2. /apis/config.openshift.io/v1/schedulers/{name}

Table 27.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Scheduler   
Show more

HTTP method
     `DELETE`
Description
     delete a Scheduler 

Table 27.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 27.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Scheduler 

Table 27.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Scheduler 

Table 27.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 27.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Scheduler 

Table 27.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 27.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema  |   
Show more

Table 27.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema   
201 - Created  |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 27.2.3. /apis/config.openshift.io/v1/schedulers/{name}/status

Table 27.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Scheduler   
Show more

HTTP method
     `GET`
Description
     read status of the specified Scheduler 

Table 27.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Scheduler 

Table 27.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 27.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Scheduler 

Table 27.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 27.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema  |   
Show more

Table 27.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema   
201 - Created  |  [`Scheduler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/scheduler-config-openshift-io-v1 "Chapter 27. Scheduler \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
