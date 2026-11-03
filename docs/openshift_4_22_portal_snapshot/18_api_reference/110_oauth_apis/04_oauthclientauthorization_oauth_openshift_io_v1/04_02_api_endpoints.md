# 4.2. API endpoints

The following API endpoints are available: 

  * `/apis/oauth.openshift.io/v1/oauthclientauthorizations`

    * `DELETE`: delete collection of OAuthClientAuthorization 
    * `GET`: list or watch objects of kind OAuthClientAuthorization 
    * `POST`: create an OAuthClientAuthorization 

  * `/apis/oauth.openshift.io/v1/watch/oauthclientauthorizations`

    * `GET`: watch individual changes to a list of OAuthClientAuthorization. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/oauth.openshift.io/v1/oauthclientauthorizations/{name}`

    * `DELETE`: delete an OAuthClientAuthorization 
    * `GET`: read the specified OAuthClientAuthorization 
    * `PATCH`: partially update the specified OAuthClientAuthorization 
    * `PUT`: replace the specified OAuthClientAuthorization 

  * `/apis/oauth.openshift.io/v1/watch/oauthclientauthorizations/{name}`

    * `GET`: watch changes to an object of kind OAuthClientAuthorization. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 4.2.1. /apis/oauth.openshift.io/v1/oauthclientauthorizations

HTTP method
     `DELETE`
Description
     delete collection of OAuthClientAuthorization 

Table 4.1. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind OAuthClientAuthorization 

Table 4.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OAuthClientAuthorizationList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-oauth-v1-OAuthClientAuthorizationList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an OAuthClientAuthorization 

Table 4.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.5. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OAuthClientAuthorization`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/oauth_apis/oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization \[oauth.openshift.io/v1\]") schema  |   
Show more

Table 4.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OAuthClientAuthorization`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/oauth_apis/oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization \[oauth.openshift.io/v1\]") schema   
201 - Created  |  [`OAuthClientAuthorization`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/oauth_apis/oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization \[oauth.openshift.io/v1\]") schema   
202 - Accepted  |  [`OAuthClientAuthorization`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/oauth_apis/oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization \[oauth.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.2. /apis/oauth.openshift.io/v1/watch/oauthclientauthorizations

HTTP method
     `GET`
Description
     watch individual changes to a list of OAuthClientAuthorization. deprecated: use the 'watch' parameter with a list operation instead. 

Table 4.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.3. /apis/oauth.openshift.io/v1/oauthclientauthorizations/{name}

Table 4.8. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OAuthClientAuthorization   
Show more

HTTP method
     `DELETE`
Description
     delete an OAuthClientAuthorization 

Table 4.9. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.10. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified OAuthClientAuthorization 

Table 4.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OAuthClientAuthorization`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/oauth_apis/oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization \[oauth.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified OAuthClientAuthorization 

Table 4.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OAuthClientAuthorization`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/oauth_apis/oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization \[oauth.openshift.io/v1\]") schema   
201 - Created  |  [`OAuthClientAuthorization`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/oauth_apis/oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization \[oauth.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified OAuthClientAuthorization 

Table 4.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.15. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`OAuthClientAuthorization`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/oauth_apis/oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization \[oauth.openshift.io/v1\]") schema  |   
Show more

Table 4.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`OAuthClientAuthorization`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/oauth_apis/oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization \[oauth.openshift.io/v1\]") schema   
201 - Created  |  [`OAuthClientAuthorization`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/oauth_apis/oauthclientauthorization-oauth-openshift-io-v1 "Chapter 4. OAuthClientAuthorization \[oauth.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.4. /apis/oauth.openshift.io/v1/watch/oauthclientauthorizations/{name}

Table 4.17. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the OAuthClientAuthorization   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind OAuthClientAuthorization. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 4.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
