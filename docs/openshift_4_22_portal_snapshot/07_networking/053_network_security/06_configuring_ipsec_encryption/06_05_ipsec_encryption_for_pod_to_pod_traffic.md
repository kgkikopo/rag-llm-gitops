# 6.5. IPsec encryption for pod-to-pod traffic

IPsec encryption of pod-to-pod traffic covers which traffic is encrypted, which protocol is used, and how X.509 certificates are handled. 

IPsec encryption between the cluster and external hosts requires manual configuration for your specific external network infrastructure. 

## 6.5.1. Types of network traffic flows encrypted by pod-to-pod IPsec

When pod-to-pod IPsec is enabled in OpenShift Container Platform, OVN-Kubernetes encrypts only selected traffic flows between pods on different nodes and from host-network pods. Other flows, such as traffic on the same node, remain unencrypted. 

The following network traffic flows between pods are encrypted when pod-to-pod IPsec is enabled: 

  * Traffic between pods on different nodes on the cluster network 
  * Traffic from a pod on the host network to a pod on the cluster network 



The following traffic flows are not encrypted when pod-to-pod IPsec is enabled: * Traffic between pods on the same node on the cluster network * Traffic between pods on the host network * Traffic from a pod on the cluster network to a pod on the host network 

The encrypted and unencrypted flows are illustrated in the following diagram: 

![IPsec encrypted and unencrypted traffic flows](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_security-en-US/images/84757edea0d11c95de018b57280f88ed/nw-ipsec-encryption.png) ![IPsec encrypted and unencrypted traffic flows](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Network_security-en-US/images/84757edea0d11c95de018b57280f88ed/nw-ipsec-encryption.png)

## 6.5.2. Encryption protocol and IPsec mode

Pod-to-pod IPsec in OpenShift Container Platform uses `AES-GCM-16-256` in transport mode with a 256-bit key and a 16-byte integrity check value (ICV). 

_Transport mode_ encrypts end-to-end communication by adding an Encapsulated Security Payload (ESP) header to the IP header of the original packet and encrypts the packet data. 

OpenShift Container Platform does not currently use or support IPsec _Tunnel mode_ for pod-to-pod communication. 

## 6.5.3. Security certificate generation and rotation

The Cluster Network Operator (CNO) generates a self-signed X.509 certificate authority (CA) that is used by IPsec for encryption. Certificate signing requests (CSRs) from each node are automatically fulfilled by the CNO. 

The CA is valid for 10 years. The individual node certificates are valid for 5 years and are automatically rotated after 4 1/2 years elapse.
