# 5.2. API endpoints

The following API endpoints are available: 

  * `/apis/authorization.openshift.io/v1/namespaces/{namespace}/selfsubjectrulesreviews`

    * `POST`: create a SelfSubjectRulesReview 




## 5.2.1. /apis/authorization.openshift.io/v1/namespaces/{namespace}/selfsubjectrulesreviews

Table 5.1. Global query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

HTTP method
     `POST`
Description
     create a SelfSubjectRulesReview 

Table 5.2. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`SelfSubjectRulesReview`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authorization_apis/selfsubjectrulesreview-authorization-openshift-io-v1 "Chapter 5. SelfSubjectRulesReview \[authorization.openshift.io/v1\]") schema  |   
Show more

Table 5.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SelfSubjectRulesReview`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authorization_apis/selfsubjectrulesreview-authorization-openshift-io-v1 "Chapter 5. SelfSubjectRulesReview \[authorization.openshift.io/v1\]") schema   
201 - Created  |  [`SelfSubjectRulesReview`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authorization_apis/selfsubjectrulesreview-authorization-openshift-io-v1 "Chapter 5. SelfSubjectRulesReview \[authorization.openshift.io/v1\]") schema   
202 - Accepted  |  [`SelfSubjectRulesReview`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authorization_apis/selfsubjectrulesreview-authorization-openshift-io-v1 "Chapter 5. SelfSubjectRulesReview \[authorization.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
