# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  CustomResourceDefinitionSpec describes how a user wants their resource to appear   
`status` |  `object` |  CustomResourceDefinitionStatus indicates the state of the CustomResourceDefinition   
Show more

## 3.1.1. .spec

Description
     CustomResourceDefinitionSpec describes how a user wants their resource to appear 
Type
     `object`
Required
    

  * `group`
  * `names`
  * `scope`
  * `versions`



Property| Type| Description  
---|---|---  
`conversion` |  `object` |  CustomResourceConversion describes how to convert different versions of a CR.   
`group` |  `string` |  group is the API group of the defined custom resource. The custom resources are served under `/apis/<group>/…​`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`).   
`names` |  `object` |  CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition   
`preserveUnknownFields` |  `boolean` |  preserveUnknownFields indicates that object fields which are not specified in the OpenAPI schema should be preserved when persisting to storage. apiVersion, kind, metadata and known fields inside metadata are always preserved. This field is deprecated in favor of setting `x-preserve-unknown-fields` to true in `spec.versions[*].schema.openAPIV3Schema`. See <https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#field-pruning> for details.   
`scope` |  `string` |  scope indicates whether the defined custom resource is cluster- or namespace-scoped. Allowed values are `Cluster` and `Namespaced`.   
`versions` |  `array` |  versions is the list of all API versions of the defined custom resource. Version names are used to compute the order in which served versions are listed in API discovery. If the version string is "kube-like", it will sort above non "kube-like" version strings, which are ordered lexicographically. "Kube-like" versions start with a "v", then are followed by a number (the major version), then optionally the string "alpha" or "beta" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10.   
`versions[]` |  `object` |  CustomResourceDefinitionVersion describes a version for CRD.   
Show more

## 3.1.2. .spec.conversion

Description
     CustomResourceConversion describes how to convert different versions of a CR. 
Type
     `object`
Required
    

  * `strategy`



Property| Type| Description  
---|---|---  
`strategy` |  `string` |  strategy specifies how custom resources are converted between versions. Allowed values are: - `"None"`: The converter only change the apiVersion and would not touch any other field in the custom resource. - `"Webhook"`: API Server will call to an external webhook to do the conversion. Additional information is needed for this option. This requires spec.preserveUnknownFields to be false, and spec.conversion.webhook to be set.   
`webhook` |  `object` |  WebhookConversion describes how to call a conversion webhook   
Show more

## 3.1.3. .spec.conversion.webhook

Description
     WebhookConversion describes how to call a conversion webhook 
Type
     `object`
Required
    

  * `conversionReviewVersions`



Property| Type| Description  
---|---|---  
`clientConfig` |  `object` |  WebhookClientConfig contains the information to make a TLS connection with the webhook.   
`conversionReviewVersions` |  `array (string)` |  conversionReviewVersions is an ordered list of preferred `ConversionReview` versions the Webhook expects. The API server will use the first version in the list which it supports. If none of the versions specified in this list are supported by API server, conversion will fail for the custom resource. If a persisted Webhook configuration specifies allowed versions and does not include any versions known to the API Server, calls to the webhook will fail.   
Show more

## 3.1.4. .spec.conversion.webhook.clientConfig

Description
     WebhookClientConfig contains the information to make a TLS connection with the webhook. 
Type
     `object`

Property| Type| Description  
---|---|---  
`caBundle` |  `string` |  caBundle is a PEM encoded CA bundle which will be used to validate the webhook’s server certificate. If unspecified, system trust roots on the apiserver are used.   
`service` |  `object` |  ServiceReference holds a reference to Service.legacy.k8s.io   
`url` |  `string` |  url gives the location of the webhook, in standard URL form (`scheme://host:port/path`). Exactly one of `url` or `service` must be specified.  The `host` should not refer to a service running in the cluster; use the `service` field instead. The host might be resolved via external DNS in some apiservers (e.g., `kube-apiserver` cannot resolve in-cluster DNS as that would be a layering violation). `host` may also be an IP address.  Please note that using `localhost` or `127.0.0.1` as a `host` is risky unless you take great care to run this webhook on all hosts which run an apiserver which might need to make calls to this webhook. Such installs are likely to be non-portable, i.e., not easy to turn up in a new cluster.  The scheme must be "https"; the URL must begin with "https://".  A path is optional, and if present may be any string permissible in a URL. You may use the path to pass an arbitrary string to the webhook, for example, a cluster identifier.  Attempting to use a user or basic auth e.g. "user:password@" is not allowed. Fragments ("#…​") and query parameters ("?…​") are not allowed, either.   
Show more

