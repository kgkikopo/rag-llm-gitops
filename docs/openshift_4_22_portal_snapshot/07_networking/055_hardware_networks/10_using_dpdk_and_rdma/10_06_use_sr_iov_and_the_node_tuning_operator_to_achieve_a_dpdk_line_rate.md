# 10.6. Use SR-IOV and the Node Tuning Operator to achieve a DPDK line rate

You can use the Node Tuning Operator to configure isolated CPUs, hugepages, and a topology scheduler. You can then use the Node Tuning Operator with Single Root I/O Virtualization (SR-IOV) to achieve a specific Data Plane Development Kit (DPDK) line rate. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have installed the SR-IOV Network Operator. 
  * You have logged in as a user with `cluster-admin` privileges. 
  * You have deployed a standalone Node Tuning Operator. 

Note

In previous versions of OpenShift Container Platform, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift applications. In OpenShift Container Platform 4.11 and later, this functionality is part of the Node Tuning Operator. 




**Procedure**

  1. Create a `PerformanceProfile` object based on the following example: 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: performance
spec:
  globallyDisableIrqLoadBalancing: true
  cpu:
    isolated: 21-51,73-103
    reserved: 0-20,52-72
  hugepages:
    defaultHugepagesSize: 1G
    pages:
      - count: 32
        size: 1G
  net:
    userLevelNetworking: true
  numa:
    topologyPolicy: "single-numa-node"
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
```


where: 

`metadata.name`
     Specifies the name of the performance profile. 
`spec.cpu.isolated`
     Specifies the CPUs that are isolated for the application workloads. If Hyper-Threading is enabled on the system, allocate the relevant symbolic links to the `isolated` and `reserved` CPU groups. If the system has multiple non-uniform memory access (NUMA) nodes, allocate CPUs from both NUMAs to both groups. You can also use the Performance Profile Creator for this task. For more information, see _Creating a performance profile_. 
`spec.cpu.reserved`
     Specifies the CPUs that are reserved for the operating system and Kubernetes system daemons. You can also specify a list of devices that will have their queues set to the reserved CPU count. For more information, see _Reducing NIC queues using the Node Tuning Operator_. 
`spec.hugepages.defaultHugepagesSize`
     Specifies the default size of hugepages. 
`spec.hugepages.pages`
     Specifies the number and size of hugepages to allocate. You can specify the NUMA configuration for the hugepages. By default, the system allocates an even number to every NUMA node on the system. 
`spec.net.userLevelNetworking`
     Specifies whether to enable user-level networking. Set to `true` for DPDK workloads. 
`spec.numa.topologyPolicy`
     Specifies the NUMA topology policy. Set to `single-numa-node` to ensure that all resources are allocated from the same NUMA node. 
`spec.nodeSelector`
     Specifies the node selector label for nodes that this performance profile applies to. 

  2. Save the `yaml` file as `mlx-dpdk-perfprofile-policy.yaml`. 
  3. Apply the performance profile using the following command: 

```shell-session
$ oc create -f mlx-dpdk-perfprofile-policy.yaml
```


## 10.6.1. DPDK library for use with container applications

An [optional library](https://github.com/openshift/app-netutil), `app-netutil`, provides several API methods for gathering network information about a pod from within a container running within that pod. 

This library can assist with integrating SR-IOV virtual functions (VFs) in Data Plane Development Kit (DPDK) mode into the container. The library provides both a Golang API and a C API. 

Currently there are three API methods implemented: 

`GetCPUInfo()`
     This function determines which CPUs are available to the container and returns the list. 
`GetHugepages()`
     This function determines the amount of huge page memory requested in the `Pod` spec for each container and returns the values. 
`GetInterfaces()`
     This function determines the set of interfaces in the container and returns the list. The return value includes the interface type and type-specific data for each interface. 

The repository for the library includes a sample Dockerfile to build a container image, `dpdk-app-centos`. The container image can run one of the following DPDK sample applications, depending on an environment variable in the pod specification: `l2fwd`, `l3wd` or `testpmd`. The container image provides an example of integrating the `app-netutil` library into the container image itself. The library can also integrate into an init container. The init container can collect the required data and pass the data to an existing DPDK workload. 

## 10.6.2. Example SR-IOV Network Operator for virtual functions

You can use the Single Root I/O Virtualization (SR-IOV) Network Operator to allocate and configure Virtual Functions (VFs) from SR-IOV-supporting Physical Function NICs on the nodes. 

For more information on deploying the Operator, see _Installing the SR-IOV Network Operator_. For more information on configuring an SR-IOV network device, see _Configuring an SR-IOV network device_. 

There are some differences between running Data Plane Development Kit (DPDK) workloads on Intel VFs and Mellanox VFs. This section provides object configuration examples for both VF types. The following is an example of an `sriovNetworkNodePolicy` object used to run DPDK applications on Intel NICs: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-1
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  needVhostNet: true
  nicSelector:
    pfNames: ["ens3f0"]
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  numVfs: 10
  priority: 99
  resourceName: dpdk_nic_1
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-1
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  needVhostNet: true
  nicSelector:
    pfNames: ["ens3f1"]
  nodeSelector:
  node-role.kubernetes.io/worker-cnf: ""
  numVfs: 10
  priority: 99
  resourceName: dpdk_nic_2
```


where: 

`spec.deviceType`
     For Intel NICs, `deviceType` must be `vfio-pci`. 
