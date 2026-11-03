# Chapter 17. GatewayClass [gateway.networking.k8s.io/v1]

Description
    

GatewayClass describes a class of Gateways available to the user for creating Gateway resources. 

It is recommended that this resource be used as a template for Gateways. This means that a Gateway is based on the state of the GatewayClass at the time it was created and changes to the GatewayClass or associated parameters are not propagated down to existing Gateways. This recommendation is intended to limit the blast radius of changes to GatewayClass or associated parameters. If implementations choose to propagate GatewayClass changes to existing Gateways, that MUST be clearly documented by the implementation. 

Whenever one or more Gateways are using a GatewayClass, implementations SHOULD add the `gateway-exists-finalizer.gateway.networking.k8s.io` finalizer on the associated GatewayClass. This ensures that a GatewayClass associated with a Gateway is not deleted while in use. 

GatewayClass is a Cluster level resource. 

Type
     `object`
Required
    

  * `spec`

- [17.1. Specification](17_01_specification.md)
- [17.2. API endpoints](17_02_api_endpoints.md)
