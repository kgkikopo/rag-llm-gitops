# 13.2. API endpoints

The following API endpoints are available: 

  * `/apis/operators.coreos.com/v1alpha1/subscriptions`

    * `GET`: list objects of kind Subscription 

  * `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/subscriptions`

    * `DELETE`: delete collection of Subscription 
    * `GET`: list objects of kind Subscription 
    * `POST`: create a Subscription 

  * `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/subscriptions/{name}`

    * `DELETE`: delete a Subscription 
    * `GET`: read the specified Subscription 
    * `PATCH`: partially update the specified Subscription 
    * `PUT`: replace the specified Subscription 

  * `/apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/subscriptions/{name}/status`

    * `GET`: read status of the specified Subscription 
    * `PATCH`: partially update status of the specified Subscription 
    * `PUT`: replace status of the specified Subscription 




## 13.2.1. /apis/operators.coreos.com/v1alpha1/subscriptions

HTTP method
     `GET`
Description
     list objects of kind Subscription 

Table 13.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SubscriptionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-operators-v1alpha1-SubscriptionList) schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.2. /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/subscriptions

HTTP method
     `DELETE`
Description
     delete collection of Subscription 

Table 13.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind Subscription 

Table 13.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SubscriptionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-coreos-operators-v1alpha1-SubscriptionList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Subscription 

Table 13.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema  |   
Show more

Table 13.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema   
201 - Created  |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema   
202 - Accepted  |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.3. /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/subscriptions/{name}

Table 13.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Subscription   
Show more

HTTP method
     `DELETE`
Description
     delete a Subscription 

Table 13.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 13.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Subscription 

Table 13.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Subscription 

Table 13.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Subscription 

Table 13.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema  |   
Show more

Table 13.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema   
201 - Created  |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 13.2.4. /apis/operators.coreos.com/v1alpha1/namespaces/{namespace}/subscriptions/{name}/status

Table 13.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Subscription   
Show more

HTTP method
     `GET`
Description
     read status of the specified Subscription 

Table 13.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Subscription 

Table 13.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Subscription 

Table 13.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 13.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema  |   
Show more

Table 13.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema   
201 - Created  |  [`Subscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/operatorhub_apis/subscription-operators-coreos-com-v1alpha1 "Chapter 13. Subscription \[operators.coreos.com/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
