# 11.4. Configuration options for Cluster API machines

## 11.4.1. Cluster API configuration options for Amazon Web Services

You can change the configuration of your Amazon Web Services (AWS) Cluster API machines by updating values in the Cluster API custom resource manifests. 

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

The YAML file examples show configurations for an Amazon Web Services cluster. 

You can enable features by updating values in the Cluster API custom resource manifests. 

### 11.4.1.1. Sample YAML for a Cluster API machine template resource on Amazon Web Services

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines. 

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      iamInstanceProfile: # ...
      instanceType: m5.large
      ignition:
        storageType: UnencryptedUserData
        version: "3.4"
      ami:
        id: # ...
      subnet:
        filters:
        - name: tag:Name
          values:
          - # ...
      additionalSecurityGroups:
      - filters:
        - name: tag:Name
          values:
          - # ...
```


where: 

`kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`metadata.name`
     Specifies a name for the machine template. 
`spec.template.spec`
     Specifies the details for your environment. The values here are examples. 

### 11.4.1.2. Sample YAML for a Cluster API compute machine set resource on Amazon Web Services

The compute machine set resource defines additional properties of the machines that the resource creates. The compute machine set also references the cluster resource and machine template when creating machines. 

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: AWSMachineTemplate
        name: <template_name>
```


where: 

`metadata.name`
     Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`. 
`metadata.labels.cluster.x-k8s.io/cluster-name`
     Specifies the cluster ID as the name of the cluster. 
`spec.clusterName`
     Specifies the cluster ID as the name of the cluster. 
`spec.template.spec.infrastructureRef.kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`spec.template.spec.infrastructureRef.name`
     Specifies the machine template name. 

#### 11.4.1.2.1. Elastic Fabric Adapter instances and placement group options

You can deploy compute machines on Elastic Fabric Adapter (EFA) instances within an existing AWS placement group. 

EFA instances do not require placement groups, and you can use placement groups for purposes other than configuring an EFA. The following example uses an EFA and placement group together to demonstrate a configuration that can improve network performance for machines within the specified placement group. 

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines. 

**Sample EFA instance and placement group configuration**

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceType: <supported_instance_type>
      networkInterfaceType: efa
      placementGroupName: <placement_group>
      placementGroupPartition: <placement_group_partition_number>
# ...
```


where: 

`spec.template.spec.instanceType`
     Specifies an instance type that supports EFAs. For more information, see "Supported instance types". 
`spec.template.spec.networkInterfaceType`
     Specifies the `efa` network interface type. 
`spec.template.spec.placementGroupName`
     Specifies the name of the existing AWS placement group to deploy machines in. 
`spec.template.spec.placementGroupPartition`
     Specifies the partition number of the existing AWS placement group where you want your machines deployed. Setting a value for the parameter is optional. 

Note

Ensure that the rules and limitations for the type of placement group that you create are compatible with your intended use case. For more information, see "Placement groups for your Amazon EC2 instances". 

