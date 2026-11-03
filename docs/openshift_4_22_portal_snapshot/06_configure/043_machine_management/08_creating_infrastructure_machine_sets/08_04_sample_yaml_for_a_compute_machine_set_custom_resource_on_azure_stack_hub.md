# 8.4. Sample YAML for a compute machine set custom resource on Azure Stack Hub

You can create a machine set on Microsoft Azure Stack Hub. By defining a YAML configuration with specific cluster IDs and provider details, you can automate the provisioning of specialized nodes. 

The Microsoft Azure sample YAML defines a compute machine set that runs in the `1` Azure zone in a region and creates nodes that are labeled with `node-role.kubernetes.io/infra: ""`. The sample YAML specifies a taint to prevent user workloads from being scheduled on infra nodes. After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171). 

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<infra>` is the node label to add. 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <infra>
    machine.openshift.io/cluster-api-machine-type: <infra>
  name: <infrastructure_id>-infra-<region>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<region>
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <infra>
        machine.openshift.io/cluster-api-machine-type: <infra>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<region>
    spec:
      metadata:
        creationTimestamp: null
        labels:
          node-role.kubernetes.io/infra: ""
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          availabilitySet: <availability_set>
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          image:
            offer: ""
            publisher: ""
            resourceID: /resourceGroups/<infrastructure_id>-rg/providers/Microsoft.Compute/images/<infrastructure_id>
            sku: ""
            version: ""
          internalLoadBalancer: ""
          kind: AzureMachineProviderSpec
          location: <region>
          managedIdentity: <infrastructure_id>-identity
          metadata:
            creationTimestamp: null
          natRule: null
          networkResourceGroup: ""
          osDisk:
            diskSizeGB: 128
            managedDisk:
              storageAccountType: Premium_LRS
            osType: Linux
          publicIP: false
          publicLoadBalancer: ""
          resourceGroup: <infrastructure_id>-rg
          sshPrivateKey: ""
          sshPublicKey: ""
          subnet: <infrastructure_id>-<role>-subnet
          userDataSecret:
            name: worker-user-data
          vmSize: Standard_DS4_v2
          vnet: <infrastructure_id>-vnet
          zone: "1"
```


where: 

`<infrastructure_id>`
    

Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift Container Platform CLI installed, you can obtain the infrastructure ID by running the following command: 

```shell-session
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```


You can obtain the subnet by running the following command: 

```shell-session
$  oc -n openshift-machine-api \
    -o jsonpath='{.spec.template.spec.providerSpec.value.subnet}{"\n"}' \
    get machineset/<infrastructure_id>-worker-centralus1
```


You can obtain the vnet by running the following command: 

```shell-session
$  oc -n openshift-machine-api \
    -o jsonpath='{.spec.template.spec.providerSpec.value.vnet}{"\n"}' \
    get machineset/<infrastructure_id>-worker-centralus1
```


`<infra>`
     Specifies the `<infra>` node label. 
`<infrastructure_id>-infra-<region>`
     Specifies the infrastructure ID, `<infra>` node label, and region. 
`<region>`
    

Specifies the region to place machines on. 

Note

The `spec.template.spec.providerSpec.value.zone` specifies the zone within your region to place machines on. Be sure that your region supports the zone that you specify. 

`<availability_set>`
     Specifies the availability set for the cluster. 
`<image>`
     Specifies the boot image to use. You should use the use the latest image when adding a new machine set. 

Note

Machine sets running on Azure Stack Hub do not support non-guaranteed Spot VMs.
