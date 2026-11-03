# 17.1. Creating a performance profile

You can create a cluster performance profile by using the Performance Profile Creator (PPC) tool. The PPC is a function of the Node Tuning Operator. 

The PPC combines information about your cluster with user-supplied configurations to generate a performance profile that is appropriate to your hardware, topology and use-case. 

Note

Performance profiles are applicable only to bare-metal environments where the cluster has direct access to the underlying hardware resources. You can configure performances profiles for both single-node OpenShift and multi-node clusters. 

The following is a high-level workflow for creating and applying a performance profile in your cluster: 

  * Create a machine config pool (MCP) for nodes that you want to target with performance configurations. In single-node OpenShift clusters, you must use the `master` MCP because there is only one node in the cluster. 
  * Gather information about your cluster using the `must-gather` command. 
  * Use the PPC tool to create a performance profile by using either of the following methods: 

    * Run the PPC tool by using Podman as described in _Running the Performance Profile Creator using Podman_. . 
    * Run the PPC tool by using a wrapper script as described in _Running the Performance Profile Creator wrapper script_.. 

  * Configure the performance profile for your use case and apply the performance profile to your cluster. 



## 17.1.1. About the Performance Profile Creator

The Performance Profile Creator (PPC) is a command-line tool and is delivered with the Node Tuning Operator. You can use the PPC CLI to create a performance profile for your cluster. 

Initially, you can use the PPC tool to process the `must-gather` data to display key performance configurations for your cluster, including the following information: 

  * NUMA cell partitioning with the allocated CPU IDs 
  * Hyper-Threading node configuration 



You can use this information to help you configure the performance profile. 

Specify performance configuration arguments to the PPC tool to generate a proposed performance profile that is appropriate for your hardware, topology, and use-case. 

You can run the PPC by using one of the following methods: 

  * Run the PPC by using Podman 
  * Run the PPC by using the wrapper script 



Note

Using the wrapper script abstracts some of the more granular Podman tasks into an executable script. For example, the wrapper script handles tasks such as pulling and running the required container image, mounting directories into the container, and providing parameters directly to the container through Podman. Both methods achieve the same result. 

## 17.1.2. Create a machine config pool to target nodes for performance tuning

For multi-node clusters, you can define a machine config pool (MCP) to identify the target nodes that you want to configure with a performance profile. 

In single-node OpenShift clusters, you must use the `master` MCP because there is only one node in the cluster. You do not need to create a separate MCP for single-node OpenShift clusters. 

**Prerequisites**

  * You have `cluster-admin` role access. 
  * You installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Label the target nodes for configuration by running the following command: 

```shell-session
$ oc label node <node_name> node-role.kubernetes.io/worker-cnf=""
```


     * `<node_name>`: Specifies the name of your node. This example applies the `worker-cnf` label. 

  2. Create a `MachineConfigPool` resource containing the target nodes: 

     1. Create a YAML file that defines the `MachineConfigPool` resource: 

**Example`mcp-worker-cnf.yaml` file**

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: worker-cnf
  labels:
    machineconfiguration.openshift.io/role: worker-cnf
