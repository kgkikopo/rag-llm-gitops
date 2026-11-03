# 7.2. API endpoints

The following API endpoints are available: 

  * `/apis/events.k8s.io/v1/events`

    * `GET`: list or watch objects of kind Event 

  * `/apis/events.k8s.io/v1/watch/events`

    * `GET`: watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/events.k8s.io/v1/namespaces/{namespace}/events`

    * `DELETE`: delete collection of Event 
    * `GET`: list or watch objects of kind Event 
    * `POST`: create an Event 

  * `/apis/events.k8s.io/v1/watch/namespaces/{namespace}/events`

    * `GET`: watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead. 

  * `/apis/events.k8s.io/v1/namespaces/{namespace}/events/{name}`

    * `DELETE`: delete an Event 
    * `GET`: read the specified Event 
    * `PATCH`: partially update the specified Event 
    * `PUT`: replace the specified Event 

  * `/apis/events.k8s.io/v1/watch/namespaces/{namespace}/events/{name}`

    * `GET`: watch changes to an object of kind Event. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 




## 7.2.1. /apis/events.k8s.io/v1/events

HTTP method
     `GET`
Description
     list or watch objects of kind Event 

Table 7.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EventList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-events-v1-EventList) schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.2. /apis/events.k8s.io/v1/watch/events

HTTP method
     `GET`
Description
     watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead. 

Table 7.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.3. /apis/events.k8s.io/v1/namespaces/{namespace}/events

HTTP method
     `DELETE`
Description
     delete collection of Event 

Table 7.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 7.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list or watch objects of kind Event 

Table 7.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`EventList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-events-v1-EventList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create an Event 

Table 7.6. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.7. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Event`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/event-events-k8s-io-v1 "Chapter 7. Event \[events.k8s.io/v1\]") schema  |   
Show more

Table 7.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Event`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/event-events-k8s-io-v1 "Chapter 7. Event \[events.k8s.io/v1\]") schema   
201 - Created  |  [`Event`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/event-events-k8s-io-v1 "Chapter 7. Event \[events.k8s.io/v1\]") schema   
202 - Accepted  |  [`Event`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/event-events-k8s-io-v1 "Chapter 7. Event \[events.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.4. /apis/events.k8s.io/v1/watch/namespaces/{namespace}/events

HTTP method
     `GET`
Description
     watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead. 

Table 7.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.5. /apis/events.k8s.io/v1/namespaces/{namespace}/events/{name}

Table 7.10. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Event   
Show more

HTTP method
     `DELETE`
Description
     delete an Event 

Table 7.11. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 7.12. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified Event 

Table 7.13. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Event`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/event-events-k8s-io-v1 "Chapter 7. Event \[events.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified Event 

Table 7.14. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.15. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Event`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/event-events-k8s-io-v1 "Chapter 7. Event \[events.k8s.io/v1\]") schema   
201 - Created  |  [`Event`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/event-events-k8s-io-v1 "Chapter 7. Event \[events.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified Event 

Table 7.16. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 7.17. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`Event`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/event-events-k8s-io-v1 "Chapter 7. Event \[events.k8s.io/v1\]") schema  |   
Show more

Table 7.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Event`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/event-events-k8s-io-v1 "Chapter 7. Event \[events.k8s.io/v1\]") schema   
201 - Created  |  [`Event`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/event-events-k8s-io-v1 "Chapter 7. Event \[events.k8s.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 7.2.6. /apis/events.k8s.io/v1/watch/namespaces/{namespace}/events/{name}

Table 7.19. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the Event   
Show more

HTTP method
     `GET`
Description
     watch changes to an object of kind Event. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter. 

Table 7.20. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`WatchEvent`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-WatchEvent) schema   
401 - Unauthorized  |  Empty   
Show more
