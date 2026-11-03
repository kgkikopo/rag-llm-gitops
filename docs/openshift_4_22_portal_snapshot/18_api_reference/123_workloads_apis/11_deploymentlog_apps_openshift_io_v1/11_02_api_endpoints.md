# 11.2. API endpoints

The following API endpoints are available: 

  * `/apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/log`

    * `GET`: read log of the specified DeploymentConfig 




## 11.2.1. /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/log

Table 11.1. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the DeploymentLog   
Show more

HTTP method
     `GET`
Description
     read log of the specified DeploymentConfig 

Table 11.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`DeploymentLog`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/workloads_apis/deploymentlog-apps-openshift-io-v1 "Chapter 11. DeploymentLog \[apps.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
