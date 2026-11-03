# 10.5. Configuration options for control plane machines

## 10.5.1. Control plane configuration options for Amazon Web Services

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 

The following example YAML snippets show provider specification and failure domain configurations for an AWS cluster. 

### 10.5.1.1. Sample AWS provider specification

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification. 

The following example YAML illustrates a valid configuration for an Amazon Web Services (AWS) cluster. 

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates. 

You can omit any field that has a value set in the failure domain section of the CR. 

In the following example, the `<cluster_id>` string is the infrastructure ID. The infrastructure ID matches the cluster ID that the installation program used during cluster provisioning. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command: 

```shell-session
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```


**Sample AWS`providerSpec` values**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            ami:
              id: ami-<ami_id_string>
            apiVersion: machine.openshift.io/v1beta1
            blockDevices:
            - ebs:
                encrypted: true
                iops: 0
                kmsKey:
                  arn: ""
                volumeSize: 120
                volumeType: gp3
            credentialsSecret:
              name: aws-cloud-credentials
            deviceIndex: 0
            iamInstanceProfile:
              id: <cluster_id>-master-profile
            instanceType: m6i.xlarge
            kind: AWSMachineProviderConfig
            loadBalancers:
            - name: <cluster_id>-int
              type: network
            - name: <cluster_id>-ext
              type: network
            metadata:
              creationTimestamp: null
            metadataServiceOptions: {}
            placement:
              region: <region>
              availabilityZone: ""
              tenancy:
            securityGroups:
              - filters:
                - name: tag:Name
                  values:
                  - <cluster_id>-node
              - filters:
                - name: tag:Name
                  values:
                  - <cluster_id>-lb
              - filters:
                - name: tag:Name
                  values:
                  - <cluster_id>-controlplane
            subnet: {}
            userDataSecret:
              name: master-user-data
```


where: 

`<ami_id_string>`
     Specifies the Red Hat Enterprise Linux CoreOS (RHCOS) Amazon Machine Images (AMI) ID for the cluster. The AMI must belong to the same region as the cluster. If you want to use an AWS Marketplace image, you must complete the OpenShift Container Platform subscription from the [AWS Marketplace](https://aws.amazon.com/marketplace/fulfillment?productId=59ead7de-2540-4653-a8b0-fa7926d5c845) to obtain an AMI ID for your region. 
`spec.template.spec.providerSpec.value.blockDevices.ebs`
     Specifies the configuration of an encrypted Amazon Elastic Block Store (Amazon EBS) volume. 
`spec.template.spec.providerSpec.value.credentialsSecret.name`
     Specifies the secret name for the cluster. Do not change this value. 
`spec.template.spec.providerSpec.value.iamInstanceProfile`
     Specifies the AWS Identity and Access Management (IAM) instance profile. Do not change this value. 
`spec.template.spec.providerSpec.value.instanceType`
     Specifies the AWS instance type for the control plane. 
`spec.template.spec.providerSpec.value.kind`
     Specifies the cloud provider platform type. Do not change this value. 
`spec.template.spec.providerSpec.value.loadBalancers`
    

Specifies the internal (`int`) and external (`ext`) load balancers for the cluster. 

Note

You can omit the external (`ext`) load balancer parameters on private OpenShift Container Platform clusters. 

`spec.template.spec.providerSpec.value.placement`
    

Specifies where to create the control plane instance in AWS. The following keys in this stanza specify additional details: 

`region`
     Specifies the AWS region for the cluster. 
`availabilityZone`
     This parameter is in the failure domain configuration and has an empty value here. 

If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain. 

`tenancy`
    

Specifies the AWS Dedicated Instance configuration for the control plane. For more information, see AWS documentation about [Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html). The following values are valid: 

  * `default`: The Dedicated Instance runs on shared hardware. 
  * `dedicated`: The Dedicated Instance runs on single-tenant hardware. 
  * `host`: The Dedicated Instance runs on a Dedicated Host, which is an isolated server with configurations that you can control. 



`spec.template.spec.providerSpec.value.securityGroups`
     Specifies the control plane machines security group. 
`spec.template.spec.providerSpec.value.subnet`
    

This parameter is in the failure domain configuration and has an empty value here. 

If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain. 

Note

If the failure domain configuration does not specify a value, the control plane machines use the value in the provider specification. 

`spec.template.spec.providerSpec.value.userDataSecret`
     Specifies the control plane user data secret. Do not change this value. 

### 10.5.1.2. Sample AWS failure domain configuration

To prevent downtime for your applications due to the failure of a single Amazon Web Services (AWS) region, you can configure failure domains in the control plane machine set by configuring appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` object. 

The control plane machine set concept of a failure domain is analogous to the AWS concept of an [_Availability Zone (AZ)_](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones). The `ControlPlaneMachineSet` CR spreads control plane machines across more than one failure domain when possible. 

When configuring AWS failure domains in the control plane machine set, you must specify the availability zone name and the subnet to use. 

**Sample AWS failure domain values**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        aws:
        - placement:
            availabilityZone: <aws_zone_a>
          subnet:
            filters:
            - name: tag:Name
              values:
              - <cluster_id>-subnet-private-<aws_zone_a>
            type: Filters
        - placement:
            availabilityZone: <aws_zone_b>
          subnet:
            filters:
            - name: tag:Name
              values:
              - <cluster_id>-subnet-private-<aws_zone_b>
            type: Filters
        platform: AWS
# ...
```


where: 

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.placement.availabilityZone: <aws_zone_a>`
     Specifies an AWS availability zone for the first failure domain. 
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet`
     Specifies a subnet configuration. In this example, the subnet type is `Filters`, so there is a `filters` stanza. 
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet.filters.values: <cluster_id>-subnet-private-<aws_zone_a>`
     Specifies the subnet name for the first failure domain, using the infrastructure ID and the AWS availability zone. 
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet.type`
     Specifies the subnet type. The following values are valid: `ARN`, `Filters` and `ID`. The default value is `Filters`. 
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.placement.availabilityZone: <aws_zone_b>`
     Specifies an AWS availability zone for an additional failure domain. 
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet.filters.values: <cluster_id>-subnet-private-<aws_zone_b>`
     Specifies the subnet name for the additional failure domain, using the infrastructure ID and the AWS availability zone. 
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`
     Specifies the cloud provider platform name. Do not change this value. 

