# 4.1. Installing the ovnkube-trace on local host

To run `ovnkube-trace` from your local host against a cluster, you can copy the binary from an `ovnkube-control-plane` pod and use familiar Kubernetes namespace and pod arguments. 

The `ovnkube-trace` tool traces packet simulations for arbitrary UDP or TCP traffic between points in an OVN-Kubernetes driven OpenShift Container Platform cluster. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You are logged in to the cluster with `cluster-admin` privileges. 



**Procedure**

  1. Create a pod variable by using the following command: 

```shell-session
$  POD=$(oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-control-plane -o name | head -1 | awk -F '/' '{print $NF}')
```


  2. Run the following command on your local host to copy the binary from the `ovnkube-control-plane` pods: 

```shell-session
$  oc cp -n openshift-ovn-kubernetes $POD:/usr/bin/ovnkube-trace -c ovnkube-cluster-manager ovnkube-trace
```


Note

If you are using Red Hat Enterprise Linux (RHEL) 8 to run the `ovnkube-trace` tool, you must copy the file `/usr/lib/rhel8/ovnkube-trace` to your local host. 

  3. Make `ovnkube-trace` executable by running the following command: 

```shell-session
$  chmod +x ovnkube-trace
```


  4. Display the options available with `ovnkube-trace` by running the following command: 

```shell-session
$  ./ovnkube-trace -help
```


**Example output**

```shell-session
Usage of ./ovnkube-trace:
  -addr-family string
    	Address family (ip4 or ip6) to be used for tracing (default "ip4")
  -dst string
    	dest: destination pod name
  -dst-ip string
    	destination IP address (meant for tests to external targets)
  -dst-namespace string
    	k8s namespace of dest pod (default "default")
  -dst-port string
    	dst-port: destination port (default "80")
  -kubeconfig string
    	absolute path to the kubeconfig file
  -loglevel string
    	loglevel: klog level (default "0")
  -ovn-config-namespace string
    	namespace used by ovn-config itself
  -service string
    	service: destination service name
  -skip-detrace
    	skip ovn-detrace command
  -src string
    	src: source pod name
  -src-namespace string
    	k8s namespace of source pod (default "default")
  -tcp
    	use tcp transport protocol
  -udp
    	use udp transport protocol
```


The command-line arguments supported are familiar Kubernetes constructs, such as namespaces, pods, services so you do not need to find the MAC address, the IP address of the destination nodes, or the ICMP type. 

The log levels are: 

     * 0 (minimal output) 
     * 2 (more verbose output showing results of trace commands) 
     * 5 (debug output)
