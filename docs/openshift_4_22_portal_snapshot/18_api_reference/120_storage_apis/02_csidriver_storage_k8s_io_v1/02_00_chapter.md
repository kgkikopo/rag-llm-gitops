# Chapter 2. CSIDriver [storage.k8s.io/v1]

Description
     CSIDriver captures information about a Container Storage Interface (CSI) volume driver deployed on the cluster. Kubernetes attach detach controller uses this object to determine whether attach is required. Kubelet uses this object to determine whether pod information needs to be passed on mount. CSIDriver objects are non-namespaced. 
Type
     `object`
Required
    

  * `spec`

- [2.1. Specification](02_01_specification.md)
- [2.2. API endpoints](02_02_api_endpoints.md)
