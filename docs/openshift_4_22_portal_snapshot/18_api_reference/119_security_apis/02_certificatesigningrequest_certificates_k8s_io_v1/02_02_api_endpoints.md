# 2.2. API endpoints

The following API endpoints are available: 

  * `/apis/certificates.k8s.io/v1/certificatesigningrequests`

    * `DELETE`: delete collection of CertificateSigningRequest 
    * `GET`: list or watch objects of kind CertificateSigningRequest 
    * `POST`: create a CertificateSigningRequest 

  * `/apis/certificates.k8s.io/v1/watch/certificatesigningrequests`

    * `GET`: watch individual changes to a list of CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/certificates.k8s.io/v1/certificatesigningrequests/{name}`

    * `DELETE`: delete a CertificateSigningRequest 
    * `GET`: read the specified CertificateSigningRequest 
    * `PATCH`: partially update the specified CertificateSigningRequest 
    * `PUT`: replace the specified CertificateSigningRequest 

  * `/apis/certificates.k8s.io/v1/watch/certificatesigningrequests/{name}`

    * `GET`: watch changes to an object of kind CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/status`

    * `GET`: read status of the specified CertificateSigningRequest 
    * `PATCH`: partially update status of the specified CertificateSigningRequest 
    * `PUT`: replace status of the specified CertificateSigningRequest 

  * `/apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/approval`

    * `GET`: read approval of the specified CertificateSigningRequest 
    * `PATCH`: partially update approval of the specified CertificateSigningRequest 
    * `PUT`: replace approval of the specified CertificateSigningRequest 




## 2.2.1. /apis/certificates.k8s.io/v1/certificatesigningrequests

HTTP method
     `DELETE`
Description
     delete collection of CertificateSigningRequest 

Table 2.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind CertificateSigningRequest 

Table 2.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CertificateSigningRequestList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-certificates-v1-CertificateSigningRequestList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a CertificateSigningRequest 

Table 2.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema  |   
Show more

Table 2.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
201 - Created  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
202 - Accepted  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /apis/certificates.k8s.io/v1/watch/certificatesigningrequests

HTTP method
     `GET`
Description
     watch individual changes to a list of CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead. 

Table 2.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /apis/certificates.k8s.io/v1/certificatesigningrequests/{name}

Table 2.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CertificateSigningRequest   
Show more

HTTP method
     `DELETE`
Description
     delete a CertificateSigningRequest 

Table 2.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified CertificateSigningRequest 

Table 2.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified CertificateSigningRequest 

Table 2.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
201 - Created  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified CertificateSigningRequest 

Table 2.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema  |   
Show more

Table 2.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
201 - Created  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.4. /apis/certificates.k8s.io/v1/watch/certificatesigningrequests/{name}

Table 2.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CertificateSigningRequest   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 2.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.5. /apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/status

Table 2.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CertificateSigningRequest   
Show more

HTTP method
     `GET`
Description
     read status of the specified CertificateSigningRequest 

Table 2.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified CertificateSigningRequest 

Table 2.21. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
201 - Created  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified CertificateSigningRequest 

Table 2.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.24. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema  |   
Show more

Table 2.25. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
201 - Created  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.6. /apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/approval

Table 2.26. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the CertificateSigningRequest   
Show more

HTTP method
     `GET`
Description
     read approval of the specified CertificateSigningRequest 

Table 2.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update approval of the specified CertificateSigningRequest 

Table 2.28. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.29. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
201 - Created  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace approval of the specified CertificateSigningRequest 

Table 2.30. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.31. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema  |   
Show more

Table 2.32. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
201 - Created  |  [`CertificateSigningRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_apis/certificatesigningrequest-certificates-k8s-io-v1 "Chapter 2. CertificateSigningRequest \[certificates.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
