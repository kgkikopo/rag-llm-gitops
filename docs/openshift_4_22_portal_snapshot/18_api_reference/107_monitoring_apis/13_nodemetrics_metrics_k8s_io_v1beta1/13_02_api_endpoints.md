# 13.2. API endpoints

The following API endpoints are available: 

  * `/apis/metrics.k8s.io/v1beta1/nodes`

    * `GET`: list objects of kind NodeMetrics 

  * `/apis/metrics.k8s.io/v1beta1/nodes/{name}`

    * `GET`: read the specified NodeMetrics 




## 13.2.1. /apis/metrics.k8s.io/v1beta1/nodes

HTTP method
     `GET`
Description
     list objects of kind NodeMetrics 

Table 13.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NodeMetricsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-metrics-pkg-apis-metrics-v1beta1-NodeMetricsList) schema   
Show more

## 13.2.2. /apis/metrics.k8s.io/v1beta1/nodes/{name}

Table 13.2. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the NodeMetrics   
Show more

HTTP method
     `GET`
Description
     read the specified NodeMetrics 

Table 13.3. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`NodeMetrics`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/nodemetrics-metrics-k8s-io-v1beta1 "Chapter 13. NodeMetrics \[metrics.k8s.io/v1beta1\]") schema   
Show more
