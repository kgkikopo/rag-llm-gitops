# 4.1. Machine CIDR

In the Machine classless inter-domain routing (CIDR) field, you must specify the IP address range for machines or cluster nodes. 

Note

You cannot change Machine CIDR ranges after you create your cluster. 

The default is `10.0.0.0/16`. This range must not conflict with any connected networks. 

**Additional resources**

  * [Cluster Network Operator configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#nw-operator-cr_cluster-network-operator)
