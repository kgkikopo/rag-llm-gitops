# 8.18. Advanced virtual machine management

## 8.18.1. Working with resource quotas for virtual machines

Manage and control virtual machine resource consumption to prevent overcommitment and ensure stable workload performance. 

Create and manage resource quotas for virtual machines. 

### 8.18.1.1. Set resource quota limits for VMs by using the CLI

OpenShift Virtualization manages CPU and memory limits for virtual machines (VMs) automatically. If a namespace enforces a resource quota that requires limits, you can customize the memory limit ratio or set limits manually so that your VMs comply with the quota. 

By default, the memory limit is set to twice the requested memory and the CPU limit is set to one per vCPU. 

You can customize the memory limit ratio for a specific namespace by adding the `alpha.kubevirt.io/auto-memory-limits-ratio` label to the namespace. For example, the following command sets the memory limit ratio to 1.2: 

```shell-session
$ oc label ns/my-virtualization-project alpha.kubevirt.io/auto-memory-limits-ratio=1.2
```


Warning

Avoid managing resource quota limits manually. To prevent misconfigurations or scheduling issues, rely on the automatic resource limit management provided by OpenShift Virtualization unless you have a specific need to override the defaults. 

Resource quotas that only use requests automatically work with VMs. If your resource quota uses limits, you must manually set resource limits on VMs. Memory resource limits, defined by the `spec.template.spec.domain.resources.limits.memory` value, must be at least 500 MiB, or 2% larger than the `spec.template.spec.domain.memory.guest` value. 

**Procedure**

  1. Set limits for a VM by editing the `VirtualMachine` manifest. For example: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: with-limits
spec:
  runStrategy: Halted
  template:
    spec:
      domain:
        memory:
          guest: 128Mi
        resources:
          limits:
            memory: 256Mi
```


where 

spec.template.spec.domain.memory.guest
     Specifies the actual amount of RAM that is shown to the guest operating system in the VM. 
spec.template.spec.domain.resources.limits.memory
    

Specifies the hard limit for total memory consumption by the `virt-launcher` pod that hosts the VM. This limit must account for the guest operating system RAM plus the hypervisor runtime resource consumption. 

This example configuration is supported because the `spec.template.spec.domain.resources.limits.memory` value is at least `100Mi` larger than the `spec.template.spec.domain.memory.guest` value. 

  2. Save the `VirtualMachine` manifest. 



### 8.18.1.2. Accurate VM resource measurement with AAQ

The Application Aware Quota (AAQ) Operator measures the CPU and memory that your virtual machines (VMs) actually use. The `ResourceQuota` object counts the whole VM pod, including the resources that the hypervisor consumes, so it overstates VM consumption. 

AAQ provides quota enforcement designed for virtualization workloads: 

Kubernetes ResourceQuota
     Measures and enforces resource limits at the pod level. When applied to VMs, it measures the entire VM pod’s resource consumption, including the resources consumed by the hypervisor and the pod infrastructure, which does not reflect actual VM resource allocation. 
Application Aware Quota (AAQ)
     Extends ResourceQuota functionality to accurately measure and enforce VM resource consumption. AAQ understands the virtualization layer and can measure actual virtual CPU and memory allocated to VMs, separate from what the pod itself consumes. 

AAQ supports two types of quotas: 

Project-scoped quotas
     Apply resource limits to a specific namespace or project. These are the most common use case for virtualization workloads. 
Cluster-scoped quotas
     Apply resource limits across the entire cluster. These are useful for advanced scenarios where you need cluster-wide resource enforcement. 

When you enable AAQ, you must configure a quota calculation method. This setting determines how AAQ measures VM resource consumption across your cluster: 

Virtual resources
     Measures only the virtual CPU and memory allocated to virtual machines (VMs), excluding the CPU and memory that the pod runtime consumes. This is the default option for virtualization workloads. 
Virtual Machine Instance (VMI) pod usage
     Measures the total virtual CPU and memory consumption of the VM pod, including both the virtual machine and the pod runtime. 
Dedicated virtual resources
     Measures the virtual CPU and memory resources assigned to virtual machines and their associated pods, tracking quota usage separately for each type. 

### 8.18.1.3. Enable the Application Aware Quota Operator

Enable the Application Aware Quota (AAQ) Operator and choose a quota calculation method in the web console. Using the web console avoids editing the `HyperConverged` custom resource (CR) by hand. 

**Prerequisites**

  * You have cluster administrator privileges. 
  * The OpenShift Virtualization operator is installed and running. 



**Procedure**

  1. In the OpenShift Container Platform web console, click **Virtualization** **Settings**. 
  2. Under **Resource Management** , toggle the **Application Aware Quotas (AAQ)** to On. 

The operator deployment begins automatically. The status changes from **Disabled** to **Enabled** after the operator pods are running. 

  3. Optional: Click the **Edit** icon next to the **Quota calculation method** field to change the calculation method. 

A modal dialog is displayed with the following options: 

     * **Virtual resources** : Measures only the virtual CPU and memory allocated to virtual machines (VMs), excluding the CPU and memory that the pod runtime consumes. This is the default option for virtualization workloads. 
     * **Virtual Machine Instance (VMI) pod usage** : Measures the total virtual CPU and memory consumption of the VM pod, including both the virtual machine and the pod runtime. 
     * **Dedicated virtual resources** : Measures the virtual CPU and memory resources assigned to virtual machines and their associated pods, tracking quota usage separately for each type. 

  4. Select your preferred quota calculation method and click **Save**. 



**Verification**

  1. Verify that a new **Quotas** option is displayed in the left navigation menu under **Virtualization**. This indicates that AAQ is ready for quota creation and management. 



### 8.18.1.4. Create VM quotas by using the web console

Use the guided form in the OpenShift Container Platform web console to create an Application Aware Quota (AAQ) that limits virtual machine (VM) resource use in a project. The form is the simplest way to set quota limits without writing YAML. 

**Prerequisites**

  * You have cluster administrator privileges. 
  * The Application Aware Quota Operator is enabled in your cluster. See [Enable the Application Aware Quota Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-enabling-aaq-operator_virt-working-with-resource-quotas-for-vms "8.18.1.3. Enable the Application Aware Quota Operator"). 
  * The project where you want to create the quota exists. 



**Procedure**

  1. In the OpenShift Container Platform web console, click **Virtualization** **Quotas**. 
  2. Click **Create quota**. 
  3. In the dropdown menu, select **With form**. 

The create quota form is displayed. 

  4. Enter a name for your quota in the **Name** field. 

The name must be unique within the project. 

  5. Select the project where you want to apply this quota. 

By default, the current project is selected. You can click the dropdown to select a different project if needed. 

Note

If a Kubernetes `ResourceQuota` already exists in the selected project, an alert is displayed with a link to view the existing ResourceQuota. You can still create the AAQ quota, but both quotas will apply to the project. 

  6. Configure CPU, memory, and VMI limits for the quota: 

The fields displayed vary based on the selected quota calculation method. For example: 

     * For the `Virtual resources` or `Dedicated virtual resources` quota calculation method, the quotas exclude the resources that the pod consumes: 

       * Use the **vCPU allocation** field to set the maximum number of virtual CPUs permitted for all VMs in the project, excluding the CPU that infrastructure consumes. 
       * Use the **Virtual memory allocation** field to set the maximum memory capacity, in GiB, excluding the memory that infrastructure consumes. 
       * Use the **VMI limits** field to set the maximum number of virtual machine instances. 

     * For the `Virtual Machine Instance (VMI) pod usage` quota calculation method, the quotas include the resources that the pod consumes: 

       * Use the **CPU allocation** field to set the maximum number of CPU cores for pods that run VM workloads 
       * Use the **Memory allocation** field to set the maximum memory capacity, in GiB, for pods that run VM workloads. 
       * Use the **VMI limits** field to set the maximum number of virtual machine instances. 

Note

The resources consumed by live migration are excluded from the `Virtual Machine Instance (VMI) pod usage` quota calculation method. 

  7. Review the configuration and click **Create**. 

The quota is created and you are redirected to the quota details page. The new quota is now active and enforcing resource limits on virtual machines in the selected project. 




**Verification**

  1. In the OpenShift Container Platform web console, click **Virtualization** **Quotas**. 
  2. In the quotas list, locate your newly created quota. 
  3. Verify that the quota name is displayed in the list with the correct project and resource limits configured. 
  4. Click the quota name to open its details page and confirm all settings are correct. 



### 8.18.1.5. Manage VM quotas by using the list view

You can use the **Quotas** page in the OpenShift Container Platform web console to view the status and usage of every Application Aware Quota (AAQ) in your cluster, and to create, edit, or delete a quota, without searching through individual projects. 

**Prerequisites**

  * You have cluster administrator privileges. 
  * The Application Aware Quota Operator is enabled in your cluster. 
  * At least one Application Aware Quota exists in a namespace that matches the label selector configured in the HyperConverged Operator (HCO). 



**Procedure**

  1. In the OpenShift Container Platform web console, click **Virtualization** **Quotas**. 

The quotas list view is displayed, showing all project-scoped AAQ quotas by default. 

  2. Click the **Cluster-scoped quotas** tab to view cluster scoped quotas. 

This tab is displayed only if cluster-scoped quotas have been defined in your cluster. 

Note

Cluster-scoped quotas can only be created or edited using YAML. The form-based creation option is not available for cluster-scoped quotas due to their complexity. 

  3. To view detailed information about a specific quota, click the quota name to open the quota details page. 
  4. To edit a quota, click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) at the end of the quota row 

     1. Select **Edit quota**. 

The edit form is displayed with the current quota configuration. 

     2. Click **Save** after you have completed modifying the resource limits. 

Note

If the quota was initially created with advanced settings via YAML, clicking **Edit quota** opens the YAML editor instead of the form. 

  5. To delete a quota, click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) at the end of the quota row and select **Delete quota**. A confirmation dialog is displayed. 

     1. Click **Delete** to remove the quota. 

Warning

Deleting a quota removes all resource enforcement for the quota. Virtual machines in the affected project are no longer subject to the quota limits. 

  6. To create a new quota from the list view, click **Create quota**. 

     1. Select an option from the dropdown menu: 

        * **With form** : Opens the form-based creation experience for simple VM quota use cases. 
        * **With YAML** : Opens the YAML editor for advanced quota configurations that include pod limits or other resource types. 




### 8.18.1.6. Manage VM quota details by using the web console

You can use the **Quota details** page in the OpenShift Container Platform web console to review the resource limits, current usage, and utilization charts for an Application Aware Quota (AAQ), so you can tell how close a project is to its limits. 

Note

Cluster scoped quotas show only the YAML definition due to the complexity that these quotas require. 

**Prerequisites**

  * You have cluster administrator privileges. 
  * The Application Aware Quota Operator is enabled in your cluster. 
  * An Application Aware Quota exists in your cluster. 



**Procedure**

  1. In the OpenShift Container Platform web console, click **Virtualization** **Quotas**. 
  2. Click the quota name to open the **Quota details** view. 

The **Quota details** view displays visual indicators, quota metadata, and tabulated data: 

     * Circular utilization charts visually represent resource consumption in your project 
     * The **Details** element provides metadata such as the Quota name, scope, applied labels and project. 
     * The **Quota details** element provides a tabulated views that display the current and maximum utilization of each resource type. 

Note

If a Kubernetes `ResourceQuota` also exists in the same project as this AAQ quota, an alert is displayed at the top of the details page with a link to view the ResourceQuota. Both quotas apply simultaneously to the project. 

  3. Optional: Click the **YAML** tab to review the resource configuration of the quota. 
  4. Optional: Use the **Actions** panel to edit or delete the quota. 



### 8.18.1.7. Additional resources

  * [Resource quotas per project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#quotas-setting-per-project)
  * [Resource quotas across many projects](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#quotas-setting-across-multiple-projects)
  * [Understanding the Application Aware Quota operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-understanding-aaq-operator_virt-working-with-resource-quotas-for-vms "8.18.1.2. Accurate VM resource measurement with AAQ")
  * [Enabling the Application Aware Quota operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-enabling-aaq-operator_virt-working-with-resource-quotas-for-vms "8.18.1.3. Enable the Application Aware Quota Operator")
  * [Creating virtual machine quotas using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-creating-vm-quotas-web_virt-working-with-resource-quotas-for-vms "8.18.1.4. Create VM quotas by using the web console")
  * [Managing virtual machine quotas using the list view](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-managing-quotas-list-web_virt-working-with-resource-quotas-for-vms "8.18.1.5. Manage VM quotas by using the list view")
  * [Managing virtual machine quota details using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-managing-quota-details-web_virt-working-with-resource-quotas-for-vms "8.18.1.6. Manage VM quota details by using the web console")



## 8.18.2. Configuring the Application-Aware Quota (AAQ) Operator

You can use the Application-Aware Quota (AAQ) Operator to customize and manage resource quotas for individual components in an OpenShift Container Platform cluster. 

### 8.18.2.1. The AAQ Operator

The Application Aware Quota (AAQ) Operator manages quotas for clusters that run virtual machines (VMs). Unlike the native `ResourceQuota` object, AAQ accounts for the resources that live migration and VM infrastructure consume, so a quota does not block a VM migration or an upgrade. 

In a multitenant cluster environment, where multiple workloads operate on shared infrastructure and resources, using the Kubernetes native `ResourceQuota` object to limit aggregate CPU and memory consumption creates live migration challenges for OpenShift Virtualization workloads, because the quota also counts the resources that VM infrastructure consumes. 

OpenShift Virtualization requires significant compute resource allocation to handle virtual machine (VM) live migrations and to run the VM infrastructure itself. When upgrading OpenShift Virtualization, you must migrate VMs to upgrade the `virt-launcher` pod. However, migrating a VM in the presence of a resource quota can cause the migration, and subsequently the upgrade, to fail. 

With AAQ, you can allocate resources for VMs without interfering with cluster-level activities such as upgrades and node maintenance. The AAQ Operator also supports non-compute resources which eliminates the need to manage both the native resource quota and AAQ API objects separately. 

#### 8.18.2.1.1. AAQ Operator controller and custom resources

The AAQ Operator introduces two new API objects defined as custom resource definitions (CRDs) for managing alternative quota implementations across multiple namespaces: 

  * `ApplicationAwareResourceQuota`: Sets aggregate quota restrictions enforced per namespace. The `ApplicationAwareResourceQuota` API is compatible with the native `ResourceQuota` object and shares the same specification and status definitions. 

Example manifest: 

```yaml
apiVersion: aaq.kubevirt.io/v1alpha1
kind: ApplicationAwareResourceQuota
metadata:
  name: example-resource-quota
spec:
  hard:
    requests.memory: 1Gi
    limits.memory: 1Gi
    requests.cpu/vmi: "1"
    requests.memory/vmi: 1Gi
