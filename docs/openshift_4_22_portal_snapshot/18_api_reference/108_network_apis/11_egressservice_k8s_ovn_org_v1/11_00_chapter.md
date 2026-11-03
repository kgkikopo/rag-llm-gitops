# Chapter 11. EgressService [k8s.ovn.org/v1]

Description
     EgressService is a CRD that allows the user to request that the source IP of egress packets originating from all of the pods that are endpoints of the corresponding LoadBalancer Service would be its ingress IP. In addition, it allows the user to request that egress packets originating from all of the pods that are endpoints of the LoadBalancer service would use a different network than the main one. 
Type
     `object`

- [11.1. Specification](11_01_specification.md)
- [11.2. API endpoints](11_02_api_endpoints.md)
