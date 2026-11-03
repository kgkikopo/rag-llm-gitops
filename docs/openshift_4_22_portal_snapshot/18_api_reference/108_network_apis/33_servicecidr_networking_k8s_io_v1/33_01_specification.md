# 33.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ServiceCIDRSpec define the CIDRs the user wants to use for allocating ClusterIPs for Services.   
`status` |  `object` |  ServiceCIDRStatus describes the current state of the ServiceCIDR.   
Show more

## 33.1.1. .spec

Description
     ServiceCIDRSpec define the CIDRs the user wants to use for allocating ClusterIPs for Services. 
Type
     `object`

Property| Type| Description  
---|---|---  
`cidrs` |  `array (string)` |  CIDRs defines the IP blocks in CIDR notation (e.g. "192.168.0.0/24" or "2001:db8::/64") from which to assign service cluster IPs. Max of two CIDRs is allowed, one of each IP family. This field is immutable.   
Show more

## 33.1.2. .status

Description
     ServiceCIDRStatus describes the current state of the ServiceCIDR. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  [`array (Condition)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Condition) |  conditions holds an array of metav1.Condition that describe the state of the ServiceCIDR. Current service state   
Show more
