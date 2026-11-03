# 5.2. API endpoints

The following API endpoints are available: 

  * `/apis/user.openshift.io/v1/users`

    * `DELETE`: delete collection of User 
    * `GET`: list or watch objects of kind User 
    * `POST`: create an User 

  * `/apis/user.openshift.io/v1/watch/users`

    * `GET`: watch individual changes to a list of User. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/user.openshift.io/v1/users/{name}`

    * `DELETE`: delete an User 
    * `GET`: read the specified User 
    * `PATCH`: partially update the specified User 
    * `PUT`: replace the specified User 

  * `/apis/user.openshift.io/v1/watch/users/{name}`

    * `GET`: watch changes to an object of kind User. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 5.2.1. /apis/user.openshift.io/v1/users

HTTP method
     `DELETE`
Description
     delete collection of User 

Table 5.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind User 

Table 5.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`UserList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-user-v1-UserList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an User 

Table 5.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`User`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/user-user-openshift-io-v1 "Chapter 5. User \[user.openshift.io/v1\]") schema  |   
Show more

Table 5.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`User`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/user-user-openshift-io-v1 "Chapter 5. User \[user.openshift.io/v1\]") schema   
201 - Created  |  [`User`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/user-user-openshift-io-v1 "Chapter 5. User \[user.openshift.io/v1\]") schema   
202 - Accepted  |  [`User`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/user-user-openshift-io-v1 "Chapter 5. User \[user.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.2. /apis/user.openshift.io/v1/watch/users

HTTP method
     `GET`
Description
     watch individual changes to a list of User. deprecated: use the 'watch' parameter with a list operation instead. 

Table 5.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.3. /apis/user.openshift.io/v1/users/{name}

Table 5.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the User   
Show more

HTTP method
     `DELETE`
Description
     delete an User 

Table 5.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 5.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified User 

Table 5.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`User`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/user-user-openshift-io-v1 "Chapter 5. User \[user.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified User 

Table 5.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`User`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/user-user-openshift-io-v1 "Chapter 5. User \[user.openshift.io/v1\]") schema   
201 - Created  |  [`User`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/user-user-openshift-io-v1 "Chapter 5. User \[user.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified User 

Table 5.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 5.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`User`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/user-user-openshift-io-v1 "Chapter 5. User \[user.openshift.io/v1\]") schema  |   
Show more

Table 5.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`User`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/user-user-openshift-io-v1 "Chapter 5. User \[user.openshift.io/v1\]") schema   
201 - Created  |  [`User`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/user_and_group_apis/user-user-openshift-io-v1 "Chapter 5. User \[user.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 5.2.4. /apis/user.openshift.io/v1/watch/users/{name}

Table 5.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the User   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind User. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 5.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
