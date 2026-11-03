# 23.2. API endpoints

The following API endpoints are available: 

  * `/apis/whereabouts.cni.cncf.io/v1alpha1/ippools`

    * `GET`: list objects of kind IPPool 

  * `/apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/ippools`

    * `DELETE`: delete collection of IPPool 
    * `GET`: list objects of kind IPPool 
    * `POST`: create an IPPool 

  * `/apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/ippools/{name}`

    * `DELETE`: delete an IPPool 
    * `GET`: read the specified IPPool 
    * `PATCH`: partially update the specified IPPool 
    * `PUT`: replace the specified IPPool 




## 23.2.1. /apis/whereabouts.cni.cncf.io/v1alpha1/ippools

HTTP method
     `GET`
Description
     list objects of kind IPPool 

Table 23.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPPoolList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-cncf-cni-whereabouts-v1alpha1-IPPoolList) schema   
401 - Unauthorized  |  Empty   
Show more

## 23.2.2. /apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/ippools

HTTP method
     `DELETE`
Description
     delete collection of IPPool 

Table 23.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind IPPool 

Table 23.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPPoolList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-cncf-cni-whereabouts-v1alpha1-IPPoolList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an IPPool 

Table 23.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 23.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`IPPool`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ippool-whereabouts-cni-cncf-io-v1alpha1 "Chapter 23. IPPool \[whereabouts.cni.cncf.io/v1alpha1\]") schema  |   
Show more

Table 23.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPPool`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ippool-whereabouts-cni-cncf-io-v1alpha1 "Chapter 23. IPPool \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
201 - Created  |  [`IPPool`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ippool-whereabouts-cni-cncf-io-v1alpha1 "Chapter 23. IPPool \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
202 - Accepted  |  [`IPPool`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ippool-whereabouts-cni-cncf-io-v1alpha1 "Chapter 23. IPPool \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 23.2.3. /apis/whereabouts.cni.cncf.io/v1alpha1/namespaces/{namespace}/ippools/{name}

Table 23.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the IPPool   
Show more

HTTP method
     `DELETE`
Description
     delete an IPPool 

Table 23.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 23.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified IPPool 

Table 23.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPPool`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ippool-whereabouts-cni-cncf-io-v1alpha1 "Chapter 23. IPPool \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified IPPool 

Table 23.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 23.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPPool`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ippool-whereabouts-cni-cncf-io-v1alpha1 "Chapter 23. IPPool \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified IPPool 

Table 23.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 23.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`IPPool`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ippool-whereabouts-cni-cncf-io-v1alpha1 "Chapter 23. IPPool \[whereabouts.cni.cncf.io/v1alpha1\]") schema  |   
Show more

Table 23.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IPPool`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ippool-whereabouts-cni-cncf-io-v1alpha1 "Chapter 23. IPPool \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
201 - Created  |  [`IPPool`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/ippool-whereabouts-cni-cncf-io-v1alpha1 "Chapter 23. IPPool \[whereabouts.cni.cncf.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
