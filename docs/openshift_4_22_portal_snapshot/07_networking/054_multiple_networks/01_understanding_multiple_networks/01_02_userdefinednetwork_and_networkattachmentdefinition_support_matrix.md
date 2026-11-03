# 1.2. UserDefinedNetwork and NetworkAttachmentDefinition support matrix

You can use user defined networks and network attachment definitions to define and configure customized networks for your needs. 

By creating `UserDefinedNetwork` and `NetworkAttachmentDefinition` custom resources (CRs), cluster administrators can complete the following tasks: 

  * Create customizable network configurations 
  * Define their own network topologies 
  * Ensure network isolation 
  * Manage IP addressing for workloads 
  * Configure advanced network features 



By creating a `ClusterUserDefinedNetwork` CR, administrators can create and define secondary networks that span multiple namespaces at the cluster level. 

User-defined networks and network attachment definitions can serve as both the primary and secondary network interface, and each support `layer2` and `layer3` topologies. 

Note

As of OpenShift Container Platform 4.19, the use of the `Localnet` topology by `ClusterUserDefinedNetwork` CRs is generally available. This configuration is the preferred method for connecting physical networks to virtual networks. Or, you can use the `NetworkAttachmentDefinition` CR to create secondary networks with `Localnet` topologies. 

The following section highlights the supported features of the `UserDefinedNetwork` and `NetworkAttachmentDefinition` CRs when used as either the primary or secondary network. A separate table for the `ClusterUserDefinedNetwork` CR is also included. 

Table 1.1. Primary network support matrix for UserDefinedNetwork and NetworkAttachmentDefinition CRsNetwork feature| Layer2 topology| Layer3 topology  
---|---|---  
east-west traffic  |  ✓  |  ✓   
north-south traffic  |  ✓  |  ✓   
Persistent IPs  |  ✓  |  X   
Services  |  ✓  |  ✓   
Routes  |  X  |  X   
`EgressIP` resource  |  ✓  |  ✓   
Multicast  |  X  |  ✓   
`NetworkPolicy` resource  |  ✓  |  ✓   
`MultinetworkPolicy` resource  |  X  |  X   
Show more

where: 

Multicast
     Must be enabled in the namespace, and it is only available between OVN-Kubernetes network pods. For more information, see "About multicast". 
`NetworkPolicy` resource
     When creating a `ClusterUserDefinedNetwork` CR with a primary network type, network policies must be created _after_ the `UserDefinedNetwork` CR. 

Table 1.2. Secondary network support matrix for UserDefinedNetwork and NetworkAttachmentDefinition CRsNetwork feature| Layer2 topology| Layer3 topology| Localnet topology  
---|---|---|---  
east-west traffic  |  ✓  |  ✓  |  ✓ (`NetworkAttachmentDefinition` CR only)   
north-south traffic  |  X  |  X  |  ✓ (`NetworkAttachmentDefinition` CR only)   
Persistent IPs  |  ✓  |  X  |  ✓ (`NetworkAttachmentDefinition` CR only)   
Services  |  X  |  X  |  X   
Routes  |  X  |  X  |  X   
`EgressIP` resource  |  X  |  X  |  X   
Multicast  |  X  |  X  |  X   
`NetworkPolicy` resource  |  X  |  X  |  X   
`MultinetworkPolicy` resource  |  ✓  |  ✓  |  ✓ (`NetworkAttachmentDefinition` CR only)   
Show more

The Localnet topology is unavailable for use with the `UserDefinedNetwork` CR. It is only supported on secondary networks for `NetworkAttachmentDefinition` CRs. 

Table 1.3. Support matrix for ClusterUserDefinedNetwork CRsNetwork feature| Layer2 topology| Layer3 topology| Localnet topology  
---|---|---|---  
east-west traffic  |  ✓  |  ✓  |  ✓   
north-south traffic  |  ✓  |  ✓  |  ✓   
Persistent IPs  |  ✓  |  X  |  ✓   
Services  |  ✓  |  ✓  |   
Routes  |  X  |  X  |   
`EgressIP` resource  |  ✓  |  ✓  |   
Multicast  |  X  |  ✓  |   
`MultinetworkPolicy` resource  |  X  |  X  |  ✓   
`NetworkPolicy` resource  |  ✓  |  ✓  |   
Show more

where: 

Multicast
     must be enabled in the namespace, and it is only available between OVN-Kubernetes network pods. For more information, see "About multicast". 
`NetworkPolicy` resource
     When creating a `ClusterUserDefinedNetwork` CR with a primary network type, network policies must be created _after_ the `UserDefinedNetwork` CR.
