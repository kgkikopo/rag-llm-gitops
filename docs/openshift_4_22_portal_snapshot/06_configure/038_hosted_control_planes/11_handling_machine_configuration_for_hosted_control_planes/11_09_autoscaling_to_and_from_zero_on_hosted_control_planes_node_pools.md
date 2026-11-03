# 11.9. Autoscaling to and from zero on hosted control planes node pools

You can configure hosted control planes node pools to autoscale down to zero compute nodes when no schedulable workloads remain on the pool and to provision nodes on-demand when pending pods require capacity. 

This capability reduces idle compute costs for variable workloads while the hosted control plane stays available. 

Note

Scale-from-zero autoscaling is available on OpenShift Container Platform 4.18 and later for eligible hosted control planes deployments on Amazon Web Services (AWS) and Azure. Platform validation and HyperShift Operator configuration determine whether a node pool can use `spec.autoScaling.min: 0`. 

When you enable autoscaling on a `NodePool` object, you set `spec.autoScaling.min` to `0` and omit `spec.replicas`. The cluster autoscaler then manages pool size instead of a fixed replica count. 

The cluster autoscaler scales up from zero differently than it scales pools that already have nodes. When a pool has zero nodes, the autoscaler cannot observe utilization on existing compute nodes. Instead, it uses instance-type metadata from the cloud provider (CPU, memory, and GPU capacity for the `NodePool` platform configuration) to decide how many nodes to provision for pending pods. 

This behavior contrasts with classic fixed-minimum autoscaling, where `spec.autoScaling.min` is at least `1`. With a minimum of one or more replicas, the pool always retains at least one node even when workloads are idle. 

The hosted control plane remains operational when compute node pools scale to zero. Control plane pods continue running on the management cluster. Workloads that target a scale-to-zero pool remain unschedulable until the autoscaler provisions new nodes. 

## 11.9.1. Terminology

`AutoscalingEnabled` condition
     A `NodePool` status condition that reports whether autoscaling is correctly configured and active on the pool. Verify that this condition is `True` after you enable autoscaling. 
minimum replicas
     The `spec.autoScaling.min` value on a `NodePool` object. When autoscaling is enabled, this value is the lowest number of nodes the autoscaler can scale the pool to. 
non-tainted pools
     Node pools without taints that can accept system and user workloads. These pools must keep baseline capacity for highly available platform Operators. 
scale-from-zero
     Provisioning the first node in a pool that currently has zero nodes because pending pods require capacity. 
scale-to-zero
     Reducing a pool to zero nodes when no schedulable workloads remain on that pool and autoscaling minimum is `0`. 
tainted pools
     Node pools with taints that restrict which pods can schedule on them. Tainted workload pools are typical candidates for `spec.autoScaling.min: 0`. 

## 11.9.2. Use cases for scale-to-zero autoscaling

Scale-to-zero autoscaling is appropriate for the following scenarios: 

  * Development and test node pools that are idle outside business hours 
  * Batch or burst workload pools that run jobs periodically 
  * GPU or specialized instance pools that are expensive when idle 
  * Tainted workload pools that isolate optional capacity from system workloads 



In each case, keep separate baseline pools for platform Operators and confine scale-to-zero configuration to pools that tolerate cold-start latency. 

Do not use scale-to-zero autoscaling in the following scenarios: 

  * Do not configure scale-to-zero on pools that must always accept system or highly available platform workloads. 
  * Scaling all non-tainted node pools to zero violates the cluster-level minimum replica constraint and can prevent system pods from scheduling. 
  * Do not use scale-to-zero as a substitute for full cluster hibernation. 
  * Data-plane node pool autoscaling removes compute nodes only; the hosted control plane and management infrastructure remain active. 



## 11.9.3. Best practices for scale-to-zero autoscaling

Base and burst pool architecture
    

Keep at least two non-tainted compute nodes across baseline pools for highly available platform Operators. Confine `spec.autoScaling.min: 0` to tainted burst pools that run dev, test, batch, or specialized workloads. 

Do not scale all non-tainted pools to zero. Use taints and tolerations to isolate burst capacity from system scheduling requirements. 

Platform and version eligibility
     Configure scale-to-zero only on AWS or Azure hosted clusters running OpenShift Container Platform 4.18 or later with a HyperShift Operator release that includes the backport. 
Drain timeout tuning
    

Set `nodeDrainTimeout` and `nodeVolumeDetachTimeout` to positive values when workloads use persistent storage or long termination grace periods. Zero values block drain and detach operations and can leave nodes stuck during scale-down. 

