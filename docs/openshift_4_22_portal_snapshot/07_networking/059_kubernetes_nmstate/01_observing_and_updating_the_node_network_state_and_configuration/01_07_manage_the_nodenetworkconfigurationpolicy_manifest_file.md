# 1.7. Manage the NodeNetworkConfigurationPolicy manifest file

To configure network interfaces on nodes in your OpenShift Container Platform cluster, you can manage the `NodeNetworkConfigurationPolicy` manifest file by using the CLI. 

## 1.7.1. Create an interface on nodes

You can create an interface on nodes in the cluster by applying a `NodeNetworkConfigurationPolicy` (NNCP) manifest to the cluster. The manifest details the requested configuration for the interface. 

By default, the manifest applies to all nodes in the cluster. To add the interface to specific nodes, add the `spec: nodeSelector` parameter and the appropriate `<key>:<value>` for your node selector. 

You can configure multiple nmstate-enabled nodes concurrently. The configuration applies to 50% of the nodes in parallel. This strategy prevents the entire cluster from being unavailable if the network connection fails. To apply the policy configuration in parallel to a specific portion of the cluster, use the `maxUnavailable` parameter in the `NodeNetworkConfigurationPolicy` manifest configuration file. 

Note

If you have two nodes and you apply an NNCP manifest with the `maxUnavailable` parameter set to `50%` to these nodes, one node at a time receives the NNCP configuration. If you then introduce an additional NNCP manifest file with the `maxUnavailable` parameter set to `50%`, this NCCP is independent of the initial NNCP; this means that if both NNCP manifests apply a bad configuration to nodes, you can no longer guarantee that half of your cluster is functional. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create the `NodeNetworkConfigurationPolicy` manifest. The following example configures a Linux bridge on all worker nodes and configures the DNS resolver: 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: br1-eth1-policy
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  maxUnavailable: 3
  desiredState:
    interfaces:
      - name: br1
        description: Linux bridge with eth1 as a port
        type: linux-bridge
        state: up
        ipv4:
          dhcp: true
          enabled: true
          auto-dns: false
        bridge:
          options:
            stp:
              enabled: false
          port:
            - name: eth1
    dns-resolver:
      config:
        search:
        - example.com
        - example.org
        server:
        - 8.8.8.8
```


     * `metadata.name` defines the name of the policy. 
     * `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes. 
     * `spec.nodeSelector.node-role.kubernetes.io/worker` uses the `node-role.kubernetes.io/worker: ""` node selector to select all worker nodes in the cluster. 
     * `spec.maxUnavailable` is optional and defines the maximum number of nmstate-enabled nodes that the policy configuration can be applied to concurrently. This parameter can be set to either a percentage value (string), for example, `"10%"`, or an absolute value (number), such as `3`. 
     * `spec.desiredState.interfaces.description` is optional and defines a human-readable description for the interface. 
     * `spec.desiredState.dns-resolver` is optional and defines the search and server settings for the DNS server. 

  2. Create the node network policy: 

```shell-session
$ oc apply -f br1-eth1-policy.yaml
```


where: 

`br1-eth1-policy.yaml`
     Specifies the file name of the node network configuration policy manifest. 




**Additional resources**

  * [Example for creating multiple interfaces in the same policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/kubernetes_nmstate/k8s-nmstate-updating-node-network-config#virt-example-nmstate-multiple-interfaces_k8s-nmstate-updating-node-network-config "1.9.5. Example: Multiple interfaces in the same node network configuration policy")
  * [Examples of different IP management methods in policies](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/kubernetes_nmstate/k8s-nmstate-updating-node-network-config#virt-example-nmstate-IP-management_k8s-nmstate-updating-node-network-config "1.12. Examples: IP management")



## 1.7.2. Confirm node network policy updates on nodes

When you apply a node network policy, a `NodeNetworkConfigurationEnactment` object is created for every node in the cluster. The node network configuration enactment is a read-only object that represents the status of execution of the policy on that node. 

If the policy fails to be applied on the node, the enactment for that node includes a traceback for troubleshooting. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. To confirm that a policy has been applied to the cluster, list the policies and their status: 

```shell-session
$ oc get nncp
```


  2. Optional: If a policy is taking longer than expected to successfully configure, you can inspect the requested state and status conditions of a particular policy: 

```shell-session
$ oc get nncp <policy> -o yaml
```


  3. Optional: If a policy is taking longer than expected to successfully configure on all nodes, you can list the status of the enactments on the cluster: 

```shell-session
$ oc get nnce
```


  4. Optional: To view the configuration of a particular enactment, including any error reporting for a failed configuration: 

```shell-session
$ oc get nnce <node>.<policy> -o yaml
```


## 1.7.3. Remove an interface from nodes

You can remove an interface from one or more nodes in the cluster by editing the `NodeNetworkConfigurationPolicy` object and setting the `state` of the interface to `absent`. 

Removing an interface from a node does not automatically restore the node network configuration to a previous state. If you want to restore the previous state, you will need to define that node network configuration in the policy. 

If you remove a bridge or bonding interface, any node NICs in the cluster that were previously attached or subordinate to that bridge or bonding interface are placed in a `down` state and become unreachable. To avoid losing connectivity, configure the node NIC in the same policy so that it has a status of `up` and either DHCP or a static IP address. 

Note

Deleting the node network policy that added an interface does not change the configuration of the policy on the node. Although a `NodeNetworkConfigurationPolicy` is an object in the cluster, the object only represents the requested configuration. Similarly, removing an interface does not delete the policy. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Update the `NodeNetworkConfigurationPolicy` manifest used to create the interface. The following example removes a Linux bridge and configures the `eth1` NIC with DHCP to avoid losing connectivity: 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: <br1-eth1-policy>
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  desiredState:
    interfaces:
    - name: br1
      type: linux-bridge
      state: absent
    - name: eth1
      type: ethernet
      state: up
      ipv4:
        dhcp: true
        enabled: true
```


     * `metadata.name` defines the name of the policy. 
     * `spec.nodeSelector` defines the `nodeSelector` parameter. This parameter is optional. If you do not include the `nodeSelector` parameter, the policy applies to all nodes in the cluster. This example uses the `node-role.kubernetes.io/worker: ""` node selector to select all worker nodes in the cluster. 
     * `spec.desiredState.interfaces` defines the name, type, and desired state of an interface. This example creates both Linux bridge and Ethernet networking interfaces. Setting `state: absent` removes the interface. 
     * `spec.desiredState.interfaces.ipv4` defines `ipv4` settings for the interface. These settings are optional. If you do not use `dhcp`, you can either set a static IP or leave the interface without an IP address. Setting `enabled: true` enables `ipv4` in this example. 

  2. Update the policy on the node and remove the interface: 

```shell-session
$ oc apply -f <filename.yaml>
```


Where `<filename.yaml>` is the filename of the policy manifest.
