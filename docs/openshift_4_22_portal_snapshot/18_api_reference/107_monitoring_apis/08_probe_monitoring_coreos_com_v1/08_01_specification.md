# 8.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec defines the specification of desired Ingress selection for target discovery by Prometheus.   
`status` |  `object` |  status defines the status subresource. It is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled.  Most recent observed status of the Probe. Read-only. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>  
Show more

## 8.1.1. .spec

Description
     spec defines the specification of desired Ingress selection for target discovery by Prometheus. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization configures the Authorization header credentials used by the client.  Cannot be set at the same time as `basicAuth`, `bearerTokenSecret` or `oauth2`.   
`basicAuth` |  `object` |  basicAuth defines the Basic Authentication credentials used by the client.  Cannot be set at the same time as `authorization`, `bearerTokenSecret` or `oauth2`.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines a key of a Secret containing the bearer token used by the client for authentication. The secret needs to be in the same namespace as the custom resource and readable by the Prometheus Operator.  Cannot be set at the same time as `authorization`, `basicAuth` or `oauth2`.  Deprecated: use `authorization` instead.   
`convertClassicHistogramsToNHCB` |  `boolean` |  convertClassicHistogramsToNHCB defines whether to convert all scraped classic histograms into a native histogram with custom buckets. It requires Prometheus >= v3.0.0.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`fallbackScrapeProtocol` |  `string` |  fallbackScrapeProtocol defines the protocol to use if a scrape returns blank, unparseable, or otherwise invalid Content-Type.  It requires Prometheus >= v3.0.0.   
`followRedirects` |  `boolean` |  followRedirects defines whether the client should follow HTTP 3xx redirects.   
`interval` |  `string` |  interval at which targets are probed using the configured prober. If not specified Prometheus' global scrape interval is used.   
`jobName` |  `string` |  jobName assigned to scraped metrics by default.   
`keepDroppedTargets` |  `integer` |  keepDroppedTargets defines the per-scrape limit on the number of targets dropped by relabeling that will be kept in memory. 0 means no limit.  It requires Prometheus >= v2.47.0.   
`labelLimit` |  `integer` |  labelLimit defines the per-scrape limit on number of labels that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.   
`labelNameLengthLimit` |  `integer` |  labelNameLengthLimit defines the per-scrape limit on length of labels name that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.   
`labelValueLengthLimit` |  `integer` |  labelValueLengthLimit defines the per-scrape limit on length of labels value that will be accepted for a sample. Only valid in Prometheus versions 2.27.0 and newer.   
`metricRelabelings` |  `array` |  metricRelabelings defines the RelabelConfig to apply to samples before ingestion.   
`metricRelabelings[]` |  `object` |  RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples.  More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>  
`module` |  `string` |  module to use for probing specifying how to probe the target. Example module configuring in the blackbox exporter: <https://github.com/prometheus/blackbox_exporter/blob/master/example.yml>  
`nativeHistogramBucketLimit` |  `integer` |  nativeHistogramBucketLimit defines ff there are more than this many buckets in a native histogram, buckets will be merged to stay within the limit. It requires Prometheus >= v2.45.0.   
`nativeHistogramMinBucketFactor` |  `integer-or-string` |  nativeHistogramMinBucketFactor defines if the growth factor of one bucket to the next is smaller than this, buckets will be merged to increase the factor sufficiently. It requires Prometheus >= v2.50.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 settings used by the client.  It requires Prometheus >= 2.27.0.  Cannot be set at the same time as `authorization`, `basicAuth` or `bearerTokenSecret`.   
`params` |  `array` |  params defines the list of HTTP query parameters for the scrape. Please note that the `.spec.module` field takes precedence over the `module` parameter from this list when both are defined. The module name must be added using Module under ProbeSpec.   
`params[]` |  `object` |  ProbeParam defines specification of extra parameters for a Probe.   
`prober` |  `object` |  prober defines the specification for the prober to use for probing targets. The prober.URL parameter is required. Targets cannot be probed if left empty.   
`sampleLimit` |  `integer` |  sampleLimit defines per-scrape limit on number of scraped samples that will be accepted.   
`scrapeClass` |  `string` |  scrapeClass defines the scrape class to apply.   
`scrapeClassicHistograms` |  `boolean` |  scrapeClassicHistograms defines whether to scrape a classic histogram that is also exposed as a native histogram. It requires Prometheus >= v2.45.0.  Notice: `scrapeClassicHistograms` corresponds to the `always_scrape_classic_histograms` field in the Prometheus configuration.   
`scrapeNativeHistograms` |  `boolean` |  scrapeNativeHistograms defines whether to enable scraping of native histograms. It requires Prometheus >= v3.8.0.   
`scrapeProtocols` |  `array (string)` |  scrapeProtocols defines the protocols to negotiate during a scrape. It tells clients the protocols supported by Prometheus in order of preference (from most to least preferred).  If unset, Prometheus uses its default value.  It requires Prometheus >= v2.49.0.   
`scrapeTimeout` |  `string` |  scrapeTimeout defines the timeout for scraping metrics from the Prometheus exporter. If not specified, the Prometheus global scrape timeout is used. The value cannot be greater than the scrape interval otherwise the operator will reject the resource.   
`targetLimit` |  `integer` |  targetLimit defines a limit on the number of scraped targets that will be accepted.   
`targets` |  `object` |  targets defines a set of static or dynamically discovered targets to probe.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration used by the client.   
Show more

