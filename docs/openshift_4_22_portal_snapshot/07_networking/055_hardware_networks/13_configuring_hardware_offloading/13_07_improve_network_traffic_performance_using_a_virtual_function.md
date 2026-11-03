# 13.7. Improve network traffic performance using a virtual function

Follow this procedure to assign a virtual function to the OVN-Kubernetes management port and increase its network traffic performance. 

This procedure results in the creation of two pools: the first has a virtual function used by OVN-Kubernetes, and the second comprises the remaining virtual functions. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Add the `network.operator.openshift.io/smart-nic` label to each worker node with a SmartNIC present by running the following command: 

```shell-session
$ oc label node <node-name> network.operator.openshift.io/smart-nic=
```


Use the `oc get nodes` command to get a list of the available nodes. 

  2. Create a policy named `sriov-node-mgmt-vf-policy.yaml` for the management port with content such as the following example: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: sriov-node-mgmt-vf-policy
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  eSwitchMode: "switchdev"
  nicSelector:
    deviceID: "1019"
    rootDevices:
    - 0000:d8:00.0
    vendor: "15b3"
    pfNames:
    - <pf_name>#0-0
  nodeSelector:
    network.operator.openshift.io/smart-nic: ""
  numVfs: <num_vfs>
  priority: 5
  resourceName: mgmtvf
```


     * `<pf_name>` specifies the network device for your use case. The `#0-0` part of the `pfNames` value reserves a single virtual function used by OVN-Kubernetes. 
     * `<num_vfs>` specifies the number of virtual functions. Replace this value with one that meets your requirements. For more information, see _SR-IOV network node configuration object_ in the _Additional resources_ section. 

  3. Create a policy named `sriov-node-policy.yaml` with content such as the following example: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: sriov-node-policy
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  eSwitchMode: "switchdev"
  nicSelector:
    deviceID: "1019"
    rootDevices:
    - 0000:d8:00.0
    vendor: "15b3"
    pfNames:
    - <pf_name>#1-5
  nodeSelector:
    network.operator.openshift.io/smart-nic: ""
  numVfs: <num_vfs>
  priority: 5
  resourceName: mlxnics
```


     * `<pf_name>` specifies the network device for your use case. 
     * `<num_vfs>` specifies the number of virtual functions. Replace this value with the value specified in the `sriov-node-mgmt-vf-policy.yaml` file. For more information, see _SR-IOV network node configuration object_ in the _Additional resources_ section. 

Note

The `sriov-node-mgmt-vf-policy.yaml` file has different values for the `pfNames` and `resourceName` keys than the `sriov-node-policy.yaml` file. 

  4. Apply the configuration for both policies: 

```shell-session
$ oc create -f sriov-node-policy.yaml
```


```shell-session
$ oc create -f sriov-node-mgmt-vf-policy.yaml
```


  5. Create a Cluster Network Operator (CNO) ConfigMap in the cluster for the management configuration: 

     1. Create a ConfigMap named `hardware-offload-config.yaml` with the following contents: 

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
    name: hardware-offload-config
    namespace: openshift-network-operator
data:
    mgmt-port-resource-name: openshift.io/mgmtvf
```


     2. Apply the configuration for the ConfigMap: 

```shell-session
$ oc create -f hardware-offload-config.yaml
```


**Additional resources**

  * [SR-IOV network node configuration object](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hardware_networks/configuring-sriov-device#nw-sriov-networknodepolicy-object_configuring-sriov-device "2.1. SR-IOV network node configuration object")
