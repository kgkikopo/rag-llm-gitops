# 26.2. API endpoints

The following API endpoints are available: 

  * `/apis/networking.k8s.io/v1/networkpolicies`

    * `GET`: list or watch objects of kind NetworkPolicy 

  * `/apis/networking.k8s.io/v1/watch/networkpolicies`

    * `GET`: watch individual changes to a list of NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies`

    * `DELETE`: delete collection of NetworkPolicy 
    * `GET`: list or watch objects of kind NetworkPolicy 
    * `POST`: create a NetworkPolicy 

  * `/apis/networking.k8s.io/v1/watch/namespaces/{namespace}/networkpolicies`

    * `GET`: watch individual changes to a list of NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies/{name}`

    * `DELETE`: delete a NetworkPolicy 
    * `GET`: read the specified NetworkPolicy 
    * `PATCH`: partially update the specified NetworkPolicy 
    * `PUT`: replace the specified NetworkPolicy 

  * `/apis/networking.k8s.io/v1/watch/namespaces/{namespace}/networkpolicies/{name}`

    * `GET`: watch changes to an object of kind NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 26.2.1. /apis/networking.k8s.io/v1/networkpolicies

HTTP method
     `GET`
Description
     list or watch objects of kind NetworkPolicy 

Table 26.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkPolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-networking-v1-NetworkPolicyList) schema   
401 - Unauthorized  |  Empty   
Show more

## 26.2.2. /apis/networking.k8s.io/v1/watch/networkpolicies

HTTP method
     `GET`
Description
     watch individual changes to a list of NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead. 

Table 26.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 26.2.3. /apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies

HTTP method
     `DELETE`
Description
     delete collection of NetworkPolicy 

Table 26.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 26.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind NetworkPolicy 

Table 26.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkPolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-networking-v1-NetworkPolicyList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a NetworkPolicy 

Table 26.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 26.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`NetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkpolicy-networking-k8s-io-v1 "Chapter 26. NetworkPolicy \[networking.k8s.io/v1\]") schema  |   
Show more

Table 26.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkpolicy-networking-k8s-io-v1 "Chapter 26. NetworkPolicy \[networking.k8s.io/v1\]") schema   
201 - Created  |  [`NetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkpolicy-networking-k8s-io-v1 "Chapter 26. NetworkPolicy \[networking.k8s.io/v1\]") schema   
202 - Accepted  |  [`NetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkpolicy-networking-k8s-io-v1 "Chapter 26. NetworkPolicy \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 26.2.4. /apis/networking.k8s.io/v1/watch/namespaces/{namespace}/networkpolicies

HTTP method
     `GET`
Description
     watch individual changes to a list of NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead. 

Table 26.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 26.2.5. /apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies/{name}

Table 26.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the NetworkPolicy   
Show more

HTTP method
     `DELETE`
Description
     delete a NetworkPolicy 

Table 26.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 26.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified NetworkPolicy 

Table 26.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkpolicy-networking-k8s-io-v1 "Chapter 26. NetworkPolicy \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified NetworkPolicy 

Table 26.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 26.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkpolicy-networking-k8s-io-v1 "Chapter 26. NetworkPolicy \[networking.k8s.io/v1\]") schema   
201 - Created  |  [`NetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkpolicy-networking-k8s-io-v1 "Chapter 26. NetworkPolicy \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified NetworkPolicy 

Table 26.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 26.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`NetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkpolicy-networking-k8s-io-v1 "Chapter 26. NetworkPolicy \[networking.k8s.io/v1\]") schema  |   
Show more

Table 26.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkpolicy-networking-k8s-io-v1 "Chapter 26. NetworkPolicy \[networking.k8s.io/v1\]") schema   
201 - Created  |  [`NetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkpolicy-networking-k8s-io-v1 "Chapter 26. NetworkPolicy \[networking.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 26.2.6. /apis/networking.k8s.io/v1/watch/namespaces/{namespace}/networkpolicies/{name}

Table 26.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the NetworkPolicy   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 26.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
