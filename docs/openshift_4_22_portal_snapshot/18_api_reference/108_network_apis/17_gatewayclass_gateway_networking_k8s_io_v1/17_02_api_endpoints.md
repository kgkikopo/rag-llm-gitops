# 17.2. API endpoints

The following API endpoints are available: 

  * `/apis/gateway.networking.k8s.io/v1/gatewayclasses`

    * `DELETE`: delete collection of GatewayClass 
    * `GET`: list objects of kind GatewayClass 
    * `POST`: create a GatewayClass 

  * `/apis/gateway.networking.k8s.io/v1/gatewayclasses/{name}`

    * `DELETE`: delete a GatewayClass 
    * `GET`: read the specified GatewayClass 
    * `PATCH`: partially update the specified GatewayClass 
    * `PUT`: replace the specified GatewayClass 

  * `/apis/gateway.networking.k8s.io/v1/gatewayclasses/{name}/status`

    * `GET`: read status of the specified GatewayClass 
    * `PATCH`: partially update status of the specified GatewayClass 
    * `PUT`: replace status of the specified GatewayClass 




## 17.2.1. /apis/gateway.networking.k8s.io/v1/gatewayclasses

HTTP method
     `DELETE`
Description
     delete collection of GatewayClass 

Table 17.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind GatewayClass 

Table 17.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`GatewayClassList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-networking-gateway-v1-GatewayClassList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a GatewayClass 

Table 17.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 17.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema  |   
Show more

Table 17.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema   
201 - Created  |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema   
202 - Accepted  |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 17.2.2. /apis/gateway.networking.k8s.io/v1/gatewayclasses/{name}

Table 17.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the GatewayClass   
Show more

HTTP method
     `DELETE`
Description
     delete a GatewayClass 

Table 17.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 17.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified GatewayClass 

Table 17.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified GatewayClass 

Table 17.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 17.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified GatewayClass 

Table 17.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 17.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema  |   
Show more

Table 17.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema   
201 - Created  |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 17.2.3. /apis/gateway.networking.k8s.io/v1/gatewayclasses/{name}/status

Table 17.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the GatewayClass   
Show more

HTTP method
     `GET`
Description
     read status of the specified GatewayClass 

Table 17.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified GatewayClass 

Table 17.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 17.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified GatewayClass 

Table 17.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 17.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema  |   
Show more

Table 17.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema   
201 - Created  |  [`GatewayClass`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/gatewayclass-gateway-networking-k8s-io-v1 "Chapter 17. GatewayClass \[gateway.networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
