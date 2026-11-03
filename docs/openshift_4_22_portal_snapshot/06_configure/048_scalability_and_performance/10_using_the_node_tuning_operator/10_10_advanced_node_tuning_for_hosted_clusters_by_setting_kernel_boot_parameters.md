# 10.10. Advanced node tuning for hosted clusters by setting kernel boot parameters

For more advanced tuning in hosted control planes, which requires setting kernel boot parameters, you can also use the Node Tuning Operator. The following example shows how you can create a node pool with huge pages reserved. 

**Procedure**

  1. Create a `ConfigMap` object that contains a `Tuned` object manifest for creating 10 huge pages that are 2 MB in size. Save this `ConfigMap` manifest in a file named `tuned-hugepages.yaml`: 

```yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: tuned-hugepages
      namespace: clusters
    data:
      tuning: |
        apiVersion: tuned.openshift.io/v1
        kind: Tuned
        metadata:
          name: hugepages
          namespace: openshift-cluster-node-tuning-operator
        spec:
          profile:
          - data: |
              [main]
              summary=Boot time configuration for hugepages
              include=openshift-node
              [bootloader]
              cmdline_openshift_node_hugepages=hugepagesz=2M hugepages=50
            name: openshift-node-hugepages
          recommend:
          - priority: 20
            profile: openshift-node-hugepages
```


Note

The `.spec.recommend.match` field is intentionally left blank. In this case, this `Tuned` object is applied to all nodes in the node pool where this `ConfigMap` object is referenced. Group nodes with the same hardware configuration into the same node pool. Otherwise, TuneD operands can calculate conflicting kernel parameters for two or more nodes that share the same node pool. 

  2. Create the `ConfigMap` object in the management cluster: 

```shell-session
$ oc --kubeconfig="<management_cluster_kubeconfig>" create -f tuned-hugepages.yaml
```


Replace `<management_cluster_kubeconfig>` with the name of your management cluster `kubeconfig` file. 

  3. Create a `NodePool` manifest YAML file, customize the upgrade type of the `NodePool`, and reference the `ConfigMap` object that you created in the `spec.tuningConfig` section. Create the `NodePool` manifest and save it in a file named `hugepages-nodepool.yaml` by using the `hcp` CLI: 

```shell-session
$ hcp create nodepool aws \
  --cluster-name <hosted_cluster_name> \
  --name <nodepool_name> \
  --node-count <nodepool_replicas> \
  --instance-type <instance_type> \
  --render > hugepages-nodepool.yaml
```


where: 

     * `<hosted_cluster_name>`: The name of your hosted cluster. 
     * `<nodepool_name>`: The name of your node pool. 
     * `<nodepool_replicas>`: The number of your node pool replicas, for example, `2`. 
     * `<instance_type>`: The instance type, for example, `m5.2xlarge`. 

Note

The `--render` flag in the `hcp create` command does not render the secrets. To render the secrets, you must use both the `--render` and the `--render-sensitive` flags in the `hcp create` command. 

  4. In the `hugepages-nodepool.yaml` file, set `.spec.management.upgradeType` to `InPlace`, and set `.spec.tuningConfig` to reference the `tuned-hugepages` `ConfigMap` object that you created. 

```yaml
    apiVersion: hypershift.openshift.io/v1alpha1
    kind: NodePool
    metadata:
      name: hugepages-nodepool
      namespace: clusters
      ...
    spec:
      management:
        ...
        upgradeType: InPlace
      ...
      tuningConfig:
      - name: tuned-hugepages
```


Note

To avoid the unnecessary re-creation of nodes when you apply the new `MachineConfig` objects, set `.spec.management.upgradeType` to `InPlace`. If you use the `Replace` upgrade type, nodes are fully deleted and new nodes can replace them when you apply the new kernel boot parameters that the TuneD operand calculated. 

  5. Create the `NodePool` in the management cluster: 

```shell-session
$ oc --kubeconfig="<management_cluster_kubeconfig>" create -f hugepages-nodepool.yaml
```


**Verification**

After the nodes are available, the containerized TuneD daemon calculates the required kernel boot parameters based on the applied TuneD profile. After the nodes are ready and reboot once to apply the generated `MachineConfig` object, you can verify that the TuneD profile is applied and that the kernel boot parameters are set. 

  1. List the `Tuned` objects in the hosted cluster: 

```shell-session
$ oc --kubeconfig="<hosted_cluster_kubeconfig>" get tuned.tuned.openshift.io \
  -n openshift-cluster-node-tuning-operator
```


**Example output**

```shell-session
NAME                 AGE
default              123m
hugepages-8dfb1fed   1m23s
rendered             123m
```


  2. List the `Profile` objects in the hosted cluster: 

```shell-session
$ oc --kubeconfig="<hosted_cluster_kubeconfig>" get profile.tuned.openshift.io \
  -n openshift-cluster-node-tuning-operator
```


**Example output**

```shell-session
NAME                           TUNED                      APPLIED   DEGRADED   AGE
nodepool-1-worker-1            openshift-node             True      False      132m
nodepool-1-worker-2            openshift-node             True      False      131m
hugepages-nodepool-worker-1    openshift-node-hugepages   True      False      4m8s
hugepages-nodepool-worker-2    openshift-node-hugepages   True      False      3m57s
```


Both of the worker nodes in the new `NodePool` have the `openshift-node-hugepages` profile applied. 

  3. To confirm that the tuning was applied correctly, start a debug shell on a node and check `/proc/cmdline`. 

```shell-session
$ oc --kubeconfig="<hosted_cluster_kubeconfig>" \
  debug node/nodepool-1-worker-1 -- chroot /host cat /proc/cmdline
```


**Example output**

```shell-session
BOOT_IMAGE=(hd0,gpt3)/ostree/rhcos-... hugepagesz=2M hugepages=50
```
