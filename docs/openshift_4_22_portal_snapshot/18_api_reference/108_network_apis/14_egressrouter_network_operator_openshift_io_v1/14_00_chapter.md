# Chapter 14. EgressRouter [network.operator.openshift.io/v1]

Description
    

EgressRouter is a feature allowing the user to define an egress router that acts as a bridge between pods and external systems. The egress router runs a service that redirects egress traffic originating from a pod or a group of pods to a remote external system or multiple destinations as per configuration. 

It is consumed by the cluster-network-operator. More specifically, given an EgressRouter CR with <name>, the CNO will create and manage: - A service called <name> \- An egress pod called <name> \- A NAD called <name>

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

EgressRouter is a single egressrouter pod configuration object. 

Type
     `object`
Required
    

  * `spec`

- [14.1. Specification](14_01_specification.md)
- [14.2. API endpoints](14_02_api_endpoints.md)
