# 5.2. API endpoints

The following API endpoints are available: 

  * `/apis/gateway.networking.k8s.io/v1/backendtlspolicies`

    * `GET`: list objects of kind BackendTLSPolicy 

  * `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies`

    * `DELETE`: delete collection of BackendTLSPolicy 
    * `GET`: list objects of kind BackendTLSPolicy 
    * `POST`: create a BackendTLSPolicy 

  * `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies/{name}`

    * `DELETE`: delete a BackendTLSPolicy 
    * `GET`: read the specified BackendTLSPolicy 
    * `PATCH`: partially update the specified BackendTLSPolicy 
    * `PUT`: replace the specified BackendTLSPolicy 

  * `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies/{name}/status`

    * `GET`: read status of the specified BackendTLSPolicy 
    * `PATCH`: partially update status of the specified BackendTLSPolicy 
    * `PUT`: replace status of the specified BackendTLSPolicy 




## 5.2.1. /apis/gateway.networking.k8s.io/v1/backendtlspolicies

HTTP method
     `GET`
Description
     list objects of kind BackendTLSPolicy 

Table 5.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BackendTLSPolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-networking-gateway-v1-BackendTLSPolicyList) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.2. /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies

HTTP method
     `DELETE`
Description
     delete collection of BackendTLSPolicy 

Table 5.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind BackendTLSPolicy 

Table 5.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BackendTLSPolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-networking-gateway-v1-BackendTLSPolicyList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a BackendTLSPolicy 

Table 5.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema  |   
Show more

Table 5.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema   
201 - Created  |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema   
202 - Accepted  |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.3. /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies/{name}

Table 5.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the BackendTLSPolicy   
Show more

HTTP method
     `DELETE`
Description
     delete a BackendTLSPolicy 

Table 5.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified BackendTLSPolicy 

Table 5.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified BackendTLSPolicy 

Table 5.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified BackendTLSPolicy 

Table 5.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema  |   
Show more

Table 5.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema   
201 - Created  |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.4. /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/backendtlspolicies/{name}/status

Table 5.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the BackendTLSPolicy   
Show more

HTTP method
     `GET`
Description
     read status of the specified BackendTLSPolicy 

Table 5.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified BackendTLSPolicy 

Table 5.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified BackendTLSPolicy 

Table 5.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema  |   
Show more

Table 5.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema   
201 - Created  |  [`BackendTLSPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/backendtlspolicy-gateway-networking-k8s-io-v1 "Chapter 5. BackendTLSPolicy \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
