# 8.20. CPU models

## 8.20.1. Choose a CPU model

You can choose an appropriate CPU model for your virtual machines based on your environment. The host-model CPU provides maximum performance and feature access in homogeneous clusters. CPU models ensure compatibility and migration flexibility in heterogeneous clusters with different CPU types. 

### 8.20.1.1. Host-model CPU for homogeneous clusters

By default, a virtual machine instance (VMI) uses the `host-model` CPU configuration, which selects the CPU model closest to the node’s physical CPU. This gives the VMI all CPU features that the node provides, and suits homogeneous clusters. 

The CPU model chosen by `host-model` is often not a standard named model supported by libvirt, which can include additional CPU features. Libvirt creates a CPU definition that only includes the available features on the initial node. This approach ensures: 

  * The VMI can start successfully on the initial node. 
  * Future live migrations only require the subset of CPU features used in the host-model, even if target nodes have different or additional features. 



#### 8.20.1.1.1. Homogeneous clusters

In a homogeneous cluster, all nodes have similar CPU features. The `host-model` CPU model is recommended for homogeneous clusters, and provides the following benefits: 

  * Provides VMs with the closest match to the physical CPU. 
  * VMs can use all CPU features available on the nodes. 
  * Live migration works smoothly because all nodes share the same CPU features. 



#### 8.20.1.1.2. Live migration with host-model

Since the CPU model and features are determined by the initial node, all the host model required CPU features exposed to the VMI must also exist on any future live migration target nodes. 

OpenShift Virtualization ensures compatibility by: 

  1. Detecting all `host-model-required-features.node.kubevirt.io/<cpuFeature>` labels on the initial node. 
  2. Storing these labels per VMI. 
  3. Using these same required CPU features to set node selectors for all future live migrations. 



This approach guarantees that VM migrations only target nodes that provide the CPU features actually needed by the VMI. 

Important

Target nodes might support more CPU features than required, but they must support at minimum all features used by the VMI. 

### 8.20.1.2. Named CPU models for heterogeneous clusters

You can use a named CPU model to select a specific CPU type for a virtual machine (VM), either for one VM or as a cluster-wide default. In a heterogeneous cluster, a common named model lets a VM migrate to more nodes. 

A node supports a named CPU model only if it includes all required CPU features defined by libvirt for that model. Nodes that support a specific CPU model are labeled with `cpu-model.node.kubevirt.io/<cpuModel>`. OpenShift Virtualization uses these labels to schedule VMs only to compatible nodes. When you configure a named CPU model, the VM receives a node selector that ensures it only runs on nodes labeled with that specific CPU model. 

#### 8.20.1.2.1. Heterogeneous clusters

In a heterogeneous cluster, nodes have different CPU generations or feature sets. 

A virtual machine instance (VMI) inherits the host model CPU feature of the node where it is first scheduled. If the initial node has CPU features unsupported by other nodes, it can prevent the VM from being migrated to them. 

Using a common named CPU model (for example, `EPYC-IBPB` or `Haswell`) is recommended for CPU models in heterogeneous clusters, and provides the following benefits: 

  * Ensures that all nodes selected for migration support the required CPU features. 
  * Maximizes the number of nodes with different CPU types that a VM can migrate to. 
  * Prevents scheduling VMs on nodes that cannot support live migration targets. 



Important

In heterogeneous clusters, using `host-model` can limit live migration options if the initial scheduling node has host model required CPU features that are not available on all other nodes in the cluster. 

## 8.20.2. Configure CPU models

You can configure CPU models for your virtual machines at both the cluster level and individual VM level. Set a cluster-wide default CPU model to automatically apply to all new VMs, or configure a specific CPU model for individual VMs to override the cluster default. 

### 8.20.2.1. Configure the default CPU model

Define a cluster-wide default CPU model. Every new virtual machine (VM) that does not specify its own CPU model uses the default, and runs only on nodes that support it. 

When you set a cluster-wide default CPU model: 

  * Every new virtual machine (VM) that does not have an explicit CPU model defined receives a node selector for the chosen CPU model. 
  * Only nodes labeled with `cpu-model.node.kubevirt.io/<cpuModel>` are eligible to run VMs using the default model. 
  * Nodes that do not support the selected CPU model are not considered during VM scheduling. 



Note

The `defaultCPUModel` is case sensitive and must match a CPU model supported by nodes in your cluster. 

A CPU model configured at the VM level always takes precedence over the cluster-wide default CPU model. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 



**Procedure**

  1. Open the `HyperConverged` CR by running the following command: 

```shell-session
$ oc edit hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
```


  2. Add the `defaultCPUModel` field to the CR and set the value to the name of a CPU model that exists in the cluster: 

```yaml
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
 name: kubevirt-hyperconverged
 namespace: openshift-cnv
spec:
  defaultCPUModel: "EPYC-IBPB"
```


where: 

`EPYC-IBPB`
     Specifies a CPU model that is supported by nodes in your cluster. 

  3. Apply the YAML file to your cluster. 



### 8.20.2.2. Configure a CPU model for a single VM

Set a named CPU model on a single virtual machine (VM) when that VM needs a different CPU type from the cluster-wide default. A per-VM model always takes precedence over the default. 

The VM CPU model depends on the availability of CPU models within the VM and the cluster. 

  * If the VM does not have a defined CPU model, the `defaultCPUModel` is automatically set using the CPU model defined at the cluster-wide level. 
  * If both the VM and the cluster have a defined CPU model, the VM’s CPU model takes precedence. 
  * If neither the VM nor the cluster have a defined CPU model, the host-model is automatically set using the CPU model defined at the host level. 



