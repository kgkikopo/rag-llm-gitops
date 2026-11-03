# 3.10. Use the NFD Topology Updater

Enable the NFD Topology Updater to detect allocated resources on worker nodes and report per-zone resource availability. This information helps the scheduler make topology-aware placement decisions for workloads that require specific NUMA node configurations. 

The NFD Topology Updater runs as a daemon on each worker node, examining the allocated resources and creating per-zone resource availability information. It communicates with nfd-master to create or update `NodeResourceTopology` custom resources with the resource topology of each zone, such as NUMA nodes. 

**Procedure**

  * To enable the Topology Updater workers in NFD, set the `topologyupdater` variable to `true` in the `NodeFeatureDiscovery` CR, as described in the section **Using the Node Feature Discovery Operator**. 



**Verification**

When run with NFD Topology Updater, NFD creates `NodeResourceTopology` custom resource instances corresponding to the node resource hardware topology, such as: 

```yaml
apiVersion: topology.node.k8s.io/v1alpha1
kind: NodeResourceTopology
metadata:
  name: node1
topologyPolicies: ["SingleNUMANodeContainerLevel"]
zones:
  - name: node-0
    type: Node
    resources:
      - name: cpu
        capacity: 20
        allocatable: 16
        available: 10
      - name: vendor/nic1
        capacity: 3
        allocatable: 3
        available: 3
  - name: node-1
    type: Node
    resources:
      - name: cpu
        capacity: 30
        allocatable: 30
        available: 15
      - name: vendor/nic2
        capacity: 6
        allocatable: 6
        available: 6
  - name: node-2
    type: Node
    resources:
      - name: cpu
        capacity: 30
        allocatable: 30
        available: 15
      - name: vendor/nic1
        capacity: 3
        allocatable: 3
        available: 3
```


## 3.10.1. NFD Topology Updater command-line flags

You can use the NFD Topology Updater command-line flags to control TLS authentication, resource detection intervals, and connection settings for communicating node resource topology to nfd-master. 

To view available flags, run the `nfd-topology-updater -help` command. For example, in a Podman container, run the following command: 

```shell-session
$ podman run gcr.io/k8s-staging-nfd/node-feature-discovery:master nfd-topology-updater -help
```


`-ca-file`
    

Specifies the TLS root certificate for verifying the authenticity of nfd-master. The `-ca-file` flag is one of three flags, together with `-cert-file` and `-key-file`, that controls mutual TLS authentication on the NFD Topology Updater. Default: empty. 

Important

The `-ca-file` flag must be specified together with the `-cert-file` and `-key-file` flags. 

**Example**

```shell-session
$ nfd-topology-updater -ca-file=/opt/nfd/ca.crt -cert-file=/opt/nfd/updater.crt -key-file=/opt/nfd/updater.key
```


`-cert-file`
    

Specifies the TLS certificate presented for authenticating outgoing requests. The `-cert-file` flag is one of three flags, together with `-ca-file` and `-key-file`, that controls mutual TLS authentication on the NFD Topology Updater. Default: empty. 

Important

The `-cert-file` flag must be specified together with the `-ca-file` and `-key-file` flags. 

**Example**

```shell-session
$ nfd-topology-updater -cert-file=/opt/nfd/updater.crt -key-file=/opt/nfd/updater.key -ca-file=/opt/nfd/ca.crt
```


`-h`, `-help`
     Print usage and exit. 
`-key-file`
    

Specifies the private key corresponding to the given certificate file, or `-cert-file`, that is used for authenticating outgoing requests. The `-key-file` flag is one of three flags, together with `-ca-file` and `-cert-file`, that controls mutual TLS authentication on the NFD Topology Updater. Default: empty. 

Important

The `-key-file` flag must be specified together with the `-ca-file` and `-cert-file` flags. 

**Example**

```shell-session
$ nfd-topology-updater -key-file=/opt/nfd/updater.key -cert-file=/opt/nfd/updater.crt -ca-file=/opt/nfd/ca.crt
```


`-kubelet-config-file`
    

Specifies the path to the kubelet’s configuration file. Default: `/host-var/lib/kubelet/config.yaml`. 

**Example**

```shell-session
$ nfd-topology-updater -kubelet-config-file=/var/lib/kubelet/config.yaml
```


`-no-publish`
    

Disables all communication with the nfd-master, making it a dry run flag for nfd-topology-updater. NFD Topology Updater runs resource hardware topology detection normally, but no CR requests are sent to nfd-master. Default: `false`. 

**Example**

```shell-session
$ nfd-topology-updater -no-publish
```


`-oneshot`
    

Causes the NFD Topology Updater to exit after one pass of resource hardware topology detection. Default: `false`. 

**Example**

```shell-session
$ nfd-topology-updater -oneshot -no-publish
```


`-podresources-socket`
    

Specifies the path to the UNIX socket where kubelet exports a gRPC service to enable discovery of in-use CPUs and devices, and to provide metadata for them. Default: `/host-var/lib/kubelet/pod-resources/kubelet.sock`. 

**Example**

```shell-session
$ nfd-topology-updater -podresources-socket=/var/lib/kubelet/pod-resources/kubelet.sock
```


`-server`
    

Specifies the address of the nfd-master endpoint to connect to. Default: `localhost:8080`. 

**Example**

```shell-session
$ nfd-topology-updater -server=nfd-master.nfd.svc.cluster.local:443
```


`-server-name-override`
    

Specifies the common name (CN) which to expect from the nfd-master TLS certificate. This flag is mostly intended for development and debugging purposes. Default: empty. 

**Example**

```shell-session
$ nfd-topology-updater -server-name-override=localhost
```


`-sleep-interval`
    

Specifies the interval between resource hardware topology re-examination and custom resource updates. A non-positive value implies infinite sleep interval and no re-detection is done. Default: `60s`. 

**Example**

```shell-session
$ nfd-topology-updater -sleep-interval=1h
```


`-version`
     Print version and exit. 
`-watch-namespace`
    

Specifies the namespace to ensure that resource hardware topology examination only happens for the pods running in the specified namespace. Pods that are not running in the specified namespace are not considered during resource accounting. This is particularly useful for testing and debugging purposes. A `*` value means that all of the pods across all namespaces are considered during the accounting process. Default: `*`. 

**Example**

```shell-session
$ nfd-topology-updater -watch-namespace=rte
```
