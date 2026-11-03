# 6.2. Configure the OVN-Kubernetes masquerade subnet as a postinstallation operation

You can change the masquerade subnet used by OVN-Kubernetes as a postinstallation operation to avoid conflicts with any existing subnets that are already in use in your environment. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Log in to the cluster as a user with `cluster-admin` privileges. 



**Procedure**

  * Change your cluster’s masquerade subnet: 

    * For dual-stack clusters that use IPv6, run the following command: 

```shell-session
$ oc patch networks.operator.openshift.io cluster --type=merge -p '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig":{"ipv4":{"internalMasqueradeSubnet": "<ipv4_masquerade_subnet>"},"ipv6":{"internalMasqueradeSubnet": "<ipv6_masquerade_subnet>"}}}}}}'
```


where: 

`ipv4_masquerade_subnet`
     Specifies an IPv4 address for the masquerade subnet. This range cannot overlap with any other subnet that OpenShift Container Platform or the host uses. In versions of OpenShift Container Platform earlier than 4.17, the default value for IPv4 was `169.254.169.0/29`, and clusters that you upgrade to version 4.17 keep this value. For new clusters starting from version 4.17, the default value is `169.254.0.0/17`. 
`ipv6_masquerade_subnet`
     Specifies an IPv6 address for the masquerade subnet. This range cannot overlap with any other subnet that OpenShift Container Platform or the host uses. The default value for IPv6 is `fd69::/125`. 

    * For clusters that use IPv4, run the following command: 

```shell-session
$ oc patch networks.operator.openshift.io cluster --type=merge -p '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig":{"ipv4":{"internalMasqueradeSubnet": "<ipv4_masquerade_subnet>"}}}}}}'
```


where: 

`ipv4_masquerade_subnet`
     Specifies an IPv4 address for the masquerade subnet. This range cannot overlap with any other subnet that OpenShift Container Platform or the host uses. In versions of OpenShift Container Platform earlier than 4.17, the default value for IPv4 was `169.254.169.0/29`, and clusters that you upgrade to version 4.17 keep this value. For new clusters starting from version 4.17, the default value is `169.254.0.0/17`.
