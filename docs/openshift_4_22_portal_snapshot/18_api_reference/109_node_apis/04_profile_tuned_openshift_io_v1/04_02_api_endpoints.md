# 4.2. API endpoints

The following API endpoints are available: 

  * `/apis/tuned.openshift.io/v1/profiles`

    * `GET`: list objects of kind Profile 

  * `/apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles`

    * `DELETE`: delete collection of Profile 
    * `GET`: list objects of kind Profile 
    * `POST`: create a Profile 

  * `/apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles/{name}`

    * `DELETE`: delete a Profile 
    * `GET`: read the specified Profile 
    * `PATCH`: partially update the specified Profile 
    * `PUT`: replace the specified Profile 

  * `/apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles/{name}/status`

    * `GET`: read status of the specified Profile 
    * `PATCH`: partially update status of the specified Profile 
    * `PUT`: replace status of the specified Profile 




## 4.2.1. /apis/tuned.openshift.io/v1/profiles

HTTP method
     `GET`
Description
     list objects of kind Profile 

Table 4.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ProfileList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-tuned-v1-ProfileList) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.2. /apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles

HTTP method
     `DELETE`
Description
     delete collection of Profile 

Table 4.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind Profile 

Table 4.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ProfileList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-tuned-v1-ProfileList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Profile 

Table 4.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema  |   
Show more

Table 4.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema   
201 - Created  |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema   
202 - Accepted  |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.3. /apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles/{name}

Table 4.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Profile   
Show more

HTTP method
     `DELETE`
Description
     delete a Profile 

Table 4.8. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Profile 

Table 4.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Profile 

Table 4.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Profile 

Table 4.13. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.14. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema  |   
Show more

Table 4.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema   
201 - Created  |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.4. /apis/tuned.openshift.io/v1/namespaces/{namespace}/profiles/{name}/status

Table 4.16. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Profile   
Show more

HTTP method
     `GET`
Description
     read status of the specified Profile 

Table 4.17. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified Profile 

Table 4.18. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.19. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified Profile 

Table 4.20. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.21. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema  |   
Show more

Table 4.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema   
201 - Created  |  [`Profile`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/node_apis/profile-tuned-openshift-io-v1 "Chapter 4. Profile \[tuned.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
