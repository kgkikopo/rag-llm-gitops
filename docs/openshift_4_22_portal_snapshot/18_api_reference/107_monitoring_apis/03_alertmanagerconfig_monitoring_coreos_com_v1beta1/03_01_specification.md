# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec defines the specification of AlertmanagerConfigSpec   
`status` |  `object` |  status defines the status subresource. It is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled.  Most recent observed status of the ServiceMonitor. Read-only. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>  
Show more

## 3.1.1. .spec

Description
     spec defines the specification of AlertmanagerConfigSpec 
Type
     `object`

Property| Type| Description  
---|---|---  
`inhibitRules` |  `array` |  inhibitRules defines the list of inhibition rules. The rules will only apply to alerts matching the resource’s namespace.   
`inhibitRules[]` |  `object` |  InhibitRule defines an inhibition rule that allows to mute alerts when other alerts are already firing. See <https://prometheus.io/docs/alerting/latest/configuration/#inhibit_rule>  
`receivers` |  `array` |  receivers defines the list of receivers.   
`receivers[]` |  `object` |  Receiver defines one or more notification integrations.   
`route` |  `object` |  route defines the Alertmanager route definition for alerts matching the resource’s namespace. If present, it will be added to the generated Alertmanager configuration as a first-level route.   
`timeIntervals` |  `array` |  timeIntervals defines the list of timeIntervals specifying when the routes should be muted.   
`timeIntervals[]` |  `object` |  TimeInterval specifies the periods in time when notifications will be muted or active.   
Show more

## 3.1.2. .spec.inhibitRules

Description
     inhibitRules defines the list of inhibition rules. The rules will only apply to alerts matching the resource’s namespace. 
Type
     `array`

## 3.1.3. .spec.inhibitRules[]

Description
     InhibitRule defines an inhibition rule that allows to mute alerts when other alerts are already firing. See <https://prometheus.io/docs/alerting/latest/configuration/#inhibit_rule>
Type
     `object`

Property| Type| Description  
---|---|---  
`equal` |  `array (string)` |  equal defines labels that must have an equal value in the source and target alert for the inhibition to take effect. This ensures related alerts are properly grouped.   
`sourceMatch` |  `array` |  sourceMatch defines matchers for which one or more alerts have to exist for the inhibition to take effect. The operator enforces that the alert matches the resource’s namespace. These are the "trigger" alerts that cause other alerts to be inhibited.   
`sourceMatch[]` |  `object` |  Matcher defines how to match on alert’s labels.   
`targetMatch` |  `array` |  targetMatch defines matchers that have to be fulfilled in the alerts to be muted. The operator enforces that the alert matches the resource’s namespace. When these conditions are met, matching alerts will be inhibited (silenced).   
`targetMatch[]` |  `object` |  Matcher defines how to match on alert’s labels.   
Show more

## 3.1.4. .spec.inhibitRules[].sourceMatch

Description
     sourceMatch defines matchers for which one or more alerts have to exist for the inhibition to take effect. The operator enforces that the alert matches the resource’s namespace. These are the "trigger" alerts that cause other alerts to be inhibited. 
Type
     `array`

## 3.1.5. .spec.inhibitRules[].sourceMatch[]

Description
     Matcher defines how to match on alert’s labels. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`matchType` |  `string` |  matchType defines the match operation available with AlertManager >= v0.22.0. Takes precedence over Regex (deprecated) if non-empty. Valid values: "=" (equality), "!=" (inequality), "=~" (regex match), "!~" (regex non-match).   
`name` |  `string` |  name defines the label to match. This specifies which alert label should be evaluated.   
`value` |  `string` |  value defines the label value to match. This is the expected value for the specified label.   
Show more

## 3.1.6. .spec.inhibitRules[].targetMatch

Description
     targetMatch defines matchers that have to be fulfilled in the alerts to be muted. The operator enforces that the alert matches the resource’s namespace. When these conditions are met, matching alerts will be inhibited (silenced). 
Type
     `array`

## 3.1.7. .spec.inhibitRules[].targetMatch[]

Description
     Matcher defines how to match on alert’s labels. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`matchType` |  `string` |  matchType defines the match operation available with AlertManager >= v0.22.0. Takes precedence over Regex (deprecated) if non-empty. Valid values: "=" (equality), "!=" (inequality), "=~" (regex match), "!~" (regex non-match).   
`name` |  `string` |  name defines the label to match. This specifies which alert label should be evaluated.   
`value` |  `string` |  value defines the label value to match. This is the expected value for the specified label.   
Show more

## 3.1.8. .spec.receivers

Description
     receivers defines the list of receivers. 
Type
     `array`

## 3.1.9. .spec.receivers[]

Description
     Receiver defines one or more notification integrations. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`discordConfigs` |  `array` |  discordConfigs defines the list of Discord configurations.   
`discordConfigs[]` |  `object` |  DiscordConfig configures notifications via Discord. See <https://prometheus.io/docs/alerting/latest/configuration/#discord_config>  
`emailConfigs` |  `array` |  emailConfigs defines the list of Email configurations.   
`emailConfigs[]` |  `object` |  EmailConfig configures notifications via Email.   
`msteamsConfigs` |  `array` |  msteamsConfigs defines the list of MSTeams configurations. It requires Alertmanager >= 0.26.0.   
`msteamsConfigs[]` |  `object` |  MSTeamsConfig configures notifications via Microsoft Teams. It requires Alertmanager >= 0.26.0.   
`msteamsv2Configs` |  `array` |  msteamsv2Configs defines the list of MSTeamsV2 configurations. It requires Alertmanager >= 0.28.0.   
`msteamsv2Configs[]` |  `object` |  MSTeamsV2Config configures notifications via Microsoft Teams using the new message format with adaptive cards as required by flows. See <https://prometheus.io/docs/alerting/latest/configuration/#msteamsv2_config> It requires Alertmanager >= 0.28.0.   
`name` |  `string` |  name defines the name of the receiver. Must be unique across all items from the list.   
`opsgenieConfigs` |  `array` |  opsgenieConfigs defines the list of OpsGenie configurations.   
`opsgenieConfigs[]` |  `object` |  OpsGenieConfig configures notifications via OpsGenie. See <https://prometheus.io/docs/alerting/latest/configuration/#opsgenie_config>  
`pagerdutyConfigs` |  `array` |  pagerdutyConfigs defines the List of PagerDuty configurations.   
`pagerdutyConfigs[]` |  `object` |  PagerDutyConfig configures notifications via PagerDuty. See <https://prometheus.io/docs/alerting/latest/configuration/#pagerduty_config>  
`pushoverConfigs` |  `array` |  pushoverConfigs defines the list of Pushover configurations.   
`pushoverConfigs[]` |  `object` |  PushoverConfig configures notifications via Pushover. See <https://prometheus.io/docs/alerting/latest/configuration/#pushover_config>  
`rocketchatConfigs` |  `array` |  rocketchatConfigs defines the list of RocketChat configurations. It requires Alertmanager >= 0.28.0.   
`rocketchatConfigs[]` |  `object` |  RocketChatConfig configures notifications via RocketChat. It requires Alertmanager >= 0.28.0.   
`slackConfigs` |  `array` |  slackConfigs defines the list of Slack configurations.   
`slackConfigs[]` |  `object` |  SlackConfig configures notifications via Slack. See <https://prometheus.io/docs/alerting/latest/configuration/#slack_config>  
`snsConfigs` |  `array` |  snsConfigs defines the list of SNS configurations   
`snsConfigs[]` |  `object` |  SNSConfig configures notifications via AWS SNS. See <https://prometheus.io/docs/alerting/latest/configuration/#sns_configs>  
`telegramConfigs` |  `array` |  telegramConfigs defines the list of Telegram configurations.   
`telegramConfigs[]` |  `object` |  TelegramConfig configures notifications via Telegram. See <https://prometheus.io/docs/alerting/latest/configuration/#telegram_config>  
`victoropsConfigs` |  `array` |  victoropsConfigs defines the list of VictorOps configurations.   
`victoropsConfigs[]` |  `object` |  VictorOpsConfig configures notifications via VictorOps. See <https://prometheus.io/docs/alerting/latest/configuration/#victorops_config>  
`webexConfigs` |  `array` |  webexConfigs defines the list of Webex configurations.   
`webexConfigs[]` |  `object` |  WebexConfig configures notification via Cisco Webex See <https://prometheus.io/docs/alerting/latest/configuration/#webex_config>  
`webhookConfigs` |  `array` |  webhookConfigs defines the List of webhook configurations.   
`webhookConfigs[]` |  `object` |  WebhookConfig configures notifications via a generic receiver supporting the webhook payload. See <https://prometheus.io/docs/alerting/latest/configuration/#webhook_config>  
`wechatConfigs` |  `array` |  wechatConfigs defines the list of WeChat configurations.   
`wechatConfigs[]` |  `object` |  WeChatConfig configures notifications via WeChat. See <https://prometheus.io/docs/alerting/latest/configuration/#wechat_config>  
Show more

## 3.1.10. .spec.receivers[].discordConfigs

Description
     discordConfigs defines the list of Discord configurations. 
Type
     `array`

## 3.1.11. .spec.receivers[].discordConfigs[]

Description
     DiscordConfig configures notifications via Discord. See <https://prometheus.io/docs/alerting/latest/configuration/#discord_config>
Type
     `object`
Required
    

  * `apiURL`



Property| Type| Description  
---|---|---  
`apiURL` |  `object` |  apiURL defines the secret’s key that contains the Discord webhook URL. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`avatarURL` |  `string` |  avatarURL defines the avatar url of the message sender.   
`content` |  `string` |  content defines the template of the content’s body.   
`httpConfig` |  `object` |  httpConfig defines HTTP client configuration.   
`message` |  `string` |  message defines the template of the message’s body.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`title` |  `string` |  title defines the template of the message’s title.   
`username` |  `string` |  username defines the username of the message sender.   
Show more

## 3.1.12. .spec.receivers[].discordConfigs[].apiURL

Description
     apiURL defines the secret’s key that contains the Discord webhook URL. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
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

## 3.1.13. .spec.receivers[].discordConfigs[].httpConfig

