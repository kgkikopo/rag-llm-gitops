# 5.15. Machine scaling with static IP addresses

After you deployed your cluster to run nodes with static IP addresses, you can scale an instance of a machine or a machine set to use one of these static IP addresses. 

## 5.15.1. Scaling machines to use static IP addresses

You can add machines with predefined static IP addresses by creating machine resources that specify static network configuration in the machine YAML file. 

You can scale additional machine sets to use predefined static IP addresses on your cluster. For this configuration, you need to create a machine resource YAML file and then define static IP addresses in this file. 

**Prerequisites**

  * You deployed a cluster that runs at least one node with a configured static IP address. 



**Procedure**

  1. Create a machine resource YAML file and define static IP address network information in the `network` parameter. 

Example of a machine resource YAML file with static IP address information defined in the `network` parameter: 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  creationTimestamp: null
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <role>
    machine.openshift.io/cluster-api-machine-type: <role>
    machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
  name: <infrastructure_id>-<role>
  namespace: openshift-machine-api
spec:
  lifecycleHooks: {}
  metadata: {}
  providerSpec:
    value:
      apiVersion: machine.openshift.io/v1beta1
      credentialsSecret:
        name: vsphere-cloud-credentials
      diskGiB: 120
      kind: VSphereMachineProviderSpec
      memoryMiB: 8192
      metadata:
        creationTimestamp: null
      network:
        devices:
        - gateway: 192.168.204.1
          ipAddrs:
          - 192.168.204.8/24
          nameservers:
          - 192.168.204.1
          networkName: qe-segment-204
      numCPUs: 4
      numCoresPerSocket: 2
      snapshot: ""
      template: <vm_template_name>
      userDataSecret:
        name: worker-user-data
      workspace:
        datacenter: <vcenter_data_center_name>
        datastore: <vcenter_datastore_name>
        folder: <vcenter_vm_folder_path>
        resourcepool: <vsphere_resource_pool>
        server: <vcenter_server_ip>
status: {}
```


where: 

`gateway`
     Specifies an IP address for the default gateway for the network interface. 
`ipAddrs`
     Specifies a list of IPv4, IPv6, or both IP addresses that installation program passes to the network interface. Both IP families must use the same network interface for the default network. 
`nameservers`
    

Specifies a DNS name server. You can define up to 3 DNS name servers. Consider defining more than one DNS name server to take advantage of DNS resolution if that one DNS name server becomes unreachable. 

     * Create a `machine` custom resource (CR) by entering the following command in your terminal: 

```shell-session
$ oc create -f <file_name>.yaml
```


## 5.15.2. Machine set scaling of machines with configured static IP addresses

You can scale machines with static IP addresses by configuring machine sets that request addresses through `IPAddressClaim` resources managed by your IP address management (IPAM) service. 

You can use a machine set to scale machines with configured static IP addresses. 

After you configure a machine set to request a static IP address for a machine, the machine controller creates an `IPAddressClaim` resource in the `openshift-machine-api` namespace. The external controller then creates an `IPAddress` resource and binds any static IP addresses to the `IPAddressClaim` resource. 

Important

Your organization might use numerous types of IP address management (IPAM) services. If you want to enable a particular IPAM service on OpenShift Container Platform, you might need to manually create the `IPAddressClaim` resource in a YAML definition and then bind a static IP address to this resource by entering the following command in your `oc` CLI: 

```shell-session
$ oc create -f <ipaddressclaim_filename>
```


The following demonstrates an example of an `IPAddressClaim` resource: 

```yaml
kind: IPAddressClaim
metadata:
  finalizers:
  - machine.openshift.io/ip-claim-protection
  name: cluster-dev-9n5wg-worker-0-m7529-claim-0-0
  namespace: openshift-machine-api
spec:
  poolRef:
    apiGroup: ipamcontroller.example.io
    kind: IPPool
    name: static-ci-pool
