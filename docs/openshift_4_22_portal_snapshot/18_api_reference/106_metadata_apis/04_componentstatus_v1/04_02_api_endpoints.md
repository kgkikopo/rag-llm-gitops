# 4.2. API endpoints

The following API endpoints are available: 

  * `/api/v1/componentstatuses`

    * `GET`: list objects of kind ComponentStatus 

  * `/api/v1/componentstatuses/{name}`

    * `GET`: read the specified ComponentStatus 




## 4.2.1. /api/v1/componentstatuses

HTTP method
     `GET`
Description
     list objects of kind ComponentStatus 

Table 4.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ComponentStatusList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ComponentStatusList) schema   
401 - Unauthorized  |  Empty   
Show more

## 4.2.2. /api/v1/componentstatuses/{name}

Table 4.2. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the ComponentStatus   
Show more

HTTP method
     `GET`
Description
     read the specified ComponentStatus 

Table 4.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`ComponentStatus`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/metadata_apis/componentstatus-v1 "Chapter 4. ComponentStatus \[v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
