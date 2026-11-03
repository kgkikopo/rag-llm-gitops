# 4.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration   
`status` |  `object` |  status holds observed values from the cluster. They may not be overridden.   
Show more

## 4.1.1. .spec

Description
     spec holds user settable values for configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`driverConfig` |  `object` |  driverConfig can be used to specify platform specific driver configuration. When omitted, this means no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time.   
`logLevel` |  `string` |  logLevel is an intent based logging for an overall component. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for their operands.  Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal".   
`managementState` |  `string` |  managementState indicates whether and how the operator should manage the component   
`observedConfig` |  ``  |  observedConfig holds a sparse config that controller has observed from the cluster state. It exists in spec because it is an input to the level for the operator   
`operatorLogLevel` |  `string` |  operatorLogLevel is an intent based logging for the operator itself. It does not give fine grained control, but it is a simple way to manage coarse grained logging choices that operators have to interpret for themselves.  Valid values are: "Normal", "Debug", "Trace", "TraceAll". Defaults to "Normal".   
`storageClassState` |  `string` |  storageClassState determines if CSI operator should create and manage storage classes. If this field value is empty or Managed - CSI operator will continuously reconcile storage class and create if necessary. If this field value is Unmanaged - CSI operator will not reconcile any previously created storage class. If this field value is Removed - CSI operator will delete the storage class it created previously. When omitted, this means the user has no opinion and the platform chooses a reasonable default, which is subject to change over time. The current default behaviour is Managed.   
`unsupportedConfigOverrides` |  ``  |  unsupportedConfigOverrides overrides the final configuration that was computed by the operator. Red Hat does not support the use of this field. Misuse of this field could lead to unexpected behavior or conflict with other configuration options. Seek guidance from the Red Hat support before using this field. Use of this property blocks cluster upgrades, it must be removed before upgrading your cluster.   
Show more

## 4.1.2. .spec.driverConfig

Description
     driverConfig can be used to specify platform specific driver configuration. When omitted, this means no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. 
Type
     `object`
Required
    

  * `driverType`



Property| Type| Description  
---|---|---  
`aws` |  `object` |  aws is used to configure the AWS CSI driver.   
`azure` |  `object` |  azure is used to configure the Azure CSI driver.   
`driverType` |  `string` |  driverType indicates type of CSI driver for which the driverConfig is being applied to. Valid values are: AWS, Azure, GCP, IBMCloud, vSphere and omitted. Consumers should treat unknown values as a NO-OP.   
`gcp` |  `object` |  gcp is used to configure the GCP CSI driver.   
`ibmcloud` |  `object` |  ibmcloud is used to configure the IBM Cloud CSI driver.   
`vSphere` |  `object` |  vSphere is used to configure the vsphere CSI driver.   
Show more

## 4.1.3. .spec.driverConfig.aws

Description
     aws is used to configure the AWS CSI driver. 
Type
     `object`

Property| Type| Description  
---|---|---  
`efsVolumeMetrics` |  `object` |  efsVolumeMetrics sets the configuration for collecting metrics from EFS volumes used by the EFS CSI Driver.   
`kmsKeyARN` |  `string` |  kmsKeyARN sets the cluster default storage class to encrypt volumes with a user-defined KMS key, rather than the default KMS key used by AWS. The value may be either the ARN or Alias ARN of a KMS key.  The ARN must follow the format: arn:<partition>:kms:<region>:<account-id>:(key|alias)/<key-id-or-alias>, where: <partition> is the AWS partition (aws, aws-cn, aws-us-gov, aws-iso, aws-iso-b, aws-iso-e, aws-iso-f, or aws-eusc), <region> is the AWS region, <account-id> is a 12-digit numeric identifier for the AWS account, <key-id-or-alias> is the KMS key ID or alias name.   
Show more

## 4.1.4. .spec.driverConfig.aws.efsVolumeMetrics

Description
     efsVolumeMetrics sets the configuration for collecting metrics from EFS volumes used by the EFS CSI Driver. 
Type
     `object`
Required
    

  * `state`



Property| Type| Description  
---|---|---  
`recursiveWalk` |  `object` |  recursiveWalk provides additional configuration for collecting volume metrics in the AWS EFS CSI Driver when the state is set to RecursiveWalk.   
`state` |  `string` |  state defines the state of metric collection in the AWS EFS CSI Driver. This field is required and must be set to one of the following values: Disabled or RecursiveWalk. Disabled means no metrics collection will be performed. This is the default value. RecursiveWalk means the AWS EFS CSI Driver will recursively scan volumes to collect metrics. This process may result in high CPU and memory usage, depending on the volume size.   
Show more

