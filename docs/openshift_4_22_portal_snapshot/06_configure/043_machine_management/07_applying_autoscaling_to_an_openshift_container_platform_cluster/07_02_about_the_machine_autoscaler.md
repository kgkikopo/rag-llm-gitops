# 7.2. About the machine autoscaler

The machine autoscaler adjusts the number of Machines in the compute machine sets that you deploy in an OpenShift Container Platform cluster. 

You can scale both the default `worker` compute machine set and any other compute machine sets that you create. The machine autoscaler makes more Machines when the cluster runs out of resources to support more deployments. Any changes to the values in `MachineAutoscaler` resources, such as the minimum or maximum number of instances, are immediately applied to the compute machine set they target. 

Important

You must deploy a machine autoscaler for the cluster autoscaler to scale your machines. The cluster autoscaler uses the annotations on compute machine sets that the machine autoscaler sets to determine the resources that it can scale. If you define a cluster autoscaler without also defining machine autoscalers, the cluster autoscaler will never scale your cluster. 

## 7.2.1. Configure machine autoscalers

After you deploy the cluster autoscaler, deploy `MachineAutoscaler` resources that reference the compute machine sets that are used to scale the cluster. 

Important

You must deploy at least one `MachineAutoscaler` resource after you deploy the `ClusterAutoscaler` resource. 

Note

You must configure separate resources for each compute machine set. Remember that compute machine sets are different in each region, so consider whether you want to enable machine scaling in multiple regions. The compute machine set that you scale must have at least one machine in it. 

### 7.2.1.1. Machine autoscaler resource definition

This `MachineAutoscaler` resource definition shows the parameters and sample values for the machine autoscaler. 

```yaml
apiVersion: "autoscaling.openshift.io/v1beta1"
kind: "MachineAutoscaler"
metadata:
  name: "worker-us-east-1a"
  namespace: "openshift-machine-api"
spec:
  minReplicas: 1
  maxReplicas: 12
  scaleTargetRef:
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineSet
    name: worker-us-east-1a
```


where: 

<name>
     Specify the machine autoscaler name. To make it easier to identify which compute machine set this machine autoscaler scales, specify or include the name of the compute machine set to scale. The compute machine set name takes the following form: `<clusterid>-<machineset>-<region>`. 
<minReplicas>
    

Specify the minimum number machines of the specified type that must remain in the specified zone after the cluster autoscaler initiates cluster scaling. If running in AWS, Google Cloud, Azure, RHOSP, or vSphere, this value can be set to `0`. For other providers, do not set this value to `0`. 

You can save on costs by setting this value to `0` for use cases such as running expensive or limited-usage hardware that is used for specialized workloads, or by scaling a compute machine set with extra large machines. The cluster autoscaler scales the compute machine set down to zero if the machines are not in use. 

Important

Do not set the `spec.minReplicas` value to `0` for the three compute machine sets that are created during the OpenShift Container Platform installation process for an installer provisioned infrastructure. 

<maxReplicas>
     Specify the maximum number machines of the specified type that the cluster autoscaler can deploy in the specified zone after it initiates cluster scaling. Ensure that the `maxNodesTotal` value in the `ClusterAutoscaler` resource definition is large enough to allow the machine autoscaler to deploy this number of machines. 
<scaleTargetRef>
     In this section, provide values that describe the existing compute machine set to scale. 
<kind>
     The `kind` parameter value is always `MachineSet`. 
<name>
     The `name` value must match the name of an existing compute machine set, as shown in the `metadata.name` parameter value. 

## 7.2.2. Deploy a machine autoscaler

To deploy a machine autoscaler, you create an instance of the `MachineAutoscaler` resource. 

**Procedure**

  1. Create a YAML file for a `MachineAutoscaler` resource that contains the custom resource definition. 
  2. Create the custom resource in the cluster by running the following command: 

```shell-session
$ oc create -f <filename>.yaml
```


where: 

`<filename>`
     Specifies the name of the YAML file you created.
