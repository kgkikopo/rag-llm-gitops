# 8.11. Create an infrastructure node

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

  * [OpenShift Container Platform infrastructure components](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/creating-infrastructure-machinesets#infrastructure-components_creating-infrastructure-machinesets "8.1. Move components to infrastructure nodes to reduce costs")
  * [Moving resources to infrastructure machine sets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/creating-infrastructure-machinesets#moving-resources-to-infrastructure-machinesets_creating-infrastructure-machinesets "8.14. Move resources to infrastructure machine sets")