Tune timeouts for cost-optimization patterns such as nightly scale-down of dev pools. 

Scale-up latency planning
    

Expect cold-start delay when pools scale from zero. Nodes must provision, join the cluster, and pull images before pending pods schedule. 

Plan batch jobs and interactive workloads to tolerate this latency, or keep a small nonzero minimum on latency-sensitive pools. 

Distinguish autoscaling from hibernation
     Data-plane node pool autoscaling removes compute nodes only. The hosted control plane remains active on the management cluster. Full cluster hibernation is a separate operational pattern. 
Cluster-level minimum replica constraint
    

The sum of `spec.autoScaling.min` (or fixed `spec.replicas` when autoscaling is disabled) across all non-tainted node pools must be at least `2`. 

This constraint ensures highly available platform Operators, such as ingress, console, monitoring, and image registry, can schedule second replicas that require anti-affinity across compute nodes. 

Tainted workload pools might use `spec.autoScaling.min: 0` because taints prevent system pods from scheduling on those nodes. Baseline non-tainted pools must retain enough minimum capacity to satisfy the cluster-wide constraint. 

## 11.9.4. Configure autoscaling to and from zero on hosted control planes node pools

Configure a `NodePool` object to autoscale between zero and a maximum replica count on supported Amazon Web Services (AWS) or Azure hosted clusters. After configuration, verify the `AutoscalingEnabled` condition and validate scale-down and scale-up behavior. 

**Prerequisites**

  * A hosted cluster on AWS or Azure running OpenShift Container Platform 4.18 or later 
  * Permission to edit `NodePool` objects in the hosted cluster namespace 
  * Understanding of scale-to-zero use cases, platform support, and Operator implications 
  * For AWS and Azure, scale-from-zero provider credentials 



**Procedure**

  1. Confirm that your hosted cluster platform supports `spec.autoScaling.min: 0`. 

On AWS and Azure, the `NodePool` API accepts `min: 0`. On other platforms, `min` must be at least `1`. 

  2. Confirm that the HyperShift Operator enables scale-from-zero. 

On AWS and Azure, confirm that `--scale-from-zero-provider` and `--scale-from-zero-creds` are configured so instance-type metadata is available. 

  3. Enable autoscaling on the target `NodePool` object by removing fixed replicas and setting autoscaling bounds. 

Replace `<hosted_cluster_namespace>`, `<nodepool_name>`, and `<max_replicas>` with your values. 

```shell-session
$ oc -n <hosted_cluster_namespace> patch nodepool <nodepool_name> \
  --type=json \
  -p '[{"op": "remove", "path": "/spec/replicas"}, \
       {"op": "add", "path": "/spec/autoScaling", \
        "value": {"min": 0, "max": <max_replicas>}}]'
```


Note

`spec.replicas` and `spec.autoScaling` are mutually exclusive. When autoscaling is enabled, omit `spec.replicas` so the cluster autoscaler manages pool size. 

  4. Optional: Configure hosted cluster-level autoscaling behavior on the `HostedCluster` resource. 

For example, set scaling behavior to `ScaleUpAndScaleDown`: 

```shell-session
$ oc patch -n <hosted_cluster_namespace> \
  hostedcluster <hosted_cluster_name> \
  --type=merge \
  --patch='{"spec": {"autoscaling": {"scaling": "ScaleUpAndScaleDown"}}}'
```


Hosted cluster autoscaling settings apply cluster-wide autoscaler behavior. Node pool autoscaling bounds are configured on each `NodePool` object. 

  5. Verify that the `AutoscalingEnabled` condition on the `NodePool` is `True`. 

```shell-session
$ oc get nodepool -n <hosted_cluster_namespace> <nodepool_name> \
  -o jsonpath='{range .status.conditions[*]}\
{.type}={.status}{"\n"}{end}'
```


The output must include `AutoscalingEnabled=True`. 

  6. Verify scale-down to zero by removing schedulable workloads from the pool. 

Remove or reschedule deployments, jobs, or other workloads that schedule on the target pool. If the pool uses taints, only workloads with matching tolerations count toward pool utilization. 

Wait for the cluster autoscaler to scale the pool down. When no schedulable workloads remain, the pool can reach zero nodes if `spec.autoScaling.min` is `0`. 

  7. Verify scale-up from zero by deploying a workload that creates pending pods on the pool. 

