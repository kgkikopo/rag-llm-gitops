# 21.5. About the Cloud Credential Operator in manual mode with short-term credentials for components

During installation, you can configure the Cloud Credential Operator (CCO) to operate in manual mode and use the CCO utility (`ccoctl`) to implement short-term security credentials for individual components that are created and managed outside the OpenShift Container Platform cluster. 

Note

This credentials strategy is supported for Amazon Web Services (AWS), Google Cloud, and global Microsoft Azure only. 

For AWS and Google Cloud clusters, you must configure your cluster to use this strategy during installation of a new OpenShift Container Platform cluster. You cannot configure an existing AWS or Google Cloud cluster that uses a different credentials strategy to use this feature. 

If you did not configure your Azure cluster to use Microsoft Entra Workload ID during installation, you can enable this authentication method on an existing cluster. For information, see "Enabling token-based authentication". 

Cloud providers use different terms for their implementation of this authentication method. 

Table 21.3. Short-term credentials provider terminologyCloud provider| Provider nomenclature  
---|---  
Amazon Web Services (AWS)  |  AWS Security Token Service (STS)   
Google Cloud  |  GCP Workload Identity   
Global Microsoft Azure  |  Microsoft Entra Workload ID   
Show more

## 21.5.1. About AWS Security Token Service

To assign IAM roles that provide short-term, limited-privilege security credentials to your cluster components, you can configure your cluster to use manual mode with Security Token Service (STS), allowing the individual OpenShift Container Platform components to use the AWS STS. 

These credentials are associated with IAM roles that are specific to each component that makes AWS API calls. 

**Additional resources**

  * [Configuring an AWS cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-with-short-term-creds_installing-aws-customizations)



### 21.5.1.1. AWS Security Token Service authentication process

You should familiarize yourself with the process that the AWS Security Token Service (STS) and the [`AssumeRole`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) API action perform to allow pods to retrieve access keys that are defined by an IAM role policy. 

The OpenShift Container Platform cluster includes a Kubernetes service account signing service. This service uses a private key to sign service account JSON web tokens (JWT). A pod that requires a service account token requests one through the pod specification. When the pod is created and assigned to a node, the node retrieves a signed service account from the service account signing service and mounts it onto the pod. 

Clusters that use STS contain an IAM role ID in their Kubernetes configuration secrets. Workloads assume the identity of this IAM role ID. The signed service account token issued to the workload aligns with the configuration in AWS, which allows AWS STS to grant access keys for the specified IAM role to the workload. 

AWS STS grants access keys only for requests that include service account tokens that meet the following conditions: 

  * The token name and namespace match the service account name and namespace. 
  * The token is signed by a key that matches the public key. 



The public key pair for the service account signing key used by the cluster is stored in an AWS S3 bucket. AWS STS federation validates that the service account token signature aligns with the public key stored in the S3 bucket. 

#### 21.5.1.1.1. Authentication flow for AWS STS

The following diagram illustrates the authentication flow between AWS and the OpenShift Container Platform cluster when using AWS STS. 

  * _Token signing_ is the Kubernetes service account signing service on the OpenShift Container Platform cluster. 
  * The _Kubernetes service account_ in the pod is the signed service account token. 



**Figure 21.2. AWS Security Token Service authentication flow**

![Detailed authentication flow between AWS and the cluster when using AWS STS](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Authentication_and_authorization-en-US/images/a187100d4a49b9308142d59828ee16fd/347_OpenShift_credentials_with_STS_updates_0623_AWS.png) ![Detailed authentication flow between AWS and the cluster when using AWS STS](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Authentication_and_authorization-en-US/images/a187100d4a49b9308142d59828ee16fd/347_OpenShift_credentials_with_STS_updates_0623_AWS.png)

Requests for new and refreshed credentials are automated by using an appropriately configured AWS IAM OpenID Connect (OIDC) identity provider combined with AWS IAM roles. Service account tokens that are trusted by AWS IAM are signed by OpenShift Container Platform and can be projected into a pod and used for authentication. 

#### 21.5.1.1.2. Token refreshing for AWS STS

The signed service account token that a pod uses expires after a period of time. For clusters that use AWS STS, this time period is 3600 seconds, or one hour. 

The kubelet on the node that the pod is assigned to ensures that the token is refreshed. The kubelet attempts to rotate a token when it is older than 80 percent of its time to live. 

#### 21.5.1.1.3. OpenID Connect requirements for AWS STS