## 4.1.5. .spec.driverConfig.aws.efsVolumeMetrics.recursiveWalk

Description
     recursiveWalk provides additional configuration for collecting volume metrics in the AWS EFS CSI Driver when the state is set to RecursiveWalk. 
Type
     `object`

Property| Type| Description  
---|---|---  
`fsRateLimit` |  `integer` |  fsRateLimit defines the rate limit, in goroutines per file system, for processing volume metrics. When omitted, this means no opinion and the platform is left to choose a reasonable default, which is subject to change over time. The current default is 5. The valid range is from 1 to 100 goroutines.   
`refreshPeriodMinutes` |  `integer` |  refreshPeriodMinutes specifies the frequency, in minutes, at which volume metrics are refreshed. When omitted, this means no opinion and the platform is left to choose a reasonable default, which is subject to change over time. The current default is 240. The valid range is from 1 to 43200 minutes (30 days).   
Show more

## 4.1.6. .spec.driverConfig.azure

Description
     azure is used to configure the Azure CSI driver. 
Type
     `object`

Property| Type| Description  
---|---|---  
`diskEncryptionSet` |  `object` |  diskEncryptionSet sets the cluster default storage class to encrypt volumes with a customer-managed encryption set, rather than the default platform-managed keys.   
Show more

## 4.1.7. .spec.driverConfig.azure.diskEncryptionSet

Description
     diskEncryptionSet sets the cluster default storage class to encrypt volumes with a customer-managed encryption set, rather than the default platform-managed keys. 
Type
     `object`
Required
    

  * `name`
  * `resourceGroup`
  * `subscriptionID`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the disk encryption set that will be set on the default storage class. The value should consist of only alphanumberic characters, underscores (_), hyphens, and be at most 80 characters in length.   
`resourceGroup` |  `string` |  resourceGroup defines the Azure resource group that contains the disk encryption set. The value should consist of only alphanumberic characters, underscores (_), parentheses, hyphens and periods. The value should not end in a period and be at most 90 characters in length.   
`subscriptionID` |  `string` |  subscriptionID defines the Azure subscription that contains the disk encryption set. The value should meet the following conditions: 1. It should be a 128-bit number. 2. It should be 36 characters (32 hexadecimal characters and 4 hyphens) long. 3. It should be displayed in five groups separated by hyphens (-). 4. The first group should be 8 characters long. 5. The second, third, and fourth groups should be 4 characters long. 6. The fifth group should be 12 characters long. An Example SubscrionID: f2007bbf-f802-4a47-9336-cf7c6b89b378   
Show more

## 4.1.8. .spec.driverConfig.gcp

Description
     gcp is used to configure the GCP CSI driver. 
Type
     `object`

Property| Type| Description  
---|---|---  
`kmsKey` |  `object` |  kmsKey sets the cluster default storage class to encrypt volumes with customer-supplied encryption keys, rather than the default keys managed by GCP.   
Show more

## 4.1.9. .spec.driverConfig.gcp.kmsKey

Description
     kmsKey sets the cluster default storage class to encrypt volumes with customer-supplied encryption keys, rather than the default keys managed by GCP. 
Type
     `object`
Required
    

  * `keyRing`
  * `name`
  * `projectID`



Property| Type| Description  
---|---|---  
`keyRing` |  `string` |  keyRing is the name of the KMS Key Ring which the KMS Key belongs to. The value should correspond to an existing KMS key ring and should consist of only alphanumeric characters, hyphens (-) and underscores (_), and be at most 63 characters in length.   
`location` |  `string` |  location is the GCP location in which the Key Ring exists. The value must match an existing GCP location, or "global". Defaults to global, if not set.   
`name` |  `string` |  name is the name of the customer-managed encryption key to be used for disk encryption. The value should correspond to an existing KMS key and should consist of only alphanumeric characters, hyphens (-) and underscores (_), and be at most 63 characters in length.   
`projectID` |  `string` |  projectID is the ID of the Project in which the KMS Key Ring exists. It must be 6 to 30 lowercase letters, digits, or hyphens. It must start with a letter. Trailing hyphens are prohibited.   
Show more

