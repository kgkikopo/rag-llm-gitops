# 12.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`subsets` |  `array` |  The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service.   
`subsets[]` |  `object` |  EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given:  { Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}], Ports: [{"name": "a", "port": 8675}, {"name": "b", "port": 309}] }  The resulting set of endpoints can be viewed as:  a: [ 10.10.1.1:8675, 10.10.2.2:8675 ], b: [ 10.10.1.1:309, 10.10.2.2:309 ]  Deprecated: This API is deprecated in v1.33+.   
Show more

## 12.1.1. .subsets

Description
     The set of all endpoints is the union of all subsets. Addresses are placed into subsets according to the IPs they share. A single address with multiple ports, some of which are ready and some of which are not (because they come from different containers) will result in the address being displayed in different subsets for the different ports. No address will appear in both Addresses and NotReadyAddresses in the same subset. Sets of addresses and ports that comprise a service. 
Type
     `array`

## 12.1.2. .subsets[]

Description
    

EndpointSubset is a group of addresses with a common set of ports. The expanded set of endpoints is the Cartesian product of Addresses x Ports. For example, given: 

```plaintext
{
  Addresses: [{"ip": "10.10.1.1"}, {"ip": "10.10.2.2"}],
  Ports:     [{"name": "a", "port": 8675}, {"name": "b", "port": 309}]
}
```


The resulting set of endpoints can be viewed as: 

```plaintext
a: [ 10.10.1.1:8675, 10.10.2.2:8675 ],
b: [ 10.10.1.1:309, 10.10.2.2:309 ]
```


Deprecated: This API is deprecated in v1.33+. 

Type
     `object`

Property| Type| Description  
---|---|---  
`addresses` |  `array` |  IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize.   
`addresses[]` |  `object` |  EndpointAddress is a tuple that describes single IP address. Deprecated: This API is deprecated in v1.33+.   
`notReadyAddresses` |  `array` |  IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check.   
`notReadyAddresses[]` |  `object` |  EndpointAddress is a tuple that describes single IP address. Deprecated: This API is deprecated in v1.33+.   
`ports` |  `array` |  Port numbers available on the related IP addresses.   
`ports[]` |  `object` |  EndpointPort is a tuple that describes a single port. Deprecated: This API is deprecated in v1.33+.   
Show more

## 12.1.3. .subsets[].addresses

Description
     IP addresses which offer the related ports that are marked as ready. These endpoints should be considered safe for load balancers and clients to utilize. 
Type
     `array`

## 12.1.4. .subsets[].addresses[]

Description
     EndpointAddress is a tuple that describes single IP address. Deprecated: This API is deprecated in v1.33+. 
Type
     `object`
Required
    

  * `ip`



Property| Type| Description  
---|---|---  
`hostname` |  `string` |  The Hostname of this endpoint   
`ip` |  `string` |  The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16).   
`nodeName` |  `string` |  Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node.   
`targetRef` |  `object` |  ObjectReference contains enough information to let you inspect or modify the referred object.   
Show more

## 12.1.5. .subsets[].addresses[].targetRef

Description
     ObjectReference contains enough information to let you inspect or modify the referred object. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`fieldPath` |  `string` |  If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`namespace` |  `string` |  Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>  
`resourceVersion` |  `string` |  Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency>  
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids>  
Show more

## 12.1.6. .subsets[].notReadyAddresses

Description
     IP addresses which offer the related ports but are not currently marked as ready because they have not yet finished starting, have recently failed a readiness check, or have recently failed a liveness check. 
Type
     `array`

## 12.1.7. .subsets[].notReadyAddresses[]

Description
     EndpointAddress is a tuple that describes single IP address. Deprecated: This API is deprecated in v1.33+. 
Type
     `object`
Required
    

  * `ip`



Property| Type| Description  
---|---|---  
`hostname` |  `string` |  The Hostname of this endpoint   
`ip` |  `string` |  The IP of this endpoint. May not be loopback (127.0.0.0/8 or ::1), link-local (169.254.0.0/16 or fe80::/10), or link-local multicast (224.0.0.0/24 or ff02::/16).   
`nodeName` |  `string` |  Optional: Node hosting this endpoint. This can be used to determine endpoints local to a node.   
`targetRef` |  `object` |  ObjectReference contains enough information to let you inspect or modify the referred object.   
Show more

## 12.1.8. .subsets[].notReadyAddresses[].targetRef

Description
     ObjectReference contains enough information to let you inspect or modify the referred object. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`fieldPath` |  `string` |  If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`namespace` |  `string` |  Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>  
`resourceVersion` |  `string` |  Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency>  
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids>  
Show more

## 12.1.9. .subsets[].ports

Description
     Port numbers available on the related IP addresses. 
Type
     `array`

## 12.1.10. .subsets[].ports[]

Description
     EndpointPort is a tuple that describes a single port. Deprecated: This API is deprecated in v1.33+. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`appProtocol` |  `string` |  The application protocol for this port. This is used as a hint for implementations to offer richer behavior for protocols that they understand. This field follows standard Kubernetes label syntax. Valid values are either:  * Un-prefixed protocol names - reserved for IANA standard service names (as per RFC-6335 and <https://www.iana.org/assignments/service-names>).  * Kubernetes-defined prefixed names: * 'kubernetes.io/h2c' - HTTP/2 prior knowledge over cleartext as described in <https://www.rfc-editor.org/rfc/rfc9113.html#name-starting-http-2-with-prior-> * 'kubernetes.io/ws' - WebSocket over cleartext as described in <https://www.rfc-editor.org/rfc/rfc6455> * 'kubernetes.io/wss' - WebSocket over TLS as described in <https://www.rfc-editor.org/rfc/rfc6455> * Other protocols should use implementation-defined prefixed names such as mycompany.com/my-custom-protocol.   
`name` |  `string` |  The name of this port. This must match the 'name' field in the corresponding ServicePort. Must be a DNS_LABEL. Optional only if one port is defined.   
`port` |  `integer` |  The port number of the endpoint.   
`protocol` |  `string` |  The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.  Possible enum values: - `"SCTP"` is the SCTP protocol. - `"TCP"` is the TCP protocol. - `"UDP"` is the UDP protocol.   
Show more
