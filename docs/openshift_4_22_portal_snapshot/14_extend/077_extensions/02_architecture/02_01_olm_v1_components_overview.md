# 2.1. OLM v1 components overview

Operator Lifecycle Manager (OLM) v1 uses two key microservice components, Operator Controller and Catalogd, to unpack content and manage extensions on your cluster. 

Operator Controller
     Extends Kubernetes with an API to install and manage Operators and extensions using metadata from Catalogd. 
Catalogd
     Unpacks file-based catalog (FBC) content and hosts metadata so users can discover installable extensions. 

## 2.1.1. Additional resources

  * [Operator Controller](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/architecture#operator-controller "2.2. Operator Controller")
  * [Catalogd](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/extensions/architecture#catalogd "2.3. Catalogd")