Description
     httpConfig defines HTTP client configuration. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.14. .spec.receivers[].discordConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.15. .spec.receivers[].discordConfigs[].httpConfig.authorization.credentials

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

## 3.1.16. .spec.receivers[].discordConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.17. .spec.receivers[].discordConfigs[].httpConfig.basicAuth.password

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

## 3.1.18. .spec.receivers[].discordConfigs[].httpConfig.basicAuth.username

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

## 3.1.19. .spec.receivers[].discordConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.20. .spec.receivers[].discordConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.21. .spec.receivers[].discordConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.22. .spec.receivers[].discordConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.23. .spec.receivers[].discordConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.24. .spec.receivers[].discordConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.25. .spec.receivers[].discordConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.26. .spec.receivers[].discordConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.27. .spec.receivers[].discordConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.28. .spec.receivers[].discordConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.29. .spec.receivers[].discordConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.30. .spec.receivers[].discordConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.31. .spec.receivers[].discordConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.32. .spec.receivers[].discordConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.33. .spec.receivers[].discordConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.34. .spec.receivers[].discordConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.35. .spec.receivers[].discordConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.36. .spec.receivers[].discordConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.37. .spec.receivers[].discordConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.38. .spec.receivers[].discordConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.39. .spec.receivers[].discordConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.40. .spec.receivers[].discordConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.41. .spec.receivers[].discordConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.42. .spec.receivers[].discordConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.43. .spec.receivers[].discordConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.44. .spec.receivers[].discordConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.45. .spec.receivers[].discordConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.46. .spec.receivers[].discordConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.47. .spec.receivers[].emailConfigs

Description
     emailConfigs defines the list of Email configurations. 
Type
     `array`

## 3.1.48. .spec.receivers[].emailConfigs[]

