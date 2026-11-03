# 7.3. Configure sysctl settings for pods associated with bonded SR-IOV interface flag

You can set interface-level network `sysctl` settings for a pod connected to a bonded SR-IOV network device. 

In this example, the specific network interface-level `sysctl` settings that can be configured are set on the bonded interface. 

The `sysctl-tuning-test` is a namespace used in this example. 

  * Use the following command to create the `sysctl-tuning-test` namespace: 

```plaintext
$ oc create namespace sysctl-tuning-test
```


## 7.3.1. Set all sysctl flag on nodes with bonded SR-IOV network devices

The SR-IOV Network Operator adds the `SriovNetworkNodePolicy.sriovnetwork.openshift.io` custom resource definition (CRD) to OpenShift Container Platform. You can configure an SR-IOV network device by creating a `SriovNetworkNodePolicy` custom resource (CR). 

Note

When applying the configuration specified in a SriovNetworkNodePolicy object, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes. 

It might take several minutes for a configuration change to apply. 

Follow this procedure to create a `SriovNetworkNodePolicy` custom resource (CR). 

**Procedure**

  1. Create an `SriovNetworkNodePolicy` custom resource (CR). Save the following YAML as the file `policyallflags-sriov-node-network.yaml`. Replace `policyallflags` with the name for the configuration. 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: policyallflags
  namespace: openshift-sriov-network-operator
spec:
  resourceName: policyallflags
  nodeSelector:
    node.alpha.kubernetes-incubator.io/nfd-network-sriov.capable = `true`
  priority: 10
  numVfs: 5
  nicSelector:
    pfNames: ["ens1f0"]
  deviceType: "netdevice"
  isRdma: false
```


     * `<name>` specifies the name for the custom resource object. 
     * `<namespace>` specifies the namespace where the SR-IOV Network Operator is installed. 
     * `<resourceName>` specifies the resource name of the SR-IOV network device plugin. You can create multiple SR-IOV network node policies for a resource name. 
     * `<nodeSelector>` specifies the node selector for the nodes to configure. Only SR-IOV network devices on the selected nodes are configured. The SR-IOV Container Network Interface (CNI) plugin and device plugin are deployed on selected nodes only. 
     * `<priority>` is optional. The priority is an integer value between `0` and `99`. A smaller value receives higher priority. For example, a priority of `10` is a higher priority than `99`. The default value is `99`. 
     * `<numVfs>` specifies the number of virtual functions (VFs) to create for the SR-IOV physical network device. For an Intel network interface controller (NIC), the number of VFs cannot be larger than the total VFs supported by the device. For a Mellanox NIC, the number of VFs cannot be larger than `127`. 
     * `<nicSelector>` identifies the device for the Operator to configure. You do not have to specify values for all the parameters. It is recommended to identify the network device with enough precision to avoid selecting a device unintentionally. If you specify `rootDevices`, you must also specify a value for `vendor`, `deviceID`, or `pfNames`. If you specify both `pfNames` and `rootDevices` at the same time, ensure that they refer to the same device. If you specify a value for `netFilter`, then you do not need to specify any other parameter because a network ID is unique. 
     * `<pfNames>` is optional. An array of one or more physical function (PF) names for the device. 
     * `<deviceType>` is optional. The driver type for the virtual functions. The only allowed value is `netdevice`. For a Mellanox NIC to work in DPDK mode on bare-metal nodes, set `isRdma` to `true`. 
     * `<isRdma>` is optional. Configures whether to enable remote direct memory access (RDMA) mode. The default value is `false`. If the `isRdma` parameter is set to `true`, you can continue to use the RDMA-enabled VF as a normal network device. A device can be used in either mode. Set `isRdma` to `true` and additionally set `needVhostNet` to `true` to configure a Mellanox NIC for use with Fast Data Path DPDK applications. 

Note

The `vfio-pci` driver type is not supported. 

  2. Create the `SriovNetworkNodePolicy` object: 

```shell-session
$ oc create -f policyallflags-sriov-node-network.yaml
```


After applying the configuration update, all the pods in sriov-network-operator namespace change to the `Running` status. 

  3. To verify that the SR-IOV network device is configured, enter the following command. Replace `<node_name>` with the name of a node with the SR-IOV network device that you just configured. Expected output shows `Succeeded`

```shell-session
$ oc get sriovnetworknodestates -n openshift-sriov-network-operator <node_name> -o jsonpath='{.status.syncStatus}'
```


## 7.3.2. Configure sysctl on a bonded SR-IOV network

You can set interface specific `sysctl` settings on a bonded interface created from two SR-IOV interfaces. Do this by adding the tuning configuration to the optional `Plugins` parameter of the bond network attachment definition. 

Note

Do not edit `NetworkAttachmentDefinition` custom resources that the SR-IOV Network Operator manages. Doing so might disrupt network traffic on your additional network. 

To change specific interface-level network `sysctl` settings create the `SriovNetwork` custom resource (CR) with the Container Network Interface (CNI) tuning plugin by using the following procedure. 

**Prerequisites**

  * Install the OpenShift Container Platform CLI (oc). 
  * Log in to the OpenShift Container Platform cluster as a user with cluster-admin privileges. 



**Procedure**

  1. Create the `SriovNetwork` custom resource (CR) for the bonded interface as in the following example CR. Save the YAML as the file `sriov-network-attachment.yaml`. 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: allvalidflags
  namespace: openshift-sriov-network-operator
spec:
  resourceName: policyallflags
  networkNamespace: sysctl-tuning-test
  capabilities: '{ "mac": true, "ips": true }'
```


     * `<name>`: A name for the object. The SR-IOV Network Operator creates a NetworkAttachmentDefinition object with same name. 
     * `<namespace>`: The namespace where the SR-IOV Network Operator is installed. 
     * `<resourceName>`: The value for the `spec.resourceName` parameter from the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network. 
     * `<networkNamespace>`: The target namespace for the `SriovNetwork` object. Only pods in the target namespace can attach to the additional network. 
     * `<capabilities>`: Optional: The capabilities to configure for this additional network. You can specify `"{ "ips": true }"` to enable IP address support or `"{ "mac": true }"` to enable MAC address support. 

  2. Create the `SriovNetwork` resource: 

