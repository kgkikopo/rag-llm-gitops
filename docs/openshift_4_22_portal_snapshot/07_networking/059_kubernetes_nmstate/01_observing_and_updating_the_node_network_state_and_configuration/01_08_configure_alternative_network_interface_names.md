# 1.8. Configure alternative network interface names

You can assign alternative names to network interfaces to create consistent, descriptive labels across cluster nodes. Alternative names help you overcome the 15-character kernel interface name limitation and simplify automation in environments where interface naming varies across hardware. 

Alternative interface names provide the following benefits: 

  * **Consistent naming** : Apply standardized names regardless of underlying hardware naming schemes, which is useful in heterogeneous clusters. 
  * **Descriptive labels** : Use descriptive names up to 127 characters, such as `production-external-interface`, in addition to kernel-assigned names like `ens3f0`. 
  * **Simplified automation** : Reference interfaces by names that remain constant across different node types, reducing configuration errors. 



You can use alternative names anywhere that accepts a standard interface name, including bond ports, VLAN base interfaces, bridge ports, and route next-hop interfaces. 

## 1.8.1. Create alternative interface names by interface name

You can create alternative names for network interfaces to enable consistent, descriptive interface references across cluster nodes. Alternative names persist across reboots and can be used anywhere standard interface names are accepted. 

Important

You cannot configure alternative names on the `br-ex` bridge or any OVN-Kubernetes-managed Open vSwitch bridge. You also cannot configure alternative names on interfaces, bonds, VLANs, or other devices associated with the `br-ex` bridge. 

**Prerequisites**

  * You installed the Kubernetes NMState Operator. 
  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You installed the OpenShift CLI (`oc`). 
  * You identified the target interface by interface name. 
  * The target interface is not the `br-ex` bridge, an OVN-Kubernetes-managed bridge, or associated with these bridges. 



**Procedure**

  1. Create a `NodeNetworkConfigurationPolicy` custom resource (CR) to define alternative names for a target interface. 

Note

Alternative names are appended to any existing alternative names. If you apply a policy multiple times with the same alternative names, the configuration remains unchanged. 

The following example creates a file named `ethernet-alt-names.yaml`: 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: ethernet-alt-names-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node_name>
  desiredState:
    interfaces:
      - name: <interface_name>
        type: ethernet
        state: up
        alt-names:
          - name: <alternative_name_1>
          - name: <alternative_name_2>
```


where: 

     * `<node_name>` is the target node name. To target multiple nodes, use a different label selector such as `node-role.kubernetes.io/worker: ""`. 
     * `<interface_name>` is the target interface name. 
     * `<alternative_name_1>` and `<alternative_name_2>` are the alternative names you want to assign. 

  2. Apply the policy to the cluster by running the following command: 

```shell-session
$ oc apply -f ethernet-alt-names.yaml
```


**Example output**

```shell-session
nodenetworkconfigurationpolicy.nmstate.io/ethernet-alt-names-policy created
```


**Verification**

  1. Verify that the policy was applied successfully by running the following command: 

```shell-session
$ oc get nncp ethernet-alt-names-policy -o yaml
```


Check the `status` section to confirm the policy state is `Available`: 

```yaml
status:
  conditions:
  - lastTransitionTime: "2026-03-31T12:00:00Z"
    message: 2/2 nodes successfully configured
    reason: SuccessfullyConfigured
    status: "True"
    type: Available
```


  2. Create a debug pod on the target node and open a shell to the node filesystem by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


  3. Verify that the alternative names are configured on the interface by running the following command: 

```shell-session
sh-4.4# ip link show <interface_name>
```


**Example output**

```shell-session
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
    altname production-network
    altname external-interface
```


The `altname` entries show the configured alternative names. 




## 1.8.2. Create alternative interface names by MAC address or PCI address

You can match network interfaces by MAC address or peripheral component interconnect (PCI) address to create configurations that target interfaces based on hardware identifiers rather than interface name. 

MAC address matching is useful when you want to target a specific network interface controller. PCI address matching is useful when interface names vary across nodes but hardware slot locations remain consistent. 

**Prerequisites**

  * You installed the Kubernetes NMState Operator. 
  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You installed the OpenShift CLI (`oc`). 
  * You identified the target interface by MAC address or PCI address. 



**Procedure**

  1. Create a `NodeNetworkConfigurationPolicy` custom resource (CR) to define alternative names for a target interface by using one of the following methods: 

     1. To target an interface by MAC address, create a file named `identifier-alt-names.yaml` with content similar to the following example: 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: mac-alt-names-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node_name>
  desiredState:
    interfaces:
      - name: <interface_name>
        type: ethernet
        identifier: mac-address
        mac-address: <mac_address>
        state: up
        alt-names:
          - name: <alternative_name_1>
          - name: <alternative_name_2>
```


where: 

        * `<node_name>` is the target node name. 
        * `<interface_name>` is any identifier because the interface is matched by MAC address. 
        * `<mac_address>` is the MAC address of the target interface. 
        * `<alternative_name_1>` and `<alternative_name_2>` are the alternative names you want to assign. 

     2. To target an interface by PCI address, create a file named `identifier-alt-names.yaml` with content similar to the following example: 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: pci-alt-names-policy
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  desiredState:
    interfaces:
      - name: <interface_name>
        type: ethernet
        state: up
        identifier: pci-address
        pci-address: <pci_address>
        alt-names:
          - name: <alternative_name_1>
          - name: <alternative_name_2>
