# 3.2. API endpoints

The following API endpoints are available: 

  * `/apis/console.openshift.io/v1/consoleexternalloglinks`

    * `DELETE`: delete collection of ConsoleExternalLogLink 
    * `GET`: list objects of kind ConsoleExternalLogLink 
    * `POST`: create a ConsoleExternalLogLink 

  * `/apis/console.openshift.io/v1/consoleexternalloglinks/{name}`

    * `DELETE`: delete a ConsoleExternalLogLink 
    * `GET`: read the specified ConsoleExternalLogLink 
    * `PATCH`: partially update the specified ConsoleExternalLogLink 
    * `PUT`: replace the specified ConsoleExternalLogLink 

  * `/apis/console.openshift.io/v1/consoleexternalloglinks/{name}/status`

    * `GET`: read status of the specified ConsoleExternalLogLink 
    * `PATCH`: partially update status of the specified ConsoleExternalLogLink 
    * `PUT`: replace status of the specified ConsoleExternalLogLink 




## 3.2.1. /apis/console.openshift.io/v1/consoleexternalloglinks

HTTP method
     `DELETE`
Description
     delete collection of ConsoleExternalLogLink 

Table 3.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind ConsoleExternalLogLink 

Table 3.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleExternalLogLinkList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsoleExternalLogLinkList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ConsoleExternalLogLink 

Table 3.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema  |   
Show more

Table 3.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema   
201 - Created  |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema   
202 - Accepted  |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.2. /apis/console.openshift.io/v1/consoleexternalloglinks/{name}

Table 3.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ConsoleExternalLogLink   
Show more

HTTP method
     `DELETE`
Description
     delete a ConsoleExternalLogLink 

Table 3.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ConsoleExternalLogLink 

Table 3.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ConsoleExternalLogLink 

Table 3.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ConsoleExternalLogLink 

Table 3.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema  |   
Show more

Table 3.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema   
201 - Created  |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.3. /apis/console.openshift.io/v1/consoleexternalloglinks/{name}/status

Table 3.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ConsoleExternalLogLink   
Show more

HTTP method
     `GET`
Description
     read status of the specified ConsoleExternalLogLink 

Table 3.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ConsoleExternalLogLink 

Table 3.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ConsoleExternalLogLink 

Table 3.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema  |   
Show more

Table 3.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema   
201 - Created  |  [`ConsoleExternalLogLink`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleexternalloglink-console-openshift-io-v1 "Chapter 3. ConsoleExternalLogLink \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