## 8.1.2. .spec.authorization

Description
    

authorization configures the Authorization header credentials used by the client. 

Cannot be set at the same time as `basicAuth`, `bearerTokenSecret` or `oauth2`. 

Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 8.1.3. .spec.authorization.credentials

Description
     credentials defines a key of a Secret in the namespace that contains the credentials for authentication. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.4. .spec.basicAuth

Description
    

basicAuth defines the Basic Authentication credentials used by the client. 

Cannot be set at the same time as `authorization`, `bearerTokenSecret` or `oauth2`. 

Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 8.1.5. .spec.basicAuth.password

Description
     password defines a key of a Secret containing the password for authentication. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.6. .spec.basicAuth.username

Description
     username defines a key of a Secret containing the username for authentication. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.7. .spec.bearerTokenSecret

Description
    

bearerTokenSecret defines a key of a Secret containing the bearer token used by the client for authentication. The secret needs to be in the same namespace as the custom resource and readable by the Prometheus Operator. 

Cannot be set at the same time as `authorization`, `basicAuth` or `oauth2`. 

Deprecated: use `authorization` instead. 

Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.8. .spec.metricRelabelings

Description
     metricRelabelings defines the RelabelConfig to apply to samples before ingestion. 
Type
     `array`

## 8.1.9. .spec.metricRelabelings[]

Description
    

RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples. 

More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>

Type
     `object`

Property| Type| Description  
---|---|---  
`action` |  `string` |  action to perform based on the regex matching.  `Uppercase` and `Lowercase` actions require Prometheus >= v2.36.0. `DropEqual` and `KeepEqual` actions require Prometheus >= v2.41.0.  Default: "Replace"   
`modulus` |  `integer` |  modulus to take of the hash of the source label values.  Only applicable when the action is `HashMod`.   
`regex` |  `string` |  regex defines the regular expression against which the extracted value is matched.   
`replacement` |  `string` |  replacement value against which a Replace action is performed if the regular expression matches.  Regex capture groups are available.   
`separator` |  `string` |  separator defines the string between concatenated SourceLabels.   
`sourceLabels` |  `array (string)` |  sourceLabels defines the source labels select values from existing labels. Their content is concatenated using the configured Separator and matched against the configured regular expression.   
`targetLabel` |  `string` |  targetLabel defines the label to which the resulting string is written in a replacement.  It is mandatory for `Replace`, `HashMod`, `Lowercase`, `Uppercase`, `KeepEqual` and `DropEqual` actions.  Regex capture groups are available.   
Show more

## 8.1.10. .spec.oauth2

Description
    

oauth2 defines the OAuth2 settings used by the client. 

It requires Prometheus >= 2.27.0. 

Cannot be set at the same time as `authorization`, `basicAuth` or `bearerTokenSecret`. 

Type
     `object`
Required
    

  * `clientId`
  * `clientSecret`
  * `tokenUrl`



Property| Type| Description  
---|---|---  
`clientId` |  `object` |  clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID.   
`clientSecret` |  `object` |  clientSecret defines a key of a Secret containing the OAuth2 client’s secret.   
`endpointParams` |  `object (string)` |  endpointParams configures the HTTP parameters to append to the token URL.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`scopes` |  `array (string)` |  scopes defines the OAuth2 scopes used for the token request.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration to use when connecting to the OAuth2 server. It requires Prometheus >= v2.43.0.   
`tokenUrl` |  `string` |  tokenUrl defines the URL to fetch the token from.   
Show more

## 8.1.11. .spec.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 8.1.12. .spec.oauth2.clientId.configMap

Description
     configMap defines the ConfigMap containing data to use for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key to select.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the ConfigMap or its key must be defined   
Show more

## 8.1.13. .spec.oauth2.clientId.secret

