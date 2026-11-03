# Chapter 9. SecurityContextConstraints [security.openshift.io/v1]

Description
    

SecurityContextConstraints governs the ability to make requests that affect the SecurityContext that will be applied to a container. For historical reasons SCC was exposed under the core Kubernetes API group. That exposure is deprecated and will be removed in a future release - users should instead use the security.openshift.io group to manage SecurityContextConstraints. 

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer). 

Type
     `object`
Required
    

  * `allowHostDirVolumePlugin`
  * `allowHostIPC`
  * `allowHostNetwork`
  * `allowHostPID`
  * `allowHostPorts`
  * `allowPrivilegedContainer`
  * `readOnlyRootFilesystem`

- [9.1. Specification](09_01_specification.md)
- [9.2. API endpoints](09_02_api_endpoints.md)
