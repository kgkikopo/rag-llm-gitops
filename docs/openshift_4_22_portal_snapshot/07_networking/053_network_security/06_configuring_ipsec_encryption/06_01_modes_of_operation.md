# 6.1. Modes of operation

You can configure IPsec on OpenShift Container Platform clusters in `Disabled`, `External`, or `Full` pod-to-pod and external encryption modes. Each mode determines which traffic OVN-Kubernetes encrypts by default. 

The following table describes the different modes of operation: 

Table 6.1. IPsec modes of operationMode| Description| Default  
---|---|---  
`Disabled` |  No traffic is encrypted. This is the cluster default.  |  Yes   
`Full` |  Pod-to-pod traffic is encrypted as described in "Types of network traffic flows encrypted by pod-to-pod IPsec". Traffic to external nodes may be encrypted after you complete the required configuration steps for IPsec.  |  No   
`External` |  Traffic to external nodes may be encrypted after you complete the required configuration steps for IPsec.  |  No   
Show more
