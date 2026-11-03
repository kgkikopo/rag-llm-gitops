# 3.15. cert-manager Operator

The cert-manager Operator for OpenShift Container Platform manages the lifecycle of TLS certificates for cluster components and workloads. 

New in this release
    

  * The cert-manager Operator is a new optional component in this release. 



Description
     The cert-manager Operator for OpenShift Container Platform manages the lifecycle of TLS certificates for cluster components and workloads. The cert-manager Operator automates certificate issuance, renewal, and rotation, eliminating manual certificate management. The reference configuration includes the cert-manager Operator to optionally manage certificates for the API server and ingress controller endpoints. 
Limits and requirements
    

  * The reference configuration includes only the ACME DNS01 challenge type for platform certificate issuance. 



Engineering considerations
    

  * Use RHACM `CertificatePolicy` resources on the hub cluster to monitor certificate expiration and compliance across managed clusters.
