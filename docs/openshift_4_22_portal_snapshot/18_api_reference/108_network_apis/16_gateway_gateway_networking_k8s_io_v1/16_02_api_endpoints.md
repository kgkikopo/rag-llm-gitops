# 16.2. API endpoints

The following API endpoints are available: 

  * `/apis/gateway.networking.k8s.io/v1/gateways`

    * `GET`: list objects of kind Gateway 

  * `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/gateways`

    * `DELETE`: delete collection of Gateway 
    * `GET`: list objects of kind Gateway 
    * `POST`: create a Gateway 

  * `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/gateways/{name}`

    * `DELETE`: delete a Gateway 
    * `GET`: read the specified Gateway 
    * `PATCH`: partially update the specified Gateway 
    * `PUT`: replace the specified Gateway 

  * `/apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/gateways/{name}/status`

    * `GET`: read status of the specified Gateway 
    * `PATCH`: partially update status of the specified Gateway 
    * `PUT`: replace status of the specified Gateway 




## 16.2.1. /apis/gateway.networking.k8s.io/v1/gateways

HTTP method
     `GET`
Description
     list objects of kind Gateway 

Table 16.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`GatewayList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-networking-gateway-v1-GatewayList) schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.2. /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/gateways

HTTP method
     `DELETE`
Description
     delete collection of Gateway 

Table 16.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind Gateway 

Table 16.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`GatewayList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-networking-gateway-v1-GatewayList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Gateway 

Table 16.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema  |   
Show more

Table 16.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema   
201 - Created  |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema   
202 - Accepted  |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.3. /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/gateways/{name}

Table 16.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Gateway   
Show more

HTTP method
     `DELETE`
Description
     delete a Gateway 

Table 16.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 16.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Gateway 

Table 16.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Gateway 

Table 16.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Gateway 

Table 16.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema  |   
Show more

Table 16.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema   
201 - Created  |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 16.2.4. /apis/gateway.networking.k8s.io/v1/namespaces/{namespace}/gateways/{name}/status

Table 16.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Gateway   
Show more

HTTP method
     `GET`
Description
     read status of the specified Gateway 

Table 16.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Gateway 

Table 16.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Gateway 

Table 16.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 16.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema  |   
Show more

Table 16.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema   
201 - Created  |  [`Gateway`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gateway-gateway-networking-k8s-io-v1 "Chapter 16. Gateway \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
