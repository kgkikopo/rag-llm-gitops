# 11.2. API endpoints

The following API endpoints are available: 

  * `/apis/k8s.ovn.org/v1/egressservices`

    * `GET`: list objects of kind EgressService 

  * `/apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices`

    * `DELETE`: delete collection of EgressService 
    * `GET`: list objects of kind EgressService 
    * `POST`: create an EgressService 

  * `/apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices/{name}`

    * `DELETE`: delete an EgressService 
    * `GET`: read the specified EgressService 
    * `PATCH`: partially update the specified EgressService 
    * `PUT`: replace the specified EgressService 

  * `/apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices/{name}/status`

    * `GET`: read status of the specified EgressService 
    * `PATCH`: partially update status of the specified EgressService 
    * `PUT`: replace status of the specified EgressService 




## 11.2.1. /apis/k8s.ovn.org/v1/egressservices

HTTP method
     `GET`
Description
     list objects of kind EgressService 

Table 11.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EgressServiceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#org-ovn-k8s-v1-EgressServiceList) schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.2. /apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices

HTTP method
     `DELETE`
Description
     delete collection of EgressService 

Table 11.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind EgressService 

Table 11.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EgressServiceList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#org-ovn-k8s-v1-EgressServiceList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an EgressService 

Table 11.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema  |   
Show more

Table 11.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema   
201 - Created  |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema   
202 - Accepted  |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.3. /apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices/{name}

Table 11.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the EgressService   
Show more

HTTP method
     `DELETE`
Description
     delete an EgressService 

Table 11.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 11.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified EgressService 

Table 11.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified EgressService 

Table 11.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified EgressService 

Table 11.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema  |   
Show more

Table 11.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema   
201 - Created  |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.4. /apis/k8s.ovn.org/v1/namespaces/{namespace}/egressservices/{name}/status

Table 11.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the EgressService   
Show more

HTTP method
     `GET`
Description
     read status of the specified EgressService 

Table 11.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified EgressService 

Table 11.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified EgressService 

Table 11.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema  |   
Show more

Table 11.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema   
201 - Created  |  [`EgressService`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/egressservice-k8s-ovn-org-v1 "Chapter 11. EgressService \[k8s.ovn.org/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
