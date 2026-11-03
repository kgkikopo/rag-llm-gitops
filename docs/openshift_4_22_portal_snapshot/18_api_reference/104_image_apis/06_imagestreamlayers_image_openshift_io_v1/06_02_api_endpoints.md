# 6.2. API endpoints

The following API endpoints are available: 

  * `/apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/layers`

    * `GET`: read layers of the specified ImageStream 




## 6.2.1. /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/layers

Table 6.1. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ImageStreamLayers   
Show more

HTTP method
     `GET`
Description
     read layers of the specified ImageStream 

Table 6.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStreamLayers`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamlayers-image-openshift-io-v1 "Chapter 6. ImageStreamLayers \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
