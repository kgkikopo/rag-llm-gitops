# Chapter 15. GRPCRoute [gateway.networking.k8s.io/v1]

Description
    

GRPCRoute provides a way to route gRPC requests. This includes the capability to match requests by hostname, gRPC service, gRPC method, or HTTP/2 header. Filters can be used to specify additional processing steps. Backends specify where matching requests will be routed. 

GRPCRoute falls under extended support within the Gateway API. Within the following specification, the word "MUST" indicates that an implementation supporting GRPCRoute must conform to the indicated requirement, but an implementation not supporting this route type need not follow the requirement unless explicitly indicated. 

Implementations supporting `GRPCRoute` with the `HTTPS` `ProtocolType` MUST accept HTTP/2 connections without an initial upgrade from HTTP/1.1, i.e. via ALPN. If the implementation does not support this, then it MUST set the "Accepted" condition to "False" for the affected listener with a reason of "UnsupportedProtocol". Implementations MAY also accept HTTP/2 connections with an upgrade from HTTP/1. 

Implementations supporting `GRPCRoute` with the `HTTP` `ProtocolType` MUST support HTTP/2 over cleartext TCP (h2c, <https://www.rfc-editor.org/rfc/rfc7540#section-3.1>) without an initial upgrade from HTTP/1.1, i.e. with prior knowledge (<https://www.rfc-editor.org/rfc/rfc7540#section-3.4>). If the implementation does not support this, then it MUST set the "Accepted" condition to "False" for the affected listener with a reason of "UnsupportedProtocol". Implementations MAY also accept HTTP/2 connections with an upgrade from HTTP/1, i.e. without prior knowledge. 

Type
     `object`
Required
    

  * `spec`

- [15.1. Specification](15_01_specification.md)
- [15.2. API endpoints](15_02_api_endpoints.md)
