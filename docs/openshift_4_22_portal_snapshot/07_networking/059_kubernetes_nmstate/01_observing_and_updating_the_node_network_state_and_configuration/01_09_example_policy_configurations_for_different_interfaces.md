# 1.9. Example policy configurations for different interfaces

Before you read the different example `NodeNetworkConfigurationPolicy` (NNCP) manifest configurations, consider the following factors when you apply a policy to nodes so that your cluster runs under its best performance conditions. 

  * If you want to apply multiple NNCP CRs to a node, you must create the NNCPs in a logical order that is based on the alphanumeric sorting of the policy names. The Kubernetes NMState Operator continuously checks for a newly created NNCP CR so that the Operator can instantly apply the CR to node. 
  * When you need to apply a policy to many nodes but you only want to create a single NNCP for all the nodes, the Kubernetes NMState Operator applies the policy to each node in sequence. You can set the speed and coverage of policy application for target nodes with the `maxUnavailable` parameter in the cluster’s configuration file. By setting a lower percentage value for the parameter, you can reduce the risk of a cluster-wide outage if the outage impacts the small percentage of nodes that are receiving the policy application. 
  * If you set the `maxUnavailable` parameter to `50%` in two NNCP manifests, the policy configuration coverage applies to 100% of the nodes in your cluster. 
  * When a node restarts, the Kubernetes NMState Operator cannot control the order to which it applies policies to nodes. The Kubernetes NMState Operator might apply interdependent policies in a sequence that results in a degraded network object. 
  * Consider specifying all related network configurations in a single policy. 



## 1.9.1. Example: Ethernet interface node network configuration policy

You can configure an Ethernet interface on nodes in the cluster by applying a `NodeNetworkConfigurationPolicy` manifest to the cluster. 

The following YAML file is an example of a manifest for an Ethernet interface. It includes sample values that you must replace with your own information. 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: eth1-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node01>
  desiredState:
    interfaces:
    - name: eth1
      description: Configuring eth1 on node01
      type: ethernet
      state: up
      ipv4:
        dhcp: true
        enabled: true
```


  * `metadata.name` defines the name of the policy. 
  * `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes. 
  * `spec.nodeSelector.kubernetes.io/hostname` uses a hostname node selector. 
  * `spec.desiredState.interfaces.name` defines the name of the interface. 
  * `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface. 
  * `spec.desiredState.interfaces.type` defines the type of interface. This example creates an Ethernet networking interface. 
  * `spec.desiredState.interfaces.state` defines the requested state for the interface after creation. 
  * `spec.desiredState.interfaces.ipv4.dhcp` is optional. If you do not use `dhcp`, you can either set a static IP or leave the interface without an IP address. 
  * `spec.desiredState.interfaces.ipv4.enabled` defines that `ipv4` is enabled in this example. 



## 1.9.2. Example: Linux bridge interface node network configuration policy

You can create a Linux bridge interface on nodes in the cluster by applying a `NodeNetworkConfigurationPolicy` manifest to the cluster. 

The following YAML file is an example of a manifest for a Linux bridge interface. It includes samples values that you must replace with your own information. 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: br1-eth1-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node01>
  desiredState:
    interfaces:
      - name: br1
        description: Linux bridge with eth1 as a port
        type: linux-bridge
        state: up
        ipv4:
          dhcp: true
          enabled: true
        bridge:
          options:
            stp:
              enabled: false
          port:
            - name: eth1
```


  * `metadata.name` defines the name of the policy. 
  * `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes. 
  * `spec.nodeSelector.kubernetes.io/hostname` uses a hostname node selector. 
  * `spec.desiredState.interfaces.name` defines the name of the interface. 
  * `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface. 
  * `spec.desiredState.interfaces.type` defines the type of interface. This example creates a bridge. 
  * `spec.desiredState.interfaces.state` defines the requested state for the interface after creation. 
  * `spec.desiredState.interfaces.ipv4.dhcp` is optional. If you do not use `dhcp`, you can either set a static IP or leave the interface without an IP address. 
  * `spec.desiredState.interfaces.ipv4.enabled` defines that `ipv4` is enabled in this example. 
  * `spec.desiredState.interfaces.bridge.options.stp.enabled` defines that `stp` is disabled in this example. 
  * `spec.desiredState.interfaces.bridge.port.name` defines the node NIC to which the bridge attaches. 



