# 28.2. API endpoints

The following API endpoints are available: 

  * `/apis/whereabouts.cni.cncf.io/v1alpha1/overlappingrangeipreservations`

    * `GET`: list objects of kind OverlappingRangeIPReservation 

  * `/apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/overlappingrangeipreservations`

    * `DELETE`: delete collection of OverlappingRangeIPReservation 
    * `GET`: list objects of kind OverlappingRangeIPReservation 
    * `POST`: create an OverlappingRangeIPReservation 

  * `/apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/overlappingrangeipreservations/{name}`

    * `DELETE`: delete an OverlappingRangeIPReservation 
    * `GET`: read the specified OverlappingRangeIPReservation 
    * `PATCH`: partially update the specified OverlappingRangeIPReservation 
    * `PUT`: replace the specified OverlappingRangeIPReservation 




## 28.2.1. /apis/whereabouts.cni.cncf.io/v1alpha1/overlappingrangeipreservations

HTTP method
     `GET`
Description
     list objects of kind OverlappingRangeIPReservation 

Table 28.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OverlappingRangeIPReservationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-cncf-cni-whereabouts-v1alpha1-OverlappingRangeIPReservationList) schema   
401 - Unauthorized  |  Empty   
Show more

## 28.2.2. /apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/overlappingrangeipreservations

HTTP method
     `DELETE`
Description
     delete collection of OverlappingRangeIPReservation 

Table 28.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind OverlappingRangeIPReservation 

Table 28.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OverlappingRangeIPReservationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-cncf-cni-whereabouts-v1alpha1-OverlappingRangeIPReservationList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an OverlappingRangeIPReservation 

Table 28.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 28.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OverlappingRangeIPReservation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1 "Chapter 28. OverlappingRangeIPReservation \[whereabouts.cni.cncf.io/v1alpha1\]") schema  |   
Show more

Table 28.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OverlappingRangeIPReservation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1 "Chapter 28. OverlappingRangeIPReservation \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
201 - Created  |  [`OverlappingRangeIPReservation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1 "Chapter 28. OverlappingRangeIPReservation \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
202 - Accepted  |  [`OverlappingRangeIPReservation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1 "Chapter 28. OverlappingRangeIPReservation \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 28.2.3. /apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/overlappingrangeipreservations/{name}

Table 28.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OverlappingRangeIPReservation   
Show more

HTTP method
     `DELETE`
Description
     delete an OverlappingRangeIPReservation 

Table 28.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 28.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified OverlappingRangeIPReservation 

Table 28.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OverlappingRangeIPReservation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1 "Chapter 28. OverlappingRangeIPReservation \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified OverlappingRangeIPReservation 

Table 28.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 28.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OverlappingRangeIPReservation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1 "Chapter 28. OverlappingRangeIPReservation \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified OverlappingRangeIPReservation 

Table 28.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 28.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OverlappingRangeIPReservation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1 "Chapter 28. OverlappingRangeIPReservation \[whereabouts.cni.cncf.io/v1alpha1\]") schema  |   
Show more

Table 28.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OverlappingRangeIPReservation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1 "Chapter 28. OverlappingRangeIPReservation \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
201 - Created  |  [`OverlappingRangeIPReservation`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1 "Chapter 28. OverlappingRangeIPReservation \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
