# 2.2. API endpoints

The following API endpoints are available: 

  * `/apis/quota.openshift.io/v1/appliedclusterresourcequotas`

    * `GET`: list objects of kind AppliedClusterResourceQuota 

  * `/apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas`

    * `GET`: list objects of kind AppliedClusterResourceQuota 

  * `/apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas/{name}`

    * `GET`: read the specified AppliedClusterResourceQuota 




## 2.2.1. /apis/quota.openshift.io/v1/appliedclusterresourcequotas

HTTP method
     `GET`
Description
     list objects of kind AppliedClusterResourceQuota 

Table 2.1. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AppliedClusterResourceQuotaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-quota-v1-AppliedClusterResourceQuotaList) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.2. /apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas

HTTP method
     `GET`
Description
     list objects of kind AppliedClusterResourceQuota 

Table 2.2. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AppliedClusterResourceQuotaList`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#com-github-openshift-api-quota-v1-AppliedClusterResourceQuotaList) schema   
401 - Unauthorized  |  Empty   
Show more

## 2.2.3. /apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas/{name}

Table 2.3. Global path parametersParameter| Type| Description  
---|---|---  
`name` |  `string` |  name of the AppliedClusterResourceQuota   
Show more

HTTP method
     `GET`
Description
     read the specified AppliedClusterResourceQuota 

Table 2.4. HTTP responsesHTTP code| Reponse body  
---|---  
200 - OK  |  [`AppliedClusterResourceQuota`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/schedule_and_quota_apis/appliedclusterresourcequota-quota-openshift-io-v1 "Chapter 2. AppliedClusterResourceQuota \[quota.openshift.io/v1\]") schema   
401 - Unauthorized  |  Empty   
Show more