spec:
  machineConfigSelector:
    matchExpressions:
      - {
           key: machineconfiguration.openshift.io/role,
           operator: In,
           values: [worker, worker-cnf],
        }
  paused: false
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/worker-cnf: ""
```


where: 

`metadata.name`
     Specifies a name for the `MachineConfigPool` resource. 
`machineconfiguration.openshift.io/role`
     Specifes a unique label for the machine config pool. 
`node-role.kubernetes.io/worker-cnf`
     Specifies the nodes with the target label that you defined. 

     2. Apply the `MachineConfigPool` resource by running the following command: 

```shell-session
$ oc apply -f mcp-worker-cnf.yaml
```


**Example output**

```shell-session
machineconfigpool.machineconfiguration.openshift.io/worker-cnf created
```


**Verification**

  * Check the machine config pools in your cluster by running the following command: 

```shell-session
$ oc get mcp
```


**Example output**

```shell-session
NAME         CONFIG                                                 UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master       rendered-master-58433c7c3c1b4ed5ffef95234d451490       True      False      False      3              3                   3                     0                      6h46m
worker       rendered-worker-168f52b168f151e4f853259729b6azc4       True      False      False      2              2                   2                     0                      6h46m
worker-cnf   rendered-worker-cnf-168f52b168f151e4f853259729b6azc4   True      False      False      1              1                   1                     0                      73s
```


## 17.1.3. Gather data about your cluster for the PPC

The Performance Profile Creator (PPC) tool requires `must-gather` data. As a cluster administrator, run the `must-gather` command to capture information about your cluster. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 
  * You installed the OpenShift CLI (`oc`). 
  * You identified a target MCP that you want to configure with a performance profile. 



**Procedure**

  1. Navigate to the directory where you want to store the `must-gather` data. 
  2. Collect cluster information by running the following command: 

```shell-session
$ oc adm must-gather
```


The command creates a folder with the `must-gather` data in your local directory with a naming format similar to the following: `must-gather.local.1971646453781853027`. 

  3. Optional: Create a compressed file from the `must-gather` directory: 

```shell-session
$ tar cvaf must-gather.tar.gz <must_gather_folder>
```


     * `<must_gather_folder>`: Specifies the name of the `must-gather` data folder. 

Note

Compressed output is required if you are running the Performance Profile Creator wrapper script. 




**Additional resources**

  * [Gathering data about your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#nodes-nodes-managing)



## 17.1.4. Run the Performance Profile Creator using Podman

As a cluster administrator, you can use Podman with the Performance Profile Creator (PPC) to create a performance profile. 

For more information about the PPC arguments, see the section "Performance Profile Creator arguments". 

Important

The PPC uses the `must-gather` data from your cluster to create the performance profile. If you make any changes to your cluster, such as relabeling a node targeted for performance configuration, you must re-create the `must-gather` data before running PPC again. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 
  * A cluster installed on bare-metal hardware. 
  * You installed `podman` and the OpenShift CLI (`oc`). 
  * Access to the Node Tuning Operator image. 
  * You identified a machine config pool containing target nodes for configuration. 
  * You have access to the `must-gather` data for your cluster. 



**Procedure**

  1. Check the machine config pool by running the following command: 

```shell-session
$ oc get mcp
```


The following output lists the available machine config pools: 

```shell-session
NAME         CONFIG                                                 UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master       rendered-master-58433c8c3c0b4ed5feef95434d455490       True      False      False      3              3                   3                     0                      8h
worker       rendered-worker-668f56a164f151e4a853229729b6adc4       True      False      False      2              2                   2                     0                      8h
worker-cnf   rendered-worker-cnf-668f56a164f151e4a853229729b6adc4   True      False      False      1              1                   1                     0                      79m
```


  2. Use Podman to authenticate to `registry.redhat.io` by running the following command: 

```shell-session
$ podman login registry.redhat.io
```


```bash
Username: <user_name>
Password: <password>
```


  3. Optional: Display help for the PPC tool by running the following command: 

```shell-session
$ podman run --rm --entrypoint performance-profile-creator registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.22 -h
```


The following output shows the available flags and commands for the PPC tool: 

```shell-session
A tool that automates creation of Performance Profiles

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  help        Help about any command
  info        requires --must-gather-dir-path, ignores other arguments. [Valid values: log,json]

Usage:
  performance-profile-creator [flags]
  performance-profile-creator [command]

Flags:
      --disable-ht                        Disable Hyperthreading
      --enable-hardware-tuning            Enable setting maximum cpu frequencies
  -h, --help                              help for performance-profile-creator
      --mcp-name string                   MCP name corresponding to the target machines (required)
      --must-gather-dir-path string       Must gather directory path (default "must-gather")
      --offlined-cpu-count int            Number of offlined CPUs
      --per-pod-power-management          Enable Per Pod Power Management
      --power-consumption-mode string     The power consumption mode.  [Valid values: default, low-latency, ultra-low-latency] (default "default")
      --profile-name string               Name of the performance profile to be created (default "performance")
      --reserved-cpu-count int            Number of reserved CPUs (required)
      --rt-kernel                         Enable Real Time Kernel (required)
      --split-reserved-cpus-across-numa   Split the Reserved CPUs across NUMA nodes
      --topology-manager-policy string    Kubelet Topology Manager Policy of the performance profile to be created. [Valid values: single-numa-node, best-effort, restricted] (default "restricted")
      --user-level-networking             Run with User level Networking(DPDK) enabled

