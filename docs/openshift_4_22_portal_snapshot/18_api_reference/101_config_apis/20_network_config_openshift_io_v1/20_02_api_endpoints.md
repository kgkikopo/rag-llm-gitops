# 20.2. API endpoints

The following API endpoints are available: 

  * `/apis/config.openshift.io/v1/networks`

    * `DELETE`: delete collection of Network 
    * `GET`: list objects of kind Network 
    * `POST`: create a Network 

  * `/apis/config.openshift.io/v1/networks/{name}`

    * `DELETE`: delete a Network 
    * `GET`: read the specified Network 
    * `PATCH`: partially update the specified Network 
    * `PUT`: replace the specified Network 




## 20.2.1. /apis/config.openshift.io/v1/networks

HTTP method
     `DELETE`
Description
     delete collection of Network 

Table 20.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind Network 

Table 20.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-config-v1-NetworkList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Network 

Table 20.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 20.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Network`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/network-config-openshift-io-v1 "Chapter 20. Network \[config.openshift.io/v1\]") schema  |   
Show more

Table 20.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Network`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/network-config-openshift-io-v1 "Chapter 20. Network \[config.openshift.io/v1\]") schema   
201 - Created  |  [`Network`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/network-config-openshift-io-v1 "Chapter 20. Network \[config.openshift.io/v1\]") schema   
202 - Accepted  |  [`Network`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/network-config-openshift-io-v1 "Chapter 20. Network \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 20.2.2. /apis/config.openshift.io/v1/networks/{name}

Table 20.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Network   
Show more

HTTP method
     `DELETE`
Description
     delete a Network 

Table 20.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 20.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Network 

Table 20.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Network`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/network-config-openshift-io-v1 "Chapter 20. Network \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Network 

Table 20.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 20.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Network`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/network-config-openshift-io-v1 "Chapter 20. Network \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Network 

Table 20.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 20.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Network`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/network-config-openshift-io-v1 "Chapter 20. Network \[config.openshift.io/v1\]") schema  |   
Show more

Table 20.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Network`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/network-config-openshift-io-v1 "Chapter 20. Network \[config.openshift.io/v1\]") schema   
201 - Created  |  [`Network`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/network-config-openshift-io-v1 "Chapter 20. Network \[config.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
