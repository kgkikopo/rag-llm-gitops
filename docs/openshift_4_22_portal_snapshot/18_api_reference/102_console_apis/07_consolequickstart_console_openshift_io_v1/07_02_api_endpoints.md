# 7.2. API endpoints

The following API endpoints are available: 

  * `/apis/console.openshift.io/v1/consolequickstarts`

    * `DELETE`: delete collection of ConsoleQuickStart 
    * `GET`: list objects of kind ConsoleQuickStart 
    * `POST`: create a ConsoleQuickStart 

  * `/apis/console.openshift.io/v1/consolequickstarts/{name}`

    * `DELETE`: delete a ConsoleQuickStart 
    * `GET`: read the specified ConsoleQuickStart 
    * `PATCH`: partially update the specified ConsoleQuickStart 
    * `PUT`: replace the specified ConsoleQuickStart 




## 7.2.1. /apis/console.openshift.io/v1/consolequickstarts

HTTP method
     `DELETE`
Description
     delete collection of ConsoleQuickStart 

Table 7.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind ConsoleQuickStart 

Table 7.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleQuickStartList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsoleQuickStartList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ConsoleQuickStart 

Table 7.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ConsoleQuickStart`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart \[console.openshift.io/v1\]") schema  |   
Show more

Table 7.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleQuickStart`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart \[console.openshift.io/v1\]") schema   
201 - Created  |  [`ConsoleQuickStart`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart \[console.openshift.io/v1\]") schema   
202 - Accepted  |  [`ConsoleQuickStart`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.2. /apis/console.openshift.io/v1/consolequickstarts/{name}

Table 7.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ConsoleQuickStart   
Show more

HTTP method
     `DELETE`
Description
     delete a ConsoleQuickStart 

Table 7.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 7.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ConsoleQuickStart 

Table 7.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleQuickStart`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ConsoleQuickStart 

Table 7.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleQuickStart`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ConsoleQuickStart 

Table 7.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ConsoleQuickStart`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart \[console.openshift.io/v1\]") schema  |   
Show more

Table 7.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleQuickStart`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart \[console.openshift.io/v1\]") schema   
201 - Created  |  [`ConsoleQuickStart`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consolequickstart-console-openshift-io-v1 "Chapter 7. ConsoleQuickStart \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