Use "performance-profile-creator [command] --help" for more information about a command.
```


  4. To display information about the cluster, run the PPC tool with the `info` command by running the following command: 

```shell-session
$ podman run --entrypoint performance-profile-creator -v <path_to_must_gather>:/must-gather:z registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.22 info --must-gather-dir-path /must-gather
```


     * `--entrypoint performance-profile-creator` defines the performance profile creator as a new entry point to `podman`. 
     * `-v <path_to_must_gather>` specifies the path to either of the following components: 

       * The directory containing the `must-gather` data. 
       * An existing directory containing the `must-gather` decompressed .tar file. 

The following output is generated from running the command: 

```shell-session
PPC: Nodes names targeted by master pool are:
PPC: Nodes names targeted by worker-cnf pool are: host2.example.com
PPC: Nodes names targeted by worker pool are: host.example.com host1.example.com
PPC: Cluster info:
MCP 'master' nodes:
---
MCP 'worker' nodes:
Node: host.example.com (NUMA cells: 1, HT: true)
NUMA cell 0 : [0 1 2 3]
CPU(s): 4
Node: host1.example.com (NUMA cells: 1, HT: true)
NUMA cell 0 : [0 1 2 3]
CPU(s): 4
---
MCP 'worker-cnf' nodes:
Node: host2.example.com (NUMA cells: 1, HT: true)
NUMA cell 0 : [0 1 2 3]
CPU(s): 4
---
```


  5. Create a performance profile by running the following command. The example uses sample PPC arguments and values: 

```shell-session
$ podman run --entrypoint performance-profile-creator -v <path_to_must_gather>:/must-gather:z registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.22 --mcp-name=worker-cnf --reserved-cpu-count=2 --rt-kernel=true --split-reserved-cpus-across-numa=false --must-gather-dir-path /must-gather --power-consumption-mode=ultra-low-latency > my-performance-profile.yaml
```


     * `-v <path_to_must_gather>` specifies the path to either of the following components: 

       * The directory containing the `must-gather` data. 
       * The directory containing the `must-gather` decompressed .tar file. 

     * `--mcp-name=worker-cnf` specifies the `worker-cnf` machine config pool. 
     * `--reserved-cpu-count=2` specifies two reserved CPUs. 
     * `--rt-kernel=true` enables the real-time kernel. 
     * `--split-reserved-cpus-across-numa=false` disables reserved CPUs splitting across NUMA nodes. 
     * `--power-consumption-mode=ultra-low-latency` specifies minimal latency at the cost of increased power consumption. 

Note

The `mcp-name` argument in this example is set to `worker-cnf` based on the output of the command `oc get mcp`. For single-node OpenShift use `--mcp-name=master`. 

The following output shows the CPU and NUMA allocation for the performance profile: 

```shell-session
PPC: Nodes targeted by worker-cnf MCP are: [worker-2]
PPC: NUMA cell(s): 1
PPC: NUMA cell 0 : [0 1 2 3]
PPC: CPU(s): 4
PPC: 2 reserved CPUs allocated: 0-1
PPC: 2 isolated CPUs allocated: 2-3
PPC: Additional Kernel Args based on configuration: []
```


  6. Review the created YAML file by running the following command: 

```shell-session
$ cat my-performance-profile.yaml
```


The following example shows the contents of the generated performance profile: 

```yaml
---
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: performance
spec:
  cpu:
    isolated: 2-3
    reserved: "0-1"
  machineConfigPoolSelector:
    machineconfiguration.openshift.io/role: worker-cnf
  net:
    userLevelNetworking: false
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  numa:
    topologyPolicy: restricted
  realTimeKernel:
    enabled: true
  workloadHints:
    highPowerConsumption: true
    perPodPowerManagement: false
    realTime: true
