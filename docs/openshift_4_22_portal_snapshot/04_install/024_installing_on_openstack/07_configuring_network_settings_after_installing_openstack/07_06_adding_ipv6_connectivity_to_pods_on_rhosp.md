# 7.6. Adding IPv6 connectivity to pods on RHOSP

After you enable IPv6 connectivity in pods, add connectivity to the pods by using a Container Network Interface (CNI) configuration. 

**Procedure**

  1. To edit the Cluster Network Operator (CNO), enter the following command: 

```shell-session
$ oc edit networks.operator.openshift.io cluster
```


  2. Specify your CNI configuration under the `spec` field. For example, the following configuration uses a SLAAC address mode with MACVLAN: 

```yaml
...
spec:
  additionalNetworks:
  - name: ipv6
    namespace: ipv6
    rawCNIConfig: '{ "cniVersion": "0.3.1", "name": "ipv6", "type": "macvlan", "master": "ens4"}'
    type: Raw
```


where 

`spec.additionalNetworks.namespace`
     Be sure to create pods in the same namespace. 
`spec.additionalNetworks.rawCNIConfig`
    

The interface in the network attachment `"master"` field can differ from `"ens4"` when more networks are configured or when a different kernel driver is used. 

Note

If you are using stateful address mode, include the IP Address Management (IPAM) in the CNI configuration. 

DHCPv6 is not supported by Multus. 

  3. Save your changes and quit the text editor to commit your changes. 



**Verification**

  * To verify that the IPv6 connectivity was added to pods, enter the following command: 

```shell-session
$ oc get network-attachment-definitions -A
```


**Example output**

```shell-session
NAMESPACE       NAME            AGE
ipv6            ipv6            21h
```


You can now create pods that have secondary IPv6 connections.