**Prerequisites**

  * Install the OpenShift CLI (`oc`). 



**Procedure**

  1. To configure a named CPU model for a specific VM, edit the `VirtualMachine` custom resource (CR): 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: myvm
spec:
  template:
    spec:
      domain:
        cpu:
          model: Conroe
```


     * `spec.template.spec.domain.cpu.model` defines the named CPU model for the VM. 

  2. Apply the CR to your cluster. 



## 8.20.3. Schedule virtual machines

You can schedule a virtual machine (VM) on a node by ensuring that the VM’s CPU model and policy attribute are matched for compatibility with the CPU models and policy attributes supported by the node. 

### 8.20.3.1. Set a VM to inherit the node CPU model

Set the CPU model of a virtual machine (VM) to `host-model` so that the VM inherits the CPU model of the node where it is scheduled, and can use the CPU features that the node provides. 

**Procedure**

  * Edit the `domain` spec of your VM configuration file. The following example shows `host-model` being specified for the virtual machine: 

```yaml
apiVersion: kubevirt/v1alpha3
kind: VirtualMachine
metadata:
  name: myvm
spec:
  template:
    spec:
      domain:
        cpu:
          model: host-model
```


    * `spec.template.spec.domain.cpu.model` defines the VM that inherits the CPU model of the node where it is scheduled. 




### 8.20.3.2. Set a VM to run only on nodes with a named CPU model

Set a named CPU model on a virtual machine (VM) so that the scheduler places the VM only on nodes that support that model. 

**Procedure**

  * Edit the `domain` spec of your virtual machine configuration file. The following example shows a specific CPU model defined for a VM: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: myvm
spec:
  template:
    spec:
      domain:
        cpu:
          model: Conroe
# ...
```


    * `spec.template.spec.domain.cpu.model` defines the CPU model for the VM. 




### 8.20.3.3. CPU feature policy attributes

A policy attribute controls how strictly the scheduler enforces a CPU feature that you set on a virtual machine (VM). Use a policy attribute to require a feature, treat it as optional, or forbid it. 

Policy attribute| Description  
---|---  
force  |  The VM is forced to be scheduled on a node. This is true even if the host CPU does not support the VM’s CPU.   
require  |  Default policy that applies to a VM if the VM is not configured with a specific CPU model and feature specification. If a node is not configured to support CPU node discovery with this default policy attribute or any one of the other policy attributes, VMs are not scheduled on that node. Either the host CPU must support the VM’s CPU or the hypervisor must be able to emulate the supported CPU model.   
optional  |  The VM is added to a node if that VM is supported by the host’s physical machine CPU.   
disable  |  The VM cannot be scheduled with CPU node discovery.   
forbid  |  The VM is not scheduled even if the feature is supported by the host CPU and CPU node discovery is enabled.   
Show more

### 8.20.3.4. Set a policy attribute and CPU feature

Set a CPU feature and a policy attribute on a virtual machine (VM) so that the VM runs only where the feature is available. The feature must be supported by the host CPU or emulated by the hypervisor. 

**Procedure**

  * Edit the `domain` spec of your VM configuration file. The following example sets the CPU feature and the `require` policy for a virtual machine (VM): 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: myvm
spec:
  template:
    spec:
      domain:
        cpu:
          features:
            - name: apic
              policy: require
```


    * `spec.template.spec.domain.cpu.features.name` defines the name of the CPU feature for the VM. 
    * `spec.template.spec.domain.cpu.features.policy` defines the policy attribute for the VM. 




### 8.20.3.5. Schedule VMs with a custom scheduler

You can run a virtual machine (VM) under a custom scheduler instead of the default scheduler, so that your own scheduling logic decides which node runs the VM. 

**Prerequisites**

  * A secondary scheduler is configured for your cluster. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * Add the custom scheduler to the VM configuration by editing the `VirtualMachine` manifest. For example: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm-fedora
spec:
  runStrategy: Always
  template:
    spec:
      schedulerName: my-scheduler
      domain:
        devices:
          disks:
            - name: containerdisk
              disk:
                bus: virtio
# ...
```


`schedulerName`
     The name of the custom scheduler. If the `schedulerName` value does not match an existing scheduler, the `virt-launcher` pod stays in a `Pending` state until the specified scheduler is found. 




**Verification**

  * Verify that the VM is using the custom scheduler specified in the `VirtualMachine` manifest by checking the `virt-launcher` pod events: 

    1. View the list of pods in your cluster by entering the following command: 

```shell-session
$ oc get pods
```


Example output: 

```shell-session
NAME                             READY   STATUS    RESTARTS   AGE
virt-launcher-vm-fedora-dpc87    2/2     Running   0          24m
```


    2. Run the following command to display the pod events: 

```shell-session
$ oc describe pod virt-launcher-vm-fedora-dpc87
```


The value of the `From` field in the output verifies that the scheduler name matches the custom scheduler specified in the `VirtualMachine` manifest: 

Example output: 

```shell-session
[...]
Events:
  Type    Reason     Age   From              Message
  ----    ------     ----  ----              -------
  Normal  Scheduled  21m   my-scheduler  Successfully assigned default/virt-launcher-vm-fedora-dpc87 to node01
[...]
```


**Additional resources**

  * [Deploying a secondary scheduler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-secondary-scheduler-configuring-console_secondary-scheduler-configuring)
