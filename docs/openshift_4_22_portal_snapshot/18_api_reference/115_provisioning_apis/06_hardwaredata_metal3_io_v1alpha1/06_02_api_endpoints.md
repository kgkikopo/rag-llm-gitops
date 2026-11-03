# 6.2. API endpoints

The following API endpoints are available: 

  * `/apis/metal3.io/v1alpha1/hardwaredata`

    * `GET`: list objects of kind HardwareData 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hardwaredata`

    * `DELETE`: delete collection of HardwareData 
    * `GET`: list objects of kind HardwareData 
    * `POST`: create a HardwareData 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hardwaredata/{name}`

    * `DELETE`: delete a HardwareData 
    * `GET`: read the specified HardwareData 
    * `PATCH`: partially update the specified HardwareData 
    * `PUT`: replace the specified HardwareData 




## 6.2.1. /apis/metal3.io/v1alpha1/hardwaredata

HTTP method
     `GET`
Description
     list objects of kind HardwareData 

Table 6.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HardwareDataList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HardwareDataList) schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hardwaredata

HTTP method
     `DELETE`
Description
     delete collection of HardwareData 

Table 6.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind HardwareData 

Table 6.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HardwareDataList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HardwareDataList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a HardwareData 

Table 6.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`HardwareData`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 6.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HardwareData`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`HardwareData`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData \[metal3.io/v1alpha1\]") schema   
202 - Accepted  |  [`HardwareData`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hardwaredata/{name}

Table 6.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the HardwareData   
Show more

HTTP method
     `DELETE`
Description
     delete a HardwareData 

Table 6.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 6.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified HardwareData 

Table 6.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HardwareData`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified HardwareData 

Table 6.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HardwareData`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified HardwareData 

Table 6.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`HardwareData`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 6.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HardwareData`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`HardwareData`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hardwaredata-metal3-io-v1alpha1 "Chapter 6. HardwareData \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