## 3.1.5. .spec.conversion.webhook.clientConfig.service

Description
     ServiceReference holds a reference to Service.legacy.k8s.io 
Type
     `object`
Required
    

  * `namespace`
  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is the name of the service. Required   
`namespace` |  `string` |  namespace is the namespace of the service. Required   
`path` |  `string` |  path is an optional URL path at which the webhook will be contacted.   
`port` |  `integer` |  port is an optional service port at which the webhook will be contacted. `port` should be a valid port number (1-65535, inclusive). Defaults to 443 for backward compatibility.   
Show more

## 3.1.6. .spec.names

Description
     CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition 
Type
     `object`
Required
    

  * `plural`
  * `kind`



Property| Type| Description  
---|---|---  
`categories` |  `array (string)` |  categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by clients to support invocations like `kubectl get all`.   
`kind` |  `string` |  kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the `kind` attribute in API calls.   
`listKind` |  `string` |  listKind is the serialized kind of the list for this resource. Defaults to "`kind`List".   
`plural` |  `string` |  plural is the plural name of the resource to serve. The custom resources are served under `/apis/<group>/<version>/…​/<plural>`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). Must be all lowercase.   
`shortNames` |  `array (string)` |  shortNames are short names for the resource, exposed in API discovery documents, and used by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase.   
`singular` |  `string` |  singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased `kind`.   
Show more

## 3.1.7. .spec.versions

Description
     versions is the list of all API versions of the defined custom resource. Version names are used to compute the order in which served versions are listed in API discovery. If the version string is "kube-like", it will sort above non "kube-like" version strings, which are ordered lexicographically. "Kube-like" versions start with a "v", then are followed by a number (the major version), then optionally the string "alpha" or "beta" and another number (the minor version). These are sorted first by GA > beta > alpha (where GA is a version with no suffix such as beta or alpha), and then by comparing major version, then minor version. An example sorted list of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1, v11alpha2, foo1, foo10. 
Type
     `array`

## 3.1.8. .spec.versions[]

Description
     CustomResourceDefinitionVersion describes a version for CRD. 
Type
     `object`
Required
    

  * `name`
  * `served`
  * `storage`



Property| Type| Description  
---|---|---  
`additionalPrinterColumns` |  `array` |  additionalPrinterColumns specifies additional columns returned in Table output. See <https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables> for details. If no columns are specified, a single column displaying the age of the custom resource is used.   
`additionalPrinterColumns[]` |  `object` |  CustomResourceColumnDefinition specifies a column for server side printing.   
`deprecated` |  `boolean` |  deprecated indicates this version of the custom resource API is deprecated. When set to true, API requests to this version receive a warning header in the server response. Defaults to false.   
`deprecationWarning` |  `string` |  deprecationWarning overrides the default warning returned to API clients. May only be set when `deprecated` is true. The default warning indicates this version is deprecated and recommends use of the newest served version of equal or greater stability, if one exists.   
`name` |  `string` |  name is the version name, e.g. “v1”, “v2beta1”, etc. The custom resources are served under this version at `/apis/<group>/<version>/…​` if `served` is true.   
`schema` |  `object` |  CustomResourceValidation is a list of validation methods for CustomResources.   
`selectableFields` |  `array` |  selectableFields specifies paths to fields that may be used as field selectors. A maximum of 8 selectable fields are allowed. See <https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors>  
`selectableFields[]` |  `object` |  SelectableField specifies the JSON path of a field that may be used with field selectors.   
`served` |  `boolean` |  served is a flag enabling/disabling this version from being served via REST APIs   
`storage` |  `boolean` |  storage indicates this version should be used when persisting custom resources to storage. There must be exactly one version with storage=true.   
`subresources` |  `object` |  CustomResourceSubresources defines the status and scale subresources for CustomResources.   
Show more

