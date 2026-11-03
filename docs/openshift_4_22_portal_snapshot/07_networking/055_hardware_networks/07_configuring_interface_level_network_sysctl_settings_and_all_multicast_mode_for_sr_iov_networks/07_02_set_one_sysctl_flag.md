# 7.2. Set one sysctl flag

You can set interface-level network `sysctl` settings for a pod connected to a SR-IOV network device. 

In this example, `net.ipv4.conf.IFNAME.accept_redirects` is set to `1` on the created virtual interfaces. 

The `sysctl-tuning-test` is a namespace used in this example. 

  * Use the following command to create the `sysctl-tuning-test` namespace: 

```plaintext
$ oc create namespace sysctl-tuning-test
```


## 7.2.1. Set one sysctl flag on nodes with SR-IOV network devices

The SR-IOV Network Operator adds the `SriovNetworkNodePolicy.sriovnetwork.openshift.io` custom resource definition (CRD) to OpenShift Container Platform. You can configure an SR-IOV network device by creating a `SriovNetworkNodePolicy` custom resource (CR). 

Note

When applying the configuration specified in a `SriovNetworkNodePolicy` object, the SR-IOV Operator might drain and reboot the nodes. 

It can take several minutes for a configuration change to apply. 

Follow this procedure to create a `SriovNetworkNodePolicy` custom resource (CR). 

**Procedure**

  1. Create an `SriovNetworkNodePolicy` custom resource (CR). For example, save the following YAML as the file `policyoneflag-sriov-node-network.yaml`: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: policyoneflag
  namespace: openshift-sriov-network-operator
spec:
  resourceName: policyoneflag
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable="true"
  priority: 10
  numVfs: 5
  nicSelector:
    pfNames: ["ens5"]
  deviceType: "netdevice"
  isRdma: false
```


     * `<name>` specifies the name for the custom resource object. 
     * `<namespace>` specifies the namespace where the SR-IOV Network Operator is installed. 
     * `<resourceName>` specifies the resource name of the SR-IOV network device plugin. You can create multiple SR-IOV network node policies for a resource name. 
     * `<nodeSelector>` specifies the node selector for the nodes to configure. Only SR-IOV network devices on the selected nodes are configured. The SR-IOV Container Network Interface (CNI) plugin and device plugin are deployed on selected nodes only. 
     * `<priority>` is optional. The priority is an integer value between `0` and `99`. A smaller value receives higher priority. For example, a priority of `10` is a higher priority than `99`. The default value is `99`. 
     * `<numVfs>` specifies the number of the virtual functions (VFs) to create for the SR-IOV physical network device. For an Intel network interface controller (NIC), the number of VFs cannot be larger than the total VFs supported by the device. For a Mellanox NIC, the number of VFs cannot be larger than `127`. 
     * `<nicSelector>` identifies the device for the Operator to configure. You do not have to specify values for all the parameters. It is recommended to identify the network device with enough precision to avoid selecting a device unintentionally. If you specify `rootDevices`, you must also specify a value for `vendor`, `deviceID`, or `pfNames`. If you specify both `pfNames` and `rootDevices` at the same time, ensure that they refer to the same device. If you specify a value for `netFilter`, then you do not need to specify any other parameter because a network ID is unique. 
     * `<pfNames>` is optional. An array of one or more physical function (PF) names for the device. 
     * `<deviceType>` is optional. The driver type for the virtual functions. The only allowed value is `netdevice`. For a Mellanox NIC to work in DPDK mode on bare-metal nodes, set `isRdma` to `true`. 
     * `<isRdma>` is optional. Configures whether to enable remote direct memory access (RDMA) mode. The default value is `false`. If the `isRdma` parameter is set to `true`, you can continue to use the RDMA-enabled VF as a normal network device. A device can be used in either mode. Set `isRdma` to `true` and additionally set `needVhostNet` to `true` to configure a Mellanox NIC for use with Fast Data Path DPDK applications. 

Note

The `vfio-pci` driver type is not supported. 

  2. Create the `SriovNetworkNodePolicy` object: 

```shell-session
$ oc create -f policyoneflag-sriov-node-network.yaml
```


After applying the configuration update, all the pods in `sriov-network-operator` namespace change to the `Running` status. 

  3. To verify that the SR-IOV network device is configured, enter the following command. Replace `<node_name>` with the name of a node with the SR-IOV network device that you just configured. Expected output shows `Succeeded`. 

```shell-session
$ oc get sriovnetworknodestates -n openshift-sriov-network-operator <node_name> -o jsonpath='{.status.syncStatus}'
```


## 7.2.2. Configure sysctl on a SR-IOV network

You can set interface specific `sysctl` settings on virtual interfaces created by SR-IOV by adding the tuning configuration to the optional `metaPlugins` parameter of the `SriovNetwork` resource. 

The SR-IOV Network Operator manages additional network definitions. When you specify an additional SR-IOV network to create, the SR-IOV Network Operator creates the `NetworkAttachmentDefinition` custom resource (CR) automatically. 

Note

Do not edit `NetworkAttachmentDefinition` custom resources that the SR-IOV Network Operator manages. Doing so might disrupt network traffic on your additional network. 

To change the interface-level network `net.ipv4.conf.IFNAME.accept_redirects` `sysctl` settings, create an additional SR-IOV network with the Container Network Interface (CNI) tuning plugin. 

**Prerequisites**

  * Install the OpenShift Container Platform CLI (oc). 
  * Log in to the OpenShift Container Platform cluster as a user with cluster-admin privileges. 



**Procedure**

  1. Create the `SriovNetwork` custom resource (CR) for the additional SR-IOV network attachment and insert the `metaPlugins` configuration, as in the following example CR. Save the YAML as the file `sriov-network-interface-sysctl.yaml`. 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: onevalidflag
  namespace: openshift-sriov-network-operator
spec:
  resourceName: policyoneflag
  networkNamespace: sysctl-tuning-test
  ipam: '{ "type": "static" }'
  capabilities: '{ "mac": true, "ips": true }'
  metaPlugins : |
    {
      "type": "tuning",
      "capabilities":{
        "mac":true
      },
      "sysctl":{
         "net.ipv4.conf.IFNAME.accept_redirects": "1"
      }
    }
```


     * `<name>` specifies a name for the object. The SR-IOV Network Operator creates a NetworkAttachmentDefinition object with same name. 
     * `<namespace>` specifies the namespace where the SR-IOV Network Operator is installed. 
     * `<resourceName>` specifies the value for the `spec.resourceName` parameter from the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network. 
     * `<networkNamespace>` specifies the target namespace for the `SriovNetwork` object. Only pods in the target namespace can attach to the additional network. 
     * `<ipam>` specifies a configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition. 
     * `<capabilities>` specifies optional capabilities for the additional network. You can specify `"{ "ips": true }"` to enable IP address support or `"{ "mac": true }"` to enable MAC address support. 
     * `<metaPlugins>` specifies optional additional capabilities for the device. In this use case set the `type` field to `tuning`. Specify the interface-level network `sysctl` you want to set in the `sysctl` field. 

  2. Create the `SriovNetwork` resource: 

