# 3.2. API endpoints

The following API endpoints are available: 

  * `/apis/cloudcredential.openshift.io/v1/credentialsrequests`

    * `GET`: list objects of kind CredentialsRequest 

  * `/apis/cloudcredential.openshift.io/v1/namespaces/{namespace}/credentialsrequests`

    * `DELETE`: delete collection of CredentialsRequest 
    * `GET`: list objects of kind CredentialsRequest 
    * `POST`: create a CredentialsRequest 

  * `/apis/cloudcredential.openshift.io/v1/namespaces/{namespace}/credentialsrequests/{name}`

    * `DELETE`: delete a CredentialsRequest 
    * `GET`: read the specified CredentialsRequest 
    * `PATCH`: partially update the specified CredentialsRequest 
    * `PUT`: replace the specified CredentialsRequest 

  * `/apis/cloudcredential.openshift.io/v1/namespaces/{namespace}/credentialsrequests/{name}/status`

    * `GET`: read status of the specified CredentialsRequest 
    * `PATCH`: partially update status of the specified CredentialsRequest 
    * `PUT`: replace status of the specified CredentialsRequest 




## 3.2.1. /apis/cloudcredential.openshift.io/v1/credentialsrequests

HTTP method
     `GET`
Description
     list objects of kind CredentialsRequest 

Table 3.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CredentialsRequestList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-cloudcredential-v1-CredentialsRequestList) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.2. /apis/cloudcredential.openshift.io/v1/namespaces/{namespace}/credentialsrequests

HTTP method
     `DELETE`
Description
     delete collection of CredentialsRequest 

Table 3.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind CredentialsRequest 

Table 3.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CredentialsRequestList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-cloudcredential-v1-CredentialsRequestList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a CredentialsRequest 

Table 3.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema  |   
Show more

Table 3.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema   
201 - Created  |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema   
202 - Accepted  |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.3. /apis/cloudcredential.openshift.io/v1/namespaces/{namespace}/credentialsrequests/{name}

Table 3.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CredentialsRequest   
Show more

HTTP method
     `DELETE`
Description
     delete a CredentialsRequest 

Table 3.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified CredentialsRequest 

Table 3.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified CredentialsRequest 

Table 3.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified CredentialsRequest 

Table 3.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema  |   
Show more

Table 3.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema   
201 - Created  |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.4. /apis/cloudcredential.openshift.io/v1/namespaces/{namespace}/credentialsrequests/{name}/status

Table 3.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CredentialsRequest   
Show more

HTTP method
     `GET`
Description
     read status of the specified CredentialsRequest 

Table 3.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified CredentialsRequest 

Table 3.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified CredentialsRequest 

Table 3.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema  |   
Show more

Table 3.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema   
201 - Created  |  [`CredentialsRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/credentialsrequest-cloudcredential-openshift-io-v1 "Chapter 3. CredentialsRequest \[cloudcredential.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
