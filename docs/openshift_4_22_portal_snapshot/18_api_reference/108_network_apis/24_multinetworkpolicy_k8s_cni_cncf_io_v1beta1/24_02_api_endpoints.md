# 24.2. API endpoints

The following API endpoints are available: 

  * `/apis/k8s.cni.cncf.io/v1beta1/multi-networkpolicies`

    * `GET`: list objects of kind MultiNetworkPolicy 

  * `/apis/k8s.cni.cncf.io/v1beta1/namespaces/{namespace}/multi-networkpolicies`

    * `DELETE`: delete collection of MultiNetworkPolicy 
    * `GET`: list objects of kind MultiNetworkPolicy 
    * `POST`: create a MultiNetworkPolicy 

  * `/apis/k8s.cni.cncf.io/v1beta1/namespaces/{namespace}/multi-networkpolicies/{name}`

    * `DELETE`: delete a MultiNetworkPolicy 
    * `GET`: read the specified MultiNetworkPolicy 
    * `PATCH`: partially update the specified MultiNetworkPolicy 
    * `PUT`: replace the specified MultiNetworkPolicy 




## 24.2.1. /apis/k8s.cni.cncf.io/v1beta1/multi-networkpolicies

HTTP method
     `GET`
Description
     list objects of kind MultiNetworkPolicy 

Table 24.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MultiNetworkPolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-cncf-cni-k8s-v1beta1-MultiNetworkPolicyList) schema   
401 - Unauthorized  |  Empty   
Show more

## 24.2.2. /apis/k8s.cni.cncf.io/v1beta1/namespaces/{namespace}/multi-networkpolicies

HTTP method
     `DELETE`
Description
     delete collection of MultiNetworkPolicy 

Table 24.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind MultiNetworkPolicy 

Table 24.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MultiNetworkPolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-cncf-cni-k8s-v1beta1-MultiNetworkPolicyList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a MultiNetworkPolicy 

Table 24.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 24.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`MultiNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/multinetworkpolicy-k8s-cni-cncf-io-v1beta1 "Chapter 24. MultiNetworkPolicy \[k8s.cni.cncf.io/v1beta1\]") schema  |   
Show more

Table 24.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MultiNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/multinetworkpolicy-k8s-cni-cncf-io-v1beta1 "Chapter 24. MultiNetworkPolicy \[k8s.cni.cncf.io/v1beta1\]") schema   
201 - Created  |  [`MultiNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/multinetworkpolicy-k8s-cni-cncf-io-v1beta1 "Chapter 24. MultiNetworkPolicy \[k8s.cni.cncf.io/v1beta1\]") schema   
202 - Accepted  |  [`MultiNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/multinetworkpolicy-k8s-cni-cncf-io-v1beta1 "Chapter 24. MultiNetworkPolicy \[k8s.cni.cncf.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 24.2.3. /apis/k8s.cni.cncf.io/v1beta1/namespaces/{namespace}/multi-networkpolicies/{name}

Table 24.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the MultiNetworkPolicy   
Show more

HTTP method
     `DELETE`
Description
     delete a MultiNetworkPolicy 

Table 24.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 24.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified MultiNetworkPolicy 

Table 24.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MultiNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/multinetworkpolicy-k8s-cni-cncf-io-v1beta1 "Chapter 24. MultiNetworkPolicy \[k8s.cni.cncf.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified MultiNetworkPolicy 

Table 24.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 24.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MultiNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/multinetworkpolicy-k8s-cni-cncf-io-v1beta1 "Chapter 24. MultiNetworkPolicy \[k8s.cni.cncf.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified MultiNetworkPolicy 

Table 24.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 24.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`MultiNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/multinetworkpolicy-k8s-cni-cncf-io-v1beta1 "Chapter 24. MultiNetworkPolicy \[k8s.cni.cncf.io/v1beta1\]") schema  |   
Show more

Table 24.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`MultiNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/multinetworkpolicy-k8s-cni-cncf-io-v1beta1 "Chapter 24. MultiNetworkPolicy \[k8s.cni.cncf.io/v1beta1\]") schema   
201 - Created  |  [`MultiNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/multinetworkpolicy-k8s-cni-cncf-io-v1beta1 "Chapter 24. MultiNetworkPolicy \[k8s.cni.cncf.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more
