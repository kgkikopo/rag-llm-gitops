# 11.10. Set the priority expander in a hosted cluster

You can define the priority for your node pools and create high priority machines before low priority machines by using the priority expander in your hosted cluster. 

**Prerequisites**

  * You have created the `HostedCluster` and `NodePool` resources. 



**Procedure**

  1. To define the priority for your node pools, create a config map named `priority-expander-configmap.yaml` in your hosted cluster. Node pools with low numbers receive high priority. See the following example configuration: 

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-autoscaler-priority-expander
  namespace: kube-system
# ...
data:
  priorities: |-
    10:
      - ".*<node_pool_name1>.*"
    100:
      - ".*<node_pool_name2>.*"
# ...
```


  2. Generate the `kubeconfig` file by running the following command: 

```shell-session
$ hcp create kubeconfig --name <hosted_cluster_name> --namespace <hosted_cluster_namespace> > nested.config
```


  3. Create the `ConfigMap` object by running the following command: 

```shell-session
$ oc --kubeconfig nested.config create -f priority-expander-configmap.yaml
```


  4. Enable cluster autoscaling by setting the priority expander for your hosted cluster. Run the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  hostedcluster <hosted_cluster_name> \
  --type=merge \
  --patch='{"spec": {"autoscaling": {"scaling": "ScaleUpOnly", "maxPodGracePeriod": 60, "expanders": ["Priority"]}}}'
```


  5. Remove the `spec.replicas` field from the `NodePool` resource to allow the cluster autoscaler to manage the node count. Run the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  nodepool <node_pool_name> \
  --type=json
  --patch='[{"op": "remove", "path": "/spec/replicas"}]'
```


  6. Enable cluster autoscaling to configure the minimum and maximum node counts for your node pools. Run the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  nodepool <nodepool_name> \
  --type=merge --patch='{"spec": {"autoScaling": {"max": 3, "min": 1}}}'
```


**Verification**

  * After you apply new workloads, verify that the compute nodes associated with the priority node pool are scaled up first. Run the following command to check the status of the compute node: 

```shell-session
$ oc --kubeconfig nested.config get nodes -l 'hypershift.openshift.io/nodePool=<node_pool_name>'
```
