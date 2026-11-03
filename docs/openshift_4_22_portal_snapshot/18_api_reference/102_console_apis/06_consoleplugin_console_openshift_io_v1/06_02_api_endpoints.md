# 6.2. API endpoints

The following API endpoints are available: 

  * `/apis/console.openshift.io/v1/consoleplugins`

    * `DELETE`: delete collection of ConsolePlugin 
    * `GET`: list objects of kind ConsolePlugin 
    * `POST`: create a ConsolePlugin 

  * `/apis/console.openshift.io/v1/consoleplugins/{name}`

    * `DELETE`: delete a ConsolePlugin 
    * `GET`: read the specified ConsolePlugin 
    * `PATCH`: partially update the specified ConsolePlugin 
    * `PUT`: replace the specified ConsolePlugin 




## 6.2.1. /apis/console.openshift.io/v1/consoleplugins

HTTP method
     `DELETE`
Description
     delete collection of ConsolePlugin 

Table 6.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind ConsolePlugin 

Table 6.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsolePluginList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsolePluginList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ConsolePlugin 

Table 6.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ConsolePlugin`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin \[console.openshift.io/v1\]") schema  |   
Show more

Table 6.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsolePlugin`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin \[console.openshift.io/v1\]") schema   
201 - Created  |  [`ConsolePlugin`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin \[console.openshift.io/v1\]") schema   
202 - Accepted  |  [`ConsolePlugin`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.2. /apis/console.openshift.io/v1/consoleplugins/{name}

Table 6.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ConsolePlugin   
Show more

HTTP method
     `DELETE`
Description
     delete a ConsolePlugin 

Table 6.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 6.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ConsolePlugin 

Table 6.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsolePlugin`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ConsolePlugin 

Table 6.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsolePlugin`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ConsolePlugin 

Table 6.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ConsolePlugin`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin \[console.openshift.io/v1\]") schema  |   
Show more

Table 6.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsolePlugin`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin \[console.openshift.io/v1\]") schema   
201 - Created  |  [`ConsolePlugin`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleplugin-console-openshift-io-v1 "Chapter 6. ConsolePlugin \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
