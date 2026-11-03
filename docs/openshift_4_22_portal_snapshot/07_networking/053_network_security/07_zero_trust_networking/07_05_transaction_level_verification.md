# 7.5. Transaction-level verification

In addition to the ability to identify and authenticate connections, it is also useful to control access to individual transactions. This can include rate-limiting by source, observability, and semantic validation that a transaction is well formed. 

Leverage: 

  * [Red Hat OpenShift Service Mesh](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/service_mesh/#ossm-about): Perform L7 inspection of requests, rejecting malformed HTTP requests, transaction-level [observability and reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/service_mesh/#understanding-kiali). Service Mesh can also provide [request-based authentication](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/service_mesh/#restrict-access-with-json-web-token) using JWT.
