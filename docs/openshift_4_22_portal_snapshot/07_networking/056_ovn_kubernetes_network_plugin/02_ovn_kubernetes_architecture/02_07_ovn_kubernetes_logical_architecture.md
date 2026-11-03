# 2.7. OVN-Kubernetes logical architecture

OVN-Kubernetes is a network virtualization solution that creates logical switches and routers across cluster nodes. These virtual infrastructure components interconnect to construct distinct network topologies. 

**Figure 2.2. OVN-Kubernetes router and switch components**

![OVN-Kubernetes logical architecture](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-OVN-Kubernetes_network_plugin-en-US/images/41737354ae3b644b4e1ae9eb6b5d033e/299_OpenShift_OVN-Kubernetes_arch_1023_2.png) ![OVN-Kubernetes logical architecture](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-OVN-Kubernetes_network_plugin-en-US/images/41737354ae3b644b4e1ae9eb6b5d033e/299_OpenShift_OVN-Kubernetes_arch_1023_2.png)

The key components involved in packet processing are: 

Gateway routers
     Gateway routers sometimes called L3 gateway routers, are typically used between the distributed routers and the physical network. Gateway routers including their logical patch ports are bound to a physical location (not distributed), or chassis. The patch ports on this router are known as l3gateway ports in the ovn-southbound database (`ovn-sbdb`). 
Distributed logical routers
     Distributed logical routers and the logical switches behind them, to which virtual machines and containers attach, effectively reside on each hypervisor. 
Join local switch
     Join local switches are used to connect the distributed router and gateway routers. It reduces the number of IP addresses needed on the distributed router. 
Logical switches with patch ports
     Logical switches with patch ports virtualize the network stack. These components connect remote logical ports through network encapsulation tunnels. 
Logical switches with localnet ports
     Logical switches with localnet ports connect the OVN layout to the physical network. These elements connect remote logical ports by bridging packets to directly attached physical Layer 2 segments. 
Patch ports
     Patch ports provide connectivity between logical switches and logical routers, or between peer logical routers. A single connection uses a pair of patch ports at each connectivity intersection, one on each side. 
`l3gateway` ports
     Port binding entries in the `ovn-sbdb` for logical patch ports used in gateway routers. They are called `l3gateway` ports rather than patch ports because these ports are bound to a chassis similar to the gateway router itself. 
localnet ports
     localnet ports are present on the bridged logical switches that allows a connection to a locally accessible network from each `ovn-controller` instance. This helps model the direct connectivity to the physical network from the logical switches. A logical switch can only have a single localnet port attached to it. 

Note

Executing `ovnkube-trace` with the log level configuration set to `2` or `5` exposes these internal OVN-Kubernetes logical routing components for analysis. 

## 2.7.1. Installing network-tools on local host

Install `network-tools` on your local host for debugging OpenShift Container Platform cluster network issues. 

**Procedure**

  1. Clone the `network-tools` repository onto your workstation with the following command: 

```shell-session
$ git clone git@github.com:openshift/network-tools.git
```


  2. Change into the directory for the repository you just cloned: 

```shell-session
$ cd network-tools
```


  3. Optional: List all available commands: 

```shell-session
$ ./debug-scripts/network-tools -h
```


## 2.7.2. Running network-tools

Run `network-tools` to retrieve configuration status from logical switches and routers when diagnosing internal routing loops and cluster network issues. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You are logged in to the cluster as a user with `cluster-admin` privileges. 
  * You have installed `network-tools` on local host. 



**Procedure**

  1. Display the logical router map by entering the following command: 

```shell-session
$ ./debug-scripts/network-tools ovn-db-run-command ovn-nbctl lr-list
```


**Example output**

```shell-session
944a7b53-7948-4ad2-a494-82b55eeccf87 (GR_ci-ln-54932yb-72292-kd676-worker-c-rzj99)
84bd4a4c-4b0b-4a47-b0cf-a2c32709fc53 (ovn_cluster_router)
```


  2. Locate active port bindings with local network attributes by entering the following command: 

```shell-session
$ ./debug-scripts/network-tools ovn-db-run-command "ovn-sbctl find Port_Binding type=localnet"
```


**Example output**

```shell-session
_uuid               : d05298f5-805b-4838-9224-1211afc2f199
additional_chassis  : []
additional_encap    : []
chassis             : []
datapath            : f3c2c959-743b-4037-854d-26627902597c
encap               : []
external_ids        : {}
gateway_chassis     : []
ha_chassis_group    : []
logical_port        : br-ex_ci-ln-54932yb-72292-kd676-worker-c-rzj99
mac                 : [unknown]
mirror_rules        : []
nat_addresses       : []
options             : {network_name=physnet}
parent_port         : []
port_security       : []
requested_additional_chassis: []
requested_chassis   : []
tag                 : []
tunnel_key          : 2
type                : localnet
up                  : false
virtual_parent      : []

[...]
```


  3. List the `l3gateway` ports by entering the following command: 

