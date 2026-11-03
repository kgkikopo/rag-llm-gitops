# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. metadata.name must be the Kubernetes node name.   
`spec` |  `object` |  CSINodeSpec holds information about the specification of all CSI drivers installed on a node   
Show more

## 3.1.1. .spec

Description
     CSINodeSpec holds information about the specification of all CSI drivers installed on a node 
Type
     `object`
Required
    

  * `drivers`



Property| Type| Description  
---|---|---  
`drivers` |  `array` |  drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty.   
`drivers[]` |  `object` |  CSINodeDriver holds information about the specification of one CSI driver installed on a node   
Show more

## 3.1.2. .spec.drivers

Description
     drivers is a list of information of all CSI Drivers existing on a node. If all drivers in the list are uninstalled, this can become empty. 
Type
     `array`

## 3.1.3. .spec.drivers[]

Description
     CSINodeDriver holds information about the specification of one CSI driver installed on a node 
Type
     `object`
Required
    

  * `name`
  * `nodeID`



Property| Type| Description  
---|---|---  
`allocatable` |  `object` |  VolumeNodeResources is a set of resource limits for scheduling of volumes.   
`name` |  `string` |  name represents the name of the CSI driver that this object refers to. This MUST be the same name returned by the CSI GetPluginName() call for that driver.   
`nodeID` |  `string` |  nodeID of the node from the driver point of view. This field enables Kubernetes to communicate with storage systems that do not share the same nomenclature for nodes. For example, Kubernetes may refer to a given node as "node1", but the storage system may refer to the same node as "nodeA". When Kubernetes issues a command to the storage system to attach a volume to a specific node, it can use this field to refer to the node name using the ID that the storage system will understand, e.g. "nodeA" instead of "node1". This field is required.   
`topologyKeys` |  `array (string)` |  topologyKeys is the list of keys supported by the driver. When a driver is initialized on a cluster, it provides a set of topology keys that it understands (e.g. "company.com/zone", "company.com/region"). When a driver is initialized on a node, it provides the same topology keys along with values. Kubelet will expose these topology keys as labels on its own node object. When Kubernetes does topology aware provisioning, it can use this list to determine which labels it should retrieve from the node object and pass back to the driver. It is possible for different nodes to use different topology keys. This can be empty if driver does not support topology.   
Show more

## 3.1.4. .spec.drivers[].allocatable

Description
     VolumeNodeResources is a set of resource limits for scheduling of volumes. 
Type
     `object`

Property| Type| Description  
---|---|---  
`count` |  `integer` |  count indicates the maximum number of unique volumes managed by the CSI driver that can be used on a node. A volume that is both attached and mounted on a node is considered to be used once, not twice. The same rule applies for a unique volume that is shared among multiple pods on the same node. If this field is not specified, then the supported number of volumes on this node is unbounded.   
Show more
