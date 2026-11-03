# 13.5. Configure a machine config pool for hardware offloading

To enable hardware offloading, you now create a dedicated machine config pool and configure it to work with the SR-IOV Network Operator. 

**Prerequisites**

  * SR-IOV Network Operator installed and set into `systemd` mode. 



**Procedure**

  1. Create a machine config pool for machines you want to use hardware offloading on. 

     1. Create a file, such as `mcp-offloading.yaml`, with content such as the following example: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: <mcp_name>
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,<mcp_name>]}
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/<mcp_name>: ""
```


        * `<mcp_name>` specifies the name of your machine config pool for hardware offloading. This value is used as the machine config pool name, the machine config selector value, and the node role label. 

     2. Apply the configuration for the machine config pool: 

```shell-session
$ oc create -f mcp-offloading.yaml
```


  2. Add nodes to the machine config pool. Label each node with the node role label of your pool: 

```shell-session
$ oc label node worker-2 node-role.kubernetes.io/mcp-offloading=""
```


  3. Optional: To verify that the new pool is created, run the following command: 

```shell-session
$ oc get nodes
```


The following is example output: 

```shell-session
NAME       STATUS   ROLES                   AGE   VERSION
master-0   Ready    master                  2d    v1.35.4
master-1   Ready    master                  2d    v1.35.4
worker-0   Ready    worker                  2d    v1.35.4
worker-1   Ready    worker                  2d    v1.35.4
worker-2   Ready    mcp-offloading,worker   47h   v1.35.4
```


  4. Add this machine config pool to the `SriovNetworkPoolConfig` custom resource: 

     1. Create a file, such as `sriov-pool-config.yaml`, with content such as the following example: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkPoolConfig
metadata:
  name: sriovnetworkpoolconfig-offload
  namespace: openshift-sriov-network-operator
spec:
  ovsHardwareOffloadConfig:
    name: <mcp_name>
```


        * `<mcp_name>` specifies the name of your machine config pool for hardware offloading. 

     2. Apply the configuration: 

```shell-session
$ oc create -f <SriovNetworkPoolConfig_name>.yaml
```


Note

When you apply the configuration specified in a `SriovNetworkPoolConfig` object, the SR-IOV Operator drains and restarts the nodes in the machine config pool. 

It might take several minutes for a configuration changes to apply.
