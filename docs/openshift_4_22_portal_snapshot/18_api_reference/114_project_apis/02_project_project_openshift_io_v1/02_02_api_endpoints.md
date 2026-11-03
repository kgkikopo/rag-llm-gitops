# 2.2. API endpoints

The following API endpoints are available: 

  * `/apis/project.openshift.io/v1/projects`

    * `GET`: list or watch objects of kind Project 
    * `POST`: create a Project 

  * `/apis/project.openshift.io/v1/watch/projects`

    * `GET`: watch individual changes to a list of Project. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/project.openshift.io/v1/projects/{name}`

    * `DELETE`: delete a Project 
    * `GET`: read the specified Project 
    * `PATCH`: partially update the specified Project 
    * `PUT`: replace the specified Project 

  * `/apis/project.openshift.io/v1/watch/projects/{name}`

    * `GET`: watch changes to an object of kind Project. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 2.2.1. /apis/project.openshift.io/v1/projects

HTTP method
     `GET`
Description
     list or watch objects of kind Project 

Table 2.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ProjectList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-project-v1-ProjectList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a Project 

Table 2.2. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.3. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Project`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/project_apis/project-project-openshift-io-v1 "Chapter 2. Project \[project.openshift.io/v1\]") schema  |   
Show more

Table 2.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Project`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/project_apis/project-project-openshift-io-v1 "Chapter 2. Project \[project.openshift.io/v1\]") schema   
201 - Created  |  [`Project`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/project_apis/project-project-openshift-io-v1 "Chapter 2. Project \[project.openshift.io/v1\]") schema   
202 - Accepted  |  [`Project`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/project_apis/project-project-openshift-io-v1 "Chapter 2. Project \[project.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /apis/project.openshift.io/v1/watch/projects

HTTP method
     `GET`
Description
     watch individual changes to a list of Project. deprecated: use the 'watch' parameter with a list operation instead. 

Table 2.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /apis/project.openshift.io/v1/projects/{name}

Table 2.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Project   
Show more

HTTP method
     `DELETE`
Description
     delete a Project 

Table 2.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 2.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Project 

Table 2.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Project`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/project_apis/project-project-openshift-io-v1 "Chapter 2. Project \[project.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Project 

Table 2.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Project`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/project_apis/project-project-openshift-io-v1 "Chapter 2. Project \[project.openshift.io/v1\]") schema   
201 - Created  |  [`Project`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/project_apis/project-project-openshift-io-v1 "Chapter 2. Project \[project.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Project 

Table 2.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 2.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Project`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/project_apis/project-project-openshift-io-v1 "Chapter 2. Project \[project.openshift.io/v1\]") schema  |   
Show more

Table 2.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Project`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/project_apis/project-project-openshift-io-v1 "Chapter 2. Project \[project.openshift.io/v1\]") schema   
201 - Created  |  [`Project`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/project_apis/project-project-openshift-io-v1 "Chapter 2. Project \[project.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.4. /apis/project.openshift.io/v1/watch/projects/{name}

Table 2.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Project   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Project. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 2.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
