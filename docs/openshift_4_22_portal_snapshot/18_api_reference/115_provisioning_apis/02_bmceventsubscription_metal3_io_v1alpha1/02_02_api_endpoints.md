# 2.2. API endpoints

The following API endpoints are available: 

  * `/apis/metal3.io/v1alpha1/bmceventsubscriptions`

    * `GET`: list objects of kind BMCEventSubscription 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions`

    * `DELETE`: delete collection of BMCEventSubscription 
    * `GET`: list objects of kind BMCEventSubscription 
    * `POST`: create a BMCEventSubscription 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}`

    * `DELETE`: delete a BMCEventSubscription 
    * `GET`: read the specified BMCEventSubscription 
    * `PATCH`: partially update the specified BMCEventSubscription 
    * `PUT`: replace the specified BMCEventSubscription 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}/status`

    * `GET`: read status of the specified BMCEventSubscription 
    * `PATCH`: partially update status of the specified BMCEventSubscription 
    * `PUT`: replace status of the specified BMCEventSubscription 




## 2.2.1. /apis/metal3.io/v1alpha1/bmceventsubscriptions

HTTP method
     `GET`
Description
     list objects of kind BMCEventSubscription 

Table 2.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BMCEventSubscriptionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-BMCEventSubscriptionList) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions

HTTP method
     `DELETE`
Description
     delete collection of BMCEventSubscription 

Table 2.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind BMCEventSubscription 

Table 2.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BMCEventSubscriptionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-BMCEventSubscriptionList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a BMCEventSubscription 

Table 2.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 2.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema   
202 - Accepted  |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}

Table 2.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the BMCEventSubscription   
Show more

HTTP method
     `DELETE`
Description
     delete a BMCEventSubscription 

Table 2.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified BMCEventSubscription 

Table 2.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified BMCEventSubscription 

Table 2.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified BMCEventSubscription 

Table 2.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 2.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.4. /apis/metal3.io/v1alpha1/namespaces/{namespace}/bmceventsubscriptions/{name}/status

Table 2.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the BMCEventSubscription   
Show more

HTTP method
     `GET`
Description
     read status of the specified BMCEventSubscription 

Table 2.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified BMCEventSubscription 

Table 2.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified BMCEventSubscription 

Table 2.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 2.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`BMCEventSubscription`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/bmceventsubscription-metal3-io-v1alpha1 "Chapter 2. BMCEventSubscription \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
