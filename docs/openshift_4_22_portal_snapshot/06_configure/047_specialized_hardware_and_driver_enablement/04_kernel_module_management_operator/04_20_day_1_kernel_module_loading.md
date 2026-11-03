# 4.20. Day 1 kernel module loading

Day 1 kernel module loading lets you insert kernel modules during Linux `systemd` initialization on OpenShift Container Platform, before the standard KMM Day 2 loading and a complete initialization of a Linux (RHCOS) server. 

You can use the Machine Config Operator (MCO) when a module must load earlier than full node initialization. 

**Additional resources**

  * [Machine Config Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#machine-config-index)



## 4.20.1. Day 1 supported use cases

Day 1 supported use cases define when OpenShift Container Platform can load out-of-tree (OOT) kernel modules before NetworkManager starts. This functionality does not support loading modules during the `initramfs` stage. 

The following are the conditions needed for Day 1 functionality: 

  * The kernel module is not loaded in the kernel. 
  * The in-tree kernel module is loaded into the kernel, but can be unloaded and replaced by the OOT kernel module. This means that the in-tree module is not referenced by any other kernel modules. 
  * In order for Day 1 functionlity to work, the node must have a functional network interface, that is, an in-tree kernel driver for that interface. The OOT kernel module can be a network driver that will replace the functional network driver. 



## 4.20.2. OOT kernel module loading flow

To load an out-of-tree kernel module during OpenShift Container Platform node boot, you can apply a `MachineConfig` through the Machine Config Operator (MCO). MCO reboots nodes and deploys `systemd` services that pull the kernel module image and swap in-tree modules for OOT modules. 

**Procedure**

  1. Apply a `MachineConfig` resource to the existing running cluster. In order to identify the necessary nodes that need to be updated, you must create an appropriate `MachineConfigPool` resource. 
  2. MCO applies the reboots node by node. On any rebooted node, two new `systemd` services are deployed: `pull` service and `load` service. 
  3. The `load` service is configured to run prior to the `NetworkConfiguration` service. The service tries to pull a predefined kernel module image and then, using that image, to unload an in-tree module and load an OOT kernel module. 
  4. The `pull` service is configured to run after NetworkManager service. The service checks if the preconfigured kernel module image is located on the node’s filesystem. If it is, the service exists normally, and the server continues with the boot process. If not, it pulls the image onto the node and reboots the node afterwards. 



## 4.20.3. The kernel module image

Day 1 kernel module loading in OpenShift Container Platform uses Driver Toolkit-based container images shared with Day 2 KMM builds. These images must contain your out-of-tree kernel modules so the Machine Config Operator can pull and load them during node boot. 

The out-of-tree kernel module should be located under `/opt/lib/modules/${kernelVersion}`. 

**Additional resources**

  * [Driver Toolkit](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/specialized_hardware_and_driver_enablement/driver-toolkit "Chapter 2. Driver Toolkit")



## 4.20.4. In-tree module replacement

Day 1 kernel module loading in OpenShift Container Platform replaces in-tree kernel modules with out-of-tree (OOT) versions when present. If the in-tree module is not loaded, KMM loads the OOT module without affecting the flow. 

## 4.20.5. MCO yaml creation

Kernel Module Management (KMM) exposes a `ProduceMachineConfig` API that generates Machine Config Operator (MCO) YAML for Day 1 out-of-tree kernel module loading on OpenShift Container Platform. You apply the returned manifest to target nodes in a specified `MachineConfigPool` object. 

```plaintext
ProduceMachineConfig(machineConfigName, machineConfigPoolRef, kernelModuleImage, kernelModuleName string) (string, error)
```


The returned output is a string representation of the MCO YAML manifest to be applied. It is up to the customer to apply this YAML. 

The parameters are: 

`machineConfigName`
     The name of the MCO YAML manifest. This parameter is set as the `name` parameter of the metadata of the MCO YAML manifest. 
`machineConfigPoolRef`
     The `MachineConfigPool` name used to identify the targeted nodes. 
`kernelModuleImage`
     The name of the container image that includes the OOT kernel module. 
`kernelModuleName`
     The name of the OOT kernel module. This parameter is used both to unload the in-tree kernel module (if loaded into the kernel) and to load the OOT kernel module. 

The API is located under `pkg/mcproducer` package of the KMM source code. The KMM operator does not need to be running to use the Day 1 functionality. You only need to import the `pkg/mcproducer` package into their operator/utility code, call the API, and apply the produced MCO YAML to the cluster. 

## 4.20.6. The MachineConfigPool

A `MachineConfigPool` objectidentifies a collection of OpenShift Container Platform nodes affected by Machine Config Operator changes. 

```yaml
kind: MachineConfigPool
metadata:
  name: sfc
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker, sfc]}
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/sfc: ""
  paused: false
  maxUnavailable: 1
```


where: 

`spec.machineConfigSelector`
     Specifies labels that match in the MachineConfig. 
`spec.nodeSelector`
     Specifies labels that match on the node. 

There are predefined `MachineConfigPools` in the OCP cluster: 

  * `worker`: Targets all worker nodes in the cluster 
  * `master`: Targets all master nodes in the cluster 



Define the following `MachineConfig` to target the master `MachineConfigPool`: 

```yaml
metadata:
  labels:
    machineconfiguration.opensfhit.io/role: master
```


Define the following `MachineConfig` to target the worker `MachineConfigPool`: 

```yaml
metadata:
  labels:
    machineconfiguration.opensfhit.io/role: worker
```


**Additional resources**

  * [About MachineConfigPool](https://www.redhat.com/en/blog/openshift-container-platform-4-how-does-machine-config-pool-work)