### 10.5.1.3. Additional resources

  * [Updating the control plane configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration")
  * [Configuring Amazon Web Services features for control plane machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-supported-features-aws "10.5.2. Configuring Amazon Web Services features for control plane machines")



## 10.5.2. Configuring Amazon Web Services features for control plane machines

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 

### 10.5.2.1. Restrict the API server to private for an Amazon Web Services cluster

If the security posture of your organization does not allow clusters to use an open API endpoint, you can restrict the API server to use only internal load balancers. 

To implement this API server restriction, use the Amazon Web Services (AWS) console and OpenShift CLI (`oc`) to delete the external load balancer components. 

**Prerequisites**

  * You have installed an OpenShift Container Platform cluster on AWS. 
  * You have access to the AWS console as a user with administrator privileges. 
  * You have access to the OpenShift CLI (`oc`) as a user with administrator privileges. 



**Procedure**

  1. Log in to the AWS console as a user with administrator privileges. 
  2. Delete the external load balancer. 

Note

The API DNS entry in the private zone already points to the internal load balancer, which uses an identical configuration, so you do not need to modify the internal load balancer. 

  3. Delete the `api.<cluster_name>.<domain_name>` DNS entry in the public zone. 

where `<cluster_name>` is the name of the cluster and `<domain_name>` is the base domain for the cluster. 

  4. To remove the external load balancers, log in to the OpenShift CLI (`oc`) as a user with administrator privileges. 
  5. Edit the `ControlPlaneMachineSet` CR by running the following command: 

```shell-session
$ oc edit controlplanemachineset.machine.openshift.io cluster \
  -n openshift-machine-api
```


  6. Remove the external load balancers by deleting the corresponding lines in the control plane machine set custom resource (CR). 

In the `spec.template.spec.providerSpec.value.loadBalancers` section of the CR, the `name` value for the external load balancer ends in `-ext`. Delete the line with the external load balancer `name` value and the line with the external load balancer `type` value that accompanies it. 

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            loadBalancers:
            - name: <cluster_id>-ext
              type: network
            - name: <cluster_id>-int
              type: network
# ...
```


  7. Save your changes and exit the object specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 




**Additional resources**

  * [Configuring the Ingress Controller endpoint publishing scope to Internal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ingress_and_load_balancing/#nw-ingresscontroller-change-internal_nw-configuring-ingress-controller-endpoint-publishing-strategy)



### 10.5.2.2. Change the Amazon Web Services instance type by using a control plane machine set

If you need more resources for your control plane machines, you can change the Amazon Web Services (AWS) instance type that they use. To change the instance type, you update the instance type value in the control plane machine set custom resource (CR). 

**Prerequisites**

  * You have access to the OpenShift CLI (`oc`) as a user with administrator privileges. 
  * Your AWS cluster uses a control plane machine set. 



**Procedure**

  1. Edit your control plane machine set CR by running the following command: 

```shell-session
$ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
```


  2. Update the CR to implement your configuration changes: 

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            instanceType: <compatible_aws_instance_type>
```


where `<compatible_aws_instance_type>` specifies a larger AWS instance type with the same base. For example, you can change this value from `m6i.xlarge` to `m6i.2xlarge` or `m6i.4xlarge`. 

  3. Save your changes and exit the object specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. 

     * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration. 
     * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually. 




### 10.5.2.3. Assigning machines to placement groups for Elastic Fabric Adapter instances by using machine sets

You can configure a machine set to deploy machines on Elastic Fabric Adapter (EFA) instances within an existing Amazon Web Services (AWS) placement group. 

[EFA](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) instances do not require placement groups, and you can use placement groups for purposes other than configuring an EFA. This example uses both to demonstrate a configuration that can improve network performance for machines within the specified placement group. 

**Prerequisites**

  * You have access to the OpenShift CLI (`oc`) as a user with administrator privileges. 
  * You created a placement group in the AWS console. 

Note

Ensure that the [rules and limitations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#limitations-placement-groups) for the type of placement group that you create are compatible with your intended use case. The control plane machine set spreads the control plane machines across multiple failure domains when possible. To use placement groups for the control plane, you must use a placement group type that can span multiple Availability Zones. 




**Procedure**

  1. Edit your control plane machine set custom resource (CR) by running the following command: 

```shell-session
$ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
```


  2. Update the CR to implement your configuration changes: 

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            instanceType: <supported_instance_type>
            networkInterfaceType: <interface_type>
            placement:
              availabilityZone: <zone>
              region: <region>
            placementGroupName: <placement_group>
            placementGroupPartition: <placement_group_partition_number>
```


where: 

`<supported_instance_type>`
     Specifies an instance type that [supports EFAs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types). 
`<interface_type>`
     Specifies the network interface type. To use an EFA, set this value to `EFA`. 
`<zone>`
     Specifies the zone; for example, `us-east-1a`. 
`<region>`
     Specifies the region; for example, `us-east-1`. 
`<placement_group>`
     Specifies the name of the existing AWS placement group to deploy machines in. 
`<placement_group_partition_number>`
     Specifies the partition number of the existing AWS placement group to deploy machines in. This parameter is optional. 

  3. Save your changes and exit the object specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. 

     * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration. 
     * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually. 




**Verification**

  * In the AWS console, find a machine that the machine set created and verify the following in the machine properties: 

    * The placement group field has the value that you specified for the `placementGroupName` parameter in the machine set. 
    * If you specified a partition number, the partition number field has the value that you specified for the `placementGroupPartition` parameter in the machine set. 
    * The interface type field indicates that it uses an EFA. 




### 10.5.2.4. Configuring the AWS EC2 Instance Metadata Service by using machine sets

You can use machine sets to create machines that use the version of the Amazon EC2 Instance Metadata Service (IMDS) that meets the security requirements of your organization. 

Machine sets can create machines that allow the use of both IMDSv1 and [IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) or machines that require the use of IMDSv2. 

You can specify whether to require the use of IMDSv2 by adding or editing the value of `metadataServiceOptions.authentication` in the machine set. 

Important

Before configuring a machine set to create machines that require IMDSv2, ensure that any workloads that interact with the AWS metadata service support IMDSv2. 

**Prerequisites**

  * To use IMDSv2, your AWS cluster must have been created with OpenShift Container Platform version 4.7 or later. 



**Procedure**

  1. Edit your control plane machine set custom resource (CR) by running the following command: 

```shell-session
$ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
```


  2. Update the CR to implement your configuration changes: 

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            imetadataServiceOptions:
              authentication: Required
```


To require IMDSv2, set the `metadataServiceOptions.authentication` parameter value to `Required`. To allow the use of both IMDSv1 and IMDSv2, set the parameter value to `Optional`. If you do not specify a value, machines that the machine set creates allow the use of both IMDSv1 and IMDSv2. 

  3. Save your changes and exit the object specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. 

     * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration. 
     * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually. 




**Additional resources**

  * [Boot image management](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/#mco-update-boot-images)



### 10.5.2.5. Configuring storage throughput for gp3 drives

You can improve performance for high traffic services by increasing the throughput of gp3 storage volumes in an AWS cluster. You can configure the storage throughput by editing your compute or control plane machine set. 

**Prerequisites**

  * You use gp3 storage volume(s). 



**Procedure**

  * Add or edit the following lines under the `providerSpec` field in your compute or control plane machine set: 

```yaml
providerSpec:
  value:
    blockDevices:
      - ebs:
          throughputMib: <throughput_value>
```


where: 

`<throughput_value>`
     Specifies a value in MiB per second between 125 and 2,000. You can only edit this value on gp3 volumes. The default value is `125`. 




### 10.5.2.6. Creating Dedicated Instances by using machine sets

You can configure a machine set to deploy machines as Dedicated Instances that run in a virtual private cloud (VPC) on hardware that only a single customer can use. To change use Dedicated Instances, you update the placement tenancy value in the machine set custom resource (CR). 

Amazon Web Services (AWS) Dedicated Instances are EC2 instances that are physically isolated at the host hardware level. This isolation applies to instances that a single payer account owns even if the instances belong to different AWS accounts. 

Public tenancy is the default tenancy. Instances with public tenancy run on shared hardware and can share hardware with Dedicated Instances that belong to the same AWS account. 

**Prerequisites**

  * You have access to the OpenShift CLI (`oc`) as a user with administrator privileges. 



**Procedure**

  1. Edit your control plane machine set custom resource (CR) by running the following command: 

```shell-session
$ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
```


  2. Update the CR to implement your configuration changes: 

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            placement:
              tenancy: dedicated
```


To use Dedicated Instances, set the `placement.tenancy` parameter value to `dedicated`. 

  3. Save your changes and exit the object specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. 

     * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration. 
     * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually. 




### 10.5.2.7. Configure Capacity Reservations by using machine sets

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define by using Capacity Reservations on Amazon Web Services clusters, including On-Demand Capacity Reservations and Capacity Blocks for ML. 

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define. 

These parameters specify the instance type, region, and number of instances that you want to reserve. If your Capacity Reservation can accommodate the capacity request, the deployment succeeds. 

For more information, including limitations and suggested use cases for this Amazon Web Services offering, see [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) in the AWS documentation. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You installed the OpenShift CLI (`oc`). 
  * You have purchased an On-Demand Capacity Reservation or Capacity Block for ML. For more information, see [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) in the AWS documentation. 



**Procedure**

  1. Edit your control plane machine set custom resource (CR) by running the following command: 

```shell-session
$ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
```


  2. Update the CR to implement your configuration changes: 

**Sample configuration**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            capacityReservationId: <capacity_reservation>
            marketType: <market_type>
# ...
```


where: 

`<capacity_reservation>`
     Specifies the ID of the Capacity Block for ML or On-Demand Capacity Reservation that you want the machine set to deploy machines on. 
`<market_type>`
    

Specifies the market type to use. The following values are valid: 

`CapacityBlock`
     Use this market type with Capacity Blocks for ML. 
`OnDemand`
     Use this market type with On-Demand Capacity Reservations. 

  3. Save your changes and exit the object specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. 

     * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration. 
     * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually. 




**Verification**

  * To verify machine deployment, list the machines that the machine set created by running the following command: 

```shell-session
$ oc get machine \
  -n openshift-machine-api \
  -l machine.openshift.io/cluster-api-machine-role=master
```


In the output, verify that the characteristics of the listed machines match the parameters of your Capacity Reservation. 




### 10.5.2.8. Additional resources

  * [Updating the control plane configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration")
  * [Control plane configuration options for Amazon Web Services](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-config-options-aws "10.5.1. Control plane configuration options for Amazon Web Services")



## 10.5.3. Control plane configuration options for Microsoft Azure

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 

The following example YAML snippets show provider specification and failure domain configurations for an Azure cluster. 

### 10.5.3.1. Sample Azure provider specification

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification. 

The following example YAML illustrates a valid configuration for a Microsoft Azure cluster. 

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates. 

You can omit any field that has a value set in the failure domain section of the CR. 

In the following example, the `<cluster_id>` string is the infrastructure ID. The infrastructure ID matches the cluster ID that the installation program used during cluster provisioning. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command: 

```shell-session
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```


**Sample Azure`providerSpec` values**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            acceleratedNetworking: true
            apiVersion: machine.openshift.io/v1beta1
            credentialsSecret:
              name: azure-cloud-credential
              namespace: openshift-machine-api
            diagnostics: {}
            image:
              offer: ""
              publisher: ""
              resourceID: /resourceGroups/<cluster_id>-rg/providers/Microsoft.Compute/galleries/gallery_<cluster_id>/images/<cluster_id>-gen2/versions/412.86.20220930
              sku: ""
              version: ""
            internalLoadBalancer: <cluster_id>-internal
            kind: AzureMachineProviderSpec
            location: <region>
            managedIdentity: <cluster_id>-identity
            metadata:
              creationTimestamp: null
              name: <cluster_id>
            networkResourceGroup: <cluster_id>-rg
            osDisk:
              diskSettings: {}
              diskSizeGB: 1024
              managedDisk:
                storageAccountType: Premium_LRS
              osType: Linux
            publicIP: false
            publicLoadBalancer: <cluster_id>
            resourceGroup: <cluster_id>-rg
            subnet: <cluster_id>-master-subnet
            userDataSecret:
              name: master-user-data
            vmSize: Standard_D8s_v3
            vnet: <cluster_id>-vnet
            zone: "1"
```


where: 

`spec.template.spec.providerSpec.value.credentialsSecret.name`
     Specifies the secret name for the cluster. Do not change this value. 
`spec.template.spec.providerSpec.value.image`
     Specifies the image details for your control plane machine set. 
`spec.template.spec.providerSpec.value.image.resourceID`
     Specifies an image that is compatible with your instance type. The Hyper-V generation V2 images created by the installation program have a `-gen2` suffix, while V1 images have the same name without the suffix. 
`spec.template.spec.providerSpec.value.internalLoadBalancer`
     Specifies the internal load balancer for the control plane. The `ControlPlaneMachineSet` and control plane `Machine` CRs require this field. If the field is empty, specify a valid value. 
`spec.template.spec.providerSpec.value.kind`
     Specifies the cloud provider platform type. Do not change this value. 
`spec.template.spec.providerSpec.value.location`
     Specifies the region to place control plane machines on. 
`spec.template.spec.providerSpec.value.osDisk`
     Specifies the disk configuration for the control plane. 
`spec.template.spec.providerSpec.value.publicLoadBalancer`
    

Specifies the public load balancer for the control plane. 

Note

You can omit the `publicLoadBalancer` parameter on private OpenShift Container Platform clusters that have user-defined outbound routing. 

`spec.template.spec.providerSpec.value.subnet`
     Specifies the subnet for the control plane. 
`spec.template.spec.providerSpec.value.userDataSecret`
     Specifies the control plane user data secret. Do not change this value. 
`spec.template.spec.providerSpec.value.zone`
    

Specifies the zone configuration for clusters that use a single zone for all failure domains. 

Note

If the cluster uses a different zone for each failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using different zones for each failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain. 

### 10.5.3.2. Sample Azure failure domain configuration

To prevent downtime for your applications due to the failure of a single Microsoft Azure region, you can configure failure domains in the control plane machine set by configuring appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` object. 

The control plane machine set concept of a failure domain is analogous to the Azure concept of an [_Azure availability zone_](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/concept-availability-zones). The `ControlPlaneMachineSet` CR spreads control plane machines across more than one failure domain when possible. 

When configuring Azure failure domains in the control plane machine set, you must specify the availability zone name. An Azure cluster can use the following configurations: 

  * One subnet for each availability zone. 
  * One subnet that spans more than one availability zone. 
  * More than one subnet in more than one availability zone. 



**Sample Azure failure domain values**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        azure:
        - zone: "1"
          subnet: <subnet_zone_1>
        - zone: "2"
          subnet: <subnet_zone_2>
        - zone: "3"
          subnet: <subnet_zone_3>
        platform: Azure
# ...
```


where: 

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.azure.zone`
    

Each instance of `zone` specifies an Azure availability zone for a failure domain. 

Note

If the cluster uses a single zone for all failure domains, the `zone` parameter is in the provider specification instead of in the failure domain configuration. 

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.azure.subnet`
     Optional: Specifies the network subnet in which to create the control plane VM. When omitted, the control plane machine set uses the `subnet` value from the machine `providerSpec` template. 
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`
     Specifies the cloud provider platform name. Do not change this value. 

### 10.5.3.3. Additional resources

  * [Updating the control plane configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration")
  * [Configuring Microsoft Azure features for control plane machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-supported-features-azure "10.5.4. Configuring Microsoft Azure features for control plane machines")



## 10.5.4. Configuring Microsoft Azure features for control plane machines

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 

### 10.5.4.1. Restrict the API server to private for an Microsoft Azure cluster

If the security posture of your organization does not allow clusters to use an open API endpoint, you can restrict the API server to use only internal load balancers. To implement this API server restriction, use the Microsoft Azure console to delete the external load balancer component. 

**Prerequisites**

  * You have installed an OpenShift Container Platform cluster on Azure. 
  * You have access to the Azure console as a user with administrator privileges. 



**Procedure**

  1. Log in to the Azure console as a user with administrator privileges. 
  2. Delete the following resources: 

     * The `api-v4` rule for the public load balancer. 
     * The `frontendIPConfiguration` parameter that is associated with the `api-v4` rule for the public load balancer. 
     * The public IP address that is specified in the `frontendIPConfiguration` parameter. 

  3. Configure the Ingress Controller endpoint publishing scope to `Internal`. For more information, see "Configuring the Ingress Controller endpoint publishing scope to Internal". 
  4. Delete the `api.<cluster_name>` DNS entry in the public zone. 

where `<cluster_name>` is the name of the cluster. 




**Additional resources**

  * [Configuring the Ingress Controller endpoint publishing scope to Internal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ingress_and_load_balancing/#nw-ingresscontroller-change-internal_nw-configuring-ingress-controller-endpoint-publishing-strategy)



### 10.5.4.2. Using the Azure Marketplace offering

You can create a machine set running on Azure that deploys machines that use the Azure Marketplace offering. To use this offering, you must first obtain the Azure Marketplace image. When obtaining your image, consider the following: 

  * While the images are the same, the Azure Marketplace publisher is different depending on your region. If you are located in North America, specify `redhat` as the publisher. If you are located in EMEA, specify `redhat-limited` as the publisher. 
  * The offer includes a `rh-ocp-worker` SKU and a `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker` SKU represents a Hyper-V generation version 2 VM image. The default instance types used in OpenShift Container Platform are version 2 compatible. If you plan to use an instance type that is only version 1 compatible, use the image associated with the `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker-gen1` SKU represents a Hyper-V version 1 VM image. 



Important

Installing images with the Azure marketplace is not supported on clusters with 64-bit ARM instances. 

You should only modify the RHCOS image for compute machines to use an Azure Marketplace image. Control plane machines and infrastructure nodes do not require an OpenShift Container Platform subscription and use the public RHCOS default image by default, which does not incur subscription costs on your Azure bill. Therefore, you should not modify the cluster default boot image or the control plane boot images. Applying the Azure Marketplace image to them will incur additional licensing costs that cannot be recovered. 

**Prerequisites**

  * You have installed the Azure CLI client `(az)`. 
  * Your Azure account is entitled for the offer and you have logged into this account with the Azure CLI client. 



**Procedure**

  1. Display all of the available OpenShift Container Platform images by running one of the following commands: 

     * North America: 

```shell-session
$  az vm image list --all --offer rh-ocp-worker --publisher redhat -o table
```


**Example output**

```shell-session
Offer          Publisher       Sku                 Urn                                                             Version
-------------  --------------  ------------------  --------------------------------------------------------------  -----------------
rh-ocp-worker  RedHat          rh-ocp-worker       RedHat:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
rh-ocp-worker  RedHat          rh-ocp-worker-gen1  RedHat:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
```


     * EMEA: 

```shell-session
$  az vm image list --all --offer rh-ocp-worker --publisher redhat-limited -o table
```


**Example output**

```shell-session
Offer          Publisher       Sku                 Urn                                                                     Version
-------------  --------------  ------------------  --------------------------------------------------------------          -----------------
rh-ocp-worker  redhat-limited  rh-ocp-worker       redhat-limited:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
rh-ocp-worker  redhat-limited  rh-ocp-worker-gen1  redhat-limited:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
```


Note

Use the latest image that is available for compute and control plane nodes. If required, your VMs are automatically upgraded as part of the installation process. 

  2. Inspect the image for your offer by running one of the following commands: 

     * North America: 

```shell-session
$ az vm image show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
```


     * EMEA: 

```shell-session
$ az vm image show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
```


  3. Review the terms of the offer by running one of the following commands: 

     * North America: 

```shell-session
$ az vm image terms show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
```


     * EMEA: 

```shell-session
$ az vm image terms show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
```


  4. Accept the terms of the offering by running one of the following commands: 

     * North America: 

```shell-session
$ az vm image terms accept --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
```


     * EMEA: 

```shell-session
$ az vm image terms accept --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
```


  5. Record the image details of your offer, specifically the values for `publisher`, `offer`, `sku`, and `version`. 
  6. Add the following parameters to the `providerSpec` section of your machine set YAML file using the image details for your offer: 

**Sample`providerSpec` image values for Azure Marketplace machines**

```yaml
providerSpec:
  value:
    image:
      offer: rh-ocp-worker
      publisher: redhat
      resourceID: ""
      sku: rh-ocp-worker
      type: MarketplaceWithPlan
      version: 413.92.2023101700
```


### 10.5.4.3. Enabling Microsoft Azure boot diagnostics

You can enable boot diagnostics on Microsoft Azure machines that your machine set creates. Use this to store console logs that you can use to troubleshoot why a node fails to boot. 

**Prerequisites**

  * Have an existing Azure cluster. 



**Procedure**

  * Add the `diagnostics` configuration that is applicable to your storage type to the `providerSpec` field in your machine set YAML file: 

    * For an Azure Managed storage account: 

```yaml
providerSpec:
  value:
    diagnostics:
      boot:
        storageAccountType: <azure_managed>
```


where: 

`<azure_managed>`
     Specifies an Azure Managed storage account. 

    * For an Azure Unmanaged storage account: 

```yaml
providerSpec:
  value:
    diagnostics:
      boot:
        storageAccountType: <customer_managed>
        customerManaged:
          storageAccountURI: <https://<storage_account>.blob.core.windows.net>
```


where: 

`<customer_managed>`
     Specifies an Azure Unmanaged storage account. 
`https://<storage_account>.blob.core.windows.net`
     Specifies the storage account URL. Replace `<storage_account>` with the name of your storage account. 

Note

Only the Azure Blob Storage data service is supported. 




**Verification**

  * On the Azure portal, review the **Boot diagnostics** page for a machine deployed by the machine set, and verify that you can see the serial logs for the machine. 



### 10.5.4.4. Machine sets that deploy machines with ultra disks as data disks

You can create a machine set running on Microsoft Azure that deploys machines with ultra disks. Ultra disks are high-performance storage that are intended for use with the most demanding data workloads. 

**Additional resources**

  * [Microsoft Azure ultra disks documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/disks-types#ultra-disks)



#### 10.5.4.4.1. Creating machines with ultra disks by using machine sets

You can deploy machines with ultra disks on Microsoft Azure by editing your machine set YAML file. 

**Prerequisites**

  * Have an existing Microsoft Azure cluster. 



**Procedure**

  1. Create a custom secret in the `openshift-machine-api` namespace by using the `master` data secret by running the following command: 

```shell-session
$ oc -n openshift-machine-api \
get secret <role>-user-data \
--template='{{index .data.userData | base64decode}}' | jq > userData.txt
```


where: 

`<role>`
     Replace with `master`. 
`userData.txt`
     Specifies `userData.txt` as the name of the new custom secret. 

  2. In a text editor, open the `userData.txt` file and locate the final `}` character in the file. 

     1. On the immediately preceding line, add a `,`. 
     2. Create a new line after the `,` and add the following configuration details: 

```plaintext
"storage": {
  "disks": [
    {
      "device": "/dev/disk/azure/scsi1/lun0",
      "partitions": [
        {
          "label": "lun0p1",
          "sizeMiB": 1024,
          "startMiB": 0
        }
      ]
    }
  ],
  "filesystems": [
    {
      "device": "/dev/disk/by-partlabel/lun0p1",
      "format": "xfs",
      "path": "/var/lib/lun0p1"
    }
  ]
},
"systemd": {
  "units": [
    {
      "contents": "[Unit]\nBefore=local-fs.target\n[Mount]\nWhere=/var/lib/lun0p1\nWhat=/dev/disk/by-partlabel/lun0p1\nOptions=defaults,pquota\n[Install]\nWantedBy=local-fs.target\n",
      "enabled": true,
      "name": "var-lib-lun0p1.mount"
    }
  ]
}
```


where: 

`"disks"`
     Specifies the configuration details for the disk that you want to attach to a node as an ultra disk. 
`"device"`
     Specifies the `lun` value that is defined in the `dataDisks` stanza of the machine set you are using. For example, if the machine set contains `lun: 0`, specify `lun0`. You can initialize multiple data disks by specifying multiple `"disks"` entries in this configuration file. If you specify multiple `"disks"` entries, ensure that the `lun` value for each matches the value in the machine set. 
`"partitions"`
     Specifies the configuration details for a new partition on the disk. 
`"label"`
     Specifies a label for the partition. You might find it helpful to use hierarchical names, such as `lun0p1` for the first partition of `lun0`. 
`"sizeMiB"`
     Specifies the total size in MiB of the partition. 
`"filesystems"`
     Specifies the filesystem to use when formatting a partition. Use the partition label to specify the partition. 
`"units"`
     Specifies a `systemd` unit to mount the partition at boot. Use the partition label to specify the partition. You can create multiple partitions by specifying multiple `"partitions"` entries in this configuration file. If you specify multiple `"partitions"` entries, you must specify a `systemd` unit for each. 
`"contents"`
     Specifies the value of `storage.filesystems.path` for `Where`. Specifies the value of `storage.filesystems.device` for `What`. 

  3. Extract the disabling template value to a file called `disableTemplating.txt` by running the following command: 

```shell-session
$ oc -n openshift-machine-api get secret <role>-user-data \
--template='{{index .data.disableTemplating | base64decode}}' | jq > disableTemplating.txt
```


Replace `<role>` with `master`. 

  4. Combine the `userData.txt` file and `disableTemplating.txt` file to create a data secret file by running the following command: 

```shell-session
$ oc -n openshift-machine-api create secret generic <role>-user-data-x5 \
--from-file=userData=userData.txt \
--from-file=disableTemplating=disableTemplating.txt
```


For `<role>-user-data-x5`, specify the name of the secret. Replace `<role>` with `master`. 

  5. Edit your control plane machine set CR by running the following command: 

```shell-session
$ oc --namespace openshift-machine-api edit controlplanemachineset.machine.openshift.io cluster
```


  6. Add the following lines in the positions indicated: 

```yaml
apiVersion: machine.openshift.io/v1beta1
kind: ControlPlaneMachineSet
spec:
  template:
    spec:
      metadata:
        labels:
          disk: ultrassd
      providerSpec:
        value:
          ultraSSDCapability: Enabled
          dataDisks:
          - nameSuffix: ultrassd
            lun: 0
            diskSizeGB: 4
            deletionPolicy: Delete
            cachingType: None
            managedDisk:
              storageAccountType: UltraSSD_LRS
          userDataSecret:
            name: <role>-user-data-x5
```


where: 

`spec.template.spec.metadata.labels.disk`
     Specifies a label to use to select a node that is created by this machine set. The example uses `disk.ultrassd` for this value. 
`spec.template.spec.providerSpec.value.ultraSSDCapability`
     Enables the use of ultra disks. For `dataDisks`, include the entire stanza. 
`spec.template.spec.providerSpec.value.userDataSecret.name`
     Specifies the user data secret created earlier. Replace `<role>` with `master`. 

  7. Save your changes. 

     * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration. 
     * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually. 




**Verification**

  1. Validate that the machines are created by running the following command: 

```shell-session
$ oc get machines
```


The machines should be in the `Running` state. 

  2. For a machine that is running and has a node attached, validate the partition by running the following command: 

```shell-session
$ oc debug node/<node_name> -- chroot /host lsblk
```


In this command, `oc debug node/<node_name>` starts a debugging shell on the node `<node_name>` and passes a command with `--`. The passed command `chroot /host` provides access to the underlying host OS binaries, and `lsblk` shows the block devices that are attached to the host OS machine. 




**Next steps**

  * To use an ultra disk on the control plane, reconfigure your workload to use the control plane’s ultra disk mount point. 



#### 10.5.4.4.2. Troubleshooting resources for machine sets that enable ultra disks

You can recover from issues that you might encounter when you enable ultra disks for machine sets. Review fields, such as disk settings, and ensure that the parameters are correctly configured. 

##### 10.5.4.4.2.1. Incorrect ultra disk configuration

If an incorrect configuration of the `ultraSSDCapability` parameter is specified in the machine set, the machine provisioning fails. 

For example, if the `ultraSSDCapability` parameter is set to `Disabled`, but an ultra disk is specified in the `dataDisks` parameter, the following error message appears: 

```shell-session
StorageAccountType UltraSSD_LRS can be used only when additionalCapabilities.ultraSSDEnabled is set.
```


  * To resolve this issue, verify that your machine set configuration is correct. 



##### 10.5.4.4.2.2. Unsupported disk parameters

If a region, availability zone, or instance size that is not compatible with ultra disks is specified in the machine set, the machine provisioning fails. Check the logs for the following error message: 

```shell-session
failed to create vm <machine_name>: failure sending request for machine <machine_name>: cannot create vm: compute.VirtualMachinesClient#CreateOrUpdate: Failure sending request: StatusCode=400 -- Original Error: Code="BadRequest" Message="Storage Account type 'UltraSSD_LRS' is not supported <more_information_about_why>."
```


  * To resolve this issue, verify that you are using this feature in a supported environment and that your machine set configuration is correct. 



##### 10.5.4.4.2.3. Unable to delete disks

If the deletion of ultra disks as data disks is not working as expected, the machines are deleted and the data disks are orphaned. You must delete the orphaned disks manually if desired. 

### 10.5.4.5. Enable customer-managed encryption keys for a machine set on Azure

To enhance data security, enable customer-managed encryption on Microsoft Azure by adding the disk encryption set ID to your machine set. 

You can supply an encryption key to Azure to encrypt data on managed disks at rest. You can enable server-side encryption with customer-managed keys by using the Machine API. 

An Azure Key Vault, a disk encryption set, and an encryption key are required to use a customer-managed key. The disk encryption set must be in a resource group where the Cloud Credential Operator (CCO) has granted permissions. If not, an additional reader role is required to be granted on the disk encryption set. 

**Prerequisites**

  * [You created an Azure Key Vault instance (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#create-an-azure-key-vault-instance). 
  * [You created an instance of a disk encryption set (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#create-an-instance-of-a-diskencryptionset). 
  * [You granted the disk encryption set access to key vault (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#grant-the-diskencryptionset-access-to-key-vault). 



**Procedure**

  * Configure the disk encryption set under the `providerSpec` field in your machine set YAML file. For example: 

```yaml
providerSpec:
  value:
    osDisk:
      diskSizeGB: 128
      managedDisk:
        diskEncryptionSet:
          id: /subscriptions/<subscription_id>/resourceGroups/<resource_group_name>/providers/Microsoft.Compute/diskEncryptionSets/<disk_encryption_set_name>
        storageAccountType: Premium_LRS
```


**Additional resources**

  * [Customer-managed keys (Azure documentation)](https://docs.microsoft.com/en-us/azure/virtual-machines/disk-encryption#customer-managed-keys)



### 10.5.4.6. Configuring trusted launch for Azure virtual machines by using machine sets

By editing the machine set YAML file, you can configure the trusted launch for Microsoft Azure virtual machines (VMs) options that a machine set uses for machines that it deploys. 

For example, you can configure these machines to use UEFI security features such as Secure Boot or a dedicated virtual Trusted Platform Module (vTPM) instance. 

Note

Some feature combinations result in an invalid configuration. 

Table 10.2. UEFI feature combination compatibilitySecure Boot[1]| vTPM[2]| Valid configuration  
---|---|---  
Enabled  |  Enabled  |  Yes   
Enabled  |  Disabled  |  Yes   
Enabled  |  Omitted  |  Yes   
Disabled  |  Enabled  |  Yes   
Omitted  |  Enabled  |  Yes   
Disabled  |  Disabled  |  No   
Omitted  |  Disabled  |  No   
Omitted  |  Omitted  |  No   
Show more

  1. Using the `secureBoot` field. 
  2. Using the `virtualizedTrustedPlatformModule` field. 



For more information about related features and functionality, see the Microsoft Azure documentation about [Trusted launch for Azure virtual machines](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch). 

**Procedure**

  1. In a text editor, open the YAML file for an existing machine set or create a new one. 
  2. Edit the following section under the `providerSpec` field to provide a valid configuration: 

**Sample valid configuration with UEFI Secure Boot and vTPM enabled**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            securityProfile:
              settings:
                securityType: TrustedLaunch
                trustedLaunch:
                  uefiSettings:
                    secureBoot: Enabled
                    virtualizedTrustedPlatformModule: Enabled
# ...
```


where: 

`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.securityType`
     Enables the use of trusted launch for Azure virtual machines. This value is required for all valid configurations. 
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings`
     Specifies which UEFI security features to use. This section is required for all valid configurations. 
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings.secureBoot`
     Enables UEFI Secure Boot. 
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings.virtualizedTrustedPlatformModule`
     Enables the use of a vTPM. 




**Verification**

  * On the Microsoft Azure portal, review the details for a machine deployed by the machine set and verify that the trusted launch options match the values that you configured. 



### 10.5.4.7. Configure Azure confidential virtual machines by using machine sets

You can enable Microsoft Azure confidential virtual machines (VMs) to use memory encryption to improve data confidentiality. 

Note

Confidential VMs are currently not supported on 64-bit ARM architectures. 

By editing the machine set YAML file, you can configure the confidential VM options that a machine set uses for machines that it deploys. For example, you can configure these machines to use UEFI security features such as Secure Boot or a dedicated virtual Trusted Platform Module (vTPM) instance. 

Warning

Not all instance types support confidential VMs. Do not change the instance type for a control plane machine set that is configured to use confidential VMs to a type that is incompatible. Using an incompatible instance type can cause your cluster to become unstable. 

For more information about related features and functionality, see the Microsoft Azure documentation about [Confidential virtual machines](https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview). 

**Procedure**

  1. In a text editor, open the YAML file for an existing machine set or create a new one. 
  2. Edit the following section under the `providerSpec` field: 

**Sample configuration**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    spec:
      providerSpec:
        value:
          osDisk:
            # ...
            managedDisk:
              securityProfile:
                securityEncryptionType: VMGuestStateOnly
            # ...
          securityProfile:
            settings:
                securityType: ConfidentialVM
                confidentialVM:
                  uefiSettings:
                    secureBoot: Disabled
                    virtualizedTrustedPlatformModule: Enabled
          vmSize: Standard_DC16ads_v5
# ...
```


where: 

`spec.template.spec.providerSpec.value.osDisk.managedDisk.securityProfile`
     Specifies security profile settings for the managed disk when using a confidential VM. 
`spec.template.spec.providerSpec.value.osDisk.managedDisk.securityProfile.securityEncryptionType`
     Enables encryption of the Microsoft Azure VM Guest State (VMGS) blob. This setting requires the use of vTPM. 
`spec.template.spec.providerSpec.value.securityProfile`
     Specifies security profile settings for the confidential VM. 
`spec.template.spec.providerSpec.value.securityProfile.settings.securityType`
     Enables the use of confidential VMs. This value is required for all valid configurations. 
`spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings`
     Specifies which UEFI security features to use. This section is required for all valid configurations. 
`spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings.secureBoot`
     Disables UEFI Secure Boot. 
`spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings.virtualizedTrustedPlatformModule`
     Enables the use of a vTPM. 
`spec.template.spec.providerSpec.value.vmSize`
     Specifies an instance type that supports confidential VMs. 




**Verification**

  * On the Microsoft Azure portal, review the details for a machine deployed by the machine set and verify that the confidential VM options match the values that you configured. 



### 10.5.4.8. Configure Capacity Reservations by using machine sets

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define by using on-demand Capacity Reservation with Capacity Reservation groups on Microsoft Azure clusters. 

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define. 

These parameters specify the VM size, region, and number of instances that you want to reserve. If your Azure subscription quota can accommodate the capacity request, the deployment succeeds. 

For more information, including limitations and suggested use cases for this Microsoft Azure offering, see [On-demand Capacity Reservation](https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-overview) in the Azure documentation. 

Note

You cannot change an existing Capacity Reservation configuration for a machine set. To use a different Capacity Reservation group, you must replace the machine set and the machines that the previous machine set deployed. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You installed the OpenShift CLI (`oc`). 
  * You have created a Capacity Reservation group. For more information, see [Create a Capacity Reservation](https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-create) in the Microsoft Azure documentation. 



**Procedure**

  1. Edit your control plane machine set custom resource (CR) by running the following command: 

```shell-session
$ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
```


  2. Update the CR to implement your configuration changes: 

**Sample configuration**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            capacityReservationGroupID: <capacity_reservation_group>
# ...
```


where: 

`<capacity_reservation_group>`
     Specifies the ID of the Capacity Reservation group that you want the machine set to deploy machines on. 

  3. Save your changes and exit the object specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. 

     * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration. 
     * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually. 




**Verification**

  * To verify machine deployment, list the machines that the machine set created by running the following command: 

```shell-session
$ oc get machine \
  -n openshift-machine-api \
  -l machine.openshift.io/cluster-api-machine-role=master
```


In the output, verify that the characteristics of the listed machines match the parameters of your Capacity Reservation. 




### 10.5.4.9. Accelerated Networking for Microsoft Azure VMs

You can enable Accelerated Networking, which uses single root I/O virtualization (SR-IOV) to provide Microsoft Azure VMs with a more direct path to the switch, after installation. This enhances network performance. 

#### 10.5.4.9.1. Limitations

Consider the following limitations when deciding whether to use Accelerated Networking: 

  * Accelerated Networking is only supported on clusters where the Machine API is operational. 
  * Accelerated Networking requires an Azure VM size that includes at least four vCPUs. To satisfy this requirement, you can change the value of `vmSize` in your machine set. For information about Azure VM sizes, see [Microsoft Azure documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/sizes). 




#### 10.5.4.9.2. Enabling Accelerated Networking on an existing Microsoft Azure cluster

You can enable Accelerated Networking on Microsoft Azure by adding `acceleratedNetworking` to your machine set YAML file. Accelerated Networking uses SR-IOV to help improve network performance for new nodes. 

**Prerequisites**

  * Have an existing Azure cluster where the Machine API is operational. 



**Procedure**

  * Add the following to the `providerSpec` field: 

```yaml
providerSpec:
  value:
    acceleratedNetworking: true
    vmSize: <azure-vm-size>
```


where: 

`providerSpec.value.acceleratedNetworking`
     Enables Accelerated Networking. 
`providerSpec.value.vmSize`
     Specifies an Azure VM size that includes at least four vCPUs. For information about VM sizes, see the Microsoft Azure documentation [Sizes for virtual machines in Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/sizes). 




**Verification**

  * On the Microsoft Azure portal, review the **Networking** settings page for a machine provisioned by the machine set, and verify that the `Accelerated networking` field is set to `Enabled`. 



### 10.5.4.10. Additional resources

  * [Updating the control plane configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration")
  * [Control plane configuration options for Microsoft Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-config-options-azure "10.5.3. Control plane configuration options for Microsoft Azure")



## 10.5.5. Control plane configuration options for Google Cloud

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 

The following example YAML snippets show provider specification and failure domain configurations for a Google Cloud cluster. 

### 10.5.5.1. Sample Google Cloud provider specification

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification. 

The following example YAML illustrates a valid configuration for an Google Cloud cluster. 

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates. 

You can omit any field that has a value set in the failure domain section of the CR. 

In the following example, you can obtain some of the values for your cluster by using the OpenShift CLI (`oc`). 

Infrastructure ID
    

The `<cluster_id>` string is the infrastructure ID. The infrastructure ID matches the cluster ID that the installation program used during cluster provisioning. If you have `oc` installed, you can obtain the infrastructure ID by running the following command: 

```shell-session
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```


Image path
    

The `<path_to_image>` string is the path to the source image for the disk. If you have `oc` installed, you can obtain the path to the image by running the following command: 

```shell-session
$ oc -n openshift-machine-api \
  -o jsonpath='{.spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.disks[0].image}{"\n"}' \
  get ControlPlaneMachineSet/cluster
```


**Sample Google Cloud`providerSpec` values**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            apiVersion: machine.openshift.io/v1beta1
            canIPForward: false
            credentialsSecret:
              name: gcp-cloud-credentials
            deletionProtection: false
            disks:
            - autoDelete: true
              boot: true
              image: <path_to_image>
              labels: null
              sizeGb: 200
              type: pd-ssd
            kind: GCPMachineProviderSpec
            machineType: e2-standard-4
            metadata:
              creationTimestamp: null
            metadataServiceOptions: {}
            networkInterfaces:
            - network: <cluster_id>-network
              subnetwork: <cluster_id>-master-subnet
            projectID: <project_name>
            region: <region>
            serviceAccounts:
            - email: <cluster_id>-m@<project_name>.iam.gserviceaccount.com
              scopes:
              - https://www.googleapis.com/auth/cloud-platform
            shieldedInstanceConfig: {}
            tags:
            - <cluster_id>-master
            targetPools:
            - <cluster_id>-api
            userDataSecret:
              name: master-user-data
            zone: ""
```


where: 

`spec.template.spec.providerSpec.value.credentialsSecret.name`
     Specifies the secret name for the cluster. Do not change this value. 
`spec.template.spec.providerSpec.value.disk.image`
    

Specifies the path to the source image for the disk. 

To use a Google Cloud Marketplace image, specify the offer to use: 

  * OpenShift Container Platform: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-ocp-413-x86-64-202305021736`
  * OpenShift Platform Plus: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-opp-413-x86-64-202305021736`
  * OpenShift Kubernetes Engine: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-oke-413-x86-64-202305021736`



`spec.template.spec.providerSpec.value.kind`
     Specifies the cloud provider platform type. Do not change this value. 
`spec.template.spec.providerSpec.value.projectID`
     Specifies the name of the Google Cloud project that you use for your cluster. 
`spec.template.spec.providerSpec.value.projectID.region`
     Specifies the Google Cloud region for the cluster. 
`spec.template.spec.providerSpec.value.serviceAccounts`
     Specifies a single service account. Specifying more than one service account is not supported. 
`spec.template.spec.providerSpec.value.userDataSecret`
     Specifies the control plane user data secret. Do not change this value. 
`spec.template.spec.providerSpec.value.zone`
    

This parameter is in the failure domain configuration and has an empty value here. 

If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain. 

### 10.5.5.2. Sample Google Cloud failure domain configuration

To prevent downtime for your application due to the failure of a single Google Cloud region, you can configure failure domains in the control plane machine set by configuring appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` object. 

The control plane machine set concept of a failure domain is analogous to the existing Google Cloud concept of a [_zone_](https://cloud.google.com/compute/docs/regions-zones). The `ControlPlaneMachineSet` CR spreads control plane machines across more than one failure domain when possible. 

When configuring Google Cloud failure domains in the control plane machine set, you must specify the zone name to use. 

**Sample Google Cloud failure domain values**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        gcp:
        - zone: <gcp_zone_a>
        - zone: <gcp_zone_b>
        - zone: <gcp_zone_c>
        - zone: <gcp_zone_d>
        platform: GCP
# ...
```


where: 

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.gcp.zone`
     Each instance of `zone` specifies a Google Cloud zone for a failure domain. 
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`
     Specifies the cloud provider platform name. Do not change this value. 

### 10.5.5.3. Additional resources

  * [Updating the control plane configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration")
  * [Configuring Google Cloud features for control plane machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-supported-features-gcp "10.5.6. Configuring Google Cloud features for control plane machines")



## 10.5.6. Configuring Google Cloud features for control plane machines

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 

### 10.5.6.1. Configuring persistent disk types by using machine sets

Configure the persistent disk type for your machine set on Google Cloud to match your workload requirements. Editing the `MachineSet` YAML file allows you to choose between standard, balanced, or SSD persistent disks. 

For more information about persistent disk types, compatibility, regional availability, and limitations, see the Google Cloud Compute Engine documentation about [persistent disks](https://cloud.google.com/compute/docs/disks#pdspecs). 

**Procedure**

  1. In a text editor, open the YAML file for an existing machine set or create a new one. 
  2. Edit the following line under the `providerSpec` field: 

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
...
spec:
  template:
    spec:
      providerSpec:
        value:
          disks:
            type: pd-ssd
```


where: 

`spec.template.spec.providerSpec.value.disks.type`
     Uses the `pd-ssd` disk type for control plane nodes. Using the `pd-ssd` disk type is required for control plane nodes. 




**Verification**

  * Using the Google Cloud console, review the details for a machine deployed by the machine set and verify that the `Type` field matches the configured disk type. 



### 10.5.6.2. Configure Confidential VM by using machine sets on Google Cloud

You create machine sets to scale clusters on Google Cloud. By editing the machine set YAML file, you can configure the Confidential VM options that a machine set uses for machines that it deploys. 

For more information about Confidential VM features, functions, and compatibility, see the Google Cloud Compute Engine documentation about [Confidential VM](https://cloud.google.com/confidential-computing/confidential-vm/docs/about-cvm#confidential-vm). 

Note

Confidential VMs are currently not supported on 64-bit ARM architectures. If you use Confidential VM, you must ensure that you select a supported region. For details on supported regions and configurations, see the Google Cloud Compute Engine documentation about [supported zones](https://cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones). 

**Procedure**

  1. In a text editor, open the YAML file for an existing machine set or create a new one. 
  2. Edit the following section under the `providerSpec` field: 

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            confidentialCompute: Enabled
            onHostMaintenance: Terminate
            machineType: n2d-standard-8
# ...
```


where: 

`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.confidentialCompute`
     Specifies whether Confidential VM is enabled. The following values are valid: 
`Enabled`
    

Enables Confidential VM with a default selection of Confidential VM technology. The default selection is AMD Secure Encrypted Virtualization (AMD SEV). 

Important

The `Enabled` value selects Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV), which is deprecated. 

`Disabled`
     Disables Confidential VM. 
`AMDEncryptedVirtualizationNestedPaging`
     Enables Confidential VM using AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). AMD SEV-SNP supports n2d machines. 
`AMDEncryptedVirtualization`
    

Enables Confidential VM using AMD SEV. AMD SEV supports c2d, n2d, and c3d machines. 

Important

The use of Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV) has been deprecated and will be removed in a future release. 

`IntelTrustedDomainExtensions`
     Enables Confidential VM using Intel Trusted Domain Extensions (Intel TDX). Intel TDX supports n2d machines. 
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.onHostMaintenance`
     Specifies the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VM does not support live VM migration. 
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.machineType`
     Specifies a machine type that supports the Confidential VM option that you specified in the `confidentialCompute` field. 




**Verification**

  * On the Google Cloud console, review the details for a machine deployed by the machine set and verify that the Confidential VM options match the values that you configured. 



### 10.5.6.3. Configuring Shielded VM options by using machine sets on Google Cloud

To help secure your cluster instances, you can configure Shielded Virtual Machine (VM) options for your machine sets on Google Cloud by editing the `MachineSet` YAML file. 

For more information about Shielded VM features and functionality, see the Google Cloud Compute Engine documentation about [Shielded VM](https://cloud.google.com/compute/shielded-vm/docs/shielded-vm). 

**Procedure**

  1. In a text editor, open the YAML file for an existing machine set or create a new one. 
  2. Edit the following section under the `providerSpec` field: 

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    spec:
      providerSpec:
        value:
          shieldedInstanceConfig:
            integrityMonitoring: Enabled
            secureBoot: Disabled
            virtualizedTrustedPlatformModule: Enabled
# ...
```


where: 

`spec.template.spec.providerSpec.value.shieldedInstanceConfig`
     Specifies the Shielded VM configuration. 
`spec.template.spec.providerSpec.value.shieldedInstanceConfig.integrityMonitoring`
    

Specifies whether integrity monitoring is enabled. Valid values are `Disabled` or `Enabled`. 

Note

When integrity monitoring is enabled, you must not disable virtual trusted platform module (vTPM). 

`spec.template.spec.providerSpec.value.shieldedInstanceConfig.secureBoot`
     Specifies whether UEFI Secure Boot is enabled. Valid values are `Disabled` or `Enabled`. 
`spec.template.spec.providerSpec.value.shieldedInstanceConfig.virtualizedTrustedPlatformModule`
     Specifies whether vTPM is enabled. Valid values are `Disabled` or `Enabled`. 




**Verification**

  * Using the Google Cloud console, review the details for a machine deployed by the machine set and verify that the Shielded VM options match the values that you configured. 



**Additional resources**

  * [What is Shielded VM? (Google Cloud documentation)](https://cloud.google.com/compute/shielded-vm/docs/shielded-vm)
  * [Secure Boot (Google Cloud documentation)](https://cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot)
  * [Virtual Trusted Platform Module (vTPM) (Google Cloud documentation)](https://cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm)
  * [Integrity monitoring (Google Cloud documentation)](https://cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring)



### 10.5.6.4. Enable customer-managed encryption keys for a machine set on Google Cloud Compute Engine

Use Google Cloud Compute Engine to supply an encryption key to encrypt data on disks at rest. The key is used to encrypt the data encryption key, not to encrypt the customer’s data. By default, Compute Engine encrypts this data by using Compute Engine keys. 

You can enable encryption with a customer-managed key in clusters that use the Machine API. You must first [create a KMS key](https://cloud.google.com/compute/docs/disks/customer-managed-encryption#before_you_begin) and assign the correct permissions to a service account. The KMS key name, key ring name, and location are required to allow a service account to use your key. 

Note

If you do not want to use a dedicated service account for the KMS encryption, the Compute Engine default service account is used instead. You must grant the default service account permission to access the keys if you do not use a dedicated service account. The Compute Engine default service account name follows the `service-<project_number>@compute-system.iam.gserviceaccount.com` pattern. 

**Procedure**

  1. To allow a specific service account to use your KMS key and to grant the service account the correct IAM role, run the following command with your KMS key name, key ring name, and location: 

```shell-session
$ gcloud kms keys add-iam-policy-binding <key_name> \
  --keyring <key_ring_name> \
  --location <key_ring_location> \
  --member "serviceAccount:service-<project_number>@compute-system.iam.gserviceaccount.com” \
  --role roles/cloudkms.cryptoKeyEncrypterDecrypter
```


  2. Configure the encryption key under the `providerSpec` field in your machine set YAML file. For example: 

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
...
spec:
  template:
    spec:
      providerSpec:
        value:
          disks:
          - type:
            encryptionKey:
              kmsKey:
                name: machine-encryption-key
                keyRing: openshift-encryption-ring
                location: global
                projectID: openshift-gcp-project
              kmsKeyServiceAccount: openshift-service-account@openshift-gcp-project.iam.gserviceaccount.com
```


where: 

`spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.name`
     Specifies the name of the customer-managed encryption key that is used for the disk encryption. 
`spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.keyRing`
     Specifies the name of the KMS key ring that the KMS key belongs to. 
`spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.location`
     Specifies the Google Cloud location in which the KMS key ring exists. 
`spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.projectID`
     Optional: Specifies the ID of the project in which the KMS key ring exists. If a project ID is not set, the machine set `projectID` in which the machine set was created is used. 
`spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKeyServiceAccount`
    

Optional: Specifies the service account that is used for the encryption request for the given KMS key. If a service account is not set, the Compute Engine default service account is used. 

When a new machine is created by using the updated `providerSpec` object configuration, the disk encryption key is encrypted with the KMS key. 




### 10.5.6.5. Additional resources

  * [Updating the control plane configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration")
  * [Control plane configuration options for Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-config-options-gcp "10.5.5. Control plane configuration options for Google Cloud")



## 10.5.7. Control plane configuration options for Nutanix

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 

The following example YAML snippets show provider specification and failure domain configurations for a Nutanix cluster. 

### 10.5.7.1. Sample Nutanix provider specification

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification. 

The following example YAML illustrates a valid configuration for a Nutanix cluster. 

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates. 

In the following example, the `<cluster_id>` string is the infrastructure ID. The infrastructure ID matches the cluster ID that the installation program used during cluster provisioning. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command: 

```shell-session
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```


**Sample Nutanix`providerSpec` values**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
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
              name: <cluster_id>-rhcos
              type: name
            kind: NutanixMachineProviderConfig
            memorySize: 16Gi
            metadata:
              creationTimestamp: null
            project:
              type: name
              name: <project_name>
            subnets:
            - type: uuid
              uuid: <subnet_uuid>
            systemDiskSize: 120Gi
            userDataSecret:
              name: master-user-data
            vcpuSockets: 8
            vcpusPerSocket: 1
```


where: 

`spec.template.spec.providerSpec.value.bootType`
    

Specifies the boot type that the control plane machines use. For more information about boot types, see [Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment (Nutanix documentation)](https://portal.nutanix.com/page/documents/kbs/details?targetId=kA07V000000H3K9SAK). 

Valid values are `Legacy`, `SecureBoot`, or `UEFI`. The default is `Legacy`. 

Note

You must use the `Legacy` boot type in OpenShift Container Platform 4.22. 

`spec.template.spec.providerSpec.value.categories`
     Specifies one or more Nutanix Prism categories to apply to control plane machines. This stanza requires `key` and `value` parameters for a category key-value pair that exists in Prism Central. For more information about categories, see [Category management](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_6:ssp-ssp-categories-manage-pc-c.html). 
`spec.template.spec.providerSpec.value.cluster`
    

Specifies a Nutanix Prism Element cluster configuration. In this example, the cluster type is `uuid`, so there is a `uuid` stanza. 

Note

If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain. 

`spec.template.spec.providerSpec.value.credentialsSecret`
     Specifies the secret name for the cluster. Do not change this value. 
`spec.template.spec.providerSpec.value.image`
     Specifies the path to the source image for the disk. 
`spec.template.spec.providerSpec.value.kind`
     Specifies the cloud provider platform type. Do not change this value. 
`spec.template.spec.providerSpec.value.memorySize`
     Specifies the memory allocated for the control plane machines. 
`spec.template.spec.providerSpec.value.project`
     Specifies the Nutanix project that you use for your cluster. In this example, the project type is `name`, so there is a `name` stanza. 
`spec.template.spec.providerSpec.value.subnets`
    

Specify one or more Prism Element subnet objects. In this example, the subnet type is `uuid`, so there is a `uuid` stanza. A maximum of 32 subnets for each Prism Element failure domain in the cluster is supported. 

Important

Do not remove the original subnet, which hosts the API server and ingress server, from the cluster. 

The CIDR IP address prefix for one of the specified subnets must contain the virtual IP addresses that the OpenShift Container Platform cluster uses. All subnet UUID values must be unique. 

Note

If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain. 

`spec.template.spec.providerSpec.value.systemDiskSize`
     Specifies the VM disk size for the control plane machines. 
`spec.template.spec.providerSpec.value.userDataSecret`
     Specifies the control plane user data secret. Do not change this value. 
`spec.template.spec.providerSpec.value.vcpuSockets`
     Specifies the number of vCPU sockets allocated for the control plane machines. 
`spec.template.spec.providerSpec.value.vcpusPerSocket`
     Specifies the number of vCPUs for each control plane vCPU socket. 

### 10.5.7.2. Failure domains for Nutanix clusters

To modify failure domain configurations on a Nutanix cluster, you must modify the cluster infrastructure, control plane machine set, and compute machine set custom resources (CRs) to apply the new configuration. 

To add or update the failure domain configuration on a Nutanix cluster, you must make coordinated changes to several resources. The following actions are required: 

  1. Modify the cluster infrastructure custom resource (CR). 
  2. Modify the cluster control plane machine set CR. 
  3. Modify or replace the compute machine set CRs. 



For more information, see "Adding failure domains to an existing Nutanix cluster". 

### 10.5.7.3. Improving reliability for multiple subnet configurations on Nutanix

To improve reliability and avoid common networking problems with multiple subnet configurations on Nutanix, adhere to the configuration practices that minimize networking conflicts. 

The following networking configuration and management practices can help your multiple subnet configuration perform more reliably: 

  * To avoid overlapping IP address assignments, use predefined static IP addresses in the `cloud-init` metadata. 
  * Tag all VMs, disks, and networks with a unique cluster ID. 
  * Avoid IP address conflicts by using dedicated subnets for each OpenShift Container Platform cluster: 

Nutanix uses Nutanix Acropolis Hypervisor (AHV) and Nutanix Prism networking to assign IP addresses to virtual machines (VMs). If a single subnet provides IP addresses for more than one OpenShift Container Platform cluster, AHV or Prism might assign the same IP address to a VM or pod in more than one cluster. 

To avoid this issue, use dedicated subnets for each OpenShift Container Platform cluster, even when you have more than one cluster on a single Prism Central instance. You can use the Prism UI or automation tools, such as Terraform or Ansible, to create separate IP address pools for each OpenShift Container Platform cluster. 

  * Ensure that each OpenShift Container Platform cluster uses distinct DNS zones and virtual IP address ranges. 
  * Avoid DHCP conflicts by maintaining DHCP allocations: 

If you use Nutanix to manage DHCP allocation, objects in your cluster might have duplicate leases. Duplicate leases can cause DHCP conflicts when you apply changes to the control plane machine set custom resource (CR) specification. 

To avoid this issue, regularly remove stale DHCP leases. 

  * Use automation tools, such as Terraform or Ansible, to isolate the infrastructure for each OpenShift Container Platform cluster. 



### 10.5.7.4. Additional resources

  * [Updating the control plane configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration")
  * [Adding failure domains to an existing Nutanix cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_nutanix/#nutanix-failure-domains-adding-to-existing-cluster_nutanix-failure-domains)



## 10.5.8. Control plane configuration options for Red Hat OpenStack Platform (RHOSP)

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 

The following example YAML snippets show provider specification and failure domain configurations for an RHOSP cluster. 

### 10.5.8.1. Sample RHOSP provider specification

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification. 

The following example YAML illustrates a valid configuration for an Red Hat OpenStack Platform (RHOSP) cluster. 

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates. 

You can omit any field that has a value set in the failure domain section of the CR. 

In the following example, the `<cluster_id>` string is the infrastructure ID. The infrastructure ID matches the cluster ID that the installation program used during cluster provisioning. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command: 

```shell-session
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```


**Sample OpenStack`providerSpec` values**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            apiVersion: machine.openshift.io/v1alpha1
            cloudName: openstack
            cloudsSecret:
              name: openstack-cloud-credentials
              namespace: openshift-machine-api
            flavor: m1.xlarge
            image: <cluster_id>-rhcos
            kind: OpenstackProviderSpec
            metadata:
              creationTimestamp: null
            networks:
            - filter: {}
              subnets:
              - filter:
                  name: <cluster_id>-nodes
                  tags: openshiftClusterID=<cluster_id>
            securityGroups:
            - filter: {}
              name: <cluster_id>-master
            serverGroupName: <cluster_id>-master
            serverMetadata:
              Name: <cluster_id>-master
              openshiftClusterID: <cluster_id>
            tags:
            - openshiftClusterID=<cluster_id>
            trunk: true
            userDataSecret:
              name: master-user-data
```


where: 

`spec.template.spec.providerSpec.value.cloudsSecret.name`
     Specifies the secret name for the cluster. Do not change this value. 
`spec.template.spec.providerSpec.value.flavor`
     Specifies the RHOSP flavor type for the control plane. 
`spec.template.spec.providerSpec.value.kind`
     Specifies the cloud provider platform type. Do not change this value. 
`spec.template.spec.providerSpec.value.securityGroups`
     Specifies the control plane machines security group. 

### 10.5.8.2. Sample RHOSP failure domain configuration

To prevent downtime for your applications due to the failure of a single Red Hat OpenStack Platform (RHOSP) region, you can configure failure domains in the control plane machine set by configuring appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` object. 

The control plane machine set concept of a failure domain is analogous to the existing RHOSP concept of an [availability zone](https://docs.openstack.org/nova/latest/admin/availability-zones.html). The `ControlPlaneMachineSet` CR spreads control plane machines across more than one failure domain when possible. 

**Sample OpenStack failure domain values**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        openstack:
        - availabilityZone: nova-az0
          rootVolume:
            availabilityZone: cinder-az0
        - availabilityZone: nova-az1
          rootVolume:
            availabilityZone: cinder-az1
        - availabilityZone: nova-az2
          rootVolume:
            availabilityZone: cinder-az2
        platform: OpenStack
# ...
```


where: 

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.openstack`
     Specifies the availability zones for the failure domains. This example demonstrates the use of more than one Nova availability zone and corresponding Cinder availability zones. 
`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`
     Specifies the cloud provider platform name. Do not change this value. 

### 10.5.8.3. Additional resources

  * [Updating the control plane configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration")
  * [Configuring RHOSP features for control plane machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-supported-features-openstack "10.5.9. Configuring Red Hat OpenStack Platform \(RHOSP\) features for control plane machines")



## 10.5.9. Configuring Red Hat OpenStack Platform (RHOSP) features for control plane machines

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 

### 10.5.9.1. Changing the RHOSP compute flavor by using a control plane machine set

You can change the Red Hat OpenStack Platform (RHOSP) compute service (Nova) flavor that your control plane machines use by updating the specification in the control plane machine set custom resource. 

In RHOSP, flavors define the compute, memory, and storage capacity of computing instances. By increasing or decreasing the flavor size, you can scale your control plane vertically. 

**Prerequisites**

  * Your RHOSP cluster uses a control plane machine set. 



**Procedure**

  1. Edit the following line under the `providerSpec` field: 

```yaml
providerSpec:
  value:
# ...
    flavor: m1.xlarge
```


where: 

providerSpec.value.flavor
     Specify a RHOSP flavor type that has the same base as the existing selection. For example, you can change `m6i.xlarge` to `m6i.2xlarge` or `m6i.4xlarge`. You can choose larger or smaller flavors depending on your vertical scaling needs. 

  2. Save your changes. 

After you save your changes, machines are replaced with ones that use the flavor you chose. 




### 10.5.9.2. Additional resources

  * [Updating the control plane configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration")
  * [Control plane configuration options for {rh-openstack-full}](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-config-options-openstack "10.5.8. Control plane configuration options for Red Hat OpenStack Platform \(RHOSP\)")



## 10.5.10. Control plane configuration options for VMware vSphere

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 

The following example YAML snippets show provider specification and failure domain configurations for a vSphere cluster. 

### 10.5.10.1. Sample vSphere provider specification

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification. 

The following example YAML illustrates a valid configuration for a VMware vSphere cluster. 

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates. 

You can omit any field that has a value set in the failure domain section of the CR. 

**Sample vSphere`providerSpec` values**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
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
            memoryMiB: 16384
            metadata:
              creationTimestamp: null
            network:
              devices:
              - networkName: <vm_network_name>
            numCPUs: 4
            numCoresPerSocket: 4
            snapshot: ""
            template: <vm_template_name>
            userDataSecret:
              name: master-user-data
            workspace:
              datacenter: <vcenter_data_center_name>
              datastore: <vcenter_datastore_name>
              folder: <path_to_vcenter_vm_folder>
              resourcePool: <vsphere_resource_pool>
              server: <vcenter_server_ip>
```


where: 

`spec.template.spec.providerSpec.value.credentialsSecret`
     Specifies the secret name for the cluster. Do not change this value. 
`spec.template.spec.providerSpec.value.dataDisks`
     Specifies one or more data disk definitions. For more information, see "Configuring data disks by using machine sets". 
`spec.template.spec.providerSpec.value.diskGiB`
     Specifies the VM disk size for the control plane machines. 
`spec.template.spec.providerSpec.value.kind`
     Specifies the cloud provider platform type. Do not change this value. 
`spec.template.spec.providerSpec.value.memoryMiB`
     Specifies the memory allocated for the control plane machines. 
`spec.template.spec.providerSpec.value.network`
    

Specifies the network on which to deploy the control plane. 

Note

If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain. 

`spec.template.spec.providerSpec.value.numCPUs`
     Specifies the number of CPUs allocated for the control plane machines. 
`spec.template.spec.providerSpec.value.numCoresPerSocket`
     Specifies the number of cores for each control plane CPU. 
`spec.template.spec.providerSpec.value.template`
    

Specifies the vSphere VM template to use, such as `user-5ddjd-rhcos`. 

Note

If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain. 

`spec.template.spec.providerSpec.value.userDataSecret`
     Specifies the control plane user data secret. Do not change this value. 
`spec.template.spec.providerSpec.value.workspace`
    

Specifies the workspace details for the control plane. 

Note

If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain. 

The following keys in this stanza specify additional details: 

`datacenter`
     Specifies the vCenter datacenter for the control plane. 
`datastore`
     Specifies the vCenter datastore for the control plane. 
`folder`
     Specifies the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`. 
`resourcePool`
     Specifies the vSphere resource pool for your VMs. 
`server`
     Specifies the vCenter server IP or fully qualified domain name. 

### 10.5.10.2. Sample VMware vSphere failure domain configuration

To prevent downtime for your applications due to the failure of a single VMware vSphere region, you can configure failure domains in the control plane machine set by configuring appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` object. 

On vSphere infrastructure, the cluster-wide infrastructure custom resource definition (CRD), `infrastructures.config.openshift.io`, defines failure domains for your cluster. A failure domain is an infrastructure resource made up of a control plane machine set, a vCenter data center, vCenter datastore, and a network. The `providerSpec` in the `ControlPlaneMachineSet` custom resource (CR) specifies names for failure domains that the control plane machine set uses to ensure control plane nodes deploy on the appropriate failure domain. 

By using a failure domain resource, you can use a control plane machine set to deploy control plane machines on separate clusters or data centers. A control plane machine set also balances control plane machines across defined failure domains to improve fault tolerance capabilities for your infrastructure. 

Note

If you change the `ProviderSpec` configuration in the `ControlPlaneMachineSet` CR, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. 

**Sample VMware vSphere failure domain values**

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        vsphere:
        - name: <failure_domain_name_1>
        - name: <failure_domain_name_2>
        platform: VSphere
# ...
```


where: 

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.vsphere.name`
    

Each instance of `name` specifies a failure domain. 

Important

Each `name` field value in the stanza must match the corresponding value in the `failureDomains.name` field of the cluster-wide infrastructure CRD. You can find the value of the `failureDomains.name` field by running the following command: 

```shell-session
$ oc get infrastructure cluster -o=jsonpath={.spec.platformSpec.vsphere.failureDomains[0].name}
```


The `name` field is the only supported failure domain field that you can specify in the `ControlPlaneMachineSet` CR. 

For an example of a cluster-wide infrastructure CRD that defines resources for each failure domain, see "Specifying multiple regions and zones for your cluster on vSphere." 

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`
     Specifies the cloud provider platform name. Do not change this value. 

### 10.5.10.3. Additional resources

  * [Updating the control plane configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration")
  * [Configuring VMware vSphere features for control plane machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-supported-features-vsphere "10.5.11. Configuring VMware vSphere features for control plane machines")
  * [Specifying multiple regions and zones for your cluster on vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#specifying-regions-zones-infrastructure-vsphere_post-install-vsphere-zones-regions-configuration)



## 10.5.11. Configuring VMware vSphere features for control plane machines

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification. 

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration". 

### 10.5.11.1. Adding tags to machines by using machine sets

To ensure that your cluster remains scalable and resilient, you can use a `MachineSet` object and machine health checks to automate the provisioning and repair of nodes. 

OpenShift Container Platform adds a cluster-specific tag to each virtual machine (VM) that it creates. The installation program uses these tags to select the VMs to delete when uninstalling a cluster. 

In addition to the cluster-specific tags assigned to VMs, you can configure a machine set to add up to 10 additional vSphere tags to the VMs it provisions. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster installed on vSphere using an account with `cluster-admin` permissions. 
  * You have access to the VMware vCenter console associated with your cluster. 
  * You have created a tag in the vCenter console. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Use the vCenter console to find the tag ID for any tag that you want to add to your machines: 

     1. Log in to the vCenter console. 
     2. From the **Home** menu, click **Tags & Custom Attributes**. 
     3. Select a tag that you want to add to your machines. 
     4. Use the browser URL for the tag that you select to identify the tag ID. 

**Example tag URL**

```plaintext
https://vcenter.example.com/ui/app/tags/tag/urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL/permissions
```


**Example tag ID**

```plaintext
urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL
```


  2. In a text editor, open the YAML file for an existing machine set or create a new one. 
  3. Edit the following lines under the `providerSpec` field: 

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    spec:
      providerSpec:
        value:
          tagIDs:
          - <tag_id_value>
# ...
```


where 

`spec.template.spec.providerSpec.value.tagIDs`
     Specifies a list of up to 10 tags to add to the machines that this machine set provisions. Replace `<tag_id_value>` with the tag that you want to add to your machines. For example, `urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL`. 




### 10.5.11.2. Configuring data disks by using machine sets

To provide persistent storage beyond the root volume for specialized application workloads, define a `dataDisks` array in the `MachineSet` YAML file to specify disk size and storage policy. 

OpenShift Container Platform clusters on VMware vSphere support adding up to 29 disks to the virtual machine (VM) controller. 

Important

Configuring vSphere data disks is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

By configuring data disks, you can attach disks to VMs and use them to store data for etcd, container images, and other uses. Separating data can help avoid filling the primary disk so that important activities such as upgrades have the resources that they require. 

Note

Adding data disks attaches them to the VM and mounts them to the location that RHCOS designates. 

**Prerequisites**

  * You have administrator access to OpenShift CLI (`oc`) for an OpenShift Container Platform cluster on vSphere. 



**Procedure**

  1. In a text editor, open the YAML file for an existing machine set or create a new one. 
  2. Edit the following lines under the `providerSpec` field: 

```yaml
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
# ...
spec:
  template:
    machines_v1beta1_machine_openshift_io:
      spec:
        providerSpec:
          value:
            dataDisks:
            - name: "<disk_name>"
              provisioningMode: "<mode>"
              sizeGiB: 20
            - name: "<disk_name>"
              provisioningMode: "<mode>"
              sizeGiB: 20
# ...
```


where 

`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks`
     Specifies a collection of 1-29 data disk definitions. This sample configuration shows the formatting to include two data disk definitions. 
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks.name`
    

Specifies the name of the data disk. The name must meet the following requirements: 

     * Start and end with an alphanumeric character 
     * Consist only of alphanumeric characters, hyphens (`-`), and underscores (`_`) 
     * Have a maximum length of 80 characters 

`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks.provisioningMode`
     Specifies the data disk provisioning method. This value defaults to the vSphere default storage policy if not set. Valid values are `Thin`, `Thick`, and `EagerlyZeroed`. 
`spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks.sizeGiB`
     Specifies the size of the data disk in GiB. The maximum size is 16,384 GiB. 




### 10.5.11.3. Additional resources

  * [Updating the control plane configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration")
  * [Control plane configuration options for VMware vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/machine_management/managing-control-plane-machines#cpmso-config-options-vsphere "10.5.10. Control plane configuration options for VMware vSphere")