## 1.9.3. Example: VLAN interface node network configuration policy

You can create a VLAN interface on nodes in the cluster by applying a `NodeNetworkConfigurationPolicy` manifest to the cluster. 

Note

Define all related configurations for the VLAN interface of a node in a single `NodeNetworkConfigurationPolicy` manifest. For example, define the VLAN interface for a node and the related routes for the VLAN interface in the same `NodeNetworkConfigurationPolicy` manifest. 

When a node restarts, the Kubernetes NMState Operator cannot control the order in which policies are applied. Therefore, if you use separate policies for related network configurations, the Kubernetes NMState Operator might apply these policies in a sequence that results in a degraded network object. 

The following YAML file is an example of a manifest for a VLAN interface. It includes samples values that you must replace with your own information. 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: vlan-eth1-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node01>
  desiredState:
    interfaces:
    - name: eth1.102
      description: VLAN using eth1
      type: vlan
      state: up
      vlan:
        base-iface: eth1
        id: 102
```


  * `metadata.name` defines the name of the policy. 
  * `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes. 
  * `spec.nodeSelector.kubernetes.io/hostname` uses a hostname node selector. 
  * `spec.desiredState.interfaces.name` defines the name of the interface. When deploying on bare metal, only the `<interface_name>.<vlan_number>` VLAN format is supported. 
  * `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface. 
  * `spec.desiredState.interfaces.type` defines the type of interface. This example creates a VLAN. 
  * `spec.desiredState.interfaces.state` defines the requested state for the interface after creation. 
  * `spec.desiredState.interfaces.vlan.base-iface` defines the node NIC to which the VLAN is attached. 
  * `spec.desiredState.interfaces.vlan.id` defines the VLAN tag. 



**Additional resources**

  * [Configuring an SR-IOV network device](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/#configuring-sriov-device)
  * [Configuring hardware offloading](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/#configuring-hardware-offloading)



## 1.9.4. Example: Bond interface node network configuration policy

You can create a bond interface on nodes in the cluster by applying a `NodeNetworkConfigurationPolicy` manifest to the cluster. 

Note

OpenShift Container Platform only supports the following bond modes: 

  * `active-backup`
  * `balance-xor`
  * `802.3ad`



Other bond modes are not supported. 

The `balance-xor` and `802.3ad` bond modes require switch configuration to establish an "EtherChannel" or similar port grouping. Those two modes also require additional load-balancing configuration, depending on the source and destination of traffic being passed through the interface. The `active-backup` bond mode does not require any switch configuration. Other bond modes are not supported. 

The following YAML file is an example of a manifest for a bond interface. It includes samples values that you must replace with your own information. 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: bond0-eth1-eth2-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node01>
  desiredState:
    interfaces:
    - name: bond0
      description: Bond with ports eth1 and eth2
      type: bond
      state: up
      ipv4:
        dhcp: true
        enabled: true
      link-aggregation:
        mode: active-backup
        options:
          miimon: '140'
        port:
        - eth1
        - eth2
      mtu: 1450
```


  * `metadata.name` defines the name of the policy. 
  * `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes. 
  * `spec.nodeSelector.kubernetes.io/hostname` uses a hostname node selector. 
  * `spec.desiredState.interfaces.name` defines the name of the interface. 
  * `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface. 
  * `spec.desiredState.interfaces.type` defines the type of interface. This example creates a bond. 
  * `spec.desiredState.interfaces.state` defines the requested state for the interface after creation. 
  * `spec.desiredState.interfaces.ipv4.dhcp` is optional. If you do not use `dhcp`, you can either set a static IP or leave the interface without an IP address. 
  * `spec.desiredState.interfaces.ipv4.enabled` defines that `ipv4` is enabled in this example. 
  * `spec.desiredState.interfaces.link-aggregation.mode` defines the driver mode for the bond. This example uses `active backup`. 
  * `spec.desiredState.interfaces.link-aggregation.options.miimon` is optional and defines that miimon is used to inspect the bond link every 140ms. 
  * `spec.desiredState.interfaces.link-aggregation.port` defines the subordinate node NICs in the bond. 
  * `spec.desiredState.interfaces.mtu` is optional and defines the maximum transmission unit (MTU) for the bond. If not specified, this value is set to `1500` by default. 



