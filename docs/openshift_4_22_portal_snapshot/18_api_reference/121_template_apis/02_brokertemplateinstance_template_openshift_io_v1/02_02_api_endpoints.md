# 2.2. API endpoints

The following API endpoints are available: 

  * `/apis/template.openshift.io/v1/brokertemplateinstances`

    * `DELETE`: delete collection of BrokerTemplateInstance 
    * `GET`: list or watch objects of kind BrokerTemplateInstance 
    * `POST`: create a BrokerTemplateInstance 

  * `/apis/template.openshift.io/v1/watch/brokertemplateinstances`

    * `GET`: watch individual changes to a list of BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/template.openshift.io/v1/brokertemplateinstances/{name}`

    * `DELETE`: delete a BrokerTemplateInstance 
    * `GET`: read the specified BrokerTemplateInstance 
    * `PATCH`: partially update the specified BrokerTemplateInstance 
    * `PUT`: replace the specified BrokerTemplateInstance 

  * `/apis/template.openshift.io/v1/watch/brokertemplateinstances/{name}`

    * `GET`: watch changes to an object of kind BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 2.2.1. /apis/template.openshift.io/v1/brokertemplateinstances

HTTP method
     `DELETE`
Description
     delete collection of BrokerTemplateInstance 

Table 2.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind BrokerTemplateInstance 

Table 2.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BrokerTemplateInstanceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-template-v1-BrokerTemplateInstanceList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a BrokerTemplateInstance 

Table 2.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BrokerTemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance \[template.openshift.io/v1\]") schema  |   
Show more

Table 2.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BrokerTemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance \[template.openshift.io/v1\]") schema   
201 - Created  |  [`BrokerTemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance \[template.openshift.io/v1\]") schema   
202 - Accepted  |  [`BrokerTemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /apis/template.openshift.io/v1/watch/brokertemplateinstances

HTTP method
     `GET`
Description
     watch individual changes to a list of BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead. 

Table 2.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /apis/template.openshift.io/v1/brokertemplateinstances/{name}

Table 2.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the BrokerTemplateInstance   
Show more

HTTP method
     `DELETE`
Description
     delete a BrokerTemplateInstance 

Table 2.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified BrokerTemplateInstance 

Table 2.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BrokerTemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified BrokerTemplateInstance 

Table 2.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BrokerTemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance \[template.openshift.io/v1\]") schema   
201 - Created  |  [`BrokerTemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified BrokerTemplateInstance 

Table 2.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BrokerTemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance \[template.openshift.io/v1\]") schema  |   
Show more

Table 2.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BrokerTemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance \[template.openshift.io/v1\]") schema   
201 - Created  |  [`BrokerTemplateInstance`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/template_apis/brokertemplateinstance-template-openshift-io-v1 "Chapter 2. BrokerTemplateInstance \[template.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.4. /apis/template.openshift.io/v1/watch/brokertemplateinstances/{name}

Table 2.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the BrokerTemplateInstance   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind BrokerTemplateInstance. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 2.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