Description
     EmailConfig configures notifications via Email. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authIdentity` |  `string` |  authIdentity defines the identity to use for SMTP authentication. This is typically used with PLAIN authentication mechanism.   
`authPassword` |  `object` |  authPassword defines the secret’s key that contains the password to use for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`authSecret` |  `object` |  authSecret defines the secret’s key that contains the CRAM-MD5 secret. This is used for CRAM-MD5 authentication mechanism. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`authUsername` |  `string` |  authUsername defines the username to use for SMTP authentication. This is used for SMTP AUTH when the server requires authentication.   
`forceImplicitTLS` |  `boolean` |  forceImplicitTLS defines whether to force use of implicit TLS (direct TLS connection) for better security. true: force use of implicit TLS (direct TLS connection on any port) false: force disable implicit TLS (use explicit TLS/STARTTLS if required) nil (default): auto-detect based on port (465=implicit, other=explicit) for backward compatibility It requires Alertmanager >= v0.31.0.   
`from` |  `string` |  from defines the sender address for email notifications. This appears as the "From" field in the email header.   
`headers` |  `array` |  headers defines additional email header key/value pairs. These override any headers previously set by the notification implementation.   
`headers[]` |  `object` |  KeyValue defines a (key, value) tuple.   
`hello` |  `string` |  hello defines the hostname to identify to the SMTP server. This is used in the SMTP HELO/EHLO command during the connection handshake.   
`html` |  `string` |  html defines the HTML body of the email notification. This allows for rich formatting in the email content.   
`requireTLS` |  `boolean` |  requireTLS defines the SMTP TLS requirement. Note that Go does not support unencrypted connections to remote SMTP endpoints.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`smarthost` |  `string` |  smarthost defines the SMTP host and port through which emails are sent. Format should be "hostname:port", e.g. "smtp.example.com:587".   
`text` |  `string` |  text defines the plain text body of the email notification. This provides a fallback for email clients that don’t support HTML.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for SMTP connections. This includes settings for certificates, CA validation, and TLS protocol options.   
`to` |  `string` |  to defines the email address to send notifications to. This is the recipient address for alert notifications.   
Show more

## 3.1.49. .spec.receivers[].emailConfigs[].authPassword

Description
     authPassword defines the secret’s key that contains the password to use for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.50. .spec.receivers[].emailConfigs[].authSecret

Description
     authSecret defines the secret’s key that contains the CRAM-MD5 secret. This is used for CRAM-MD5 authentication mechanism. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.51. .spec.receivers[].emailConfigs[].headers

Description
     headers defines additional email header key/value pairs. These override any headers previously set by the notification implementation. 
Type
     `array`

## 3.1.52. .spec.receivers[].emailConfigs[].headers[]

Description
     KeyValue defines a (key, value) tuple. 
Type
     `object`
Required
    

  * `key`
  * `value`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the tuple. This is the identifier or name part of the key-value pair.   
`value` |  `string` |  value defines the value of the tuple. This is the data or content associated with the key.   
Show more

## 3.1.53. .spec.receivers[].emailConfigs[].tlsConfig

Description
     tlsConfig defines the TLS configuration for SMTP connections. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.54. .spec.receivers[].emailConfigs[].tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.55. .spec.receivers[].emailConfigs[].tlsConfig.ca.configMap

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

## 3.1.56. .spec.receivers[].emailConfigs[].tlsConfig.ca.secret

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

## 3.1.57. .spec.receivers[].emailConfigs[].tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.58. .spec.receivers[].emailConfigs[].tlsConfig.cert.configMap

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

## 3.1.59. .spec.receivers[].emailConfigs[].tlsConfig.cert.secret

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

## 3.1.60. .spec.receivers[].emailConfigs[].tlsConfig.keySecret

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

## 3.1.61. .spec.receivers[].msteamsConfigs

Description
     msteamsConfigs defines the list of MSTeams configurations. It requires Alertmanager >= 0.26.0. 
Type
     `array`

## 3.1.62. .spec.receivers[].msteamsConfigs[]

Description
     MSTeamsConfig configures notifications via Microsoft Teams. It requires Alertmanager >= 0.26.0. 
Type
     `object`
Required
    

  * `webhookUrl`



Property| Type| Description  
---|---|---  
`httpConfig` |  `object` |  httpConfig defines the HTTP client configuration for Teams webhook requests.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`summary` |  `string` |  summary defines the message summary template for Teams notifications. This provides a brief overview that appears in Teams notification previews. It requires Alertmanager >= 0.27.0.   
`text` |  `string` |  text defines the message body template for Teams notifications. This contains the detailed content of the Teams message.   
`title` |  `string` |  title defines the message title template for Teams notifications. This appears as the main heading of the Teams message card.   
`webhookUrl` |  `object` |  webhookUrl defines the MSTeams webhook URL for sending notifications. This is the incoming webhook URL configured in your Teams channel.   
Show more

## 3.1.63. .spec.receivers[].msteamsConfigs[].httpConfig

Description
     httpConfig defines the HTTP client configuration for Teams webhook requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.64. .spec.receivers[].msteamsConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.65. .spec.receivers[].msteamsConfigs[].httpConfig.authorization.credentials

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

## 3.1.66. .spec.receivers[].msteamsConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.67. .spec.receivers[].msteamsConfigs[].httpConfig.basicAuth.password

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

## 3.1.68. .spec.receivers[].msteamsConfigs[].httpConfig.basicAuth.username

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

## 3.1.69. .spec.receivers[].msteamsConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.70. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.71. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.72. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.73. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.74. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.75. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.76. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.77. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.78. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.79. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.80. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.81. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.82. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.83. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.84. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.85. .spec.receivers[].msteamsConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.86. .spec.receivers[].msteamsConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.87. .spec.receivers[].msteamsConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.88. .spec.receivers[].msteamsConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.89. .spec.receivers[].msteamsConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.90. .spec.receivers[].msteamsConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.91. .spec.receivers[].msteamsConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.92. .spec.receivers[].msteamsConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.93. .spec.receivers[].msteamsConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.94. .spec.receivers[].msteamsConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.95. .spec.receivers[].msteamsConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.96. .spec.receivers[].msteamsConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.97. .spec.receivers[].msteamsConfigs[].webhookUrl

Description
     webhookUrl defines the MSTeams webhook URL for sending notifications. This is the incoming webhook URL configured in your Teams channel. 
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

## 3.1.98. .spec.receivers[].msteamsv2Configs

Description
     msteamsv2Configs defines the list of MSTeamsV2 configurations. It requires Alertmanager >= 0.28.0. 
Type
     `array`

## 3.1.99. .spec.receivers[].msteamsv2Configs[]

Description
     MSTeamsV2Config configures notifications via Microsoft Teams using the new message format with adaptive cards as required by flows. See <https://prometheus.io/docs/alerting/latest/configuration/#msteamsv2_config> It requires Alertmanager >= 0.28.0. 
Type
     `object`

Property| Type| Description  
---|---|---  
`httpConfig` |  `object` |  httpConfig defines the HTTP client configuration for Teams webhook requests.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`text` |  `string` |  text defines the message body template for adaptive card notifications. This contains the detailed content displayed in the Teams adaptive card format.   
`title` |  `string` |  title defines the message title template for adaptive card notifications. This appears as the main heading in the Teams adaptive card.   
`webhookURL` |  `object` |  webhookURL defines the MSTeams incoming webhook URL for adaptive card notifications. This webhook must support the newer adaptive cards format required by Teams flows.   
Show more

## 3.1.100. .spec.receivers[].msteamsv2Configs[].httpConfig

Description
     httpConfig defines the HTTP client configuration for Teams webhook requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.101. .spec.receivers[].msteamsv2Configs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.102. .spec.receivers[].msteamsv2Configs[].httpConfig.authorization.credentials

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

## 3.1.103. .spec.receivers[].msteamsv2Configs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.104. .spec.receivers[].msteamsv2Configs[].httpConfig.basicAuth.password

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

## 3.1.105. .spec.receivers[].msteamsv2Configs[].httpConfig.basicAuth.username

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

## 3.1.106. .spec.receivers[].msteamsv2Configs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.107. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.108. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.109. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.110. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.clientId.secret

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

## 3.1.111. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.clientSecret

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

## 3.1.112. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.113. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.114. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.115. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.tlsConfig

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

## 3.1.116. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.117. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.118. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.119. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.120. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.121. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.122. .spec.receivers[].msteamsv2Configs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.123. .spec.receivers[].msteamsv2Configs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.124. .spec.receivers[].msteamsv2Configs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.125. .spec.receivers[].msteamsv2Configs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.126. .spec.receivers[].msteamsv2Configs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.127. .spec.receivers[].msteamsv2Configs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.128. .spec.receivers[].msteamsv2Configs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.129. .spec.receivers[].msteamsv2Configs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.130. .spec.receivers[].msteamsv2Configs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.131. .spec.receivers[].msteamsv2Configs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.132. .spec.receivers[].msteamsv2Configs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.133. .spec.receivers[].msteamsv2Configs[].httpConfig.tlsConfig.keySecret

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

## 3.1.134. .spec.receivers[].msteamsv2Configs[].webhookURL

Description
     webhookURL defines the MSTeams incoming webhook URL for adaptive card notifications. This webhook must support the newer adaptive cards format required by Teams flows. 
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

## 3.1.135. .spec.receivers[].opsgenieConfigs

Description
     opsgenieConfigs defines the list of OpsGenie configurations. 
Type
     `array`

## 3.1.136. .spec.receivers[].opsgenieConfigs[]

Description
     OpsGenieConfig configures notifications via OpsGenie. See <https://prometheus.io/docs/alerting/latest/configuration/#opsgenie_config>
Type
     `object`

Property| Type| Description  
---|---|---  
`actions` |  `string` |  actions defines a comma separated list of actions that will be available for the alert. These appear as action buttons in the OpsGenie interface.   
`apiKey` |  `object` |  apiKey defines the secret’s key that contains the OpsGenie API key. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`apiURL` |  `string` |  apiURL defines the URL to send OpsGenie API requests to. When not specified, defaults to the standard OpsGenie API endpoint.   
`description` |  `string` |  description defines the detailed description of the incident. This provides additional context beyond the message field.   
`details` |  `array` |  details defines a set of arbitrary key/value pairs that provide further detail about the incident. These appear as additional fields in the OpsGenie alert.   
`details[]` |  `object` |  KeyValue defines a (key, value) tuple.   
`entity` |  `string` |  entity defines an optional field that can be used to specify which domain alert is related to. This helps group related alerts together in OpsGenie.   
`httpConfig` |  `object` |  httpConfig defines the HTTP client configuration for OpsGenie API requests.   
`message` |  `string` |  message defines the alert text limited to 130 characters. This appears as the main alert title in OpsGenie.   
`note` |  `string` |  note defines an additional alert note. This provides supplementary information about the alert.   
`priority` |  `string` |  priority defines the priority level of alert. Possible values are P1, P2, P3, P4, and P5, where P1 is highest priority.   
`responders` |  `array` |  responders defines the list of responders responsible for notifications. These determine who gets notified when the alert is created.   
`responders[]` |  `object` |  OpsGenieConfigResponder defines a responder to an incident. One of `id`, `name` or `username` has to be defined.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`source` |  `string` |  source defines the backlink to the sender of the notification. This helps identify where the alert originated from.   
`tags` |  `string` |  tags defines a comma separated list of tags attached to the notifications. These help categorize and filter alerts within OpsGenie.   
Show more

## 3.1.137. .spec.receivers[].opsgenieConfigs[].apiKey

Description
     apiKey defines the secret’s key that contains the OpsGenie API key. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.138. .spec.receivers[].opsgenieConfigs[].details

Description
     details defines a set of arbitrary key/value pairs that provide further detail about the incident. These appear as additional fields in the OpsGenie alert. 
Type
     `array`

## 3.1.139. .spec.receivers[].opsgenieConfigs[].details[]

Description
     KeyValue defines a (key, value) tuple. 
Type
     `object`
Required
    

  * `key`
  * `value`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the tuple. This is the identifier or name part of the key-value pair.   
`value` |  `string` |  value defines the value of the tuple. This is the data or content associated with the key.   
Show more

## 3.1.140. .spec.receivers[].opsgenieConfigs[].httpConfig

Description
     httpConfig defines the HTTP client configuration for OpsGenie API requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.141. .spec.receivers[].opsgenieConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.142. .spec.receivers[].opsgenieConfigs[].httpConfig.authorization.credentials

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

## 3.1.143. .spec.receivers[].opsgenieConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.144. .spec.receivers[].opsgenieConfigs[].httpConfig.basicAuth.password

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

## 3.1.145. .spec.receivers[].opsgenieConfigs[].httpConfig.basicAuth.username

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

## 3.1.146. .spec.receivers[].opsgenieConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.147. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.148. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.149. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.150. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.151. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.152. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.153. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.154. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.155. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.156. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.157. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.158. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.159. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.160. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.161. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.162. .spec.receivers[].opsgenieConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.163. .spec.receivers[].opsgenieConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.164. .spec.receivers[].opsgenieConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.165. .spec.receivers[].opsgenieConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.166. .spec.receivers[].opsgenieConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.167. .spec.receivers[].opsgenieConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.168. .spec.receivers[].opsgenieConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.169. .spec.receivers[].opsgenieConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.170. .spec.receivers[].opsgenieConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.171. .spec.receivers[].opsgenieConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.172. .spec.receivers[].opsgenieConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.173. .spec.receivers[].opsgenieConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.174. .spec.receivers[].opsgenieConfigs[].responders

Description
     responders defines the list of responders responsible for notifications. These determine who gets notified when the alert is created. 
Type
     `array`

## 3.1.175. .spec.receivers[].opsgenieConfigs[].responders[]

Description
     OpsGenieConfigResponder defines a responder to an incident. One of `id`, `name` or `username` has to be defined. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`id` |  `string` |  id defines the unique identifier of the responder. This corresponds to the responder’s ID within OpsGenie.   
`name` |  `string` |  name defines the display name of the responder. This is used when the responder is identified by name rather than ID.   
`type` |  `string` |  type defines the type of responder. Valid values include "user", "team", "schedule", and "escalation". This determines how OpsGenie interprets the other identifier fields.   
`username` |  `string` |  username defines the username of the responder. This is typically used for user-type responders when identifying by username.   
Show more

## 3.1.176. .spec.receivers[].pagerdutyConfigs

Description
     pagerdutyConfigs defines the List of PagerDuty configurations. 
Type
     `array`

## 3.1.177. .spec.receivers[].pagerdutyConfigs[]

Description
     PagerDutyConfig configures notifications via PagerDuty. See <https://prometheus.io/docs/alerting/latest/configuration/#pagerduty_config>
Type
     `object`

Property| Type| Description  
---|---|---  
`class` |  `string` |  class defines the class/type of the event.   
`client` |  `string` |  client defines the client identification.   
`clientURL` |  `string` |  clientURL defines the backlink to the sender of notification.   
`component` |  `string` |  component defines the part or component of the affected system that is broken.   
`description` |  `string` |  description of the incident.   
`details` |  `array` |  details defines the arbitrary key/value pairs that provide further detail about the incident.   
`details[]` |  `object` |  KeyValue defines a (key, value) tuple.   
`group` |  `string` |  group defines a cluster or grouping of sources.   
`httpConfig` |  `object` |  httpConfig defines the HTTP client configuration.   
`pagerDutyImageConfigs` |  `array` |  pagerDutyImageConfigs defines a list of image details to attach that provide further detail about an incident.   
`pagerDutyImageConfigs[]` |  `object` |  PagerDutyImageConfig attaches images to an incident   
`pagerDutyLinkConfigs` |  `array` |  pagerDutyLinkConfigs defines a list of link details to attach that provide further detail about an incident.   
`pagerDutyLinkConfigs[]` |  `object` |  PagerDutyLinkConfig attaches text links to an incident   
`routingKey` |  `object` |  routingKey defines the secret’s key that contains the PagerDuty integration key (when using Events API v2). Either this field or `serviceKey` needs to be defined. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`serviceKey` |  `object` |  serviceKey defines the secret’s key that contains the PagerDuty service key (when using integration type "Prometheus"). Either this field or `routingKey` needs to be defined. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`severity` |  `string` |  severity of the incident.   
`source` |  `string` |  source defines the unique location of the affected system.   
`timeout` |  `string` |  timeout is the maximum time allowed to invoke the pagerduty It requires Alertmanager >= v0.30.0.   
`url` |  `string` |  url defines the URL to send requests to.   
Show more

## 3.1.178. .spec.receivers[].pagerdutyConfigs[].details

Description
     details defines the arbitrary key/value pairs that provide further detail about the incident. 
Type
     `array`

## 3.1.179. .spec.receivers[].pagerdutyConfigs[].details[]

Description
     KeyValue defines a (key, value) tuple. 
Type
     `object`
Required
    

  * `key`
  * `value`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the tuple. This is the identifier or name part of the key-value pair.   
`value` |  `string` |  value defines the value of the tuple. This is the data or content associated with the key.   
Show more

## 3.1.180. .spec.receivers[].pagerdutyConfigs[].httpConfig

Description
     httpConfig defines the HTTP client configuration. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.181. .spec.receivers[].pagerdutyConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.182. .spec.receivers[].pagerdutyConfigs[].httpConfig.authorization.credentials

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

## 3.1.183. .spec.receivers[].pagerdutyConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.184. .spec.receivers[].pagerdutyConfigs[].httpConfig.basicAuth.password

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

## 3.1.185. .spec.receivers[].pagerdutyConfigs[].httpConfig.basicAuth.username

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

## 3.1.186. .spec.receivers[].pagerdutyConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.187. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.188. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.189. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.190. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.191. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.192. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.193. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.194. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.195. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.196. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.197. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.198. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.199. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.200. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.201. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.202. .spec.receivers[].pagerdutyConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.203. .spec.receivers[].pagerdutyConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.204. .spec.receivers[].pagerdutyConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.205. .spec.receivers[].pagerdutyConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.206. .spec.receivers[].pagerdutyConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.207. .spec.receivers[].pagerdutyConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.208. .spec.receivers[].pagerdutyConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.209. .spec.receivers[].pagerdutyConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.210. .spec.receivers[].pagerdutyConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.211. .spec.receivers[].pagerdutyConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.212. .spec.receivers[].pagerdutyConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.213. .spec.receivers[].pagerdutyConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.214. .spec.receivers[].pagerdutyConfigs[].pagerDutyImageConfigs

Description
     pagerDutyImageConfigs defines a list of image details to attach that provide further detail about an incident. 
Type
     `array`

## 3.1.215. .spec.receivers[].pagerdutyConfigs[].pagerDutyImageConfigs[]

Description
     PagerDutyImageConfig attaches images to an incident 
Type
     `object`

Property| Type| Description  
---|---|---  
`alt` |  `string` |  alt is the optional alternative text for the image.   
`href` |  `string` |  href defines the optional URL; makes the image a clickable link.   
`src` |  `string` |  src of the image being attached to the incident   
Show more

## 3.1.216. .spec.receivers[].pagerdutyConfigs[].pagerDutyLinkConfigs

Description
     pagerDutyLinkConfigs defines a list of link details to attach that provide further detail about an incident. 
Type
     `array`

## 3.1.217. .spec.receivers[].pagerdutyConfigs[].pagerDutyLinkConfigs[]

Description
     PagerDutyLinkConfig attaches text links to an incident 
Type
     `object`

Property| Type| Description  
---|---|---  
`alt` |  `string` |  alt defines the text that describes the purpose of the link, and can be used as the link’s text.   
`href` |  `string` |  href defines the URL of the link to be attached   
Show more

## 3.1.218. .spec.receivers[].pagerdutyConfigs[].routingKey

Description
     routingKey defines the secret’s key that contains the PagerDuty integration key (when using Events API v2). Either this field or `serviceKey` needs to be defined. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.219. .spec.receivers[].pagerdutyConfigs[].serviceKey

Description
     serviceKey defines the secret’s key that contains the PagerDuty service key (when using integration type "Prometheus"). Either this field or `routingKey` needs to be defined. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.220. .spec.receivers[].pushoverConfigs

Description
     pushoverConfigs defines the list of Pushover configurations. 
Type
     `array`

## 3.1.221. .spec.receivers[].pushoverConfigs[]

Description
     PushoverConfig configures notifications via Pushover. See <https://prometheus.io/docs/alerting/latest/configuration/#pushover_config>
Type
     `object`

Property| Type| Description  
---|---|---  
`device` |  `string` |  device defines the name of a specific device to send the notification to. If not specified, the notification is sent to all user’s devices.   
`expire` |  `string` |  expire defines how long your notification will continue to be retried for, unless the user acknowledges the notification. Only applies to priority 2 notifications.   
`html` |  `boolean` |  html defines whether notification message is HTML or plain text. When true, the message can include HTML formatting tags. html and monospace formatting are mutually exclusive.   
`httpConfig` |  `object` |  httpConfig defines the HTTP client configuration for Pushover API requests.   
`message` |  `string` |  message defines the notification message content. This is the main body text of the Pushover notification.   
`monospace` |  `boolean` |  monospace optional HTML/monospace formatting for the message, see <https://pushover.net/api#html> html and monospace formatting are mutually exclusive.   
`priority` |  `string` |  priority defines the notification priority level. See <https://pushover.net/api#priority> for valid values and behavior.   
`retry` |  `string` |  retry defines how often the Pushover servers will send the same notification to the user. Must be at least 30 seconds. Only applies to priority 2 notifications.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`sound` |  `string` |  sound defines the name of one of the sounds supported by device clients. This overrides the user’s default sound choice for this notification.   
`title` |  `string` |  title defines the notification title displayed in the Pushover message. This appears as the bold header text in the notification.   
`token` |  `object` |  token defines the secret’s key that contains the registered application’s API token. See <https://pushover.net/apps> for application registration. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. Either `token` or `tokenFile` is required.   
`tokenFile` |  `string` |  tokenFile defines the token file that contains the registered application’s API token. See <https://pushover.net/apps> for application registration. Either `token` or `tokenFile` is required. It requires Alertmanager >= v0.26.0.   
`ttl` |  `string` |  ttl defines the time to live for the alert notification. This determines how long the notification remains active before expiring.   
`url` |  `string` |  url defines a supplementary URL shown alongside the message. This creates a clickable link within the Pushover notification.   
`urlTitle` |  `string` |  urlTitle defines a title for the supplementary URL. If not specified, the raw URL is shown instead.   
`userKey` |  `object` |  userKey defines the secret’s key that contains the recipient user’s user key. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. Either `userKey` or `userKeyFile` is required.   
`userKeyFile` |  `string` |  userKeyFile defines the user key file that contains the recipient user’s user key. Either `userKey` or `userKeyFile` is required. It requires Alertmanager >= v0.26.0.   
Show more

## 3.1.222. .spec.receivers[].pushoverConfigs[].httpConfig

Description
     httpConfig defines the HTTP client configuration for Pushover API requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.223. .spec.receivers[].pushoverConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.224. .spec.receivers[].pushoverConfigs[].httpConfig.authorization.credentials

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

## 3.1.225. .spec.receivers[].pushoverConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.226. .spec.receivers[].pushoverConfigs[].httpConfig.basicAuth.password

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

## 3.1.227. .spec.receivers[].pushoverConfigs[].httpConfig.basicAuth.username

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

## 3.1.228. .spec.receivers[].pushoverConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.229. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.230. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.231. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.232. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.233. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.234. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.235. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.236. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.237. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.238. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.239. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.240. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.241. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.242. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.243. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.244. .spec.receivers[].pushoverConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.245. .spec.receivers[].pushoverConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.246. .spec.receivers[].pushoverConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.247. .spec.receivers[].pushoverConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.248. .spec.receivers[].pushoverConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.249. .spec.receivers[].pushoverConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.250. .spec.receivers[].pushoverConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.251. .spec.receivers[].pushoverConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.252. .spec.receivers[].pushoverConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.253. .spec.receivers[].pushoverConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.254. .spec.receivers[].pushoverConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.255. .spec.receivers[].pushoverConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.256. .spec.receivers[].pushoverConfigs[].token

Description
     token defines the secret’s key that contains the registered application’s API token. See <https://pushover.net/apps> for application registration. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. Either `token` or `tokenFile` is required. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.257. .spec.receivers[].pushoverConfigs[].userKey

Description
     userKey defines the secret’s key that contains the recipient user’s user key. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. Either `userKey` or `userKeyFile` is required. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.258. .spec.receivers[].rocketchatConfigs

Description
     rocketchatConfigs defines the list of RocketChat configurations. It requires Alertmanager >= 0.28.0. 
Type
     `array`

## 3.1.259. .spec.receivers[].rocketchatConfigs[]

Description
     RocketChatConfig configures notifications via RocketChat. It requires Alertmanager >= 0.28.0. 
Type
     `object`
Required
    

  * `token`
  * `tokenID`



Property| Type| Description  
---|---|---  
`actions` |  `array` |  actions defines interactive actions to include in the message. These appear as buttons that users can click to trigger responses.   
`actions[]` |  `object` |  RocketChatActionConfig defines actions for RocketChat messages.   
`apiURL` |  `string` |  apiURL defines the API URL for RocketChat. Defaults to <https://open.rocket.chat/> if not specified.   
`channel` |  `string` |  channel defines the channel to send alerts to. This can be a channel name (e.g., "#alerts") or a direct message recipient.   
`color` |  `string` |  color defines the message color displayed in RocketChat. This appears as a colored bar alongside the message.   
`emoji` |  `string` |  emoji defines the emoji to be displayed as an avatar. If provided, this emoji will be used instead of the default avatar or iconURL.   
`fields` |  `array` |  fields defines additional fields for the message attachment. These appear as structured key-value pairs within the message.   
`fields[]` |  `object` |  RocketChatFieldConfig defines a field for RocketChat messages.   
`httpConfig` |  `object` |  httpConfig defines the HTTP client configuration for RocketChat API requests.   
`iconURL` |  `string` |  iconURL defines the icon URL for the message avatar. This displays a custom image as the message sender’s avatar.   
`imageURL` |  `string` |  imageURL defines the image URL to display within the message. This embeds an image directly in the message attachment.   
`linkNames` |  `boolean` |  linkNames defines whether to enable automatic linking of usernames and channels. When true, @username and #channel references become clickable links.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`shortFields` |  `boolean` |  shortFields defines whether to use short fields in the message layout. When true, fields may be displayed side by side to save space.   
`text` |  `string` |  text defines the message text to send. This is optional because attachments can be used instead of or alongside text.   
`thumbURL` |  `string` |  thumbURL defines the thumbnail URL for the message. This displays a small thumbnail image alongside the message content.   
`title` |  `string` |  title defines the message title displayed prominently in the message. This appears as bold text at the top of the message attachment.   
`titleLink` |  `string` |  titleLink defines the URL that the title will link to when clicked. This makes the message title clickable in the RocketChat interface.   
`token` |  `object` |  token defines the sender token for RocketChat authentication. This is the personal access token or bot token used to authenticate API requests. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`tokenID` |  `object` |  tokenID defines the sender token ID for RocketChat authentication. This is the user ID associated with the token used for API requests. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
Show more

## 3.1.260. .spec.receivers[].rocketchatConfigs[].actions

Description
     actions defines interactive actions to include in the message. These appear as buttons that users can click to trigger responses. 
Type
     `array`

## 3.1.261. .spec.receivers[].rocketchatConfigs[].actions[]

Description
     RocketChatActionConfig defines actions for RocketChat messages. 
Type
     `object`

Property| Type| Description  
---|---|---  
`msg` |  `string` |  msg defines the message to send when the button is clicked. This allows the button to post a predefined message to the channel.   
`text` |  `string` |  text defines the button text displayed to users. This is the label that appears on the interactive button.   
`url` |  `string` |  url defines the URL the button links to when clicked. This creates a clickable button that opens the specified URL.   
Show more

## 3.1.262. .spec.receivers[].rocketchatConfigs[].fields

Description
     fields defines additional fields for the message attachment. These appear as structured key-value pairs within the message. 
Type
     `array`

## 3.1.263. .spec.receivers[].rocketchatConfigs[].fields[]

Description
     RocketChatFieldConfig defines a field for RocketChat messages. 
Type
     `object`

Property| Type| Description  
---|---|---  
`short` |  `boolean` |  short defines whether this field should be a short field. When true, the field may be displayed inline with other short fields to save space.   
`title` |  `string` |  title defines the title of this field. This appears as bold text labeling the field content.   
`value` |  `string` |  value defines the value of this field, displayed underneath the title. This contains the actual data or content for the field.   
Show more

## 3.1.264. .spec.receivers[].rocketchatConfigs[].httpConfig

Description
     httpConfig defines the HTTP client configuration for RocketChat API requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.265. .spec.receivers[].rocketchatConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.266. .spec.receivers[].rocketchatConfigs[].httpConfig.authorization.credentials

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

## 3.1.267. .spec.receivers[].rocketchatConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.268. .spec.receivers[].rocketchatConfigs[].httpConfig.basicAuth.password

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

## 3.1.269. .spec.receivers[].rocketchatConfigs[].httpConfig.basicAuth.username

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

## 3.1.270. .spec.receivers[].rocketchatConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.271. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.272. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.273. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.274. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.275. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.276. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.277. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.278. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.279. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.280. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.281. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.282. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.283. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.284. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.285. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.286. .spec.receivers[].rocketchatConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.287. .spec.receivers[].rocketchatConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.288. .spec.receivers[].rocketchatConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.289. .spec.receivers[].rocketchatConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.290. .spec.receivers[].rocketchatConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.291. .spec.receivers[].rocketchatConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.292. .spec.receivers[].rocketchatConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.293. .spec.receivers[].rocketchatConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.294. .spec.receivers[].rocketchatConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.295. .spec.receivers[].rocketchatConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.296. .spec.receivers[].rocketchatConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.297. .spec.receivers[].rocketchatConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.298. .spec.receivers[].rocketchatConfigs[].token

Description
     token defines the sender token for RocketChat authentication. This is the personal access token or bot token used to authenticate API requests. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
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

## 3.1.299. .spec.receivers[].rocketchatConfigs[].tokenID

Description
     tokenID defines the sender token ID for RocketChat authentication. This is the user ID associated with the token used for API requests. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
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

## 3.1.300. .spec.receivers[].slackConfigs

Description
     slackConfigs defines the list of Slack configurations. 
Type
     `array`

## 3.1.301. .spec.receivers[].slackConfigs[]

Description
     SlackConfig configures notifications via Slack. See <https://prometheus.io/docs/alerting/latest/configuration/#slack_config>
Type
     `object`

Property| Type| Description  
---|---|---  
`actions` |  `array` |  actions defines a list of Slack actions that are sent with each notification.   
`actions[]` |  `object` |  SlackAction configures a single Slack action that is sent with each notification. See <https://api.slack.com/docs/message-attachments#action_fields> and <https://api.slack.com/docs/message-buttons> for more information.   
`apiURL` |  `object` |  apiURL defines the secret’s key that contains the Slack webhook URL. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`callbackId` |  `string` |  callbackId defines an identifier for the message used in interactive components.   
`channel` |  `string` |  channel defines the channel or user to send notifications to.   
`color` |  `string` |  color defines the color of the left border of the Slack message attachment. Can be a hex color code (e.g., "#ff0000") or a predefined color name.   
`fallback` |  `string` |  fallback defines a plain-text summary of the attachment for clients that don’t support attachments.   
`fields` |  `array` |  fields defines a list of Slack fields that are sent with each notification.   
`fields[]` |  `object` |  SlackField configures a single Slack field that is sent with each notification. Each field must contain a title, value, and optionally, a boolean value to indicate if the field is short enough to be displayed next to other fields designated as short. See <https://api.slack.com/docs/message-attachments#fields> for more information.   
`footer` |  `string` |  footer defines small text displayed at the bottom of the message attachment.   
`httpConfig` |  `object` |  httpConfig defines the HTTP client configuration.   
`iconEmoji` |  `string` |  iconEmoji defines the emoji to use as the bot’s avatar (e.g., ":ghost:").   
`iconURL` |  `string` |  iconURL defines the URL to an image to use as the bot’s avatar.   
`imageURL` |  `string` |  imageURL defines the URL to an image file that will be displayed inside the message attachment.   
`linkNames` |  `boolean` |  linkNames enables automatic linking of channel names and usernames in the message. When true, @channel and @username will be converted to clickable links.   
`messageText` |  `string` |  messageText defines text content of the Slack message. If set, this is sent as the top-level 'text' field in the Slack payload. It requires Alertmanager >= v0.31.0.   
`mrkdwnIn` |  `array (string)` |  mrkdwnIn defines which fields should be parsed as Slack markdown. Valid values include "pretext", "text", and "fields".   
`pretext` |  `string` |  pretext defines optional text that appears above the message attachment block.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`shortFields` |  `boolean` |  shortFields determines whether fields are displayed in a compact format. When true, fields are shown side by side when possible.   
`text` |  `string` |  text defines the main text content of the Slack message attachment.   
`thumbURL` |  `string` |  thumbURL defines the URL to an image file that will be displayed as a thumbnail on the right side of the message attachment.   
`timeout` |  `string` |  timeout defines the maximum time to wait for a webhook request to complete, before failing the request and allowing it to be retried. It requires Alertmanager >= v0.30.0.   
`title` |  `string` |  title defines the title text displayed in the Slack message attachment.   
`titleLink` |  `string` |  titleLink defines the URL that the title will link to when clicked.   
`username` |  `string` |  username defines the slack bot user name.   
Show more

## 3.1.302. .spec.receivers[].slackConfigs[].actions

Description
     actions defines a list of Slack actions that are sent with each notification. 
Type
     `array`

## 3.1.303. .spec.receivers[].slackConfigs[].actions[]

Description
     SlackAction configures a single Slack action that is sent with each notification. See <https://api.slack.com/docs/message-attachments#action_fields> and <https://api.slack.com/docs/message-buttons> for more information. 
Type
     `object`
Required
    

  * `text`
  * `type`



Property| Type| Description  
---|---|---  
`confirm` |  `object` |  confirm defines an optional confirmation dialog that appears before the action is executed. When set, users must confirm their intent before the action proceeds.   
`name` |  `string` |  name defines a unique identifier for the action within the message. This value is sent back to your application when the action is triggered.   
`style` |  `string` |  style defines the visual appearance of the action element. Valid values include "default", "primary" (green), and "danger" (red).   
`text` |  `string` |  text defines the user-visible label displayed on the action element. For buttons, this is the button text. For select menus, this is the placeholder text.   
`type` |  `string` |  type defines the type of interactive component. Common values include "button" for clickable buttons and "select" for dropdown menus.   
`url` |  `string` |  url defines the URL to open when the action is triggered. Only applicable for button-type actions. When set, clicking the button opens this URL.   
`value` |  `string` |  value defines the payload sent when the action is triggered. This data is included in the callback sent to your application.   
Show more

## 3.1.304. .spec.receivers[].slackConfigs[].actions[].confirm

Description
     confirm defines an optional confirmation dialog that appears before the action is executed. When set, users must confirm their intent before the action proceeds. 
Type
     `object`
Required
    

  * `text`



Property| Type| Description  
---|---|---  
`dismissText` |  `string` |  dismissText defines the label for the cancel button in the dialog. When not specified, defaults to "Cancel". This button cancels the action.   
`okText` |  `string` |  okText defines the label for the confirmation button in the dialog. When not specified, defaults to "Okay". This button proceeds with the action.   
`text` |  `string` |  text defines the main message displayed in the confirmation dialog. This should be a clear question or statement asking the user to confirm their action.   
`title` |  `string` |  title defines the title text displayed at the top of the confirmation dialog. When not specified, a default title will be used.   
Show more

## 3.1.305. .spec.receivers[].slackConfigs[].apiURL

Description
     apiURL defines the secret’s key that contains the Slack webhook URL. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.306. .spec.receivers[].slackConfigs[].fields

Description
     fields defines a list of Slack fields that are sent with each notification. 
Type
     `array`

## 3.1.307. .spec.receivers[].slackConfigs[].fields[]

Description
     SlackField configures a single Slack field that is sent with each notification. Each field must contain a title, value, and optionally, a boolean value to indicate if the field is short enough to be displayed next to other fields designated as short. See <https://api.slack.com/docs/message-attachments#fields> for more information. 
Type
     `object`
Required
    

  * `title`
  * `value`



Property| Type| Description  
---|---|---  
`short` |  `boolean` |  short determines whether this field can be displayed alongside other short fields. When true, Slack may display this field side by side with other short fields. When false or not specified, the field takes the full width of the message.   
`title` |  `string` |  title defines the label or header text displayed for this field. This appears as bold text above the field value in the Slack message.   
`value` |  `string` |  value defines the content or data displayed for this field. This appears below the title and can contain plain text or Slack markdown.   
Show more

## 3.1.308. .spec.receivers[].slackConfigs[].httpConfig

Description
     httpConfig defines the HTTP client configuration. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.309. .spec.receivers[].slackConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.310. .spec.receivers[].slackConfigs[].httpConfig.authorization.credentials

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

## 3.1.311. .spec.receivers[].slackConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.312. .spec.receivers[].slackConfigs[].httpConfig.basicAuth.password

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

## 3.1.313. .spec.receivers[].slackConfigs[].httpConfig.basicAuth.username

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

## 3.1.314. .spec.receivers[].slackConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.315. .spec.receivers[].slackConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.316. .spec.receivers[].slackConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.317. .spec.receivers[].slackConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.318. .spec.receivers[].slackConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.319. .spec.receivers[].slackConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.320. .spec.receivers[].slackConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.321. .spec.receivers[].slackConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.322. .spec.receivers[].slackConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.323. .spec.receivers[].slackConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.324. .spec.receivers[].slackConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.325. .spec.receivers[].slackConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.326. .spec.receivers[].slackConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.327. .spec.receivers[].slackConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.328. .spec.receivers[].slackConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.329. .spec.receivers[].slackConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.330. .spec.receivers[].slackConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.331. .spec.receivers[].slackConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.332. .spec.receivers[].slackConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.333. .spec.receivers[].slackConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.334. .spec.receivers[].slackConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.335. .spec.receivers[].slackConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.336. .spec.receivers[].slackConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.337. .spec.receivers[].slackConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.338. .spec.receivers[].slackConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.339. .spec.receivers[].slackConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.340. .spec.receivers[].slackConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.341. .spec.receivers[].slackConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.342. .spec.receivers[].snsConfigs

Description
     snsConfigs defines the list of SNS configurations 
Type
     `array`

## 3.1.343. .spec.receivers[].snsConfigs[]

Description
     SNSConfig configures notifications via AWS SNS. See <https://prometheus.io/docs/alerting/latest/configuration/#sns_configs>
Type
     `object`

Property| Type| Description  
---|---|---  
`apiURL` |  `string` |  apiURL defines the SNS API URL, e.g. <https://sns.us-east-2.amazonaws.com>. If not specified, the SNS API URL from the SNS SDK will be used.   
`attributes` |  `object (string)` |  attributes defines SNS message attributes as key-value pairs. These provide additional metadata that can be used for message filtering and routing.   
`httpConfig` |  `object` |  httpConfig defines the HTTP client configuration for SNS API requests.   
`message` |  `string` |  message defines the message content of the SNS notification. This is the actual notification text that will be sent to subscribers.   
`phoneNumber` |  `string` |  phoneNumber defines the phone number if message is delivered via SMS in E.164 format. If you don’t specify this value, you must specify a value for the TopicARN or TargetARN.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`sigv4` |  `object` |  sigv4 configures AWS’s Signature Verification 4 signing process to sign requests. This includes AWS credentials and region configuration for authentication.   
`subject` |  `string` |  subject defines the subject line when the message is delivered to email endpoints. This field is only used when sending to email subscribers of an SNS topic.   
`targetARN` |  `string` |  targetARN defines the mobile platform endpoint ARN if message is delivered via mobile notifications. If you don’t specify this value, you must specify a value for the TopicARN or PhoneNumber.   
`topicARN` |  `string` |  topicARN defines the SNS topic ARN, e.g. arn:aws:sns:us-east-2:698519295917:My-Topic. If you don’t specify this value, you must specify a value for the PhoneNumber or TargetARN.   
Show more

## 3.1.344. .spec.receivers[].snsConfigs[].httpConfig

Description
     httpConfig defines the HTTP client configuration for SNS API requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.345. .spec.receivers[].snsConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.346. .spec.receivers[].snsConfigs[].httpConfig.authorization.credentials

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

## 3.1.347. .spec.receivers[].snsConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.348. .spec.receivers[].snsConfigs[].httpConfig.basicAuth.password

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

## 3.1.349. .spec.receivers[].snsConfigs[].httpConfig.basicAuth.username

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

## 3.1.350. .spec.receivers[].snsConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.351. .spec.receivers[].snsConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.352. .spec.receivers[].snsConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.353. .spec.receivers[].snsConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.354. .spec.receivers[].snsConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.355. .spec.receivers[].snsConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.356. .spec.receivers[].snsConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.357. .spec.receivers[].snsConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.358. .spec.receivers[].snsConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.359. .spec.receivers[].snsConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.360. .spec.receivers[].snsConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.361. .spec.receivers[].snsConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.362. .spec.receivers[].snsConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.363. .spec.receivers[].snsConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.364. .spec.receivers[].snsConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.365. .spec.receivers[].snsConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.366. .spec.receivers[].snsConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.367. .spec.receivers[].snsConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.368. .spec.receivers[].snsConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.369. .spec.receivers[].snsConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.370. .spec.receivers[].snsConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.371. .spec.receivers[].snsConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.372. .spec.receivers[].snsConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.373. .spec.receivers[].snsConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.374. .spec.receivers[].snsConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.375. .spec.receivers[].snsConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.376. .spec.receivers[].snsConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.377. .spec.receivers[].snsConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.378. .spec.receivers[].snsConfigs[].sigv4

Description
     sigv4 configures AWS’s Signature Verification 4 signing process to sign requests. This includes AWS credentials and region configuration for authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`accessKey` |  `object` |  accessKey defines the AWS API key. If not specified, the environment variable `AWS_ACCESS_KEY_ID` is used.   
`profile` |  `string` |  profile defines the named AWS profile used to authenticate.   
`region` |  `string` |  region defines the AWS region. If blank, the region from the default credentials chain used.   
`roleArn` |  `string` |  roleArn defines the named AWS profile used to authenticate.   
`secretKey` |  `object` |  secretKey defines the AWS API secret. If not specified, the environment variable `AWS_SECRET_ACCESS_KEY` is used.   
`useFIPSSTSEndpoint` |  `boolean` |  useFIPSSTSEndpoint defines the FIPS mode for the AWS STS endpoint. It requires Prometheus >= v2.54.0.   
Show more

## 3.1.379. .spec.receivers[].snsConfigs[].sigv4.accessKey

Description
     accessKey defines the AWS API key. If not specified, the environment variable `AWS_ACCESS_KEY_ID` is used. 
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

## 3.1.380. .spec.receivers[].snsConfigs[].sigv4.secretKey

Description
     secretKey defines the AWS API secret. If not specified, the environment variable `AWS_SECRET_ACCESS_KEY` is used. 
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

## 3.1.381. .spec.receivers[].telegramConfigs

Description
     telegramConfigs defines the list of Telegram configurations. 
Type
     `array`

## 3.1.382. .spec.receivers[].telegramConfigs[]

Description
     TelegramConfig configures notifications via Telegram. See <https://prometheus.io/docs/alerting/latest/configuration/#telegram_config>
Type
     `object`
Required
    

  * `chatID`



Property| Type| Description  
---|---|---  
`apiURL` |  `string` |  apiURL defines the Telegram API URL, e.g. <https://api.telegram.org>. If not specified, the default Telegram API URL will be used.   
`botToken` |  `object` |  botToken defines the Telegram bot token. It is mutually exclusive with `botTokenFile`. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. Either `botToken` or `botTokenFile` is required.   
`botTokenFile` |  `string` |  botTokenFile defines the file to read the Telegram bot token from. It is mutually exclusive with `botToken`. Either `botToken` or `botTokenFile` is required. It requires Alertmanager >= v0.26.0.   
`chatID` |  `integer` |  chatID defines the Telegram chat ID where messages will be sent. This can be a user ID, group ID, or channel ID (with @ prefix for public channels).   
`disableNotifications` |  `boolean` |  disableNotifications controls whether Telegram notifications are sent silently. When true, users will receive the message without notification sounds.   
`httpConfig` |  `object` |  httpConfig defines the HTTP client configuration for Telegram API requests.   
`message` |  `string` |  message defines the message template for the Telegram notification. This is the content that will be sent to the specified chat.   
`messageThreadID` |  `integer` |  messageThreadID defines the Telegram Group Topic ID for threaded messages. This allows sending messages to specific topics within Telegram groups. It requires Alertmanager >= 0.26.0.   
`parseMode` |  `string` |  parseMode defines the parse mode for telegram message formatting. Valid values are "MarkdownV2", "Markdown", and "HTML". This determines how text formatting is interpreted in the message.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
Show more

## 3.1.383. .spec.receivers[].telegramConfigs[].botToken

Description
     botToken defines the Telegram bot token. It is mutually exclusive with `botTokenFile`. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. Either `botToken` or `botTokenFile` is required. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.384. .spec.receivers[].telegramConfigs[].httpConfig

Description
     httpConfig defines the HTTP client configuration for Telegram API requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.385. .spec.receivers[].telegramConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.386. .spec.receivers[].telegramConfigs[].httpConfig.authorization.credentials

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

## 3.1.387. .spec.receivers[].telegramConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.388. .spec.receivers[].telegramConfigs[].httpConfig.basicAuth.password

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

## 3.1.389. .spec.receivers[].telegramConfigs[].httpConfig.basicAuth.username

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

## 3.1.390. .spec.receivers[].telegramConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.391. .spec.receivers[].telegramConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.392. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.393. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.394. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.395. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.396. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.397. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.398. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.399. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.400. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.401. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.402. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.403. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.404. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.405. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.406. .spec.receivers[].telegramConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.407. .spec.receivers[].telegramConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.408. .spec.receivers[].telegramConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.409. .spec.receivers[].telegramConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.410. .spec.receivers[].telegramConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.411. .spec.receivers[].telegramConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.412. .spec.receivers[].telegramConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.413. .spec.receivers[].telegramConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.414. .spec.receivers[].telegramConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.415. .spec.receivers[].telegramConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.416. .spec.receivers[].telegramConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.417. .spec.receivers[].telegramConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.418. .spec.receivers[].victoropsConfigs

Description
     victoropsConfigs defines the list of VictorOps configurations. 
Type
     `array`

## 3.1.419. .spec.receivers[].victoropsConfigs[]

Description
     VictorOpsConfig configures notifications via VictorOps. See <https://prometheus.io/docs/alerting/latest/configuration/#victorops_config>
Type
     `object`
Required
    

  * `routingKey`



Property| Type| Description  
---|---|---  
`apiKey` |  `object` |  apiKey defines the secret’s key that contains the API key to use when talking to the VictorOps API. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`apiUrl` |  `string` |  apiUrl defines the VictorOps API URL. When not specified, defaults to the standard VictorOps API endpoint.   
`customFields` |  `array` |  customFields defines additional custom fields for notification. These provide extra metadata that will be included with the VictorOps incident.   
`customFields[]` |  `object` |  KeyValue defines a (key, value) tuple.   
`entityDisplayName` |  `string` |  entityDisplayName contains a summary of the alerted problem. This appears as the main title or identifier for the incident.   
`httpConfig` |  `object` |  httpConfig defines the HTTP client’s configuration for VictorOps API requests.   
`messageType` |  `string` |  messageType describes the behavior of the alert. Valid values are "CRITICAL", "WARNING", and "INFO".   
`monitoringTool` |  `string` |  monitoringTool defines the monitoring tool the state message is from. This helps identify the source system that generated the alert.   
`routingKey` |  `string` |  routingKey defines a key used to map the alert to a team. This determines which VictorOps team will receive the alert notification.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`stateMessage` |  `string` |  stateMessage contains a long explanation of the alerted problem. This provides detailed context about the incident.   
Show more

## 3.1.420. .spec.receivers[].victoropsConfigs[].apiKey

Description
     apiKey defines the secret’s key that contains the API key to use when talking to the VictorOps API. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.421. .spec.receivers[].victoropsConfigs[].customFields

Description
     customFields defines additional custom fields for notification. These provide extra metadata that will be included with the VictorOps incident. 
Type
     `array`

## 3.1.422. .spec.receivers[].victoropsConfigs[].customFields[]

Description
     KeyValue defines a (key, value) tuple. 
Type
     `object`
Required
    

  * `key`
  * `value`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the tuple. This is the identifier or name part of the key-value pair.   
`value` |  `string` |  value defines the value of the tuple. This is the data or content associated with the key.   
Show more

## 3.1.423. .spec.receivers[].victoropsConfigs[].httpConfig

Description
     httpConfig defines the HTTP client’s configuration for VictorOps API requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.424. .spec.receivers[].victoropsConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.425. .spec.receivers[].victoropsConfigs[].httpConfig.authorization.credentials

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

## 3.1.426. .spec.receivers[].victoropsConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.427. .spec.receivers[].victoropsConfigs[].httpConfig.basicAuth.password

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

## 3.1.428. .spec.receivers[].victoropsConfigs[].httpConfig.basicAuth.username

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

## 3.1.429. .spec.receivers[].victoropsConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.430. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.431. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.432. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.433. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.434. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.435. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.436. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.437. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.438. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.439. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.440. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.441. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.442. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.443. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.444. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.445. .spec.receivers[].victoropsConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.446. .spec.receivers[].victoropsConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.447. .spec.receivers[].victoropsConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.448. .spec.receivers[].victoropsConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.449. .spec.receivers[].victoropsConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.450. .spec.receivers[].victoropsConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.451. .spec.receivers[].victoropsConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.452. .spec.receivers[].victoropsConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.453. .spec.receivers[].victoropsConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.454. .spec.receivers[].victoropsConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.455. .spec.receivers[].victoropsConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.456. .spec.receivers[].victoropsConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.457. .spec.receivers[].webexConfigs

Description
     webexConfigs defines the list of Webex configurations. 
Type
     `array`

## 3.1.458. .spec.receivers[].webexConfigs[]

Description
     WebexConfig configures notification via Cisco Webex See <https://prometheus.io/docs/alerting/latest/configuration/#webex_config>
Type
     `object`
Required
    

  * `roomID`



Property| Type| Description  
---|---|---  
`apiURL` |  `string` |  apiURL defines the Webex Teams API URL i.e. <https://webexapis.com/v1/messages>  
`httpConfig` |  `object` |  httpConfig defines the HTTP client’s configuration. You must use this configuration to supply the bot token as part of the HTTP `Authorization` header.   
`message` |  `string` |  message defines the message template   
`roomID` |  `string` |  roomID defines the ID of the Webex Teams room where to send the messages.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
Show more

## 3.1.459. .spec.receivers[].webexConfigs[].httpConfig

Description
     httpConfig defines the HTTP client’s configuration. You must use this configuration to supply the bot token as part of the HTTP `Authorization` header. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.460. .spec.receivers[].webexConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.461. .spec.receivers[].webexConfigs[].httpConfig.authorization.credentials

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

## 3.1.462. .spec.receivers[].webexConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.463. .spec.receivers[].webexConfigs[].httpConfig.basicAuth.password

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

## 3.1.464. .spec.receivers[].webexConfigs[].httpConfig.basicAuth.username

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

## 3.1.465. .spec.receivers[].webexConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.466. .spec.receivers[].webexConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.467. .spec.receivers[].webexConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.468. .spec.receivers[].webexConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.469. .spec.receivers[].webexConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.470. .spec.receivers[].webexConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.471. .spec.receivers[].webexConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.472. .spec.receivers[].webexConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.473. .spec.receivers[].webexConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.474. .spec.receivers[].webexConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.475. .spec.receivers[].webexConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.476. .spec.receivers[].webexConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.477. .spec.receivers[].webexConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.478. .spec.receivers[].webexConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.479. .spec.receivers[].webexConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.480. .spec.receivers[].webexConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.481. .spec.receivers[].webexConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.482. .spec.receivers[].webexConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.483. .spec.receivers[].webexConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.484. .spec.receivers[].webexConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.485. .spec.receivers[].webexConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.486. .spec.receivers[].webexConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.487. .spec.receivers[].webexConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.488. .spec.receivers[].webexConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.489. .spec.receivers[].webexConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.490. .spec.receivers[].webexConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.491. .spec.receivers[].webexConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.492. .spec.receivers[].webexConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.493. .spec.receivers[].webhookConfigs

Description
     webhookConfigs defines the List of webhook configurations. 
Type
     `array`

## 3.1.494. .spec.receivers[].webhookConfigs[]

Description
     WebhookConfig configures notifications via a generic receiver supporting the webhook payload. See <https://prometheus.io/docs/alerting/latest/configuration/#webhook_config>
Type
     `object`

Property| Type| Description  
---|---|---  
`httpConfig` |  `object` |  httpConfig defines the HTTP client configuration for webhook requests.   
`maxAlerts` |  `integer` |  maxAlerts defines the maximum number of alerts to be sent per webhook message. When 0, all alerts are included in the webhook payload.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`timeout` |  `string` |  timeout defines the maximum time to wait for a webhook request to complete, before failing the request and allowing it to be retried. It requires Alertmanager >= v0.28.0.   
`url` |  `string` |  url defines the URL to send HTTP POST requests to. urlSecret takes precedence over url. One of urlSecret and url should be defined.   
`urlSecret` |  `object` |  urlSecret defines the secret’s key that contains the webhook URL to send HTTP requests to. urlSecret takes precedence over url. One of urlSecret and url should be defined. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
Show more

## 3.1.495. .spec.receivers[].webhookConfigs[].httpConfig

Description
     httpConfig defines the HTTP client configuration for webhook requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.496. .spec.receivers[].webhookConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.497. .spec.receivers[].webhookConfigs[].httpConfig.authorization.credentials

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

## 3.1.498. .spec.receivers[].webhookConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.499. .spec.receivers[].webhookConfigs[].httpConfig.basicAuth.password

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

## 3.1.500. .spec.receivers[].webhookConfigs[].httpConfig.basicAuth.username

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

## 3.1.501. .spec.receivers[].webhookConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.502. .spec.receivers[].webhookConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.503. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.504. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.505. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.506. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.507. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.508. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.509. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.510. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.511. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.512. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.513. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.514. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.515. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.516. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.517. .spec.receivers[].webhookConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.518. .spec.receivers[].webhookConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.519. .spec.receivers[].webhookConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.520. .spec.receivers[].webhookConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.521. .spec.receivers[].webhookConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.522. .spec.receivers[].webhookConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.523. .spec.receivers[].webhookConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.524. .spec.receivers[].webhookConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.525. .spec.receivers[].webhookConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.526. .spec.receivers[].webhookConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.527. .spec.receivers[].webhookConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.528. .spec.receivers[].webhookConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.529. .spec.receivers[].webhookConfigs[].urlSecret

Description
     urlSecret defines the secret’s key that contains the webhook URL to send HTTP requests to. urlSecret takes precedence over url. One of urlSecret and url should be defined. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.530. .spec.receivers[].wechatConfigs

Description
     wechatConfigs defines the list of WeChat configurations. 
Type
     `array`

## 3.1.531. .spec.receivers[].wechatConfigs[]

Description
     WeChatConfig configures notifications via WeChat. See <https://prometheus.io/docs/alerting/latest/configuration/#wechat_config>
Type
     `object`

Property| Type| Description  
---|---|---  
`agentID` |  `string` |  agentID defines the application agent ID within WeChat Work. This identifies which WeChat Work application will send the notifications.   
`apiSecret` |  `object` |  apiSecret defines the secret’s key that contains the WeChat API key. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`apiURL` |  `string` |  apiURL defines the WeChat API URL. When not specified, defaults to the standard WeChat Work API endpoint.   
`corpID` |  `string` |  corpID defines the corp id for authentication. This is the unique identifier for your WeChat Work organization.   
`httpConfig` |  `object` |  httpConfig defines the HTTP client configuration for WeChat API requests.   
`message` |  `string` |  message defines the API request data as defined by the WeChat API. This contains the actual notification content to be sent.   
`messageType` |  `string` |  messageType defines the type of message to send. Valid values include "text", "markdown", and other WeChat Work supported message types.   
`sendResolved` |  `boolean` |  sendResolved defines whether or not to notify about resolved alerts.   
`toParty` |  `string` |  toParty defines the target department(s) to receive the notification. Can be a single department ID or multiple department IDs separated by '|'.   
`toTag` |  `string` |  toTag defines the target tag(s) to receive the notification. Can be a single tag ID or multiple tag IDs separated by '|'.   
`toUser` |  `string` |  toUser defines the target user(s) to receive the notification. Can be a single user ID or multiple user IDs separated by '|'.   
Show more

## 3.1.532. .spec.receivers[].wechatConfigs[].apiSecret

Description
     apiSecret defines the secret’s key that contains the WeChat API key. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.533. .spec.receivers[].wechatConfigs[].httpConfig

Description
     httpConfig defines the HTTP client configuration for WeChat API requests. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+.   
`basicAuth` |  `object` |  basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether HTTP requests follow HTTP 3xx redirects. When true, the client will automatically follow redirect responses.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyURL` |  `string` |  proxyURL defines an optional proxy URL for HTTP requests. If defined, this field takes precedence over `proxyUrl`.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options.   
Show more