Description
     secret defines the Secret containing data to use for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.14. .spec.oauth2.clientSecret

Description
     clientSecret defines a key of a Secret containing the OAuth2 client’s secret. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.15. .spec.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 8.1.16. .spec.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 8.1.17. .spec.oauth2.proxyConnectHeader{}[]

Description
     SecretKeySelector selects a key of a Secret. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.18. .spec.oauth2.tlsConfig

Description
     tlsConfig defines the TLS configuration to use when connecting to the OAuth2 server. It requires Prometheus >= v2.43.0. 
Type
     `object`

Property| Type| Description  
---|---|---  
`ca` |  `object` |  ca defines the Certificate authority used when verifying server certificates.   
`cert` |  `object` |  cert defines the Client certificate to present when doing client-authentication.   
`insecureSkipVerify` |  `boolean` |  insecureSkipVerify defines how to disable target certificate validation.   
`keySecret` |  `object` |  keySecret defines the Secret containing the client key file for the targets.   
`maxVersion` |  `string` |  maxVersion defines the maximum acceptable TLS version.  It requires Prometheus >= v2.41.0 or Thanos >= v0.31.0.   
`minVersion` |  `string` |  minVersion defines the minimum acceptable TLS version.  It requires Prometheus >= v2.35.0 or Thanos >= v0.28.0.   
`serverName` |  `string` |  serverName is used to verify the hostname for the targets.   
Show more

## 8.1.19. .spec.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 8.1.20. .spec.oauth2.tlsConfig.ca.configMap

Description
     configMap defines the ConfigMap containing data to use for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key to select.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the ConfigMap or its key must be defined   
Show more

## 8.1.21. .spec.oauth2.tlsConfig.ca.secret

Description
     secret defines the Secret containing data to use for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.22. .spec.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 8.1.23. .spec.oauth2.tlsConfig.cert.configMap

Description
     configMap defines the ConfigMap containing data to use for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key to select.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the ConfigMap or its key must be defined   
Show more

## 8.1.24. .spec.oauth2.tlsConfig.cert.secret

Description
     secret defines the Secret containing data to use for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.25. .spec.oauth2.tlsConfig.keySecret

Description
     keySecret defines the Secret containing the client key file for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.26. .spec.params

Description
     params defines the list of HTTP query parameters for the scrape. Please note that the `.spec.module` field takes precedence over the `module` parameter from this list when both are defined. The module name must be added using Module under ProbeSpec. 
Type
     `array`

## 8.1.27. .spec.params[]

Description
     ProbeParam defines specification of extra parameters for a Probe. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name defines the parameter name   
`values` |  `array (string)` |  values defines the parameter values   
Show more

## 8.1.28. .spec.prober

Description
     prober defines the specification for the prober to use for probing targets. The prober.URL parameter is required. Targets cannot be probed if left empty. 
Type
     `object`
Required
    

  * `url`



Property| Type| Description  
---|---|---  
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`path` |  `string` |  path to collect metrics from. Defaults to `/probe`.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`scheme` |  `string` |  scheme defines the HTTP scheme to use when scraping the prober.   
`url` |  `string` |  url defines the address of the prober.  Unlike what the name indicates, the value should be in the form of `address:port` without any scheme which should be specified in the `scheme` field.   
Show more

## 8.1.29. .spec.prober.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 8.1.30. .spec.prober.proxyConnectHeader{}

Description
    
Type
     `array`

## 8.1.31. .spec.prober.proxyConnectHeader{}[]

Description
     SecretKeySelector selects a key of a Secret. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.32. .spec.targets

Description
     targets defines a set of static or dynamically discovered targets to probe. 
Type
     `object`

Property| Type| Description  
---|---|---  
`ingress` |  `object` |  ingress defines the Ingress objects to probe and the relabeling configuration. If `staticConfig` is also defined, `staticConfig` takes precedence.   
`staticConfig` |  `object` |  staticConfig defines the static list of targets to probe and the relabeling configuration. If `ingress` is also defined, `staticConfig` takes precedence. More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#static_config>.   
Show more

## 8.1.33. .spec.targets.ingress

Description
     ingress defines the Ingress objects to probe and the relabeling configuration. If `staticConfig` is also defined, `staticConfig` takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`namespaceSelector` |  `object` |  namespaceSelector defines from which namespaces to select Ingress objects.   
`relabelingConfigs` |  `array` |  relabelingConfigs to apply to the label set of the target before it gets scraped. The original ingress address is available via the `__tmp_prometheus_ingress_address` label. It can be used to customize the probed URL. The original scrape job’s name is available via the `\__tmp_prometheus_job_name` label. More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>  
`relabelingConfigs[]` |  `object` |  RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples.  More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>  
`selector` |  `object` |  selector to select the Ingress objects.   
Show more