```


  7. Apply the generated profile: 

```shell-session
$ oc apply -f my-performance-profile.yaml
```


The following output confirms that the performance profile is created: 

```shell-session
performanceprofile.performance.openshift.io/performance created
```


## 17.1.5. Run the Performance Profile Creator wrapper script

The wrapper script simplifies the process of creating a performance profile with the Performance Profile Creator (PPC) tool. 

The script handles tasks such as pulling and running the required container image, mounting directories into the container, and providing parameters directly to the container through Podman. 

For more information about the Performance Profile Creator arguments, see the section "Performance Profile Creator arguments". 

Important

The PPC uses the `must-gather` data from your cluster to create the performance profile. If you make any changes to your cluster, such as relabeling a node targeted for performance configuration, you must re-create the `must-gather` data before running PPC again. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 
  * A cluster installed on bare-metal hardware. 
  * You installed `podman` and the OpenShift CLI (`oc`). 
  * Access to the Node Tuning Operator image. 
  * You identified a machine config pool containing target nodes for configuration. 
  * Access to the `must-gather` tarball. 



**Procedure**

  1. Create a file on your local machine named, for example, `run-perf-profile-creator.sh`: 

```shell-session
$ vi run-perf-profile-creator.sh
```


  2. Paste the following code into the file: 

```bash
#!/bin/bash

readonly CONTAINER_RUNTIME=${CONTAINER_RUNTIME:-podman}
readonly CURRENT_SCRIPT=$(basename "$0")
readonly CMD="${CONTAINER_RUNTIME} run --entrypoint performance-profile-creator"
readonly IMG_EXISTS_CMD="${CONTAINER_RUNTIME} image exists"
readonly IMG_PULL_CMD="${CONTAINER_RUNTIME} image pull"
readonly MUST_GATHER_VOL="/must-gather"

NTO_IMG="registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.22"
MG_TARBALL=""
DATA_DIR=""

usage() {
  print "Wrapper usage:"
  print "  ${CURRENT_SCRIPT} [-h] [-p image][-t path] -- [performance-profile-creator flags]"
  print ""
  print "Options:"
  print "   -h                 help for ${CURRENT_SCRIPT}"
  print "   -p                 Node Tuning Operator image"
  print "   -t                 path to a must-gather tarball"

  ${IMG_EXISTS_CMD} "${NTO_IMG}" && ${CMD} "${NTO_IMG}" -h
}

function cleanup {
  [ -d "${DATA_DIR}" ] && rm -rf "${DATA_DIR}"
}
trap cleanup EXIT

exit_error() {
  print "error: $*"
  usage
  exit 1
}

print() {
  echo  "$*" >&2
}

check_requirements() {
  ${IMG_EXISTS_CMD} "${NTO_IMG}" || ${IMG_PULL_CMD} "${NTO_IMG}" || \
      exit_error "Node Tuning Operator image not found"

  [ -n "${MG_TARBALL}" ] || exit_error "Must-gather tarball file path is mandatory"
  [ -f "${MG_TARBALL}" ] || exit_error "Must-gather tarball file not found"

  DATA_DIR=$(mktemp -d -t "${CURRENT_SCRIPT}XXXX") || exit_error "Cannot create the data directory"
  tar -zxf "${MG_TARBALL}" --directory "${DATA_DIR}" || exit_error "Cannot decompress the must-gather tarball"
  chmod a+rx "${DATA_DIR}"

  return 0
}

main() {
  while getopts ':hp:t:' OPT; do
    case "${OPT}" in
      h)
        usage
        exit 0
        ;;
      p)
        NTO_IMG="${OPTARG}"
        ;;
      t)
        MG_TARBALL="${OPTARG}"
        ;;
      ?)
        exit_error "invalid argument: ${OPTARG}"
        ;;
    esac
  done
  shift $((OPTIND - 1))

  check_requirements || exit 1

  ${CMD} -v "${DATA_DIR}:${MUST_GATHER_VOL}:z" "${NTO_IMG}" "$@" --must-gather-dir-path "${MUST_GATHER_VOL}"
  echo "" 1>&2
}

