# Chapter 4. AdminPolicyBasedExternalRoute [k8s.ovn.org/v1]

Description
     AdminPolicyBasedExternalRoute is a CRD allowing the cluster administrators to configure policies for external gateway IPs to be applied to all the pods contained in selected namespaces. Egress traffic from the pods that belong to the selected namespaces to outside the cluster is routed through these external gateway IPs. 
Type
     `object`
Required
    

  * `spec`

- [4.1. Specification](04_01_specification.md)
- [4.2. API endpoints](04_02_api_endpoints.md)
