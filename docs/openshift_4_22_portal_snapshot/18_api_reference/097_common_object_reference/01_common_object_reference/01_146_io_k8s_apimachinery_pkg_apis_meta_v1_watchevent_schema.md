# 1.146. io.k8s.apimachinery.pkg.apis.meta.v1.WatchEvent schema

Description
     Event represents a single event to a watched resource. 
Type
     `object`
Required
    

  * `type`
  * `object`



## 1.146.1. Schema

Property| Type| Description  
---|---|---  
`object` |  [`RawExtension`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/common_object_reference/api-object-reference#io-k8s-apimachinery-pkg-runtime-RawExtension "1.147. io.k8s.apimachinery.pkg.runtime.RawExtension schema") |  Object is: * If Type is Added or Modified: the new state of the object. * If Type is Deleted: the state of the object immediately before deletion. * If Type is Error: *Status is recommended; other types may make sense depending on context.   
`type` |  `string` |   
Show more
