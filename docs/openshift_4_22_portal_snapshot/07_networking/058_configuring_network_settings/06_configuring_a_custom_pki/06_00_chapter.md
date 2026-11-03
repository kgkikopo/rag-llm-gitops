# Chapter 6. Configuring a custom PKI

To ensure secure communication between internal components in your OpenShift Container Platform cluster, you can add your organization’s custom Certificate Authority (CA) certificates to the cluster-wide truststore. 

You can add your custom CA certificates to the cluster-wide truststore in one of two ways: 

  * During cluster installation, by adding your CA certificate to the `install-config.yaml` file. 
  * On a running cluster, by creating a `ConfigMap` object that contains your CA certificate and referencing it in the cluster `Proxy` object. 



Important

The cluster Proxy object is the mechanism for managing the cluster-wide truststore. This guide focuses only on the task of adding a CA. If you also need to configure an egress proxy, refer to the "Configuring the cluster-wide proxy" chapter for detailed instructions.

- [6.1. Adding a custom CA during cluster installation](06_01_adding_a_custom_ca_during_cluster_installation.md)
- [6.2. Adding a custom CA to a running cluster](06_02_adding_a_custom_ca_to_a_running_cluster.md)
- [6.3. Verifying the custom CA configuration](06_03_verifying_the_custom_ca_configuration.md)
- [6.4. Certificate injection using Operators](06_04_certificate_injection_using_operators.md)
