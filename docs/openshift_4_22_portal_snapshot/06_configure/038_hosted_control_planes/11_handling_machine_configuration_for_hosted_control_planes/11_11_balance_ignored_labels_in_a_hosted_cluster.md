# 11.11. Balance ignored labels in a hosted cluster

After you scale up your node pools, you can use `balancingIgnoredLabels` to evenly distribute the machines across node pools. 

**Prerequisites**

  * You have created the `HostedCluster` and `NodePool` resources. 



**Procedure**

  1. Add the `node.group.balancing.ignored` label to each of the relevant node pool by using the same label value. Run the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  nodepool <node_pool_name> \
  --type=merge \
  --patch='{"spec": {"nodeLabels": {"node.group.balancing.ignored": "<label_name>"}}}'
```


  2. Enable cluster autoscaling for your hosted cluster by running the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
 hostedcluster <hosted_cluster_name> \
 --type=merge \
 --patch='{"spec": {"autoscaling": {"balancingIgnoredLabels": ["node.group.balancing.ignored"]}}}'
```


  3. Remove the `spec.replicas` field from the `NodePool` resource to allow the cluster autoscaler to manage the node count. Run the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  nodepool <node_pool_name> \
  --type=json \
  --patch='[{"op": "remove", "path": "/spec/replicas"}]'
```


  4. Enable cluster autoscaling to configure the minimum and maximum node counts for your node pools. Run the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  nodepool <nodepool_name> \
  --type=merge --patch='{"spec": {"autoScaling": {"max": 3, "min": 1}}}'
```


  5. Generate the `kubeconfig` file by running the following command: 

```shell-session
$ hcp create kubeconfig \
  --name <hosted_cluster_name> \
  --namespace <hosted_cluster_namespace> > nested.config
```


  6. After you scale up the node pools, check that all compute nodes are in the `Ready` status by running the following command: 

```shell-session
$ oc --kubeconfig nested.config get nodes -l 'hypershift.openshift.io/nodePool=<node_pool_name>'
```


  7. Confirm that the new nodes contain the `node.group.balancing.ignored` label by running the following command: 

```shell-session
$ oc --kubeconfig nested.config get nodes \
  -l 'hypershift.openshift.io/nodePool=<node_pool_name>' \
  -o jsonpath='{.items[*].metadata.labels}' | grep "node.group.balancing.ignored"
```


  8. Enable cluster autoscaling for your hosted cluster by running the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  hostedcluster <hosted_cluster_name> \
  --type=merge \
  --patch='{"spec": {"autoscaling": {"balancingIgnoredLabels": ["node.group.balancing.ignored"]}}}'
```


**Verification**

  * Verify that the number of nodes provisioned by each node pool is evenly distributed. For example, if you created three node pools with the same label value, the node counts might be 3, 2, and 3. Run the following command: 

```shell-session
$ oc --kubeconfig nested.config get nodes -l 'hypershift.openshift.io/nodePool=<node_pool_name>'
```
