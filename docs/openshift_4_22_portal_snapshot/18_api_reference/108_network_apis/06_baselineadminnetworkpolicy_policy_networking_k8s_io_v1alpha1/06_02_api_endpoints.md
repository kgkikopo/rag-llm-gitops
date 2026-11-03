# 6.2. API endpoints

The following API endpoints are available: 

  * `/apis/policy.networking.k8s.io/v1alpha1/baselineadminnetworkpolicies`

    * `DELETE`: delete collection of BaselineAdminNetworkPolicy 
    * `GET`: list objects of kind BaselineAdminNetworkPolicy 
    * `POST`: create a BaselineAdminNetworkPolicy 

  * `/apis/policy.networking.k8s.io/v1alpha1/baselineadminnetworkpolicies/{name}`

    * `DELETE`: delete a BaselineAdminNetworkPolicy 
    * `GET`: read the specified BaselineAdminNetworkPolicy 
    * `PATCH`: partially update the specified BaselineAdminNetworkPolicy 
    * `PUT`: replace the specified BaselineAdminNetworkPolicy 

  * `/apis/policy.networking.k8s.io/v1alpha1/baselineadminnetworkpolicies/{name}/status`

    * `GET`: read status of the specified BaselineAdminNetworkPolicy 
    * `PATCH`: partially update status of the specified BaselineAdminNetworkPolicy 
    * `PUT`: replace status of the specified BaselineAdminNetworkPolicy 




## 6.2.1. /apis/policy.networking.k8s.io/v1alpha1/baselineadminnetworkpolicies

HTTP method
     `DELETE`
Description
     delete collection of BaselineAdminNetworkPolicy 

Table 6.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind BaselineAdminNetworkPolicy 

Table 6.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BaselineAdminNetworkPolicyList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-networking-policy-v1alpha1-BaselineAdminNetworkPolicyList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a BaselineAdminNetworkPolicy 

Table 6.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema  |   
Show more

Table 6.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema   
201 - Created  |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema   
202 - Accepted  |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.2. /apis/policy.networking.k8s.io/v1alpha1/baselineadminnetworkpolicies/{name}

Table 6.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the BaselineAdminNetworkPolicy   
Show more

HTTP method
     `DELETE`
Description
     delete a BaselineAdminNetworkPolicy 

Table 6.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 6.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified BaselineAdminNetworkPolicy 

Table 6.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified BaselineAdminNetworkPolicy 

Table 6.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified BaselineAdminNetworkPolicy 

Table 6.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema  |   
Show more

Table 6.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema   
201 - Created  |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.3. /apis/policy.networking.k8s.io/v1alpha1/baselineadminnetworkpolicies/{name}/status

Table 6.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the BaselineAdminNetworkPolicy   
Show more

HTTP method
     `GET`
Description
     read status of the specified BaselineAdminNetworkPolicy 

Table 6.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified BaselineAdminNetworkPolicy 

Table 6.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified BaselineAdminNetworkPolicy 

Table 6.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 6.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema  |   
Show more

Table 6.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema   
201 - Created  |  [`BaselineAdminNetworkPolicy`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1 "Chapter 6. BaselineAdminNetworkPolicy \[policy.networking.k8s.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
