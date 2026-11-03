# 6.2. API endpoints

The following API endpoints are available: 

  * `/apis/oauth.openshift.io/v1/useroauthaccesstokens`

    * `GET`: list or watch objects of kind UserOAuthAccessToken 

  * `/apis/oauth.openshift.io/v1/watch/useroauthaccesstokens`

    * `GET`: watch individual changes to a list of UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/oauth.openshift.io/v1/useroauthaccesstokens/{name}`

    * `DELETE`: delete an UserOAuthAccessToken 
    * `GET`: read the specified UserOAuthAccessToken 

  * `/apis/oauth.openshift.io/v1/watch/useroauthaccesstokens/{name}`

    * `GET`: watch changes to an object of kind UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 6.2.1. /apis/oauth.openshift.io/v1/useroauthaccesstokens

HTTP method
     `GET`
Description
     list or watch objects of kind UserOAuthAccessToken 

Table 6.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`UserOAuthAccessTokenList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-oauth-v1-UserOAuthAccessTokenList) schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.2. /apis/oauth.openshift.io/v1/watch/useroauthaccesstokens

HTTP method
     `GET`
Description
     watch individual changes to a list of UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead. 

Table 6.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.3. /apis/oauth.openshift.io/v1/useroauthaccesstokens/{name}

Table 6.3. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the UserOAuthAccessToken   
Show more

HTTP method
     `DELETE`
Description
     delete an UserOAuthAccessToken 

Table 6.4. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 6.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified UserOAuthAccessToken 

Table 6.6. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`UserOAuthAccessToken`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/oauth_apis/useroauthaccesstoken-oauth-openshift-io-v1 "Chapter 6. UserOAuthAccessToken \[oauth.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 6.2.4. /apis/oauth.openshift.io/v1/watch/useroauthaccesstokens/{name}

Table 6.7. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the UserOAuthAccessToken   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind UserOAuthAccessToken. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 6.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