## 8.1.34. .spec.targets.ingress.namespaceSelector

Description
     namespaceSelector defines from which namespaces to select Ingress objects. 
Type
     `object`

Property| Type| Description  
---|---|---  
`any` |  `boolean` |  any defines the boolean describing whether all namespaces are selected in contrast to a list restricting them.   
`matchNames` |  `array (string)` |  matchNames defines the list of namespace names to select from.   
Show more

## 8.1.35. .spec.targets.ingress.relabelingConfigs

Description
     relabelingConfigs to apply to the label set of the target before it gets scraped. The original ingress address is available via the `__tmp_prometheus_ingress_address` label. It can be used to customize the probed URL. The original scrape job’s name is available via the `\__tmp_prometheus_job_name` label. More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>
Type
     `array`

## 8.1.36. .spec.targets.ingress.relabelingConfigs[]

Description
    

RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples. 

More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>

Type
     `object`

Property| Type| Description  
---|---|---  
`action` |  `string` |  action to perform based on the regex matching.  `Uppercase` and `Lowercase` actions require Prometheus >= v2.36.0. `DropEqual` and `KeepEqual` actions require Prometheus >= v2.41.0.  Default: "Replace"   
`modulus` |  `integer` |  modulus to take of the hash of the source label values.  Only applicable when the action is `HashMod`.   
`regex` |  `string` |  regex defines the regular expression against which the extracted value is matched.   
`replacement` |  `string` |  replacement value against which a Replace action is performed if the regular expression matches.  Regex capture groups are available.   
`separator` |  `string` |  separator defines the string between concatenated SourceLabels.   
`sourceLabels` |  `array (string)` |  sourceLabels defines the source labels select values from existing labels. Their content is concatenated using the configured Separator and matched against the configured regular expression.   
`targetLabel` |  `string` |  targetLabel defines the label to which the resulting string is written in a replacement.  It is mandatory for `Replace`, `HashMod`, `Lowercase`, `Uppercase`, `KeepEqual` and `DropEqual` actions.  Regex capture groups are available.   
Show more

## 8.1.37. .spec.targets.ingress.selector

Description
     selector to select the Ingress objects. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 8.1.38. .spec.targets.ingress.selector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 8.1.39. .spec.targets.ingress.selector.matchExpressions[]

Description
     A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key is the label key that the selector applies to.   
`operator` |  `string` |  operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`values` |  `array (string)` |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
Show more

## 8.1.40. .spec.targets.staticConfig

Description
     staticConfig defines the static list of targets to probe and the relabeling configuration. If `ingress` is also defined, `staticConfig` takes precedence. More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#static_config>. 
Type
     `object`

Property| Type| Description  
---|---|---  
`labels` |  `object (string)` |  labels defines all labels assigned to all metrics scraped from the targets.   
`relabelingConfigs` |  `array` |  relabelingConfigs defines relabelings to be apply to the label set of the targets before it gets scraped. More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>  
`relabelingConfigs[]` |  `object` |  RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples.  More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>  
`static` |  `array (string)` |  static defines the list of hosts to probe.   
Show more

## 8.1.41. .spec.targets.staticConfig.relabelingConfigs

Description
     relabelingConfigs defines relabelings to be apply to the label set of the targets before it gets scraped. More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>
Type
     `array`

## 8.1.42. .spec.targets.staticConfig.relabelingConfigs[]

Description
    

RelabelConfig allows dynamic rewriting of the label set for targets, alerts, scraped samples and remote write samples. 

More info: <https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config>

Type
     `object`

Property| Type| Description  
---|---|---  
`action` |  `string` |  action to perform based on the regex matching.  `Uppercase` and `Lowercase` actions require Prometheus >= v2.36.0. `DropEqual` and `KeepEqual` actions require Prometheus >= v2.41.0.  Default: "Replace"   
`modulus` |  `integer` |  modulus to take of the hash of the source label values.  Only applicable when the action is `HashMod`.   
`regex` |  `string` |  regex defines the regular expression against which the extracted value is matched.   
`replacement` |  `string` |  replacement value against which a Replace action is performed if the regular expression matches.  Regex capture groups are available.   
`separator` |  `string` |  separator defines the string between concatenated SourceLabels.   
`sourceLabels` |  `array (string)` |  sourceLabels defines the source labels select values from existing labels. Their content is concatenated using the configured Separator and matched against the configured regular expression.   
`targetLabel` |  `string` |  targetLabel defines the label to which the resulting string is written in a replacement.  It is mandatory for `Replace`, `HashMod`, `Lowercase`, `Uppercase`, `KeepEqual` and `DropEqual` actions.  Regex capture groups are available.   
Show more