## 3.1.534. .spec.receivers[].wechatConfigs[].httpConfig.authorization

Description
     authorization defines the authorization header configuration for the client. This is mutually exclusive with BasicAuth and is only available starting from Alertmanager v0.22+. 
Type
     `object`

Property| Type| Description  
---|---|---  
`credentials` |  `object` |  credentials defines a key of a Secret in the namespace that contains the credentials for authentication.   
`type` |  `string` |  type defines the authentication type. The value is case-insensitive.  "Basic" is not a supported value.  Default: "Bearer"   
Show more

## 3.1.535. .spec.receivers[].wechatConfigs[].httpConfig.authorization.credentials

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

## 3.1.536. .spec.receivers[].wechatConfigs[].httpConfig.basicAuth

Description
     basicAuth defines the basic authentication credentials for the client. This is mutually exclusive with Authorization. If both are defined, BasicAuth takes precedence. 
Type
     `object`

Property| Type| Description  
---|---|---  
`password` |  `object` |  password defines a key of a Secret containing the password for authentication.   
`username` |  `object` |  username defines a key of a Secret containing the username for authentication.   
Show more

## 3.1.537. .spec.receivers[].wechatConfigs[].httpConfig.basicAuth.password

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

## 3.1.538. .spec.receivers[].wechatConfigs[].httpConfig.basicAuth.username

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