`spec.needVhostNet`
     If kernel communication with DPDK workloads is required, set to `true`. This mounts the `/dev/net/tun` and `/dev/vhost-net` devices into the container so the application can create a tap device and connect the tap device to the DPDK workload. 

The following is an example of an `sriovNetworkNodePolicy` object for Mellanox NICs: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-1
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: true
  nicSelector:
    rootDevices:
      - "0000:5e:00.1"
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  numVfs: 5
  priority: 99
  resourceName: dpdk_nic_1
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-2
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: true
  nicSelector:
    rootDevices:
      - "0000:5e:00.0"
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  numVfs: 5
  priority: 99
  resourceName: dpdk_nic_2
```


where: 

`spec.deviceType`
     For Mellanox devices the `deviceType` must be `netdevice`. 
`spec.isRdma`
     For Mellanox devices `isRdma` must be `true`. Mellanox cards are connected to DPDK applications using Flow Bifurcation. This mechanism splits traffic between Linux user space and kernel space, and can enhance line rate processing capability. 

## 10.6.3. Example SR-IOV network operator

The following is an example definition of an `sriovNetwork` object. In this case, Intel and Mellanox configurations are identical: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: dpdk-network-1
  namespace: openshift-sriov-network-operator
spec:
  ipam: '{"type": "host-local","ranges": [[{"subnet": "10.0.1.0/24"}]],"dataDir":
   "/run/my-orchestrator/container-ipam-state-1"}'
  networkNamespace: dpdk-test
  spoofChk: "off"
  trust: "on"
  resourceName: dpdk_nic_1
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: dpdk-network-2
  namespace: openshift-sriov-network-operator
spec:
  ipam: '{"type": "host-local","ranges": [[{"subnet": "10.0.2.0/24"}]],"dataDir":
   "/run/my-orchestrator/container-ipam-state-1"}'
  networkNamespace: dpdk-test
  spoofChk: "off"
  trust: "on"
  resourceName: dpdk_nic_2
```


  * You can use a different IP Address Management (IPAM) implementation, such as Whereabouts. For more information, see _Dynamic IP address assignment configuration with Whereabouts_. 
  * You must request the `networkNamespace` where the network attachment definition will be created. You must create the `sriovNetwork` CR under the `openshift-sriov-network-operator` namespace. 
  * The `resourceName` value must match that of the `resourceName` created under the `sriovNetworkNodePolicy`. 



## 10.6.4. Example DPDK base workload

The following is an example of a Data Plane Development Kit (DPDK) container: 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: dpdk-test
---
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: '[
     {
      "name": "dpdk-network-1",
      "namespace": "dpdk-test"
     },
     {
      "name": "dpdk-network-2",
      "namespace": "dpdk-test"
     }
   ]'
    irq-load-balancing.crio.io: "disable"
    cpu-load-balancing.crio.io: "disable"
  labels:
    app: dpdk
  name: testpmd
  namespace: dpdk-test
spec:
  runtimeClassName: performance-performance
  containers:
    - command:
        - /bin/bash
        - -c
        - sleep INF
      image: registry.redhat.io/openshift4/dpdk-base-rhel8
      imagePullPolicy: Always
      name: dpdk
      resources:
        limits:
          cpu: "16"
          hugepages-1Gi: 8Gi
          memory: 2Gi
        requests:
          cpu: "16"
          hugepages-1Gi: 8Gi
          memory: 2Gi
      securityContext:
        capabilities:
          add:
            - IPC_LOCK
            - SYS_RESOURCE
            - NET_RAW
            - NET_ADMIN
        runAsUser: 0
      volumeMounts:
        - mountPath: /mnt/huge
          name: hugepages
  terminationGracePeriodSeconds: 5
  volumes:
    - emptyDir:
        medium: HugePages
      name: hugepages
```


  * Request the SR-IOV networks you need. Resources for the devices are injected automatically. 
  * Disable the CPU and IRQ load balancing base. See _Disabling interrupt processing for individual pods_ for more information. 
  * Set the `runtimeClass` to `performance-performance`. Do not set the `runtimeClass` to `HostNetwork` or `privileged`. 
  * Request an equal number of resources for requests and limits to start the pod with `Guaranteed` Quality of Service (QoS). 



Note

Do not start the pod with `SLEEP` and then exec into the pod to start the testpmd or the DPDK workload. This can add additional interrupts as the `exec` process is not pinned to any CPU. 

## 10.6.5. Example testpmd script

The following is an example script for running `testpmd`: 

```shell-session
#!/bin/bash
set -ex
export CPU=$(cat /sys/fs/cgroup/cpuset/cpuset.cpus)
echo ${CPU}

dpdk-testpmd -l ${CPU} -a ${PCIDEVICE_OPENSHIFT_IO_DPDK_NIC_1} -a ${PCIDEVICE_OPENSHIFT_IO_DPDK_NIC_2} -n 4 -- -i --nb-cores=15 --rxd=4096 --txd=4096 --rxq=7 --txq=7 --forward-mode=mac --eth-peer=0,50:00:00:00:00:01 --eth-peer=1,50:00:00:00:00:02
```


This example uses two different `sriovNetwork` CRs. The environment variable contains the Virtual Function (VF) PCI address that was allocated for the pod. If you use the same network in the pod definition, you must split the `pciAddress`. It is important to configure the correct MAC addresses of the traffic generator. This example uses custom MAC addresses.