You can store the public portion of the encryption keys for your OIDC configuration in a public or private S3 bucket. 

The OIDC spec requires the use of HTTPS. AWS services require a public endpoint to expose the OIDC documents in the form of JSON web key set (JWKS) public keys. This allows AWS services to validate the bound tokens signed by Kubernetes and determine whether to trust certificates. As a result, both S3 bucket options require a public HTTPS endpoint and private endpoints are not supported. 

To use AWS STS, the public AWS backbone for the AWS STS service must be able to communicate with a public S3 bucket or a private S3 bucket with a public CloudFront endpoint. You can choose which type of bucket to use when you process `CredentialsRequest` objects during installation: 

  * By default, the CCO utility (`ccoctl`) stores the OIDC configuration files in a public S3 bucket and uses the S3 URL as the public OIDC endpoint. 
  * As an alternative, you can have the `ccoctl` utility store the OIDC configuration in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL. 



### 21.5.1.2. AWS component secret formats

To change the content of the AWS credentials that are provided to individual OpenShift Container Platform components, you can use manual mode with the AWS Security Token Service (STS) . 

Compare the following secret formats: 

**AWS secret format using long-term credentials**

```yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace>
  name: <target_secret_name>
data:
  aws_access_key_id: <base64_encoded_access_key_id>
  aws_secret_access_key: <base64_encoded_secret_access_key>
```


where: 

`metadata.namespace`
     Specifies the namespace for the component. 
`metadata.name`
     Specifies the name of the component secret. 

**AWS secret format using AWS STS**

```yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace>
  name: <target_secret_name>
stringData:
  credentials: |-
    [default]
    sts_regional_endpoints = regional
    role_name: <operator_role_name>
    web_identity_token_file: <path_to_token>
```


where: 

`metadata.namespace`
     Specifies the namespace for the component. 
`metadata.name`
     Specifies the name of the component secret. 
`stringData.credentials.role_name`
     Specifies the IAM role for the component. 
`stringData.credentials.web_identity_token_file`
     Specifies the path to the service account token inside the pod. By convention, this is `/var/run/secrets/openshift/serviceaccount/token` for OpenShift Container Platform components. 

### 21.5.1.3. AWS component secret permissions requirements

You should familiarize yourself with the permissions required by the OpenShift Container Platform components. These values are in the `CredentialsRequest` custom resource (CR) for each component. 

OpenShift Container Platform components require the following permissions: 

Note

These permissions apply to all resources. Unless specified, there are no request conditions on these permissions. 

Component| Custom resource| Required permissions for services  
---|---|---  
Cluster CAPI Operator  |  `openshift-cluster-api-aws` |  **EC2**

  * `ec2:CreateTags`
  * `ec2:DescribeAvailabilityZones`
  * `ec2:DescribeDhcpOptions`
  * `ec2:DescribeImages`
  * `ec2:DescribeInstances`
  * `ec2:DescribeInternetGateways`
  * `ec2:DescribeSecurityGroups`
  * `ec2:DescribeSubnets`
  * `ec2:DescribeVpcs`
  * `ec2:DescribeNetworkInterfaces`
  * `ec2:DescribeNetworkInterfaceAttribute`
  * `ec2:ModifyNetworkInterfaceAttribute`
  * `ec2:RunInstances`
  * `ec2:TerminateInstances`

**Elastic load balancing**

  * `elasticloadbalancing:DescribeLoadBalancers`
  * `elasticloadbalancing:DescribeTargetGroups`
  * `elasticloadbalancing:DescribeTargetHealth`
  * `elasticloadbalancing:RegisterInstancesWithLoadBalancer`
  * `elasticloadbalancing:RegisterTargets`
  * `elasticloadbalancing:DeregisterTargets`

**Identity and Access Management (IAM)**

  * `iam:PassRole`
  * `iam:CreateServiceLinkedRole`

**Key Management Service (KMS)**

  * `kms:Decrypt`
  * `kms:Encrypt`
  * `kms:GenerateDataKey`
  * `kms:GenerateDataKeyWithoutPlainText`
  * `kms:DescribeKey`
  * `kms:RevokeGrant`[1]
  * `kms:CreateGrant` [1]
  * `kms:ListGrants` [1]

  
