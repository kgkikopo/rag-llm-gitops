# 15.2. API endpoints

The following API endpoints are available: 

  * `/apis/config.openshift.io/v1/imagepolicies`

    * `GET`: list objects of kind ImagePolicy 

  * `/apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies`

    * `DELETE`: delete collection of ImagePolicy 
    * `GET`: list objects of kind ImagePolicy 
    * `POST`: create an ImagePolicy 

  * `/apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies/{name}`

    * `DELETE`: delete an ImagePolicy 
    * `GET`: read the specified ImagePolicy 
    * `PATCH`: partially update the specified ImagePolicy 
    * `PUT`: replace the specified ImagePolicy 

  * `/apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies/{name}/status`

    * `GET`: read status of the specified ImagePolicy 
    * `PATCH`: partially update status of the specified ImagePolicy 
    * `PUT`: replace status of the specified ImagePolicy 




## 15.2.1. /apis/config.openshift.io/v1/imagepolicies

HTTP method
     `GET`
Description
     list objects of kind ImagePolicy 

Table 15.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImagePolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ImagePolicyList) schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.2. /apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies

HTTP method
     `DELETE`
Description
     delete collection of ImagePolicy 

Table 15.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind ImagePolicy 

Table 15.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImagePolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-ImagePolicyList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an ImagePolicy 

Table 15.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema  |   
Show more

Table 15.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema   
201 - Created  |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema   
202 - Accepted  |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.3. /apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies/{name}

Table 15.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ImagePolicy   
Show more

HTTP method
     `DELETE`
Description
     delete an ImagePolicy 

Table 15.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 15.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ImagePolicy 

Table 15.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ImagePolicy 

Table 15.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ImagePolicy 

Table 15.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema  |   
Show more

Table 15.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema   
201 - Created  |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 15.2.4. /apis/config.openshift.io/v1/namespaces/{namespace}/imagepolicies/{name}/status

Table 15.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ImagePolicy   
Show more

HTTP method
     `GET`
Description
     read status of the specified ImagePolicy 

Table 15.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ImagePolicy 

Table 15.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ImagePolicy 

Table 15.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 15.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema  |   
Show more

Table 15.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema   
201 - Created  |  [`ImagePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/imagepolicy-config-openshift-io-v1 "Chapter 15. ImagePolicy \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
