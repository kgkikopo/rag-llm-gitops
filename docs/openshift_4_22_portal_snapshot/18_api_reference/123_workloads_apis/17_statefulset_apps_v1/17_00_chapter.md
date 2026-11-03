# Chapter 17. StatefulSet [apps/v1]

Description
    

StatefulSet represents a set of pods with consistent identities. Identities are defined as: - Network: A single stable DNS and hostname. - Storage: As many VolumeClaims as requested. 

The StatefulSet guarantees that a given network identity will always map to the same storage identity. 

Type
     `object`

- [17.1. Specification](17_01_specification.md)
- [17.2. API endpoints](17_02_api_endpoints.md)