main "$@"
```


  3. Add execute permissions for everyone on this script: 

```shell-session
$ chmod a+x run-perf-profile-creator.sh
```


  4. Use Podman to authenticate to `registry.redhat.io` by running the following command: 

```shell-session
$ podman login registry.redhat.io
```


```bash
Username: <user_name>
Password: <password>
```


  5. Optional: Display help for the PPC tool by running the following command: 

```shell-session
$ ./run-perf-profile-creator.sh -h
```


```shell-session
Wrapper usage:
  run-perf-profile-creator.sh [-h] [-p image][-t path] -- [performance-profile-creator flags]

Options:
   -h                 help for run-perf-profile-creator.sh
   -p                 Node Tuning Operator image
   -t                 path to a must-gather tarball
A tool that automates creation of Performance Profiles

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  help        Help about any command
  info        requires --must-gather-dir-path, ignores other arguments. [Valid values: log,json]

Usage:
  performance-profile-creator [flags]
  performance-profile-creator [command]

Flags:
      --disable-ht                        Disable Hyperthreading
      --enable-hardware-tuning            Enable setting maximum cpu frequencies
  -h, --help                              help for performance-profile-creator
      --mcp-name string                   MCP name corresponding to the target machines (required)
      --must-gather-dir-path string       Must gather directory path (default "must-gather")
      --offlined-cpu-count int            Number of offlined CPUs
      --per-pod-power-management          Enable Per Pod Power Management
      --power-consumption-mode string     The power consumption mode.  [Valid values: default, low-latency, ultra-low-latency] (default "default")
      --profile-name string               Name of the performance profile to be created (default "performance")
      --reserved-cpu-count int            Number of reserved CPUs (required)
      --rt-kernel                         Enable Real Time Kernel (required)
      --split-reserved-cpus-across-numa   Split the Reserved CPUs across NUMA nodes
      --topology-manager-policy string    Kubelet Topology Manager Policy of the performance profile to be created. [Valid values: single-numa-node, best-effort, restricted] (default "restricted")
      --user-level-networking             Run with User level Networking(DPDK) enabled

Use "performance-profile-creator [command] --help" for more information about a command.
```


Note

You can optionally set a path for the Node Tuning Operator image using the `-p` option. If you do not set a path, the wrapper script uses the default image: `registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.22`. 

  6. To display information about the cluster, run the PPC tool with the `info` command by running the following command: 

```shell-session
$ ./run-perf-profile-creator.sh -t /<path_to_must_gather_dir>/must-gather.tar.gz -- info
```


     * `-t /<path_to_must_gather_dir>/must-gather.tar.gz`: Specifies the path to directory containing the must-gather tarball. This is a required argument for the wrapper script. 

The following example shows the cluster information output: 

```shell-session
PPC: Cluster info:
MCP 'master' nodes:
---
MCP 'worker' nodes:
Node: host.example.com (NUMA cells: 1, HT: true)
NUMA cell 0 : [0 1 2 3]
CPU(s): 4
Node: host1.example.com (NUMA cells: 1, HT: true)
NUMA cell 0 : [0 1 2 3]
CPU(s): 4
---
MCP 'worker-cnf' nodes:
Node: host2.example.com (NUMA cells: 1, HT: true)
NUMA cell 0 : [0 1 2 3]
CPU(s): 4
---
```


  7. Create a performance profile by running the following command. The example command uses sample PPC arguments and values. 

```shell-session
$ ./run-perf-profile-creator.sh -t /path-to-must-gather/must-gather.tar.gz -- --mcp-name=worker-cnf --reserved-cpu-count=2 --rt-kernel=true --split-reserved-cpus-across-numa=false --power-consumption-mode=ultra-low-latency > my-performance-profile.yaml
```


     * `--mcp-name=worker-cnf` specifies the `worker-cnf` machine config pool. 
     * `--reserved-cpu-count=2` specifies two reserved CPUs. 
     * `--rt-kernel=true` enables the real-time kernel. 
     * `--split-reserved-cpus-across-numa=false` disables reserved CPUs splitting across NUMA nodes. 
     * `--power-consumption-mode=ultra-low-latency` specifies minimal latency at the cost of increased power consumption. 

Note

The `mcp-name` argument in this example is set to `worker-cnf` based on the output of the command `oc get mcp`. For single-node OpenShift use `--mcp-name=master`. 

  8. Review the created YAML file by running the following command: 

```shell-session
$ cat my-performance-profile.yaml
```


The generated YAML file should contain the following output: 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: performance
spec:
  cpu:
    isolated: 2-3
    reserved: "0-1"
  machineConfigPoolSelector:
    machineconfiguration.openshift.io/role: worker-cnf
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  numa:
    topologyPolicy: restricted
  realTimeKernel:
    enabled: true
  workloadHints:
    highPowerConsumption: true
    perPodPowerManagement: false
    realTime: true
```


  9. Apply the generated profile: 

