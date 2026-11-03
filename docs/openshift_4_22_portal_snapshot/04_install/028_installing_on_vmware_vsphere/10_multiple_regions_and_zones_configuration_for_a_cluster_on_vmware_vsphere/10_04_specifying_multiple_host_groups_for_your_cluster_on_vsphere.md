# 10.4. Specifying multiple host groups for your cluster on vSphere

You can configure the `infrastructures.config.openshift.io` configuration resource to specify multiple host groups for your OpenShift Container Platform cluster that runs on a VMware vSphere instance. 

This is necessary if your vSphere instance is in a stretched cluster configuration, with your ESXi hosts and storage distributed across multiple physical data centers. Use this procedure if you did not already configure host groups for your OpenShift Container Platform cluster at installation, or if you need to update your OpenShift Container Platform cluster with additional host groups. 

**Prerequisites**

  * ESXi hosts are grouped into host groups, which are linked via VM-host affinity rules to corresponding virtual machine (VM) groups. See the following example `govc` commands for details: 

```shell-session
# This example shows the correct configuration for a cluster with two host groups:

# Create host groups:
govc cluster.group.create -name <host_group_1> -host
govc cluster.group.create -name <host_group_2> -host

# Create VM groups:
govc cluster.group.create -name <vm_group_1> -vm
govc cluster.group.create -name <vm_group_2> -vm

# Create VM-host affinity rules:
govc cluster.rule.create -name <rule_1> -enable -vm-host -vm-group <vm_group_1> -host-affine-group <host_group_1>
govc cluster.rule.create -name <rule_2> -enable -vm-host -vm-group <vm_group_2> -host-affine-group <host_group_2>

# Add ESXi hosts to host groups:
govc cluster.group.change -name <host_group_1> <esxi_host_1_ip>
govc cluster.group.change -name <host_group_2> <esxi_host_2_ip>
```


  * `openshift-region` and `openshift-zone` tag categories are created on the vCenter server. 
  * Compute clusters have tags from the `openshift-region` tag category. 
  * ESXi hosts within host groups have tags from the `openshift-zone` tag category. 
  * `Host.Inventory.EditCluster` privilege is granted on the vSphere vCenter cluster object. 



**Procedure**

  1. Edit the infrastructure settings of your OpenShift Container Platform cluster. 

     1. To copy your existing infrastructure settings to a file, run the following command: 

```shell-session
$ oc get infrastructures.config.openshift.io cluster -o yaml > <name_of_infrastructure_file>.yaml
```


     2. Edit your infrastructure file to include a failure domain for each host group in your vSphere cluster. Refer to the following YAML file for an example of this configuration. Ensure you replace any values wrapped in angle brackets (`< >`) with your values: 

```yaml
apiVersion: config.openshift.io/v1
kind: Infrastructure
metadata:
  name: cluster
spec:
  cloudConfig:
    key: config
    name: cloud-provider-config
  platformSpec:
    type: VSphere
    vsphere:
      apiServerInternalIPs:
      - <internal_ip_of_api_server>
      failureDomains:
      - name: <unique_name_for_failure_domain_1>
        region: <cluster_1_region_tag>
        server: <vcenter_server_ip_address>
        zoneAffinity:
          type: HostGroup
          hostGroup:
            vmGroup: <name_of_vm_group_1>
            hostGroup: <name_of_host_group_1>
            vmHostRule: <name_of_vm_host_affinity_rule_1>
        regionAffinity:
          type: ComputeCluster
        topology:
          computeCluster: /<data_center_1>/host/<cluster_1>
          datacenter: <data_center_1>
          datastore: /<data_center_1>/datastore/<datastore_1>
          networks:
          - VM Network
          resourcePool: /<data_center_1>/host/<cluster_1>/Resources
          template: /<data_center_1>/vm/<vm_template>
        zone: <host_group_1_tag>
      - name: <unique_name_for_failure_domain_2>
        region: <cluster_1_region_tag>
        server: <vcenter_server_ip_address>
        zoneAffinity:
          type: HostGroup
          hostGroup:
            vmGroup: <name_of_vm_group_2>
            hostGroup: <name_of_host_group_2>
            vmHostRule: <name_of_vm_host_affinity_rule_2>
        regionAffinity:
          type: ComputeCluster
        topology:
          computeCluster: /<data_center_1>/host/<cluster_1>
          datacenter: <data_center_1>
          datastore: /<data_center_1>/datastore/<datastore_1>
          networks:
          - VM Network
          resourcePool: /<data_center_1>/host/<cluster_1>/Resources
          template: /<data_center_1>/vm/<vm_template>
        zone: <host_group_2_tag>
# ...
```


     3. To update your cluster with these changes, run the following command: 

```shell-session
$ oc replace -f <name_of_infrastructure_file>.yaml
```


  2. Update your `ControlPlaneMachineSet` custom resource (CR) with the new failure domains by completing the following steps: 

     1. Edit the `ControlPlaneMachineSet` CR by running the following command: 

```shell-session
$ oc edit controlplanemachinesets.machine.openshift.io -n openshift-machine-api cluster
```


     2. Edit the `failureDomains` parameter as shown in the following example: 

```yaml
spec:
  replicas: 3
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: jdoe3-whb8l
      machine.openshift.io/cluster-api-machine-role: master
      machine.openshift.io/cluster-api-machine-type: master
  state: Active
  strategy:
    type: RollingUpdate
  template:
    machineType: machines_v1beta1_machine_openshift_io
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        platform: VSphere
        vsphere:
        - name: <failure_domain_1_name>
        - name: <failure_domain_2_name>
# ...
```


     3. Verify that your control plane nodes have finished updating before proceeding further. To do this, run the following command: 

```shell-session
$ oc get controlplanemachinesets.machine.openshift.io -n openshift-machine-api
```


  3. Create new `MachineSet` CRs for your failure domains. 

     1. To retrieve the configuration of an existing `MachineSet` CR for use as a template, run the following command: 

```shell-session
$ oc get machinesets.machine.openshift.io -n openshift-machine-api <existing_machine_set> -o yaml > machineset-<failure_domain_name>.yaml
```


     2. Copy the template as needed to create `MachineSet` CR files for each failure domain that you defined in your infrastructure file. Refer to the following example: 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <machineset_name>
  namespace: openshift-machine-api
spec:
  replicas: 0
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <machineset_name>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <machineset_name>
    spec:
      lifecycleHooks: {}
      metadata: {}
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          credentialsSecret:
            name: vsphere-cloud-credentials
          diskGiB: <disk_GiB>
          kind: VSphereMachineProviderSpec
          memoryMiB: <memory_in_MiB>
          metadata:
            creationTimestamp: null
          network:
            devices:
            - networkName: VM Network
          numCPUs: <number_of_cpus>
          numCoresPerSocket: <number_of_cores_per_socket>
          snapshot: ""
          template: <template_name>
          userDataSecret:
            name: worker-user-data
          workspace:
            datacenter: <data_center_1>
            datastore: /<data_center_1>/datastore/<datastore_1>
            folder: /<data_center_1>/vm/<folder>
            resourcePool: /<data_center_1>/host/<cluster_1>/Resources
            server: <server_ip_address>
            vmGroup: <name_of_vm_group_1>
# ...
```


     3. For each `MachineSet` CR file, run the following command: 

```shell-session
$ oc create -f <name_of_machine_set_file>.yaml
```
