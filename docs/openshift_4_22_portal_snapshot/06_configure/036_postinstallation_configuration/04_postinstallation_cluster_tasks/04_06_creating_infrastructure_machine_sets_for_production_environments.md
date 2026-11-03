# 4.6. Creating infrastructure machine sets for production environments

Create infrastructure machine sets to host cluster infrastructure components without counting those machines toward subscription limits. 

You can create a compute machine set to create machines that host only infrastructure components, such as the default router, the integrated container image registry, and components for cluster metrics and monitoring. These infrastructure machines are not counted toward the total number of subscriptions that are required to run the environment. 

For information on infrastructure nodes and which components can run on infrastructure nodes, see "Creating infrastructure machine sets". 

To create an infrastructure node, see "Use a machine set to create an infrastructure node", "Assign a label to infrastructure nodes", or "Use a machine config pool for infrastructure nodes". 

For sample machine sets that you can use with these procedures, see "Creating machine sets for different clouds". 

Applying a specific node selector to all infrastructure components causes OpenShift Container Platform to schedule those workloads on nodes with that label; see "Schedule infrastructure workloads using node selectors". 

**Additional resources**

  * [Creating infrastructure machine sets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#creating-infrastructure-machinesets)
  * [Use a machine set to create an infrastructure node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/post-install-cluster-tasks#machineset-creating_post-install-cluster-tasks "4.6.1. Create a compute machine set")
  * [Assign a label to infrastructure nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/post-install-cluster-tasks#creating-an-infra-node_post-install-cluster-tasks "4.6.2. Create an infrastructure node")
  * [Use a machine config pool for infrastructure nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/post-install-cluster-tasks#creating-infra-machines_post-install-cluster-tasks "4.6.3. Create a machine config pool for infrastructure machines")
  * [Creating machine sets for different clouds](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#creating-infrastructure-machinesets-clouds)
  * [Schedule infrastructure workloads using node selectors](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/post-install-cluster-tasks#moving-resources-to-infrastructure-machinesets_post-install-cluster-tasks "4.8. Moving resources to infrastructure machine sets")



## 4.6.1. Create a compute machine set

To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning. 

**Prerequisites**

  * Deploy an OpenShift Container Platform cluster. 
  * Install the OpenShift CLI (`oc`). 
  * Log in to `oc` as a user with `cluster-admin` permission. 



**Procedure**

  1. Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`. 

Ensure that you set the `<clusterID>` and `<role>` parameter values. 

  2. Optional: If you are not sure which value to set for a specific field, you can check an existing compute machine set from your cluster. 

     1. To list the compute machine sets in your cluster, run the following command: 

```shell-session
$ oc get machinesets -n openshift-machine-api
```


The following is example output: 

```shell-session
NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1d   0         0                             55m
agl030519-vplxk-worker-us-east-1e   0         0                             55m
agl030519-vplxk-worker-us-east-1f   0         0                             55m
```


     2. To view values of a specific compute machine set custom resource (CR), run the following command: 

```shell-session
$ oc get machineset <machineset_name> \
  -n openshift-machine-api -o yaml
```


The following is example output: 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-<role>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
    spec:
      providerSpec:
        ...
```


where: 

`metadata.labels.machine.openshift.io/cluster-api-cluster`
     Specifies the cluster infrastructure ID. 
`metadata.labels.name`
    

Specifies a default node label. 

Note

For clusters that have user-provisioned infrastructure, a compute machine set can only create `worker` and `infra` type machines. 

`spec.template.metadata.spec.providerSpec`
     Specifies the values of the compute machine set CR. The values are platform-specific. For more information about `<providerSpec>` parameters in the CR, see the sample compute machine set CR configuration for your provider. 

  3. Create a `MachineSet` CR by running the following command: 

```shell-session
$ oc create -f <file_name>.yaml
```


**Verification**

  * View the list of compute machine sets by running the following command: 

```shell-session
$ oc get machineset -n openshift-machine-api
```


The following is example output: 

```shell-session
NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
agl030519-vplxk-infra-us-east-1a    1         1         1       1           11m
agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
agl030519-vplxk-worker-us-east-1d   0         0                             55m
agl030519-vplxk-worker-us-east-1e   0         0                             55m
agl030519-vplxk-worker-us-east-1f   0         0                             55m
```


When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again. 




## 4.6.2. Create an infrastructure node

To reduce subscription costs, you can use labels to configure compute nodes as infrastructure nodes, where you can move infrastructure resources. 

After you create the infrastructure nodes, you can move appropriate workloads to those nodes by using taints and tolerations. 

You can optionally create a default cluster-wide node selector. The default node selector is applied to pods created in all namespaces and creates an intersection with any existing node selectors on a pod, which additionally constrains the pod’s selector. 

Important

  * See "Creating infrastructure machine sets" for installer-provisioned infrastructure environments or for any cluster where the control plane nodes are managed by the Machine API. 
  * If the default node selector key conflicts with the key of a pod’s label, then the default node selector is not applied. 

However, do not set a default node selector that might cause a pod to become unschedulable. For example, setting the default node selector to a specific node role, such as `node-role.kubernetes.io/infra=""`, when a pod’s label is set to a different node role, such as `node-role.kubernetes.io/master=""`, can cause the pod to become unschedulable. For this reason, use caution when setting the default node selector to specific node roles. 

You can alternatively use a project node selector to avoid cluster-wide node selector key conflicts. 




**Procedure**

  1. Add a label to the compute nodes that you want to act as infrastructure nodes by running the following command: 

```shell-session
$ oc label node <node-name> node-role.kubernetes.io/infra=""
```


  2. Check to see if applicable nodes now have the `infra` role by running the following command: 

```shell-session
$ oc get nodes
```


  3. Optional: Create a default cluster-wide node selector. 

     1. Edit the `Scheduler` object by running the following command: 

```shell-session
$ oc edit scheduler cluster
```


     2. Add the `defaultNodeSelector` field with the appropriate node selector by running the following command: 

```yaml
apiVersion: config.openshift.io/v1
kind: Scheduler
metadata:
  name: cluster
spec:
  defaultNodeSelector: node-role.kubernetes.io/infra=""
# ...
```


This example node selector deploys pods on infrastructure nodes by default. 

     3. Save the file to apply the changes. 

You can now move infrastructure resources to the new infrastructure nodes and remove any workloads that you do not want, or that do not belong, on the new infrastructure node. See the list of workloads supported for use on infrastructure nodes in "OpenShift Container Platform infrastructure components". 




**Additional resources**

  * [Project node selectors](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#project-node-selectors_nodes-scheduler-node-selectors)



## 4.6.3. Create a machine config pool for infrastructure machines

You can create a machine configuration pool for infrastructure machines to apply dedicated configuration to infra machines. You might want to apply dedicated configuration to infra machines because they run distinct workloads from other nodes in the cluster. 

Important

Creating a custom machine configuration pool overrides default worker pool configurations if they refer to the same file or unit. 

**Procedure**

  1. Add a label to the node you want to assign as the infra node by running the following command: 

```shell-session
$ oc label node <node_name> node-role.kubernetes.io/infra=
```


where: 

`<node_name>`
     Specifies the name of the node you want to assign as an infra node. 

  2. Create a YAML file that defines the machine config pool, as in the following example: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: infra
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,infra]}
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/infra: ""
```


     * Add the worker role and your custom role in the `spec.machineConfigSelector.matchExpressions[]` field. 
     * Add the label you added to the node in the `spec.nodeSelector.matchLabels` field. 

Note

Custom machine config pools inherit machine configs from the worker pool. Custom pools use any machine config targeted for the worker pool, but add the ability to also deploy changes that are targeted at only the custom pool. Because a custom pool inherits resources from the worker pool, any change to the worker pool also affects the custom pool. 

  3. After you have the YAML file, you can create the machine config pool by specifying the file you created in the following command: 

```shell-session
$ oc create -f <filename>
```


  4. Check the machine configs to ensure that the infrastructure configuration rendered successfully by running the following command: 

```shell-session
$ oc get machineconfig
```


**Example output**

```shell-session
NAME                                                        GENERATEDBYCONTROLLER                      IGNITIONVERSION   CREATED
00-master                                                   365c1cfd14de5b0e3b85e0fc815b0060f36ab955   3.5.0             31d
00-worker                                                   365c1cfd14de5b0e3b85e0fc815b0060f36ab955   3.5.0             31d
# ...
rendered-infra-4e48906dca84ee702959c71a53ee80e7             365c1cfd14de5b0e3b85e0fc815b0060f36ab955   3.5.0             23m
```


You should see a new machine config, with the `rendered-infra-*` prefix. 

  5. Optional: To deploy changes to a custom pool, create a machine config that uses the custom pool name as the label, such as `infra`. Note that this is not required and only shown for instructional purposes. In this manner, you can apply any custom configurations specific to only your infra nodes. 

Note

After you create the new machine config pool, the MCO generates a new rendered config for that pool, and associated nodes of that pool reboot to apply the new configuration. 

     1. Create a YAML file that defines the machine config pool, as in the following example: 

```shell-session
$ cat infra.mc.yaml
```


**Example output**

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  name: 51-infra
  labels:
    machineconfiguration.openshift.io/role: <role>
spec:
  config:
    ignition:
      version: 3.5.0
    storage:
      files:
      - path: /etc/infratest
        mode: 0644
        contents:
          source: data:,infra
```


where: 

`role`
     Specifies the label you added to the node as a `nodeSelector`. 

     2. Apply the machine config to the infra-labeled nodes by running the following command: 

```shell-session
$ oc create -f infra.mc.yaml
```


  6. Confirm that your new machine config pool is available by running the following command: 

```shell-session
$ oc get mcp
```


**Example output**

```shell-session
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
infra    rendered-infra-60e35c2e99f42d976e084fa94da4d0fc    True      False      False      1              1                   1                     0                      4m20s
master   rendered-master-9360fdb895d4c131c7c4bebbae099c90   True      False      False      3              3                   3                     0                      91m
worker   rendered-worker-60e35c2e99f42d976e084fa94da4d0fc   True      False      False      2              2                   2                     0                      91m
```


In this example, the role of the node was changes from `worker` to `infra`. 




**Additional resources**

  * [Node configuration management with machine config pools](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-machine-config-pools_control-plane)
