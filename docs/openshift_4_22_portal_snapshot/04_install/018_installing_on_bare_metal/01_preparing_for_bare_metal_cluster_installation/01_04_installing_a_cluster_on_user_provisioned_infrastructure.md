# 1.4. Installing a cluster on user-provisioned infrastructure

You can install a cluster on bare-metal infrastructure that you provision, by using one of the following methods: 

**Installing a user-provisioned cluster on bare metal**
     You can install OpenShift Container Platform on bare-metal infrastructure that you provision. For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines. 
**Installing a user-provisioned bare-metal cluster with network customizations**
     You can install a bare-metal cluster on user-provisioned infrastructure with network-customizations. By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations. Most of the network customizations must be applied at the installation stage. 
**Installing a user-provisioned bare-metal cluster on a restricted network**
     You can install a user-provisioned bare-metal cluster on a restricted or disconnected network by using a mirror registry. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.
