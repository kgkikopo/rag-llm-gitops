# 9.2. API endpoints

The following API endpoints are available: 

  * `/apis/security.openshift.io/v1/securitycontextconstraints`

    * `DELETE`: delete collection of SecurityContextConstraints 
    * `GET`: list objects of kind SecurityContextConstraints 
    * `POST`: create SecurityContextConstraints 

  * `/apis/security.openshift.io/v1/watch/securitycontextconstraints`

    * `GET`: watch individual changes to a list of SecurityContextConstraints. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/security.openshift.io/v1/securitycontextconstraints/{name}`

    * `DELETE`: delete SecurityContextConstraints 
    * `GET`: read the specified SecurityContextConstraints 
    * `PATCH`: partially update the specified SecurityContextConstraints 
    * `PUT`: replace the specified SecurityContextConstraints 

  * `/apis/security.openshift.io/v1/watch/securitycontextconstraints/{name}`

    * `GET`: watch changes to an object of kind SecurityContextConstraints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 9.2.1. /apis/security.openshift.io/v1/securitycontextconstraints

HTTP method
     `DELETE`
Description
     delete collection of SecurityContextConstraints 

Table 9.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind SecurityContextConstraints 

Table 9.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SecurityContextConstraintsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-security-v1-SecurityContextConstraintsList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create SecurityContextConstraints 

Table 9.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 9.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`SecurityContextConstraints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/securitycontextconstraints-security-openshift-io-v1 "Chapter 9. SecurityContextConstraints \[security.openshift.io/v1\]") schema  |   
Show more

Table 9.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SecurityContextConstraints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/securitycontextconstraints-security-openshift-io-v1 "Chapter 9. SecurityContextConstraints \[security.openshift.io/v1\]") schema   
201 - Created  |  [`SecurityContextConstraints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/securitycontextconstraints-security-openshift-io-v1 "Chapter 9. SecurityContextConstraints \[security.openshift.io/v1\]") schema   
202 - Accepted  |  [`SecurityContextConstraints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/securitycontextconstraints-security-openshift-io-v1 "Chapter 9. SecurityContextConstraints \[security.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 9.2.2. /apis/security.openshift.io/v1/watch/securitycontextconstraints

HTTP method
     `GET`
Description
     watch individual changes to a list of SecurityContextConstraints. deprecated: use the 'watch' parameter with a list operation instead. 

Table 9.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 9.2.3. /apis/security.openshift.io/v1/securitycontextconstraints/{name}

Table 9.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the SecurityContextConstraints   
Show more

HTTP method
     `DELETE`
Description
     delete SecurityContextConstraints 

Table 9.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 9.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified SecurityContextConstraints 

Table 9.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SecurityContextConstraints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/securitycontextconstraints-security-openshift-io-v1 "Chapter 9. SecurityContextConstraints \[security.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified SecurityContextConstraints 

Table 9.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 9.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SecurityContextConstraints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/securitycontextconstraints-security-openshift-io-v1 "Chapter 9. SecurityContextConstraints \[security.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified SecurityContextConstraints 

Table 9.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 9.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`SecurityContextConstraints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/securitycontextconstraints-security-openshift-io-v1 "Chapter 9. SecurityContextConstraints \[security.openshift.io/v1\]") schema  |   
Show more

Table 9.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SecurityContextConstraints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/securitycontextconstraints-security-openshift-io-v1 "Chapter 9. SecurityContextConstraints \[security.openshift.io/v1\]") schema   
201 - Created  |  [`SecurityContextConstraints`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/securitycontextconstraints-security-openshift-io-v1 "Chapter 9. SecurityContextConstraints \[security.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 9.2.4. /apis/security.openshift.io/v1/watch/securitycontextconstraints/{name}

Table 9.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the SecurityContextConstraints   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind SecurityContextConstraints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 9.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
