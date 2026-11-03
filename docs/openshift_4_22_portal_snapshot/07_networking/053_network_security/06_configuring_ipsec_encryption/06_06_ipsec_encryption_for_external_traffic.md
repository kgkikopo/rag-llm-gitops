# 6.6. IPsec encryption for external traffic

OpenShift Container Platform supports the use of IPsec to encrypt traffic destined for external hosts, ensuring confidentiality and integrity of data in transit. This feature relies on X.509 certificates that you must supply. 

## 6.6.1. Supported platforms

This feature is supported on the following platforms: 

  * Bare metal 
  * Google Cloud 
  * Red Hat OpenStack Platform (RHOSP) 
  * VMware vSphere 



Important

If you have Red Hat Enterprise Linux (RHEL) compute nodes, these do not support IPsec encryption for external traffic. 

If your cluster uses hosted control planes for Red Hat OpenShift Container Platform, configuring IPsec for encrypting traffic to external hosts is not supported. 

## 6.6.2. Limitations

Ensure that the following prohibitions are observed: 

  * IPv6 configuration is not currently supported by the NMState Operator when configuring IPsec for external traffic. 
  * Certificate common names (CN) in the provided certificate bundle must not begin with the `ovs_` prefix, because this naming can conflict with pod-to-pod IPsec CN names in the Network Security Services (NSS) database of each node.
