# 2.5. IAM Policies and AWS authentication

You can specify your own IAM roles if required. By default, the installation program creates instance profiles for the bootstrap, control plane, and compute instances with the necessary permissions for the cluster to operate. 

Note

To enable pulling images from the Amazon Elastic Container Registry (ECR) as a postinstallation task in a single-node OpenShift cluster, you must add the `AmazonEC2ContainerRegistryReadOnly` policy to the IAM role associated with the cluster’s control plane role. 

However, you can create your own IAM roles and specify them as part of the installation process. You might need to specify your own roles to deploy the cluster or to manage the cluster after installation. For example: 

  * Your organization’s security policies require that you use a more restrictive set of permissions to install the cluster. 
  * After the installation, the cluster is configured with an Operator that requires access to additional services. 



If you choose to specify your own IAM roles, you can take the following steps: 

  * Begin with the default policies and adapt as required. For more information, see "Default permissions for IAM instance profiles". 
  * To create a policy template that is based on the cluster’s activity, see "Using AWS IAM Analyzer to create policy templates". 



## 2.5.1. Default permissions for IAM instance profiles

To ensure your cluster operates with the correct security permissions in OpenShift Container Platform, review the default IAM instance profiles created by the installation program. 

By default, the installation program creates IAM instance profiles for the bootstrap, control plane, and compute instances with the necessary permissions for the cluster to operate. 

The following list specifies the default IAM role permissions for control plane instance profiles: 

  * `ec2:AttachVolume`
  * `ec2:AuthorizeSecurityGroupIngress`
  * `ec2:CreateSecurityGroup`
  * `ec2:CreateTags`
  * `ec2:CreateVolume`
  * `ec2:DeleteSecurityGroup`
  * `ec2:DeleteVolume`
  * `ec2:Describe*`
  * `ec2:DetachVolume`
  * `ec2:ModifyInstanceAttribute`
  * `ec2:ModifyVolume`
  * `ec2:RevokeSecurityGroupIngress`
  * `elasticloadbalancing:AddTags`
  * `elasticloadbalancing:AttachLoadBalancerToSubnets`
  * `elasticloadbalancing:ApplySecurityGroupsToLoadBalancer`
  * `elasticloadbalancing:CreateListener`
  * `elasticloadbalancing:CreateLoadBalancer`
  * `elasticloadbalancing:CreateLoadBalancerPolicy`
  * `elasticloadbalancing:CreateLoadBalancerListeners`
  * `elasticloadbalancing:CreateTargetGroup`
  * `elasticloadbalancing:ConfigureHealthCheck`
  * `elasticloadbalancing:DeleteListener`
  * `elasticloadbalancing:DeleteLoadBalancer`
  * `elasticloadbalancing:DeleteLoadBalancerListeners`
  * `elasticloadbalancing:DeleteTargetGroup`
  * `elasticloadbalancing:DeregisterInstancesFromLoadBalancer`
  * `elasticloadbalancing:DeregisterTargets`
  * `elasticloadbalancing:Describe*`
  * `elasticloadbalancing:DetachLoadBalancerFromSubnets`
  * `elasticloadbalancing:ModifyListener`
  * `elasticloadbalancing:ModifyLoadBalancerAttributes`
  * `elasticloadbalancing:ModifyTargetGroup`
  * `elasticloadbalancing:ModifyTargetGroupAttributes`
  * `elasticloadbalancing:RegisterInstancesWithLoadBalancer`
  * `elasticloadbalancing:RegisterTargets`
  * `elasticloadbalancing:SetLoadBalancerPoliciesForBackendServer`
  * `elasticloadbalancing:SetLoadBalancerPoliciesOfListener`
  * `kms:DescribeKey`



The following list specifies the default IAM permissions for compute instance profiles: 

  * `ec2:DescribeInstances`
  * `ec2:DescribeRegions`



## 2.5.2. Specifying an existing IAM role

Instead of allowing the installation program to create IAM instance profiles with the default permissions, you can use the `install-config.yaml` file to specify an existing IAM role for control plane and compute instances. 

**Prerequisites**

  * You have an existing `install-config.yaml` file. 



**Procedure**

  1. Update `compute.platform.aws.iamRole` with an existing role for the compute machines. 

**Sample`install-config.yaml` file with an IAM role for compute instances**

```yaml
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    aws:
      iamRole: ExampleRole
```


  2. Update `controlPlane.platform.aws.iamRole` with an existing role for the control plane machines. 

**Sample`install-config.yaml` file with an IAM role for control plane instances**

```yaml
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    aws:
      iamRole: ExampleRole
```


  3. Save the file and reference it when installing the OpenShift Container Platform cluster. 

Note

To change or update an IAM account after the cluster has been installed, see [RHOCP 4 AWS cloud-credentials access key is expired](https://access.redhat.com/solutions/4284011) (Red Hat Knowledgebase). 




**Additional resources**

  * [Deploying the cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_aws/installer-provisioned-infrastructure#installation-launching-installer_installing-aws-customizations "3.3.10. Deploying the cluster")



## 2.5.3. Using AWS IAM Analyzer to create policy templates

To reduce security risk, you can use AWS IAM Access Analyzer and CloudTrail to generate and apply minimal, fine-grained IAM policies for cluster control plane and compute instance profiles. 

The minimal set of permissions that the control plane and compute instance profiles require depends on how the cluster is configured for its daily operation. 

One way to determine which permissions the cluster instances require is to use the AWS Identity and Access Management Access Analyzer (IAM Access Analyzer) to create a policy template: 

  * A policy template contains the permissions the cluster has used over a specified period of time. 
  * You can then use the template to create policies with fine-grained permissions. 



**Procedure**

  1. Ensure that CloudTrail is enabled. CloudTrail records all of the actions and events in your AWS account, including the API calls that are required to create a policy template. For more information, see the AWS documentation for [working with CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-getting-started.html). 
  2. Create an instance profile for control plane instances and an instance profile for compute instances. Be sure to assign each role a permissive policy, such as PowerUserAccess. For more information, see the AWS documentation for [creating instance profile roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). 
  3. Install the cluster in a development environment and configure it as required. Be sure to deploy all of applications the cluster will host in a production environment. 
  4. Test the cluster thoroughly. Testing the cluster ensures that all of the required API calls are logged. 
  5. Use the IAM Access Analyzer to create a policy template for each instance profile. For more information, see the AWS documentation for [generating policies based on the CloudTrail logs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html). 
  6. Create and add a fine-grained policy to each instance profile. 
  7. Remove the permissive policy from each instance profile. 
  8. Deploy a production cluster using the existing instance profiles with the new policies. 

Note

You can add [IAM Conditions](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) to your policy to make it more restrictive and compliant with your organization security requirements.
