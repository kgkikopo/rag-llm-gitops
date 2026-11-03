# 11.2. API endpoints

The following API endpoints are available: 

  * `/apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/secrets`

    * `GET`: read secrets of the specified ImageStream 




## 11.2.1. /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/secrets

Table 11.1. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the SecretList   
Show more

HTTP method
     `GET`
Description
     read secrets of the specified ImageStream 

Table 11.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`SecretList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/secretlist-image-openshift-io-v1 "Chapter 11. SecretList \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
