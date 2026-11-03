# Chapter 2. Use cases for a secondary network

You can use a secondary network in situations where you require network isolation, including data plane and control plane separation. 

Isolating network traffic is useful for the following performance and security reasons: 

  * Performance 

**Traffic management** : You can send traffic on two different planes to manage how much traffic is along each plane. 

  * Security 

**Network isolation** : You can send sensitive traffic onto a network plane that is managed specifically for security considerations, and you can separate private data that must not be shared between tenants or customers. 




All of the pods in the cluster still use the cluster-wide default network to maintain connectivity across the cluster. Every pod has an `eth0` interface that is attached to the cluster-wide pod network. You can view the interfaces for a pod by using the `oc exec -it <pod_name> -- ip a` command. If you add secondary network interfaces that use the Multus Container Network Interface (CNI). These secondary networks are named `net1`, `net2`, and so on. 

To attach secondary network interfaces to a pod, you must create configurations that define how the interfaces are attached. Use either a `UserDefinedNetwork` custom resource (CR) or a `NetworkAttachmentDefinition` CR to specify each interface. A CNI configuration inside each of these CRs defines how that interface is created.

- [2.1. Secondary networks in OpenShift Container Platform](02_01_secondary_networks_in_openshift_container_platform.md)
- [2.2. UserDefinedNetwork and NetworkAttachmentDefinition support matrix](02_02_userdefinednetwork_and_networkattachmentdefinition_support_matrix.md)
- [2.3. Additional resources](02_03_additional_resources.md)
