# 33.2. API endpoints

The following API endpoints are available: 

  * `/apis/networking.k8s.io/v1/servicecidrs`

    * `DELETE`: delete collection of ServiceCIDR 
    * `GET`: list or watch objects of kind ServiceCIDR 
    * `POST`: create a ServiceCIDR 

  * `/apis/networking.k8s.io/v1/watch/servicecidrs`

    * `GET`: watch individual changes to a list of ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/networking.k8s.io/v1/servicecidrs/{name}`

    * `DELETE`: delete a ServiceCIDR 
    * `GET`: read the specified ServiceCIDR 
    * `PATCH`: partially update the specified ServiceCIDR 
    * `PUT`: replace the specified ServiceCIDR 

  * `/apis/networking.k8s.io/v1/watch/servicecidrs/{name}`

    * `GET`: watch changes to an object of kind ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/networking.k8s.io/v1/servicecidrs/{name}/status`

    * `GET`: read status of the specified ServiceCIDR 
    * `PATCH`: partially update status of the specified ServiceCIDR 
    * `PUT`: replace status of the specified ServiceCIDR 




## 33.2.1. /apis/networking.k8s.io/v1/servicecidrs

HTTP method
     `DELETE`
Description
     delete collection of ServiceCIDR 

Table 33.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 33.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind ServiceCIDR 

Table 33.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceCIDRList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-networking-v1-ServiceCIDRList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a ServiceCIDR 

Table 33.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 33.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema  |   
Show more

Table 33.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
201 - Created  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
202 - Accepted  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 33.2.2. /apis/networking.k8s.io/v1/watch/servicecidrs

HTTP method
     `GET`
Description
     watch individual changes to a list of ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead. 

Table 33.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 33.2.3. /apis/networking.k8s.io/v1/servicecidrs/{name}

Table 33.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ServiceCIDR   
Show more

HTTP method
     `DELETE`
Description
     delete a ServiceCIDR 

Table 33.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 33.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ServiceCIDR 

Table 33.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ServiceCIDR 

Table 33.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 33.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
201 - Created  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ServiceCIDR 

Table 33.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 33.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema  |   
Show more

Table 33.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
201 - Created  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 33.2.4. /apis/networking.k8s.io/v1/watch/servicecidrs/{name}

Table 33.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ServiceCIDR   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 33.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 33.2.5. /apis/networking.k8s.io/v1/servicecidrs/{name}/status

Table 33.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ServiceCIDR   
Show more

HTTP method
     `GET`
Description
     read status of the specified ServiceCIDR 

Table 33.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ServiceCIDR 

Table 33.21. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 33.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
201 - Created  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ServiceCIDR 

Table 33.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 33.24. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema  |   
Show more

Table 33.25. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
201 - Created  |  [`ServiceCIDR`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/servicecidr-networking-k8s-io-v1 "Chapter 33. ServiceCIDR \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