status: {}
```


The machine controller updates the machine with a status of `IPAddressClaimed` to indicate that a static IP address has successfully bound to the `IPAddressClaim` resource. The machine controller applies the same status to a machine with multiple `IPAddressClaim` resources that each contain a bound static IP address.The machine controller then creates a virtual machine and applies static IP addresses to any nodes listed in the `providerSpec` of a machine’s configuration. 

## 5.15.3. Using a machine set to scale machines with configured static IP addresses

You can scale machines that use static IP addresses by configuring a machine set to request addresses from an IP address pool. 

You can use a machine set to scale machines with configured static IP addresses. 

The example in the procedure demonstrates the use of controllers for scaling machines in a machine set. 

**Prerequisites**

  * You deployed a cluster that runs at least one node with a configured static IP address. 



**Procedure**

  1. Configure a machine set by specifying IP pool information in the `network.devices.addressesFromPools` schema of the machine set’s YAML file: 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  annotations:
    machine.openshift.io/memoryMb: "8192"
    machine.openshift.io/vCPU: "4"
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-<role>
  namespace: openshift-machine-api
spec:
  replicas: 0
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
  template:
    metadata:
      labels:
        ipam: "true"
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
    spec:
      lifecycleHooks: {}
      metadata: {}
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          credentialsSecret:
            name: vsphere-cloud-credentials
          diskGiB: 120
          kind: VSphereMachineProviderSpec
          memoryMiB: 8192
          metadata: {}
          network:
            devices:
            - addressesFromPools:
              - group: ipamcontroller.example.io
                name: static-ci-pool
                resource: IPPool
              nameservers:
              - "192.168.204.1"
              networkName: qe-segment-204
          numCPUs: 4
          numCoresPerSocket: 2
          snapshot: ""
          template: rvanderp4-dev-9n5wg-rhcos-generated-region-generated-zone
          userDataSecret:
            name: worker-user-data
          workspace:
            datacenter: IBMCdatacenter
            datastore: /IBMCdatacenter/datastore/vsanDatastore
            folder: /IBMCdatacenter/vm/rvanderp4-dev-9n5wg
            resourcePool: /IBMCdatacenter/host/IBMCcluster//Resources
            server: vcenter.ibmc.devcluster.openshift.com
```


where: 

`addressesFromPools`
     Specifies an IP pool, which lists a static IP address or a range of static IP addresses. The IP Pool can either be a reference to a custom resource definition (CRD) or a resource supported by the `IPAddressClaims` resource handler. The machine controller accesses static IP addresses listed in the machine set’s configuration and then allocates each address to each machine. 
`nameservers`
     Lists a name server. You must specify a name server for nodes that receive static IP address, because the Dynamic Host Configuration Protocol (DHCP) network configuration does not support static IP addresses. 

  2. Scale the machine set by entering the following commands in your `oc` CLI: 

```shell-session
$ oc scale --replicas=2 machineset <machineset> -n openshift-machine-api
```


Or: 

```shell-session
$ oc edit machineset <machineset> -n openshift-machine-api
```


After each machine is scaled up, the machine controller creates an `IPAddressClaim` resource. 

  3. Optional: Check that the `IPAddressClaim` resource exists in the `openshift-machine-api` namespace by entering the following command: 

```shell-session
$ oc get ipaddressclaims.ipam.cluster.x-k8s.io -n openshift-machine-api
```


**Example`oc` CLI output that lists two IP pools listed in the `openshift-machine-api` namespace**

```shell-session
NAME                                         POOL NAME        POOL KIND
cluster-dev-9n5wg-worker-0-m7529-claim-0-0   static-ci-pool   IPPool
cluster-dev-9n5wg-worker-0-wdqkt-claim-0-0   static-ci-pool   IPPool
```


  4. Create an `IPAddress` resource by entering the following command: 

```shell-session
$ oc create -f ipaddress.yaml
```


The following example shows an `IPAddress` resource with defined network configuration information and one defined static IP address: 

```yaml
apiVersion: ipam.cluster.x-k8s.io/v1alpha1
kind: IPAddress
metadata:
  name: cluster-dev-9n5wg-worker-0-m7529-ipaddress-0-0
  namespace: openshift-machine-api
spec:
  address: 192.168.204.129
  claimRef:
    name: cluster-dev-9n5wg-worker-0-m7529-claim-0-0
  gateway: 192.168.204.1
  poolRef:
    apiGroup: ipamcontroller.example.io
    kind: IPPool
    name: static-ci-pool
  prefix: 23
```


where: 

`claimRef`
     The name of the target `IPAddressClaim` resource. 
`poolRef`
    

Details information about the static IP address or addresses from your nodes. 

Note

By default, the external controller automatically scans any resources in the machine set for recognizable address pool types. When the external controller finds `kind: IPPool` defined in the `IPAddress` resource, the controller binds any static IP addresses to the `IPAddressClaim` resource. 

  5. Update the `IPAddressClaim` status with a reference to the `IPAddress` resource: 

```shell-session
$ oc --type=merge patch IPAddressClaim cluster-dev-9n5wg-worker-0-m7529-claim-0-0 -p='{"status":{"addressRef": {"name": "cluster-dev-9n5wg-worker-0-m7529-ipaddress-0-0"}}}' -n openshift-machine-api --subresource=status
```


**Additional resources**

  * [Static IP addresses for vSphere nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installation-vsphere-installer-infra-requirements_ipi-vsphere-installation-reqs)
