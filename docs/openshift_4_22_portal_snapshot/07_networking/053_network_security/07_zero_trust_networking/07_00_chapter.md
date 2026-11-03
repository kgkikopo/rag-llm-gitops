# Chapter 7. Zero trust networking

Zero trust is an approach to designing security architectures based on the premise that every interaction begins in an untrusted state. This contrasts with traditional architectures, which might determine trustworthiness based on whether communication starts inside a firewall. More specifically, zero trust attempts to close gaps in security architectures that rely on implicit trust models and one-time authentication. 

OpenShift Container Platform can add some zero trust networking capabilities to containers running on the platform without requiring changes to the containers or the software running in them. There are also several products that Red Hat offers that can further augment the zero trust networking capabilities of containers. If you have the ability to change the software running in the containers, then there are other projects that Red Hat supports that can add further capabilities. 

Explore the following targeted capabilities of zero trust networking.

- [7.1. Root of trust](07_01_root_of_trust.md)
- [7.2. Traffic authentication and encryption](07_02_traffic_authentication_and_encryption.md)
- [7.3. Identification and authentication](07_03_identification_and_authentication.md)
- [7.4. Inter-service authorization](07_04_inter_service_authorization.md)
- [7.5. Transaction-level verification](07_05_transaction_level_verification.md)
- [7.6. Risk assessment](07_06_risk_assessment.md)
- [7.7. Site-wide policy enforcement and distribution](07_07_site_wide_policy_enforcement_and_distribution.md)
- [7.8. Observability for constant, and retrospective, evaluation](07_08_observability_for_constant_and_retrospective_evaluation.md)
- [7.9. Endpoint security](07_09_endpoint_security.md)
- [7.10. Extending trust outside of the cluster](07_10_extending_trust_outside_of_the_cluster.md)
