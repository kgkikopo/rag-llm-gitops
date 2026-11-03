# 8.2. API endpoints

The following API endpoints are available: 

  * `/apis/metal3.io/v1alpha1/hostfirmwaresettings`

    * `GET`: list objects of kind HostFirmwareSettings 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings`

    * `DELETE`: delete collection of HostFirmwareSettings 
    * `GET`: list objects of kind HostFirmwareSettings 
    * `POST`: create HostFirmwareSettings 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}`

    * `DELETE`: delete HostFirmwareSettings 
    * `GET`: read the specified HostFirmwareSettings 
    * `PATCH`: partially update the specified HostFirmwareSettings 
    * `PUT`: replace the specified HostFirmwareSettings 

  * `/apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}/status`

    * `GET`: read status of the specified HostFirmwareSettings 
    * `PATCH`: partially update status of the specified HostFirmwareSettings 
    * `PUT`: replace status of the specified HostFirmwareSettings 




## 8.2.1. /apis/metal3.io/v1alpha1/hostfirmwaresettings

HTTP method
     `GET`
Description
     list objects of kind HostFirmwareSettings 

Table 8.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HostFirmwareSettingsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HostFirmwareSettingsList) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.2. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings

HTTP method
     `DELETE`
Description
     delete collection of HostFirmwareSettings 

Table 8.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind HostFirmwareSettings 

Table 8.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HostFirmwareSettingsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-metal3-v1alpha1-HostFirmwareSettingsList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create HostFirmwareSettings 

Table 8.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 8.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema   
202 - Accepted  |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.3. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}

Table 8.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the HostFirmwareSettings   
Show more

HTTP method
     `DELETE`
Description
     delete HostFirmwareSettings 

Table 8.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 8.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified HostFirmwareSettings 

Table 8.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified HostFirmwareSettings 

Table 8.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified HostFirmwareSettings 

Table 8.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 8.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.4. /apis/metal3.io/v1alpha1/namespaces/{namespace}/hostfirmwaresettings/{name}/status

Table 8.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the HostFirmwareSettings   
Show more

HTTP method
     `GET`
Description
     read status of the specified HostFirmwareSettings 

Table 8.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified HostFirmwareSettings 

Table 8.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified HostFirmwareSettings 

Table 8.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema  |   
Show more

Table 8.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema   
201 - Created  |  [`HostFirmwareSettings`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1 "Chapter 8. HostFirmwareSettings \[metal3.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
