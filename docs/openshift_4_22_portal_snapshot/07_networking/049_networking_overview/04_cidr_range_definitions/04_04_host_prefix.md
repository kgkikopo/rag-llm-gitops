# 4.4. Host prefix

In the `hostPrefix` parameter, you must specify the subnet prefix length assigned to pods scheduled to individual machines. The host prefix determines the pod IP address pool for each machine. 

For example, if the host prefix is set to `/23`, each machine is assigned a `/23` subnet from the pod CIDR address range. The default is `/23`, allowing 510 cluster nodes and 510 pod IP addresses per node. 

Consider another example where you set the `clusterNetwork.cidr` parameter to `10.128.0.0/16`, you define the complete address space for the cluster. This assigns a pool of 65,536 IP addresses to your cluster. If you then set the `hostPrefix` parameter to `/23`, you define a subnet slice to each node in the cluster, where the `/23` slice becomes a subnet of the `/16` subnet network. This assigns 512 IP addresses to each node, where 2 IP addresses get reserved for networking and broadcasting purposes. The following example calculation uses these IP address figures to determine the maximum number of nodes that you can create for your cluster: 

```plaintext
65536 / 512 = 128
```


## 4.4.1. Additional resources

  * [Red Hat OpenShift Network Calculator: calculate the maximum number of nodes for your cluster](https://access.redhat.com/labs/ocpnc/)
