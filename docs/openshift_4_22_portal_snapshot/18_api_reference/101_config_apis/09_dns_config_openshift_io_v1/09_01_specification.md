# 9.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration   
`status` |  `object` |  status holds observed values from the cluster. They may not be overridden.   
Show more

## 9.1.1. .spec

Description
     spec holds user settable values for configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`baseDomain` |  `string` |  baseDomain is the base domain of the cluster. All managed DNS records will be sub-domains of this base.  For example, given the base domain `openshift.example.com`, an API server DNS record may be created for `cluster-api.openshift.example.com`.  Once set, this field cannot be changed.   
`platform` |  `object` |  platform holds configuration specific to the underlying infrastructure provider for DNS. When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time.   
`privateZone` |  `object` |  privateZone is the location where all the DNS records that are only available internally to the cluster exist.  If this field is nil, no private records should be created.  Once set, this field cannot be changed.   
`publicZone` |  `object` |  publicZone is the location where all the DNS records that are publicly accessible to the internet exist.  If this field is nil, no public records should be created.  Once set, this field cannot be changed.   
Show more

## 9.1.2. .spec.platform

Description
     platform holds configuration specific to the underlying infrastructure provider for DNS. When omitted, this means the user has no opinion and the platform is left to choose reasonable defaults. These defaults are subject to change over time. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`aws` |  `object` |  aws contains DNS configuration specific to the Amazon Web Services cloud provider.   
`type` |  `string` |  type is the underlying infrastructure provider for the cluster. Allowed values: "", "AWS".  Individual components may not support all platforms, and must handle unrecognized platforms with best-effort defaults.   
Show more

## 9.1.3. .spec.platform.aws

Description
     aws contains DNS configuration specific to the Amazon Web Services cloud provider. 
Type
     `object`

Property| Type| Description  
---|---|---  
`privateZoneIAMRole` |  `string` |  privateZoneIAMRole contains the ARN of an IAM role that should be assumed when performing operations on the cluster’s private hosted zone specified in the cluster DNS config. When left empty, no role should be assumed.  The ARN must follow the format: arn:<partition>:iam::<account-id>:role/<role-name>, where: <partition> is the AWS partition (aws, aws-cn, aws-us-gov, or aws-eusc), <account-id> is a 12-digit numeric identifier for the AWS account, <role-name> is the IAM role name.   
Show more

## 9.1.4. .spec.privateZone

Description
    

privateZone is the location where all the DNS records that are only available internally to the cluster exist. 

If this field is nil, no private records should be created. 

Once set, this field cannot be changed. 

Type
     `object`

Property| Type| Description  
---|---|---  
`id` |  `string` |  id is the identifier that can be used to find the DNS hosted zone.  on AWS zone can be fetched using `ID` as id in [1] on Azure zone can be fetched using `ID` as a pre-determined name in [2], on GCP zone can be fetched using `ID` as a pre-determined name in [3].  [1]: <https://docs.aws.amazon.com/cli/latest/reference/route53/get-hosted-zone.html#options> [2]: <https://docs.microsoft.com/en-us/cli/azure/network/dns/zone?view=azure-cli-latest#az-network-dns-zone-show> [3]: <https://cloud.google.com/dns/docs/reference/v1/managedZones/get>  
`tags` |  `object (string)` |  tags can be used to query the DNS hosted zone.  on AWS, resourcegroupstaggingapi [1] can be used to fetch a zone using `Tags` as tag-filters,  [1]: <https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/get-resources.html#options>  
Show more

## 9.1.5. .spec.publicZone

Description
    

publicZone is the location where all the DNS records that are publicly accessible to the internet exist. 

If this field is nil, no public records should be created. 

Once set, this field cannot be changed. 

Type
     `object`

Property| Type| Description  
---|---|---  
`id` |  `string` |  id is the identifier that can be used to find the DNS hosted zone.  on AWS zone can be fetched using `ID` as id in [1] on Azure zone can be fetched using `ID` as a pre-determined name in [2], on GCP zone can be fetched using `ID` as a pre-determined name in [3].  [1]: <https://docs.aws.amazon.com/cli/latest/reference/route53/get-hosted-zone.html#options> [2]: <https://docs.microsoft.com/en-us/cli/azure/network/dns/zone?view=azure-cli-latest#az-network-dns-zone-show> [3]: <https://cloud.google.com/dns/docs/reference/v1/managedZones/get>  
`tags` |  `object (string)` |  tags can be used to query the DNS hosted zone.  on AWS, resourcegroupstaggingapi [1] can be used to fetch a zone using `Tags` as tag-filters,  [1]: <https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/get-resources.html#options>  
Show more

## 9.1.6. .status

Description
     status holds observed values from the cluster. They may not be overridden. 
Type
     `object`
