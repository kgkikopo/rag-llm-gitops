# 8.3. Sample YAML for a compute machine set custom resource on Azure

You can define a machine set YAML to provision nodes by specifying parameters such as `vmSize` and `image`. You can use this to automate and scale infrastructure consistently, to ensure compute nodes meet specific workload requirements within the cluster. 

The sample YAML defines a compute machine set that runs in the `1` Microsoft Azure zone in a region and creates nodes that are labeled with ifdef::infra[`node-role.kubernetes.io/infra: ""`. The YAML specifies a taint to prevent user workloads from being scheduled on infra nodes. After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171). 

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `infra` is the node label to add. 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: infra
    machine.openshift.io/cluster-api-machine-type: infra
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
        machine.openshift.io/cluster-api-machine-role: infra
        machine.openshift.io/cluster-api-machine-type: infra
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<region>
    spec:
      metadata:
        creationTimestamp: null
        labels:
          machine.openshift.io/cluster-api-machineset: <machineset_name>
          node-role.kubernetes.io/infra: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          image:
            offer: ""
            publisher: ""
            resourceID: /resourceGroups/<infrastructure_id>-rg/providers/Microsoft.Compute/galleries/gallery_<infrastructure_id>/images/<infrastructure_id>-gen2/versions/latest
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
          tags:
            <custom_tag_name_1>: <custom_tag_value_1>
            <custom_tag_name_2>: <custom_tag_value_2>
          subnet: <infrastructure_id>-<role>-subnet
          userDataSecret:
            name: worker-user-data
          vmSize: Standard_D4s_v3
          vnet: <infrastructure_id>-vnet
          zone: "1"
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
```


where: 

`<infrastructure_id>`
    

Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command: 

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


Note

The value of the `metadata.labels.machine.openshift.io/cluster-api-machine-role` parameter specifies the `infra` node label. 

`<infrastructure_id>-infra-<region>`
     Specifies the infrastructure ID, `infra` node label, and region. 

Note

The value of the `spec.template.spec.providerSpec.value.image` parameter specifies the image details for your compute machine set. If you want to use an Azure Marketplace image, see "Using the Azure Marketplace offering". 

The value of the `spec.template.spec.providerSpec.value.image.resourceID` parameter specifies an image that is compatible with your instance type. The Hyper-V generation V2 images created by the installation program have a `-gen2` suffix, while V1 images have the same name without the suffix. 

The value of the `spec.template.spec.providerSpec.value.location` parameter specifies the region to place machines on. 

`<custom_tag_name_1>`
     Optional: Specifies custom tags in your machine set. Provide the tag name in `<custom_tag_name>` field and the corresponding tag value in `<custom_tag_value>` field. 

Note

The value of the `spec.template.spec.providerSpec.value.zone` parameter specifies the zone within your region to place machines on. Ensure that your region supports the zone that you specify. If your region supports availability zones, you must specify the zone. Specifying the zone avoids volume node affinity failure when a pod requires a persistent volume attachment. To do this, you can create a compute machine set for each zone in the same region. 

**Additional resources**

  * [Machine sets that deploy machines as Spot VMs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#machineset-non-guaranteed-instance_creating-machineset-azure "2.2.6. Machine sets that deploy machines as Spot VMs")
  * [Using the Azure Marketplace offering](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-compute-machines-with-the-machine-api#installation-azure-marketplace-subscribe_creating-machineset-azure "2.2.4. Using the Azure Marketplace offering")