## 4.1.10. .spec.driverConfig.ibmcloud

Description
     ibmcloud is used to configure the IBM Cloud CSI driver. 
Type
     `object`
Required
    

  * `encryptionKeyCRN`



Property| Type| Description  
---|---|---  
`encryptionKeyCRN` |  `string` |  encryptionKeyCRN is the IBM Cloud CRN of the customer-managed root key to use for disk encryption of volumes for the default storage classes.   
Show more

## 4.1.11. .spec.driverConfig.vSphere

Description
     vSphere is used to configure the vsphere CSI driver. 
Type
     `object`

Property| Type| Description  
---|---|---  
`globalMaxSnapshotsPerBlockVolume` |  `integer` |  globalMaxSnapshotsPerBlockVolume is a global configuration parameter that applies to volumes on all kinds of datastores. If omitted, the platform chooses a default, which is subject to change over time, currently that default is 3. Snapshots can not be disabled using this parameter. Increasing number of snapshots above 3 can have negative impact on performance, for more details see: <https://kb.vmware.com/s/article/1025279> Volume snapshot documentation: <https://docs.vmware.com/en/VMware-vSphere-Container-Storage-Plug-in/3.0/vmware-vsphere-csp-getting-started/GUID-E0B41C69-7EEB-450F-A73D-5FD2FF39E891.html>  
`granularMaxSnapshotsPerBlockVolumeInVSAN` |  `integer` |  granularMaxSnapshotsPerBlockVolumeInVSAN is a granular configuration parameter on vSAN datastore only. It overrides GlobalMaxSnapshotsPerBlockVolume if set, while it falls back to the global constraint if unset. Snapshots for VSAN can not be disabled using this parameter.   
`granularMaxSnapshotsPerBlockVolumeInVVOL` |  `integer` |  granularMaxSnapshotsPerBlockVolumeInVVOL is a granular configuration parameter on Virtual Volumes datastore only. It overrides GlobalMaxSnapshotsPerBlockVolume if set, while it falls back to the global constraint if unset. Snapshots for VVOL can not be disabled using this parameter.   
`topologyCategories` |  `array (string)` |  topologyCategories indicates tag categories with which vcenter resources such as hostcluster or datacenter were tagged with. If cluster Infrastructure object has a topology, values specified in Infrastructure object will be used and modifications to topologyCategories will be rejected.   
Show more

## 4.1.12. .status

Description
     status holds observed values from the cluster. They may not be overridden. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions is a list of conditions and their status   
`conditions[]` |  `object` |  OperatorCondition is just the standard condition fields.   
`generations` |  `array` |  generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction.   
`generations[]` |  `object` |  GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made.   
`latestAvailableRevision` |  `integer` |  latestAvailableRevision is the deploymentID of the most recent deployment   
`observedGeneration` |  `integer` |  observedGeneration is the last generation change you’ve dealt with   
`readyReplicas` |  `integer` |  readyReplicas indicates how many replicas are ready and at the desired state   
`version` |  `string` |  version is the level this availability applies to   
Show more

## 4.1.13. .status.conditions

Description
     conditions is a list of conditions and their status 
Type
     `array`

## 4.1.14. .status.conditions[]

Description
     OperatorCondition is just the standard condition fields. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`message` |  `string` |   
`reason` |  `string` |   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase.   
Show more

## 4.1.15. .status.generations

Description
     generations are used to determine when an item needs to be reconciled or has changed in a way that needs a reaction. 
Type
     `array`

## 4.1.16. .status.generations[]

Description
     GenerationStatus keeps track of the generation for a given resource so that decisions about forced updates can be made. 
Type
     `object`
Required
    

  * `group`
  * `name`
  * `namespace`
  * `resource`



Property| Type| Description  
---|---|---  
`group` |  `string` |  group is the group of the thing you’re tracking   
`hash` |  `string` |  hash is an optional field set for resources without generation that are content sensitive like secrets and configmaps   
`lastGeneration` |  `integer` |  lastGeneration is the last generation of the workload controller involved   
`name` |  `string` |  name is the name of the thing you’re tracking   
`namespace` |  `string` |  namespace is where the thing you’re tracking is   
`resource` |  `string` |  resource is the resource type of the thing you’re tracking   
Show more