## 3.1.539. .spec.receivers[].wechatConfigs[].httpConfig.bearerTokenSecret

Description
     bearerTokenSecret defines the secret’s key that contains the bearer token to be used by the client for authentication. The secret needs to be in the same namespace as the AlertmanagerConfig object and accessible by the Prometheus Operator. 
Type
     `object`
Required
    

  * `key`
  * `name`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key defines the key of the secret to select from. Must be a valid secret key.   
`name` |  `string` |  name defines the name of the secret in the object’s namespace to select from.   
Show more

## 3.1.540. .spec.receivers[].wechatConfigs[].httpConfig.oauth2

Description
     oauth2 defines the OAuth2 client credentials used to fetch a token for the targets. This enables OAuth2 authentication flow for HTTP requests. 
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

## 3.1.541. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.542. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.clientId.configMap

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

## 3.1.543. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.clientId.secret

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

## 3.1.544. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.clientSecret

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

## 3.1.545. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.546. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.547. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.proxyConnectHeader{}[]

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

## 3.1.548. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.tlsConfig

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

## 3.1.549. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.550. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.tlsConfig.ca.configMap

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

## 3.1.551. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.tlsConfig.ca.secret

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

## 3.1.552. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.553. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.tlsConfig.cert.configMap

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

## 3.1.554. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.tlsConfig.cert.secret

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

