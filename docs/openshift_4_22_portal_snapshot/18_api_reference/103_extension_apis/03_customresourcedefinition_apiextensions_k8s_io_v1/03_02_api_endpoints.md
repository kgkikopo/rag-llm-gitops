# 3.2. API endpoints

The following API endpoints are available: 

  * `/apis/apiextensions.k8s.io/v1/customresourcedefinitions`

    * `DELETE`: delete collection of CustomResourceDefinition 
    * `GET`: list or watch objects of kind CustomResourceDefinition 
    * `POST`: create a CustomResourceDefinition 

  * `/apis/apiextensions.k8s.io/v1/watch/customresourcedefinitions`

    * `GET`: watch individual changes to a list of CustomResourceDefinition. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}`

    * `DELETE`: delete a CustomResourceDefinition 
    * `GET`: read the specified CustomResourceDefinition 
    * `PATCH`: partially update the specified CustomResourceDefinition 
    * `PUT`: replace the specified CustomResourceDefinition 

  * `/apis/apiextensions.k8s.io/v1/watch/customresourcedefinitions/{name}`

    * `GET`: watch changes to an object of kind CustomResourceDefinition. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}/status`

    * `GET`: read status of the specified CustomResourceDefinition 
    * `PATCH`: partially update status of the specified CustomResourceDefinition 
    * `PUT`: replace status of the specified CustomResourceDefinition 




## 3.2.1. /apis/apiextensions.k8s.io/v1/customresourcedefinitions

HTTP method
     `DELETE`
Description
     delete collection of CustomResourceDefinition 

Table 3.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind CustomResourceDefinition 

Table 3.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CustomResourceDefinitionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-CustomResourceDefinitionList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a CustomResourceDefinition 

Table 3.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema  |   
Show more

Table 3.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
201 - Created  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
202 - Accepted  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.2. /apis/apiextensions.k8s.io/v1/watch/customresourcedefinitions

HTTP method
     `GET`
Description
     watch individual changes to a list of CustomResourceDefinition. deprecated: use the 'watch' parameter with a list operation instead. 

Table 3.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.3. /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}

Table 3.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CustomResourceDefinition   
Show more

HTTP method
     `DELETE`
Description
     delete a CustomResourceDefinition 

Table 3.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified CustomResourceDefinition 

Table 3.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified CustomResourceDefinition 

Table 3.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
201 - Created  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified CustomResourceDefinition 

Table 3.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema  |   
Show more

Table 3.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
201 - Created  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.4. /apis/apiextensions.k8s.io/v1/watch/customresourcedefinitions/{name}

Table 3.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CustomResourceDefinition   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind CustomResourceDefinition. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 3.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.5. /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}/status

Table 3.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CustomResourceDefinition   
Show more

HTTP method
     `GET`
Description
     read status of the specified CustomResourceDefinition 

Table 3.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified CustomResourceDefinition 

Table 3.21. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
201 - Created  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified CustomResourceDefinition 

Table 3.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.24. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema  |   
Show more

Table 3.25. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
201 - Created  |  [`CustomResourceDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extension_apis/customresourcedefinition-apiextensions-k8s-io-v1 "Chapter 3. CustomResourceDefinition \[apiextensions.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
