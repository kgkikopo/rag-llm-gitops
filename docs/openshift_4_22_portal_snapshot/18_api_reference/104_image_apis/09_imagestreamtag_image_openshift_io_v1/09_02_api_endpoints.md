# 9.2. API endpoints

The following API endpoints are available: 

  * `/apis/image.openshift.io/v1/imagestreamtags`

    * `GET`: list objects of kind ImageStreamTag 

  * `/apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamtags`

    * `GET`: list objects of kind ImageStreamTag 
    * `POST`: create an ImageStreamTag 

  * `/apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamtags/{name}`

    * `DELETE`: delete an ImageStreamTag 
    * `GET`: read the specified ImageStreamTag 
    * `PATCH`: partially update the specified ImageStreamTag 
    * `PUT`: replace the specified ImageStreamTag 




## 9.2.1. /apis/image.openshift.io/v1/imagestreamtags

HTTP method
     `GET`
Description
     list objects of kind ImageStreamTag 

Table 9.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStreamTagList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-image-v1-ImageStreamTagList) schema   
401 - Unauthorized  |  Empty   
Show more

## 9.2.2. /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamtags

HTTP method
     `GET`
Description
     list objects of kind ImageStreamTag 

Table 9.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStreamTagList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-image-v1-ImageStreamTagList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an ImageStreamTag 

Table 9.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 9.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ImageStreamTag`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamtag-image-openshift-io-v1 "Chapter 9. ImageStreamTag \[image.openshift.io/v1\]") schema  |   
Show more

Table 9.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStreamTag`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamtag-image-openshift-io-v1 "Chapter 9. ImageStreamTag \[image.openshift.io/v1\]") schema   
201 - Created  |  [`ImageStreamTag`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamtag-image-openshift-io-v1 "Chapter 9. ImageStreamTag \[image.openshift.io/v1\]") schema   
202 - Accepted  |  [`ImageStreamTag`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamtag-image-openshift-io-v1 "Chapter 9. ImageStreamTag \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 9.2.3. /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamtags/{name}

Table 9.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ImageStreamTag   
Show more

HTTP method
     `DELETE`
Description
     delete an ImageStreamTag 

Table 9.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 9.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ImageStreamTag 

Table 9.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStreamTag`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamtag-image-openshift-io-v1 "Chapter 9. ImageStreamTag \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ImageStreamTag 

Table 9.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 9.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStreamTag`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamtag-image-openshift-io-v1 "Chapter 9. ImageStreamTag \[image.openshift.io/v1\]") schema   
201 - Created  |  [`ImageStreamTag`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamtag-image-openshift-io-v1 "Chapter 9. ImageStreamTag \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ImageStreamTag 

Table 9.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 9.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ImageStreamTag`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamtag-image-openshift-io-v1 "Chapter 9. ImageStreamTag \[image.openshift.io/v1\]") schema  |   
Show more

Table 9.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStreamTag`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamtag-image-openshift-io-v1 "Chapter 9. ImageStreamTag \[image.openshift.io/v1\]") schema   
201 - Created  |  [`ImageStreamTag`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamtag-image-openshift-io-v1 "Chapter 9. ImageStreamTag \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