**Additional resources**

  * [Elastic Fabric Adapter (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html)
  * [Placement groups for your Amazon EC2 instances (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#limitations-placement-groups)
  * [Supported instance types (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types)



#### 11.4.1.2.2. Amazon EC2 Instance Metadata Service configuration options

You can restrict the version of the Amazon EC2 Instance Metadata Service (IMDS) that machines on Amazon Web Services (AWS) clusters use. Machines can require the use of IMDSv2, or allow the use of IMDSv1 in addition to IMDSv2. 

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines. 

Important

Before creating machines that require IMDSv2, ensure that any workloads that interact with the IMDS support IMDSv2. 

**Sample IMDS configuration**

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceMetadataOptions:
        httpEndpoint: enabled
        httpPutResponseHopLimit: 1
        httpTokens: optional
        instanceMetadataTags: disabled
# ...
```


where: 

`spec.template.spec.instanceMetadataOptions.httpPutResponseHopLimit`
     Specifies the number of network hops allowed for IMDSv2 calls. If no value is specified, this parameter is set to `1` by default. 
`spec.template.spec.instanceMetadataOptions.httpTokens`
    

Specifies whether to require the use of IMDSv2. If no value is specified, this parameter is set to `optional` by default. The following values are valid: 

  * `optional`: Allow the use of both IMDSv1 and IMDSv2. 
  * `required`: Require IMDSv2. 



Note

The Machine API does not support the `httpEndpoint`, `httpPutResponseHopLimit`, and `instanceMetadataTags` fields. If you migrate a Cluster API machine template that uses this feature to a Machine API compute machine set, any Machine API machines that it creates will not have these fields and the underlying instances will not use these settings. Any existing machines that the migrated machine set manages will retain these fields and the underlying instances will continue to use these settings. 

Requiring the use of IMDSv2 might cause timeouts. For more information, including mitigation strategies, see "Instance metadata access considerations". 

**Additional resources**

  * [IMDSv2 (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)
  * [Instance metadata access considerations (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html#imds-considerations)



#### 11.4.1.2.3. Dedicated Instance configuration options

You can deploy machines that are backed by Dedicated Instances on Amazon Web Services (AWS) clusters. 

Dedicated Instances run in a virtual private cloud (VPC) on hardware that is dedicated to a single customer. These Amazon EC2 instances are physically isolated at the host hardware level. The isolation of Dedicated Instances occurs even if the instances belong to different AWS accounts that are linked to a single payer account. However, other instances that are not dedicated can share hardware with Dedicated Instances if they belong to the same AWS account. 

OpenShift Container Platform supports instances with public or dedicated tenancy. 

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines. 

**Sample Dedicated Instances configuration**

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      tenancy: dedicated
# ...
```


The `tenancy` field specifies using instances with dedicated tenancy that run on single-tenant hardware. If you do not specify the `dedicated` value, instances with public tenancy that run on shared hardware are used by default. 

#### 11.4.1.2.4. Place machines on Dedicated Hosts by using machine templates

You can configure a machine template to place machines on Amazon Web Services (AWS) Dedicated Hosts. With dynamic host allocation, the Cluster API requests a Dedicated Host from AWS and applies the specified tags to the Dedicated Host. 

Important

AWS Dedicated Host support is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines. 

**Procedure**

  * Configure the following fields in your `AWSMachineTemplate` resource: 

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      tenancy: host
      hostAffinity: host
      dynamicHostAllocation:
        tags:
          <tag_name>: <tag_value>
# ...
```


where: 

`spec.template.spec.dynamicHostAllocation.tags`
     Optional parameter. Specifies tags to apply to the dynamically allocated Dedicated Host. If you specify tags, you must specify both a key and a value. For `<tag_name>`, specify the tag key, for example `Environment`. For `<tag_value>`, specify the tag value, for example `production`. 




#### 11.4.1.2.5. Place machines on a specific Dedicated Host by using machine templates

You can configure a machine template to place machines on a specific Amazon Web Services (AWS) Dedicated Host by specifying the host ID. 

Important

AWS Dedicated Host support is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines. 

**Procedure**

  * Configure the following fields in your `AWSMachineTemplate` resource: 

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      tenancy: host
      hostAffinity: host
      hostID: <dedicated_host_id>
# ...
```


where: 

`<dedicated_host_id>`
     Specifies the ID of the AWS Dedicated Host on which to place the machine, for example `h-0123456789abcdef0`. 




#### 11.4.1.2.6. Non-guaranteed Spot Instances and hourly cost limits

You can deploy machines as non-guaranteed Spot Instances on Amazon Web Services (AWS). Spot Instances use spare AWS EC2 capacity and are less expensive than On-Demand Instances. You can use Spot Instances for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads. 

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines. 

Important

AWS EC2 can reclaim the capacity for a Spot Instance at any time. 

**Sample Spot Instance configuration**

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      spotMarketOptions:
        maxPrice: <price_per_hour>
# ...
```


where: 

`spec.template.spec.spotMarketOptions`
     Specifies the use of Spot Instances. 
`spec.template.spec.spotMarketOptions.maxPrice`
    

Optional parameter. Specifies an hourly cost limit in US dollars for the Spot Instance. For example, setting the `<price_per_hour>` value to `2.50` limits the cost of the Spot Instance to USD 2.50 per hour. When this value is not set, the maximum price charges up to the On-Demand Instance price. 

Warning

Setting a specific `maxPrice: <price_per_hour>` value might increase the frequency of interruptions compared to using the default On-Demand Instance price. Red Hat recommends to use the default On-Demand Instance price and to not set the maximum price for Spot Instances. 

Interruptions can occur when using Spot Instances for the following reasons: 

  * The instance price exceeds your maximum price 
  * The demand for Spot Instances increases 
  * The supply of Spot Instances decreases 



AWS gives a two-minute warning to the user when an interruption occurs. OpenShift Container Platform begins to remove the workloads from the affected instances when AWS issues the termination warning. 

When AWS terminates an instance, a termination handler running on the Spot Instance node deletes the machine resource. To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a Spot Instance. 

#### 11.4.1.2.7. Configuring storage throughput for gp3 drives

You can improve performance for high traffic services by increasing the throughput of gp3 storage volumes in an AWS cluster. You can configure the storage throughput for the root volume, non root volumes, or both. 

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines. 

**Prerequisites**

  * You use gp3 storage volume(s). 



**Procedure**

  * On the machine template in which you want to configure throughput, add the `throughput` parameter: 

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      nonRootVolumes:
      - throughput: <throughput_value>
      rootVolume:
        throughput: <throughput_value>
# ...
```


where: 

`<throughput_value>`
     Specifies a value in MiB per second between 125 and 2,000. You can only edit this value on gp3 volumes. The default value is `125`. 




#### 11.4.1.2.8. Capacity Reservation configuration options

OpenShift Container Platform version 4.22 and later supports Capacity Reservations on Amazon Web Services clusters, including On-Demand Capacity Reservations and Capacity Blocks for ML. 

You can deploy machines on any available resources that match the parameters of a capacity request that you define. These parameters specify the instance type, region, and number of instances that you want to reserve. If your Capacity Reservation can accommodate the capacity request, the deployment succeeds. 

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines. 

**Sample Capacity Reservation configuration**

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      capacityReservationId: <capacity_reservation>
      capacityReservationPreference: <reservation_preference>
      marketType: <market_type>
# ...
```


where: 

`spec.template.spec.capacityReservationId`
     Specifies the ID of the Capacity Block for ML or On-Demand Capacity Reservation that you want to deploy machines on. 
`spec.template.spec.capacityReservationPreference`
    

Specifies your preferred capacity reservation behavior. The following values are valid: 

`CapacityReservationsOnly`
     Use this option to require a matching capacity reservation. If no matching capacity reservation is available, the instance fails to launch. 
`Open`
     Use this option to allow using an open capacity reservation that matches the availability zone and instance type. 
`None`
     Use this option to prohibit using a capacity reservation. You might use this option to help keep capacity reservations available for workloads that you want to use them. 

`spec.template.spec.marketType`
    

Specifies the market type to use. The following values are valid: 

`CapacityBlock`
     Use this market type with Capacity Blocks for ML. 
`OnDemand`
     Use this market type with On-Demand Capacity Reservations. 
`Spot`
     Use this market type with Spot Instances. This option is not compatible with Capacity Reservations. 

For more information, including limitations and suggested use cases for this offering, see On-Demand Capacity Reservations and Capacity Blocks for ML (AWS documentation). 

**Additional resources**

  * [On-Demand Capacity Reservations and Capacity Blocks for ML (AWS documentation)](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html)



#### 11.4.1.2.9. GPU-enabled machine options

You can deploy GPU-enabled compute machines on Amazon Web Services (AWS). 

The following sample configuration uses an AWS G4dn instance type, which includes an NVIDIA Tesla T4 Tensor Core GPU, as an example. 

For more information about supported instance types, see the following pages in the NVIDIA documentation: 

  * NVIDIA GPU Operator Community support matrix 
  * NVIDIA AI Enterprise support matrix 



To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file and a machine set YAML file that references the machine template when it deploys machines. 

**Sample GPU-enabled machine template configuration**

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceType: g4dn.xlarge
# ...
```


  * The `spec.template.spec.instanceType` field specifies a G4dn instance type. 



**Sample GPU-enabled machine set configuration**

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <cluster_name>-gpu-<region>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <cluster_name>-gpu-<region>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <cluster_name>-gpu-<region>
        node-role.kubernetes.io/<role>: ""
# ...
```


where: 

`metadate.name`
     Specifies a name that includes the `gpu` role. The name includes the cluster ID as a prefix and the region as a suffix. 
`spec.selector.matchLabels.cluster.x-k8s.io/set-name`
     Specifies a selector label that matches the machine set name. 
`spec.template.metadata.labels.cluster.x-k8s.io/set-name`
     Specifies a template label that matches the machine set name. 

**Additional resources**

  * [AWS G4dn instance type](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing)
  * [NVIDIA GPU Operator Community support matrix (NVIDIA documentation)](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/platform-support.html)
  * [NVIDIA AI Enterprise support matrix (NVIDIA documentation)](https://docs.nvidia.com/ai-enterprise/latest/product-support-matrix/index.html)



## 11.4.2. Cluster API configuration options for Google Cloud

You can change the configuration of your Google Cloud Cluster API machines by updating values in the Cluster API custom resource manifests. 

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

### 11.4.2.1. Sample YAML for configuring Google Cloud clusters

The following example YAML files show configurations for a Google Cloud cluster. 

#### 11.4.2.1.1. Sample YAML for a Cluster API machine template resource on Google Cloud

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines. 

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: GCPMachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      rootDeviceType: pd-ssd
      rootDeviceSize: 128
      instanceType: n1-standard-4
      image: projects/rhcos-cloud/global/images/rhcos-411-85-202203181601-0-gcp-x86-64
      subnet: <cluster_name>-worker-subnet
      serviceAccounts:
        email: <service_account_email_address>
        scopes:
          - https://www.googleapis.com/auth/cloud-platform
      additionalLabels:
        kubernetes-io-cluster-<cluster_name>: owned
      additionalNetworkTags:
        - <cluster_name>-worker
      ipForwarding: Disabled
```


where: 

`kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`metadata.name`
     Specifies a name for the machine template. 
`spec.template.spec`
     Specifies the details for your environment. The values here are examples. 

#### 11.4.2.1.2. Sample YAML for a Cluster API compute machine set resource on Google Cloud

The compute machine set resource defines additional properties of the machines that it creates. The compute machine set also references the cluster resource and machine template when creating machines. 

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: GCPMachineTemplate
        name: <template_name>
      failureDomain: <failure_domain>
```


where: 

`metadata.name`
     Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`. 
`metadata.labels.cluster.x-k8s.io/cluster-name`
     Specifies the cluster ID as the name of the cluster. 
`spec.clusterName`
     Specifies the cluster ID as the name of the cluster. 
`spec.template.spec.infrastructureRef.kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`spec.template.spec.infrastructureRef.name`
     Specifies the machine template name. 
`spec.template.spec.failureDomain`
     Specifies the failure domain within the Google Cloud region. 

## 11.4.3. Cluster API configuration options for Microsoft Azure

You can change the configuration of your Microsoft Azure Cluster API machines by updating values in the Cluster API custom resource manifests. 

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

The following example YAML files show configurations for an Azure cluster. 

### 11.4.3.1. Sample YAML for a Cluster API machine template resource on Microsoft Azure

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines. 

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: AzureMachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      disableExtensionOperations: true
      identity: UserAssigned
      image:
        id: /subscriptions/<subscription_id>/resourceGroups/<cluster_name>-rg/providers/Microsoft.Compute/galleries/gallery_<compliant_cluster_name>/images/<cluster_name>-gen2/versions/latest
      networkInterfaces:
        - acceleratedNetworking: true
          privateIPConfigs: 1
          subnetName: <cluster_name>-worker-subnet
      osDisk:
        diskSizeGB: 128
        managedDisk:
          storageAccountType: Premium_LRS
        osType: Linux
      sshPublicKey: <ssh_key_value>
      userAssignedIdentities:
        - providerID: 'azure:///subscriptions/<subscription_id>/resourcegroups/<cluster_name>-rg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<cluster_name>-identity'
      vmSize: Standard_D4s_v3
```


where: 

`kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`metadata.name`
     Specifies a name for the machine template. 
`spec.template.spec`
     Specifies the details for your environment. The values here are examples. 
`spec.template.spec.image.id`
     Specifies an image that is compatible with your instance type. The Hyper-V generation V2 images created by the installation program have a `-gen2` suffix, while V1 images have the same name without the suffix. 

Note

Default OpenShift Container Platform cluster names contain hyphens (`-`), which are not compatible with Azure gallery name requirements. The value of `<compliant_cluster_name>` in this configuration must use underscores (`_`) instead of hyphens to comply with these requirements. Other instances of `<cluster_name>` do not change. 

For example, a cluster name of `jdoe-test-2m2np` transforms to `jdoe_test_2m2np`. The full string for `gallery_<compliant_cluster_name>` in this example is `gallery_jdoe_test_2m2np`, not `gallery_jdoe-test-2m2np`. The complete value of `spec.template.spec.image.id` for this example value is `/subscriptions/<subscription_id>/resourceGroups/jdoe-test-2m2np-rg/providers/Microsoft.Compute/galleries/gallery_jdoe_test_2m2np/images/jdoe-test-2m2np-gen2/versions/latest`. 

### 11.4.3.2. Sample YAML for a Cluster API compute machine set resource on Microsoft Azure

The compute machine set resource defines additional properties of the machines that it creates. The compute machine set also references the cluster resource and machine template when creating machines. 

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
        dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: AzureMachineTemplate
        name: <template_name>
```


where: 

`metadata.name`
     Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`. 
`metadata.labels.cluster.x-k8s.io/cluster-name`
     Specifies the cluster ID as the name of the cluster. 
`spec.template.spec.infrastructureRef.kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`spec.template.spec.infrastructureRef.name`
     Specifies the machine template name. 

## 11.4.4. Cluster API configuration options for Red Hat OpenStack Platform

You can change the configuration of your Red Hat OpenStack Platform (RHOSP) Cluster API machines by updating values in the Cluster API custom resource manifests. 

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

### 11.4.4.1. Sample YAML for configuring RHOSP clusters

The following example YAML files show configurations for a RHOSP cluster. 

#### 11.4.4.1.1. Sample YAML for a Cluster API machine template resource on RHOSP

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines. 

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: OpenStackMachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      flavor: <openstack_node_machine_flavor>
      image:
        filter:
          name: <openstack_image>
```


where: 

`kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`metadata.name`
     Specifies a name for the machine template. 
`spec.template.spec`
     Specifies the details for your environment. The values here are examples. 
`spec.template.spec.flavor`
     Specifies the RHOSP flavor to use. For more information, see "Creating flavors for launching instances". 
`spec.template.spec.image.filter.name`
     Specifies the image to use. 

**Additional resources**

  * [Creating flavors for launching instances](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/17.1/html/configuring_the_compute_service_for_instance_creation/assembly_creating-flavors-for-launching-instances_instance-flavors)



#### 11.4.4.1.2. Sample YAML for a Cluster API compute machine set resource on RHOSP

The compute machine set resource defines additional properties of the machines that the resource creates. The compute machine set also references the infrastructure resource and machine template when creating machines. 

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: OpenStackMachineTemplate
        name: <template_name>
      failureDomain: <nova_availability_zone>
```


where: 

`metadata.name`
     Specifies a name for the compute machine set. 
`spec.clusterName`
     Specifies the cluster ID as the name of the cluster. 
`spec.template.spec.bootstrap.dataSecretName`
     For the Cluster API Technology Preview, the Operator can use the worker user data secret from the `openshift-machine-api` namespace. 
`spec.template.spec.infrastructureRef.kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`spec.template.spec.infrastructureRef.name`
     Specifies the machine template name. 
`spec.template.spec.failureDomain`
     Optional parameter. Specifies the name of the Nova availability zone for the machine set to create machines in. If you do not specify a value, machines are not restricted to a specific availability zone. 

## 11.4.5. Cluster API configuration options for VMware vSphere

You can change the configuration of your VMware vSphere Cluster API machines by updating values in the Cluster API custom resource manifests. 

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

### 11.4.5.1. Sample YAML for configuring VMware vSphere clusters

The following example YAML files show configurations for a VMware vSphere cluster. 

#### 11.4.5.1.1. Sample YAML for a Cluster API machine template resource on VMware vSphere

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines. 

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: VSphereMachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      template: <vm_template_name>
      server: <vcenter_server_ip>
      diskGiB: 128
      cloneMode: linkedClone
      datacenter: <vcenter_data_center_name>
      datastore: <vcenter_datastore_name>
      folder: <vcenter_vm_folder_path>
      resourcePool: <vsphere_resource_pool>
      numCPUs: 4
      memoryMiB: 16384
      network:
        devices:
        - dhcp4: true
          networkName: "<vm_network_name>"
```


where: 

`kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`metadata.name`
     Specifies a name for the machine template. 
`spec.template.spec`
     Specifies the details for your environment. The values here are examples. 
`spec.template.spec.template`
     Specifies the vSphere VM template to use, such as `user-5ddjd-rhcos`. 
`spec.template.spec.server`
     Specifies the vCenter server IP or fully qualified domain name. 
`spec.template.spec.cloneMode`
    

Specifies the type of VM clone to use. The following values are valid: 

  * `fullClone`
  * `linkedClone`



When using the `linkedClone` type, the disk size matches the clone source instead of using the `diskGiB` value. For more information, see the vSphere documentation about VM clone types. 

`spec.template.spec.datacenter`
     Specifies the vCenter data center to deploy the compute machine set on. 
`spec.template.spec.datastore`
     Specifies the vCenter datastore to deploy the compute machine set on. 
`spec.template.spec.folder`
     Specifies the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`. 
`spec.template.spec.resourcePool`
     Specifies the vSphere resource pool for your VMs. 
`spec.template.spec.network.devices.networkName`
     Specifies the vSphere VM network to deploy the compute machine set to. This VM network must be where other compute machines reside in the cluster. 

#### 11.4.5.1.2. Sample YAML for a Cluster API compute machine set resource on VMware vSphere

The compute machine set resource defines additional properties of the machines that the resource creates. The compute machine set also references the cluster resource and machine template when creating machines. 

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: VSphereMachineTemplate
        name: <template_name>
      failureDomain:
        - name: <failure_domain_name>
          region: <region_a>
          zone: <zone_a>
          server: <vcenter_server_name>
          topology:
            datacenter: <region_a_data_center>
            computeCluster: "</region_a_data_center/host/zone_a_cluster>"
            resourcePool: "</region_a_data_center/host/zone_a_cluster/Resources/resource_pool>"
            datastore: "</region_a_data_center/datastore/datastore_a>"
            networks:
            - port-group
```


where: 

`metadata.name`
     Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`. 
`metadata.labels.cluster.x-k8s.io/cluster-name`
     Specifies the cluster ID as the name of the cluster. 
`spec.clusterName`
     Specifies the cluster ID as the name of the cluster. 
`spec.template.spec.infrastructureRef.kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`spec.template.spec.infrastructureRef.name`
     Specifies the machine template name. 
`spec.template.spec.failureDomain`
     Specifies the failure domain configuration details. 

Note

Using multiple regions and zones on a vSphere cluster that uses the Cluster API is not a validated configuration. 

## 11.4.6. Cluster API configuration options for bare metal

You can change the configuration of your bare metal Cluster API machines by updating values in the Cluster API custom resource manifests. 

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

### 11.4.6.1. Sample YAML for configuring bare metal clusters

The following example YAML files show configurations for a bare metal cluster. 

#### 11.4.6.1.1. Sample YAML for a Cluster API machine template resource on bare metal

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines. 

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: Metal3MachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      customDeploy: install_coreos
      userData:
        name: worker-user-data-managed
```


where: 

`kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`metadata.name`
     Specifies a name for the machine template. 
`spec.template.spec`
     Specifies the details for your environment. The values here are examples. 
`spec.template.spec.userData.name`
     Specifies the Ignition configuration, which the Machine API Operator generates during installation. You must apply the `openshift-cluster-api` namespace to ensure the cluster can access the secret by running the following command: 

```shell-session
$ oc get secret worker-user-data-managed \
  -n openshift-machine-api -o yaml | \
  sed 's/namespace: .*/namespace: openshift-cluster-api/' | oc apply -f -
```


#### 11.4.6.1.2. Sample YAML for a Cluster API compute machine set resource on bare metal

The compute machine set resource defines additional properties of the machines that it creates. The compute machine set also references the cluster resource and machine template when creating machines. 

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/worker: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data-managed
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: Metal3MachineTemplate
        name: <template_name>
```


where: 

`metadata.name`
     Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`. 
`metadata.labels.cluster.x-k8s.io/cluster-name`
     Specifies the cluster ID as the name of the cluster. 
`spec.template.spec.infrastructureRef.kind`
     Specifies the machine template kind. This value must match the value for your platform. 
`spec.template.spec.infrastructureRef.name`
     Specifies the machine template name.