## 3.1.9. .spec.versions[].additionalPrinterColumns

Description
     additionalPrinterColumns specifies additional columns returned in Table output. See <https://kubernetes.io/docs/reference/using-api/api-concepts/#receiving-resources-as-tables> for details. If no columns are specified, a single column displaying the age of the custom resource is used. 
Type
     `array`

## 3.1.10. .spec.versions[].additionalPrinterColumns[]

Description
     CustomResourceColumnDefinition specifies a column for server side printing. 
Type
     `object`
Required
    

  * `name`
  * `type`
  * `jsonPath`



Property| Type| Description  
---|---|---  
`description` |  `string` |  description is a human readable description of this column.   
`format` |  `string` |  format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See <https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types> for details.   
`jsonPath` |  `string` |  jsonPath is a simple JSON path (i.e. with array notation) which is evaluated against each custom resource to produce the value for this column.   
`name` |  `string` |  name is a human readable name for the column.   
`priority` |  `integer` |  priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a priority greater than 0.   
`type` |  `string` |  type is an OpenAPI type definition for this column. See <https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types> for details.   
Show more

## 3.1.11. .spec.versions[].schema

Description
     CustomResourceValidation is a list of validation methods for CustomResources. 
Type
     `object`

Property| Type| Description  
---|---|---  
`openAPIV3Schema` |  [``](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps) |  openAPIV3Schema is the OpenAPI v3 schema to use for validation and pruning.   
Show more

## 3.1.12. .spec.versions[].selectableFields

Description
     selectableFields specifies paths to fields that may be used as field selectors. A maximum of 8 selectable fields are allowed. See <https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors>
Type
     `array`

## 3.1.13. .spec.versions[].selectableFields[]

Description
     SelectableField specifies the JSON path of a field that may be used with field selectors. 
Type
     `object`
Required
    

  * `jsonPath`



Property| Type| Description  
---|---|---  
`jsonPath` |  `string` |  jsonPath is a simple JSON path which is evaluated against each custom resource to produce a field selector value. Only JSON paths without the array notation are allowed. Must point to a field of type string, boolean or integer. Types with enum values and strings with formats are allowed. If jsonPath refers to absent field in a resource, the jsonPath evaluates to an empty string. Must not point to metdata fields. Required.   
Show more

## 3.1.14. .spec.versions[].subresources

Description
     CustomResourceSubresources defines the status and scale subresources for CustomResources. 
Type
     `object`

Property| Type| Description  
---|---|---  
`scale` |  `object` |  CustomResourceSubresourceScale defines how to serve the scale subresource for CustomResources.   
`status` |  `object` |  CustomResourceSubresourceStatus defines how to serve the status subresource for CustomResources. Status is represented by the `.status` JSON path inside of a CustomResource. When set, * exposes a /status subresource for the custom resource * PUT requests to the /status subresource take a custom resource object, and ignore changes to anything except the status stanza * PUT/POST/PATCH requests to the custom resource ignore changes to the status stanza   
Show more

## 3.1.15. .spec.versions[].subresources.scale

Description
     CustomResourceSubresourceScale defines how to serve the scale subresource for CustomResources. 
Type
     `object`
Required
    

  * `specReplicasPath`
  * `statusReplicasPath`



