# 2.7. Supported AWS regions

You can deploy an OpenShift Container Platform cluster to the following regions. 

Note

Your IAM user must have the permission `tag:GetResources` in the region `us-east-1` to delete the base cluster resources. As part of the AWS API requirement, the OpenShift Container Platform installation program performs various actions in this region. 

## 2.7.1. AWS public regions

The following AWS public regions are supported: 

  * `af-south-1` (Cape Town) 
  * `ap-east-1` (Hong Kong) 
  * `ap-east-2` (Taipei) 
  * `ap-northeast-1` (Tokyo) 
  * `ap-northeast-2` (Seoul) 
  * `ap-northeast-3` (Osaka) 
  * `ap-south-1` (Mumbai) 
  * `ap-south-2` (Hyderabad) 
  * `ap-southeast-1` (Singapore) 
  * `ap-southeast-2` (Sydney) 
  * `ap-southeast-3` (Jakarta) 
  * `ap-southeast-4` (Melbourne) 
  * `ap-southeast-5` (Malaysia) 
  * `ap-southeast-6` (New Zealand) 
  * `ap-southeast-7` (Thailand) 
  * `ca-central-1` (Central Canada) 
  * `ca-west-1` (Calgary) 
  * `eu-central-1` (Frankfurt) 
  * `eu-central-2` (Zurich) 
  * `eu-north-1` (Stockholm) 
  * `eu-south-1` (Milan) 
  * `eu-south-2` (Spain) 
  * `eu-west-1` (Ireland) 
  * `eu-west-2` (London) 
  * `eu-west-3` (Paris) 
  * `il-central-1` (Tel Aviv) 
  * `me-central-1` (UAE) 
  * `me-south-1` (Bahrain) 
  * `mx-central-1` (Central Mexico) 
  * `sa-east-1` (São Paulo) 
  * `us-east-1` (N. Virginia) 
  * `us-east-2` (Ohio) 
  * `us-west-1` (N. California) 
  * `us-west-2` (Oregon) 



## 2.7.2. AWS EUSC region

Important

European Sovereign Cloud (EUSC) region is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

Installing an OpenShift Container Platform cluster into the AWS European Sovereign Cloud (EUSC) region helps maximize the sovereignty of your data and satisfy your organization’s regulatory requirements. The AWS EUSC is separate and independent from other AWS regions. The infrastructure is located wholly within the European Union (EU). For more information, see [Establishing a European trust service provider for the AWS European Sovereign Cloud](https://aws.amazon.com/blogs/security/establishing-a-european-trust-service-provider-for-the-aws-european-sovereign-cloud/) in the AWS documentation. 

The following AWS EUSC region is supported: 

  * `eusc-de-east-1` (Brandenburg) 



Important

The following list outlines the limitations that apply to installing an OpenShift Container Platform cluster into the AWS EUSC region: 

  * Only one region, `eusc-de-east-1`, and two zones in that region are available. 
  * The Amazon Machine Images (AMIs) for public Red Hat Enterprise Linux CoreOS (RHCOS) are not yet available in the EUSC region. As a workaround, until the AMI publication for RHCOS is extended to the EUSC region, you must edit your `install-config.yaml` file to specify a custom AMI in the `amiID` field. 
  * Support is not yet provided for the AWS Security Token Service (STS). 
  * Support is not yet provided for installing a cluster into a shared Virtual Private Cloud (VPC) with a cross-account private hosted zone. 



## 2.7.3. AWS GovCloud regions

The following AWS GovCloud regions are supported: 

  * `us-gov-west-1`
  * `us-gov-east-1`



## 2.7.4. AWS SC2S and C2S secret regions

The following AWS secret regions are supported: 

  * `us-isob-east-1` Secret Commercial Cloud Services (SC2S) 
  * `us-iso-east-1` Commercial Cloud Services (C2S) 



## 2.7.5. AWS China regions

The following AWS China regions are supported: 

  * `cn-north-1` (Beijing) 
  * `cn-northwest-1` (Ningxia) 



**Additional resources**

  * [Quickly install a cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_aws/installer-provisioned-infrastructure#installing-aws-default "3.2. Installing a cluster on AWS")
  * [Install a cluster with cloud customizations on installer-provisioned infrastructure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_aws/installer-provisioned-infrastructure#installing-aws-customizations "3.3. Installing a cluster on AWS with customizations")
  * [Installing a cluster on user-provisioned infrastructure in AWS by using CloudFormation templates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_aws/user-provisioned-infrastructure#installing-aws-user-infra "4.3. Installing a cluster on user-provisioned infrastructure in AWS by using CloudFormation templates")
