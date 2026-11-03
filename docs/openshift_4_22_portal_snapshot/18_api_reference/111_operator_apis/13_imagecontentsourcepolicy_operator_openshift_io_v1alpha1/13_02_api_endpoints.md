# 13.2. API endpoints

The following API endpoints are available: 

  * `/apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies`

    * `DELETE`: delete collection of ImageContentSourcePolicy 
    * `GET`: list objects of kind ImageContentSourcePolicy 
    * `POST`: create an ImageContentSourcePolicy 

  * `/apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies/{name}`

    * `DELETE`: delete an ImageContentSourcePolicy 
    * `GET`: read the specified ImageContentSourcePolicy 
    * `PATCH`: partially update the specified ImageContentSourcePolicy 
    * `PUT`: replace the specified ImageContentSourcePolicy 

  * `/apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies/{name}/status`

    * `GET`: read status of the specified ImageContentSourcePolicy 
    * `PATCH`: partially update status of the specified ImageContentSourcePolicy 
    * `PUT`: replace status of the specified ImageContentSourcePolicy 




## 13.2.1. /apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies

HTTP method
     `DELETE`
Description
     delete collection of ImageContentSourcePolicy 

Table 13.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind ImageContentSourcePolicy 

Table 13.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageContentSourcePolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-operator-v1alpha1-ImageContentSourcePolicyList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an ImageContentSourcePolicy 

Table 13.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema  |   
Show more

Table 13.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema   
201 - Created  |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema   
202 - Accepted  |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.2. /apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies/{name}

Table 13.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ImageContentSourcePolicy   
Show more

HTTP method
     `DELETE`
Description
     delete an ImageContentSourcePolicy 

Table 13.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 13.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ImageContentSourcePolicy 

Table 13.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ImageContentSourcePolicy 

Table 13.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ImageContentSourcePolicy 

Table 13.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema  |   
Show more

Table 13.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema   
201 - Created  |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.3. /apis/operator.openshift.io/v1alpha1/imagecontentsourcepolicies/{name}/status

Table 13.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ImageContentSourcePolicy   
Show more

HTTP method
     `GET`
Description
     read status of the specified ImageContentSourcePolicy 

Table 13.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ImageContentSourcePolicy 

Table 13.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ImageContentSourcePolicy 

Table 13.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema  |   
Show more

Table 13.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema   
201 - Created  |  [`ImageContentSourcePolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1 "Chapter 13. ImageContentSourcePolicy \[operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
