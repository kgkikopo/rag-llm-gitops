# 5.2. API endpoints

The following API endpoints are available: 

  * `/apis/testextension.redhat.io/v1/testextensionadmissions`

    * `DELETE`: delete collection of TestExtensionAdmission 
    * `GET`: list objects of kind TestExtensionAdmission 
    * `POST`: create a TestExtensionAdmission 

  * `/apis/testextension.redhat.io/v1/testextensionadmissions/{name}`

    * `DELETE`: delete a TestExtensionAdmission 
    * `GET`: read the specified TestExtensionAdmission 
    * `PATCH`: partially update the specified TestExtensionAdmission 
    * `PUT`: replace the specified TestExtensionAdmission 

  * `/apis/testextension.redhat.io/v1/testextensionadmissions/{name}/status`

    * `GET`: read status of the specified TestExtensionAdmission 
    * `PATCH`: partially update status of the specified TestExtensionAdmission 
    * `PUT`: replace status of the specified TestExtensionAdmission 




## 5.2.1. /apis/testextension.redhat.io/v1/testextensionadmissions

HTTP method
     `DELETE`
Description
     delete collection of TestExtensionAdmission 

Table 5.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind TestExtensionAdmission 

Table 5.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TestExtensionAdmissionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-redhat-testextension-v1-TestExtensionAdmissionList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a TestExtensionAdmission 

Table 5.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema  |   
Show more

Table 5.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema   
201 - Created  |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema   
202 - Accepted  |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.2. /apis/testextension.redhat.io/v1/testextensionadmissions/{name}

Table 5.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the TestExtensionAdmission   
Show more

HTTP method
     `DELETE`
Description
     delete a TestExtensionAdmission 

Table 5.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified TestExtensionAdmission 

Table 5.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified TestExtensionAdmission 

Table 5.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified TestExtensionAdmission 

Table 5.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema  |   
Show more

Table 5.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema   
201 - Created  |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.3. /apis/testextension.redhat.io/v1/testextensionadmissions/{name}/status

Table 5.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the TestExtensionAdmission   
Show more

HTTP method
     `GET`
Description
     read status of the specified TestExtensionAdmission 

Table 5.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified TestExtensionAdmission 

Table 5.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified TestExtensionAdmission 

Table 5.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema  |   
Show more

Table 5.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema   
201 - Created  |  [`TestExtensionAdmission`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/testextensionadmission-testextension-redhat-io-v1 "Chapter 5. TestExtensionAdmission \[testextension.redhat.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
