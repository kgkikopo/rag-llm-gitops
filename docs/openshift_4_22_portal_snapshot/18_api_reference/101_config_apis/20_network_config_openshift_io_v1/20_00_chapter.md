# Chapter 20. Network [config.openshift.io/v1]

Description
    

Network holds cluster-wide information about Network. The canonical name is `cluster`. It is used to configure the desired network configuration, such as: IP address pools for services/pod IPs, network plugin, etc. Please view network.spec for an explanation on what applies when configuring this resource. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `spec`

- [20.1. Specification](20_01_specification.md)
- [20.2. API endpoints](20_02_api_endpoints.md)
