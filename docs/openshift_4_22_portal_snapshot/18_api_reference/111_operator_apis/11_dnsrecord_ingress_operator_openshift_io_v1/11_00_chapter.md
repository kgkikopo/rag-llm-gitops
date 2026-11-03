# Chapter 11. DNSRecord [ingress.operator.openshift.io/v1]

Description
    

DNSRecord is a DNS record managed in the zones defined by dns.config.openshift.io/cluster .spec.publicZone and .spec.privateZone. 

Cluster admin manipulation of this resource is not supported. This resource is only for internal communication of OpenShift operators. 

If DNSManagementPolicy is "Unmanaged", the operator will not be responsible for managing the DNS records on the cloud provider. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`

- [11.1. Specification](11_01_specification.md)
- [11.2. API endpoints](11_02_api_endpoints.md)
