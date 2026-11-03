# 17.12. Configuring memory page sizes

By configuring memory page sizes, system administrators can implement more efficient memory management on a specific node to suit workload requirements. The Node Tuning Operator provides a method for configuring huge pages and kernel page sizes by using a performance profile. 

## 17.12.1. Configure kernel page sizes

Use the `kernelPageSize` specification in a performance profile to configure the kernel page size on a specific node. Specify larger kernel page sizes for memory-intensive, high-performance workloads. 

Note

For nodes with an x86_64 or AMD64 architecture, you can only specify `4k` for the `kernelPageSize` specification. For nodes with an AArch64 architecture, you can specify `4k` or `64k` for the `kernelPageSize` specification. You must disable the realtime kernel before you can use the `64k` option. The default value is `4k`. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 
  * Install the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a performance profile to target nodes where you want to configure the kernel page size by creating a YAML file that defines the `PerformanceProfile` resource: 

**Example`pp-kernel-pages.yaml` file**

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
    name: example-performance-profile
#...
spec:
    kernelPageSize: "64k"
    realTimeKernel:
        enabled: false
    nodeSelector:
        node-role.kubernetes.io/worker: ""
```


where: 

`spec.kernelPageSize`
     Specifies a kernel page size of `64k`. You can only specify `64k` for nodes with an AArch64 architecture. The default value is `4k`. 
`spec.realTimeKernel.enabled:false`
     Specifies whether to disable the realtime kernel. A setting of `false` disables the kernel. You must disable the realtime kernel to use the `64k` kernel page size option. 
`spec.nodeSelector.node-role.kubernetes.io/worker`
     Specifies targets nodes with the `worker` role. 

  2. Apply the performance profile to the cluster: 

```bash
$ oc create -f pp-kernel-pages.yaml
```


**Example output**

```plaintext
performanceprofile.performance.openshift.io/example-performance-profile created
```


**Verification**

  1. Start a debug session on the node where you applied the performance profile by running the following command: 

```bash
$ oc debug node/<node_name>
```


     * `<node_name>`: Replace `<node_name>` with the name of the node with the performance profile applied. 

  2. Verify that the kernel page size is set to the value you specified in the performance profile by running the following command: 

```bash
$ getconf PAGESIZE
```


**Example output**

```plaintext
65536
```


## 17.12.2. Configure huge pages

Because nodes must pre-allocate huge pages used in an OpenShift Container Platform cluster, use the Node Tuning Operator to allocate huge pages on a specific node. 

OpenShift Container Platform provides a method for creating and allocating huge pages. Node Tuning Operator provides an easier method for doing this using the performance profile. 

**Procedure**

  * In the `hugepages.pages` section of the performance profile, specify multiple blocks of `size`, `count`, and, optionally, `node`: 

**Example configuration**

```yaml
hugepages:
   defaultHugepagesSize: "1G"
   pages:
   - size:  "1G"
     count:  4
     node:  0
# ...
```


where: 

`hugepages.pages.node`
    

Specifies the `node` that is the NUMA node in which the huge pages are allocated. If you omit `node`, the pages are evenly spread across all NUMA nodes. 

Note

Wait for the relevant machine config pool status that indicates the update is finished. 

These are the only configuration steps you need to do to allocate huge pages. 




**Verification**

  * To verify the configuration, see the `/proc/meminfo` file on the node: 

```shell-session
$ oc debug node/ip-10-0-141-105.ec2.internal
```


```shell-session
# grep -i huge /proc/meminfo
```


**Example output**

```shell-session
AnonHugePages:    ###### ##
ShmemHugePages:        0 kB
HugePages_Total:       2
HugePages_Free:        2
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       #### ##
Hugetlb:            #### ##
```


  * Use `oc describe` to report the new size: 

```shell-session
$ oc describe node worker-0.ocp4poc.example.com | grep -i huge
```


**Example output**

```shell-session
                                   hugepages-1g=true
 hugepages-###:  ###
 hugepages-###:  ###
```


## 17.12.3. Allocate multiple huge page sizes

You can request huge pages with different sizes under the same container. By doing this task, you can define more complicated pods consisting of containers with different huge page size needs. 

The following example, shows you how to define sizes `1G` and `2M`. The Node Tuning Operator configures both sizes on the node. 

**Procedure**

  * Edit the `PerformanceProfile` object to define `1G` and `2M` sizes for the huge pages. The Node Tuning Operator configures both sizes on the node. 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
    name: example-performance-profile
#...
spec:
  hugepages:
    defaultHugepagesSize: 1G
    pages:
    - count: 1024
      node: 0
      size: 2M
    - count: 4
      node: 1
      size: 1G
# ...
```
