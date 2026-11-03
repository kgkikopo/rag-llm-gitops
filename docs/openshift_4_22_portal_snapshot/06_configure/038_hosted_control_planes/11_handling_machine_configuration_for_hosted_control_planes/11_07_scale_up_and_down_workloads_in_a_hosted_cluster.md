# 11.7. Scale up and down workloads in a hosted cluster

To scale up and down the workloads in your hosted cluster, you can use the `ScaleUpAndScaleDown` behavior. The compute nodes scale up when you add workloads and scale down when you delete workloads. 

**Prerequisites**

  * You have created the `HostedCluster` and `NodePool` resources. 



**Procedure**

  1. Enable cluster autoscaling for your hosted cluster by setting the scaling behavior to `ScaleUpAndScaleDown`. Run the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  hostedcluster <hosted_cluster_name> \
  --type=merge \
  --patch='{"spec": {"autoscaling": {"scaling": "ScaleUpAndScaleDown", "maxPodGracePeriod": 60, "scaleDown": {"utilizationThresholdPercent": 50}}}}'
```


  2. Remove the `spec.replicas` field from the `NodePool` resource to allow cluster autoscaler to manage the node count. Run the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  nodepool <node_pool_name> \
  --type=json  \
  --patch='[{"op": "remove", "path": "/spec/replicas"}]'
```


  3. Enable cluster autoscaling to configure the minimum and maximum node counts for your node pools. Run the following command: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  nodepool <nodepool_name> \
  --type=merge --patch='{"spec": {"autoScaling": {"max": 3, "min": 1}}}'
```


**Verification**

  * To verify that all compute nodes are in the `Ready` status, run the following command: 

```shell-session
$ oc --kubeconfig <hosted_cluster_name>.kubeconfig get nodes
```


**Additional resources**

  * [Scaling the NodePool object for a hosted cluster (bare-metal platforms)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/managing-hosted-control-planes#hcp-bm-scale-np_hcp-manage-bm "5.2.2. Scaling the NodePool object for a hosted cluster")
  * [Scaling the NodePool object for a hosted cluster (non-bare metal agent machines)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/managing-hosted-control-planes#hcp-bm-scale-np_hcp-manage-non-bm "5.4.2. Scaling the NodePool object for a hosted cluster")
  * [Scaling a node pool (OpenShift Virtualization)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/hosted_control_planes/deploying-hosted-control-planes#hcp-virt-scale-nodpool_hcp-deploy-virt "4.4.9. Scaling a node pool")
