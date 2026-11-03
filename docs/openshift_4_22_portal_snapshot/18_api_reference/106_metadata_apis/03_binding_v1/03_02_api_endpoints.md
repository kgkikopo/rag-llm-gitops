# 3.2. API endpoints

The following API endpoints are available: 

  * `/api/v1/namespaces/{namespace}/bindings`

    * `POST`: create a Binding 

  * `/api/v1/namespaces/{namespace}/pods/{name}/binding`

    * `POST`: create binding of a Pod 




## 3.2.1. /api/v1/namespaces/{namespace}/bindings

Table 3.1. Global query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

HTTP method
     `POST`
Description
     create a Binding 

Table 3.2. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Binding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/binding-v1 "Chapter 3. Binding \[v1\]") schema  |   
Show more

Table 3.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Binding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/binding-v1 "Chapter 3. Binding \[v1\]") schema   
201 - Created  |  [`Binding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/binding-v1 "Chapter 3. Binding \[v1\]") schema   
202 - Accepted  |  [`Binding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/binding-v1 "Chapter 3. Binding \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 3.2.2. /api/v1/namespaces/{namespace}/pods/{name}/binding

Table 3.4. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Binding   
Show more

Table 3.5. Global query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

HTTP method
     `POST`
Description
     create binding of a Pod 

Table 3.6. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Binding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/binding-v1 "Chapter 3. Binding \[v1\]") schema  |   
Show more

Table 3.7. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Binding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/binding-v1 "Chapter 3. Binding \[v1\]") schema   
201 - Created  |  [`Binding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/binding-v1 "Chapter 3. Binding \[v1\]") schema   
202 - Accepted  |  [`Binding`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/binding-v1 "Chapter 3. Binding \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
