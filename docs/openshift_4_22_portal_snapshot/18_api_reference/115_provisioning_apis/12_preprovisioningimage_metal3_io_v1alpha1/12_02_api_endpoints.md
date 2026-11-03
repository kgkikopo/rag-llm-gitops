# 12.2. API endpoints

The following API endpoints are available: 

  * `/apis/metal3.io/v1alpha1/preprovisioningimages`

    * `GET`: list objects of kind PreprovisioningImage 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages`

    * `DELETE`: delete collection of PreprovisioningImage 
    * `GET`: list objects of kind PreprovisioningImage 
    * `POST`: create a PreprovisioningImage 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages/{name}`

    * `DELETE`: delete a PreprovisioningImage 
    * `GET`: read the specified PreprovisioningImage 
    * `PATCH`: partially update the specified PreprovisioningImage 
    * `PUT`: replace the specified PreprovisioningImage 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages/{name}/status`

    * `GET`: read status of the specified PreprovisioningImage 
    * `PATCH`: partially update status of the specified PreprovisioningImage 
    * `PUT`: replace status of the specified PreprovisioningImage 




## 12.2.1. /apis/metal3.io/v1alpha1/preprovisioningimages

HTTP method
     `GET`
Description
     list objects of kind PreprovisioningImage 

Table 12.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PreprovisioningImageList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-PreprovisioningImageList) schema   
401 - Unauthorized  |  Empty   
Show more

## 12.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages

HTTP method
     `DELETE`
Description
     delete collection of PreprovisioningImage 

Table 12.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind PreprovisioningImage 

Table 12.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PreprovisioningImageList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-PreprovisioningImageList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a PreprovisioningImage 

Table 12.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 12.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 12.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema   
202 - Accepted  |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 12.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages/{name}

Table 12.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PreprovisioningImage   
Show more

HTTP method
     `DELETE`
Description
     delete a PreprovisioningImage 

Table 12.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 12.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified PreprovisioningImage 

Table 12.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified PreprovisioningImage 

Table 12.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 12.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified PreprovisioningImage 

Table 12.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 12.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 12.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 12.2.4. /apis/metal3.io/v1alpha1/namespaces/{namespace}/preprovisioningimages/{name}/status

Table 12.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PreprovisioningImage   
Show more

HTTP method
     `GET`
Description
     read status of the specified PreprovisioningImage 

Table 12.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified PreprovisioningImage 

Table 12.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 12.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified PreprovisioningImage 

Table 12.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 12.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 12.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`PreprovisioningImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/preprovisioningimage-metal3-io-v1alpha1 "Chapter 12. PreprovisioningImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
