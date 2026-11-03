# 1.16. StatefulSet [apps/v1]

Description
    

StatefulSet represents a set of pods with consistent identities. Identities are defined as: - Network: A single stable DNS and hostname. - Storage: As many VolumeClaims as requested. 

The StatefulSet guarantees that a given network identity will always map to the same storage identity. 

Type
     `object`