## 3.1.555. .spec.receivers[].wechatConfigs[].httpConfig.oauth2.tlsConfig.keySecret

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

## 3.1.556. .spec.receivers[].wechatConfigs[].httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 3.1.557. .spec.receivers[].wechatConfigs[].httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 3.1.558. .spec.receivers[].wechatConfigs[].httpConfig.proxyConnectHeader{}[]

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

## 3.1.559. .spec.receivers[].wechatConfigs[].httpConfig.tlsConfig

Description
     tlsConfig defines the TLS configuration for the client. This includes settings for certificates, CA validation, and TLS protocol options. 
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

## 3.1.560. .spec.receivers[].wechatConfigs[].httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.561. .spec.receivers[].wechatConfigs[].httpConfig.tlsConfig.ca.configMap

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

## 3.1.562. .spec.receivers[].wechatConfigs[].httpConfig.tlsConfig.ca.secret

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

## 3.1.563. .spec.receivers[].wechatConfigs[].httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 3.1.564. .spec.receivers[].wechatConfigs[].httpConfig.tlsConfig.cert.configMap

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

## 3.1.565. .spec.receivers[].wechatConfigs[].httpConfig.tlsConfig.cert.secret

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

## 3.1.566. .spec.receivers[].wechatConfigs[].httpConfig.tlsConfig.keySecret

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