## 1.9.5. Example: Multiple interfaces in the same node network configuration policy

You can create multiple interfaces in the same node network configuration policy. These interfaces can reference each other, allowing you to build and deploy a network configuration by using a single policy manifest. 

Important

If multiple interfaces use the same default configuration, a single Network Manager connection profile activates on multiple interfaces simultaneously and this causes connections to have the same universally unique identifier (UUID). To avoid this issue, ensure that each interface has a specific configuration that is different from the default configuration. 

The following example YAML file creates a bond that is named `bond10` across two NICs and VLAN that is named `bond10.103` that connects to the bond. 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: bond-vlan
spec:
  nodeSelector:
    kubernetes.io/hostname: <node01>
  desiredState:
    interfaces:
    - name: bond10
      description: Bonding eth2 and eth3
      type: bond
      state: up
      link-aggregation:
        mode: balance-xor
        options:
          miimon: '140'
        port:
        - eth2
        - eth3
    - name: bond10.103
      description: vlan using bond10
      type: vlan
      state: up
      vlan:
         base-iface: bond10
         id: 103
      ipv4:
        dhcp: true
        enabled: true
```


  * `metadata.name` defines the name of the policy. 
  * `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes. 
  * `spec.nodeSelector.kubernetes.io/hostname` uses a hostname node selector. 
  * `spec.desiredState.interfaces.name` defines the name of the interface. 
  * `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface. 
  * `spec.desiredState.interfaces.type` defines the type of interface. 
  * `spec.desiredState.interfaces.state` defines the requested state for the interface after creation. 
  * `spec.desiredState.interfaces.link-aggregation.mode` defines the driver mode for the bond. 
  * `spec.desiredState.interfaces.link-aggregation.options.miimon` is optional and defines that miimon is used to inspect the bond link every 140ms. 
  * `spec.desiredState.interfaces.link-aggregation.port` defines the subordinate node NICs in the bond. 
  * `spec.desiredState.interfaces.vlan.base-iface` defines the node NIC to which the VLAN is attached. 
  * `spec.desiredState.interfaces.vlan.id` defines the VLAN tag. 
  * `spec.desiredState.interfaces.ipv4.dhcp` is optional. If you do not use dhcp, you can either set a static IP or leave the interface without an IP address. 
  * `spec.desiredState.interfaces.ipv4.enabled` defines that ipv4 is enabled in this example. 



## 1.9.6. Example: Node network configuration policy for virtual functions

You can update host network settings for Single Root I/O Virtualization (SR-IOV) network virtual functions (VF) in an existing cluster by applying a `NodeNetworkConfigurationPolicy` manifest. 

You can apply a `NodeNetworkConfigurationPolicy` manifest to an existing cluster to complete the following tasks: 

  * Configure QoS host network settings for VFs to optimize performance. 
  * Add, remove, or update VFs for a network interface. 
  * Manage VF bonding configurations. 



Note

To update host network settings for SR-IOV VFs by using NMState on physical functions that are also managed through the SR-IOV Network Operator, you must set the `externallyManaged` parameter in the relevant `SriovNetworkNodePolicy` resource to `true`. For more information, see the _Additional resources_ section. 

The following YAML file is an example of a manifest that defines QoS policies for a VF. This YAML includes samples values that you must replace with your own information. 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: qos
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  desiredState:
    interfaces:
      - name: ens1f0
        description: Change QOS on VF0
        type: ethernet
        state: up
        ethernet:
         sr-iov:
           total-vfs: 3
           vfs:
           - id: 0
             max-tx-rate: 200
```


  * `metadata.name` defines the name of the policy. 
  * `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes. 
  * `spec.nodeSelector.node-role.kubernetes.io/worker` defines that this example applies to all nodes with the `worker` role. 
  * `spec.desiredState.interfaces.name` defines the name of the physical function (PF) network interface. 
  * `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface. 
  * `spec.desiredState.interfaces.type` defines the type of interface. 
  * `spec.desiredState.interfaces.state` defines the requested state for the interface after configuration. 
  * `spec.desiredState.interfaces.ethernet.sr-iov.total-vfs` defines the total number of VFs. 
  * `spec.desiredState.interfaces.ethernet.sr-iov.vfs.id` defines the VF ID. In this example, the VF has an ID of `0`. 
  * `spec.desiredState.interfaces.ethernet.sr-iov.vfs.max-tx-rate` defines a maximum transmission rate, in Mbps, for the VF. This sample value sets a rate of 200 Mbps. 



