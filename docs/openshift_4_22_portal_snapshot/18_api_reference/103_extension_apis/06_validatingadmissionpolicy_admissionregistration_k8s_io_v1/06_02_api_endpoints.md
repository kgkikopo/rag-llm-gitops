# 6.2. API endpoints

The following API endpoints are available: 

  * `/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies`

    * `DELETE`: delete collection of ValidatingAdmissionPolicy 
    * `GET`: list or watch objects of kind ValidatingAdmissionPolicy 
    * `POST`: create a ValidatingAdmissionPolicy 

  * `/apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies`

    * `GET`: watch individual changes to a list of ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}`

    * `DELETE`: delete a ValidatingAdmissionPolicy 
    * `GET`: read the specified ValidatingAdmissionPolicy 
    * `PATCH`: partially update the specified ValidatingAdmissionPolicy 
    * `PUT`: replace the specified ValidatingAdmissionPolicy 

  * `/apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies/{name}`

    * `GET`: watch changes to an object of kind ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status`

    * `GET`: read status of the specified ValidatingAdmissionPolicy 
    * `PATCH`: partially update status of the specified ValidatingAdmissionPolicy 
    * `PUT`: replace status of the specified ValidatingAdmissionPolicy 




## 6.2.1. /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies

HTTP method
     `DELETE`
Description
     delete collection of ValidatingAdmissionPolicy 

Table 6.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 6.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind ValidatingAdmissionPolicy 

Table 6.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ValidatingAdmissionPolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-admissionregistration-v1-ValidatingAdmissionPolicyList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ValidatingAdmissionPolicy 

Table 6.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema  |   
Show more

Table 6.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
201 - Created  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
202 - Accepted  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.2. /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies

HTTP method
     `GET`
Description
     watch individual changes to a list of ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead. 

Table 6.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.3. /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}

Table 6.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ValidatingAdmissionPolicy   
Show more

HTTP method
     `DELETE`
Description
     delete a ValidatingAdmissionPolicy 

Table 6.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 6.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ValidatingAdmissionPolicy 

Table 6.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ValidatingAdmissionPolicy 

Table 6.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
201 - Created  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ValidatingAdmissionPolicy 

Table 6.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema  |   
Show more

Table 6.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
201 - Created  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.4. /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies/{name}

Table 6.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ValidatingAdmissionPolicy   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 6.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.5. /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status

Table 6.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ValidatingAdmissionPolicy   
Show more

HTTP method
     `GET`
Description
     read status of the specified ValidatingAdmissionPolicy 

Table 6.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ValidatingAdmissionPolicy 

Table 6.21. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
201 - Created  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ValidatingAdmissionPolicy 

Table 6.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.24. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema  |   
Show more

Table 6.25. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
201 - Created  |  [`ValidatingAdmissionPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1 "Chapter 6. ValidatingAdmissionPolicy \[admissionregistration.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
