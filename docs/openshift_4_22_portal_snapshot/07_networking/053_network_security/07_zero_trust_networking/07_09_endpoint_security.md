# 7.9. Endpoint security

It is important to be able to trust that the software running the services in your cluster has not been compromised. For example, you might need to ensure that certified images are run on trusted hardware, and have policies to only allow connections to or from an endpoint based on endpoint characteristics. 

Leverage: 

  * OpenShift Container Platform: Secureboot can ensure that the nodes in the cluster are running trusted software, so the platform itself (including the container runtime) have not been tampered with. You can configure OpenShift Container Platform to only run images that have been [signed by certain signatures](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#security-container-signature). 
  * [Red Hat Trusted Artifact Signer](https://catalog.redhat.com/software/container-stacks/detail/6525b71aa53de2eb01ac9628): This can be used in a trusted build chain and produce signed container images.
