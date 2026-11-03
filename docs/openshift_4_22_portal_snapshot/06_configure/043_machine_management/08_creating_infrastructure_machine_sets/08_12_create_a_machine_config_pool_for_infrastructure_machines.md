# 8.12. Create a machine config pool for infrastructure machines

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