# ...
```


    * `spec.hard.requests.cpu/vmi` defines the maximum amount of CPU that is allowed for VM workloads in the default namespace. 
    * `spec.hard.requests.memory/vmi` defines the maximum amount of RAM that is allowed for VM workloads in the default namespace. 

  * `ApplicationAwareClusterResourceQuota`: Mirrors the `ApplicationAwareResourceQuota` object at a cluster scope. It is compatible with the native `ClusterResourceQuota` API object and shares the same specification and status definitions. When creating an AAQ cluster quota, you can select multiple namespaces based on annotation selection, label selection, or both by editing the `spec.selector.labels` or `spec.selector.annotations` fields. You can only create an `ApplicationAwareClusterResourceQuota` object if the `spec.applicationAwareConfig.allowApplicationAwareClusterResourceQuota` field in the `HyperConverged` custom resource (CR) is set to `true`. 

Example manifest: 

```yaml
apiVersion: aaq.kubevirt.io/v1alpha1
kind: ApplicationAwareClusterResourceQuota
metadata:
  name: example-resource-quota
spec:
  quota:
    hard:
      requests.memory: 1Gi
      limits.memory: 1Gi
      requests.cpu/vmi: "1"
      requests.memory/vmi: 1Gi
  selector:
    annotations: null
    labels:
      matchLabels:
        kubernetes.io/metadata.name: default
# ...
```


Note

If both `spec.selector.labels` and `spec.selector.annotations` fields are set, only namespaces that match both are selected. 




The AAQ controller uses a scheduling gate mechanism to evaluate whether there is enough of a resource available to run a workload. If so, the scheduling gate is removed from the pod and it is considered ready for scheduling. The quota usage status is updated to indicate how much of the quota is used. 

If the CPU and memory requests and limits for the workload exceed the enforced quota usage limit, the pod remains in `SchedulingGated` status until there is enough quota available. The AAQ controller creates an event of type `Warning` with details on why the quota was exceeded. You can view the event details by using the `oc get events` command. 

Important

Pods that have the `spec.nodeName` field set to a specific node cannot use namespaces that match the `spec.namespaceSelector` labels defined in the `HyperConverged` CR. 

### 8.18.2.2. Enable the Application Aware Quota Operator

Enable the Application Aware Quota (AAQ) Operator and choose a quota calculation method in the web console. Using the web console avoids editing the `HyperConverged` custom resource (CR) by hand. 

**Prerequisites**

  * You have cluster administrator privileges. 
  * The OpenShift Virtualization operator is installed and running. 



**Procedure**

  1. In the OpenShift Container Platform web console, click **Virtualization** **Settings**. 
  2. Under **Resource Management** , toggle the **Application Aware Quotas (AAQ)** to On. 

The operator deployment begins automatically. The status changes from **Disabled** to **Enabled** after the operator pods are running. 

  3. Optional: Click the **Edit** icon next to the **Quota calculation method** field to change the calculation method. 

A modal dialog is displayed with the following options: 

     * **Virtual resources** : Measures only the virtual CPU and memory allocated to virtual machines (VMs), excluding the CPU and memory that the pod runtime consumes. This is the default option for virtualization workloads. 
     * **Virtual Machine Instance (VMI) pod usage** : Measures the total virtual CPU and memory consumption of the VM pod, including both the virtual machine and the pod runtime. 
     * **Dedicated virtual resources** : Measures the virtual CPU and memory resources assigned to virtual machines and their associated pods, tracking quota usage separately for each type. 

  4. Select your preferred quota calculation method and click **Save**. 



**Verification**

  1. Verify that a new **Quotas** option is displayed in the left navigation menu under **Virtualization**. This indicates that AAQ is ready for quota creation and management. 



### 8.18.2.3. Configure the AAQ Operator by using the CLI

Configure the Application Aware Quota (AAQ) Operator to control how AAQ counts virtual machine (VM) resources and which namespaces it applies to, so that quota enforcement matches how your teams use the cluster. 

**Prerequisites**

  * You have access to the cluster as a user with `cluster-admin` privileges. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * Update the `HyperConverged` CR by running the following command: 

```shell-session
$ oc patch hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv --type merge -p '{
  "spec": {
    "applicationAwareConfig": {
      "vmiCalcConfigName": "DedicatedVirtualResources",
      "namespaceSelector": {
        "matchLabels": {
          "app": "my-app"
        }
      },
      "allowApplicationAwareClusterResourceQuota": true
    }
  }
}'
```


where: 

`vmiCalcConfigName`
    

Specifies how resource counting is managed for pods that run virtual machine (VM) workloads. Possible values are: 

    * `VmiPodUsage`: Counts compute resources for pods associated with VMs in the same way as native resource quotas and excludes migration-related resources. 
    * `VirtualResources`: Counts compute resources based on the VM specifications, using the VM RAM size for memory and virtual CPUs for processing. 
    * `DedicatedVirtualResources` (default): Similar to `VirtualResources`, but separates resource tracking for pods associated with VMs by adding a `/vmi` suffix to CPU and memory resource names. For example, `requests.cpu/vmi` and `requests.memory/vmi`. 

`namespaceSelector`
     Determines the namespaces for which an AAQ scheduling gate is added to pods when they are created. If a namespace selector is not defined, the AAQ Operator targets namespaces with the `application-aware-quota/enable-gating` label as default. 
`allowApplicationAwareClusterResourceQuota`
     If set to `true`, you can create and manage the `ApplicationAwareClusterResourceQuota` object. Setting this attribute to `true` can increase scheduling time. 




### 8.18.2.4. Additional resources

  * [Resource quotas per project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#quotas-setting-per-project)
  * [Resource quotas across multiple projects](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/building_applications/#quotas-setting-across-multiple-projects)
  * [`ResourceQuota` API reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#resourcequota-v1)
  * [`ClusterResourceQuota` API reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#clusterresourcequota-quota-openshift-io-v1)
  * [Pod scheduling gates specification](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#spec-schedulinggates)
  * [Viewing system event information in an OpenShift Container Platform cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-containers-events)



## 8.18.3. Specifying nodes for virtual machines

You can place virtual machines (VMs) on specific nodes by using node placement rules. 

### 8.18.3.1. Node placement rules for VMs

Node placement rules control which nodes a virtual machine (VM) can run on. Use them to spread VMs across nodes for fault tolerance, to keep related VMs together, or to place a VM on a node with hardware that the VM requires. 

You might want to do this if: 

  * You have several VMs. To ensure fault tolerance, you want them to run on different nodes. 
  * You have two chatty VMs. To avoid redundant inter-node routing, you want the VMs to run on the same node. 
  * Your VMs require specific hardware features that are not present on all available nodes. 
  * You have a pod that adds capabilities to a node, and you want to place a VM on that node so that it can use those capabilities. 



Note

Virtual machine placement relies on any existing node placement rules for workloads. If workloads are excluded from specific nodes on the component level, virtual machines cannot be placed on those nodes. 

You can use the following rule types in the `spec` field of a `VirtualMachine` manifest: 

`nodeSelector`
     Allows virtual machines to be scheduled on nodes that are labeled with the key-value pair or pairs that you specify in this field. The node must have labels that exactly match all listed pairs. 
`affinity`
     Enables you to use more expressive syntax to set rules that match nodes with virtual machines. For example, you can specify that a rule is a preference, rather than a hard requirement, so that virtual machines are still scheduled if the rule is not satisfied. Pod affinity, pod anti-affinity, and node affinity are supported for virtual machine placement. Pod affinity works for virtual machines because the `VirtualMachine` workload type is based on the `Pod` object. 
`tolerations`
    

Allows virtual machines to be scheduled on nodes that have matching taints. If a taint is applied to a node, that node only accepts virtual machines that tolerate the taint. 

Note

Affinity rules only apply during scheduling. OpenShift Container Platform does not reschedule running workloads if the constraints are no longer met. 

### 8.18.3.2. Node placement examples

The following example YAML file snippets use `nodePlacement`, `affinity`, and `tolerations` fields to customize node placement for virtual machines. 

#### 8.18.3.2.1. VM node placement with nodeSelector

Use a `nodeSelector` rule to run a virtual machine (VM) only on nodes that carry every label you specify. 

In this example, the virtual machine requires a node that has metadata containing both `example-key-1 = example-value-1` and `example-key-2 = example-value-2` labels. 

Warning

If there are no nodes that fit this description, the virtual machine is not scheduled. 

**Example 8.1. Example VM manifest**

```yaml
metadata:
  name: example-vm-node-selector
apiVersion: kubevirt.io/v1
kind: VirtualMachine
spec:
  template:
    spec:
      nodeSelector:
        example-key-1: example-value-1
        example-key-2: example-value-2
# ...
```


#### 8.18.3.2.2. VM node placement with pod affinity and pod anti-affinity

Use pod affinity and pod anti-affinity rules to place a virtual machine (VM) on the same node as specific pods, or away from them. 

In this example, the VM must be scheduled on a node that has a running pod with the label `example-key-1 = example-value-1`. If there is no such pod running on any node, the VM is not scheduled. 

If possible, the VM is not scheduled on a node that has any pod with the label `example-key-2 = example-value-2`. However, if all candidate nodes have a pod with this label, the scheduler ignores this constraint. 

**Example 8.2. Example VM manifest**

```yaml
metadata:
  name: example-vm-pod-affinity
apiVersion: kubevirt.io/v1
kind: VirtualMachine
spec:
  template:
    spec:
      affinity:
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: example-key-1
                operator: In
                values:
                - example-value-1
            topologyKey: kubernetes.io/hostname
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: example-key-2
                  operator: In
                  values:
                  - example-value-2
              topologyKey: kubernetes.io/hostname
# ...
```


  * If you use the `requiredDuringSchedulingIgnoredDuringExecution` rule type, the VM is not scheduled if the constraint is not met. 
  * If you use the `preferredDuringSchedulingIgnoredDuringExecution` rule type, the VM is still scheduled if the constraint is not met, provided that all required constraints are met. 



#### 8.18.3.2.3. VM node placement with node affinity

Use a node affinity rule to run a virtual machine (VM) on nodes that match the labels you specify, as either a hard requirement or a preference. 

In this example, the VM must be scheduled on a node that has the label `example.io/example-key = example-value-1` or the label `example.io/example-key = example-value-2`. The constraint is met if only one of the labels is present on the node. If neither label is present, the VM is not scheduled. 

If possible, the scheduler avoids nodes that have the label `example-node-label-key = example-node-label-value`. However, if all candidate nodes have this label, the scheduler ignores this constraint. 

**Example 8.3. Example VM manifest**

```yaml
metadata:
  name: example-vm-node-affinity
apiVersion: kubevirt.io/v1
kind: VirtualMachine
spec:
  template:
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: example.io/example-key
                operator: In
                values:
                - example-value-1
                - example-value-2
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 1
            preference:
              matchExpressions:
              - key: example-node-label-key
                operator: In
                values:
                - example-node-label-value
# ...
```


  * If you use the `requiredDuringSchedulingIgnoredDuringExecution` rule type, the VM is not scheduled if the constraint is not met. 
  * If you use the `preferredDuringSchedulingIgnoredDuringExecution` rule type, the VM is still scheduled if the constraint is not met, provided that all required constraints are met. 



#### 8.18.3.2.4. VM node placement with tolerations

Use tolerations to let a virtual machine (VM) run on nodes that are reserved by a taint, such as nodes set aside for virtualization workloads. 

In this example, nodes that are reserved for virtual machines are already tainted with `key=virtualization:NoSchedule`. Because this virtual machine has matching `tolerations`, it can schedule onto the tainted nodes. 

Note

A virtual machine that tolerates a taint is not required to schedule onto a node with that taint. 

**Example 8.4. Example VM manifest**

```yaml
metadata:
  name: example-vm-tolerations
apiVersion: kubevirt.io/v1
kind: VirtualMachine
spec:
  tolerations:
  - key: "key"
    operator: "Equal"
    value: "virtualization"
    effect: "NoSchedule"
# ...
```


### 8.18.3.3. Additional resources

  * [Specifying nodes for virtualization components](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/postinstallation-configuration#virt-node-placement-virt-components "5.2. Specifying nodes for OpenShift Virtualization components")
  * [Placing pods on specific nodes using node selectors](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-scheduler-node-selectors)
  * [Controlling pod placement on nodes using node affinity rules](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-scheduler-node-affinity)
  * [Controlling pod placement using node taints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-scheduler-taints-tolerations)



## 8.18.4. Using UEFI mode for virtual machines

You can boot a virtual machine (VM) in Unified Extensible Firmware Interface (UEFI) mode for faster boot times, the ability to boot to larger disks, and added security features. 

### 8.18.4.1. About UEFI mode for virtual machines

Unified Extensible Firmware Interface (UEFI), like legacy BIOS, initializes hardware components and operating system image files when a computer starts. UEFI supports more modern features and customization options than BIOS, enabling faster boot times. 

It stores all the information about initialization and startup in a file with a `.efi` extension, which is stored on a special partition called EFI System Partition (ESP). The ESP also contains the boot loader programs for the operating system that is installed on the computer. 

### 8.18.4.2. Boot virtual machines in UEFI mode

You can configure a virtual machine to boot in UEFI mode by editing the `VirtualMachine` manifest. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 



**Procedure**

  1. To boot a virtual machine (VM) in UEFI mode with secure boot active, edit or create a `VirtualMachine` manifest file. Use the `spec.firmware.bootloader` stanza to configure UEFI mode: 

```yaml
apiversion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  labels:
    special: vm-secureboot
  name: vm-secureboot
spec:
  template:
    metadata:
      labels:
        special: vm-secureboot
    spec:
      domain:
        devices:
          disks:
          - disk:
              bus: virtio
            name: containerdisk
        features:
          acpi: {}
          smm:
            enabled: true
        firmware:
          bootloader:
            efi:
              secureBoot: true
# ...
```


     * You must set `spec.template.spec.domain.features.ssm.enabled` to have a value of `true`. 
     * If `spec.template.spec.domain.firmware.bootloader.efi.secureBoot` is set to `true`, then UEFI mode is required. However, you can enable UEFI mode without using Secure Boot. 

  2. Apply the manifest to your cluster by running the following command: 

```shell-session
$ oc create -f <file_name>.yaml
```


### 8.18.4.3. Configure VMs with persistent EFI

You can configure a VM to have EFI persistence enabled by editing its manifest file. 

**Procedure**

  * Edit the VM manifest file and save to apply settings. 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: vm
spec:
  template:
    spec:
      domain:
        firmware:
          bootloader:
            efi:
              persistent: true
# ...
```


## 8.18.5. Configuring PXE booting for virtual machines

PXE booting, or network booting, allows a computer to boot and load an operating system or other program without requiring a locally attached storage device. For example, you can use it to choose your desired OS image from a PXE server when deploying a new host. 

### 8.18.5.1. PXE boot a VM with a specified MAC address

You can boot a virtual machine (VM) over the network by creating a `NetworkAttachmentDefinition` object for your PXE network. Then, reference the `NetworkAttachmentDefinition` in your VM instance configuration file, `VirtualMachine`, before you start the VM instance. 

You can also specify a MAC address in the `VirtualMachine` configuration, if required by the PXE server. 

**Prerequisites**

  * A Linux bridge must be connected. 
  * The PXE server must be connected to the same VLAN as the bridge. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Configure a PXE network on the cluster: 

     1. Create the network attachment definition file for PXE network `pxe-net-conf`: 

