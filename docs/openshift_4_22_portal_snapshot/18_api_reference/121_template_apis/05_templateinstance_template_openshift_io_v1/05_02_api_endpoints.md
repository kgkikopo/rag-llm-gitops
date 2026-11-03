# 5.2. API endpoints

The following API endpoints are available: 

  * `/apis/template.openshift.io/v1/templateinstances`

    * `GET`: list or watch objects of kind TemplateInstance 

  * `/apis/template.openshift.io/v1/watch/templateinstances`

    * `GET`: watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances`

    * `DELETE`: delete collection of TemplateInstance 
    * `GET`: list or watch objects of kind TemplateInstance 
    * `POST`: create a TemplateInstance 

  * `/apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances`

    * `GET`: watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}`

    * `DELETE`: delete a TemplateInstance 
    * `GET`: read the specified TemplateInstance 
    * `PATCH`: partially update the specified TemplateInstance 
    * `PUT`: replace the specified TemplateInstance 

  * `/apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances/{name}`

    * `GET`: watch changes to an object of kind TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}/status`

    * `GET`: read status of the specified TemplateInstance 
    * `PATCH`: partially update status of the specified TemplateInstance 
    * `PUT`: replace status of the specified TemplateInstance 




## 5.2.1. /apis/template.openshift.io/v1/templateinstances

HTTP method
     `GET`
Description
     list or watch objects of kind TemplateInstance 

Table 5.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TemplateInstanceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-template-v1-TemplateInstanceList) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.2. /apis/template.openshift.io/v1/watch/templateinstances

HTTP method
     `GET`
Description
     watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead. 

Table 5.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.3. /apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances

HTTP method
     `DELETE`
Description
     delete collection of TemplateInstance 

Table 5.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind TemplateInstance 

Table 5.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TemplateInstanceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-template-v1-TemplateInstanceList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a TemplateInstance 

Table 5.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema  |   
Show more

Table 5.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
201 - Created  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
202 - Accepted  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.4. /apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances

HTTP method
     `GET`
Description
     watch individual changes to a list of TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead. 

Table 5.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.5. /apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}

Table 5.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the TemplateInstance   
Show more

HTTP method
     `DELETE`
Description
     delete a TemplateInstance 

Table 5.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified TemplateInstance 

Table 5.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified TemplateInstance 

Table 5.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
201 - Created  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified TemplateInstance 

Table 5.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema  |   
Show more

Table 5.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
201 - Created  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.6. /apis/template.openshift.io/v1/watch/namespaces/{namespace}/templateinstances/{name}

Table 5.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the TemplateInstance   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind TemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 5.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.7. /apis/template.openshift.io/v1/namespaces/{namespace}/templateinstances/{name}/status

Table 5.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the TemplateInstance   
Show more

HTTP method
     `GET`
Description
     read status of the specified TemplateInstance 

Table 5.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified TemplateInstance 

Table 5.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
201 - Created  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified TemplateInstance 

Table 5.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema  |   
Show more

Table 5.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
201 - Created  |  [`TemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/templateinstance-template-openshift-io-v1 "Chapter 5. TemplateInstance \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
