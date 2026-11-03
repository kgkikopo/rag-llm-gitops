# 13.9. External Secrets Operator for Red Hat OpenShift APIs

External Secrets Operator for Red Hat OpenShift uses the following two APIs to configure the `external-secrets` application deployment. 

Group| Version| Kind  
---|---|---  
`operator.openshift.io` |  `v1alpha1` |  `externalsecretsConfig`  
`operator.openshift.io` |  `v1alpha1` |  `externalsecretsmanager`  
Show more

The following list contains the External Secrets Operator for Red Hat OpenShift APIs: 

  * ExternalSecretsConfig 
  * ExternalSecretsManager 



## 13.9.1. applicationConfig

The `applicationConfig` object customizes the runtime behavior and deployment constraints of the operand. Use this section to control observability, define the operational scope, and configure webhook specifics. Additionally, you can tailor the deployment to your infrastructure requirements. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`logLevel` |  _integer_ |  `logLevel` supports a range of values as defined in the [kubernetes logging guidelines](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-instrumentation/logging.md#what-method-to-use).  |  1  |  The maximum range value is 5  The minimum range value is 1  Optional   
`operatingNamespace` |  _string_ |  `operatingNamespace` restricts the `external-secrets` operand operations to the provided namespace. Enabling this field disables `ClusterSecretStore` and `ClusterExternalSecret`.  |  |  The maximum length is 63  The minimum length is 1  Optional   
`webhookConfig` |  _object_ |  `webhookConfig` configures webhook specifics of the `external-secrets` operand.  |  |   
`resources` |  [_ResourceRequirements_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#resourcerequirements-v1-core) |  `resources` defines the resource requirements. You cannot change the value of this field after setting it initially. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |  |  Optional   
`affinity` |  [_Affinity_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#affinity-v1-core) |  `affinity` sets the scheduling affinity rules. For more information, see <https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/> |  |  Optional   
`tolerations` |  [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#toleration-v1-core) _array_ |  `tolerations` sets the pod tolerations. For more information, see <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/> |  |  The maximum number of items is 50  The minimum number of items is 0  Optional   
`nodeSelector` |  _object (keys:string, values:string)_ |  `nodeSelector` defines the scheduling criteria by using node labels. For more information, see <https://kubernetes.io/docs/concepts/configuration/assign-pod-node/> |  |  The maximum number of properties is 50  The minimum number of properties is 0  Optional   
`proxy` |  _object (keys:string, values:string)_ |  `proxy` sets the proxy configurations available in operand containers managed by the Operator as environment variables.  |  |  Optional   
Show more

## 13.9.2. bitwardenSecretManagerProvider

To enable the Bitwarden secrets manager provider and set up the additional service required to connect to the Bitwarden server, you can configure the `bitwardenSecretManagerProvider` field. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`mode` |  _string_ |  `mode` field enables the `bitwardenSecretManagerProvider` provider state, which can be set to `Enabled` or `Disabled`. If set to `Enabled`, the Operator ensures the plugin is deployed and synchronized. If set to `Disabled`, the Bitwarden provider plugin reconciliation is disabled. The plugin and resources remain in their current state, and are not managed by the Operator.  |  `Disabled` |  enum: [Enabled Disabled]  Optional   
`secretRef` |  _SecretReference_ |  `SecretRef` specifies the Kubernetes secret that contains the TLS key pair for the Bitwarden server. If this reference is not provided and the `certManagerConfig` field is configured, the issuer defined in `certManagerConfig` generates the required certificate. The secret must use `tls.crt` for certificate, `tls.key` for the private key, and `ca.crt` for CA certificate.  |  |  Optional   
Show more

## 13.9.3. certManagerConfig

You can integrate the External Secrets Operator for Red Hat OpenShift with cert-manager to secure internal webhooks. Use these settings to replace the default internal certificate management with cert-manager, specify custom issuers, and define certificate lifecycle and renewal policies. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`mode` |  _string_ |  `mode` specifies whether to use cert-manager for certificate management instead of the built-in `cert-controller` which can be indicated by setting either `Enabled` or `Disabled`. If set to `Enabled`, uses `cert-manager` for obtaining the certificates for the webhook server and other components. If set to `Disabled`, uses the `cert-controller` for obtaining the certificates for the webhook server. `Disabled` is the default behavior.  |  |  enum: [Enabled Disabled]   
`injectAnnotations` |  _string_ |  `injectAnnotations` adds the `cert-manager.io/inject-ca-from` annotation to the webhooks and custom resource definitions (CRDs) to automatically configure the webhook with the `cert-manager` Operator certificate authority (CA). This requires CA Injector to be enabled in `cert-manager` Operator. Set this field to `true` or `false`. When set, this field cannot be changed.  |  false  |  enum: [true false]   
`issuerRef` |  _ObjectReference_ |  `issuerRef` contains details of the referenced object used for obtaining certificates. The object must exist in the `external-secrets` namespace unless a cluster-scoped `cert-manager` Operator issuer is used.  |  |   
`certificateDuration` |  [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#duration-v1-meta) |  `certificateDuration` sets the validity period of the webhook certificate.  |  8760h  |   
`certificateRenewBefore` |  [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#duration-v1-meta) |  `certificateRenewBefore` sets the ahead time to renew the webhook certificate before expiry.  |  30m  |   
Show more

## 13.9.4. certProvidersConfig

The `certProvidersConfig` defines the configuration for the certificate providers used to manage TLS certificates for webhook and plugins. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`certManager` |  _object_ |  `certManager` defines the configuration for `cert-manager` provider specifics.  |  |   
Show more

## 13.9.5. commonConfigs

The `commonConfigs` specifies the common configurations available for all operands managed by the Operator. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`logLevel` |  _integer_ |  `logLevel` supports the value range as defined in the [_Time_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#time-v1-meta).  |  1  |  The maximum number of log levels is 5.  The minimum number of log levels is 1.   
`resources` |  [_ResourceRequirements_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#resourcerequirements-v1-core).  |  `resources` defines the resource requirements. This cannot be updated. See [Resource Management for Pods and Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).  |  |   
`affinity` |  [_affinity_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#affinity-v1-core).  |  `affinity` is used for setting scheduling affinity rules. See See [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/).  |  |   
`tolerations` |  [_toleration array_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#toleration-v1-core) |  `tolerations` sets the pod tolerations.  |  |  The maximum number of items is 50.  The minimum number of items is 0.   
`nodeSelector` |  _object (keys:string, values:string)_ |  `nodeSelector` defines the scheduling criteria using node labels.  |  |  The maximum number of properties is 50.  The minimum number of properties is 0.   
`proxy` |  _proxyConfig_ |  `proxy` sets the proxy configurations which are made available in operand containers managed by the Operator as environment variables.  |  |   
Show more

## 13.9.6. componentConfig

The `componentConfig` field defines configuration overrides for a specific `external-secrets` component. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`componentName` |  _string_ |  `componentName` identifies which `external-secrets` component this configuration applies to. Valid values are `ExternalSecretsCoreController`, `Webhook`, `CertController`, and `BitwardenSDKServer`.  |  |  Enum: [`ExternalSecretsCoreController`, `Webhook`, `CertController`, `BitwardenSDKServer`]  Required   
`deploymentConfigs` |  _object_ |  `deploymentConfigs` specifies overrides for the Kubernetes Deployment resource of this component.  |  |   
`overrideEnv` |  **EnvVar** _array_ |  `overrideEnv` specifies custom environment variables for this component’s container. These are merged with operator-managed environment variables, with user-defined values taking precedence. Environment variable names starting with `HOSTNAME`, `KUBERNETES_` or `EXTERNAL_SECRETS_` are reserved and are not allowed.  |  |  The maximum number of items is 50.   
Show more

## 13.9.7. componentName

The `componentName` field represents the different external-secrets components that can have network policies applied. 

Field| Type| Description  
---|---|---  
`ExternalSecretsCoreController` |  _object_ |  `ExternalSecretsCoreController` represents the `external-secret` component.   
`BitwardenSDKServer` |  _object_ |  `BitwardenSDKServer` represents the `bitwarden-sdk-server` component.   
`Webhook` |  _object_ |  `Webhook` represents the `external-secrets` webhook component.   
`CertController` |  _object_ |  `CertController` represents the `cert-controller` component.   
Show more

## 13.9.8. condition

The `condition` object reports the current health and operational state of the External Secrets Operator for Red Hat OpenShift deployment. 

It provides a standardized status check by detailing the specific type of condition, its current status, and a message to verify deployment success or troubleshooting errors. 

Field| Type| Description  
---|---|---  
`type` |  _string_ |  `type` contains the condition of the deployment.   
`status` |  [_ConditionStatus_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#conditionstatus-v1-meta) |  `status` contains the status of the condition of the deployment   
`message` |  _string_ |  `message` provides details on the state of the deployment   
Show more

## 13.9.9. conditionalStatus

The `conditionalStatus` field holds information about the current state of the `external-secrets` deployment. 

Field| Type| Description  
---|---|---  
`conditions` |  _array_ |  `conditions` contains information on the current state of the deployment.   
Show more

## 13.9.10. configMapKeyReference

The `configMapKeyReference` specifies a specific key in a ConfigMap. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`name` |  _string_ |  `name` specifies the name of the ConfigMap resource being referred to.  |  |  The maximum length of the name is 253 characters.  The minimum length of the name is 1 character.   
`key` |  _string_ |  `key` specifies the specific key to be used in the ConfigMap. When ommitted, defaults to `ca-bundle.crt`.  |  `ca-bundle.crt` |  The maximum length of the key is 253 characters.  The minimum length of the key is 1 character.  The pattern is: `^[-._a-zA-Z0-9]+$`  
Show more

## 13.9.11. controllerConfig

The `controllerConfig` specifies the configurations used by the controller when installing the `external-secrets` operand and the plugins. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`certProvider` |  _string_ |  `certProvider` defines the configuration for the certificate providers used to manage TLS certificates for webhook and plugins.  |  |   
`labels` |  _object (keys:string, values:string)_ |  `labels` field applies labels to all resources created for the `external-secrets` operand deployment.  |  |  The maximum number of properties is 20.  The minimum number of properties is 0.   
`annotations` |  _object (keys:string, values:string)_ |  `annotations` add custom annotations to all the resources created for the `external-secrets` deployment. The annotations are merged with any default annotations set by the Operator. User-specified annotations take precedence over defaults in case of conflicts. Annotation keys containing the reserved domains `kubernetes.io/`, `openshift.io/`, `k8s.io/`, or `cert-manager.io/` (including subdomains like `*.kubernetes.io/`) are not allowed.  |  |  The maximum number of annotations is 20.  The minimum number of annotations is 0.   
`networkPolicies` |  _networkPolicy array_ |  `networkPolicies` specifies the list of network policy configurations to be applied to the `external-secrets` pods. Each entry allows specifying a name for the generated `NetworkPolicy` object, along with its full Kubernetes `NetworkPolicy` definition. The Operator prepends `eso-user-` to the provided name when creating the Kubernetes object. If this field is not provided, `external-secrets` components are isolated with `deny-all` network policies, which prevents proper operation.  |  |  The maximum number of items is 50.  The minimum number of items is 0.   
`componentConfigs` |  _ComponentConfig array_ |  `componentConfigs` allows specifying deployment-level configuration overrides for individual `external-secrets` components. This field enables fine-grained control over deployment settings for each component independently. Each component can have only one configuration entry.  |  |  The maximum number of items is 4.  The minimum number of items is 0.   
`trustedCABundle` **ConfigMapKeyReference** |  _object_ |  `trustedCABundle` references a ConfigMap containing PEM-encoded CA certificates for the `external-secrets` core controller to trust when making outbound TLS connections. If specified, this bundle is used for all outbound TLS traffic, including connections to external secret management systems and configured proxies.  The ConfigMap must exist in the `external-secrets` Operand namespace and must not carry the CNO inject-trusted-cabundle label when proxy is configured. When omitted, external providers use standard system certificates. When proxy is configured, proxy TLS connections use the operator-managed OpenShift Container Platform trusted CA bundle injected by the Cluster Network Operator.  |  |   
Show more

## 13.9.12. controllerStatus

The `controllerStatus` field tracks the health and synchronization state of the individual controllers managed by the Operator. It identifies each controller by name, details its current operational conditions, and verifies that the controller is processing the latest configuration version. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`name` |  _string_ |  `name` specifies the name of the controller for which the observed condition is recorded.  |  |   
`conditions` |  _array_ |  `conditions` contains information about the current state of the External Secrets Operator controllers.  |  |   
`observedGeneration` |  _integer_ |  `observedGeneration` represents the `.metadata.generation` on the observed resource.  |  |  The minimum number of observed resources is 0.   
Show more

## 13.9.13. deploymentConfig

The `deploymentConfig` field defines configuration overrides for a Kubernetes Deployment resource. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`revisionHistoryLimit` |  _integer_ |  `revisionHistoryLimit` specifies the number of old `ReplicaSets` to retain for rollback purposes. This allows rolling back to previous deployment versions using the command `oc rollout undo`. Must be at least 1 to ensure rollback capability.  |  10  |  The maximum value is 50.  The minimum value is 1.   
Show more

## 13.9.14. externalSecretsConfig

The `externalSecretsConfig` object defines the configuration and information for the managed `external-secrets` operand deployment. Set the name to `cluster` as `externalSecretsConfig` object allows only one instance per cluster. 

Creating an `externalSecretsConfig` object triggers the deployment of the `external-secrets` operand and maintains the desired state. 

Field| Type| Description  
---|---|---  
`apiVersion` |  _string_ |  The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`.   
`kind` |  _string_ |  `kind` specifies the type of the object, which is `externalSecrets` for this object.   
`metadata` |  [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#objectmeta-v1-meta) |  Refer to Kubernetes API documentation for details about the `metadata` fields.   
`spec` |  _object_ |  `spec` contains the specifications of the desired behavior of the `externalSecrets` object.   
`status` |  _object_ |  `status` displays the most recently observed status of the `externalSecrets` object.   
Show more

## 13.9.15. externalSecretsConfigList

The `externalSecretsConfigList` object fetches the list of `externalSecretsConfig` objects. 

Field| Type| Description  
---|---|---  
`apiVersion` |  _string_ |  The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`  
`kind` |  _string_ |  `kind` specifies the type of the object, which is `externalSecretsList` for this API.   
`metadata` |  [_ListMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#listmeta-v1-meta) |  Refer to Kubernetes API documentation for details about the `metadata` fields.   
`items` |  _array_ |  `Items` contains a list of `externalSecrets` objects.   
Show more

## 13.9.16. externalSecretsConfigSpec

The `externalSecretsConfigSpec` field defines the desired behavior of the `externalSecrets` object. 

Field| Type| Description  
---|---|---  
`appConfig` |  _object_ |  `appConfig` configures the behavior of the `external-secrets` operand.   
`plugins` |  _object_ |  `plugins` configures the optional provider plugins.   
`controllerConfig` |  _object_ |  `controllerConfig` configures the controller to set up defaults that enable `external-secrets` operand.   
Show more

## 13.9.17. externalSecretsConfigStatus

The `externalSecretsConfigStatus` field shows the most recently observed status of the `externalSecretsConfig` Object. 

Field| Type| Description  
---|---|---  
`conditions` |  [_Condition_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#condition-v1-meta) _array_ |  `conditions` contains information about the current state of deployment.   
`externalSecretsImage` |  _string_ |  `externalSecretsImage` specifies the image name and tag used for deploy `external-secrets` operand.   
`bitwardenSDKServerImage` |  _string_ |  `bitwardenSDKServerImage` specifies the name of the image and tag used for deploying the `bitwarden-sdk-server`.   
Show more

## 13.9.18. externalSecretsManager

The `externalSecretsManager` object defines the configuration and information of deployments managed by the External Secrets Operator. 

Set the name to `cluster` as this allows only one instance of `externalSecretsManager` per cluster. You can configure global options by using `externalSecretsManager`. This serves as a centralized configuration for managing multiple controllers of the Operator. The Operator automatically creates the `externalSecretsManager` object during installation. 

Field| Type| Description  
---|---|---  
`apiVersion` |  _string_ |  The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`.   
`kind` |  _string_ |  `kind` specifies the type of the object, which is `externalSecretsManager` for this Object.   
`metadata` |  [_ObjectMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#objectmeta-v1-meta) |  Refer to Kubernetes API documentation for details about the `metadata` fields.   
`spec` |  _object_ |  `spec` contains specifications of the desired behavior.   
`status` |  _object_ |  `status` displays the most recently observed state of the controllers in the External Secrets Operator.   
Show more

## 13.9.19. externalSecretsManagerList

The `externalSecretsManagerList` object fetches the list of `externalSecretsManager` objects. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`apiVersion` |  _string_ |  The `apiVersion` specifies the version of the schema in use, which is `operator.openshift.io/v1alpha1`.  |  |   
`kind` |  _string_ |  `kind` specifies the type of the object, which is `externalSecretsManagerList` for this API.  |  |   
`metadata` |  [_ListMeta_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#listmeta-v1-meta) |  Refer to Kubernetes API documentation for details about the `metadata` fields.  |  |   
`items` |  _array_ |  |  |   
Show more

## 13.9.20. externalSecretsManagerSpec

The `externalSecretsManagerSpec` field defines the desired behavior of the `externalSecretsManager` object. 

Field| type| Description| Default| Validation  
---|---|---|---|---  
`globalConfig` |  _object_ |  `globalConfig` configures the behavior of deployments that External Secrets Operator manages.  |  |  Optional   
Show more

## 13.9.21. externalSecretsManagerStatus

The `externalSecretsManagerStatus` field shows the most recently observed status of the `externalSecretsManager` object. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`controllerStatuses` |  _array_ |  `controllerStatuses` holds the observed conditions of the controllers used by the Operator.  |  |   
`lastTransitionTime` |  [_Time_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.32/#time-v1-meta) |  `lastTransitionTime` records the most recent time the status of the condition changed.  |  |  Format: date-time  Type: string   
Show more

## 13.9.22. Feature

The `Feature` field configures an optional capability that is applied by the `external-secrets-operator` across its managed deployments. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`name` |  **FeatureName** _string_ |  `name` identifies the optional feature to configure. Currently, the only supported value is `UnsafeAllowGenericTargets`.  |  |  Enum: [`UnsafeAllowGenericTargets`]   
`mode` |  **mode** _string_ |  `mode` mode controls whether the feature is active. When set to `Enabled`, the Operator applies the configuration associated with the named feature to the relevant managed deployments. For `UnsafeAllowGenericTargets`, this passes the `--unsafe-allow-generic-targets` flag to the `external-secrets` core controller, allowing `ExternalSecret` resources to target Kubernetes resources other than `Secrets`. For example, ConfigMaps or custom resources.  Warning Generic targets require additional RBAC permissions on the affected operand; enabling this feature without the appropriate permissions will cause reconciliation failures.  |  Disabled  |  Enum:[`Enabled` `Disabled`]   
Show more

## 13.9.23. featureName

The `featureName` field identifies an optional feature that can be configured on the `ExternalSecretsManager` and applied by the `external-secrets-operator`. 

Field| Type| Description  
---|---|---  
`UnsafeAllowGenericTargets` |  _object_ |  `UnsafeAllowGenericTargets` configures the `external-secrets` core controller to run with the `--unsafe-allow-generic-targets` startup flag, which allows `ExternalSecret` resources to sync data into Kubernetes resources other than `Secrets`.   
Show more

## 13.9.24. globalConfig

The `globalConfig` field defines the baseline behavior and deployment parameters for the External Secrets Operator for Red Hat OpenShift. 

Use this section to apply labels to all managed resources and configure the logging verbosity. It also provides infrastructure-level controls to govern where and how the Operator is scheduled, alongside proxy settings for network compatibility. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`logLevel` |  _integer_ |  `logLevel` supports a range of values as defined in the [kubernetes logging guidelines](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-instrumentation/logging.md#what-method-to-use).  |  1  |  The maximum range value is 5  The minimum range value is 1   
`resources` |  [_ResourceRequirements_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#resourcerequirements-v1-core) |  `resources` defines the resource requirements. You cannot change the value of this field after setting it initially. For more information, see <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |  |   
`affinity` |  [_Affinity_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#affinity-v1-core) |  `affinity` sets the scheduling affinity rules. For more information, see <https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/> |  |   
`tolerations` |  [_Toleration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#toleration-v1-core) _array_ |  `tolerations` sets the pod tolerations. For more information, see <https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/> |  |  The maximum number of items is 50  The minimum number of items is 0   
`nodeSelector` |  _object (keys:string, values:string)_ |  `nodeSelector` defines the scheduling criteria by using the node labels. For more information, see <https://kubernetes.io/docs/concepts/configuration/assign-pod-node/> |  |  The maximum number of properties is 50  The minimum number of properties is 0   
`proxy` |  _object_ |  `proxy` sets the proxy configurations available in the operand containers managed by the Operator as environment variables.  |  |   
`labels` |  _object (keys:string, values:string)_ |  `labels` applies to all resources created by the Operator. This field can have a maximum of 20 entries  |  |  The maximum number of properties is 20  The minimum number of properties is 0   
Show more

## 13.9.25. managementState

The `managementState` field controls whether the Operator manages the resource lifecycle. 

Field| Type| Description  
---|---|---  
`Managed` |  _string_ |  `ManagementStateManaged` indicates the Operator is responsible for the resource lifecycle.   
`Unmanaged` |  _string_ |  `ManagementStateUnmanaged` indicates the user is responsible for the resource lifecycle.   
Show more

## 13.9.26. mode

The `mode` field indicates the operational state of the optional features. 

Field| Type| Description  
---|---|---  
`Enabled` |  _string_ |  `Enabled` indicates the optional configuration is enabled.   
`Disabled` |  _string_ |  `Disabled` indicates the optional configuration is disabled.   
Show more

## 13.9.27. networkPolicy

The `networkPolicy` field represents a custom network policy configuration for operator-managed components. The field includes a name for identification and the network policy rules to be enforced. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`name` |  _string_ |  `name` is the logical identifier for this network policy entry. The Operator prepends `eso-user-` to this value when creating the Kubernetes `NetworkPolicy` object, for example `allow-egress` becomes `eso-user-allow-egress`. The maximum length is 243 to accommodate the prefix within the 253-character Kubernetes name limit.  |  |  The maximum length is 243 characters.  The minimum length is 1. character.   
`componentName` |  _string_ |  `componentName` specifies which external-secrets component this network policy applies to.  |  |  Enum:[`ExternalSecretsCoreController` `BitwardenSDIServer`]   
`egress` **NetworkPolicyegressRule** |  _array_ |  `egress` is a list of egress rules to be applied to the selected pods. Outgoing traffic is allowed if there are no `NetworkPolicies` selecting the pod, and cluster policy otherwise allows the traffic, or if the traffic matches at least one egress rule across all the `NetworkPolicy` objects whose `podSelector` matches the pod. If this field is empty, then this `NetworkPolicy` limits all outgoing traffic and serves solely to ensure that the pods it selects are isolated by default. The Operator automatically handles ingress rules based on the current running ports.  |  |   
Show more

## 13.9.28. objectReference

The `ObjectReference` object acts as a pointer to a specific Kubernetes resource. It uniquely identifies the target by requiring its name, and optionally, helps scope the reference to a specific resource type and API group. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`name` |  _string_ |  `name` specifies the name of the resource being referred to.  |  |  The maximum length is 253 characters.  The minimum length is 1 character.  Required   
`kind` |  _string_ |  `kind` specifies the kind of the resource being referred to.  |  |  The maximum length is 253 characters.  The minimum length is 1 character.  Optional   
`group` |  _string_ |  `group` specifies the group of the resource being referred to.  |  |  The maximum length is 253 characters.  The minimum length is 1 character.  Optional   
Show more

## 13.9.29. pluginsConfig

The `pluginsConfig` configures the optional plugins. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`bitwardenSecretManagerProvider` |  _object_ |  `bitwardenSecretManagerProvider` enables the `bitwarden-secrets-manager` provider plugin for connecting with the 'bitwarden-secrets-manager'.  |  |  Optional   
Show more

## 13.9.30. proxyConfig

The `proxyConfig` object defines the network proxy settings that the Operator injects into managed containers as environment variables. Use this configuration to ensure proper connectivity in restricted network environments, or to bypass the proxy and connect directly. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`httpProxy` |  _string_ |  The `httpProxy` field contains the URL of the proxy for HTTP requests. This field can have a maximum of 2048 characters.  |  |  The maximum length is 2048 characters.  The minimum length is 0 characters.   
`httpsProxy` |  _string_ |  The `httpsProxy` field contains the URL of the proxy for HTTPS requests. This field can have a maximum of 2048 characters.  |  |  The maximum length is 2048 characters.  The minimum length is 0 characters.   
`noProxy` |  _string_ |  The `noProxy` field is a comma-separated list of hostnames, classless inter-domain routings (CIDRs), and IP addresses or a combination of the three for which the proxy should not be used. This field can have a maximum of 4096 characters.  |  |  The maximum length is 4096 characters.  The minimum length is 0 characters.   
`networkPolicyProvisioning` **ManagementState** |  _string_ |  The `networkPolicyProvisioning` field defines the management strategy for the proxy egress rule. When set to `Managed`, the Operator automatically provisions and maintains a `NetworkPolicy` allowing traffic to the configured proxy. If no proxy is configured, a `NetworkPolicy` is not created regardless of this setting.  |  Managed  |  Enum:[`Managed` `Unmanaged`]   
Show more

## 13.9.31. secretReference

The `secretReference` field refers to a secret with the given name in the same namespace where it used. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`name` |  _string_ |  `name` specifies the name of the secret resource being referred to.  |  |  The maximum length is 253.  The minimum length is 1.   
Show more

## 13.9.32. webhookConfig

The `webhookConfig` field configures the specifics of the `external-secrets` application webhook. 

Field| Type| Description| Default| Validation  
---|---|---|---|---  
`certificateCheckInterval` |  [_Duration_](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.31/#duration-v1-meta) |  `certificateCheckInterval` configures the polling interval to check certificate validity.  |  5m  |  Optional   
Show more
