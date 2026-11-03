# 8.1. Extend existing clusters to use AWS Local Zones or Wavelength Zones

As a post-installation task, you can extend an existing OpenShift Container Platform cluster on Amazon Web Services to use AWS Local Zones or Wavelength Zones. 

Extending nodes to Local Zones or Wavelength Zones locations comprises the following steps: 

  * Adjusting the cluster-network maximum transmission unit (MTU). 
  * Opting in the Local Zones or Wavelength Zones group to AWS Local Zones or Wavelength Zones. 
  * Creating a subnet in the existing VPC for a Local Zones or Wavelength Zones location. 

Important

Before you extend an existing OpenShift Container Platform cluster on AWS to use Local Zones or Wavelength Zones, check that the existing VPC contains available Classless Inter-Domain Routing (CIDR) blocks. These blocks are needed for creating the subnets. 

  * Creating the machine set manifest, and then creating a node in each Local Zone or Wavelength Zone location. 
  * Local Zones only: Adding the permission `ec2:ModifyAvailabilityZoneGroup` to the Identity and Access Management (IAM) user or role, so that the required network resources can be created. For example: 

**Example of an additional IAM policy for AWS Local Zones deployments**

```yaml
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "ec2:ModifyAvailabilityZoneGroup"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```


  * Wavelength Zone only: Adding the permissions `ec2:ModifyAvailabilityZoneGroup`, `ec2:CreateCarrierGateway`, and `ec2:DeleteCarrierGateway` to the Identity and Access Management (IAM) user or role, so that the required network resources can be created. For example: 

**Example of an additional IAM policy for AWS Wavelength Zones deployments**

```yaml
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DeleteCarrierGateway",
        "ec2:CreateCarrierGateway"
      ],
      "Resource": "*"
    },
    {
      "Action": [
        "ec2:ModifyAvailabilityZoneGroup"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```


**Additional resources**

  * [AWS Local Zones features (AWS documentation)](https://aws.amazon.com/about-aws/global-infrastructure/localzones/features/)
  * [AWS Wavelength features (AWS documentation)](https://aws.amazon.com/wavelength/features/)



## 8.1.1. About edge compute pools

The edge compute pool configuration is common between Amazon Web Services (AWS) Local Zones or Wavelength Zones locations. 

You can use the edge compute pool to create new labels to deploy applications onto Amazon Web Services (AWS) Local Zones or Wavelength Zones nodes. Edge compute nodes are tainted compute nodes that run in AWS Local Zones or Wavelength Zones locations. 

When deploying a cluster that uses Local Zones or Wavelength Zones, consider the following points: 

  * Amazon EC2 instances in the Local Zones or Wavelength Zones are more expensive than Amazon EC2 instances in the Availability Zones. 
  * The latency is lower between the applications running in AWS Local Zones or Wavelength Zones and the user. A latency impact exists for some workloads if, for example, ingress traffic is mixed between Local Zones or Wavelength Zones and Availability Zones. 



Important

Generally, the maximum transmission unit (MTU) between an Amazon EC2 instance in a Local Zones or Wavelength Zones and an Amazon EC2 instance in the Region is 1300. The cluster network MTU must be always less than the EC2 MTU to account for the overhead. The specific overhead is determined by the network plugin. For example: OVN-Kubernetes has an overhead of `100 bytes`. 

The network plugin can provide additional features, such as IPsec, that also affect the MTU sizing. 

OpenShift Container Platform 4.12 introduced a new compute pool, _edge_ , that is designed for use in remote zones. The edge compute pool configuration is common between Amazon Web Services (AWS) Local Zones or Wavelength Zones locations. Because of the type and size limitations of resources like EC2 and EBS on Local Zones or Wavelength Zones resources, the default instance type can vary from the traditional compute pool. 

The default Elastic Block Store (EBS) for Local Zones or Wavelength Zones locations is `gp2`, which differs from the non-edge compute pool. The instance type used for each Local Zones or Wavelength Zones on an edge compute pool also might differ from other compute pools, depending on the instance offerings on the zone. 

The edge compute pool creates new labels that developers can use to deploy applications onto AWS Local Zones or Wavelength Zones nodes. The new labels are: 

  * `node-role.kubernetes.io/edge=''`
  * Local Zones only: `machine.openshift.io/zone-type=local-zone`
  * Wavelength Zones only: `machine.openshift.io/zone-type=wavelength-zone`
  * `machine.openshift.io/zone-group=$ZONE_GROUP_NAME`



By default, the machine sets for the edge compute pool define the taint of `NoSchedule` to prevent other workloads from spreading on Local Zones or Wavelength Zones instances. Users can only run user workloads if they define tolerations in the pod specification. 

**Additional resources**

  * [How AWS Local Zones work (AWS documentation)](https://docs.aws.amazon.com/local-zones/latest/ug/how-local-zones-work.html)
  * [How AWS Wavelength works (AWS documentation)](https://docs.aws.amazon.com/wavelength/latest/developerguide/how-wavelengths-work.html)