For example, create a deployment with resource requests that exceed available capacity: 

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: scale-from-zero-test
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      app: scale-from-zero-test
  template:
    metadata:
      labels:
        app: scale-from-zero-test
    spec:
      tolerations:
      - key: "<taint_key>"
        operator: "Equal"
        value: "<taint_value>"
        effect: "NoSchedule"
      containers:
      - name: app
        image: registry.redhat.io/ubi9/ubi-minimal
        resources:
          requests:
            cpu: "1"
            memory: 1Gi
```


Apply the manifest and wait for the cluster autoscaler to provision nodes from zero. 

  8. Extract the hosted cluster kubeconfig and verify node count changes. 

```shell-session
$ oc extract -n <hosted_cluster_namespace> \
  secret/<hosted_cluster_name>-admin-kubeconfig \
  --to=./hostedcluster-secrets --confirm
```


```shell-session
$ oc --kubeconfig ./hostedcluster-secrets/kubeconfig get nodes
```


**Verification**

  * The `AutoscalingEnabled` condition on the `NodePool` is `True`. 
  * After workloads are removed, the pool scales down and `CURRENT NODES` can reach `0` when `min` is `0`. 
  * After pending pods are created, new nodes appear and reach `Ready` status. 



Note

When pools are at zero nodes, platform Operators on non-tainted baseline pools can report degraded status if minimum replica constraints are not satisfied. 

## 11.9.5. NodePool autoscaling configuration reference

Get familiar with the `NodePool` fields and status conditions for autoscaling to and from zero on hosted control planes. 

Field or condition| Description  
---|---  
`spec.autoScaling.min` |  Minimum nodes the cluster autoscaler can scale the pool to. Valid values include `0` on Amazon Web Services (AWS) and Azure. On other platforms, the minimum must be at least `1`.   
`spec.autoScaling.max` |  Maximum nodes the cluster autoscaler can scale the pool to. Must be greater than or equal to `spec.autoScaling.min`.   
`spec.replicas` |  Fixed replica count when autoscaling is disabled. Must be omitted when `spec.autoScaling` is configured.   
`AutoscalingEnabled` condition  |  Reports whether autoscaling is active on the `NodePool`. Status `True` indicates the autoscaler manages pool size.   
`--scale-from-zero-provider` and `--scale-from-zero-creds` |  On AWS and Azure, credentials and provider configuration for instance-type metadata used during scale-from-zero.   
Non-tainted pool minimum sum  |  Sum of minimum replicas across non-tainted pools must be at least `2` cluster-wide for HA platform operators.   
Show more

Note

`spec.replicas` and `spec.autoScaling` are mutually exclusive. Patch or edit the `NodePool` to remove `spec.replicas` before adding `spec.autoScaling`. 

## 11.9.6. NodePool API reference for autoscaling

Get familiar with the `NodePool` specification fields related to autoscaling, including scaling to and from zero on supported platforms. 

### 11.9.6.1. spec.autoScaling

Field| Type| Description  
---|---|---  
`min` |  integer  |  Minimum number of nodes for the pool when autoscaling is enabled. `0` is valid on Amazon Web Services (AWS) and Azure. Other platforms require `min` to be at least `1`.   
`max` |  integer  |  Maximum number of nodes the cluster autoscaler can add to the pool.   
Show more

### 11.9.6.2. spec.replicas

Field| Type| Description  
---|---|---  
`replicas` |  integer  |  Fixed number of nodes when autoscaling is disabled. Omit this field when `spec.autoScaling` is set.   
Show more

### 11.9.6.3. Drain and detach timeouts

Field| Type| Description  
---|---|---  
`nodeDrainTimeout` |  duration  |  Time the controller spends draining a node during scale-down. A value of `0s` blocks draining until a positive timeout is set.   
`nodeVolumeDetachTimeout` |  duration  |  Time the controller spends detaching volumes from a node during scale-down. A value of `0` blocks detachment until a positive timeout is set.   
Show more

### 11.9.6.4. status.conditions

Condition| Description  
---|---  
`AutoscalingEnabled` |  Reports `True` when autoscaling is correctly configured and the autoscaler manages the pool.   
Show more

### 11.9.6.5. HyperShift Operator flags

Flag| Description  
---|---  
`--scale-from-zero-provider` |  Provider used to fetch instance-type metadata on AWS and Azure.   
`--scale-from-zero-creds` |  Credentials for the scale-from-zero provider on AWS and Azure.   
Show more