Machine API Operator  |  `openshift-machine-api-aws` |  **EC2**

  * `ec2:CreateTags`
  * `ec2:DescribeAvailabilityZones`
  * `ec2:DescribeDhcpOptions`
  * `ec2:DescribeImages`
  * `ec2:DescribeInstances`
  * `ec2:DescribeInstanceTypes`
  * `ec2:DescribeInternetGateways`
  * `ec2:DescribeSecurityGroups`
  * `ec2:DescribeRegions`
  * `ec2:DescribeSubnets`
  * `ec2:DescribeVpcs`
  * `ec2:RunInstances`
  * `ec2:TerminateInstances`

**Elastic load balancing**

  * `elasticloadbalancing:DescribeLoadBalancers`
  * `elasticloadbalancing:DescribeTargetGroups`
  * `elasticloadbalancing:DescribeTargetHealth`
  * `elasticloadbalancing:RegisterInstancesWithLoadBalancer`
  * `elasticloadbalancing:RegisterTargets`
  * `elasticloadbalancing:DeregisterTargets`

**Identity and Access Management (IAM)**

  * `iam:PassRole`
  * `iam:CreateServiceLinkedRole`

**Key Management Service (KMS)**

  * `kms:Decrypt`
  * `kms:Encrypt`
  * `kms:GenerateDataKey`
  * `kms:GenerateDataKeyWithoutPlainText`
  * `kms:DescribeKey`
  * `kms:RevokeGrant`[1]
  * `kms:CreateGrant` [1]
  * `kms:ListGrants` [1]

  
Cloud Credential Operator  |  `cloud-credential-operator-iam-ro` |  **Identity and Access Management (IAM)**

  * `iam:GetUser`
  * `iam:GetUserPolicy`
  * `iam:ListAccessKeys`

  
Cluster Image Registry Operator  |  `openshift-image-registry` |  **S3**

  * `s3:CreateBucket`
  * `s3:DeleteBucket`
  * `s3:PutBucketTagging`
  * `s3:GetBucketTagging`
  * `s3:PutBucketPublicAccessBlock`
  * `s3:GetBucketPublicAccessBlock`
  * `s3:PutEncryptionConfiguration`
  * `s3:GetEncryptionConfiguration`
  * `s3:PutLifecycleConfiguration`
  * `s3:GetLifecycleConfiguration`
  * `s3:GetBucketLocation`
  * `s3:ListBucket`
  * `s3:GetObject`
  * `s3:PutObject`
  * `s3:DeleteObject`
  * `s3:ListBucketMultipartUploads`
  * `s3:AbortMultipartUpload`
  * `s3:ListMultipartUploadParts`

  
Ingress Operator  |  `openshift-ingress` |  **Elastic load balancing**

  * `elasticloadbalancing:DescribeLoadBalancers`

**Route 53**

  * `route53:ListHostedZones`
  * `route53:ListTagsForResources`
  * `route53:ChangeResourceRecordSets`

**Tag**

  * `tag:GetResources`

**Security Token Service (STS)**

  * `sts:AssumeRole`

  
Cluster Network Operator  |  `openshift-cloud-network-config-controller-aws` |  **EC2**

  * `ec2:DescribeInstances`
  * `ec2:DescribeInstanceStatus`
  * `ec2:DescribeInstanceTypes`
  * `ec2:UnassignPrivateIpAddresses`
  * `ec2:AssignPrivateIpAddresses`
  * `ec2:UnassignIpv6Addresses`
  * `ec2:AssignIpv6Addresses`
  * `ec2:DescribeSubnets`
  * `ec2:DescribeNetworkInterfaces`

  
AWS Elastic Block Store CSI Driver Operator  |  `aws-ebs-csi-driver-operator` |  **EC2**

  * `ec2:AttachVolume`
  * `ec2:CreateSnapshot`
  * `ec2:CreateTags`
  * `ec2:CreateVolume`
  * `ec2:DeleteSnapshot`
  * `ec2:DeleteTags`
  * `ec2:DeleteVolume`
  * `ec2:DescribeInstances`
  * `ec2:DescribeSnapshots`
  * `ec2:DescribeTags`
  * `ec2:DescribeVolumes`
  * `ec2:DescribeVolumesModifications`
  * `ec2:DetachVolume`
  * `ec2:ModifyVolume`
  * `ec2:DescribeAvailabilityZones`
  * `ec2:EnableFastSnapshotRestores`

**Key Management Service (KMS)**

  * `kms:ReEncrypt*`
  * `kms:Decrypt`
  * `kms:Encrypt`
  * `kms:GenerateDataKey`
  * `kms:GenerateDataKeyWithoutPlainText`
  * `kms:DescribeKey`
  * `kms:RevokeGrant`[1]
  * `kms:CreateGrant` [1]
  * `kms:ListGrants` [1]

  