```shell-session
$ ./debug-scripts/network-tools ovn-db-run-command "ovn-sbctl find Port_Binding type=l3gateway"
```


**Example output**

```shell-session
_uuid               : 5207a1f3-1cf3-42f1-83e9-387bbb06b03c
additional_chassis  : []
additional_encap    : []
chassis             : ca6eb600-3a10-4372-a83e-e0d957c4cd92
datapath            : f3c2c959-743b-4037-854d-26627902597c
encap               : []
external_ids        : {}
gateway_chassis     : []
ha_chassis_group    : []
logical_port        : etor-GR_ci-ln-54932yb-72292-kd676-worker-c-rzj99
mac                 : ["42:01:0a:00:80:04"]
mirror_rules        : []
nat_addresses       : ["42:01:0a:00:80:04 10.0.128.4"]
options             : {l3gateway-chassis="84737c36-b383-4c83-92c5-2bd5b3c7e772", peer=rtoe-GR_ci-ln-54932yb-72292-kd676-worker-c-rzj99}
parent_port         : []
port_security       : []
requested_additional_chassis: []
requested_chassis   : []
tag                 : []
tunnel_key          : 1
type                : l3gateway
up                  : true
virtual_parent      : []

_uuid               : 6088d647-84f2-43f2-b53f-c9d379042679
additional_chassis  : []
additional_encap    : []
chassis             : ca6eb600-3a10-4372-a83e-e0d957c4cd92
datapath            : dc9cea00-d94a-41b8-bdb0-89d42d13aa2e
encap               : []
external_ids        : {}
gateway_chassis     : []
ha_chassis_group    : []
logical_port        : jtor-GR_ci-ln-54932yb-72292-kd676-worker-c-rzj99
mac                 : [router]
mirror_rules        : []
nat_addresses       : []
options             : {l3gateway-chassis="84737c36-b383-4c83-92c5-2bd5b3c7e772", peer=rtoj-GR_ci-ln-54932yb-72292-kd676-worker-c-rzj99}
parent_port         : []
port_security       : []
requested_additional_chassis: []
requested_chassis   : []
tag                 : []
tunnel_key          : 2
type                : l3gateway
up                  : true
virtual_parent      : []

[...]
```


  4. List the patch ports by entering the following command: 

```shell-session
$ ./debug-scripts/network-tools ovn-db-run-command "ovn-sbctl find Port_Binding type=patch"
```


**Example output**

```shell-session
_uuid               : 785fb8b6-ee5a-4792-a415-5b1cb855dac2
additional_chassis  : []
additional_encap    : []
chassis             : []
datapath            : f1ddd1cc-dc0d-43b4-90ca-12651305acec
encap               : []
external_ids        : {}
gateway_chassis     : []
ha_chassis_group    : []
logical_port        : stor-ci-ln-54932yb-72292-kd676-worker-c-rzj99
mac                 : [router]
mirror_rules        : []
nat_addresses       : ["0a:58:0a:80:02:01 10.128.2.1 is_chassis_resident(\"cr-rtos-ci-ln-54932yb-72292-kd676-worker-c-rzj99\")"]
options             : {peer=rtos-ci-ln-54932yb-72292-kd676-worker-c-rzj99}
parent_port         : []
port_security       : []
requested_additional_chassis: []
requested_chassis   : []
tag                 : []
tunnel_key          : 1
type                : patch
up                  : false
virtual_parent      : []

_uuid               : c01ff587-21a5-40b4-8244-4cd0425e5d9a
additional_chassis  : []
additional_encap    : []
chassis             : []
datapath            : f6795586-bf92-4f84-9222-efe4ac6a7734
encap               : []
external_ids        : {}
gateway_chassis     : []
ha_chassis_group    : []
logical_port        : rtoj-ovn_cluster_router
mac                 : ["0a:58:64:40:00:01 100.64.0.1/16"]
mirror_rules        : []
nat_addresses       : []
options             : {peer=jtor-ovn_cluster_router}
parent_port         : []
port_security       : []
requested_additional_chassis: []
requested_chassis   : []
tag                 : []
tunnel_key          : 1
type                : patch
up                  : false
virtual_parent      : []
[...]
```
