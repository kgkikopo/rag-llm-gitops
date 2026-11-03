# 4.12. Network configuration phases

You can customize your OpenShift Container Platform network plugin configuration, such as cluster network CIDR and service network ranges, during two phases before installation to integrate with your existing network environment. 

Phase 1
    

You can customize the following network-related fields in the `install-config.yaml` file before you create the manifest files: 

  * `networking.networkType`
  * `networking.clusterNetwork`
  * `networking.serviceNetwork`
  * `networking.machineNetwork`
  * `nodeNetworking`

For more information, see "Installation configuration parameters". 

Note

Set the `networking.machineNetwork` to match the Classless Inter-Domain Routing (CIDR) where the preferred subnet is located. 

Important

The CIDR range `172.17.0.0/16` is reserved by `libVirt`. You cannot use any other CIDR range that overlaps with the `172.17.0.0/16` CIDR range for networks in your cluster. 




Phase 2
     After creating the manifest files by running `openshift-install create manifests`, you can define a customized Cluster Network Operator manifest with only the fields you want to modify. You can use the manifest to specify an advanced network configuration. 

During phase 2, you cannot override the values that you specified in phase 1 in the `install-config.yaml` file. However, you can customize the network plugin during phase 2.
