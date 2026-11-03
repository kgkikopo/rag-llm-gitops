# 4.2. API endpoints

The following API endpoints are available: 

  * `/apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name}/log`

    * `GET`: read log of the specified Build 




## 4.2.1. /apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name}/log

Table 4.1. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the BuildLog   
Show more

HTTP method
     `GET`
Description
     read log of the specified Build 

Table 4.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`BuildLog`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/buildlog-build-openshift-io-v1 "Chapter 4. BuildLog \[build.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