```yaml
apiVersion: "k8s.cni.cncf.io/v1"
kind: NetworkAttachmentDefinition
metadata:
  name: pxe-net-conf
spec:
  config: |
    {
      "cniVersion": "0.3.1",
      "name": "pxe-net-conf",
      "type": "bridge",
      "bridge": "bridge-interface",
      "macspoofchk": false,
      "vlan": 100,
      "disableContainerInterface": true,
      "preserveDefaultVlan": false
    }
```


        * `metadata.name` specifies the name for the `NetworkAttachmentDefinition` object. 
        * `spec.config.name` specifies the name for the configuration. It is recommended to match the configuration name to the `name` value of the network attachment definition. 
        * `spec.config.type` specifies the actual name of the Container Network Interface (CNI) plugin that provides the network for this network attachment definition. This example uses a Linux bridge CNI plugin. You can also use an OVN-Kubernetes localnet or an SR-IOV CNI plugin. 
        * `spec.config.bridge` specifies the name of the Linux bridge configured on the node. 
        * `spec.config.macspoofchk` is an optional flag to enable the MAC spoof check. When set to `true`, you cannot change the MAC address of the pod or guest interface. This attribute allows only a single MAC address to exit the pod, which provides security against a MAC spoofing attack. 
        * `spec.config.vlan` is an optional VLAN tag. No additional VLAN configuration is required on the node network configuration policy. 
        * `spec.config.preserveDefaultVlan` is an optional flag that indicates whether the VM connects to the bridge through the default VLAN. The default value is `true`. 

  2. Create the network attachment definition by using the file you created in the previous step: 

```shell-session
$ oc create -f pxe-net-conf.yaml
```


  3. Edit the virtual machine instance configuration file to include the details of the interface and network. 

     1. Specify the network and MAC address, if required by the PXE server. If the MAC address is not specified, a value is assigned automatically. 

Ensure that `bootOrder` is set to `1` so that the interface boots first. In this example, the interface is connected to a network called `<pxe-net>`: 

```yaml
interfaces:
- masquerade: {}
  name: default
- bridge: {}
  name: pxe-net
  macAddress: de:00:00:00:00:de
  bootOrder: 1
```


Note

Boot order is global for interfaces and disks. 

     2. Assign a boot device number to the disk to ensure proper booting after operating system provisioning. 

Set the disk `bootOrder` value to `2`: 

```yaml
devices:
  disks:
  - disk:
      bus: virtio
    name: containerdisk
    bootOrder: 2
```


     3. Specify that the network is connected to the previously created network attachment definition. In this scenario, `<pxe-net>` is connected to the network attachment definition called `<pxe-net-conf>`: 

```yaml
networks:
- name: default
  pod: {}
- name: pxe-net
  multus:
    networkName: pxe-net-conf
```


  4. Create the virtual machine instance: 

```shell-session
$ oc create -f vmi-pxe-boot.yaml
```


Example output: 

```shell-session
  virtualmachineinstance.kubevirt.io "vmi-pxe-boot" created
```


  5. Wait for the virtual machine instance to run: 

```shell-session
$ oc get vmi vmi-pxe-boot -o yaml | grep -i phase
  phase: Running
```


  6. View the virtual machine instance using VNC: 

```shell-session
$ virtctl vnc vmi-pxe-boot
```


  7. Watch the boot screen to verify that the PXE boot is successful. 
  8. Log in to the virtual machine instance: 

```shell-session
$ virtctl console vmi-pxe-boot
```


**Verification**

  1. Verify the interfaces and MAC address on the virtual machine and that the interface connected to the bridge has the specified MAC address. In this case, we used `eth1` for the PXE boot, without an IP address. The other interface, `eth0`, got an IP address from OpenShift Container Platform. 

```shell-session
$ ip addr
```


Example output: 

```shell-session
...
3. eth1: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
   link/ether de:00:00:00:00:de brd ff:ff:ff:ff:ff:ff
```


### 8.18.5.2. OpenShift Virtualization networking glossary

Definitions of key OpenShift Virtualization networking terms and technologies. 