## 3.1.567. .spec.route

Description
     route defines the Alertmanager route definition for alerts matching the resource’s namespace. If present, it will be added to the generated Alertmanager configuration as a first-level route. 
Type
     `object`

Property| Type| Description  
---|---|---  
`activeTimeIntervals` |  `array (string)` |  activeTimeIntervals is a list of TimeInterval names when this route should be active.   
`continue` |  `boolean` |  continue defines the boolean indicating whether an alert should continue matching subsequent sibling nodes. It will always be overridden to true for the first-level route by the Prometheus operator.   
`groupBy` |  `array (string)` |  groupBy defines the list of labels to group by. Labels must not be repeated (unique list). Special label "…​" (aggregate by all possible labels), if provided, must be the only element in the list.   
`groupInterval` |  `string` |  groupInterval defines how long to wait before sending an updated notification. Must be greater than 0. Example: "5m"   
`groupWait` |  `string` |  groupWait defines how long to wait before sending the initial notification. Example: "30s"   
`matchers` |  `array` |  matchers defines the list of matchers that the alert’s labels should match. For the first level route, the operator removes any existing equality and regexp matcher on the `namespace` label and adds a `namespace: <object namespace>` matcher.   
`matchers[]` |  `object` |  Matcher defines how to match on alert’s labels.   
`muteTimeIntervals` |  `array (string)` |  muteTimeIntervals is a list of MuteTimeInterval names that will mute this route when matched,   
`receiver` |  `string` |  receiver defines the name of the receiver for this route. If not empty, it should be listed in the `receivers` field.   
`repeatInterval` |  `string` |  repeatInterval defines how long to wait before repeating the last notification. Must be greater than 0. Example: "4h"   
`routes` |  `array (undefined)` |  routes defines the child routes.   
Show more

