# 11.8. Scale up workloads in a hosted cluster

To scale up the workloads in your hosted cluster, you can use the `ScaleUpOnly` behavior. 

**Prerequisites**

  * You have created the `HostedCluster` and `NodePool` resources. 



**Procedure**

  1. Enable cluster autoscaling for your hosted cluster by setting the scaling behavior to `ScaleUpOnly`. Run the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> hostedcluster <hosted_cluster_name> --type=merge --patch='{"spec": {"autoscaling": {"scaling": "ScaleUpOnly", "maxPodGracePeriod": 60}}}'
```


  2. Remove the `spec.replicas` field from the `NodePool` resource to allow the cluster autoscaler to manage the node count. Additionally, enable cluster autoscaling to configure the minimum and maximum node counts for your node pools. Enter the following command: 

```shell-session
$ oc -n clusters patch nodepool yhe-hosted-ap-northeast-1a \
  --type=json \
  -p='[
    {"op":"remove","path":"/spec/replicas"},
    {"op":"add","path":"/spec/autoScaling","value":{"min":2,"max":4}}
  ]'
```


**Verification**

  1. Verify that all compute nodes are in the `Ready` status by running the following command: 

```shell-session
$ oc --kubeconfig <hosted_cluster_name>.kubeconfig get nodes
```


  2. Verify that the compute nodes are scaled up successfully by checking the node count for your node pools. Run the following command: 

```shell-session
$ oc --kubeconfig nested.config get nodes -l 'hypershift.openshift.io/nodePool=<node_pool_name>'
```
