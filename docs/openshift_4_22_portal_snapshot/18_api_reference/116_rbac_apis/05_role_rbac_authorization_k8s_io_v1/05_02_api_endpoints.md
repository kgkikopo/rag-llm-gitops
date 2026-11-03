# 5.2. API endpoints

The following API endpoints are available: 

  * `/apis/rbac.authorization.k8s.io/v1/roles`

    * `GET`: list or watch objects of kind Role 

  * `/apis/rbac.authorization.k8s.io/v1/watch/roles`

    * `GET`: watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles`

    * `DELETE`: delete collection of Role 
    * `GET`: list or watch objects of kind Role 
    * `POST`: create a Role 

  * `/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles`

    * `GET`: watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles/{name}`

    * `DELETE`: delete a Role 
    * `GET`: read the specified Role 
    * `PATCH`: partially update the specified Role 
    * `PUT`: replace the specified Role 

  * `/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles/{name}`

    * `GET`: watch changes to an object of kind Role. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 5.2.1. /apis/rbac.authorization.k8s.io/v1/roles

HTTP method
     `GET`
Description
     list or watch objects of kind Role 

Table 5.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RoleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-RoleList) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.2. /apis/rbac.authorization.k8s.io/v1/watch/roles

HTTP method
     `GET`
Description
     watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead. 

Table 5.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.3. /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles

HTTP method
     `DELETE`
Description
     delete collection of Role 

Table 5.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Role 

Table 5.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`RoleList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-rbac-v1-RoleList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Role 

Table 5.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Role`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/role-rbac-authorization-k8s-io-v1 "Chapter 5. Role \[rbac.authorization.k8s.io/v1\]") schema  |   
Show more

Table 5.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Role`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/role-rbac-authorization-k8s-io-v1 "Chapter 5. Role \[rbac.authorization.k8s.io/v1\]") schema   
201 - Created  |  [`Role`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/role-rbac-authorization-k8s-io-v1 "Chapter 5. Role \[rbac.authorization.k8s.io/v1\]") schema   
202 - Accepted  |  [`Role`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/role-rbac-authorization-k8s-io-v1 "Chapter 5. Role \[rbac.authorization.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.4. /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles

HTTP method
     `GET`
Description
     watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead. 

Table 5.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.5. /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles/{name}

Table 5.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Role   
Show more

HTTP method
     `DELETE`
Description
     delete a Role 

Table 5.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Role 

Table 5.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Role`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/role-rbac-authorization-k8s-io-v1 "Chapter 5. Role \[rbac.authorization.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Role 

Table 5.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Role`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/role-rbac-authorization-k8s-io-v1 "Chapter 5. Role \[rbac.authorization.k8s.io/v1\]") schema   
201 - Created  |  [`Role`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/role-rbac-authorization-k8s-io-v1 "Chapter 5. Role \[rbac.authorization.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Role 

Table 5.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Role`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/role-rbac-authorization-k8s-io-v1 "Chapter 5. Role \[rbac.authorization.k8s.io/v1\]") schema  |   
Show more

Table 5.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Role`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/role-rbac-authorization-k8s-io-v1 "Chapter 5. Role \[rbac.authorization.k8s.io/v1\]") schema   
201 - Created  |  [`Role`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/rbac_apis/role-rbac-authorization-k8s-io-v1 "Chapter 5. Role \[rbac.authorization.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.6. /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles/{name}

Table 5.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Role   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Role. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 5.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
