# 1.2. How network policy is evaluated and applied

When a network connection is established, the network provider (default: OVN-Kubernetes) checks the connection details against network policy rules to determine how to handle the connection. 

OVN-Kubernetes evaluates connections against network policy objects in the following order: 

  1. Check for matches in the AdminNetworkPolicy tier. 

     1. If a connection matches an `Allow` or `Deny` rule, follow that rule and stop evaluating. 
     2. If a connection matches a `Pass` rule, move to the NetworkPolicy tier. 

  2. Check for matches in the NetworkPolicy tier. 

     1. If a connection matches a rule, follow that rule and stop evaluating. 
     2. If no match is found, move to the BaselineAdminNetworkPolicy tier. 

  3. Follow a matching rule in the BaselineAdminNetworkPolicy tier. 



**Figure 1.1. Evaluation of network policies by OVN-Kubernetes**

![OVN-Kubernetes Access Control List \(ACL\)](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_security-en-US/images/249735160b08c0b9c9bd53c59101d6bc/615_OpenShift_OVN-K_ACLs_0324.png) ![OVN-Kubernetes Access Control List \(ACL\)](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_security-en-US/images/249735160b08c0b9c9bd53c59101d6bc/615_OpenShift_OVN-K_ACLs_0324.png)
