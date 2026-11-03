# 21.2. API endpoints

The following API endpoints are available: 

  * `/apis/networking.k8s.io/v1/ipaddresses`

    * `DELETE`: delete collection of IPAddress 
    * `GET`: list or watch objects of kind IPAddress 
    * `POST`: create an IPAddress 

  * `/apis/networking.k8s.io/v1/watch/ipaddresses`

    * `GET`: watch individual changes to a list of IPAddress. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/networking.k8s.io/v1/ipaddresses/{name}`

    * `DELETE`: delete an IPAddress 
    * `GET`: read the specified IPAddress 
    * `PATCH`: partially update the specified IPAddress 
    * `PUT`: replace the specified IPAddress 

  * `/apis/networking.k8s.io/v1/watch/ipaddresses/{name}`

    * `GET`: watch changes to an object of kind IPAddress. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 21.2.1. /apis/networking.k8s.io/v1/ipaddresses

HTTP method
     `DELETE`
Description
     delete collection of IPAddress 

Table 21.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 21.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind IPAddress 

Table 21.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAddressList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-networking-v1-IPAddressList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an IPAddress 

Table 21.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 21.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`IPAddress`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipaddress-networking-k8s-io-v1 "Chapter 21. IPAddress \[networking.k8s.io/v1\]") schema  |   
Show more

Table 21.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAddress`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipaddress-networking-k8s-io-v1 "Chapter 21. IPAddress \[networking.k8s.io/v1\]") schema   
201 - Created  |  [`IPAddress`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipaddress-networking-k8s-io-v1 "Chapter 21. IPAddress \[networking.k8s.io/v1\]") schema   
202 - Accepted  |  [`IPAddress`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipaddress-networking-k8s-io-v1 "Chapter 21. IPAddress \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 21.2.2. /apis/networking.k8s.io/v1/watch/ipaddresses

HTTP method
     `GET`
Description
     watch individual changes to a list of IPAddress. deprecated: use the 'watch' parameter with a list operation instead. 

Table 21.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 21.2.3. /apis/networking.k8s.io/v1/ipaddresses/{name}

Table 21.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the IPAddress   
Show more

HTTP method
     `DELETE`
Description
     delete an IPAddress 

Table 21.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 21.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified IPAddress 

Table 21.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAddress`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipaddress-networking-k8s-io-v1 "Chapter 21. IPAddress \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified IPAddress 

Table 21.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 21.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAddress`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipaddress-networking-k8s-io-v1 "Chapter 21. IPAddress \[networking.k8s.io/v1\]") schema   
201 - Created  |  [`IPAddress`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipaddress-networking-k8s-io-v1 "Chapter 21. IPAddress \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified IPAddress 

Table 21.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 21.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`IPAddress`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipaddress-networking-k8s-io-v1 "Chapter 21. IPAddress \[networking.k8s.io/v1\]") schema  |   
Show more

Table 21.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAddress`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipaddress-networking-k8s-io-v1 "Chapter 21. IPAddress \[networking.k8s.io/v1\]") schema   
201 - Created  |  [`IPAddress`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipaddress-networking-k8s-io-v1 "Chapter 21. IPAddress \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 21.2.4. /apis/networking.k8s.io/v1/watch/ipaddresses/{name}

Table 21.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the IPAddress   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind IPAddress. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 21.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