```shell-session
$ oc create -f sriov-network-interface-sysctl.yaml
```


**Verification**

  * Confirm that the SR-IOV Network Operator created the `NetworkAttachmentDefinition` CR by running the following command: 

```shell-session
$ oc get network-attachment-definitions -n <namespace>
```


    * Replace `<namespace>` with the value for `networkNamespace` that you specified in the `SriovNetwork` object. For example, `sysctl-tuning-test`. The expected output shows the name of the NAD CRD and the creation age in minutes. 

Note

There might be a delay before the SR-IOV Network Operator creates the CR. 

    1. Create a `Pod` CR. Save the following YAML as the file `examplepod.yaml`: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: tunepod
  namespace: sysctl-tuning-test
  annotations:
    k8s.v1.cni.cncf.io/networks: |-
      [
        {
          "name": "onevalidflag",
          "mac": "0a:56:0a:83:04:0c",
          "ips": ["10.100.100.200/24"]
       }
      ]
spec:
  containers:
  - name: podexample
    image: centos
    command: ["/bin/bash", "-c", "sleep INF"]
    securityContext:
      runAsUser: 2000
      runAsGroup: 3000
      allowPrivilegeEscalation: false
      capabilities:
        drop: ["ALL"]
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
```


       * `<name>` specifies the name of the SR-IOV network attachment definition CR. 
       * `<mac>` is optional. The MAC address for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. To use this feature, you also must specify `{ "mac": true }` in the SriovNetwork object. 
       * `<ips>` is optional. IP addresses for the SR-IOV device that are allocated from the resource type defined in the SR-IOV network attachment definition CR. Both IPv4 and IPv6 addresses are supported. To use this feature, you also must specify `{ "ips": true }` in the `SriovNetwork` object. 

    2. Create the `Pod` CR: 

```shell-session
$ oc apply -f examplepod.yaml
```


    3. Verify that the pod is created by running the following command: 

```shell-session
$ oc get pod -n sysctl-tuning-test
```


The following is example output: 

```shell-session
NAME      READY   STATUS    RESTARTS   AGE
tunepod   1/1     Running   0          47s
```


    4. Log in to the pod by running the following command: 

```shell-session
$ oc rsh -n sysctl-tuning-test tunepod
```


    5. Verify the values of the configured sysctl flag. Find the value `net.ipv4.conf.IFNAME.accept_redirects` by running the following command: 

```shell-session
$ sysctl net.ipv4.conf.net1.accept_redirects
```
