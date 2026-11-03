# 11.2. API endpoints

The following API endpoints are available: 

  * `/apis/helm.openshift.io/v1beta1/helmchartrepositories`

    * `DELETE`: delete collection of HelmChartRepository 
    * `GET`: list objects of kind HelmChartRepository 
    * `POST`: create a HelmChartRepository 

  * `/apis/helm.openshift.io/v1beta1/helmchartrepositories/{name}`

    * `DELETE`: delete a HelmChartRepository 
    * `GET`: read the specified HelmChartRepository 
    * `PATCH`: partially update the specified HelmChartRepository 
    * `PUT`: replace the specified HelmChartRepository 

  * `/apis/helm.openshift.io/v1beta1/helmchartrepositories/{name}/status`

    * `GET`: read status of the specified HelmChartRepository 
    * `PATCH`: partially update status of the specified HelmChartRepository 
    * `PUT`: replace status of the specified HelmChartRepository 




## 11.2.1. /apis/helm.openshift.io/v1beta1/helmchartrepositories

HTTP method
     `DELETE`
Description
     delete collection of HelmChartRepository 

Table 11.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     list objects of kind HelmChartRepository 

Table 11.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HelmChartRepositoryList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-openshift-helm-v1beta1-HelmChartRepositoryList) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `POST`
Description
     create a HelmChartRepository 

Table 11.3. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.4. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema  |   
Show more

Table 11.5. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema   
201 - Created  |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema   
202 - Accepted  |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.2. /apis/helm.openshift.io/v1beta1/helmchartrepositories/{name}

Table 11.6. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the HelmChartRepository   
Show more

HTTP method
     `DELETE`
Description
     delete a HelmChartRepository 

Table 11.7. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
Show more

Table 11.8. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
202 - Accepted  |  [`Status`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Status) schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `GET`
Description
     read the specified HelmChartRepository 

Table 11.9. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update the specified HelmChartRepository 

Table 11.10. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.11. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace the specified HelmChartRepository 

Table 11.12. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.13. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema  |   
Show more

Table 11.14. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema   
201 - Created  |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

## 11.2.3. /apis/helm.openshift.io/v1beta1/helmchartrepositories/{name}/status

Table 11.15. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the HelmChartRepository   
Show more

HTTP method
     `GET`
Description
     read status of the specified HelmChartRepository 

Table 11.16. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PATCH`
Description
     partially update status of the specified HelmChartRepository 

Table 11.17. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.18. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more

HTTP method
     `PUT`
Description
     replace status of the specified HelmChartRepository 

Table 11.19. Query parametersParameter| Type| Description  
---|---|---  
`dryRun` |  `string` |  When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed   
`fieldValidation` |  `string` |  fieldValidation instructs the server on how to handle objects in the request (POST/PUT/PATCH) containing unknown or duplicate fields. Valid values are: - Ignore: This will ignore any unknown fields that are silently dropped from the object, and will ignore all but the last duplicate field that the decoder encounters. This is the default behavior prior to v1.23. - Warn: This will send a warning via the standard warning response header for each unknown field that is dropped from the object, and for each duplicate field that is encountered. The request will still succeed if there are no other errors, and will only persist the last of any duplicate fields. This is the default in v1.23+ - Strict: This will fail the request with a BadRequest error if any unknown fields would be dropped from the object, or if any duplicate fields are present. The error returned from the server will contain all unknown and duplicate fields encountered.   
Show more

Table 11.20. Body parametersParameter| Type| Description  
---|---|---  
`body` |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema  |   
Show more

Table 11.21. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema   
201 - Created  |  [`HelmChartRepository`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/config_apis/helmchartrepository-helm-openshift-io-v1beta1 "Chapter 11. HelmChartRepository \[helm.openshift.io/v1beta1\]") schema   
401 - Unauthorized  |  Empty   
Show more
