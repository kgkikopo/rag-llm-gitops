# 11.2. API endpoints

The following API endpoints are available: 

  * `/apis/resource.k8s.io/v1/resourceclaimtemplates`

    * `GET`: list or watch objects of kind ResourceClaimTemplate 

  * `/apis/resource.k8s.io/v1/watch/resourceclaimtemplates`

    * `GET`: watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates`

    * `DELETE`: delete collection of ResourceClaimTemplate 
    * `GET`: list or watch objects of kind ResourceClaimTemplate 
    * `POST`: create a ResourceClaimTemplate 

  * `/apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaimtemplates`

    * `GET`: watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates/{name}`

    * `DELETE`: delete a ResourceClaimTemplate 
    * `GET`: read the specified ResourceClaimTemplate 
    * `PATCH`: partially update the specified ResourceClaimTemplate 
    * `PUT`: replace the specified ResourceClaimTemplate 

  * `/apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaimtemplates/{name}`

    * `GET`: watch changes to an object of kind ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 11.2.1. /apis/resource.k8s.io/v1/resourceclaimtemplates

HTTP method
     `GET`
Description
     list or watch objects of kind ResourceClaimTemplate 

Table 11.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaimTemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-resource-v1-ResourceClaimTemplateList) schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.2. /apis/resource.k8s.io/v1/watch/resourceclaimtemplates

HTTP method
     `GET`
Description
     watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead. 

Table 11.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.3. /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates

HTTP method
     `DELETE`
Description
     delete collection of ResourceClaimTemplate 

Table 11.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 11.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind ResourceClaimTemplate 

Table 11.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaimTemplateList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-resource-v1-ResourceClaimTemplateList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ResourceClaimTemplate 

Table 11.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema  |   
Show more

Table 11.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema   
201 - Created  |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema   
202 - Accepted  |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.4. /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaimtemplates

HTTP method
     `GET`
Description
     watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead. 

Table 11.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.5. /apis/resource.k8s.io/v1/namespaces/{namespace}/resourceclaimtemplates/{name}

Table 11.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ResourceClaimTemplate   
Show more

HTTP method
     `DELETE`
Description
     delete a ResourceClaimTemplate 

Table 11.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 11.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema   
202 - Accepted  |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ResourceClaimTemplate 

Table 11.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ResourceClaimTemplate 

Table 11.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema   
201 - Created  |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ResourceClaimTemplate 

Table 11.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema  |   
Show more

Table 11.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema   
201 - Created  |  [`ResourceClaimTemplate`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/resourceclaimtemplate-resource-k8s-io-v1 "Chapter 11. ResourceClaimTemplate \[resource.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.6. /apis/resource.k8s.io/v1/watch/namespaces/{namespace}/resourceclaimtemplates/{name}

Table 11.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ResourceClaimTemplate   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 11.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
