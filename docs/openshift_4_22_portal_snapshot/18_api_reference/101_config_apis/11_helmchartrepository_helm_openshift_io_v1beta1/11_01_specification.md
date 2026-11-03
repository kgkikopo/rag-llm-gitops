# 11.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec holds user settable values for configuration   
`status` |  `object` |  Observed status of the repository within the cluster..   
Show more

## 11.1.1. .spec

Description
     spec holds user settable values for configuration 
Type
     `object`

Property| Type| Description  
---|---|---  
`connectionConfig` |  `object` |  Required configuration for connecting to the chart repo   
`description` |  `string` |  Optional human readable repository description, it can be used by UI for displaying purposes   
`disabled` |  `boolean` |  If set to true, disable the repo usage in the cluster/namespace   
`name` |  `string` |  Optional associated human readable repository name, it can be used by UI for displaying purposes   
Show more

## 11.1.2. .spec.connectionConfig

Description
     Required configuration for connecting to the chart repo 
Type
     `object`

Property| Type| Description  
---|---|---  
`ca` |  `object` |  ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca-bundle.crt" is used to locate the data. If empty, the default system roots are used. The namespace for this config map is openshift-config.   
`tlsClientConfig` |  `object` |  tlsClientConfig is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate and private key to present when connecting to the server. The key "tls.crt" is used to locate the client certificate. The key "tls.key" is used to locate the private key. The namespace for this secret is openshift-config.   
`url` |  `string` |  Chart repository URL   
Show more

## 11.1.3. .spec.connectionConfig.ca

Description
     ca is an optional reference to a config map by name containing the PEM-encoded CA bundle. It is used as a trust anchor to validate the TLS certificate presented by the remote server. The key "ca-bundle.crt" is used to locate the data. If empty, the default system roots are used. The namespace for this config map is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced config map   
Show more

## 11.1.4. .spec.connectionConfig.tlsClientConfig

Description
     tlsClientConfig is an optional reference to a secret by name that contains the PEM-encoded TLS client certificate and private key to present when connecting to the server. The key "tls.crt" is used to locate the client certificate. The key "tls.key" is used to locate the private key. The namespace for this secret is openshift-config. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the metadata.name of the referenced secret   
Show more

## 11.1.5. .status

Description
     Observed status of the repository within the cluster.. 
Type
     `object`

Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions is a list of conditions and their statuses   
`conditions[]` |  `object` |  Condition contains details for one aspect of the current state of this API Resource.   
Show more

## 11.1.6. .status.conditions

Description
     conditions is a list of conditions and their statuses 
Type
     `array`

## 11.1.7. .status.conditions[]

Description
     Condition contains details for one aspect of the current state of this API Resource. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `message`
  * `reason`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.   
`message` |  `string` |  message is a human readable message indicating details about the transition. This may be an empty string.   
`observedGeneration` |  `integer` |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`reason` |  `string` |  reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty.   
`status` |  `string` |  status of the condition, one of True, False, Unknown.   
`type` |  `string` |  type of condition in CamelCase or in foo.example.com/CamelCase.   
Show more
