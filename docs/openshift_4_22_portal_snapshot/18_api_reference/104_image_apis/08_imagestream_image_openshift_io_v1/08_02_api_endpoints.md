# 8.2. API endpoints

The following API endpoints are available: 

  * `/apis/image.openshift.io/v1/imagestreams`

    * `GET`: list or watch objects of kind ImageStream 

  * `/apis/image.openshift.io/v1/watch/imagestreams`

    * `GET`: watch individual changes to a list of ImageStream. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams`

    * `DELETE`: delete collection of ImageStream 
    * `GET`: list or watch objects of kind ImageStream 
    * `POST`: create an ImageStream 

  * `/apis/image.openshift.io/v1/watch/namespaces/{namespace}/imagestreams`

    * `GET`: watch individual changes to a list of ImageStream. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}`

    * `DELETE`: delete an ImageStream 
    * `GET`: read the specified ImageStream 
    * `PATCH`: partially update the specified ImageStream 
    * `PUT`: replace the specified ImageStream 

  * `/apis/image.openshift.io/v1/watch/namespaces/{namespace}/imagestreams/{name}`

    * `GET`: watch changes to an object of kind ImageStream. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/status`

    * `GET`: read status of the specified ImageStream 
    * `PATCH`: partially update status of the specified ImageStream 
    * `PUT`: replace status of the specified ImageStream 




## 8.2.1. /apis/image.openshift.io/v1/imagestreams

HTTP method
     `GET`
Description
     list or watch objects of kind ImageStream 

Table 8.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStreamList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-image-v1-ImageStreamList) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.2. /apis/image.openshift.io/v1/watch/imagestreams

HTTP method
     `GET`
Description
     watch individual changes to a list of ImageStream. deprecated: use the 'watch' parameter with a list operation instead. 

Table 8.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.3. /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams

HTTP method
     `DELETE`
Description
     delete collection of ImageStream 

Table 8.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 8.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind ImageStream 

Table 8.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStreamList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-image-v1-ImageStreamList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an ImageStream 

Table 8.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema  |   
Show more

Table 8.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
201 - Created  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
202 - Accepted  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.4. /apis/image.openshift.io/v1/watch/namespaces/{namespace}/imagestreams

HTTP method
     `GET`
Description
     watch individual changes to a list of ImageStream. deprecated: use the 'watch' parameter with a list operation instead. 

Table 8.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.5. /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}

Table 8.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ImageStream   
Show more

HTTP method
     `DELETE`
Description
     delete an ImageStream 

Table 8.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 8.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
202 - Accepted  |  [`Status_v2`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status_v2) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified ImageStream 

Table 8.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified ImageStream 

Table 8.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
201 - Created  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified ImageStream 

Table 8.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema  |   
Show more

Table 8.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
201 - Created  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.6. /apis/image.openshift.io/v1/watch/namespaces/{namespace}/imagestreams/{name}

Table 8.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ImageStream   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind ImageStream. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 8.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 8.2.7. /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/status

Table 8.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ImageStream   
Show more

HTTP method
     `GET`
Description
     read status of the specified ImageStream 

Table 8.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified ImageStream 

Table 8.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
201 - Created  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified ImageStream 

Table 8.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 8.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema  |   
Show more

Table 8.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
201 - Created  |  [`ImageStream`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestream-image-openshift-io-v1 "Chapter 8. ImageStream \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
