# 23.1. Enable workload partitioning

To partition cluster management pods into a specified CPU affinity, enable workload partitioning. This configuration ensures that management pods operate within the reserved CPU limits defined in your Performance Profile. 

Consider additional post-installation Operators that use workload partitioning when calculating how many reserved CPU cores to set aside for the platform. 

Workload partitioning isolates user workloads from platform workloads using standard Kubernetes scheduling capabilities. 

Note

You can enable workload partitioning only during cluster installation. You cannot disable workload partitioning post-installation. However, you can change the CPU configuration for `reserved` and `isolated` CPUs post-installation. 

The procedure demonstrates enabling workload partitioning cluster-wide. 

**Procedure**

  * In the `install-config.yaml` file, add the additional field `cpuPartitioningMode` and set it to `AllNodes`. 

```yaml
apiVersion: v1
baseDomain: devcluster.openshift.com
cpuPartitioningMode: AllNodes
compute:
  - architecture: amd64
    hyperthreading: Enabled
    name: worker
    platform: {}
    replicas: 3
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform: {}
  replicas: 3
```


    * `cpuPartitioningMode`: Specifies the cluster to set up for CPU partitioning at install time. The default value is `None`, which ensures that no CPU partitioning is enabled at install time.
