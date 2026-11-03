# 3.2. API endpoints

The following API endpoints are available: 

  * `/apis/user.openshift.io/v1/identities`

    * `DELETE`: delete collection of Identity 
    * `GET`: list or watch objects of kind Identity 
    * `POST`: create an Identity 

  * `/apis/user.openshift.io/v1/watch/identities`

    * `GET`: watch individual changes to a list of Identity. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/user.openshift.io/v1/identities/{name}`

    * `DELETE`: delete an Identity 
    * `GET`: read the specified Identity 
    * `PATCH`: partially update the specified Identity 
    * `PUT`: replace the specified Identity 

  * `/apis/user.openshift.io/v1/watch/identities/{name}`

    * `GET`: watch changes to an object of kind Identity. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 3.2.1. /apis/user.openshift.io/v1/identities

HTTP method
     `DELETE`
Description
     delete collection of Identity 

Table 3.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Identity 

Table 3.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`IdentityList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-user-v1-IdentityList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an Identity 

Table 3.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Identity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/identity-user-openshift-io-v1 "Chapter 3. Identity \[user.openshift.io/v1\]") schema  |   
Show more

Table 3.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Identity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/identity-user-openshift-io-v1 "Chapter 3. Identity \[user.openshift.io/v1\]") schema   
201 - Created  |  [`Identity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/identity-user-openshift-io-v1 "Chapter 3. Identity \[user.openshift.io/v1\]") schema   
202 - Accepted  |  [`Identity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/identity-user-openshift-io-v1 "Chapter 3. Identity \[user.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.2. /apis/user.openshift.io/v1/watch/identities

HTTP method
     `GET`
Description
     watch individual changes to a list of Identity. deprecated: use the 'watch' parameter with a list operation instead. 

Table 3.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.3. /apis/user.openshift.io/v1/identities/{name}

Table 3.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Identity   
Show more

HTTP method
     `DELETE`
Description
     delete an Identity 

Table 3.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 3.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Identity 

Table 3.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Identity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/identity-user-openshift-io-v1 "Chapter 3. Identity \[user.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Identity 

Table 3.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Identity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/identity-user-openshift-io-v1 "Chapter 3. Identity \[user.openshift.io/v1\]") schema   
201 - Created  |  [`Identity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/identity-user-openshift-io-v1 "Chapter 3. Identity \[user.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Identity 

Table 3.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 3.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Identity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/identity-user-openshift-io-v1 "Chapter 3. Identity \[user.openshift.io/v1\]") schema  |   
Show more

Table 3.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Identity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/identity-user-openshift-io-v1 "Chapter 3. Identity \[user.openshift.io/v1\]") schema   
201 - Created  |  [`Identity`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/identity-user-openshift-io-v1 "Chapter 3. Identity \[user.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.4. /apis/user.openshift.io/v1/watch/identities/{name}

Table 3.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Identity   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Identity. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 3.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
