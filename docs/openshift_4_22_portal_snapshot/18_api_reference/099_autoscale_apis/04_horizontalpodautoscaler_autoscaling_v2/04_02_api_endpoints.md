# 4.2. API endpoints

The following API endpoints are available: 

  * `/apis/autoscaling/v2/horizontalpodautoscalers`

    * `GET`: list or watch objects of kind HorizontalPodAutoscaler 

  * `/apis/autoscaling/v2/watch/horizontalpodautoscalers`

    * `GET`: watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers`

    * `DELETE`: delete collection of HorizontalPodAutoscaler 
    * `GET`: list or watch objects of kind HorizontalPodAutoscaler 
    * `POST`: create a HorizontalPodAutoscaler 

  * `/apis/autoscaling/v2/watch/namespaces/{namespace}/horizontalpodautoscalers`

    * `GET`: watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}`

    * `DELETE`: delete a HorizontalPodAutoscaler 
    * `GET`: read the specified HorizontalPodAutoscaler 
    * `PATCH`: partially update the specified HorizontalPodAutoscaler 
    * `PUT`: replace the specified HorizontalPodAutoscaler 

  * `/apis/autoscaling/v2/watch/namespaces/{namespace}/horizontalpodautoscalers/{name}`

    * `GET`: watch changes to an object of kind HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

  * `/apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}/status`

    * `GET`: read status of the specified HorizontalPodAutoscaler 
    * `PATCH`: partially update status of the specified HorizontalPodAutoscaler 
    * `PUT`: replace status of the specified HorizontalPodAutoscaler 




## 4.2.1. /apis/autoscaling/v2/horizontalpodautoscalers

HTTP method
     `GET`
Description
     list or watch objects of kind HorizontalPodAutoscaler 

Table 4.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HorizontalPodAutoscalerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-autoscaling-v2-HorizontalPodAutoscalerList) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.2. /apis/autoscaling/v2/watch/horizontalpodautoscalers

HTTP method
     `GET`
Description
     watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead. 

Table 4.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.3. /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers

HTTP method
     `DELETE`
Description
     delete collection of HorizontalPodAutoscaler 

Table 4.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind HorizontalPodAutoscaler 

Table 4.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HorizontalPodAutoscalerList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-autoscaling-v2-HorizontalPodAutoscalerList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a HorizontalPodAutoscaler 

Table 4.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema  |   
Show more

Table 4.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
201 - Created  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
202 - Accepted  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.4. /apis/autoscaling/v2/watch/namespaces/{namespace}/horizontalpodautoscalers

HTTP method
     `GET`
Description
     watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead. 

Table 4.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.5. /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}

Table 4.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the HorizontalPodAutoscaler   
Show more

HTTP method
     `DELETE`
Description
     delete a HorizontalPodAutoscaler 

Table 4.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 4.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified HorizontalPodAutoscaler 

Table 4.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified HorizontalPodAutoscaler 

Table 4.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
201 - Created  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified HorizontalPodAutoscaler 

Table 4.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema  |   
Show more

Table 4.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
201 - Created  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.6. /apis/autoscaling/v2/watch/namespaces/{namespace}/horizontalpodautoscalers/{name}

Table 4.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the HorizontalPodAutoscaler   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 4.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.7. /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}/status

Table 4.21. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the HorizontalPodAutoscaler   
Show more

HTTP method
     `GET`
Description
     read status of the specified HorizontalPodAutoscaler 

Table 4.22. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified HorizontalPodAutoscaler 

Table 4.23. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.24. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
201 - Created  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified HorizontalPodAutoscaler 

Table 4.25. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 4.26. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema  |   
Show more

Table 4.27. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
201 - Created  |  [`HorizontalPodAutoscaler`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2 "Chapter 4. HorizontalPodAutoscaler \[autoscaling/v2\]") schema   
401 - Unauthorized  |  Empty   
Show more