The following YAML file is an example of a manifest that adds a VF for a network interface. 

In this sample configuration, the `ens1f1v0` VF is created on the `ens1f1` physical interface, and this VF is added to a bonded network interface `bond0`. The bond uses `active-backup` mode for redundancy. In this example, the VF is configured to use hardware offloading to manage the VLAN directly on the physical interface. 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: addvf
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  maxUnavailable: 3
  desiredState:
    interfaces:
      - name: ens1f1
        type: ethernet
        state: up
        ethernet:
            sr-iov:
              total-vfs: 1
              vfs:
                - id: 0
                  trust: true
                  vlan-id: 477
      - name: bond0
        description: Attach VFs to bond
        type: bond
        state: up
        link-aggregation:
          mode: active-backup
          options:
            primary: ens1f0v0
          port:
            - ens1f0v0
            - ens1f1v0
```


  * `metadata.name` defines the name of the policy. 
  * `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes. 
  * `spec.nodeSelector.node-role.kubernetes.io/worker` defines that the example applies to all nodes with the `worker` role. 
  * `spec.desiredState.interfaces[0].name` defines the name of the VF network interface. 
  * `spec.desiredState.interfaces[0].ethernet.sr-iov.total-vfs` defines the number of VFs to create. 
  * `spec.desiredState.interfaces[0].ethernet.sr-iov.vfs.trust` defines a setting to allow failover bonding between the active and backup VFs. 
  * `spec.desiredState.interfaces[0].ethernet.sr-iov.vfs.vlan-id` defines the ID of the VLAN. The example uses hardware offloading to define a VLAN directly on the VF. 
  * `spec.desiredState.interfaces[1].name` defines the name of the bonding network interface. 
  * `spec.desiredState.interfaces[1].description` is optional and defines a human-readable description of the interface. 
  * `spec.desiredState.interfaces[1].type` defines the type of interface. 
  * `spec.desiredState.interfaces[1].state` defines the requested state for the interface after configuration. 
  * `spec.desiredState.interfaces[1].link-aggregation.mode` defines the bonding policy for the bond. 
  * `spec.desiredState.interfaces[1].link-aggregation.options.primary` defines the primary attached bonding port. 
  * `spec.desiredState.interfaces[1].link-aggregation.port` defines the ports for the bonded network interface. In this example, `ens1f1v0` is the VLAN network interface added as an additional interface to the bonded network interface. 



## 1.9.7. Example: Network interface with a VRF instance node network configuration policy

