# 3.1. Ethernet device configuration object

You can configure an Ethernet network device by defining an `SriovNetwork` object. 

The following YAML describes an `SriovNetwork` object: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: <name>
  namespace: openshift-sriov-network-operator
spec:
  resourceName: <sriov_resource_name>
  networkNamespace: <target_namespace>
  vlan: <vlan>
  spoofChk: "<spoof_check>"
  ipam: |-
    {}
  linkState: <link_state>
  maxTxRate: <max_tx_rate>
  minTxRate: <min_tx_rate>
  vlanQoS: <vlan_qos>
  trust: "<trust_vf>"
  capabilities: <capabilities>
```


`metadata.name`
     Specifies a name for the object. The SR-IOV Network Operator creates a `NetworkAttachmentDefinition` object with same name. 
`metadata.namespace`
     Specifies the namespace where the SR-IOV Network Operator is installed. You can also install the SR-IOV Network Operator in any namespace. 
`spec.resourceName`
     Specifies the value for the `spec.resourceName` parameter from the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network. 
`spec.networkNamespace`
     Specifies the target namespace for the `SriovNetwork` object. Only pods in the target namespace can attach to the additional network. When installing the SR-IOV Network Operator in a namespace other than `openshift-sriov-network-operator`, you must not configure this field. 
`spec.vlan`
     Optional: Specifies the VLAN ID to assign to an additional network. The default value of `0` means that an additional network has no VLAN ID tag. Supported VLAN ID values range from `1` to `4094`. 
`spec.spoofChk`
    

Optional: Specifies the spoof check mode of the VF. The allowed values are the strings `"on"` and `"off"`. 

Important

You must enclose the value you specify in quotes or the object is rejected by the SR-IOV Network Operator. 

`spec.ipam`
     Specifies a configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition. 
`spec.linkState`
     Optional: Specifies the link state of virtual function (VF). Allowed values are `enable`, `disable`, and `auto`. 
`spec.maxTxRate`
     Optional: Specifies a maximum transmission rate, in Mbps, for the VF. 
`spec.minTxRate`
    

Optional: Specifies a minimum transmission rate, in Mbps, for the VF. This value must be less than or equal to the maximum transmission rate. 

Note

Intel NICs do not support the `minTxRate` parameter. For more information, see [BZ#1772847](https://bugzilla.redhat.com/show_bug.cgi?id=1772847). 

`spec.vlanQoS`
     Optional: Specifies an IEEE 802.1p priority level for the VF. The default value is `0`. 
`spec.trust`
    

Optional: Specifies the trust mode of the VF. The allowed values are the strings `"on"` and `"off"`. 

Important

You must enclose the value that you specify in quotes, or the SR-IOV Network Operator rejects the object. 

`spec.capabilities`
     Optional: Specifies the capabilities to configure for this additional network. You can specify `'{ "ips": true }'` to enable IP address support or `'{ "mac": true }'` to enable MAC address support. 

**Additional resources**

  * [Installing the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator)
  * [Configuring namespaced SR-IOV resources](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hardware_networks/configuring-namespaced-sriov-resources#introduction-to-namespaced-sriovnetwork-resources_configuring-namespaced-sriov-resources "5.1. An introduction to namespaced SriovNetwork resources")



## 3.1.1. Create a configuration for assignment of dual-stack IP addresses dynamically

You can dynamically assign dual-stack IP addresses to a secondary network so that pods can communicate over both IPv4 and IPv6 addresses. 

You can configure the following IP address assignment types in the `ipRanges` parameter: 

  * IPv4 addresses 
  * IPv6 addresses 
  * multiple IP address assignment 



**Procedure**

  1. Set `type` to `whereabouts`. 
  2. Use `ipRanges` to allocate IP addresses as shown in the following example: 

```yaml
cniVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  additionalNetworks:
  - name: whereabouts-shim
    namespace: default
    type: Raw
    rawCNIConfig: |-
      {
       "name": "whereabouts-dual-stack",
       "cniVersion": "0.3.1,
       "type": "bridge",
       "ipam": {
         "type": "whereabouts",
         "ipRanges": [
                  {"range": "192.168.10.0/24"},
                  {"range": "2001:db8::/64"}
              ]
       }
      }
