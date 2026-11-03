# 4.2. API endpoints

The following API endpoints are available: 

  * `/apis/template.openshift.io/v1/templates`

    * `GET`: list or watch objects of kind Template 

  * `/apis/template.openshift.io/v1/watch/templates`

    * `GET`: watch individual changes to a list of Template. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/template.openshift.io/v1/namespaces/{namespace}/templates`

    * `DELETE`: delete collection of Template 
    * `GET`: list or watch objects of kind Template 
    * `POST`: create a Template 

  * `/apis/template.openshift.io/v1/watch/namespaces/{namespace}/templates`

    * `GET`: watch individual changes to a list of Template. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/template.openshift.io/v1/namespaces/{namespace}/templates/{name}`

    * `DELETE`: delete a Template 
    * `GET`: read the specified Template 
    * `PATCH`: partially update the specified Template 
    * `PUT`: replace the specified Template 

  * `/apis/template.openshift.io/v1/namespaces/{namespace}/processedtemplates`

    * `POST`: create a Template 

  * `/apis/template.openshift.io/v1/watch/namespaces/{namespace}/templates/{name}`

    * `GET`: watch changes to an object of kind Template. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 4.2.1. /apis/template.openshift.io/v1/templates

HTTP method
     `GET`
Description
     list or watch objects of kind Template 

Table 4.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-template-v1-TemplateList) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.2. /apis/template.openshift.io/v1/watch/templates

HTTP method
     `GET`
Description
     watch individual changes to a list of Template. deprecated: use the 'watch' parameter with a list operation instead. 

Table 4.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.3. /apis/template.openshift.io/v1/namespaces/{namespace}/templates

HTTP method
     `DELETE`
Description
     delete collection of Template 

Table 4.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Template 

Table 4.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`TemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-template-v1-TemplateList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Template 

Table 4.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema  |   
Show more

Table 4.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
201 - Created  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
202 - Accepted  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.4. /apis/template.openshift.io/v1/watch/namespaces/{namespace}/templates

HTTP method
     `GET`
Description
     watch individual changes to a list of Template. deprecated: use the 'watch' parameter with a list operation instead. 

Table 4.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.5. /apis/template.openshift.io/v1/namespaces/{namespace}/templates/{name}

Table 4.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Template   
Show more

HTTP method
     `DELETE`
Description
     delete a Template 

Table 4.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
202 - Accepted  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Template 

Table 4.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Template 

Table 4.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
201 - Created  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Template 

Table 4.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema  |   
Show more

Table 4.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
201 - Created  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.6. /apis/template.openshift.io/v1/namespaces/{namespace}/processedtemplates

Table 4.19. Global query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

HTTP method
     `POST`
Description
     create a Template 

Table 4.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema  |   
Show more

Table 4.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
201 - Created  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
202 - Accepted  |  [`Template`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/template-template-openshift-io-v1 "Chapter 4. Template \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.7. /apis/template.openshift.io/v1/watch/namespaces/{namespace}/templates/{name}

Table 4.22. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Template   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Template. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 4.23. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
