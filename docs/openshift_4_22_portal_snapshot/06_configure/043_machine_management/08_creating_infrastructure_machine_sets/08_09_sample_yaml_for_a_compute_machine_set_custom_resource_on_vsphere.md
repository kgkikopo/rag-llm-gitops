# 8.9. Sample YAML for a compute machine set custom resource on vSphere

To enable the Machine API to automate node provisioning on VMware vSphere infrastructure, define a `MachineSet` resource with parameters that are specific to vSphere, for example data center, resource pool, and template. 

The sample YAML file defines a compute machine set that runs on vSphere and creates nodes that are labeled with `node-role.kubernetes.io/infra: ""`. 

In this sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `infra` is the node label to add. 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  creationTimestamp: null
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-infra
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: infra
        machine.openshift.io/cluster-api-machine-type: infra
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra
    spec:
      metadata:
        creationTimestamp: null
        labels:
          node-role.kubernetes.io/infra: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          credentialsSecret:
            name: vsphere-cloud-credentials
          dataDisks:
          - name: "<disk_name>"
            provisioningMode: "<mode>"
            sizeGiB: 20
          diskGiB: 120
          kind: VSphereMachineProviderSpec
          memoryMiB: 8192
          metadata:
            creationTimestamp: null
          network:
            devices:
            - networkName: "<vm_network_name>"
          numCPUs: 4
          numCoresPerSocket: 1
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
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
```


where 

`<infrastructure_id>`
     Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command: 

```shell-session
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```


`<infrastructure_id>-infra`
     Specifies the infrastructure ID and `infra` node label. 
`infra`
     Specifies the `infra` node label. 
`<disk_name>`
     Specifies one or more data disk definitions. For more information, see "Configuring data disks by using machine sets". 
`<image_name>`
     Specifies the image to use as a boot image for your nodes. 
`<vm_network_name>`
     Specifies the vSphere VM network to deploy the compute machine set to. This VM network must be where other compute machines reside in the cluster. 
`<vm_template_name>`
     Specifies the vSphere VM template to use as a boot image for your nodes, such as `user-5ddjd-rhcos`. You should use a template with the latest OpenShift Container Platform image when adding a new machine set. 
`<vcenter_data_center_name>`
     Specifies the vCenter datacenter to deploy the compute machine set on. 
`<vcenter_datastore_name>`
     Specifies the vCenter datastore to deploy the compute machine set on. 
`<vcenter_vm_folder_path>`
     Specifies the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`. 
`<vsphere_resource_pool>`
     Specifies the vSphere resource pool for your VMs. 
`<vcenter_server_ip>`
     Specifies the vCenter server IP or fully qualified domain name. 
`taints`
    

Specifies a taint to prevent user workloads from being scheduled on infra nodes. 

Note

After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171). 

**Additional resources**

  * [Manually updating the boot image](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#mco-update-boot-images-manual)
