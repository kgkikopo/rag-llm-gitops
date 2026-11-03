# 6.2. Prerequisites for IPsec encryption for external traffic

The following prerequisites are required to add certificates into the host NSS database and to configure IPsec to communicate with external hosts. 

  * Set `routingViaHost=true` in the `ovnKubernetesConfig.gatewayConfig` specification of the OVN-Kubernetes network plugin. 
  * Install the NMState Operator. This Operator is required for specifying the IPsec configuration. For more information, see "Kubernetes NMState Operator". 

Note

The NMState Operator is supported on Google Cloud only for configuring IPsec.
