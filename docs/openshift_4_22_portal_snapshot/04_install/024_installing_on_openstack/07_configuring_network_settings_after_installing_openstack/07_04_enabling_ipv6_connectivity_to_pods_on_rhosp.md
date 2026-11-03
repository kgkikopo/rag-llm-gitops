# 7.4. Enabling IPv6 connectivity to pods on RHOSP

To enable IPv6 connectivity between pods on additional networks across different nodes, disable port security for the IPv6 port of the server. 

Disabling port security removes the need to create allowed address pairs for each IPv6 address assigned to pods and enables traffic on the security group. 

Important

Only the following IPv6 additional network configurations are supported: 

  * SLAAC and host-device 
  * SLAAC and MACVLAN 
  * DHCP stateless and host-device 
  * DHCP stateless and MACVLAN 



**Procedure**

  * To disable port security for the IPv6 port of the server, enter the following command: 

```shell-session
$ openstack port set --no-security-group --disable-port-security <compute_ipv6_port>
```


Replace `<compute_ipv6_port>` with the IPv6 port of the compute server. 

Important

This command removes security groups from the port and disables port security. Traffic restrictions are removed entirely from the port.
