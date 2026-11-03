# 6.27. Machine Config Operator

The Machine Config Operator manages and applies configuration and updates of the base operating system and container runtime, including everything between the kernel and kubelet. 

There are four components: 

  * `machine-config-server`: Provides Ignition configuration to new machines joining the cluster. 
  * `machine-config-controller`: Coordinates the upgrade of machines to the desired configurations defined by a `MachineConfig` object. Options are provided to control the upgrade for sets of machines individually. 
  * `machine-config-daemon`: Applies new machine configuration during update. Validates and verifies the state of the machine to the requested machine configuration. 
  * `machine-config`: Provides a complete source of machine configuration at installation, first start up, and updates for a machine. 



Important

Currently, there is no supported way to block or restrict the machine config server endpoint. The machine config server must be exposed to the network so that newly-provisioned machines, which have no existing configuration or state, are able to fetch their configuration. In this model, the root of trust is the certificate signing requests (CSR) endpoint, which is where the kubelet sends its certificate signing request for approval to join the cluster. Because of this, machine configs should not be used to distribute sensitive information, such as secrets and certificates. 

To ensure that the machine config server endpoints, ports 22623 and 22624, are secured in bare metal scenarios, customers must configure proper network policies. 

**Additional resources**

  * [openshift-machine-config-operator](https://github.com/openshift/machine-config-operator)