```shell-session
$ oc apply -f my-performance-profile.yaml
```


The performance profile is successfully applied and created as shown in the following output: 

```shell-session
performanceprofile.performance.openshift.io/performance created
```


## 17.1.6. Performance Profile Creator arguments

To customize the generation of performance profiles, review the arguments for the Performance Profile Creator. 

Table 17.1. Required Performance Profile Creator argumentsArgument| Description  
---|---  
`mcp-name` |  Name for MCP; for example, `worker-cnf` corresponding to the target machines.   
`must-gather-dir-path` |  The path of the must gather directory.  This argument is only required if you run the PPC tool by using Podman. If you use the PPC with the wrapper script, do not use this argument. Instead, specify the directory path to the `must-gather` tarball by using the `-t` option for the wrapper script.   
`reserved-cpu-count` |  Number of reserved CPUs. Use a natural number greater than zero.   
`rt-kernel` |  Enables real-time kernel.  Possible values: `true` or `false`.   
Show more

Table 17.2. Optional Performance Profile Creator argumentsArgument| Description  
---|---  
`disable-ht` |  Disable Hyper-Threading.  Possible values: `true` or `false`.  Default: `false`.  Warning If this argument is set to `true` you should not disable Hyper-Threading in the BIOS. Disabling Hyper-Threading is accomplished with a kernel command-line argument.   
enable-hardware-tuning  |  Enable the setting of maximum CPU frequencies.  To enable this feature, set the maximum frequency for applications running on isolated and reserved CPUs for both of the following fields: 

  * `spec.hardwareTuning.isolatedCpuFreq`
  * `spec.hardwareTuning.reservedCpuFreq`

This is an advanced feature. If you configure hardware tuning, the generated `PerformanceProfile` includes warnings and guidance on how to set frequency settings.   
`info` |  This captures cluster information. This argument also requires the `must-gather-dir-path` argument. If any other arguments are set they are ignored.  Possible values: 

  * `log`
  * `JSON`

Default: `log`.   
`offlined-cpu-count` |  Number of offlined CPUs.  Note Use a natural number greater than zero. If not enough logical processors are offlined, then error messages are logged. The messages are: `Error: failed to compute the reserved and isolated CPUs: please ensure that reserved-cpu-count plus offlined-cpu-count should be in the range [0,1]``Error: failed to compute the reserved and isolated CPUs: please specify the offlined CPU count in the range [0,1]`  
`power-consumption-mode` |  The power consumption mode.  Possible values: 

  * `default`: Performance achieved through CPU partitioning only. 
  * `low-latency`: Enhanced measures to improve latency. 
  * `ultra-low-latency`: Priority given to optimal latency, at the expense of power management. 

Default: `default`.   
`per-pod-power-management` |  Enable per pod power management. You cannot use this argument if you configured `ultra-low-latency` as the power consumption mode.  Possible values: `true` or `false`.  Default: `false`.   
`profile-name` |  Name of the performance profile to create.  Default: `performance`.   
`split-reserved-cpus-across-numa` |  Split the reserved CPUs across NUMA nodes.  Possible values: `true` or `false`.  Default: `false`.   
`topology-manager-policy` |  Kubelet Topology Manager policy of the performance profile to be created.  Possible values: 

  * `single-numa-node`
  * `best-effort`
  * `restricted`

Default: `restricted`.   
`user-level-networking` |  Run with user level networking (DPDK) enabled.  Possible values: `true` or `false`.  Default: `false`.   
Show more
