# 25.2. API endpoints

The following API endpoints are available: 

  * `/apis/k8s.cni.cncf.io/v1/network-attachment-definitions`

    * `GET`: list objects of kind NetworkAttachmentDefinition 

  * `/apis/k8s.cni.cncf.io/v1/namespaces/{namespace}/network-attachment-definitions`

    * `DELETE`: delete collection of NetworkAttachmentDefinition 
    * `GET`: list objects of kind NetworkAttachmentDefinition 
    * `POST`: create a NetworkAttachmentDefinition 

  * `/apis/k8s.cni.cncf.io/v1/namespaces/{namespace}/network-attachment-definitions/{name}`

    * `DELETE`: delete a NetworkAttachmentDefinition 
    * `GET`: read the specified NetworkAttachmentDefinition 
    * `PATCH`: partially update the specified NetworkAttachmentDefinition 
    * `PUT`: replace the specified NetworkAttachmentDefinition 




## 25.2.1. /apis/k8s.cni.cncf.io/v1/network-attachment-definitions

HTTP method
     `GET`
Description
     list objects of kind NetworkAttachmentDefinition 

Table 25.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkAttachmentDefinitionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-cncf-cni-k8s-v1-NetworkAttachmentDefinitionList) schema   
401 - Unauthorized  |  Empty   
Show more

## 25.2.2. /apis/k8s.cni.cncf.io/v1/namespaces/{namespace}/network-attachment-definitions

HTTP method
     `DELETE`
Description
     delete collection of NetworkAttachmentDefinition 

Table 25.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind NetworkAttachmentDefinition 

Table 25.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkAttachmentDefinitionList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-cncf-cni-k8s-v1-NetworkAttachmentDefinitionList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a NetworkAttachmentDefinition 

Table 25.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 25.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`NetworkAttachmentDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkattachmentdefinition-k8s-cni-cncf-io-v1 "Chapter 25. NetworkAttachmentDefinition \[k8s.cni.cncf.io/v1\]") schema  |   
Show more

Table 25.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkAttachmentDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkattachmentdefinition-k8s-cni-cncf-io-v1 "Chapter 25. NetworkAttachmentDefinition \[k8s.cni.cncf.io/v1\]") schema   
201 - Created  |  [`NetworkAttachmentDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkattachmentdefinition-k8s-cni-cncf-io-v1 "Chapter 25. NetworkAttachmentDefinition \[k8s.cni.cncf.io/v1\]") schema   
202 - Accepted  |  [`NetworkAttachmentDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkattachmentdefinition-k8s-cni-cncf-io-v1 "Chapter 25. NetworkAttachmentDefinition \[k8s.cni.cncf.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 25.2.3. /apis/k8s.cni.cncf.io/v1/namespaces/{namespace}/network-attachment-definitions/{name}

Table 25.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the NetworkAttachmentDefinition   
Show more

HTTP method
     `DELETE`
Description
     delete a NetworkAttachmentDefinition 

Table 25.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 25.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified NetworkAttachmentDefinition 

Table 25.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkAttachmentDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkattachmentdefinition-k8s-cni-cncf-io-v1 "Chapter 25. NetworkAttachmentDefinition \[k8s.cni.cncf.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified NetworkAttachmentDefinition 

Table 25.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 25.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkAttachmentDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkattachmentdefinition-k8s-cni-cncf-io-v1 "Chapter 25. NetworkAttachmentDefinition \[k8s.cni.cncf.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified NetworkAttachmentDefinition 

Table 25.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 25.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`NetworkAttachmentDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkattachmentdefinition-k8s-cni-cncf-io-v1 "Chapter 25. NetworkAttachmentDefinition \[k8s.cni.cncf.io/v1\]") schema  |   
Show more

Table 25.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NetworkAttachmentDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkattachmentdefinition-k8s-cni-cncf-io-v1 "Chapter 25. NetworkAttachmentDefinition \[k8s.cni.cncf.io/v1\]") schema   
201 - Created  |  [`NetworkAttachmentDefinition`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/networkattachmentdefinition-k8s-cni-cncf-io-v1 "Chapter 25. NetworkAttachmentDefinition \[k8s.cni.cncf.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
