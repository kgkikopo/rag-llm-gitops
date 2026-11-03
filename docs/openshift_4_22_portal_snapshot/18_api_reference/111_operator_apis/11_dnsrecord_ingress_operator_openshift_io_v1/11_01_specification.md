# 11.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec is the specification of the desired behavior of the dnsRecord.   
`status` |  `object` |  status is the most recently observed status of the dnsRecord.   
Show more

## 11.1.1. .spec

Description
     spec is the specification of the desired behavior of the dnsRecord. 
Type
     `object`
Required
    

  * `dnsManagementPolicy`
  * `dnsName`
  * `recordTTL`
  * `recordType`
  * `targets`



Property| Type| Description  
---|---|---  
`dnsManagementPolicy` |  `string` |  dnsManagementPolicy denotes the current policy applied on the DNS record. Records that have policy set as "Unmanaged" are ignored by the ingress operator. This means that the DNS record on the cloud provider is not managed by the operator, and the "Published" status condition will be updated to "Unknown" status, since it is externally managed. Any existing record on the cloud provider can be deleted at the discretion of the cluster admin.  This field defaults to Managed. Valid values are "Managed" and "Unmanaged".   
`dnsName` |  `string` |  dnsName is the hostname of the DNS record   
`recordTTL` |  `integer` |  recordTTL is the record TTL in seconds. If zero, the default is 30. RecordTTL will not be used in AWS regions Alias targets, but will be used in CNAME targets, per AWS API contract.   
`recordType` |  `string` |  recordType is the DNS record type. For example, "A", "AAAA", or "CNAME".   
`targets` |  `array (string)` |  targets are record targets.   
Show more

## 11.1.2. .status

Description
     status is the most recently observed status of the dnsRecord. 
Type
     `object`

Property| Type| Description  
---|---|---  
`observedGeneration` |  `integer` |  observedGeneration is the most recently observed generation of the DNSRecord. When the DNSRecord is updated, the controller updates the corresponding record in each managed zone. If an update for a particular zone fails, that failure is recorded in the status condition for the zone so that the controller can determine that it needs to retry the update for that specific zone.   
`zones` |  `array` |  zones are the status of the record in each zone.   
`zones[]` |  `object` |  DNSZoneStatus is the status of a record within a specific zone.   
Show more

## 11.1.3. .status.zones

Description
     zones are the status of the record in each zone. 
Type
     `array`

## 11.1.4. .status.zones[]

Description
     DNSZoneStatus is the status of a record within a specific zone. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions are any conditions associated with the record in the zone.  If publishing the record succeeds, the "Published" condition will be set with status "True" and upon failure it will be set to "False" along with the reason and message describing the cause of the failure.   
`conditions[]` |  `object` |  DNSZoneCondition is just the standard condition fields.   
`dnsZone` |  `object` |  dnsZone is the zone where the record is published.   
Show more

## 11.1.5. .status.zones[].conditions

Description
    

conditions are any conditions associated with the record in the zone. 

If publishing the record succeeds, the "Published" condition will be set with status "True" and upon failure it will be set to "False" along with the reason and message describing the cause of the failure. 

Type
     `array`

## 11.1.6. .status.zones[].conditions[]

Description
     DNSZoneCondition is just the standard condition fields. 
Type
     `object`
Required
    

  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |   
`message` |  `string` |   
`reason` |  `string` |   
`status` |  `string` |   
`type` |  `string` |   
Show more

## 11.1.7. .status.zones[].dnsZone

Description
     dnsZone is the zone where the record is published. 
Type
     `object`

Property| Type| Description  
---|---|---  
`id` |  `string` |  id is the identifier that can be used to find the DNS hosted zone.  on AWS zone can be fetched using `ID` as id in [1] on Azure zone can be fetched using `ID` as a pre-determined name in [2], on GCP zone can be fetched using `ID` as a pre-determined name in [3].  [1]: <https://docs.aws.amazon.com/cli/latest/reference/route53/get-hosted-zone.html#options> [2]: <https://docs.microsoft.com/en-us/cli/azure/network/dns/zone?view=azure-cli-latest#az-network-dns-zone-show> [3]: <https://cloud.google.com/dns/docs/reference/v1/managedZones/get>  
`tags` |  `object (string)` |  tags can be used to query the DNS hosted zone.  on AWS, resourcegroupstaggingapi [1] can be used to fetch a zone using `Tags` as tag-filters,  [1]: <https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/get-resources.html#options>  
Show more
