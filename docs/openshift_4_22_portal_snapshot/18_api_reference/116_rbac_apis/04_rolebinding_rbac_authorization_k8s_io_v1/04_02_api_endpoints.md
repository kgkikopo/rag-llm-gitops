# 4.2. API endpoints

The following API endpoints are available: 

  * `/apis/rbac.authorization.k8s.io/v1/rolebindings`

    * `GET`: list or watch objects of kind RoleBinding 

  * `/apis/rbac.authorization.k8s.io/v1/watch/rolebindings`

    * `GET`: watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings`

    * `DELETE`: delete collection of RoleBinding 
    * `GET`: list or watch objects of kind RoleBinding 
    * `POST`: create a RoleBinding 

  * `/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings`

    * `GET`: watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings/{name}`

    * `DELETE`: delete a RoleBinding 
    * `GET`: read the specified RoleBinding 
    * `PATCH`: partially update the specified RoleBinding 
    * `PUT`: replace the specified RoleBinding 

  * `/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings/{name}`

    * `GET`: watch changes to an object of kind RoleBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 4.2.1. /apis/rbac.authorization.k8s.io/v1/rolebindings

HTTP method
     `GET`
Description
     list or watch objects of kind RoleBinding 

Table 4.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RoleBindingList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-RoleBindingList) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.2. /apis/rbac.authorization.k8s.io/v1/watch/rolebindings

HTTP method
     `GET`
Description
     watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead. 

Table 4.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.3. /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings

HTTP method
     `DELETE`
Description
     delete collection of RoleBinding 

Table 4.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind RoleBinding 

Table 4.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RoleBindingList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-RoleBindingList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a RoleBinding 

Table 4.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`RoleBinding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding \[rbac.authorization.k8s.io/v1\]") schema  |   
Show more

Table 4.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RoleBinding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding \[rbac.authorization.k8s.io/v1\]") schema   
201 - Created  |  [`RoleBinding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding \[rbac.authorization.k8s.io/v1\]") schema   
202 - Accepted  |  [`RoleBinding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding \[rbac.authorization.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.4. /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings

HTTP method
     `GET`
Description
     watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead. 

Table 4.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.5. /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings/{name}

Table 4.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the RoleBinding   
Show more

HTTP method
     `DELETE`
Description
     delete a RoleBinding 

Table 4.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified RoleBinding 

Table 4.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RoleBinding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding \[rbac.authorization.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified RoleBinding 

Table 4.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RoleBinding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding \[rbac.authorization.k8s.io/v1\]") schema   
201 - Created  |  [`RoleBinding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding \[rbac.authorization.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified RoleBinding 

Table 4.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`RoleBinding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding \[rbac.authorization.k8s.io/v1\]") schema  |   
Show more

Table 4.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RoleBinding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding \[rbac.authorization.k8s.io/v1\]") schema   
201 - Created  |  [`RoleBinding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/rolebinding-rbac-authorization-k8s-io-v1 "Chapter 4. RoleBinding \[rbac.authorization.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.6. /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings/{name}

Table 4.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the RoleBinding   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind RoleBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 4.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
