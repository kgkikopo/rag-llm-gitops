# 29.2. API endpoints

The following API endpoints are available: 

  * `/apis/controlplane.operator.openshift.io/v1alpha1/podnetworkconnectivitychecks`

    * `GET`: list objects of kind PodNetworkConnectivityCheck 

  * `/apis/controlplane.operator.openshift.io/v1alpha1/namespaces/{namespace}/podnetworkconnectivitychecks`

    * `DELETE`: delete collection of PodNetworkConnectivityCheck 
    * `GET`: list objects of kind PodNetworkConnectivityCheck 
    * `POST`: create a PodNetworkConnectivityCheck 

  * `/apis/controlplane.operator.openshift.io/v1alpha1/namespaces/{namespace}/podnetworkconnectivitychecks/{name}`

    * `DELETE`: delete a PodNetworkConnectivityCheck 
    * `GET`: read the specified PodNetworkConnectivityCheck 
    * `PATCH`: partially update the specified PodNetworkConnectivityCheck 
    * `PUT`: replace the specified PodNetworkConnectivityCheck 

  * `/apis/controlplane.operator.openshift.io/v1alpha1/namespaces/{namespace}/podnetworkconnectivitychecks/{name}/status`

    * `GET`: read status of the specified PodNetworkConnectivityCheck 
    * `PATCH`: partially update status of the specified PodNetworkConnectivityCheck 
    * `PUT`: replace status of the specified PodNetworkConnectivityCheck 




## 29.2.1. /apis/controlplane.operator.openshift.io/v1alpha1/podnetworkconnectivitychecks

HTTP method
     `GET`
Description
     list objects of kind PodNetworkConnectivityCheck 

Table 29.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodNetworkConnectivityCheckList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-operator-controlplane-v1alpha1-PodNetworkConnectivityCheckList) schema   
401 - Unauthorized  |  Empty   
Show more

## 29.2.2. /apis/controlplane.operator.openshift.io/v1alpha1/namespaces/{namespace}/podnetworkconnectivitychecks

HTTP method
     `DELETE`
Description
     delete collection of PodNetworkConnectivityCheck 

Table 29.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind PodNetworkConnectivityCheck 

Table 29.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodNetworkConnectivityCheckList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-operator-controlplane-v1alpha1-PodNetworkConnectivityCheckList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a PodNetworkConnectivityCheck 

Table 29.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 29.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema  |   
Show more

Table 29.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema   
201 - Created  |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema   
202 - Accepted  |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 29.2.3. /apis/controlplane.operator.openshift.io/v1alpha1/namespaces/{namespace}/podnetworkconnectivitychecks/{name}

Table 29.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PodNetworkConnectivityCheck   
Show more

HTTP method
     `DELETE`
Description
     delete a PodNetworkConnectivityCheck 

Table 29.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 29.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified PodNetworkConnectivityCheck 

Table 29.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified PodNetworkConnectivityCheck 

Table 29.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 29.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified PodNetworkConnectivityCheck 

Table 29.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 29.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema  |   
Show more

Table 29.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema   
201 - Created  |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 29.2.4. /apis/controlplane.operator.openshift.io/v1alpha1/namespaces/{namespace}/podnetworkconnectivitychecks/{name}/status

Table 29.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PodNetworkConnectivityCheck   
Show more

HTTP method
     `GET`
Description
     read status of the specified PodNetworkConnectivityCheck 

Table 29.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified PodNetworkConnectivityCheck 

Table 29.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 29.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified PodNetworkConnectivityCheck 

Table 29.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 29.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema  |   
Show more

Table 29.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema   
201 - Created  |  [`PodNetworkConnectivityCheck`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1 "Chapter 29. PodNetworkConnectivityCheck \[controlplane.operator.openshift.io/v1alpha1\]") schema   
401 - Unauthorized  |  Empty   
Show more
