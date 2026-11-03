# 5.4. Huge pages

Understand and configure huge pages to optimize memory mapping efficiency on cluster nodes. 

## 5.4.1. What huge pages do

To optimize memory mapping efficiency, understand the function of huge pages. Unlike standard 4Ki blocks, huge pages are larger memory segments that reduce the tracking load on the translation lookaside buffer (TLB) hardware cache. 

Memory is managed in blocks known as pages. On most systems, a page is 4Ki; 1Mi of memory is equal to 256 pages; 1Gi of memory is 256,000 pages, and so on. CPUs have a built-in memory management unit that manages a list of these pages in hardware. The translation lookaside buffer (TLB) is a small hardware cache of virtual-to-physical page mappings. If the virtual address passed in a hardware instruction can be found in the TLB, the mapping can be determined quickly. If not, a TLB miss occurs, and the system falls back to slower, software-based address translation, resulting in performance issues. Since the size of the TLB is fixed, the only way to reduce the chance of a TLB miss is to increase the page size. 

A huge page is a memory page that is larger than 4Ki. On x86_64 architectures, there are two common huge page sizes: 2Mi and 1Gi. Sizes vary on other architectures. To use huge pages, code must be written so that applications are aware of them. Transparent huge pages (THP) attempt to automate the management of huge pages without application knowledge, but they have limitations. In particular, they are limited to 2Mi page sizes. THP can lead to performance degradation on nodes with high memory utilization or fragmentation because of defragmenting efforts of THP, which can lock memory pages. For this reason, some applications might be designed to or recommend usage of pre-allocated huge pages instead of THP. 

## 5.4.2. How huge pages are consumed by apps

You must ensure that nodes pre-allocate huge pages in order for the node to report its huge page capacity. A node can only pre-allocate huge pages for a single size. 

Huge pages can be consumed through container-level resource requirements by using the resource name `hugepages-<size>`, where size is the most compact binary notation by using integer values supported on a particular node. For example, if a node supports 2048 KiB page sizes, the node exposes a schedulable resource `hugepages-2Mi`. Unlike CPU or memory, huge pages do not support over-commitment. 

```yaml
apiVersion: v1
kind: Pod
metadata:
  generateName: hugepages-volume-
spec:
  containers:
  - securityContext:
      privileged: true
    image: rhel7:latest
    command:
    - sleep
    - inf
    name: example
    volumeMounts:
    - mountPath: /dev/hugepages
      name: hugepage
    resources:
      limits:
        hugepages-2Mi: 100Mi
        memory: "1Gi"
        cpu: "1"
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
```


  * `spec.containers.resources.limits.hugepages-2Mi`: Specifies the amount of memory for `hugepages` as the exact amount to be allocated. 

Important

Do not specify this value as the amount of memory for `hugepages` multiplied by the size of the page. For example, given a huge page size of 2 MB, if you want to use 100 MB of huge-page-backed RAM for your application, then you would allocate 50 huge pages. OpenShift Container Platform handles the math for you. As in the above example, you can specify `100MB` directly. 




### 5.4.2.1. Allocating huge pages of a specific size

Some platforms support multiple huge page sizes. To allocate huge pages of a specific size, precede the huge pages boot command parameters with a huge page size selection parameter `hugepagesz=<size>`. The `<size>` value must be specified in bytes with an optional scale suffix [`kKmMgG`]. The default huge page size can be defined with the `default_hugepagesz=<size>` boot parameter. 

### 5.4.2.2. Huge page requirements

  * Huge page requests must equal the limits. This is the default if limits are specified, but requests are not. 
  * Huge pages are isolated at a pod scope. Container isolation is planned in a future iteration. 
  * `EmptyDir` volumes backed by huge pages must not consume more huge page memory than the pod request. 
  * Applications that consume huge pages via `shmget()` with `SHM_HUGETLB` must run with a supplemental group that matches **_proc/sys/vm/hugetlb_shm_group_**. 



## 5.4.3. Configure huge pages at boot time

To ensure nodes in your OpenShift Container Platform cluster pre-allocate memory for specific workloads, reserve huge pages at boot time. 

There are two ways of reserving huge pages: at boot time and at run time. Reserving at boot time increases the possibility of success because the memory has not yet been significantly fragmented. The Node Tuning Operator currently supports boot-time allocation of huge pages on specific nodes. 

Note

The TuneD boot-loader plugin only supports Red Hat Enterprise Linux CoreOS (RHCOS) compute nodes. 

**Procedure**

  1. Label all nodes that need the same huge pages setting by a label by entering the following command: 

```shell-session
$ oc label node <node_using_hugepages> node-role.kubernetes.io/worker-hp=
```


  2. Create a file with the following content and name it `hugepages-tuned-boottime.yaml`: 

```yaml
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
  - machineConfigLabels:
      machineconfiguration.openshift.io/role: "worker-hp"
    priority: 30
    profile: openshift-node-hugepages
# ...
```


where: 

`metadata.name`
     Specifies the `name` of the Tuned resource to `hugepages`. 
`spec.profile`
     Specifies the `profile` section to allocate huge pages. 
`spec.profile.data`
     Specifies the order of parameters. The order is important as some platforms support huge pages of various sizes. 
`spec.recommend.machineConfigLabels`
     Specifies the enablement of a machine config pool based matching. 

  3. Create the Tuned `hugepages` object by entering the following command: 

```shell-session
$ oc create -f hugepages-tuned-boottime.yaml
```


  4. Create a file with the following content and name it `hugepages-mcp.yaml`: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: worker-hp
  labels:
    worker-hp: ""
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,worker-hp]}
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/worker-hp: ""
```


  5. Create the machine config pool by entering the following command: 

```shell-session
$ oc create -f hugepages-mcp.yaml
```


**Verification**

  * To check that enough non-fragmented memory exists and that all the nodes in the `worker-hp` machine config pool now have 50 2Mi huge pages allocated, enter the following command: 

```shell-session
$ oc get node <node_using_hugepages> -o jsonpath="{.status.allocatable.hugepages-2Mi}"
100Mi
```
