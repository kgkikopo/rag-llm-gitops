# Chapter 3. CSINode [storage.k8s.io/v1]

Description
     CSINode holds information about all CSI drivers installed on a node. CSI drivers do not need to create the CSINode object directly. As long as they use the node-driver-registrar sidecar container, the kubelet will automatically populate the CSINode object for the CSI driver as part of kubelet plugin registration. CSINode has the same name as a node. If the object is missing, it means either there are no CSI Drivers available on the node, or the Kubelet version is low enough that it doesn’t create this object. CSINode has an OwnerReference that points to the corresponding node object. 
Type
     `object`
Required
    

  * `spec`

- [3.1. Specification](03_01_specification.md)
- [3.2. API endpoints](03_02_api_endpoints.md)