## 8.1.43. .spec.tlsConfig

Description
     tlsConfig defines the TLS configuration used by the client. 
Type
     `object`

Property| Type| Description  
---|---|---  
`ca` |  `object` |  ca defines the Certificate authority used when verifying server certificates.   
`cert` |  `object` |  cert defines the Client certificate to present when doing client-authentication.   
`insecureSkipVerify` |  `boolean` |  insecureSkipVerify defines how to disable target certificate validation.   
`keySecret` |  `object` |  keySecret defines the Secret containing the client key file for the targets.   
`maxVersion` |  `string` |  maxVersion defines the maximum acceptable TLS version.  It requires Prometheus >= v2.41.0 or Thanos >= v0.31.0.   
`minVersion` |  `string` |  minVersion defines the minimum acceptable TLS version.  It requires Prometheus >= v2.35.0 or Thanos >= v0.28.0.   
`serverName` |  `string` |  serverName is used to verify the hostname for the targets.   
Show more

## 8.1.44. .spec.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 8.1.45. .spec.tlsConfig.ca.configMap

Description
     configMap defines the ConfigMap containing data to use for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key to select.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the ConfigMap or its key must be defined   
Show more

## 8.1.46. .spec.tlsConfig.ca.secret

Description
     secret defines the Secret containing data to use for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.47. .spec.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 8.1.48. .spec.tlsConfig.cert.configMap

Description
     configMap defines the ConfigMap containing data to use for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key to select.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the ConfigMap or its key must be defined   
Show more

## 8.1.49. .spec.tlsConfig.cert.secret

Description
     secret defines the Secret containing data to use for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.50. .spec.tlsConfig.keySecret

Description
     keySecret defines the Secret containing the client key file for the targets. 
Type
     `object`
Required
    

  * `key`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret or its key must be defined   
Show more

## 8.1.51. .status

Description
    

status defines the status subresource. It is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled. 

Most recent observed status of the Probe. Read-only. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

Type
     `object`

Property| Type| Description  
---|---|---  
`bindings` |  `array` |  bindings defines the list of workload resources (Prometheus, PrometheusAgent, ThanosRuler or Alertmanager) which select the configuration resource.   
`bindings[]` |  `object` |  WorkloadBinding is a link between a configuration resource and a workload resource.   
Show more

## 8.1.52. .status.bindings

Description
     bindings defines the list of workload resources (Prometheus, PrometheusAgent, ThanosRuler or Alertmanager) which select the configuration resource. 
Type
     `array`

## 8.1.53. .status.bindings[]

Description
     WorkloadBinding is a link between a configuration resource and a workload resource. 
Type
     `object`
Required
    

  * `group`
  * `name`
  * `namespace`
  * `resource`



Property| Type| Description  
---|---|---  
`conditions` |  `array` |  conditions defines the current state of the configuration resource when bound to the referenced Workload object.   
`conditions[]` |  `object` |  ConfigResourceCondition describes the status of configuration resources linked to Prometheus, PrometheusAgent, Alertmanager or ThanosRuler.   
`group` |  `string` |  group defines the group of the referenced resource.   
`name` |  `string` |  name defines the name of the referenced object.   
`namespace` |  `string` |  namespace defines the namespace of the referenced object.   
`resource` |  `string` |  resource defines the type of resource being referenced (e.g. Prometheus, PrometheusAgent, ThanosRuler or Alertmanager).   
Show more

## 8.1.54. .status.bindings[].conditions

Description
     conditions defines the current state of the configuration resource when bound to the referenced Workload object. 
Type
     `array`

## 8.1.55. .status.bindings[].conditions[]

Description
     ConfigResourceCondition describes the status of configuration resources linked to Prometheus, PrometheusAgent, Alertmanager or ThanosRuler. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime defines the time of the last update to the current status property.   
`message` |  `string` |  message defines the human-readable message indicating details for the condition’s last transition.   
`observedGeneration` |  `integer` |  observedGeneration defines the .metadata.generation that the condition was set based upon. For instance, if `.metadata.generation` is currently 12, but the `.status.conditions[].observedGeneration` is 9, the condition is out of date with respect to the current state of the object.   
`reason` |  `string` |  reason for the condition’s last transition.   
`status` |  `string` |  status of the condition.   
`type` |  `string` |  type of the condition being reported. Currently, only "Accepted" is supported.   
Show more