Container Network Interface (CNI)
     A [Cloud Native Computing Foundation](https://www.cncf.io/) project, focused on container network connectivity. OpenShift Virtualization uses CNI plugins to build upon the basic Kubernetes networking functionality. 
Multus
     A "meta" CNI plugin that allows multiple CNIs to exist so that a pod or virtual machine can use the interfaces it needs. 
Custom resource definition (CRD)
     A [Kubernetes](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) API resource that allows you to define custom resources, or an object defined by using the CRD API resource. 
`NetworkAttachmentDefinition`
     A CRD introduced by the Multus project that allows you to attach pods, virtual machines, and virtual machine instances to one or more networks. 
`UserDefinedNetwork`
     A namespace-scoped CRD introduced by the user-defined network (UDN) API that can be used to create a tenant network that isolates the tenant namespace from other namespaces. 
`ClusterUserDefinedNetwork`
     A cluster-scoped CRD introduced by the user-defined network API that cluster administrators can use to create a shared network across multiple namespaces. 
`NodeNetworkConfigurationPolicy`
     A CRD introduced by the nmstate project, describing the requested network configuration on nodes. You update the node network configuration, including adding and removing interfaces, by applying a `NodeNetworkConfigurationPolicy` manifest to the cluster. 

## 8.18.6. Using huge pages with virtual machines

You can use huge pages as backing memory for virtual machines in your cluster. 

### 8.18.6.1. What huge pages do

To optimize memory mapping efficiency, understand the function of huge pages. Unlike standard 4Ki blocks, huge pages are larger memory segments that reduce the tracking load on the translation lookaside buffer (TLB) hardware cache. 

Memory is managed in blocks known as pages. On most systems, a page is 4Ki; 1Mi of memory is equal to 256 pages; 1Gi of memory is 256,000 pages, and so on. CPUs have a built-in memory management unit that manages a list of these pages in hardware. The translation lookaside buffer (TLB) is a small hardware cache of virtual-to-physical page mappings. If the virtual address passed in a hardware instruction can be found in the TLB, the mapping can be determined quickly. If not, a TLB miss occurs, and the system falls back to slower, software-based address translation, resulting in performance issues. Since the size of the TLB is fixed, the only way to reduce the chance of a TLB miss is to increase the page size. 

A huge page is a memory page that is larger than 4Ki. On x86_64 architectures, there are two common huge page sizes: 2Mi and 1Gi. Sizes vary on other architectures. To use huge pages, code must be written so that applications are aware of them. Transparent huge pages (THP) attempt to automate the management of huge pages without application knowledge, but they have limitations. In particular, they are limited to 2Mi page sizes. THP can lead to performance degradation on nodes with high memory utilization or fragmentation because of defragmenting efforts of THP, which can lock memory pages. For this reason, some applications might be designed to or recommend usage of pre-allocated huge pages instead of THP. 

In OpenShift Virtualization, virtual machines can be configured to consume pre-allocated huge pages. 

### 8.18.6.2. Map VM memory more efficiently with huge pages

Configure a virtual machine (VM) to use pre-allocated huge pages so that the VM’s memory is mapped more efficiently than with standard 4Ki pages. 

The memory request must be divisible by the page size. For example, you cannot request `500Mi` memory with a page size of `1Gi`. 

Note

The memory layouts of the host and the guest operating system are unrelated. Huge pages requested in the virtual machine manifest apply to QEMU. Huge pages inside the guest can only be configured based on the amount of available memory of the virtual machine instance. 

If you edit a running virtual machine, the virtual machine must be rebooted for the changes to take effect. 

**Prerequisites**

  * Nodes must have pre-allocated huge pages configured. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. In your virtual machine configuration, add the `resources.requests.memory` and `memory.hugepages.pageSize` parameters to the `spec.domain`. The following configuration snippet is for a virtual machine that requests a total of `4Gi` memory with a page size of `1Gi`: 

```yaml
kind: VirtualMachine
# ...
spec:
  domain:
    resources:
      requests:
        memory: "4Gi"
    memory:
      hugepages:
        pageSize: "1Gi"
# ...
```


     * `memory` defines the total amount of memory requested for the virtual machine. This value must be divisible by the page size. 
     * `pageSize` defines the size of each huge page. Valid values for x86_64 architecture are `1Gi` and `2Mi`. The page size must be smaller than the requested memory. 

  2. Apply the virtual machine configuration: 

```shell-session
$ oc apply -f <virtual_machine>.yaml
```


## 8.18.7. Enabling dedicated resources for virtual machines

To improve performance, you can dedicate node resources, such as CPU, to a virtual machine. 

### 8.18.7.1. Exclusive CPU use for predictable VM latency

Dedicated resources give a virtual machine (VM) workload exclusive use of its CPUs, which improves VM performance and the accuracy of latency predictions. 

When you enable dedicated resources, the VM’s workload is pinned to specific CPUs on the node, and no other process is scheduled on those CPUs. The node must have CPU Manager configured. 

### 8.18.7.2. Enable dedicated resources for a virtual machine

Enable dedicated resources for a virtual machine in the OpenShift Container Platform web console so that its workload gets exclusive use of its CPUs. 

You can configure dedicated resources for virtual machines that were created from a Red Hat template. 

**Prerequisites**

  * The CPU Manager must be configured on the node. Verify that the node has the `cpumanager = true` label before scheduling virtual machine workloads. 
  * The virtual machine must be powered off. 



**Procedure**

  1. In the OpenShift Container Platform console, click **Virtualization** **VirtualMachines** from the side menu. 
  2. Select a virtual machine to open the **VirtualMachine details** page. 
  3. On the **Configuration Scheduling** tab, click the edit icon beside **Dedicated Resources**. 
  4. Select **Schedule this workload with dedicated resources (guaranteed policy)**. 
  5. Click **Save**. 



## 8.18.8. Configure PCI passthrough

The Peripheral Component Interconnect (PCI) passthrough feature enables you to access and manage hardware devices from a virtual machine (VM). When PCI passthrough is configured, the PCI devices function as if they were physically attached to the guest operating system. 

### 8.18.8.1. Node preparation for GPU passthrough

You can prevent GPU operands from deploying on worker nodes that you designated for GPU passthrough. 

#### 8.18.8.1.1. Prevent NVIDIA GPU operand deployment on nodes

If you use the NVIDIA GPU Operator in your cluster, you can apply the `nvidia.com/gpu.deploy.operands=false` label to nodes that you do not want to configure for GPU or vGPU operands. 

This prevents the creation of the pods that configure GPU or vGPU operands and terminates existing pods. 

**Prerequisites**

  * The OpenShift CLI (`oc`) is installed. 



**Procedure**

  * Label the node by running the following command: 

```shell-session
$ oc label node <node_name> nvidia.com/gpu.deploy.operands=false
```


where: 

`<node_name>`
     Specifies the name of a node where you do not want to install the NVIDIA GPU operands. 




**Verification**

  1. Verify that the label was added to the node by running the following command: 

```shell-session
$ oc describe node <node_name>
```


  2. Optional: If GPU operands were previously deployed on the node, verify their removal. 

     1. Check the status of the pods in the `nvidia-gpu-operator` namespace by running the following command: 

```shell-session
$ oc get pods -n nvidia-gpu-operator
```


Example output: 

```shell-session
NAME                             READY   STATUS        RESTARTS   AGE
gpu-operator-59469b8c5c-hw9wj    1/1     Running       0          8d
nvidia-sandbox-validator-7hx98   1/1     Running       0          8d
nvidia-sandbox-validator-hdb7p   1/1     Running       0          8d
nvidia-sandbox-validator-kxwj7   1/1     Terminating   0          9d
nvidia-vfio-manager-7w9fs        1/1     Running       0          8d
nvidia-vfio-manager-866pz        1/1     Running       0          8d
nvidia-vfio-manager-zqtck        1/1     Terminating   0          9d
```


     2. Monitor the pod status until the pods with `Terminating` status are removed: 

```shell-session
$ oc get pods -n nvidia-gpu-operator
```


Example output: 

```shell-session
NAME                             READY   STATUS    RESTARTS   AGE
gpu-operator-59469b8c5c-hw9wj    1/1     Running   0          8d
nvidia-sandbox-validator-7hx98   1/1     Running   0          8d
nvidia-sandbox-validator-hdb7p   1/1     Running   0          8d
nvidia-vfio-manager-7w9fs        1/1     Running   0          8d
nvidia-vfio-manager-866pz        1/1     Running   0          8d
```


### 8.18.8.2. Preparing host devices for PCI passthrough

#### 8.18.8.2.1. Host device preparation for PCI passthrough

To prepare a host device for PCI passthrough by using the CLI, create a `MachineConfig` object and add kernel arguments to enable the Input-Output Memory Management Unit (IOMMU). 

Bind the PCI device to the Virtual Function I/O (VFIO) driver and then expose it in the cluster by editing the `permittedHostDevices` field of the `HyperConverged` custom resource (CR). The `permittedHostDevices` list is empty when you first install the OpenShift Virtualization Operator. 

To remove a PCI host device from the cluster by using the CLI, delete the PCI device information from the `HyperConverged` CR. 

#### 8.18.8.2.2. Kernel module blocklist for PCI passthrough

For `vfio-pci` to allocate a PCI device, no other kernel driver can manage that device. If a driver already manages the device, you must add the specific kernel module to a blocklist. Adding a kernel module to a blocklist makes all devices handled by that module unavailable to the host. 

Cluster administrators can expose and manage host devices that are permitted to be used in the cluster by using the `oc` command-line interface (CLI). 

You can add a kernel module to the blocklist by creating a `MachineConfig` object that generates a configuration file in `/etc/modprobe.d/` and adds kernel arguments. 

The following example shows a `MachineConfig` object that adds the `enic` network driver to the blocklist: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 100-blocklist-enic
spec:
  config:
    ignition:
      version: 3.4.0
    storage:
      files:
      - contents:
          source: data:,blocklist%20enic%0A
        mode: 420
        overwrite: true
        path: /etc/modprobe.d/blocklist-enic.conf
  kernelArguments:
    - enic.blocklist=1
    - rd.driver.blocklist=enic
```


#### 8.18.8.2.3. Add kernel arguments to enable the IOMMU driver

You must enable the Input-Output Memory Management Unit (IOMMU) driver before you can configure mediated devices. To enable the IOMMU driver in the kernel, create the `MachineConfig` object and add the kernel arguments. 

**Prerequisites**

  * You have cluster administrator permissions. 
  * Your CPU hardware is Intel or AMD. 

Note

Enabling IOMMU is not required on `s390x` architecture. 

  * You enabled Intel Virtualization Technology for Directed I/O extensions or AMD IOMMU in the BIOS. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a `MachineConfig` object that identifies the kernel argument. The following example shows a kernel argument for an Intel CPU. 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 100-worker-iommu
spec:
  config:
    ignition:
      version: 3.2.0
  kernelArguments:
      - intel_iommu=on
# ...
```


     * `metadata.labels.machineconfiguration.openshift.io/role` specifies that the new kernel argument is applied only to worker nodes. 
     * `metadata.name` specifies the ranking of this kernel argument (100) among the machine configs and its purpose. If you have an AMD CPU, specify the kernel argument as `amd_iommu=on`. 
     * `spec.kernelArguments` specifies the kernel argument as `intel_iommu` for an Intel CPU. 

  2. Create the new `MachineConfig` object: 

```shell-session
$ oc create -f 100-worker-kernel-arg-iommu.yaml
```


**Verification**

  1. Verify that the new `MachineConfig` object was added by entering the following command and observing the output: 

```shell-session
$ oc get MachineConfig
```


Example output: 

```shell-session
NAME                                       IGNITIONVERSION                    AGE
00-master                                   3.5.0                             164m
00-worker                                   3.5.0                             164m
01-master-container-runtime                 3.5.0                             164m
01-master-kubelet                           3.5.0                             164m
01-worker-container-runtime                 3.5.0                             164m
01-worker-kubelet                           3.5.0                             164m
100-master-chrony-configuration             3.5.0                             169m
100-master-set-core-user-password           3.5.0                             169m
100-worker-chrony-configuration             3.5.0                             169m
100-worker-iommu                            3.5.0                             14s
```


  2. Verify that IOMMU is enabled at the operating system (OS) level by entering the following command: 

```shell-session
$ dmesg | grep -i iommu
```


     * If IOMMU is enabled, output is displayed as shown in the following example: 

Example output: 

```shell-session
Intel: [ 0.000000] DMAR: Intel(R) IOMMU Driver
AMD: [ 0.000000] AMD-Vi: IOMMU Initialized
```


#### 8.18.8.2.4. Bind PCI devices to the VFIO driver

To bind PCI devices to the VFIO (Virtual Function I/O) driver, obtain the values for the vendor ID and the device ID from each device and create a list with the values. Add this list to the `MachineConfig` object. 

The `MachineConfig` Operator generates the `/etc/modprobe.d/vfio.conf` on the nodes with the PCI devices, and binds the PCI devices to the VFIO driver. 

**Prerequisites**

  * You added kernel arguments to enable IOMMU for the CPU. 

Note

Enabling IOMMU is not required on `s390x` architecture. 

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Run the `lspci` command with the name of the GPU accelerator to obtain the vendor ID and the device ID for the PCI device. 

Note

NVIDIA GPU is supported on `x86` and `aarch64` architectures, Intel QAT is supported on `x86` architecture, and IBM® Spyre is supported on `s390x` architecture. 

```shell-session
$ lspci -nnv | grep -i <gpu_accelerator>
```


Valid values for `<gpu_accelerator>` are `nvidia`, `qat`, and `spyre`. 

Example output: 

```shell-session
02:01.0 3D controller [0302]: NVIDIA Corporation GV100GL [Tesla V100 PCIe 32GB] [10de:1eb8] (rev a1)
```


  2. Create a Butane config file, `100-worker-vfiopci.bu`, binding the PCI device to the VFIO driver. 

Note

The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.22.0`. See "Creating machine configs with Butane" for information about Butane. 

Example: 

```yaml
variant: openshift
version: 4.22.0
metadata:
  name: 100-worker-vfiopci
  labels:
    machineconfiguration.openshift.io/role: worker
storage:
  files:
  - path: /etc/modprobe.d/vfio.conf
    mode: 0644
    overwrite: true
    contents:
      inline: |
        options vfio-pci ids=<vendor_id>:<device_id>
  - path: /etc/modules-load.d/vfio-pci.conf
    mode: 0644
    overwrite: true
    contents:
      inline: vfio-pci
```


     * `metadata.labels.machineconfiguration.openshift.io/role: worker` specifies that the new kernel argument is applied only to compute nodes. 
     * `storage.files.contents.inline`, where the path is `/etc/modprobe.d/vfio.conf`, specifies the previously determined hexadecimal vendor ID and device ID values to bind a device to the VFIO driver. You can add a list of multiple devices with their vendor and device information. 
     * `storage.files.path`, where the `contents.inline` is `vfio-pci`, specifies the file that loads the `vfio-pci` kernel module on the compute nodes. 

  3. Use Butane to generate a `MachineConfig` object file, `100-worker-vfiopci.yaml`, containing the configuration to be delivered to the compute nodes: 

```shell-session
$ butane 100-worker-vfiopci.bu -o 100-worker-vfiopci.yaml
```


  4. Apply the `MachineConfig` object to the compute nodes: 

```shell-session
$ oc apply -f 100-worker-vfiopci.yaml
```


  5. Verify that the `MachineConfig` object was added. 

```shell-session
$ oc get MachineConfig
```


Example output: 

```shell-session
NAME                             GENERATEDBYCONTROLLER                      IGNITIONVERSION  AGE
00-master                        d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
00-worker                        d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
01-master-container-runtime      d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
01-master-kubelet                d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
01-worker-container-runtime      d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
01-worker-kubelet                d3da910bfa9f4b599af4ed7f5ac270d55950a3a1   3.5.0            25h
100-worker-iommu                                                            3.5.0            30s
100-worker-vfiopci-configuration                                            3.5.0            30s
```


**Verification**

  * Verify that the VFIO driver is loaded. 

```shell-session
$ lspci -nnk -d <vendor_id>:
```


The output confirms that the VFIO driver is being used. 

Example output: 

```plaintext
04:00.0 3D controller [0302]: NVIDIA Corporation GP102GL [Tesla P40] [10de:1eb8] (rev a1)
        Subsystem: NVIDIA Corporation Device [10de:1eb8]
        Kernel driver in use: vfio-pci
        Kernel modules: nouveau
```


#### 8.18.8.2.5. Expose PCI host devices in the cluster

To expose PCI host devices in the cluster, add details about the PCI devices to the `spec.permittedHostDevices.pciHostDevices` array of the `HyperConverged` custom resource (CR). 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Edit the `HyperConverged` CR in your default editor by running the following command: 

```shell-session
$ oc edit hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
```


  2. Add the PCI device information to the `spec.permittedHostDevices.pciHostDevices` array. 

Example configuration file: 

```yaml
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  permittedHostDevices:
    pciHostDevices:
    - pciDeviceSelector: "10DE:1DB6"
      resourceName: "nvidia.com/GV100GL_Tesla_V100"
    - pciDeviceSelector: "10DE:1EB8"
      resourceName: "nvidia.com/TU104GL_Tesla_T4"
    - pciDeviceSelector: "8086:6F54"
      resourceName: "intel.com/qat"
      externalResourceProvider: true
# ...
```


     * `spec.permittedHostDevices` specifies the host devices that are permitted to be used in the cluster. 
     * `spec.permittedHostDevices.pciHostDevices` specifies the list of PCI devices available on the node. 
     * `spec.permittedHostDevices.pciHostDevices.pciDeviceSelector` specifies the vendor ID and the device ID required to identify the PCI device. 
     * `spec.permittedHostDevices.pciHostDevices.resourceName` specifies the name of a PCI host device. 
     * `spec.permittedHostDevices.pciHostDevices.externalResourceProvider` is an optional setting. Setting this field to `true` indicates that the resource is provided by an external device plugin. OpenShift Virtualization allows the usage of this device in the cluster but leaves the allocation and monitoring to an external device plugin. 

Note

The above example snippet shows two PCI host devices that are named `nvidia.com/GV100GL_Tesla_V100` and `nvidia.com/TU104GL_Tesla_T4` added to the list of permitted host devices in the `HyperConverged` CR. These devices have been tested and verified to work with OpenShift Virtualization. 

Example configuration file for an IBM® Spyre device on `s390x` architecture: 

```yaml
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  permittedHostDevices:
    pciHostDevices:
    - pciDeviceSelector: "1014:06a8"
      resourceName: "ibm.com/spyre"
# ...
```


  3. Save your changes and exit the editor. 



**Verification**

  * Verify that the PCI host devices were added to the node by running the following command. The example output shows that there is one device each associated with the `nvidia.com/GV100GL_Tesla_V100`, `nvidia.com/TU104GL_Tesla_T4`, and `intel.com/qat` resource names. 

```shell-session
$ oc describe node <node_name>
```


Example output: 

```shell-session
Capacity:
  cpu:                            64
  devices.kubevirt.io/kvm:        110
  devices.kubevirt.io/tun:        110
  devices.kubevirt.io/vhost-net:  110
  ephemeral-storage:              915128Mi
  hugepages-1Gi:                  0
  hugepages-2Mi:                  0
  memory:                         131395264Ki
  nvidia.com/GV100GL_Tesla_V100   1
  nvidia.com/TU104GL_Tesla_T4     1
  intel.com/qat:                  1
  pods:                           250
Allocatable:
  cpu:                            63500m
  devices.kubevirt.io/kvm:        110
  devices.kubevirt.io/tun:        110
  devices.kubevirt.io/vhost-net:  110
  ephemeral-storage:              863623130526
  hugepages-1Gi:                  0
  hugepages-2Mi:                  0
  memory:                         130244288Ki
  nvidia.com/GV100GL_Tesla_V100   1
  nvidia.com/TU104GL_Tesla_T4     1
  intel.com/qat:                  1
  pods:                           250
```


Note

When using an IBM® Spyre device on `s390x` architecture, the allocated device is shown as follows: `ibm.com/spyre: 1`. 




#### 8.18.8.2.6. Remove PCI host devices from the cluster

To remove a PCI host device from the cluster, delete the information for that device from the `HyperConverged` custom resource (CR). 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Edit the `HyperConverged` CR in your default editor by running the following command: 

```shell-session
$ oc edit hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
```


  2. Remove the PCI device information from the `spec.permittedHostDevices.pciHostDevices` array by deleting the `pciDeviceSelector`, `resourceName` and `externalResourceProvider` (if applicable), fields for the appropriate device. In this example, the user deletes the `nvidia.com/TU104GL_Tesla_T4`. 

Example configuration file: 

```yaml
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  permittedHostDevices:
    pciHostDevices:
    - pciDeviceSelector: "10DE:1DB6"
      resourceName: "nvidia.com/GV100GL_Tesla_V100"
# ...
```


  3. Save your changes and exit the editor. 



**Verification**

  * Verify that you removed the PCI host device from the node by running the following command. The example output shows that there are zero devices associated with the `nvidia.com/TU104GL_Tesla_T4` resource name. 

```shell-session
$ oc describe node <node_name>
```


Example output: 

```shell-session
Capacity:
  cpu:                            64
  devices.kubevirt.io/kvm:        110
  devices.kubevirt.io/tun:        110
  devices.kubevirt.io/vhost-net:  110
  ephemeral-storage:              915128Mi
  hugepages-1Gi:                  0
  hugepages-2Mi:                  0
  memory:                         131395264Ki
  nvidia.com/GV100GL_Tesla_V100   1
  nvidia.com/TU104GL_Tesla_T4     0
  pods:                           250
Allocatable:
  cpu:                            63500m
  devices.kubevirt.io/kvm:        110
  devices.kubevirt.io/tun:        110
  devices.kubevirt.io/vhost-net:  110
  ephemeral-storage:              863623130526
  hugepages-1Gi:                  0
  hugepages-2Mi:                  0
  memory:                         130244288Ki
  nvidia.com/GV100GL_Tesla_V100   1
  nvidia.com/TU104GL_Tesla_T4     0
  pods:                           250
```


### 8.18.8.3. Virtual machine configuration for PCI passthrough

After the PCI devices have been added to the cluster, you can assign them to virtual machines. The PCI devices are now available as if they are physically connected to the virtual machines. 

#### 8.18.8.3.1. Assign a PCI device to a virtual machine

When a PCI device is available in a cluster, you can assign it to a virtual machine and enable PCI passthrough. 

**Procedure**

  * Assign the PCI device to a virtual machine as a host device. 

Example: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
spec:
  domain:
    devices:
      hostDevices:
      - deviceName: nvidia.com/TU104GL_Tesla_T4
        name: hostdevices1
```


    * `spec.template.spec.domain.devices.hostDevices.deviceName` specifies the name of the PCI device that is permitted on the cluster as a host device. The virtual machine can access this host device. When using an IBM® Spyre device on `s390x` architecture, specify `ibm.com/spyre:`. 




**Verification**

  * Use the following command to verify that the host device is available from the virtual machine. 

```shell-session
$ lspci -nnk | grep <gpu_accelerator>
```


Valid values for `<gpu_accelerator>` are `nvidia`, `qat`, and `spyre`. 

Example output: 

```shell-session
$ 02:01.0 3D controller [0302]: NVIDIA Corporation GV100GL [Tesla V100 PCIe 32GB] [10de:1eb8] (rev a1)
```


### 8.18.8.4. PCI passthrough on IBM Z

On IBM Z® and IBM® LinuxONE, you can configure PCI passthrough for Network Express RoCE adapters and IBM® Internal Shared Memory (ISM) virtual PCI devices. Both use `vfio-pci` to pass devices directly to virtual machines. 

#### 8.18.8.4.1. Configure RoCE adapter passthrough on IBM Z

On IBM Z® and IBM® LinuxONE, you can configure PCI passthrough for Network Express RoCE adapters by using `vfio-pci`. This procedure applies only when the adapter is configured in RoCE mode through the Hardware Management Console (HMC). 

On IBM Z® and IBM® LinuxONE systems, Network Express adapters can be configured in two modes through the HMC: 

  * **Network Express RoCE** : The adapter is exposed as a PCI virtual function, managed by the `mlx5_core` kernel driver, and can be passed through to VMs by using `vfio-pci`. 
  * **Network Express OSA** : The adapter uses IBM Z® channel-based I/O (OSH PCI functions). OSH functions are not supported on Linux and are not exposed as PCI devices. Do not configure `vfio-pci` passthrough for adapters in OSA mode. 



To use `vfio-pci` for PCI passthrough of RoCE virtual function devices, you must prevent the `mlx5_core` kernel driver from binding to the device. Because `mlx5_core` is included in the initramfs image and loads before the root filesystem is mounted, you must add the driver to a blocklist by using both a `modprobe.d` configuration file and a kernel boot argument. You then bind the device to `vfio-pci` by using a second `MachineConfig`. 

**Prerequisites**

  * You have installed OpenShift Container Platform 4.21 or later. 
  * You have installed the OpenShift Virtualization Operator. 
  * You have cluster administrator permissions. 
  * You have installed the Butane tool for generating Ignition-compatible `MachineConfig` manifests. 
  * The Network Express adapter is configured in RoCE mode through the HMC. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. On each node, identify the RoCE virtual function PCI address and vendor ID by running the following command: 

```shell-session
$ lspci | grep -i mellanox
```


**Example output**

```shell-session
0000:00:00.0 Ethernet controller: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function [15b3:101e]
```


Record the combined PCI vendor and device ID `15b3:101e`. This value is used in the `vfio-pci` and `HyperConverged` configuration. 

  2. Create a Butane configuration file named `machine-config-roce.bu` to add the `mlx5_core` driver to the blocklist: 

```yaml
variant: openshift
version: 4.22.0
metadata:
  name: 100-worker-blocklist-mlx5
  labels:
    machineconfiguration.openshift.io/role: master
storage:
  files:
    - path: /etc/modprobe.d/blocklist-mlx5.conf
      mode: 0644
      overwrite: true
      contents:
        inline: |
          blocklist mlx5_core
openshift:
  kernel_arguments:
    - rd.driver.blacklist=mlx5_core
```


Note

The `rd.driver.blacklist=mlx5_core` kernel argument is required in addition to the `modprobe.d` blocklist entry because `mlx5_core` is included in the initramfs image and loads before `/etc/modprobe.d/` is accessible. The kernel argument blocks the driver at the initramfs stage. 

  3. Convert the Butane file to a `MachineConfig` manifest by running the following command: 

```shell-session
$ butane machine-config-roce.bu --output machine-config-roce.yaml
```


  4. Apply the `MachineConfig` to the cluster by running the following command: 

```shell-session
$ oc apply -f machine-config-roce.yaml
```


  5. Watch the `MachineConfig` rollout and wait for completion before proceeding: 

```shell-session
$ oc get mcp master -w
```


  6. Create a Butane configuration file named `machine-config-roce1.bu` to bind RoCE devices to `vfio-pci`: 

```yaml
variant: openshift
version: 4.22.0
metadata:
  name: 100-worker-vfiopci
  labels:
    machineconfiguration.openshift.io/role: master
storage:
  files:
    - path: /etc/modprobe.d/vfio.conf
      mode: 0644
      overwrite: true
      contents:
        inline: |
          options vfio-pci ids=15b3:101e
    - path: /etc/modules-load.d/vfio-pci.conf
      mode: 0644
      overwrite: true
      contents:
        inline: vfio-pci
```


  7. Convert the Butane file to a `MachineConfig` manifest by running the following command: 

```shell-session
$ butane machine-config-roce1.bu --output machine-config-roce1.yaml
```


  8. Apply the `MachineConfig` to the cluster by running the following command: 

```shell-session
$ oc apply -f machine-config-roce1.yaml
```


  9. Watch the `MachineConfig` rollout and wait for completion before proceeding: 

```shell-session
$ oc get mcp master -w
```


  10. Edit the `HyperConverged` custom resource to expose the RoCE device: 

```shell-session
$ oc edit hyperconverged kubevirt-hyperconverged -n openshift-cnv
```


Add the device under `spec.virtualization.permittedHostDevices`: 

```yaml
spec:
  virtualization:
    permittedHostDevices:
      pciHostDevices:
        - pciDeviceSelector: "15b3:101e"
          resourceName: ibm.com/roce_vf
```


  11. Add a `hostDevices` entry to the `VirtualMachine` manifest: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: <vm_name>
  namespace: <namespace>
spec:
  template:
    spec:
      domain:
        devices:
          hostDevices:
            - deviceName: ibm.com/roce_vf
              name: hostdevices1
```


  12. Apply the `VirtualMachine` manifest by running the following command: 

```shell-session
$ oc apply -f <vm_manifest>.yaml
```


**Verification**

  1. Verify `vfio-pci` binding on the nodes by running the following command: 

```shell-session
$ lspci -nnk | grep -A 3 "15b3:101e"
```


**Example output**

```shell-session
0000:00:00.0 Ethernet controller [0200]: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function [15b3:101e]
        Subsystem: Mellanox Technologies Device [15b3:0002]
        Kernel driver in use: vfio-pci
        Kernel modules: mlx5_core
```


The `Kernel driver in use: vfio-pci` line confirms that the device is bound to `vfio-pci` on the host. 

  2. Verify that the RoCE device is present inside the VM by running the following command: 

```shell-session
$ lspci -nnk | grep -A 3 "15b3:101e"
```


**Example output**

```shell-session
0001:00:00.0 Ethernet controller [0200]: Mellanox Technologies ConnectX Family mlx5Gen Virtual Function [15b3:101e]
        Subsystem: Mellanox Technologies Device [15b3:0002]
        Kernel driver in use: mlx5_core
        Kernel modules: mlx5_core
```


Note

Inside the VM, the RoCE device is managed by the guest kernel’s own `mlx5_core` driver. The host uses `vfio-pci` to pass the device through. The guest uses its native driver to operate it. 




#### 8.18.8.4.2. Configure ISM device passthrough on IBM Z

On IBM Z® and IBM® LinuxONE, IBM® Internal Shared Memory (ISM) devices are exposed as virtual PCI devices. You can configure PCI passthrough for ISM devices by binding the device to the `vfio-pci` driver by using a single `MachineConfig`. 

Unlike RoCE passthrough, which requires two separate `MachineConfig` objects to blocklist `mlx5_core` and bind `vfio-pci`, ISM passthrough requires only a single `MachineConfig`. The `ism` kernel module does not load during initramfs, so a `softdep` directive combined with kernel boot arguments is enough to ensure `vfio-pci` claims the device before `ism`. 

Note

The `softdep` directive ensures `vfio-pci` loads before the `ism` module without completely blocking `ism` from the host. The `ism` module remains available in the kernel but does not own the ISM device. 

**Prerequisites**

  * You have installed OpenShift Container Platform 4.21 or later. 
  * You have installed the OpenShift Virtualization Operator. 
  * You have cluster administrator permissions. 
  * You have installed the Butane tool for generating Ignition-compatible `MachineConfig` manifests. 
  * The ISM virtual PCI device is present and visible on the PCI bus of the target nodes. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. On each node, confirm the ISM device is displayed as a PCI device by running the following command: 

```shell-session
$ lspci | grep -i ism
```


**Example output**

```shell-session
0004:00:00.0 Non-VGA unclassified device: IBM Internal Shared Memory (ISM) virtual PCI device
```


  2. Retrieve the PCI vendor and device ID by running the following command: 

```shell-session
$ lspci -n -s 0004:00:00.0
```


**Example output**

```shell-session
0004:00:00.0 0000: 1014:04ed
```


Record the combined PCI vendor and device ID `1014:04ed`. This value is used in the `vfio-pci` and `HyperConverged` configuration. 

  3. Create a Butane configuration file named `100-master-vfio-ism.bu` to bind the ISM device to `vfio-pci`: 

```yaml
variant: openshift
version: 4.22.0
metadata:
  name: 100-master-vfio-ism
  labels:
    machineconfiguration.openshift.io/role: master
storage:
  files:
    - path: /etc/modprobe.d/vfio-ism.conf
      mode: 0644
      overwrite: true
      contents:
        inline: |
          softdep ism pre: vfio-pci
          options vfio-pci ids=1014:04ed
openshift:
  kernel_arguments:
    - rd.driver.pre=vfio-pci
    - vfio-pci.ids=1014:04ed
```


where: 

`storage.files[].contents.inline softdep ism pre: vfio-pci`
     Specifies that `vfio-pci` must load before the `ism` module. The `ism` module remains available on the host but does not own the device. 
`storage.files[].contents.inline options vfio-pci ids=1014:04ed`
     Specifies that `vfio-pci` claims devices with this PCI vendor and device ID. 
`openshift.kernel_arguments rd.driver.pre=vfio-pci`
     Specifies that `vfio-pci` loads during initramfs before any other driver. 
`openshift.kernel_arguments vfio-pci.ids=1014:04ed`
     Specifies the PCI device ID passed directly to `vfio-pci` at boot time. 

  4. Convert the Butane file to a `MachineConfig` manifest by running the following command: 

```shell-session
$ butane 100-master-vfio-ism.bu -o 100-master-vfio-ism.yaml
```


  5. Apply the `MachineConfig` to the cluster by running the following command: 

```shell-session
$ oc apply -f 100-master-vfio-ism.yaml
```


  6. Watch the `MachineConfig` rollout and wait for completion before proceeding: 

```shell-session
$ oc get mcp master -w
```


**Example output when complete**

```shell-session
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-3fb080e65525e49079d4b34e122fb64c   True      False      False      3              3                   3                     0                      27d
```


  7. Confirm the ISM device resource is visible and allocatable on the nodes by running the following command: 

```shell-session
$ oc describe nodes | grep ibm.com/ism
```


**Example output**

```shell-session
  ibm.com/ism:    1
  ibm.com/ism:    1
```


  8. Edit the `HyperConverged` custom resource to expose the ISM device by running the following command: 

```shell-session
$ oc edit hyperconverged kubevirt-hyperconverged -n openshift-cnv
```


Add the ISM device under `spec.virtualization.permittedHostDevices`: 

```yaml
spec:
  virtualization:
    permittedHostDevices:
      pciHostDevices:
        - pciDeviceSelector: "1014:04ed"
          resourceName: ibm.com/ism
```


  9. Verify the HyperConverged Operator accepted the configuration by running the following command: 

```shell-session
$ oc get hyperconverged kubevirt-hyperconverged \
  -n openshift-cnv -o json | jq '.spec.virtualization.permittedHostDevices'
```


**Example output**

```shell-session
{
  "pciHostDevices": [
    {
      "pciDeviceSelector": "1014:04ed",
      "resourceName": "ibm.com/ism"
    }
  ]
}
```


  10. Add the ISM device to a `VirtualMachine` manifest: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: <vm_name>
  namespace: <namespace>
spec:
  running: true
  template:
    spec:
      domain:
        devices:
          hostDevices:
            - deviceName: ibm.com/ism
              name: ism-device
        resources:
          requests:
            memory: 1Gi
```


  11. Apply the `VirtualMachine` manifest by running the following command: 

```shell-session
$ oc apply -f <vm_manifest>.yaml
```


**Verification**

  1. Verify `vfio-pci` binding on all control plane nodes by running the following command: 

```shell-session
$ for node in $(oc get nodes -l node-role.kubernetes.io/master -o name); do
  echo "=== $node ==="
  oc debug $node -- chroot /host bash -c \
    "lspci -nnk | grep -A2 'ISM\|1014:04ed'" 2>/dev/null
done
```


**Example output**

```shell-session
=== node/master-0 ===
0000:00:00.0 Non-VGA unclassified device [0000]: IBM Internal Shared Memory (ISM) virtual PCI device [1014:04ed]
        Kernel driver in use: vfio-pci
        Kernel modules: ism
=== node/master-1 ===
0000:00:00.0 Non-VGA unclassified device [0000]: IBM Internal Shared Memory (ISM) virtual PCI device [1014:04ed]
        Kernel driver in use: vfio-pci
        Kernel modules: ism
=== node/master-2 ===
0000:00:00.0 Non-VGA unclassified device [0000]: IBM Internal Shared Memory (ISM) virtual PCI device [1014:04ed]
        Kernel driver in use: vfio-pci
        Kernel modules: ism
```


`Kernel modules: ism` indicates the `ism` module is available in the kernel but is not actively managing the device. `vfio-pci` owns the device. 

  2. Verify the ISM device is present inside the VM by connecting to the VM console and running the following command: 

```shell-session
$ lspci -nnk | grep -i ism
```


**Example output**

```shell-session
0001:00:00.0 Non-VGA unclassified device: IBM Internal Shared Memory (ISM) virtual PCI device
```


The output confirms PCI passthrough. The guest binds the `ism` driver only if the guest image includes that module. 




### 8.18.8.5. Additional resources

  * [Enabling Intel VT-X and AMD-V Virtualization Hardware Extensions in BIOS](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-troubleshooting-enabling_intel_vt_x_and_amd_v_virtualization_hardware_extensions_in_bios)
  * [Managing file permissions](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/assembly_managing-file-permissions_configuring-basic-system-settings)
  * [Machine Config Overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#machine-config-overview)
  * [IBM® Spyre Accelerator User’s Guide](https://www.ibm.com/docs/en/systems-hardware/linuxone/9175-ML1?topic=library-spyre-accelerator-users-guide)
  * [Network adapters as of IBM® z17 and IBM® LinuxONE 5](https://www.ibm.com/docs/en/linux-on-systems?topic=networking-pci-network-adapters)



## 8.18.9. Configuring virtual GPUs

Use the NVIDIA GPU operator to create virtual GPUs (vGPUs) and assign them to virtual machines (VMs) in OpenShift Virtualization. 

### 8.18.9.1. Virtual GPUs in OpenShift Virtualization

You can create vGPUs for your virtual machines (VMs) using supported GPU cards. Refer to your hardware vendor’s documentation for functionality and support details. 

You can use the NVIDIA GPU Operator to manage vGPUs for your virtual machines (VMs) on the cluster nodes. You must add these devices to the `HyperConverged` custom resource (CR) so that OpenShift Virtualization can discover and make them available to virtual machines. 

A mediated device is a physical device that is divided into one or more virtual devices. vGPUs are a type of mediated device (mdev) where the performance of the physical GPU is divided among the virtual devices. You can assign mediated devices to one or more virtual machines (VMs), but the number of guests must be compatible with your GPU. Some GPUs do not support multiple guests. 

#### 8.18.9.1.1. Add kernel arguments to enable the IOMMU driver

You must enable the Input-Output Memory Management Unit (IOMMU) driver before you can configure mediated devices. To enable the IOMMU driver in the kernel, create the `MachineConfig` object and add the kernel arguments. 

**Prerequisites**

  * You have cluster administrator permissions. 
  * Your CPU hardware is Intel or AMD. 

Note

Enabling IOMMU is not required on `s390x` architecture. 

  * You enabled Intel Virtualization Technology for Directed I/O extensions or AMD IOMMU in the BIOS. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a `MachineConfig` object that identifies the kernel argument. The following example shows a kernel argument for an Intel CPU. 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 100-worker-iommu
spec:
  config:
    ignition:
      version: 3.2.0
  kernelArguments:
      - intel_iommu=on
# ...
```


     * `metadata.labels.machineconfiguration.openshift.io/role` specifies that the new kernel argument is applied only to worker nodes. 
     * `metadata.name` specifies the ranking of this kernel argument (100) among the machine configs and its purpose. If you have an AMD CPU, specify the kernel argument as `amd_iommu=on`. 
     * `spec.kernelArguments` specifies the kernel argument as `intel_iommu` for an Intel CPU. 

  2. Create the new `MachineConfig` object: 

```shell-session
$ oc create -f 100-worker-kernel-arg-iommu.yaml
```


**Verification**

  1. Verify that the new `MachineConfig` object was added by entering the following command and observing the output: 

```shell-session
$ oc get MachineConfig
```


Example output: 

```shell-session
NAME                                       IGNITIONVERSION                    AGE
00-master                                   3.5.0                             164m
00-worker                                   3.5.0                             164m
01-master-container-runtime                 3.5.0                             164m
01-master-kubelet                           3.5.0                             164m
01-worker-container-runtime                 3.5.0                             164m
01-worker-kubelet                           3.5.0                             164m
100-master-chrony-configuration             3.5.0                             169m
100-master-set-core-user-password           3.5.0                             169m
100-worker-chrony-configuration             3.5.0                             169m
100-worker-iommu                            3.5.0                             14s
```


  2. Verify that IOMMU is enabled at the operating system (OS) level by entering the following command: 

```shell-session
$ dmesg | grep -i iommu
```


     * If IOMMU is enabled, output is displayed as shown in the following example: 

Example output: 

```shell-session
Intel: [ 0.000000] DMAR: Intel(R) IOMMU Driver
AMD: [ 0.000000] AMD-Vi: IOMMU Initialized
```


### 8.18.9.2. Using the NVIDIA GPU Operator

You can use the NVIDIA GPU Operator to provision worker nodes for running GPU-accelerated virtual machines (VMs) in OpenShift Virtualization. 

The NVIDIA GPU Operator manages NVIDIA GPU resources in an OpenShift Container Platform cluster and automates tasks when preparing nodes for GPU workloads. The NVIDIA GPU Operator can also facilitate provisioning complex artificial intelligence and machine learning (AI/ML) workloads. 

Note

You can get support for the NVIDIA GPU Operator through NVIDIA. For more information, see "Obtaining Support from NVIDIA" in the Red Hat Knowledgebase. 

**Procedure**

  1. Configure your `ClusterPolicy` manifest. Your `ClusterPolicy` manifest must match the provided example: 

```yaml
apiVersion: nvidia.com/v1
kind: ClusterPolicy
metadata:
  name: gpu-cluster-policy
spec:
  daemonsets:
    updateStrategy: RollingUpdate
  dcgm:
    enabled: true
  dcgmExporter: {}
  devicePlugin: {}
  driver:
    enabled: false
    kernelModuleType: auto
  gfd: {}
  mig:
    strategy: single
  migManager:
    enabled: true
  nodeStatusExporter:
    enabled: true
  operator:
    defaultRuntime: crio
    initContainer: {}
    runtimeClass: nvidia
    use_ocp_driver_toolkit: true
  sandboxDevicePlugin:
    enabled: true
  sandboxWorkloads:
    defaultWorkload: vm-vgpu
    enabled: true
  toolkit:
    enabled: true
    installDir: /usr/local/nvidia
  validator:
    plugin:
      env:
      - name: WITH_WORKLOAD
        value: "true"
  vfioManager:
    enabled: true
  vgpuDeviceManager:
    enabled: true
  vgpuManager:
    enabled: true
    image: <vgpu_image_name>
    repository: <vgpu_container_registry>
    version: <nvidia_vgpu_manager_version>
```


where: 

`<vgpu_image_name>`
     Specifies the vGPU image name. 
`<vgpu_container_registry>`
     Specifies the vGPU container registry value. 
`<nvidia_vgpu_manager_version>`
     Specifies the version of the vGPU driver you have downloaded from the NVIDIA website and used to build the image. 

  2. Use the NVIDIA GPU Operator to configure mediated devices. For more information see [NVIDIA GPU Operator with OpenShift Virtualization](https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/openshift-virtualization.html). 



### 8.18.9.3. Label nodes with a MIG-backed vGPU profile

If you have GPUs that support NVIDIA Multi-Instance GPU (MIG), you can select a MIG-backed vGPU instance instead of time-sliced vGPU instances. When you use MIG, you give a partition of dedicated hardware to selected VMs. 

**Prerequisites**

  * You have configured vGPU support. 
  * You have the NVIDIA GPU Operator version 25.10 or higher. 
  * You are using the NVIDIA AI Enterprise (AIE) vGPU Manager image. 



**Procedure**

  * Label the node with the name of the MIG-backed vGPU profile: 

```shell-session
$ oc label node <node> --overwrite nvidia.com/vgpu.config=<profile>
```


    * Replace `<node>` with the fully qualified domain name (FQDN) of your compute node. 
    * Replace `<profile>` with a supported MIG profile. 

Example command: 

```shell-session
$ oc label node worker_1 --overwrite nvidia.com/vgpu.config=A30-1-6C
```


### 8.18.9.4. Create and expose mediated devices

As an administrator, you can create mediated devices and expose them to the cluster by editing the `HyperConverged` custom resource (CR). Before you edit the CR, explore a worker node to find the configuration values that are specific to your hardware devices. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You enabled the Input-Output Memory Management Unit (IOMMU) driver. 
  * If your hardware vendor provides drivers, you installed them on the nodes where you want to create mediated devices. 

    * If you use NVIDIA cards, you [installed the NVIDIA GRID driver](https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/openshift-virtualization.html). 




**Procedure**

  1. Identify the name selector and resource name values for the mediated devices by exploring a worker node: 

     1. Start a debugging session with the worker node by using the `oc debug` command. For example: 

```shell-session
$ oc debug node/node-11.redhat.com
```


     2. Change the root directory of the shell process to the file system of the host node by running the following command: 

```shell-session
# chroot /host
```


     3. Navigate to the `mdev_bus` directory and view its contents. Each subdirectory name is a PCI address of a physical GPU. For example: 

```shell-session
# cd sys/class/mdev_bus && ls
```


Example output: 

```shell-session
0000:4b:00.4
```


     4. Go to the directory for your physical device and list the supported mediated device types as defined by the hardware vendor. For example: 

```shell-session
# cd 0000:4b:00.4 && ls mdev_supported_types
```


Example output: 

```shell-session
nvidia-742  nvidia-744	nvidia-746  nvidia-748	nvidia-750  nvidia-752
nvidia-743  nvidia-745	nvidia-747  nvidia-749	nvidia-751  nvidia-753
```


     5. Select the mediated device type that you want to use and identify its name selector value by viewing the contents of its `name` file. For example: 

```shell-session
# cat nvidia-745/name
```


Example output: 

```shell-session
NVIDIA A2-2Q
```


  2. Open the `HyperConverged` CR in your default editor by running the following command: 

```shell-session
$ oc edit hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
```


  3. Create and expose the mediated devices by updating the configuration: 

     1. Enable the `disableMDevConfiguration` feature gate so that OpenShift Virtualization does not try to manage mediated devices that an external provider, such as the NVIDIA GPU Operator, already manages: 

```shell-session
$ oc patch hyperconvergeds.v1beta1.hco.kubevirt.io -n openshift-cnv kubevirt-hyperconverged \
  --type='json' -p='[{"op": "add", "path": "/spec/featureGates/disableMDevConfiguration", "value": true}]'
```


     2. Expose the mediated devices to the cluster by adding the `mdevNameSelector` and `resourceName` values to the `spec.permittedHostDevices.mediatedDevices` stanza. The `resourceName` value is based on the `mdevNameSelector` value, but you use underscores instead of spaces. 

Example `HyperConverged` CR: 

```yaml
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  permittedHostDevices:
    mediatedDevices:
    - mdevNameSelector: NVIDIA A2-2Q
      resourceName: nvidia.com/NVIDIA_A2-2Q
      externalResourceProvider: true
    - mdevNameSelector: NVIDIA A2-4Q
      resourceName: nvidia.com/NVIDIA_A2-4Q
      externalResourceProvider: true
# ...
```


where: 

`mdevNameSelector`
     Specifies the mediated devices that map to this value on the host. 
`resourceName`
     Specifies the matching resource name that is allocated on the node. 
`externalResourceProvider`
     Specifies that the device is handled by an external provider, such as the NVIDIA GPU Operator. 

  4. Save your changes and exit the editor. 



**Verification**

  * Confirm that the virtual GPU is attached to the node by running the following command: 

```shell-session
$ oc get node <node_name> -o json | jq '.status.allocatable | with_entries(select(.key | startswith("nvidia.com/"))) | with_entries(select(.value != "0"))'
```


### 8.18.9.5. Remove mediated devices from the cluster

As a cluster administrator you can remove mediated devices from the cluster so that you can reallocate GPU hardware. To remove a mediated device from the cluster, delete the information for that device from the `HyperConverged` CR. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Edit the `HyperConverged` CR in your default editor by running the following command: 

```shell-session
$ oc edit hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
```


  2. Remove the device information from the `spec.permittedHostDevices` stanza of the `HyperConverged` CR. For example: 

```yaml
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  permittedHostDevices:
    mediatedDevices:
    - mdevNameSelector: GRID T4-2Q
      resourceName: nvidia.com/GRID_T4-2Q
      externalResourceProvider: true
```


     * To remove the `GRID T4-2Q` device, delete the `mdevNameSelector` field and its corresponding `resourceName` field. 

  3. Save your changes and exit the editor. 



### 8.18.9.6. Assign a vGPU to a VM by using the CLI

After mediated devices are configured in the cluster, you can assign them to individual VMs so that VMs can access shared GPU resources. 

**Prerequisites**

  * The mediated device is configured in the `HyperConverged` custom resource. 
  * The virtual machine (VM) is stopped. 



**Procedure**

  * Assign the mediated device to a VM by editing the `spec.domain.devices.gpus` stanza of the `VirtualMachine` manifest. 

Example virtual machine manifest: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
spec:
  domain:
    devices:
      gpus:
      - deviceName: nvidia.com/TU104GL_Tesla_T4
        name: gpu1
      - deviceName: nvidia.com/GRID_T4-2Q
        name: gpu2
```


    * `spec.template.spec.domain.devices.gpus.deviceName` specifies the resource name associated with the mediated device. 
    * `spec.template.spec.domain.devices.gpus.name` specifies a name to identify the device on the VM. 




**Verification**

  * To verify that the device is available from the virtual machine, run the following command, substituting `<device_name>` with the `deviceName` value from the `VirtualMachine` manifest: 

```shell-session
$ lspci -nnk | grep <device_name>
```


### 8.18.9.7. Assign a vGPU to a VM by using the web console

You can assign virtual GPUs to virtual machines by using the OpenShift Container Platform web console. 

Note

You can add hardware devices to virtual machines created from customized templates or a YAML file. You cannot add devices to pre-supplied boot source templates for specific operating systems. 

**Prerequisites**

  * The vGPU is configured as a mediated device in your cluster. 

    * To view the devices that are connected to your cluster, click **Compute** **Hardware Devices** from the side menu. 

  * The VM is stopped. 



**Procedure**

  1. In the OpenShift Container Platform web console, click **Virtualization** **VirtualMachines** from the side menu. 
  2. Select the VM that you want to assign the device to. 
  3. On the **Details** tab, click **GPU devices**. 
  4. Click **Add GPU device**. 
  5. Enter an identifying value in the **Name** field. 
  6. From the **Device name** list, select the device that you want to add to the VM. 
  7. Click **Save**. 



**Verification**

  * To confirm that the devices were added to the VM, click the **YAML** tab and review the `VirtualMachine` configuration. Mediated devices are added to the `spec.domain.devices` stanza. 



### 8.18.9.8. Additional resources

  * [Enabling Intel VT-X and AMD-V Virtualization Hardware Extensions in BIOS](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-troubleshooting-enabling_intel_vt_x_and_amd_v_virtualization_hardware_extensions_in_bios)
  * [MIG Support in OpenShift Container Platform](https://docs.nvidia.com/datacenter/cloud-native/openshift/latest/mig-ocp.html#)
  * [Configuring PCI passthrough](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-configuring-pci-passthrough "8.18.8. Configure PCI passthrough")
  * [Obtaining Support from NVIDIA](https://access.redhat.com/solutions/5174941)
  * [MIG User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html)



## 8.18.10. Configuring USB host passthrough

You can enable passthrough of USB devices to allow a virtual machine (VM) to connect to USB hardware that is attached to an OpenShift Container Platform node, as if the hardware and the VM are physically connected. 

To expose a USB device, first enable host passthrough and then configure the VM to use the USB device. 

### 8.18.10.1. Enable USB host passthrough

To attach a USB device to a virtual machine (VM), you must first enable USB host passthrough at the cluster level. 

To do this, specify a resource name and USB device name for each device you want first to add and then assign to a VM. You can allocate more than one device, each of which is known as a `selector` in the `HyperConverged` custom resource (CR), to a single resource name. If you have multiple identical USB devices on the cluster, you can choose to allocate a VM to a specific device. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster as a user who has the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Identify the USB device vendor and product: 

```shell-session
$ lsusb
```


**Example output**

```shell-session
Bus 003 Device 007: ID 1b1c:0a60 example_manufacturer example_product_name
```


     * If you cannot use the `lsusb` command, inspect the USB device configurations in the host’s `/sys/bus/usb/devices/` directory: 

```shell-session
for dev in *; do
    if [[ -f "$dev/idVendor" && -f "$dev/idProduct" ]]; then
        echo "Device: $dev"
        echo -n "  Manufacturer : "; cat "$dev/manufacturer"
        echo -n "  Product: "; cat "$dev/product"
        echo -n "  Vendor ID : "; cat "$dev/idVendor"
        echo -n "  Product ID: "; cat "$dev/idProduct"
        echo
    fi
done
```


**Example output**

```shell-session
Device: 3-7
  Manufacturer : example_manufacturer
  Product: example_product_name
  Vendor ID : 1b1c
  Product ID: 0a60
```


  2. Open the `HyperConverged` CR in your default editor by running the following command: 

```shell-session
$ oc edit hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
```


  3. Add the required USB device to the `permittedHostDevices` stanza of the `HyperConvered` CR. The following example adds a device with vendor ID `045e` and product ID `07a5`: 

```yaml
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  permittedHostDevices:
    usbHostDevices:
    - resourceName: kubevirt.io/peripherals
      selectors:
      - vendor: "045e"
        product: "07a5"
      - vendor: "062a"
        product: "4102"
      - vendor: "072f"
        product: "b100"
```


     * `spec.permittedHostDevices` defines the host devices that have permission to be used in the cluster. 
     * `spec.permittedHostDevices.usbHostDevices` defines a list of available USB devices. 
     * `spec.permittedHostDevices.usbHostDevices.resourceName` defines the USB device that you want to add and assign to the VM. In this example, the resource is bound to three devices, each of which is identified by `vendor` and `product` and is known as a `selector`. 




### 8.18.10.2. Connect a USB device to a virtual machine

You can configure virtual machine (VM) access to a USB device. This configuration enables the VM to connect to USB hardware that is attached to an OpenShift Container Platform node, as if the hardware and the VM are physically connected. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have attached the required USB device as a resource at the cluster level. 



**Procedure**

  1. In the `HyperConverged` custom resource (CR), find the assigned resource name of the USB device: 

```shell-session
$ oc get hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
```


Example output: 

```yaml
# ...
  spec:
    permittedHostDevices:
      usbHostDevices:
        - resourceName: kubevirt.io/peripherals
          selectors:
            - vendor: "045e"
              product: "07a5"
            - vendor: "062a"
              product: "4102"
            - vendor: "072f"
              product: "b100"
```


  2. Open the VM CR: 

```shell-session
$ oc edit vm <vm_name>
```


where: 

`<vm_name>`
     Specifies the name of the `VirtualMachine` CR. 

  3. Edit the CR by adding the USB device, as shown in the following example: 

Example configuration: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: example-vm
spec:
  template:
    spec:
      architecture: amd64
      domain:
        devices:
          hostDevices:
          - deviceName: kubevirt.io/peripherals
            name: local-peripherals
# ...
```


     * `spec.template.spec.domain.devices.hostDevices.deviceName` specifies the resource name from the `HyperConverged` CR. 
     * `spec.template.spec.domain.devices.hostDevices.name` defines the name of the USB device. 

  4. Save and apply your changes: 

```shell-session
$ oc apply -f <filename>.yaml
```


where: 

`<filename>`
     Specifies the name of the `VirtualMachine` manifest YAML file. 




## 8.18.11. Enabling descheduler evictions on virtual machines

You can use the descheduler to evict pods so that the pods can be rescheduled onto more appropriate nodes. If the pod is a virtual machine, the pod eviction causes the virtual machine to be live migrated to another node. 

### 8.18.11.1. Descheduler profiles

Use descheduler profiles to enable specific eviction strategies that rebalance your cluster based on criteria such as pod lifecycle or node utilization. 

Use the `KubeVirtRelieveAndMigrate` profile to enable the descheduler on a virtual machine. 

`KubeVirtRelieveAndMigrate`
    

The `KubeVirtRelieveAndMigrate` profile evicts pods from high-cost nodes to reduce overall resource expenses and enable workload migration. It also periodically rebalances workloads to help maintain similar spare capacity across nodes, which supports better handling of sudden workload spikes. Nodes can experience the following costs: 

  * **Resource utilization** : Increased resource pressure raises the overhead for running applications. 
  * **Node maintenance** : A higher number of containers on a node increases resource consumption and maintenance costs. 



The profile enables the `LowNodeUtilization` strategy with the alpha-level `EvictionsInBackground` feature. By default, the profile uses the `PrometheusCPUMemoryCombinedProfile` utilization metric. This metric combines CPU and memory utilization with pressure stall information (PSI) for both dimensions for comprehensive node load balancing. 

The profile also exposes the following customization fields: 

  * `devActualUtilizationProfile`: Enables load-aware descheduling. You can configure the following utilization profiles: 

    * `PrometheusCPUMemoryCombinedProfile` (default): Balances nodes based on CPU utilization, CPU PSI pressure, memory utilization, and memory PSI pressure. This profile is ideal for environments with memory overcommit enabled, as it spreads the load and prevents resource contention. 
    * `PrometheusCPUCombined`: Balances nodes based on CPU utilization and CPU PSI pressure only. Use this profile in environments without memory overcommit, where memory allocations are strictly guaranteed and CPU pressure is the primary driver for workload distribution. 

  * `devLowNodeUtilizationThresholds`: Sets experimental thresholds for the `LowNodeUtilization` strategy. Do not use this field with `devDeviationThresholds`. 
  * `devDeviationThresholds`: Treats nodes with below-average resource usage as underutilized to help redistribute workloads from overutilized nodes. Do not use this field with `devLowNodeUtilizationThresholds`. Supported values are: `Low` (10%:10%), `Medium` (20%:20%), `High` (30%:30%), `AsymmetricLow` (0%:10%), `AsymmetricMedium` (0%:20%), `AsymmetricHigh` (0%:30%). 
  * `devEnableSoftTainter`: Enables the soft-tainting component to dynamically apply or remove soft taints as scheduling hints. 



Example configuration: 

```yaml
apiVersion: operator.openshift.io/v1
kind: KubeDescheduler
metadata:
  name: cluster
  namespace: openshift-kube-descheduler-operator
spec:
  managementState: Managed
  deschedulingIntervalSeconds: 30
  mode: "Automatic"
  profiles:
    - KubeVirtRelieveAndMigrate
  profileCustomizations:
    devEnableSoftTainter: true
    devDeviationThresholds: AsymmetricLow
    devActualUtilizationProfile: PrometheusCPUMemoryCombinedProfile
```


The `KubeVirtRelieveAndMigrate` profile requires PSI metrics to be enabled on all worker nodes. You can enable this by applying the following `MachineConfig` custom resource (CR): 

Example `MachineConfig` CR: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 99-openshift-machineconfig-worker-psi-karg
spec:
  kernelArguments:
    - psi=1
```


Note

The name of the `MachineConfig` object is significant because machine configs are processed in lexicographical order. By default, a config that starts with `98-` disables PSI. To ensure that PSI is enabled, name your config with a higher prefix, such as `99-openshift-machineconfig-worker-psi-karg`. 

You can use this profile with the `SoftTopologyAndDuplicates` profile to also rebalance pods based on soft topology constraints, which can be useful in hosted control plane environments. 

### 8.18.11.2. Install the descheduler

The descheduler is not available by default. To enable the descheduler, you must install the Kube Descheduler Operator from the software catalog and enable one or more descheduler profiles. 

By default, the descheduler runs in predictive mode, which means that it only simulates pod evictions. You must change the mode to automatic for the descheduler to perform the pod evictions. 

Important

If you have enabled hosted control planes in your cluster, set a custom priority threshold to lower the chance that pods in the hosted control plane namespaces are evicted. Set the priority threshold class name to `hypershift-control-plane`, because it has the lowest priority value (`100000000`) of the hosted control plane priority classes. 

**Prerequisites**

  * You are logged in to OpenShift Container Platform as a user with the `cluster-admin` role. 
  * Access to the OpenShift Container Platform web console. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Create the required namespace for the Kube Descheduler Operator. 

     1. Navigate to **Administration** **Namespaces** and click **Create Namespace**. 
     2. Enter `openshift-kube-descheduler-operator` in the **Name** field, enter `openshift.io/cluster-monitoring=true` in the **Labels** field to enable descheduler metrics, and click **Create**. 

  3. Install the Kube Descheduler Operator. 

     1. Navigate to **Ecosystem** **Software Catalog**. 
     2. Type **Kube Descheduler Operator** into the filter box. 
     3. Select the **Kube Descheduler Operator** and click **Install**. 
     4. On the **Install Operator** page, select **A specific namespace on the cluster**. Select **openshift-kube-descheduler-operator** from the drop-down menu. 
     5. Adjust the values for the **Update Channel** and **Approval Strategy** to the desired values. 
     6. Click **Install**. 

  4. Create a descheduler instance. 

     1. From the **Ecosystem** **Installed Operators** page, click the **Kube Descheduler Operator**. 
     2. Select the **Kube Descheduler** tab and click **Create KubeDescheduler**. 
     3. Edit the settings as necessary. 

        1. To evict pods instead of simulating the evictions, change the **Mode** field to **Automatic**. 
        2. Expand the **Profiles** section and select `KubeVirtRelieveAndMigrate`. The `AffinityAndTaints` profile is enabled by default. 

Note

You can also configure the profiles and settings for the descheduler later using the OpenShift CLI (`oc`). 




### 8.18.11.3. Control which VMs the descheduler evicts

After the descheduler is installed, all migratable virtual machines (VMs) are eligible for eviction by default. You can exclude specific VMs from eviction, and limit how many VMs are evicted at once. 

**Prerequisites**

  * Install the descheduler in the OpenShift Container Platform web console or OpenShift CLI (`oc`). 



**Procedure**

  1. Stop the VM. 
  2. Configure the `KubeDescheduler` object with the `KubeVirtRelieveAndMigrate` profile and enable background evictions for improved VM eviction stability during live migration: 

```yaml
apiVersion: operator.openshift.io/v1
kind: KubeDescheduler
metadata:
  name: cluster
  namespace: openshift-kube-descheduler-operator
spec:
  deschedulingIntervalSeconds: 60
  profiles:
  - KubeVirtRelieveAndMigrate
  mode: Automatic
```


  3. Optional: To evict pods, set the `mode` field value to `Automatic`. By default, the descheduler does not evict pods. 
  4. Optional: Configure limits for the number of parallel evictions to improve stability in large clusters. 

The descheduler can limit the number of concurrent evictions per node and across the cluster by using the `evictionLimits` field. Set these limits to match the migration limits configured in the `HyperConverged` custom resource (CR). 

```yaml
spec:
  evictionLimits:
    node: 2
    total: 5
```


Set values that correspond to the migration limits in the `HyperConverged` CR: 

```yaml
spec:
  liveMigrationConfig:
    parallelMigrationsPerCluster: 5
    parallelOutboundMigrationsPerNode: 2
```


  5. Optional: To exclude the VM from eviction, add the `descheduler.alpha.kubernetes.io/prefer-no-eviction` annotation to the `spec.template.metadata.annotations` field. The change is applied dynamically and is propagated to the `VirtualMachineInstance` (VMI) object and the `virt-launcher` pod. 

Only the presence of the annotation is checked. The value is not evaluated, so `"true"` and `"false"` have the same effect. 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
spec:
  template:
    metadata:
      annotations:
        descheduler.alpha.kubernetes.io/prefer-no-eviction: "true"
```


  6. Start the VM. 



**Result**

The VM is now configured according to the descheduler settings. 

### 8.18.11.4. Additional resources

  * [Descheduler overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-descheduler-about)



## 8.18.12. About high availability for virtual machines

You can enable high availability for virtual machines (VMs) by manually deleting a failed node to trigger VM failover or by configuring remediating nodes. 

Manually deleting a failed node
     If a node fails and machine health checks are not deployed on your cluster, virtual machines with `runStrategy: Always` configured are not automatically relocated to healthy nodes. To trigger VM failover, you must manually delete the `Node` object. 
Configuring remediating nodes
     You can configure remediating nodes by installing the Self Node Remediation Operator or the Fence Agents Remediation Operator from the software catalog and enabling machine health checks or node remediation checks. 

For more information on remediation, fencing, and maintaining nodes, see the "Workload Availability for Red Hat OpenShift" documentation. 

### 8.18.12.1. Additional resources

  * [Workload Availability for Red Hat OpenShift](https://docs.redhat.com/en/documentation/workload_availability_for_red_hat_openshift/24.3)
  * [Trigger VM failover by deleting the failed node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/nodes#virt-delete-failed-node-vm-failover_virt-eviction-strategies "12.2.5. Trigger VM failover by deleting the failed node")



## 8.18.13. Tune the control plane

You can configure how the control plane handles concurrency when you create or migrate virtual machines (VMs). For example, set the `QPS` or `burst` rates to batch create virtual machines (VMs) in a batch, or tune migration settings in the `HyperConverged` custom resource (CR). 

### 8.18.13.1. Configure a highBurst profile

Use the `highBurst` profile to create and maintain a large number of virtual machines (VMs) in one cluster. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * Apply the following patch to enable the `highBurst` tuning policy profile: 

```shell-session
$ oc patch hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv \
  --type=json -p='[{"op": "add", "path": "/spec/tuningPolicy", \
  "value": "highBurst"}]'
```


**Verification**

  * Run the following command to verify the `highBurst` tuning policy profile is enabled: 

```shell-session
$ oc get kubevirt.kubevirt.io/kubevirt-kubevirt-hyperconverged \
  -n openshift-cnv -o go-template --template='{{range $config, \
  $value := .spec.configuration}} {{if eq $config "apiConfiguration" \
  "webhookConfiguration" "controllerConfiguration" "handlerConfiguration"}} \
  {{"\n"}} {{$config}} = {{$value}} {{end}} {{end}} {{"\n"}}
```


## 8.18.14. Assigning compute resources

In OpenShift Virtualization, compute resources assigned to virtual machines (VMs) are backed by either guaranteed CPUs or time-sliced CPU shares. 

Guaranteed CPUs, also known as CPU reservation, dedicate CPU cores or threads to a specific workload, which makes them unavailable to any other workload. Assigning guaranteed CPUs to a VM ensures that the VM will have sole access to a reserved physical CPU. Enable dedicated resources for VMs to use a guaranteed CPU. 

Time-sliced CPUs dedicate a slice of time on a shared physical CPU to each workload. You can specify the size of the slice during VM creation, or when the VM is offline. By default, each vCPU receives 100 milliseconds, or 1/10 of a second, of physical CPU time. 

The type of CPU reservation depends on the instance type or VM configuration. 

### 8.18.14.1. Overcommitting CPU resources

Time-slicing allows multiple virtual CPUs (vCPUs) to share a single physical CPU. This is known as _CPU overcommitment_. Guaranteed VMs can not be overcommitted. 

Configure CPU overcommitment to prioritize VM density over performance when assigning CPUs to VMs. With a higher CPU over-commitment of vCPUs, more VMs fit onto a given node. 

### 8.18.14.2. Overcommit CPUs to raise VM density

Set the CPU allocation ratio to control how many virtual CPUs map to each physical CPU. A higher ratio increases overcommitment, so each virtual machine (VM) pod requests fewer physical CPUs. 

For example, a mapping or ratio of 10:1 maps 10 virtual CPUs to 1 physical CPU by using time slices. 

To change the default number of vCPUs mapped to each physical CPU, set the `vmiCPUAllocationRatio` value in the `HyperConverged` CR. The pod CPU request is calculated by multiplying the number of vCPUs by the reciprocal of the CPU allocation ratio. For example, if `vmiCPUAllocationRatio` is set to 10, OpenShift Virtualization will request 10 times fewer CPUs on the pod for that VM. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Open the `HyperConverged` CR in your default editor by running the following command: 

```shell-session
$ oc edit hyperconvergeds.v1beta1.hco.kubevirt.io kubevirt-hyperconverged -n openshift-cnv
```


  2. Set the `vmiCPUAllocationRatio`: 

```yaml
...
spec:
  resourceRequirements:
    vmiCPUAllocationRatio: 1
# ...
```


When `vmiCPUAllocationRatio` is set to `1`, the maximum amount of vCPUs are requested for the pod. 




### 8.18.14.3. Additional resources

  * [Enabling dedicated resources for virtual machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-dedicated-resources-vm "8.18.7. Enabling dedicated resources for virtual machines")
  * [Pod Quality of Service Classes](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/)



## 8.18.15. About multi-queue functionality

Use multi-queue functionality to scale network throughput and performance on virtual machines (VMs) with multiple vCPUs. 

By default, the `queueCount` value, which is derived from the domain XML, is determined by the number of vCPUs allocated to a VM. Network performance does not scale as the number of vCPUs increases. Additionally, because `virtio-net` has only one transmit and receive queue, guests cannot send or receive packs in parallel. 

Note

Enabling `virtio-net` multi-queue does not offer significant improvements when the number of vNICs in a guest instance is proportional to the number of vCPUs. 

### 8.18.15.1. Known limitations

  * Message signaled interrupt (MSI) vectors are still consumed if `virtio-net` multi-queue is enabled in the host but not enabled in the guest operating system by the administrator. 
  * Each `virtio-net` queue consumes 64 KiB of kernel memory for the `vhost` driver. 



### 8.18.15.2. Enable multi-queue for VirtIO network interfaces

You can enable multi-queue functionality for network interfaces that use a VirtIO model, so that network traffic is processed across multiple vCPUs instead of one. 

**Procedure**

  1. Set the `networkInterfaceMultiqueue` value to `true` in the `VirtualMachine` manifest file of your VM to enable multi-queue functionality: 

```yaml
apiVersion: kubevirt.io/v1
kind: VM
spec:
  domain:
    devices:
      networkInterfaceMultiqueue: true
```


  2. Save the `VirtualMachine` manifest file to apply your changes. 



## 8.18.16. Managing virtual machines by using OpenShift GitOps

To automate and optimize virtual machine (VM) management in OpenShift Virtualization, you can use Red Hat OpenShift GitOps. 

With GitOps, you can set up VM deployments based on configuration files stored in a Git repository. This also makes it easier to automate, update, or replicate these configurations, as well to use version control for tracking their changes. 

**Prerequisites**

  * You have a GitHub account. For instructions to set up an account, see [Creating an account on GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github). 
  * OpenShift Virtualuzation has been installed on your OpenShift cluster. For instructions, see [OpenShift Virtualization installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/installing#installing-virt "4.3. Installing OpenShift Virtualization"). 
  * The OpenShift GitOps operator has been installed on your OpenShift cluster. For instructions, see [Installing GitOps](https://docs.openshift.com/gitops/1.15/installing_gitops/preparing-gitops-install.html). 



**Procedure**

Follow [the _Manage OpenShift virtual machines with GitOps_ learning path](https://developers.redhat.com/learning/learn:manage-openshift-virtual-machines-gitops/resource/resources:connect-and-configure-external-repository-argo-cd-virtual-machines) in performing these steps: 

  1. Connect an external Git repository to your Argo CD instance. 
  2. Create the required VM configuration in the Git repository. 
  3. Use the VM configuration to create VMs on your cluster. 



**Additional resources**

  * [OpenShift GitOps documentation](https://docs.openshift.com/gitops/)



## 8.18.17. Working with NUMA topology for virtual machines

To reduce latency in multiprocessor systems, Non-Uniform Memory Access (NUMA) architecture allows CPUs to access local memory faster than remote memory. This design optimizes performance by prioritizing memory resources that are physically closer to the processor. 

A CPU with multiple memory controllers can use any available memory across CPU complexes, regardless of where the memory is located. However, this increased flexibility comes at the expense of performance. 

_NUMA resource topology_ refers to the physical locations of CPUs, memory, and PCI devices relative to each other in a _NUMA zone_. In a NUMA architecture, a NUMA zone is a group of CPUs that has its own processors and memory. Colocated resources are said to be in the same NUMA zone, and CPUs in a zone have faster access to the same local memory than CPUs outside of that zone. 

A CPU processing a workload using memory that is outside its NUMA zone is slower than a workload processed in a single NUMA zone. For I/O-constrained workloads, the network interface on a distant NUMA zone slows down how quickly information can reach the application. 

Applications can achieve better performance by containing data and processing within the same NUMA zone. For high-performance workloads and applications, such as telecommunications workloads, the cluster must process pod workloads in a single NUMA zone so that the workload can operate to specification. 

### 8.18.17.1. NUMA topology with OpenShift Virtualization

You must enable the NUMA functionality for OpenShift Virtualization VMs to prevent performance degradation on nodes with multiple NUMA zones. This matters most for high-performance and latency-sensitive workloads. 

Without NUMA awareness, a VM’s virtual CPUs might run on one physical NUMA zone, while its memory is allocated on another. This "cross-node" communication significantly increases latency and reduces memory bandwidth, and can cause the interconnect buses which link the NUMA zones to become a bottleneck. 

When you enable the NUMA functionality for OpenShift Virtualization VMs, you allow the host to pass its physical topology directly to the guest operating system of the VM. The guest operating system can then make intelligent, NUMA-aware decisions about scheduling and memory allocation. This ensures that process threads and memory are kept on the same physical NUMA node. By aligning the virtual topology with the physical one, you minimize latency and maximize performance. 

VM owners can enable NUMA with `ComputeExclusive` (CX) instance types, which are specifically designed for high-performance, compute-intensive workloads, and are configured to use NUMA features. For information about creating VMs by using a CX instance type, see "Creating virtual machines from instance types". 

### 8.18.17.2. Node requirements for NUMA topology

Before you can enable NUMA functionality for OpenShift Virtualization VMs, your worker nodes must have huge pages enabled and a static CPU Manager policy configured. 

  * Worker nodes must have huge pages enabled. 
  * The `KubeletConfig` object on worker nodes must be configured with the `cpuManagerPolicy: static` spec to guarantee dedicated CPU allocation, which is a prerequisite for NUMA pinning. 

Example `cpuManagerPolicy: static` spec: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: cpu-numa-static-config
spec:
  kubeletConfig:
    cpuManagerPolicy: static
# ...
```


### 8.18.17.3. Check whether a VM is configured for vNUMA

Check whether a virtual machine (VM) is configured for virtual non-uniform memory access (vNUMA), so you can confirm that a latency-sensitive workload is getting the memory locality it depends on. 

You can verify whether an already deployed VM is configured for vNUMA by checking the `spec.domain.cpu.numa` attribute. This is displayed as a **vNUMA** badge in the OpenShift Container Platform web console. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster with OpenShift Virtualization installed. 
  * If you want to use the command line for verification, you must have installed the OpenShift CLI (`oc`). Otherwise, you only need access to the OpenShift Container Platform web console. 



**Procedure**

  * To verify vNUMA status on the command line, check that the `spec.domain.cpu.numa` attribute is configured by using the OpenShift CLI (`oc`). Run the following command: 

```shell-session
$ oc get vm <vm_name> -n <namespace> -o jsonpath='{.spec.template.spec.domain.cpu.numa}'
```


If any output other than an empty string is returned, vNUMA is enabled for the VM. 

  * To verify vNUMA status in a GUI, check if the VM has a **vNUMA** badge in the OpenShift Container Platform web console. Go to **VirtualMachines** **Virtual machines** **VirtualMachine details** , and check either the **Overview** or the **Configuration** tabs. 



### 8.18.17.4. Hot plug and NUMA resource alignment

Disable the default hot plug capability of a virtual machine (VM) to keep its resource requests aligned with NUMA. Default hot plug multipliers can inflate a VM’s socket request and cause deployment failures. 

_Hot plugging_ is the ability to dynamically add resources such as memory or CPU to a VM while it is running. Default OpenShift Virtualization hot plug multipliers can cause VMs to request an excessive number of sockets. For example, if your VM requests 10 sockets, the default hot plug behavior multiplies this by 4, which means that the total request is 40 sockets. This can exceed the recommended CPUs supported by the Kernel-based Virtual Machine (KVM), which can cause deployment failures. 

#### 8.18.17.4.1. Disable CPU hot plug for an instance type

You can disable the CPU hot plug for an instance type. Every VM created from that instance type inherits the setting, which standardizes VM configurations and keeps CPU allocation NUMA-aware. 

When a VM is created by using an instance type where the CPU hot plug is disabled, the VM inherits these settings and the CPU hot plug is disabled for that VM. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a YAML file for a `VirtualMachineClusterInstancetype` custom resource (CR). Add a `maxSockets` spec to the instance type that you want to configure. 

Example `VirtualMachineClusterInstancetype` CR: 

```yaml
apiVersion: instancetype.kubevirt.io/v1beta1
kind: VirtualMachineClusterInstancetype
metadata:
  name: cx1.mycustom-numa-instance
spec:
  cpu:
    dedicatedCPUPlacement: true
    isolateEmulatorThread: true
    numa:
      guestMappingPassthrough: {}
    guest: 8
    maxSockets: 8
  memory:
    guest: 16Gi
    hugepages:
      pageSize: 1Gi
```


where: 

`spec.cpu.dedicatedCPUPlacement`
     Specifies whether dedicated resources are allocated to the VM instance. If this is set to `true`, the VM’s VCPUs are pinned to physical host CPUs. This is often used for high-performance workloads to minimize scheduling jitter. 
`spec.cpu.isolateEmulatorThread`
     Specifies whether the QEMU emulator thread should be isolated and run on a dedicated physical CPU core. This is a performance optimization that is typically used alongside the `dedicatedCPUPlacement` spec. 
`spec.cpu.numa`
     Specifies the NUMA topology configuration for the VM. 
`spec.cpu.numa.guestMappingPassthrough`
     Specifies that the VM’s NUMA topology should directly pass through the NUMA topology of the underlying host machine. This is critical for applications that are NUMA-aware and require optimal performance. 
`spec.cpu.guest`
     Specifies the total number of vCPUs to be allocated to the VM. 
`spec.cpu.maxSockets`
     Specifies the maximum number of CPU sockets the VM is allowed to have. 
`spec.memory`
     Specifies the memory configuration for the VM. 
`spec.memory.guest`
     Specifies the total amount of memory to be allocated to the VM. 
`spec.memory.hugepages`
     Specifies configuration related to hugepages. 
`spec.memory.hugepages.pageSize`
     Specifies the size of the hugepages to be used for the VM’s memory. 

  2. Create the `VirtualMachineClusterInstancetype` CR by running the following command: 

```shell-session
$ oc create -f <filename>.yaml
```


**Verification**

  1. Create a VM that uses the updated `VirtualMachineClusterInstancetype` configuration. 
  2. Inspect the configuration of the created VM by running the following command and inspecting the output: 

```shell-session
$ oc get vmi <vm_name> -o yaml
```


**Example output**

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstance
metadata:
  name: example-vmi
  labels:
    instancetype.kubevirt.io/cluster-instancetype: cx1.example-numa-instance
spec:
  domain:
    cpu:
      dedicatedCPUPlacement: true
      isolateEmulatorThread: true
      sockets: 8
      cores: 1
      threads: 1
      numa:
        guestMappingPassthrough: {}
      guest: 8
      maxSockets: 8
# ...
```


The update has applied successfully if in the `spec.template.spec.domain.cpu` section: 

     * The `sockets` value matches the `maxSockets` and `guest` values from the instance type, which ensures that no extra hot plug slots are configured. 
     * The `dedicatedCPUPlacement` and `isolateEmulatorThread` fields are present and set to `true`. 




#### 8.18.17.4.2. Adjust or disable CPU hot plug for a VM

You can adjust or disable the CPU hot plug for an individual virtual machine (VM). This is the simplest option for large, performance-critical VMs that need a fixed CPU allocation from the start. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Modify the `VirtualMachine` custom resource (CR) for the VM that you want to configure to add a `maxSockets` and `sockets` spec: 

```yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: large-numa-vm
spec:
  template:
    spec:
      domain:
        cpu:
          maxSockets: 10
          sockets: 10
          cores: 1
          threads: 1
```


By explicitly setting `maxSockets` and `sockets` to a value of 10 or higher, you are specifying that additional capacity is not reserved for hot plugging, which ensures that the entire requested cores are the actual cores allocated. 

  2. Apply the changes to the `VirtualMachine` CR by running the following command: 

```shell-session
$ oc apply -f <filename>.yaml
```


**Verification**

  1. Check that you have configured the `maxSockets` and `sockets` values correctly, by running the following commands: 

```shell-session
$ oc get vmi -o jsonpath='{.spec.domain.cpu.maxSockets}'
```


```shell-session
$ oc get vmi -o jsonpath='{.spec.domain.cpu.sockets}'
```


If the configuration was successful, the outputs are the `maxSockets` and `sockets` values that you set in the previous procedure: 

**Example output**

```shell-session
10
```


#### 8.18.17.4.3. Disable CPU hot plug for all VMs in a cluster

You can disable hot plugging for every virtual machine (VM) in a cluster to give each VM a fixed CPU allocation, without configuring VMs or instance types individually. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have installed the OpenShift Virtualization Operator. 



**Procedure**

  1. Modify the `HyperConverged` CR and set the `maxHotplugRatio` value to `1.0`: 

```yaml
apiVersion: hco.kubevirt.io/v1beta1
kind: HyperConverged
metadata:
  name: kubevirt-hyperconverged
  namespace: openshift-cnv
spec:
  # ...
  kubevirtConfiguration:
    developerConfiguration:
      maxHotplugRatio: 1.0
# ...
```


  2. Apply the changes to the `HyperConverged` CR by running the following command: 

```shell-session
$ oc apply -f <filename>.yaml
```


**Verification**

  1. Check that you have configured the `maxHotplugRatio` value correctly, by running the following command: 

```shell-session
$ oc get hyperconvergeds.v1beta1.hco.kubevirt.io -n openshift-cnv -o jsonpath='{.spec.liveUpdateConfiguration.maxHotplugRatio}'
```


If the configuration was successful, the output is the `maxHotplugRatio` value that you set in the previous procedure: 

**Example output**

```shell-session
1.0
```


### 8.18.17.5. Limitations of NUMA for OpenShift Virtualization

NUMA topology for OpenShift Virtualization VMs has limitations that affect rescheduling, live migration, and PCI devices such as GPUs. Review them before you enable NUMA for a workload. 

Asymmetrical topology
     The host scheduler cannot guarantee assigning specific NUMA nodes to a VM. For example, if a VM is rescheduled to a different host machine because of a restart or maintenance, the new host might have a different physical NUMA layout. This means that the VM could be presented with an asymmetrical NUMA topology that reflects the new host’s configuration, rather than its original or intended layout. This change can have a negative impact on the VM’s performance. 
Live migration challenges
     Migrating a NUMA-enabled VM to a different host node can be challenging if the destination node’s NUMA topology differs significantly from the source node’s. A mismatch between the NUMA layouts of the source and destination can lead to a degradation of the VM’s performance after the migration is complete. 
No support for PCI NUMA nodes
     There is no explicit support for passing GPU NUMA zone information to the VM. This means that the VM’s guest operating system is not aware of the NUMA locality of PCI devices such as GPUs. For workloads that heavily rely on these devices, this lack of awareness could potentially lead to reduced performance if the GPU’s memory is not local to the accessing CPU within the NUMA architecture. 

### 8.18.17.6. vNUMA live migration support by VM size and policy

The Topology Manager policy configured on a node determines whether a virtual machine (VM) can live migrate. Check which combinations of VM size and policy are supported before you choose one. 

Topology Manager policies determine how CPU and memory resources are allocated with respect to the physical NUMA nodes of the host. There are four available policies: `None`, `single-numa-node`, `best-effort`, and `restricted`. 

The following table outlines which policies are supported for different VM configurations, and their effect on live migration. 

  * A small VM is defined as a VM with less total cores than half of cores in NUMA node. 
  * A large VM is defined as a VM with more total cores than half of cores in NUMA node. 
  * An extra large VM is defined as a VM with more cores than 1 NUMA node. 



VM size| Topology Manager policy| Tested support status  
---|---|---  
Any  |  single-numa-node  |  The VM fails to start because the pod requests more CPUs than a single NUMA node on the host can provide. This triggers a topology affinity error during scheduling, which is expected behavior given the node’s hardware limits.   
Any  |  None  |  Live migration does not work. This is a known issue. The process ends with an incorrect memnode allocation error, and libvirt rejects the XML manifest generated by KubeVirt. See release notes for additional information.   
Small  |  None  |  Live migration works, as expected.   
Small  |  single-numa-node  |  Live migration works, as expected.   
Small  |  best-effort  |  Live migration works, as expected.   
Small  |  restricted  |  Live migration works, as expected.   
Large  |  single-numa-node  |  Live migration works, as expected.   
Large  |  best-effort  |  Live migration works, as expected.   
Large  |  restricted  |  Live migration works, as expected.   
Extra large  |  None  |  Live migration works, as expected.   
Extra large  |  best-effort  |  Live migration works, as expected.   
Extra large  |  restricted  |  VMs do not work, as expected.   
Show more

### 8.18.17.7. Additional resources

  * [Topology Manager policies](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#using-cpu-manager_topology-manager-policies)
  * [Instance types](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/creating-virtual-machines#virt-creating-vms-from-instance-types "7.5. Instance types")
