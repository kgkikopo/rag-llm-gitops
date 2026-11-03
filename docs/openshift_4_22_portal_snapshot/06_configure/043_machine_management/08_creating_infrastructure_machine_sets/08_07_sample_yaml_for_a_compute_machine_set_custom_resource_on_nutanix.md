# 8.7. Sample YAML for a compute machine set custom resource on Nutanix

You can use a YAML file to automate node provisioning and ensure workloads are scheduled correctly based on role and infrastructure requirements. 

The sample YAML shows how to define a Nutanix compute MachineSet for your cluster. It explains how to configure roles, labels, sizing, networking, and boot settings so new nodes are created consistently. 

The sample YAML defines a Nutanix compute machine set that creates nodes that are labeled with `node-role.kubernetes.io/infra: ""`. 

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<infra>` is the node label to add. 

## 8.7.1. Values obtained by using the OpenShift CLI

In the following example, you can obtain some of the values for your cluster by using the OpenShift CLI (`oc`). 

Infrastructure ID
    

The `<infrastructure_id>` string is the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command: 

```shell-session
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```


```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <infra>
    machine.openshift.io/cluster-api-machine-type: <infra>
  name: <infrastructure_id>-<infra>-<zone>
  namespace: openshift-machine-api
  annotations:
    machine.openshift.io/memoryMb: "16384"
    machine.openshift.io/vCPU: "4"
spec:
  replicas: 3
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<infra>-<zone>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <infra>
        machine.openshift.io/cluster-api-machine-type: <infra>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<infra>-<zone>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/infra: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1
          bootType: ""
          categories:
          - key: <category_name>
            value: <category_value>
          cluster:
            type: uuid
            uuid: <cluster_uuid>
          credentialsSecret:
            name: nutanix-credentials
          image:
            name: <infrastructure_id>-rhcos
            type: name
          kind: NutanixMachineProviderConfig
          memorySize: 16Gi
          project:
            type: name
            name: <project_name>
          subnets:
          - type: uuid
            uuid: <subnet_uuid>
          systemDiskSize: 120Gi
          userDataSecret:
            name: <user_data_secret>
          vcpuSockets: 4
          vcpusPerSocket: 1
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
```


where: 

`<infrastructure_id>`
     Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. 
`<infra>`
     Specifies the `<infra>` node label. 
`<infrastructure_id>-<role>-<zone>`
     Specifies the infrastructure ID, `<infra>` node label, and zone. 
`annotations`
     Specifies annotations for the cluster autoscaler. 
`bootType`
    

Specifies the boot type that the compute machines use. For more information about boot types, see [Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment](https://portal.nutanix.com/page/documents/kbs/details?targetId=kA07V000000H3K9SAK). Valid values are `Legacy`, `SecureBoot`, or `UEFI`. The default is `Legacy`. 

Note

You must use the `Legacy` boot type in OpenShift Container Platform 4.22. 

`<categories>`
     Specifies one or more Nutanix Prism categories to apply to compute machines. This stanza requires `key` and `value` parameters for a category key-value pair that exists in Prism Central. For more information about categories, see [Category management](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_6:ssp-ssp-categories-manage-pc-c.html). 
`<cluster>`
     Specifies a Nutanix Prism Element cluster configuration. In this example, the cluster type is `uuid`, so there is a `uuid` stanza. 
`<infrastructure_id>-rhcos`
     Specifies the image to use as a boot image for your nodes. You should use the use the latest image when adding a new machine set. 
`16Gi`
     Specifies the amount of memory for the cluster in Gi. 
`project`
     Specifies the Nutanix project that you use for your cluster. In this example, the project type is `name`, so there is a `name` stanza. 
`subnets`
     Specifies one or more UUID for the Prism Element subnet object. The CIDR IP address prefix for one of the specified subnets must contain the virtual IP addresses that the OpenShift Container Platform cluster uses. A maximum of 32 subnets for each Prism Element failure domain in the cluster is supported. All subnet UUID values must be unique. 
`120Gi`
     Specifies the size of the system disk in Gi. 
`<user_data_secret>`
     Specifies the name of the secret in the user data YAML file that is in the `openshift-machine-api` namespace. Use the value that installation program populates in the default compute machine set. 
`4`
     Specifies the number of vCPU sockets. 
`1`
     Specifies the number of vCPUs per socket. 
taints
    

Specifies a taint to prevent user workloads from being scheduled on infra nodes. 

Note

After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171).
