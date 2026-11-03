# 4.2. API endpoints

The following API endpoints are available: 

  * `/apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamimages/{name}`

    * `GET`: read the specified ImageStreamImage 




## 4.2.1. /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamimages/{name}

Table 4.1. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ImageStreamImage   
Show more

HTTP method
     `GET`
Description
     read the specified ImageStreamImage 

Table 4.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ImageStreamImage`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/image_apis/imagestreamimage-image-openshift-io-v1 "Chapter 4. ImageStreamImage \[image.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