Show more

  1. Request condition: `kms:GrantIsForAWSResource: true`



### 21.5.1.4. OLM-managed Operator support for authentication with AWS STS

To allow certain Operators that are managed by the Operator Lifecycle Manager (OLM) on AWS clusters to authenticate with limited-privilege, short-term credentials that are managed outside the cluster, you can use manual mode with STS. 

To determine if an Operator supports authentication with AWS STS, see the Operator description in the software catalog. 

**Additional resources**

  * [CCO-based workflow for OLM-managed Operators with AWS STS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#osdk-cco-aws-sts)



## 21.5.2. About GCP Workload Identity

To allow components to use the Google Cloud Platform Workload Identity to impersonate Google Cloud service accounts using short-term, limited-privilege credentials, you can configure your cluster to use manual mode with GCP Workload Identity. 

**Additional resources**

  * [Configuring a Google Cloud cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-with-short-term-creds_installing-gcp-customizations)



### 21.5.2.1. Google Cloud Workload Identity authentication process

You should familiarize yourself with the Google Cloud Workload Identity authentication process. 

Requests for new and refreshed credentials are automated by using an appropriately configured OpenID Connect (OIDC) identity provider combined with IAM service accounts. Service account tokens that are trusted by Google Cloud are signed by OpenShift Container Platform and can be projected into a pod and used for authentication. Tokens are refreshed after one hour. 

The following diagram details the authentication flow between Google Cloud and the OpenShift Container Platform cluster when using Google Cloud Workload Identity. 

**Figure 21.3. Google Cloud Workload Identity authentication flow**

![Detailed authentication flow between Google Cloud and the cluster when using Google Cloud Workload Identity](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Authentication_and_authorization-en-US/images/b1951689e1229704bfae2fbc196336ae/347_OpenShift_credentials_with_STS_updates_0623_GCP.png) ![Detailed authentication flow between Google Cloud and the cluster when using Google Cloud Workload Identity](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Authentication_and_authorization-en-US/images/b1951689e1229704bfae2fbc196336ae/347_OpenShift_credentials_with_STS_updates_0623_GCP.png)

### 21.5.2.2. Google Cloud component secret formats

To change the content of the Google Cloud credentials that are provided to individual OpenShift Container Platform components, you can use manual mode with Google Cloud Workload Identity. 

Compare the following secret content: 

**Google Cloud secret format**

```yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace>
  name: <target_secret_name>
data:
  service_account.json: <service_account>
```


where: 

`metadata.namespace`
     Specifies the namespace for the component. 
`metadata.name`
     Specifies the name of the component secret. 
`data.service_account.json`
     Specifies the Base64 encoded service account. 

**Content of the Base64 encoded`service_account.json` file using long-term credentials**

```plaintext
{
   "type": "service_account",
   "project_id": "<project_id>",
   "private_key_id": "<private_key_id>",
   "private_key": "<private_key>",
   "client_email": "<client_email_address>",
   "client_id": "<client_id>",
   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
   "token_uri": "https://oauth2.googleapis.com/token",
   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/<client_email_address>"
}
```


where: 

`type`
     Specifies the credential type, in this example the type is `service_account`. 
`private_key`
     Specifies the private RSA key that is used to authenticate to Google Cloud. This key must be kept secure and is not rotated. 

**Content of the Base64 encoded`service_account.json` file using Google Cloud Workload Identity**

```plaintext
{
   "type": "external_account",
   "audience": "//iam.googleapis.com/projects/123456789/locations/global/workloadIdentityPools/test-pool/providers/test-provider",
   "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
   "token_url": "https://sts.googleapis.com/v1/token",
   "service_account_impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/<client_email_address>:generateAccessToken",
   "credential_source": {
      "file": "<path_to_token>",
      "format": {
         "type": "text"
      }
   }
}
```


where: 

`type`
     Specifies the credential type, in this example the type is `external_account`. 
`audience`
     Specifies the target audience is the Google Cloud Workload Identity provider. 
`service_account_impersonation_url`
     Specifies the resource URL of the service account that can be impersonated with these credentials. 
`credential_source.file`
     Specifies the path to the service account token inside the pod. By convention, this is `/var/run/secrets/openshift/serviceaccount/token` for OpenShift Container Platform components. 

### 21.5.2.3. Google Cloud component secret permissions requirements

OpenShift Container Platform components require the following permissions. These values are in the `CredentialsRequest` custom resource (CR) for each component. 

Note

These permissions apply to all resources. Unless specified, there are no request conditions on these permissions. 

Component| Custom resource| Required permissions for services  
---|---|---  
Cloud Controller Manager Operator  |  `openshift-gcp-ccm` |  Compute Engine 

  * `compute.addresses.create`
  * `compute.addresses.delete`
  * `compute.addresses.get`
  * `compute.addresses.list`
  * `compute.firewalls.create`
  * `compute.firewalls.delete`
  * `compute.firewalls.get`
  * `compute.firewalls.update`
  * `compute.forwardingRules.create`
  * `compute.forwardingRules.delete`
  * `compute.forwardingRules.get`
  * `compute.healthChecks.create`
  * `compute.healthChecks.delete`
  * `compute.healthChecks.get`
  * `compute.healthChecks.update`
  * `compute.httpHealthChecks.create`
  * `compute.httpHealthChecks.delete`
  * `compute.httpHealthChecks.get`
  * `compute.httpHealthChecks.update`
  * `compute.instanceGroups.create`
  * `compute.instanceGroups.delete`
  * `compute.instanceGroups.get`
  * `compute.instanceGroups.update`
  * `compute.instances.get`
  * `compute.instances.use`
  * `compute.regionBackendServices.create`
  * `compute.regionBackendServices.delete`
  * `compute.regionBackendServices.get`
  * `compute.regionBackendServices.update`
  * `compute.targetPools.addInstance`
  * `compute.targetPools.create`
  * `compute.targetPools.delete`
  * `compute.targetPools.get`
  * `compute.targetPools.removeInstance`
  * `compute.zones.list`

  
Cloud Credential Operator  |  `cloud-credential-operator-gcp-ro-creds` |  Identity and Access Management (IAM) 

  * `iam.roles.get`
  * `iam.serviceAccountKeys.list`
  * `iam.serviceAccounts.get`

Resource Manager 

  * `resourcemanager.projects.get`
  * `resourcemanager.projects.getIamPolicy`

Service Usage 

  * `serviceusage.services.list`

  
Cluster Image Registry Operator  |  `openshift-image-registry-gcs` |  Cloud Storage 

  * `storage.buckets.create`
  * `storage.buckets.createTagBinding`
  * `storage.buckets.delete`
  * `storage.buckets.get`
  * `storage.buckets.list`
  * `storage.buckets.listEffectiveTags`
  * `storage.objects.create`
  * `storage.objects.delete`
  * `storage.objects.get`
  * `storage.objects.list`

Resource Manager 

  * `resourcemanager.tagValueBindings.create`
  * `resourcemanager.tagValues.get`
  * `resourcemanager.tagValues.list`

  
Cluster Ingress Operator  |  `openshift-ingress-gcp` |  Cloud DNS 

  * `dns.changes.create`
  * `dns.resourceRecordSets.create`
  * `dns.resourceRecordSets.delete`
  * `dns.resourceRecordSets.list`
  * `dns.resourceRecordSets.update`

  
Cluster Network Operator  |  `openshift-cloud-network-config-controller-gcp` |  Compute Engine 

  * `compute.instances.get`
  * `compute.instances.updateNetworkInterface`
  * `compute.subnetworks.get`
  * `compute.subnetworks.use`
  * `compute.zoneOperations.get`

  
Cluster Storage Operator  |  `openshift-gcp-pd-csi-driver-operator` |  Compute Engine 

  * `compute.instances.attachDisk`
  * `compute.instances.detachDisk`
  * `compute.instances.get`

This component also requires the following Google Cloud predefined roles: 

  * `roles/compute.storageAdmin`
  * `roles/iam.serviceAccountUser`
  * `roles/resourcemanager.tagUser`

  
Machine API Operator  |  `openshift-machine-api-gcp` |  Compute Engine 

  * `compute.acceleratorTypes.get`
  * `compute.acceleratorTypes.list`
  * `compute.disks.create`
  * `compute.disks.createTagBinding`
  * `compute.disks.setLabels`
  * `compute.globalOperations.get`
  * `compute.globalOperations.list`
  * `compute.healthChecks.useReadOnly`
  * `compute.images.get`
  * `compute.images.getFromFamily`
  * `compute.images.useReadOnly`
  * `compute.instanceGroups.create`
  * `compute.instanceGroups.delete`
  * `compute.instanceGroups.get`
  * `compute.instanceGroups.list`
  * `compute.instanceGroups.update`
  * `compute.instances.create`
  * `compute.instances.createTagBinding`
  * `compute.instances.delete`
  * `compute.instances.get`
  * `compute.instances.list`
  * `compute.instances.setLabels`
  * `compute.instances.setMetadata`
  * `compute.instances.setServiceAccount`
  * `compute.instances.setTags`
  * `compute.instances.update`
  * `compute.instances.use`
  * `compute.machineTypes.get`
  * `compute.machineTypes.list`
  * `compute.projects.get`
  * `compute.regionBackendServices.create`
  * `compute.regionBackendServices.get`
  * `compute.regionBackendServices.update`
  * `compute.regions.get`
  * `compute.regions.list`
  * `compute.subnetworks.use`
  * `compute.subnetworks.useExternalIp`
  * `compute.targetPools.addInstance`
  * `compute.targetPools.delete`
  * `compute.targetPools.get`
  * `compute.targetPools.removeInstance`
  * `compute.zoneOperations.get`
  * `compute.zoneOperations.list`
  * `compute.zones.get`
  * `compute.zones.list`

Identity and Access Management (IAM) 

  * `iam.serviceAccounts.actAs`
  * `iam.serviceAccounts.get`
  * `iam.serviceAccounts.list`

Resource Manager 

  * `resourcemanager.tagValues.get`
  * `resourcemanager.tagValues.list`

Service Usage 

  * `serviceusage.quotas.get`
  * `serviceusage.services.get`
  * `serviceusage.services.list`

  
Show more

### 21.5.2.4. OLM-managed Operator support for authentication with GCP Workload Identity

To allow certain Operators that are managed by the Operator Lifecycle Manager (OLM) on Google Cloud clusters to authenticate with limited-privilege, short-term credentials that are managed outside the cluster, you can use manual mode with GCP Workload Identity. 

To determine if an Operator supports authentication with GCP Workload Identity, see the Operator description in the software catalog. 

**Additional resources**

  * [CCO-based workflow for OLM-managed Operators with Google Cloud Platform Workload Identity](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#osdk-cco-gcp)



### 21.5.2.5. Application support for GCP Workload Identity service account tokens

You can use GCP Workload Identity authentication with applications in customer workloads on OpenShift Container Platform clusters that use Google Cloud Platform Workload Identity. 

To use this authentication method with your applications, you must complete configuration steps on the cloud provider console and your OpenShift Container Platform cluster. 

**Additional resources**

  * [Configuring GCP Workload Identity authentication for applications on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-pods-short-term-auth-configuring-gcp_nodes-pods-short-term-auth)



## 21.5.3. About Microsoft Entra Workload ID

When you configure your cluster to use manual mode with Microsoft Entra Workload ID, the individual OpenShift Container Platform cluster components use the Workload ID provider to assign to components short-term security credentials. 

**Additional resources**

  * [Configuring a global Microsoft Azure cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-with-short-term-creds_installing-azure-customizations)



### 21.5.3.1. Microsoft Entra Workload ID authentication process

You should familiarize yourself with the Microsoft Entra Workload ID authentication flow. 

The following diagram details the authentication flow between Microsoft Azure and the OpenShift Container Platform cluster when using Workload ID. 

**Figure 21.4. Workload ID authentication flow**

![Detailed authentication flow between Azure and the cluster when using Workload ID](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Authentication_and_authorization-en-US/images/c4749ac419c575e47ceedd45e1cfa029/347_OpenShift_credentials_with_STS_updates_1023_Azure.png) ![Detailed authentication flow between Azure and the cluster when using Workload ID](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Authentication_and_authorization-en-US/images/c4749ac419c575e47ceedd45e1cfa029/347_OpenShift_credentials_with_STS_updates_1023_Azure.png)

### 21.5.3.2. Azure component secret formats

To change the content of the Azure credentials that are provided to individual OpenShift Container Platform components, you can use manual mode with with Microsoft Entra Workload ID. 

Compare the following secret formats: 

**Azure secret format using long-term credentials**

```yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace>
  name: <target_secret_name>
data:
  azure_client_id: <client_id>
  azure_client_secret: <client_secret>
  azure_region: <region>
  azure_resource_prefix: <resource_group_prefix>
  azure_resourcegroup: <resource_group_prefix>-rg
  azure_subscription_id: <subscription_id>
  azure_tenant_id: <tenant_id>
type: Opaque
```


where: 

`metadata.namespace`
     Specifies the namespace for the component. 
`metadata.name`
     Specifies the name of the component secret. 
`data.azure_client_id`
     Specifies the client ID of the Microsoft Entra ID identity that the component uses to authenticate. 
`data.azure_client_secret`
     Specifies the component secret that is used to authenticate with Microsoft Entra ID for the `<client_id>` identity. 
`data.azure_resource_prefix`
     Specifies the resource group prefix. 
`data.azure_resourcegroup`
     Specifies the resource group. This value is formed by the `<resource_group_prefix>` and the suffix `-rg`. 

**Azure secret format using Microsoft Entra Workload ID**

```yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace>
  name: <target_secret_name>
data:
  azure_client_id: <client_id>
  azure_federated_token_file: <path_to_token_file>
  azure_region: <region>
  azure_subscription_id: <subscription_id>
  azure_tenant_id: <tenant_id>
type: Opaque
```


where: 

`metadata.namespace`
     Specifies the namespace for the component. 
`metadata.name`
     Specifies the name of the component secret. 
`data.azure_client_id`
     Specifies the client ID of the user-assigned managed identity that the component uses to authenticate. 
`data.azure_federated_token_file`
     Specifies the path to the mounted service account token file. 

### 21.5.3.3. Azure component secret permissions requirements

You should familiarize yourself with the permissions required by the OpenShift Container Platform components. These values are in the `CredentialsRequest` custom resource (CR) for each component. 

Component| Custom resource| Required permissions for services  
---|---|---  
Cloud Controller Manager Operator  |  `openshift-azure-cloud-controller-manager` | 

  * `Microsoft.Compute/virtualMachines/read`
  * `Microsoft.Network/loadBalancers/read`
  * `Microsoft.Network/loadBalancers/write`
  * `Microsoft.Network/networkInterfaces/read`
  * `Microsoft.Network/networkSecurityGroups/read`
  * `Microsoft.Network/networkSecurityGroups/write`
  * `Microsoft.Network/publicIPAddresses/join/action`
  * `Microsoft.Network/publicIPAddresses/read`
  * `Microsoft.Network/publicIPAddresses/write`

  
Cluster CAPI Operator  |  `openshift-cluster-api-azure` |  role: `Contributor` [1]  
Machine API Operator  |  `openshift-machine-api-azure` | 

  * `Microsoft.Compute/availabilitySets/delete`
  * `Microsoft.Compute/availabilitySets/read`
  * `Microsoft.Compute/availabilitySets/write`
  * `Microsoft.Compute/diskEncryptionSets/read`
  * `Microsoft.Compute/disks/delete`
  * `Microsoft.Compute/galleries/images/versions/read`
  * `Microsoft.Compute/skus/read`
  * `Microsoft.Compute/virtualMachines/delete`
  * `Microsoft.Compute/virtualMachines/extensions/delete`
  * `Microsoft.Compute/virtualMachines/extensions/read`
  * `Microsoft.Compute/virtualMachines/extensions/write`
  * `Microsoft.Compute/virtualMachines/read`
  * `Microsoft.Compute/virtualMachines/write`
  * `Microsoft.ManagedIdentity/userAssignedIdentities/assign/action`
  * `Microsoft.Network/applicationSecurityGroups/read`
  * `Microsoft.Network/loadBalancers/backendAddressPools/join/action`
  * `Microsoft.Network/loadBalancers/read`
  * `Microsoft.Network/loadBalancers/write`
  * `Microsoft.Network/networkInterfaces/delete`
  * `Microsoft.Network/networkInterfaces/join/action`
  * `Microsoft.Network/networkInterfaces/loadBalancers/read`
  * `Microsoft.Network/networkInterfaces/read`
  * `Microsoft.Network/networkInterfaces/write`
  * `Microsoft.Network/networkSecurityGroups/read`
  * `Microsoft.Network/networkSecurityGroups/write`
  * `Microsoft.Network/publicIPAddresses/delete`
  * `Microsoft.Network/publicIPAddresses/join/action`
  * `Microsoft.Network/publicIPAddresses/read`
  * `Microsoft.Network/publicIPAddresses/write`
  * `Microsoft.Network/routeTables/read`
  * `Microsoft.Network/virtualNetworks/delete`
  * `Microsoft.Network/virtualNetworks/read`
  * `Microsoft.Network/virtualNetworks/subnets/join/action`
  * `Microsoft.Network/virtualNetworks/subnets/read`
  * `Microsoft.Resources/subscriptions/resourceGroups/read`

  
Cluster Image Registry Operator  |  `openshift-image-registry-azure` |  **Data permissions**

  * `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/delete`
  * `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/write`
  * `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/read`
  * `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/add/action`
  * `Microsoft.Storage/storageAccounts/blobServices/containers/blobs/move/action`

**General permissions**

  * `Microsoft.Storage/storageAccounts/blobServices/read`
  * `Microsoft.Storage/storageAccounts/blobServices/containers/read`
  * `Microsoft.Storage/storageAccounts/blobServices/containers/write`
  * `Microsoft.Storage/storageAccounts/blobServices/generateUserDelegationKey/action`
  * `Microsoft.Storage/storageAccounts/read`
  * `Microsoft.Storage/storageAccounts/write`
  * `Microsoft.Storage/storageAccounts/delete`
  * `Microsoft.Storage/storageAccounts/listKeys/action`
  * `Microsoft.Resources/tags/write`

  
Ingress Operator  |  `openshift-ingress-azure` | 

  * `Microsoft.Network/dnsZones/A/delete`
  * `Microsoft.Network/dnsZones/A/write`
  * `Microsoft.Network/privateDnsZones/A/delete`
  * `Microsoft.Network/privateDnsZones/A/write`

  
Cluster Network Operator  |  `openshift-cloud-network-config-controller-azure` | 

  * `Microsoft.Network/networkInterfaces/read`
  * `Microsoft.Network/networkInterfaces/write`
  * `Microsoft.Compute/virtualMachines/read`
  * `Microsoft.Network/virtualNetworks/read`
  * `Microsoft.Network/virtualNetworks/subnets/join/action`
  * `Microsoft.Network/loadBalancers/backendAddressPools/join/action`

  
Azure File CSI Driver Operator  |  `azure-file-csi-driver-operator` | 

  * `Microsoft.Network/networkSecurityGroups/join/action`
  * `Microsoft.Network/virtualNetworks/subnets/read`
  * `Microsoft.Network/virtualNetworks/subnets/write`
  * `Microsoft.Storage/storageAccounts/delete`
  * `Microsoft.Storage/storageAccounts/fileServices/read`
  * `Microsoft.Storage/storageAccounts/fileServices/shares/delete`
  * `Microsoft.Storage/storageAccounts/fileServices/shares/read`
  * `Microsoft.Storage/storageAccounts/fileServices/shares/write`
  * `Microsoft.Storage/storageAccounts/listKeys/action`
  * `Microsoft.Storage/storageAccounts/read`
  * `Microsoft.Storage/storageAccounts/write`

  
Azure Disk CSI Driver Operator  |  `azure-disk-csi-driver-operator` | 

  * `Microsoft.Compute/disks/*`
  * `Microsoft.Compute/snapshots/*`
  * `Microsoft.Compute/virtualMachineScaleSets/*/read`
  * `Microsoft.Compute/virtualMachineScaleSets/read`
  * `Microsoft.Compute/virtualMachineScaleSets/virtualMachines/write`
  * `Microsoft.Compute/virtualMachines/*/read`
  * `Microsoft.Compute/virtualMachines/write`
  * `Microsoft.Resources/subscriptions/resourceGroups/read`

  
Show more

  1. This component requires a role rather than a set of permissions. 



### 21.5.3.4. OLM-managed Operator support for authentication with Microsoft Entra Workload ID

To allow certain Operators that are managed by the Operator Lifecycle Manager (OLM) on Azure clusters to authenticate with limited-privilege, short-term credentials that are managed outside the cluster, you can use manual mode with Microsoft Entra Workload ID. 

To determine if an Operator supports authentication with Workload ID, see the Operator description in the software catalog. 

**Additional resources**

  * [CCO-based workflow for OLM-managed Operators with Microsoft Entra Workload ID](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#osdk-cco-azure)



## 21.5.4. Additional resources

  * [Enabling token-based authentication](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#post-install-enable-token-auth_changing-cloud-credentials-configuration)
  * [Configuring an AWS cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-with-short-term-creds_installing-aws-customizations)
  * [Configuring a Google Cloud cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-with-short-term-creds_installing-gcp-customizations)
  * [Configuring a global Microsoft Azure cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-with-short-term-creds_installing-azure-customizations)
  * [Preparing to update a cluster with manually maintained credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#preparing-manual-creds-update)