You can associate a Virtual Routing and Forwarding (VRF) instance with a network interface by applying a `NodeNetworkConfigurationPolicy` custom resource (CR). 

By associating a VRF instance with a network interface, you can support traffic isolation, independent routing decisions, and the logical separation of network resources. 

Warning

When configuring Virtual Route Forwarding (VRF), you must change the VRF value to a table ID lower than `1000` because a value higher than `1000` is reserved for OpenShift Container Platform. 

In a bare-metal environment, you can announce load balancer services through interfaces belonging to a VRF instance by using MetalLB. For more information, see the _Additional resources_ section. 

The following YAML file is an example of associating a VRF instance to a network interface. It includes samples values that you must replace with your own information. 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: vrfpolicy
spec:
  nodeSelector:
    vrf: "true"
  maxUnavailable: 3
  desiredState:
    interfaces:
      - name: ens4vrf
        type: vrf
        state: up
        vrf:
          port:
            - ens4
          route-table-id: 2
```


  * `metadata.name` defines the name of the policy. 
  * `spec.nodeSelector.vrf` defines a node selector. This example applies the policy to all nodes with the label `vrf:true`. 
  * `spec.desiredState.interfaces.name` defines the name of the interface. 
  * `spec.desiredState.interfaces.type` defines the type of interface. This example creates a VRF instance. 
  * `spec.desiredState.interfaces.vrf.port` defines the node interface to which the VRF attaches. 
  * `spec.desiredState.interfaces.vrf.route-table-id` defines the route table ID for the VRF. 



## 1.9.8. Example: Network interface with a predictable route table ID

To simplify network administration and reduce configuration errors in OpenShift Container Platform, configure routes by using names instead of Virtual Routing and Forwarding (VRF) routing table ID numbers. 

Using human-readable names ensures that network routes are easier to identify and maintain without tracking abstract numerical identifiers. 

The following `NodeNetworkConfigurationPolicy` (NNCP) YAML file shows an example of creating a VRF instance and applying a route to the VRF instance. The VRF instance uses the stable method of referencing the VRF by name rather than a potentially shifting ID. 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: vrf-predictable-policy
spec:
  nodeSelector:
    vrf: "true"
  maxUnavailable: 3
  desiredState:
    interfaces:
      - name: vrf0
        type: vrf
        state: up
        vrf:
          route-table-id: 100
          port:
            - eth1
            - eth2
    routes:
      config:
        - destination: 198.51.200.0/24
          route-type: blackhole
          vrf-name: vrf0
# ...
```


where: 

`spec.nodeSelector.vrf`
     Specifies the application of the policy only to nodes that have the `vrf: true` label. This configuration prevents accidental network changes on nodes that do not require VRF support. 
`spec.desiredState.interfaces.type`
     Specifies the creation of a VRF-type interface. 
`spec.desiredState.interfaces.vrf.route-table-id`
     Specifies the `route-table-id` that the `vrf` name maps to in the routing table. 
`spec.desiredState.routes.config.route-type`
     Specifies the route type. NetworkManager supports the `unicast`, `local`, `blackhole`, `unreachable`, `prohibit`, and `throw` route types. The default is unicast. The example sets a `blackhole` route that drops any packets within the IP address range of this route. The range for the `blackhole` route is the destination CIDR, such as `198.51.200.0/24`. 
`spec.desiredState.routes.config.vrf-name`
     Specifies a stable link in that if a policy changes the `route-table-id` parameter to a different value, the route automatically follows the `vrf0` name to the new ID. You do not need to manually update the route configuration. 

**Additional resources**

  * [About virtual routing and forwarding](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/multiple_networks/#cnf-about-virtual-routing-and-forwarding_about-virtual-routing-and-forwarding)
  * [Exposing a service through a network VRF](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ingress_and_load_balancing/#nw-metallb-bgp-peer-vrf_configure-metallb-bgp-peers)