```shell-session
$ oc create -f sriov-network-attachment.yaml
```


  3. Create a bond network attachment definition as in the following example CR. Save the YAML as the file `sriov-bond-network-interface.yaml`. 

```yaml
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: bond-sysctl-network
  namespace: sysctl-tuning-test
spec:
  config: '{
  "cniVersion":"0.4.0",
  "name":"bound-net",
  "plugins":[
    {
      "type":"bond",
      "mode": "active-backup",
      "failOverMac": 1,
      "linksInContainer": true,
      "miimon": "100",
      "links": [
        {"name": "net1"},
        {"name": "net2"}
      ],
      "ipam":{
        "type":"static"
      }
    },
    {
      "type":"tuning",
      "capabilities":{
        "mac":true
      },
      "sysctl":{
        "net.ipv4.conf.IFNAME.accept_redirects": "0",
        "net.ipv4.conf.IFNAME.accept_source_route": "0",
        "net.ipv4.conf.IFNAME.disable_policy": "1",
        "net.ipv4.conf.IFNAME.secure_redirects": "0",
        "net.ipv4.conf.IFNAME.send_redirects": "0",
        "net.ipv6.conf.IFNAME.accept_redirects": "0",
        "net.ipv6.conf.IFNAME.accept_source_route": "1",
        "net.ipv6.neigh.IFNAME.base_reachable_time_ms": "20000",
        "net.ipv6.neigh.IFNAME.retrans_time_ms": "2000"
      }
    }
  ]
}'
```


     * `<type>`: The type is `bond`. 
     * `<mode>`: The `mode` attribute specifies the bonding mode. The bonding modes supported are `balance-rr` \- 0, `active-backup` \- 1, and `balance-xor` \- 2. For `balance-rr` or `balance-xor` modes, you must set the `trust` mode to `on` for the SR-IOV virtual function. 
     * `<failOverMac>`: The `failover` attribute is mandatory for active-backup mode. 
     * `<linksInContainer>`: The `linksInContainer=true` flag informs the Bond CNI that the required interfaces are to be found inside the container. By default, Bond CNI looks for these interfaces on the host which does not work for integration with SRIOV and Multus. 
     * `<links>`: The `links` section defines which interfaces will be used to create the bond. By default, Multus names the attached interfaces as: "net", plus a consecutive number, starting with one. 
     * `<ipam>`: A configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition. In this pod example IP addresses are configured manually, so in this case,`ipam` is set to static. 
     * `<tuning>`: Add additional capabilities to the device. For example, set the `type` field to `tuning`. Specify the interface-level network `sysctl` you want to set in the sysctl field. This example sets all interface-level network `sysctl` settings that can be set. 

  4. Create the bond network attachment resource: 

```shell-session
$ oc create -f sriov-bond-network-interface.yaml
```


**Verification**

  1. Confirm that the SR-IOV Network Operator created the `NetworkAttachmentDefinition` CR by running the following command: 

```shell-session
$ oc get network-attachment-definitions -n <namespace>
```


     * `<namespace>`: Replace with the networkNamespace that you specified when configuring the network attachment, for example, `sysctl-tuning-test`. Expected output shows the names of the NAD CRDs and the creation age in minutes. 

Note

There might be a delay before the SR-IOV Network Operator creates the CR. 

  2. Create a `Pod` CR. For example, save the following YAML as the file `examplepod.yaml`: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: tunepod
  namespace: sysctl-tuning-test
  annotations:
    k8s.v1.cni.cncf.io/networks: |-
      [
        {"name": "allvalidflags"},
        {"name": "allvalidflags"},
        {
          "name": "bond-sysctl-network",
          "interface": "bond0",
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


     * `<allvalidflags>`: The name of the SR-IOV network attachment definition CR. 
     * `<mac>`: Optional: The MAC address for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. To use this feature, you also must specify `{ "mac": true }` in the SriovNetwork object. 
     * `<ips>`: Optional: IP addresses for the SR-IOV device that are allocated from the resource type defined in the SR-IOV network attachment definition CR. Both IPv4 and IPv6 addresses are supported. To use this feature, you also must specify `{ "ips": true }` in the `SriovNetwork` object. 

  3. Apply the YAML: 

```shell-session
$ oc apply -f examplepod.yaml
```


  4. Verify that the pod is created by running the following command: 

```shell-session
$ oc get pod -n sysctl-tuning-test
```


The following is example output: 

```shell-session
NAME      READY   STATUS    RESTARTS   AGE
tunepod   1/1     Running   0          47s
```


  5. Log in to the pod by running the following command: 

```shell-session
$ oc rsh -n sysctl-tuning-test tunepod
```


  6. Verify the values of the configured `sysctl` flag. Find the value `net.ipv6.neigh.IFNAME.base_reachable_time_ms` by running the following command: 

```shell-session
$ sysctl net.ipv6.neigh.bond0.base_reachable_time_ms
```