```


  3. Attach the secondary network to a pod. For more information, see "Adding a pod to a secondary network". 



**Verification**

  * Verify that all IP addresses got assigned to the network interfaces within the network namespace of a pod by entering the following command: 

```yaml
$ oc exec -it <pod_name> -- ip a
```


where: 

`<pod_name>`
     The name of the pod. 




## 3.1.2. Configuration of IP address assignment for a network attachment

For secondary networks, you can assign IP addresses by using an IP Address Management (IPAM) CNI plugin, which supports various assignment methods, including Dynamic Host Configuration Protocol (DHCP) and static assignment. 

The DHCP IPAM CNI plugin responsible for dynamic assignment of IP addresses operates with two distinct components: 

  * CNI Plugin: Responsible for integrating with the Kubernetes networking stack to request and release IP addresses. 
  * DHCP IPAM CNI Daemon: A listener for DHCP events that coordinates with existing DHCP servers in the environment to handle IP address assignment requests. This daemon is not a DHCP server itself. 



For networks requiring `type: dhcp` in their IPAM configuration, ensure the DHCP server meets the following conditions: 

  * A DHCP server is available and running in the environment. 
  * The DHCP server is external to the cluster and you expect the server to form part of the existing network infrastructure for the customer. 
  * The DHCP server is appropriately configured to serve IP addresses to the nodes. 



In cases where a DHCP server is unavailable in the environment, consider using the Whereabouts IPAM CNI plugin. The Whereabouts CNI provides similar IP address management capabilities without the need for an external DHCP server. 

Note

Use the Whereabouts CNI plugin when no external DHCP server exists or where static IP address management is preferred. The Whereabouts plugin includes a reconciler daemon to manage stale IP address allocations. 

Ensure the periodic renewal of a DHCP lease throughout the lifetime of a container by including a separate daemon, the DHCP IPAM CNI Daemon. To deploy the DHCP IPAM CNI daemon, change the Cluster Network Operator (CNO) configuration to trigger the deployment of this daemon as part of the secondary network setup. 

### 3.1.2.1. Static IP address assignment configuration

The following table describes the configuration for static IP address assignment: 

Table 3.1. ipam static configuration objectField| Type| Description  
---|---|---  
`type` |  `string` |  The IPAM address type. The value `static` is required.   
`addresses` |  `array` |  An array of objects specifying IP addresses to assign to the virtual interface. Both IPv4 and IPv6 IP addresses are supported.   
`routes` |  `array` |  An array of objects specifying routes to configure inside the pod.   
`dns` |  `array` |  Optional: An array of objects specifying the DNS configuration.   
Show more

The `addresses` array requires objects with the following fields: 

Table 3.2. ipam.addresses[] arrayField| Type| Description  
---|---|---  
`address` |  `string` |  An IP address and network prefix that you specify. For example, if you specify `10.10.21.10/24`, the secondary network gets assigned an IP address of `10.10.21.10` and the subnet mask of `255.255.255.0`.   
`gateway` |  `string` |  The default gateway to route egress network traffic to.   
Show more

Table 3.3. ipam.routes[] arrayField| Type| Description  
---|---|---  
`dst` |  `string` |  The IP address range in CIDR format, such as `192.168.17.0/24` or `0.0.0.0/0` for the default route.   
`gw` |  `string` |  The gateway that routes network traffic.   
Show more

Table 3.4. ipam.dns objectField| Type| Description  
---|---|---  
`nameservers` |  `array` |  An array of one or more IP addresses where DNS queries get sent.   
`domain` |  `array` |  The default domain to append to a hostname. For example, if the domain is set to `example.com`, a DNS lookup query for `example-host` is rewritten as `example-host.example.com`.   
`search` |  `array` |  An array of domain names to append to an unqualified hostname, such as `example-host`, during a DNS lookup query.   
Show more

**Static IP address assignment configuration example**

```plaintext
{
  "ipam": {
    "type": "static",
      "addresses": [
        {
          "address": "191.168.1.7/24"
        }
      ]
  }
}
```


### 3.1.2.2. Dynamic IP address (DHCP) assignment configuration

A pod obtains its original DHCP lease when the pod gets created. The lease must be periodically renewed by a minimal DHCP server deployment running on the cluster. 

Important

For an Ethernet network attachment, the SR-IOV Network Operator does not create a DHCP server deployment; the Cluster Network Operator is responsible for creating the minimal DHCP server deployment. 

To trigger the deployment of the DHCP server, you must create a shim network attachment by editing the Cluster Network Operator configuration, as in the following example: 

**Example shim network attachment definition**

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  additionalNetworks:
  - name: dhcp-shim
    namespace: default
    type: Raw
    rawCNIConfig: |-
      {
        "name": "dhcp-shim",
        "cniVersion": "0.3.1",
        "type": "bridge",
        "ipam": {
          "type": "dhcp"
        }
      }
  # ...
```


where: 

`type`
     Specifies dynamic IP address assignment for the cluster. 

## 3.1.3. Dynamic IP address assignment configuration with Whereabouts

The Whereabouts CNI plugin helps the dynamic assignment of an IP address to a secondary network without the use of a DHCP server. 

The Whereabouts CNI plugin also supports overlapping IP address ranges and configuration of the same CIDR range multiple times within separate `NetworkAttachmentDefinition` CRDs. This provides greater flexibility and management capabilities in multitenant environments. 

### 3.1.3.1. Dynamic IP address configuration parameters

The following table describes the configuration objects for dynamic IP address assignment with Whereabouts: 

Table 3.5. ipam whereabouts configuration parametersField| Type| Description  
---|---|---  
`type` |  `string` |  The IPAM address type. The value `whereabouts` is required.   
`range` |  `string` |  An IP address and range in CIDR notation. IP addresses are assigned from within this range of addresses.   
`exclude` |  `array` |  Optional: A list of zero or more IP addresses and ranges in CIDR notation. IP addresses within an excluded address range are not assigned.   
`network_name` |  `string` |  Optional: Helps ensure that each group or domain of pods gets its own set of IP addresses, even if they share the same range of IP addresses. Setting this field is important for keeping networks separate and organized, notably in multitenant environments.   
Show more

### 3.1.3.2. Dynamic IP address assignment configuration with Whereabouts that excludes IP address ranges

The following example shows a dynamic address assignment configuration in a NAD file that uses Whereabouts: 

**Whereabouts dynamic IP address assignment that excludes specific IP address ranges**

```plaintext
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/27",
    "exclude": [
       "192.0.2.192/30",
       "192.0.2.196/32"
    ]
  }
}
```


### 3.1.3.3. Dynamic IP address assignment that uses Whereabouts with overlapping IP address ranges

The following example shows a dynamic IP address assignment that uses overlapping IP address ranges for multitenant networks. 

**NetworkAttachmentDefinition 1**

```plaintext
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/29",
    "network_name": "example_net_common",
  }
}
```


where: 

`network_name`
     Optional parameter. If set, must match the `network_name` of `NetworkAttachmentDefinition 2`. 

**NetworkAttachmentDefinition 2**

```plaintext
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/24",
    "network_name": "example_net_common",
  }
}
```


where: 

`network_name`
     Optional parameter. If set, must match the `network_name` of `NetworkAttachmentDefinition 1`.