```


where: 

        * `<interface_name>` is any identifier because the interface is matched by PCI address. 
        * `<pci_address>` is the PCI address of the target interface in the format `domain:bus:device.function`, for example, `0000:01:00.0`. 
        * `<alternative_name_1>` and `<alternative_name_2>` are the alternative names you want to assign. 

Note

This example uses `node-role.kubernetes.io/worker: ""` to target all worker nodes. Use this only when all workers have the same PCI slot configuration. For heterogeneous clusters, use `kubernetes.io/hostname: <node_name>` or hardware-specific labels. 

  2. Apply the policy to the cluster by running the following command: 

```shell-session
$ oc apply -f identifier-alt-names.yaml
```


**Verification**

  1. Verify that the policy was applied successfully by running the following command: 

```shell-session
$ oc get nncp <policy_name> -o yaml
```


Check the `status` section to confirm the policy state is `Available`: 

```yaml
status:
  conditions:
  - lastTransitionTime: "2026-03-31T12:00:00Z"
    message: 3/3 nodes successfully configured
    reason: SuccessfullyConfigured
    status: "True"
    type: Available
```


  2. Create a debug pod on the target node and open a shell to the node filesystem by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


  3. Verify that the alternative names are configured on the interface by running the following command: 

```shell-session
sh-4.4# ip link show <interface_name>
```


**Example output**

```shell-session
2: ens1f0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
    altname production-uplink
    altname external-interface
```


The `altname` entries show the configured alternative names. 




## 1.8.3. Delete alternative interface names

You can remove alternative names from network interfaces when they are no longer needed. Removing alternative names requires explicitly marking them for deletion in a `NodeNetworkConfigurationPolicy` resource. 

Warning

Alternative names used as bond ports (`link-aggregation.port.name`), VLAN base interfaces (`vlan.base-iface`), bridge ports (`linux-bridge.port.name`), or route next-hop interfaces might cause those configurations to fail if the name is removed. 

**Prerequisites**

  * The Kubernetes NMState Operator is installed. 
  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You installed the OpenShift CLI (`oc`). 
  * You configured alternative names on the target interface. 



**Procedure**

  1. Create or update a `NodeNetworkConfigurationPolicy` custom resource (CR) to remove specific alternative names by using one of the following methods: 

     1. To target an interface by interface name, create a file named `remove-alt-names.yaml` with content similar to the following example: 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: remove-alt-names-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node_name>
  desiredState:
    interfaces:
      - name: <interface_name>
        type: ethernet
        state: up
        alt-names:
          - name: <alternative_name_to_remove>
            state: absent
          - name: <another_alternative_name_to_remove>
            state: absent
```


where: 

        * `<node_name>` is the target node name. To target multiple nodes, use a different label selector such as `node-role.kubernetes.io/worker: ""`. 
        * `<interface_name>` is the target interface name. 
        * `<alternative_name_to_remove>` is the alternative name you want to delete. 

     2. To target an interface by MAC address, create a file named `remove-alt-names.yaml` with content similar to the following example: 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: remove-alt-names-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node_name>
  desiredState:
    interfaces:
      - name: <interface_name>
        type: ethernet
        identifier: mac-address
        mac-address: <mac_address>
        state: up
        alt-names:
          - name: <alternative_name_to_remove>
            state: absent
          - name: <another_alternative_name_to_remove>
            state: absent
```


where: 

        * `<node_name>` is the target node name. 
        * `<interface_name>` is any identifier because the interface is matched by MAC address. 
        * `<mac_address>` is the MAC address of the target interface. 
        * `<alternative_name_to_remove>` is the alternative name you want to delete. 

     3. To target an interface by PCI address, create a file named `remove-alt-names.yaml` with content similar to the following example: 

```yaml
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: remove-alt-names-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node_name>
  desiredState:
    interfaces:
      - name: <interface_name>
        type: ethernet
        identifier: pci-address
        pci-address: <pci_address>
        state: up
        alt-names:
          - name: <alternative_name_to_remove>
            state: absent
          - name: <another_alternative_name_to_remove>
            state: absent
```


where: 

        * `<node_name>` is the target node name. 
        * `<interface_name>` is any identifier because the interface is matched by PCI address. 
        * `<pci_address>` is the PCI address of the target interface in the format `domain:bus:device.function` (for example, `0000:01:00.0`). 
        * `<alternative_name_to_remove>` is the alternative name you want to delete. 

  2. Apply the policy to remove the alternative names by running the following command: 

```shell-session
$ oc apply -f remove-alt-names.yaml
```


**Verification**

  1. Verify that the policy was applied successfully: 

```shell-session
$ oc get nncp remove-alt-names-policy -o yaml
```


Check the `status` section to confirm the policy state is `Available`: 

```yaml
status:
  conditions:
  - lastTransitionTime: "2026-03-31T12:00:00Z"
    message: 1/1 nodes successfully configured
    reason: SuccessfullyConfigured
    status: "True"
    type: Available
```


  2. Access the target node: 

```shell-session
$ oc debug node/<node_name>
```


  3. Verify that the alternative name was removed: 

```shell-session
sh-4.4# ip link show <interface_name>
```


**Example output**

```shell-session
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
    altname production-network
    altname external-interface
```


The removed alternative name (for example, `deprecated-name`) should no longer appear in the `altname` entries. 

Note

     * If you remove an alternative name from the policy YAML without setting `state: absent`, the NMState Operator does not delete it from the interface. Alternative names use an incremental change model where applying a policy appends new names. You must explicitly mark names for deletion with `state: absent`. 
     * If you delete the entire interface configuration, all associated alternative names are also deleted.
