# 8.5. Sample YAML for a compute machine set custom resource on IBM Cloud

You can use the sample YAML file to automate the provisioning of compute or infrastructure nodes within a specific Virtual Private Cloud (VPC). 

The sample YAML defines a compute machine set that runs in a specified IBM Cloud® zone in a region and creates nodes that are labeled with `node-role.kubernetes.io/infra: ""`. 

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<infra>` is the node label to add. 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <infra>
    machine.openshift.io/cluster-api-machine-type: <infra>
  name: <infrastructure_id>-<infra>-<region>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<infra>-<region>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <infra>
        machine.openshift.io/cluster-api-machine-type: <infra>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<infra>-<region>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/infra: ""
      providerSpec:
        value:
          apiVersion: ibmcloudproviderconfig.openshift.io/v1beta1
          credentialsSecret:
            name: ibmcloud-credentials
          image: <infrastructure_id>-rhcos
          kind: IBMCloudMachineProviderSpec
          primaryNetworkInterface:
              securityGroups:
              - <infrastructure_id>-sg-cluster-wide
              - <infrastructure_id>-sg-openshift-net
              subnet: <infrastructure_id>-subnet-compute-<zone>
          profile: <instance_profile>
          region: <region>
          resourceGroup: <resource_group>
          userDataSecret:
              name: <role>-user-data
          vpc: <vpc_name>
          zone: <zone>
        taints:
        - key: node-role.kubernetes.io/infra
          effect: NoSchedule
```


where: 

`<infrastructure_id>`
    

Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command: 

```shell-session
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```


`<infra>`
     Specifies the `<infra>` node label. 
`<infrastructure_id>-<infra>-<region>`
     Specifies the infrastructure ID, `<infra>` node label, and region. 
`<infrastructure_id>-rhcos`
     Specifies the custom Red Hat Enterprise Linux CoreOS (RHCOS) image to use as a boot image for your nodes. You should use the use the latest image when adding a new machine set. 
`<infrastructure_id>-subnet-compute-<zone>`
     Specifies the infrastructure ID and zone within your region to place machines on. Be sure that your region supports the zone that you specify. 
`<instance_profile>`
     Specifies the [IBM Cloud® instance profile](https://cloud.ibm.com/docs/vpc?topic=vpc-profiles&interface=ui). 
`<region>`
     Specifies the region to place machines on. 
`<resource_group>`
     Specifies the resource group that machine resources are placed in. This is either an existing resource group specified at installation time, or an installer-created resource group named based on the infrastructure ID. 
`<vpc_name>`
     Specifies the VPC name. 
`<zone>`
     Specifies the zone within your region to place machines on. Be sure that your region supports the zone that you specify. 
`taints`
    

Specifies the taint to prevent user workloads from being scheduled on infra nodes. 

Note

After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171).
