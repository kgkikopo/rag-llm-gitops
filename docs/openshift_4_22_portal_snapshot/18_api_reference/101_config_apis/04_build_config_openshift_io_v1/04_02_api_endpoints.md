# 4.2. API endpoints

The following API endpoints are available: 

  * `/apis/config.openshift.io/v1/builds`

    * `DELETE`: delete collection of Build 
    * `GET`: list objects of kind Build 
    * `POST`: create a Build 

  * `/apis/config.openshift.io/v1/builds/{name}`

    * `DELETE`: delete a Build 
    * `GET`: read the specified Build 
    * `PATCH`: partially update the specified Build 
    * `PUT`: replace the specified Build 

  * `/apis/config.openshift.io/v1/builds/{name}/status`

    * `GET`: read status of the specified Build 
    * `PATCH`: partially update status of the specified Build 
    * `PUT`: replace status of the specified Build 




## 4.2.1. /apis/config.openshift.io/v1/builds

HTTP method
     `DELETE`
Description
     delete collection of Build 

Table 4.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind Build 

Table 4.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BuildList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-BuildList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Build 

Table 4.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema  |   
Show more

Table 4.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema   
201 - Created  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema   
202 - Accepted  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.2. /apis/config.openshift.io/v1/builds/{name}

Table 4.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Build   
Show more

HTTP method
     `DELETE`
Description
     delete a Build 

Table 4.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Build 

Table 4.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Build 

Table 4.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Build 

Table 4.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema  |   
Show more

Table 4.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema   
201 - Created  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.3. /apis/config.openshift.io/v1/builds/{name}/status

Table 4.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Build   
Show more

HTTP method
     `GET`
Description
     read status of the specified Build 

Table 4.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Build 

Table 4.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Build 

Table 4.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema  |   
Show more

Table 4.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema   
201 - Created  |  [`Build`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/build-config-openshift-io-v1 "Chapter 4. Build \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
