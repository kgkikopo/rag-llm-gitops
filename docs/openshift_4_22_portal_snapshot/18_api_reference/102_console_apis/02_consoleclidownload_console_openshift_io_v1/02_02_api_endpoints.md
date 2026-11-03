# 2.2. API endpoints

The following API endpoints are available: 

  * `/apis/console.openshift.io/v1/consoleclidownloads`

    * `DELETE`: delete collection of ConsoleCLIDownload 
    * `GET`: list objects of kind ConsoleCLIDownload 
    * `POST`: create a ConsoleCLIDownload 

  * `/apis/console.openshift.io/v1/consoleclidownloads/{name}`

    * `DELETE`: delete a ConsoleCLIDownload 
    * `GET`: read the specified ConsoleCLIDownload 
    * `PATCH`: partially update the specified ConsoleCLIDownload 
    * `PUT`: replace the specified ConsoleCLIDownload 

  * `/apis/console.openshift.io/v1/consoleclidownloads/{name}/status`

    * `GET`: read status of the specified ConsoleCLIDownload 
    * `PATCH`: partially update status of the specified ConsoleCLIDownload 
    * `PUT`: replace status of the specified ConsoleCLIDownload 




## 2.2.1. /apis/console.openshift.io/v1/consoleclidownloads

HTTP method
     `DELETE`
Description
     delete collection of ConsoleCLIDownload 

Table 2.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind ConsoleCLIDownload 

Table 2.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleCLIDownloadList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-console-v1-ConsoleCLIDownloadList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ConsoleCLIDownload 

Table 2.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema  |   
Show more

Table 2.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema   
201 - Created  |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema   
202 - Accepted  |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /apis/console.openshift.io/v1/consoleclidownloads/{name}

Table 2.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ConsoleCLIDownload   
Show more

HTTP method
     `DELETE`
Description
     delete a ConsoleCLIDownload 

Table 2.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ConsoleCLIDownload 

Table 2.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ConsoleCLIDownload 

Table 2.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ConsoleCLIDownload 

Table 2.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema  |   
Show more

Table 2.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema   
201 - Created  |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /apis/console.openshift.io/v1/consoleclidownloads/{name}/status

Table 2.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ConsoleCLIDownload   
Show more

HTTP method
     `GET`
Description
     read status of the specified ConsoleCLIDownload 

Table 2.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ConsoleCLIDownload 

Table 2.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ConsoleCLIDownload 

Table 2.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema  |   
Show more

Table 2.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema   
201 - Created  |  [`ConsoleCLIDownload`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/console_apis/consoleclidownload-console-openshift-io-v1 "Chapter 2. ConsoleCLIDownload \[console.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
