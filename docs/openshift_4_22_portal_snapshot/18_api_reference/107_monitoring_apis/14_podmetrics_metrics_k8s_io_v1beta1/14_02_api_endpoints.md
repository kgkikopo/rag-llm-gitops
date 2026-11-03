# 14.2. API endpoints

The following API endpoints are available: 

  * `/apis/metrics.k8s.io/v1beta1/pods`

    * `GET`: list objects of kind PodMetrics 

  * `/apis/metrics.k8s.io/v1beta1/namespaces/{namespace}/pods`

    * `GET`: list objects of kind PodMetrics 

  * `/apis/metrics.k8s.io/v1beta1/namespaces/{namespace}/pods/{name}`

    * `GET`: read the specified PodMetrics 




## 14.2.1. /apis/metrics.k8s.io/v1beta1/pods

HTTP method
     `GET`
Description
     list objects of kind PodMetrics 

Table 14.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodMetricsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-metrics-pkg-apis-metrics-v1beta1-PodMetricsList) schema   
Show more

## 14.2.2. /apis/metrics.k8s.io/v1beta1/namespaces/{namespace}/pods

HTTP method
     `GET`
Description
     list objects of kind PodMetrics 

Table 14.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodMetricsList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-metrics-pkg-apis-metrics-v1beta1-PodMetricsList) schema   
Show more

## 14.2.3. /apis/metrics.k8s.io/v1beta1/namespaces/{namespace}/pods/{name}

Table 14.3. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the PodMetrics   
Show more

HTTP method
     `GET`
Description
     read the specified PodMetrics 

Table 14.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`PodMetrics`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/monitoring_apis/podmetrics-metrics-k8s-io-v1beta1 "Chapter 14. PodMetrics \[metrics.k8s.io/v1beta1\]") schema   
Show more