Property| Type| Description  
---|---|---  
`labelSelectorPath` |  `string` |  labelSelectorPath defines the JSON path inside of a custom resource that corresponds to Scale `status.selector`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status` or `.spec`. Must be set to work with HorizontalPodAutoscaler. The field pointed by this JSON path must be a string field (not a complex selector struct) which contains a serialized label selector in string form. More info: <https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions#scale-subresource> If there is no value under the given path in the custom resource, the `status.selector` value in the `/scale` subresource will default to the empty string.   
`specReplicasPath` |  `string` |  specReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `spec.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.spec`. If there is no value under the given path in the custom resource, the `/scale` subresource will return an error on GET.   
`statusReplicasPath` |  `string` |  statusReplicasPath defines the JSON path inside of a custom resource that corresponds to Scale `status.replicas`. Only JSON paths without the array notation are allowed. Must be a JSON Path under `.status`. If there is no value under the given path in the custom resource, the `status.replicas` value in the `/scale` subresource will default to 0.   
Show more

## 3.1.16. .spec.versions[].subresources.status

Description
     CustomResourceSubresourceStatus defines how to serve the status subresource for CustomResources. Status is represented by the `.status` JSON path inside of a CustomResource. When set, * exposes a /status subresource for the custom resource * PUT requests to the /status subresource take a custom resource object, and ignore changes to anything except the status stanza * PUT/POST/PATCH requests to the custom resource ignore changes to the status stanza 
Type
     `object`

## 3.1.17. .status

Description
     CustomResourceDefinitionStatus indicates the state of the CustomResourceDefinition 
Type
     `object`

Property| Type| Description  
---|---|---  
`acceptedNames` |  `object` |  CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition   
`conditions` |  `array` |  conditions indicate state for particular aspects of a CustomResourceDefinition   
`conditions[]` |  `object` |  CustomResourceDefinitionCondition contains details for the current condition of this pod.   
`observedGeneration` |  `integer` |  The generation observed by the CRD controller.   
`storedVersions` |  `array (string)` |  storedVersions lists all versions of CustomResources that were ever persisted. Tracking these versions allows a migration path for stored versions in etcd. The field is mutable so a migration controller can finish a migration to another version (ensuring no old objects are left in storage), and then remove the rest of the versions from this list. Versions may not be removed from `spec.versions` while they exist in this list.   
Show more

## 3.1.18. .status.acceptedNames

Description
     CustomResourceDefinitionNames indicates the names to serve this CustomResourceDefinition 
Type
     `object`
Required
    

  * `plural`
  * `kind`



Property| Type| Description  
---|---|---  
`categories` |  `array (string)` |  categories is a list of grouped resources this custom resource belongs to (e.g. 'all'). This is published in API discovery documents, and used by clients to support invocations like `kubectl get all`.   
`kind` |  `string` |  kind is the serialized kind of the resource. It is normally CamelCase and singular. Custom resource instances will use this value as the `kind` attribute in API calls.   
`listKind` |  `string` |  listKind is the serialized kind of the list for this resource. Defaults to "`kind`List".   
`plural` |  `string` |  plural is the plural name of the resource to serve. The custom resources are served under `/apis/<group>/<version>/…​/<plural>`. Must match the name of the CustomResourceDefinition (in the form `<names.plural>.<group>`). Must be all lowercase.   
`shortNames` |  `array (string)` |  shortNames are short names for the resource, exposed in API discovery documents, and used by clients to support invocations like `kubectl get <shortname>`. It must be all lowercase.   
`singular` |  `string` |  singular is the singular name of the resource. It must be all lowercase. Defaults to lowercased `kind`.   
Show more

## 3.1.19. .status.conditions

Description
     conditions indicate state for particular aspects of a CustomResourceDefinition 
Type
     `array`

## 3.1.20. .status.conditions[]

Description
     CustomResourceDefinitionCondition contains details for the current condition of this pod. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  lastTransitionTime last time the condition transitioned from one status to another.   
`message` |  `string` |  message is a human-readable message indicating details about last transition.   
`observedGeneration` |  `integer` |  observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date with respect to the current state of the instance.   
`reason` |  `string` |  reason is a unique, one-word, CamelCase reason for the condition’s last transition.   
`status` |  `string` |  status is the status of the condition. Can be True, False, Unknown.   
`type` |  `string` |  type is the type of the condition. Types include Established, NamesAccepted and Terminating.   
Show more
