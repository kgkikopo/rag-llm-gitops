# 4.2. API endpoints

The following API endpoints are available: 

  * `/apis/metal3.io/v1alpha1/dataimages`

    * `GET`: list objects of kind DataImage 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages`

    * `DELETE`: delete collection of DataImage 
    * `GET`: list objects of kind DataImage 
    * `POST`: create a DataImage 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages/{name}`

    * `DELETE`: delete a DataImage 
    * `GET`: read the specified DataImage 
    * `PATCH`: partially update the specified DataImage 
    * `PUT`: replace the specified DataImage 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages/{name}/status`

    * `GET`: read status of the specified DataImage 
    * `PATCH`: partially update status of the specified DataImage 
    * `PUT`: replace status of the specified DataImage 




## 4.2.1. /apis/metal3.io/v1alpha1/dataimages

HTTP method
     `GET`
Description
     list objects of kind DataImage 

Table 4.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DataImageList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-DataImageList) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages

HTTP method
     `DELETE`
Description
     delete collection of DataImage 

Table 4.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind DataImage 

Table 4.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DataImageList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-DataImageList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a DataImage 

Table 4.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 4.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema   
202 - Accepted  |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages/{name}

Table 4.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the DataImage   
Show more

HTTP method
     `DELETE`
Description
     delete a DataImage 

Table 4.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified DataImage 

Table 4.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified DataImage 

Table 4.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified DataImage 

Table 4.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 4.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.4. /apis/metal3.io/v1alpha1/namespaces/{namespace}/dataimages/{name}/status

Table 4.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the DataImage   
Show more

HTTP method
     `GET`
Description
     read status of the specified DataImage 

Table 4.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified DataImage 

Table 4.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified DataImage 

Table 4.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 4.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`DataImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/dataimage-metal3-io-v1alpha1 "Chapter 4. DataImage \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
