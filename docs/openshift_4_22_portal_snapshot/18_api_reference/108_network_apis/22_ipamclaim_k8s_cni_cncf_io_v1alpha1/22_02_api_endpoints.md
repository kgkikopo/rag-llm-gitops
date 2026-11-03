# 22.2. API endpoints

The following API endpoints are available: 

  * `/apis/k8s.cni.cncf.io/v1alpha1/ipamclaims`

    * `GET`: list objects of kind IPAMClaim 

  * `/apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims`

    * `DELETE`: delete collection of IPAMClaim 
    * `GET`: list objects of kind IPAMClaim 
    * `POST`: create an IPAMClaim 

  * `/apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims/{name}`

    * `DELETE`: delete an IPAMClaim 
    * `GET`: read the specified IPAMClaim 
    * `PATCH`: partially update the specified IPAMClaim 
    * `PUT`: replace the specified IPAMClaim 

  * `/apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims/{name}/status`

    * `GET`: read status of the specified IPAMClaim 
    * `PATCH`: partially update status of the specified IPAMClaim 
    * `PUT`: replace status of the specified IPAMClaim 




## 22.2.1. /apis/k8s.cni.cncf.io/v1alpha1/ipamclaims

HTTP method
     `GET`
Description
     list objects of kind IPAMClaim 

Table 22.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAMClaimList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-cncf-cni-k8s-v1alpha1-IPAMClaimList) schema   
401 - Unauthorized  |  Empty   
Show more

## 22.2.2. /apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims

HTTP method
     `DELETE`
Description
     delete collection of IPAMClaim 

Table 22.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind IPAMClaim 

Table 22.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAMClaimList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-cncf-cni-k8s-v1alpha1-IPAMClaimList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an IPAMClaim 

Table 22.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 22.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema  |   
Show more

Table 22.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema   
201 - Created  |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema   
202 - Accepted  |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 22.2.3. /apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims/{name}

Table 22.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the IPAMClaim   
Show more

HTTP method
     `DELETE`
Description
     delete an IPAMClaim 

Table 22.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 22.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified IPAMClaim 

Table 22.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified IPAMClaim 

Table 22.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 22.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified IPAMClaim 

Table 22.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 22.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema  |   
Show more

Table 22.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema   
201 - Created  |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 22.2.4. /apis/k8s.cni.cncf.io/v1alpha1/namespaces/{namespace}/ipamclaims/{name}/status

Table 22.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the IPAMClaim   
Show more

HTTP method
     `GET`
Description
     read status of the specified IPAMClaim 

Table 22.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified IPAMClaim 

Table 22.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 22.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified IPAMClaim 

Table 22.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 22.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema  |   
Show more

Table 22.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema   
201 - Created  |  [`IPAMClaim`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1 "Chapter 22. IPAMClaim \[k8s.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