## 3.1.568. .spec.route.matchers

Description
     matchers defines the list of matchers that the alert’s labels should match. For the first level route, the operator removes any existing equality and regexp matcher on the `namespace` label and adds a `namespace: <object namespace>` matcher. 
Type
     `array`

## 3.1.569. .spec.route.matchers[]

Description
     Matcher defines how to match on alert’s labels. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`matchType` |  `string` |  matchType defines the match operation available with AlertManager >= v0.22.0. Takes precedence over Regex (deprecated) if non-empty. Valid values: "=" (equality), "!=" (inequality), "=~" (regex match), "!~" (regex non-match).   
`name` |  `string` |  name defines the label to match. This specifies which alert label should be evaluated.   
`value` |  `string` |  value defines the label value to match. This is the expected value for the specified label.   
Show more

## 3.1.570. .spec.timeIntervals

Description
     timeIntervals defines the list of timeIntervals specifying when the routes should be muted. 
Type
     `array`

## 3.1.571. .spec.timeIntervals[]

Description
     TimeInterval specifies the periods in time when notifications will be muted or active. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name of the time interval.   
`timeIntervals` |  `array` |  timeIntervals defines a list of TimePeriod.   
`timeIntervals[]` |  `object` |  TimePeriod describes periods of time.   
Show more

## 3.1.572. .spec.timeIntervals[].timeIntervals

Description
     timeIntervals defines a list of TimePeriod. 
Type
     `array`

## 3.1.573. .spec.timeIntervals[].timeIntervals[]

Description
     TimePeriod describes periods of time. 
Type
     `object`

Property| Type| Description  
---|---|---  
`daysOfMonth` |  `array` |  daysOfMonth defines a list of DayOfMonthRange   
`daysOfMonth[]` |  `object` |  DayOfMonthRange is an inclusive range of days of the month beginning at 1   
`months` |  `array (string)` |  months defines a list of MonthRange   
`times` |  `array` |  times defines a list of TimeRange   
`times[]` |  `object` |  TimeRange defines a start and end time in 24hr format   
`weekdays` |  `array (string)` |  weekdays defines a list of WeekdayRange   
`years` |  `array (string)` |  years defines a list of YearRange   
Show more

## 3.1.574. .spec.timeIntervals[].timeIntervals[].daysOfMonth

Description
     daysOfMonth defines a list of DayOfMonthRange 
Type
     `array`

## 3.1.575. .spec.timeIntervals[].timeIntervals[].daysOfMonth[]

Description
     DayOfMonthRange is an inclusive range of days of the month beginning at 1 
Type
     `object`

Property| Type| Description  
---|---|---  
`end` |  `integer` |  end of the inclusive range   
`start` |  `integer` |  start of the inclusive range   
Show more

## 3.1.576. .spec.timeIntervals[].timeIntervals[].times

Description
     times defines a list of TimeRange 
Type
     `array`

## 3.1.577. .spec.timeIntervals[].timeIntervals[].times[]

Description
     TimeRange defines a start and end time in 24hr format 
Type
     `object`

Property| Type| Description  
---|---|---  
`endTime` |  `string` |  endTime defines the end time in 24hr format.   
`startTime` |  `string` |  startTime defines the start time in 24hr format.   
Show more

## 3.1.578. .status

Description
    

status defines the status subresource. It is under active development and is updated only when the "StatusForConfigurationResources" feature gate is enabled. 

Most recent observed status of the ServiceMonitor. Read-only. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>

Type
     `object`

Property| Type| Description  
---|---|---  
`bindings` |  `array` |  bindings defines the list of workload resources (Prometheus, PrometheusAgent, ThanosRuler or Alertmanager) which select the configuration resource.   
`bindings[]` |  `object` |  WorkloadBinding is a link between a configuration resource and a workload resource.   
Show more

## 3.1.579. .status.bindings

Description
     bindings defines the list of workload resources (Prometheus, PrometheusAgent, ThanosRuler or Alertmanager) which select the configuration resource. 
Type
     `array`

## 3.1.580. .status.bindings[]

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

## 3.1.581. .status.bindings[].conditions

Description
     conditions defines the current state of the configuration resource when bound to the referenced Workload object. 
Type
     `array`

## 3.1.582. .status.bindings[].conditions[]

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
