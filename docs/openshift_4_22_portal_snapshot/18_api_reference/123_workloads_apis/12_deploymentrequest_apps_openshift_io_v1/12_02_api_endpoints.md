# 12.2. API endpoints

The following API endpoints are available: 

  * `/apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/instantiate`

    * `POST`: create instantiate of a DeploymentConfig 




## 12.2.1. /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/instantiate

Table 12.1. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the DeploymentRequest   
Show more

Table 12.2. Global query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

HTTP method
     `POST`
Description
     create instantiate of a DeploymentConfig 

Table 12.3. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`DeploymentRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deploymentrequest-apps-openshift-io-v1 "Chapter 12. DeploymentRequest \[apps.openshift.io/v1\]") schema  |   
Show more

Table 12.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DeploymentRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deploymentrequest-apps-openshift-io-v1 "Chapter 12. DeploymentRequest \[apps.openshift.io/v1\]") schema   
201 - Created  |  [`DeploymentRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deploymentrequest-apps-openshift-io-v1 "Chapter 12. DeploymentRequest \[apps.openshift.io/v1\]") schema   
202 - Accepted  |  [`DeploymentRequest`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deploymentrequest-apps-openshift-io-v1 "Chapter 12. DeploymentRequest \[apps.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
