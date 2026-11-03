# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec defines the specification of the desired behavior of the Alertmanager cluster. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>  
`status` |  `object` |  status defines the most recent observed status of the Alertmanager cluster. Read-only. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>  
Show more

## 2.1.1. .spec

Description
     spec defines the specification of the desired behavior of the Alertmanager cluster. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>
Type
     `object`

Property| Type| Description  
---|---|---  
`additionalArgs` |  `array` |  additionalArgs allows setting additional arguments for the 'Alertmanager' container. It is intended for e.g. activating hidden flags which are not supported by the dedicated configuration options yet. The arguments are passed as-is to the Alertmanager container which may cause issues if they are invalid or not supported by the given Alertmanager version.   
`additionalArgs[]` |  `object` |  Argument as part of the AdditionalArgs list.   
`additionalPeers` |  `array (string)` |  additionalPeers allows injecting a set of additional Alertmanagers to peer with to form a highly available cluster.   
`affinity` |  `object` |  affinity defines the pod’s scheduling constraints.   
`alertmanagerConfigMatcherStrategy` |  `object` |  alertmanagerConfigMatcherStrategy defines how AlertmanagerConfig objects process incoming alerts.   
`alertmanagerConfigNamespaceSelector` |  `object` |  alertmanagerConfigNamespaceSelector defines the namespaces to be selected for AlertmanagerConfig discovery. If nil, only check own namespace.   
`alertmanagerConfigSelector` |  `object` |  alertmanagerConfigSelector defines the selector to be used for to merge and configure Alertmanager with.   
`alertmanagerConfiguration` |  `object` |  alertmanagerConfiguration defines the configuration of Alertmanager.  If defined, it takes precedence over the `configSecret` field.  This is an **experimental feature** , it may change in any upcoming release in a breaking way.   
`automountServiceAccountToken` |  `boolean` |  automountServiceAccountToken defines whether a service account token should be automatically mounted in the pod. If the service account has `automountServiceAccountToken: true`, set the field to `false` to opt out of automounting API credentials.   
`baseImage` |  `string` |  baseImage that is used to deploy pods, without tag. Deprecated: use 'image' instead.   
`clusterAdvertiseAddress` |  `string` |  clusterAdvertiseAddress defines the explicit address to advertise in cluster. Needs to be provided for non RFC1918 [1] (public) addresses. [1] RFC1918: <https://tools.ietf.org/html/rfc1918>  
`clusterGossipInterval` |  `string` |  clusterGossipInterval defines the interval between gossip attempts.   
`clusterLabel` |  `string` |  clusterLabel defines the identifier that uniquely identifies the Alertmanager cluster. You should only set it when the Alertmanager cluster includes Alertmanager instances which are external to this Alertmanager resource. In practice, the addresses of the external instances are provided via the `.spec.additionalPeers` field.   
`clusterPeerTimeout` |  `string` |  clusterPeerTimeout defines the timeout for cluster peering.   
`clusterPushpullInterval` |  `string` |  clusterPushpullInterval defines the interval between pushpull attempts.   
`clusterTLS` |  `object` |  clusterTLS defines the mutual TLS configuration for the Alertmanager cluster’s gossip protocol.  It requires Alertmanager >= 0.24.0.   
`configMaps` |  `array (string)` |  configMaps defines a list of ConfigMaps in the same namespace as the Alertmanager object, which shall be mounted into the Alertmanager Pods. Each ConfigMap is added to the StatefulSet definition as a volume named `configmap-<configmap-name>`. The ConfigMaps are mounted into `/etc/alertmanager/configmaps/<configmap-name>` in the 'alertmanager' container.   
`configSecret` |  `string` |  configSecret defines the name of a Kubernetes Secret in the same namespace as the Alertmanager object, which contains the configuration for this Alertmanager instance. If empty, it defaults to `alertmanager-<alertmanager-name>`.  The Alertmanager configuration should be available under the `alertmanager.yaml` key. Additional keys from the original secret are copied to the generated secret and mounted into the `/etc/alertmanager/config` directory in the `alertmanager` container.  If either the secret or the `alertmanager.yaml` key is missing, the operator provisions a minimal Alertmanager configuration with one empty receiver (effectively dropping alert notifications).   
`containers` |  `array` |  containers allows injecting additional containers or modifying operator generated containers. This can be used to allow adding an authentication proxy to the Pods or to change the behavior of an operator generated container. Containers described here modify an operator generated container if they share the same name and modifications are done via a strategic merge patch.  The names of containers managed by the operator are: * `alertmanager` * `config-reloader` * `thanos-sidecar` Overriding containers which are managed by the operator require careful testing, especially when upgrading to a new version of the operator.   
`containers[]` |  `object` |  A single application container that you want to run within a pod.   
`dnsConfig` |  `object` |  dnsConfig defines the DNS configuration for the pods.   
`dnsPolicy` |  `string` |  dnsPolicy defines the DNS policy for the pods.   
`enableFeatures` |  `array (string)` |  enableFeatures defines the Alertmanager’s feature flags. By default, no features are enabled. Enabling features which are disabled by default is entirely outside the scope of what the maintainers will support and by doing so, you accept that this behaviour may break at any time without notice.  It requires Alertmanager >= 0.27.0.   
`enableServiceLinks` |  `boolean` |  enableServiceLinks defines whether information about services should be injected into pod’s environment variables   
`externalUrl` |  `string` |  externalUrl defines the URL used to access the Alertmanager web service. This is necessary to generate correct URLs. This is necessary if Alertmanager is not served from root of a DNS name.   
`forceEnableClusterMode` |  `boolean` |  forceEnableClusterMode ensures Alertmanager does not deactivate the cluster mode when running with a single replica. Use case is e.g. spanning an Alertmanager cluster across Kubernetes clusters with a single replica in each.   
`hostAliases` |  `array` |  hostAliases Pods configuration   
`hostAliases[]` |  `object` |  HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod’s hosts file.   
`hostNetwork` |  `boolean` |  hostNetwork controls whether the pod may use the node network namespace.  Make sure to understand the security implications if you want to enable it (<https://kubernetes.io/docs/concepts/configuration/overview/>).  When hostNetwork is enabled, this will set the DNS policy to `ClusterFirstWithHostNet` automatically (unless `.spec.dnsPolicy` is set to a different value).   
`hostUsers` |  `boolean` |  hostUsers supports the user space in Kubernetes.  More info: <https://kubernetes.io/docs/tasks/configure-pod-container/user-namespaces/> The feature requires at least Kubernetes 1.28 with the `UserNamespacesSupport` feature gate enabled. Starting Kubernetes 1.33, the feature is enabled by default.   
`image` |  `string` |  image if specified has precedence over baseImage, tag and sha combinations. Specifying the version is still necessary to ensure the Prometheus Operator knows what version of Alertmanager is being configured.   
`imagePullPolicy` |  `string` |  imagePullPolicy for the 'alertmanager', 'init-config-reloader' and 'config-reloader' containers. See <https://kubernetes.io/docs/concepts/containers/images/#image-pull-policy> for more details.   
`imagePullSecrets` |  `array` |  imagePullSecrets An optional list of references to secrets in the same namespace to use for pulling prometheus and alertmanager images from registries see <https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/>  
`imagePullSecrets[]` |  `object` |  LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.   
`initContainers` |  `array` |  initContainers allows injecting initContainers to the Pod definition. Those can be used to e.g. fetch secrets for injection into the Prometheus configuration from external sources. Any errors during the execution of an initContainer will lead to a restart of the Pod. More info: <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/> InitContainers described here modify an operator generated init containers if they share the same name and modifications are done via a strategic merge patch.  The names of init container name managed by the operator are: * `init-config-reloader`.  Overriding init containers which are managed by the operator require careful testing, especially when upgrading to a new version of the operator.   
`initContainers[]` |  `object` |  A single application container that you want to run within a pod.   
`limits` |  `object` |  limits defines the limits command line flags when starting Alertmanager.   
`listenLocal` |  `boolean` |  listenLocal defines the Alertmanager server listen on loopback, so that it does not bind against the Pod IP. Note this is only for the Alertmanager UI, not the gossip communication.   
`logFormat` |  `string` |  logFormat for Alertmanager to be configured with.   
`logLevel` |  `string` |  logLevel for Alertmanager to be configured with.   
`minReadySeconds` |  `integer` |  minReadySeconds defines the minimum number of seconds for which a newly created pod should be ready without any of its container crashing for it to be considered available.  If unset, pods will be considered available as soon as they are ready.  When the Alertmanager version is greater than or equal to v0.30.0, the duration is also used to delay the first flush of the aggregation groups. This delay helps ensuring that all alerts have been resent by the Prometheus instances to Alertmanager after a roll-out. It is possible to override this behavior passing a custom value via `.spec.additionalArgs`.   
`nodeSelector` |  `object (string)` |  nodeSelector defines which Nodes the Pods are scheduled on.   
`paused` |  `boolean` |  paused if set to true all actions on the underlying managed objects are not going to be performed, except for delete actions.   
`persistentVolumeClaimRetentionPolicy` |  `object` |  persistentVolumeClaimRetentionPolicy controls if and how PVCs are deleted during the lifecycle of a StatefulSet. The default behavior is all PVCs are retained. This is an alpha field from kubernetes 1.23 until 1.26 and a beta field from 1.26. It requires enabling the StatefulSetAutoDeletePVC feature gate.   
`podManagementPolicy` |  `string` |  podManagementPolicy defines the policy for creating/deleting pods when scaling up and down.  Unlike the default StatefulSet behavior, the default policy is `Parallel` to avoid manual intervention in case a pod gets stuck during a rollout.  Note that updating this value implies the recreation of the StatefulSet which incurs a service outage.   
`podMetadata` |  `object` |  podMetadata defines labels and annotations which are propagated to the Alertmanager pods.  The following items are reserved and cannot be overridden: * "alertmanager" label, set to the name of the Alertmanager instance. * "app.kubernetes.io/instance" label, set to the name of the Alertmanager instance. * "app.kubernetes.io/managed-by" label, set to "prometheus-operator". * "app.kubernetes.io/name" label, set to "alertmanager". * "app.kubernetes.io/version" label, set to the Alertmanager version. * "kubectl.kubernetes.io/default-container" annotation, set to "alertmanager".   
`portName` |  `string` |  portName defines the port’s name for the pods and governing service. Defaults to `web`.   
`priorityClassName` |  `string` |  priorityClassName assigned to the Pods   
`replicas` |  `integer` |  replicas defines the expected size of the alertmanager cluster. The controller will eventually make the size of the running cluster equal to the expected size.   
`resources` |  `object` |  resources defines the resource requests and limits of the Pods.   
`retention` |  `string` |  retention defines the time duration Alertmanager shall retain data for. Default is '120h', and must match the regular expression `[0-9]+(ms|s|m|h)` (milliseconds seconds minutes hours).   
`routePrefix` |  `string` |  routePrefix Alertmanager registers HTTP handlers for. This is useful, if using ExternalURL and a proxy is rewriting HTTP routes of a request, and the actual ExternalURL is still true, but the server serves requests under a different route prefix. For example for use with `kubectl proxy`.   
`schedulerName` |  `string` |  schedulerName defines the scheduler to use for Pod scheduling. If not specified, the default scheduler is used.   
`secrets` |  `array (string)` |  secrets is a list of Secrets in the same namespace as the Alertmanager object, which shall be mounted into the Alertmanager Pods. Each Secret is added to the StatefulSet definition as a volume named `secret-<secret-name>`. The Secrets are mounted into `/etc/alertmanager/secrets/<secret-name>` in the 'alertmanager' container.   
`securityContext` |  `object` |  securityContext holds pod-level security attributes and common container settings. This defaults to the default PodSecurityContext.   
`serviceAccountName` |  `string` |  serviceAccountName is the name of the ServiceAccount to use to run the Prometheus Pods.   
`serviceName` |  `string` |  serviceName defines the service name used by the underlying StatefulSet(s) as the governing service. If defined, the Service must be created before the Alertmanager resource in the same namespace and it must define a selector that matches the pod labels. If empty, the operator will create and manage a headless service named `alertmanager-operated` for Alertmanager resources. When deploying multiple Alertmanager resources in the same namespace, it is recommended to specify a different value for each. See <https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#stable-network-id> for more details.   
`sha` |  `string` |  sha of Alertmanager container image to be deployed. Defaults to the value of `version`. Similar to a tag, but the SHA explicitly deploys an immutable container image. Version and Tag are ignored if SHA is set. Deprecated: use 'image' instead. The image digest can be specified as part of the image URL.   
`storage` |  `object` |  storage defines the definition of how storage will be used by the Alertmanager instances.   
`tag` |  `string` |  tag of Alertmanager container image to be deployed. Defaults to the value of `version`. Version is ignored if Tag is set. Deprecated: use 'image' instead. The image tag can be specified as part of the image URL.   
`terminationGracePeriodSeconds` |  `integer` |  terminationGracePeriodSeconds defines the Optional duration in seconds the pod needs to terminate gracefully. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down) which may lead to data corruption.  Defaults to 120 seconds.   
`tolerations` |  `array` |  tolerations defines the pod’s tolerations.   
`tolerations[]` |  `object` |  The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>.   
`topologySpreadConstraints` |  `array` |  topologySpreadConstraints defines the Pod’s topology spread constraints.   
`topologySpreadConstraints[]` |  `object` |  TopologySpreadConstraint specifies how to spread matching pods among the given topology.   
`updateStrategy` |  `object` |  updateStrategy indicates the strategy that will be employed to update Pods in the StatefulSet when a revision is made to statefulset’s Pod Template.  The default strategy is RollingUpdate.   
`version` |  `string` |  version the cluster should be on.   
`volumeMounts` |  `array` |  volumeMounts allows configuration of additional VolumeMounts on the output StatefulSet definition. VolumeMounts specified will be appended to other VolumeMounts in the alertmanager container, that are generated as a result of StorageSpec objects.   
`volumeMounts[]` |  `object` |  VolumeMount describes a mounting of a Volume within a container.   
`volumes` |  `array` |  volumes allows configuration of additional volumes on the output StatefulSet definition. Volumes specified will be appended to other volumes that are generated as a result of StorageSpec objects.   
`volumes[]` |  `object` |  Volume represents a named volume in a pod that may be accessed by any container in the pod.   
`web` |  `object` |  web defines the web command line flags when starting Alertmanager.   
Show more

## 2.1.2. .spec.additionalArgs

Description
     additionalArgs allows setting additional arguments for the 'Alertmanager' container. It is intended for e.g. activating hidden flags which are not supported by the dedicated configuration options yet. The arguments are passed as-is to the Alertmanager container which may cause issues if they are invalid or not supported by the given Alertmanager version. 
Type
     `array`

## 2.1.3. .spec.additionalArgs[]

Description
     Argument as part of the AdditionalArgs list. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name of the argument, e.g. "scrape.discovery-reload-interval".   
`value` |  `string` |  value defines the argument value, e.g. 30s. Can be empty for name-only arguments (e.g. --storage.tsdb.no-lockfile)   
Show more

## 2.1.4. .spec.affinity

Description
     affinity defines the pod’s scheduling constraints. 
Type
     `object`

Property| Type| Description  
---|---|---  
`nodeAffinity` |  `object` |  Describes node affinity scheduling rules for the pod.   
`podAffinity` |  `object` |  Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)).   
`podAntiAffinity` |  `object` |  Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)).   
Show more

## 2.1.5. .spec.affinity.nodeAffinity

Description
     Describes node affinity scheduling rules for the pod. 
Type
     `object`

Property| Type| Description  
---|---|---  
`preferredDuringSchedulingIgnoredDuringExecution` |  `array` |  The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred.   
`preferredDuringSchedulingIgnoredDuringExecution[]` |  `object` |  An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it’s a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op).   
`requiredDuringSchedulingIgnoredDuringExecution` |  `object` |  If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node.   
Show more

## 2.1.6. .spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution

Description
     The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node matches the corresponding matchExpressions; the node(s) with the highest sum are the most preferred. 
Type
     `array`

## 2.1.7. .spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[]

Description
     An empty preferred scheduling term matches all objects with implicit weight 0 (i.e. it’s a no-op). A null preferred scheduling term matches no objects (i.e. is also a no-op). 
Type
     `object`
Required
    

  * `preference`
  * `weight`



Property| Type| Description  
---|---|---  
`preference` |  `object` |  A node selector term, associated with the corresponding weight.   
`weight` |  `integer` |  Weight associated with matching the corresponding nodeSelectorTerm, in the range 1-100.   
Show more

## 2.1.8. .spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[].preference

Description
     A node selector term, associated with the corresponding weight. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  A list of node selector requirements by node’s labels.   
`matchExpressions[]` |  `object` |  A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchFields` |  `array` |  A list of node selector requirements by node’s fields.   
`matchFields[]` |  `object` |  A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
Show more

## 2.1.9. .spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[].preference.matchExpressions

Description
     A list of node selector requirements by node’s labels. 
Type
     `array`

## 2.1.10. .spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[].preference.matchExpressions[]

Description
     A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The label key that the selector applies to.   
`operator` |  `string` |  Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.   
`values` |  `array (string)` |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.   
Show more

## 2.1.11. .spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[].preference.matchFields

Description
     A list of node selector requirements by node’s fields. 
Type
     `array`

## 2.1.12. .spec.affinity.nodeAffinity.preferredDuringSchedulingIgnoredDuringExecution[].preference.matchFields[]

Description
     A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The label key that the selector applies to.   
`operator` |  `string` |  Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.   
`values` |  `array (string)` |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.   
Show more

## 2.1.13. .spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution

Description
     If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to an update), the system may or may not try to eventually evict the pod from its node. 
Type
     `object`
Required
    

  * `nodeSelectorTerms`



Property| Type| Description  
---|---|---  
`nodeSelectorTerms` |  `array` |  Required. A list of node selector terms. The terms are ORed.   
`nodeSelectorTerms[]` |  `object` |  A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm.   
Show more

## 2.1.14. .spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms

Description
     Required. A list of node selector terms. The terms are ORed. 
Type
     `array`

## 2.1.15. .spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[]

Description
     A null or empty node selector term matches no objects. The requirements of them are ANDed. The TopologySelectorTerm type implements a subset of the NodeSelectorTerm. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  A list of node selector requirements by node’s labels.   
`matchExpressions[]` |  `object` |  A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchFields` |  `array` |  A list of node selector requirements by node’s fields.   
`matchFields[]` |  `object` |  A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
Show more

## 2.1.16. .spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[].matchExpressions

Description
     A list of node selector requirements by node’s labels. 
Type
     `array`

## 2.1.17. .spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[].matchExpressions[]

Description
     A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The label key that the selector applies to.   
`operator` |  `string` |  Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.   
`values` |  `array (string)` |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.   
Show more

## 2.1.18. .spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[].matchFields

Description
     A list of node selector requirements by node’s fields. 
Type
     `array`

## 2.1.19. .spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms[].matchFields[]

Description
     A node selector requirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The label key that the selector applies to.   
`operator` |  `string` |  Represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.   
`values` |  `array (string)` |  An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.   
Show more

## 2.1.20. .spec.affinity.podAffinity

Description
     Describes pod affinity scheduling rules (e.g. co-locate this pod in the same node, zone, etc. as some other pod(s)). 
Type
     `object`

Property| Type| Description  
---|---|---  
`preferredDuringSchedulingIgnoredDuringExecution` |  `array` |  The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.   
`preferredDuringSchedulingIgnoredDuringExecution[]` |  `object` |  The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)   
`requiredDuringSchedulingIgnoredDuringExecution` |  `array` |  If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.   
`requiredDuringSchedulingIgnoredDuringExecution[]` |  `object` |  Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running   
Show more

## 2.1.21. .spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution

Description
     The scheduler will prefer to schedule pods to nodes that satisfy the affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling affinity expressions, etc.), compute a sum by iterating through the elements of this field and adding "weight" to the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. 
Type
     `array`

## 2.1.22. .spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution[]

Description
     The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s) 
Type
     `object`
Required
    

  * `podAffinityTerm`
  * `weight`



Property| Type| Description  
---|---|---  
`podAffinityTerm` |  `object` |  Required. A pod affinity term, associated with the corresponding weight.   
`weight` |  `integer` |  weight associated with matching the corresponding podAffinityTerm, in the range 1-100.   
Show more

## 2.1.23. .spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm

Description
     Required. A pod affinity term, associated with the corresponding weight. 
Type
     `object`
Required
    

  * `topologyKey`



Property| Type| Description  
---|---|---  
`labelSelector` |  `object` |  A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods.   
`matchLabelKeys` |  `array (string)` |  MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set.   
`mismatchLabelKeys` |  `array (string)` |  MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set.   
`namespaceSelector` |  `object` |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces.   
`namespaces` |  `array (string)` |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace".   
`topologyKey` |  `string` |  This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
Show more

## 2.1.24. .spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.labelSelector

Description
     A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.25. .spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.labelSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.26. .spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.labelSelector.matchExpressions[]

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

## 2.1.27. .spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.namespaceSelector

Description
     A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.28. .spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.namespaceSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.29. .spec.affinity.podAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.namespaceSelector.matchExpressions[]

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

## 2.1.30. .spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution

Description
     If the affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. 
Type
     `array`

## 2.1.31. .spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution[]

Description
     Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running 
Type
     `object`
Required
    

  * `topologyKey`



Property| Type| Description  
---|---|---  
`labelSelector` |  `object` |  A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods.   
`matchLabelKeys` |  `array (string)` |  MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set.   
`mismatchLabelKeys` |  `array (string)` |  MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set.   
`namespaceSelector` |  `object` |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces.   
`namespaces` |  `array (string)` |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace".   
`topologyKey` |  `string` |  This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
Show more

## 2.1.32. .spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution[].labelSelector

Description
     A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.33. .spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution[].labelSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.34. .spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution[].labelSelector.matchExpressions[]

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

## 2.1.35. .spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution[].namespaceSelector

Description
     A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.36. .spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution[].namespaceSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.37. .spec.affinity.podAffinity.requiredDuringSchedulingIgnoredDuringExecution[].namespaceSelector.matchExpressions[]

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

## 2.1.38. .spec.affinity.podAntiAffinity

Description
     Describes pod anti-affinity scheduling rules (e.g. avoid putting this pod in the same node, zone, etc. as some other pod(s)). 
Type
     `object`

Property| Type| Description  
---|---|---  
`preferredDuringSchedulingIgnoredDuringExecution` |  `array` |  The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and subtracting "weight" from the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred.   
`preferredDuringSchedulingIgnoredDuringExecution[]` |  `object` |  The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s)   
`requiredDuringSchedulingIgnoredDuringExecution` |  `array` |  If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied.   
`requiredDuringSchedulingIgnoredDuringExecution[]` |  `object` |  Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running   
Show more

## 2.1.39. .spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution

Description
     The scheduler will prefer to schedule pods to nodes that satisfy the anti-affinity expressions specified by this field, but it may choose a node that violates one or more of the expressions. The node that is most preferred is the one with the greatest sum of weights, i.e. for each node that meets all of the scheduling requirements (resource request, requiredDuringScheduling anti-affinity expressions, etc.), compute a sum by iterating through the elements of this field and subtracting "weight" from the sum if the node has pods which matches the corresponding podAffinityTerm; the node(s) with the highest sum are the most preferred. 
Type
     `array`

## 2.1.40. .spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution[]

Description
     The weights of all of the matched WeightedPodAffinityTerm fields are added per-node to find the most preferred node(s) 
Type
     `object`
Required
    

  * `podAffinityTerm`
  * `weight`



Property| Type| Description  
---|---|---  
`podAffinityTerm` |  `object` |  Required. A pod affinity term, associated with the corresponding weight.   
`weight` |  `integer` |  weight associated with matching the corresponding podAffinityTerm, in the range 1-100.   
Show more

## 2.1.41. .spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm

Description
     Required. A pod affinity term, associated with the corresponding weight. 
Type
     `object`
Required
    

  * `topologyKey`



Property| Type| Description  
---|---|---  
`labelSelector` |  `object` |  A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods.   
`matchLabelKeys` |  `array (string)` |  MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set.   
`mismatchLabelKeys` |  `array (string)` |  MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set.   
`namespaceSelector` |  `object` |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces.   
`namespaces` |  `array (string)` |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace".   
`topologyKey` |  `string` |  This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
Show more

## 2.1.42. .spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.labelSelector

Description
     A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.43. .spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.labelSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.44. .spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.labelSelector.matchExpressions[]

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

## 2.1.45. .spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.namespaceSelector

Description
     A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.46. .spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.namespaceSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.47. .spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution[].podAffinityTerm.namespaceSelector.matchExpressions[]

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

## 2.1.48. .spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution

Description
     If the anti-affinity requirements specified by this field are not met at scheduling time, the pod will not be scheduled onto the node. If the anti-affinity requirements specified by this field cease to be met at some point during pod execution (e.g. due to a pod label update), the system may or may not try to eventually evict the pod from its node. When there are multiple elements, the lists of nodes corresponding to each podAffinityTerm are intersected, i.e. all terms must be satisfied. 
Type
     `array`

## 2.1.49. .spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[]

Description
     Defines a set of pods (namely those matching the labelSelector relative to the given namespace(s)) that this pod should be co-located (affinity) or not co-located (anti-affinity) with, where co-located is defined as running on a node whose value of the label with key <topologyKey> matches that of any node on which a pod of the set of pods is running 
Type
     `object`
Required
    

  * `topologyKey`



Property| Type| Description  
---|---|---  
`labelSelector` |  `object` |  A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods.   
`matchLabelKeys` |  `array (string)` |  MatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key in (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both matchLabelKeys and labelSelector. Also, matchLabelKeys cannot be set when labelSelector isn’t set.   
`mismatchLabelKeys` |  `array (string)` |  MismatchLabelKeys is a set of pod label keys to select which pods will be taken into consideration. The keys are used to lookup values from the incoming pod labels, those key-value labels are merged with `labelSelector` as `key notin (value)` to select the group of existing pods which pods will be taken into consideration for the incoming pod’s pod (anti) affinity. Keys that don’t exist in the incoming pod labels will be ignored. The default value is empty. The same key is forbidden to exist in both mismatchLabelKeys and labelSelector. Also, mismatchLabelKeys cannot be set when labelSelector isn’t set.   
`namespaceSelector` |  `object` |  A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces.   
`namespaces` |  `array (string)` |  namespaces specifies a static list of namespace names that the term applies to. The term is applied to the union of the namespaces listed in this field and the ones selected by namespaceSelector. null or empty namespaces list and null namespaceSelector means "this pod’s namespace".   
`topologyKey` |  `string` |  This pod should be co-located (affinity) or not co-located (anti-affinity) with the pods matching the labelSelector in the specified namespaces, where co-located is defined as running on a node whose value of the label with key topologyKey matches that of any node on which any of the selected pods is running. Empty topologyKey is not allowed.   
Show more

## 2.1.50. .spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[].labelSelector

Description
     A label query over a set of resources, in this case pods. If it’s null, this PodAffinityTerm matches with no Pods. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.51. .spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[].labelSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.52. .spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[].labelSelector.matchExpressions[]

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

## 2.1.53. .spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[].namespaceSelector

Description
     A label query over the set of namespaces that the term applies to. The term is applied to the union of the namespaces selected by this field and the ones listed in the namespaces field. null selector and null or empty namespaces list means "this pod’s namespace". An empty selector ({}) matches all namespaces. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.54. .spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[].namespaceSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.55. .spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution[].namespaceSelector.matchExpressions[]

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

## 2.1.56. .spec.alertmanagerConfigMatcherStrategy

Description
     alertmanagerConfigMatcherStrategy defines how AlertmanagerConfig objects process incoming alerts. 
Type
     `object`

Property| Type| Description  
---|---|---  
`type` |  `string` |  type defines the strategy used by AlertmanagerConfig objects to match alerts in the routes and inhibition rules.  The default value is `OnNamespace`.   
Show more

## 2.1.57. .spec.alertmanagerConfigNamespaceSelector

Description
     alertmanagerConfigNamespaceSelector defines the namespaces to be selected for AlertmanagerConfig discovery. If nil, only check own namespace. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.58. .spec.alertmanagerConfigNamespaceSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.59. .spec.alertmanagerConfigNamespaceSelector.matchExpressions[]

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

## 2.1.60. .spec.alertmanagerConfigSelector

Description
     alertmanagerConfigSelector defines the selector to be used for to merge and configure Alertmanager with. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.61. .spec.alertmanagerConfigSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.62. .spec.alertmanagerConfigSelector.matchExpressions[]

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

## 2.1.63. .spec.alertmanagerConfiguration

Description
    

alertmanagerConfiguration defines the configuration of Alertmanager. 

If defined, it takes precedence over the `configSecret` field. 

This is an **experimental feature** , it may change in any upcoming release in a breaking way. 

Type
     `object`

Property| Type| Description  
---|---|---  
`global` |  `object` |  global defines the global parameters of the Alertmanager configuration.   
`name` |  `string` |  name defines the name of the AlertmanagerConfig custom resource which is used to generate the Alertmanager configuration. It must be defined in the same namespace as the Alertmanager object. The operator will not enforce a `namespace` label for routes and inhibition rules.   
`templates` |  `array` |  templates defines the custom notification templates.   
`templates[]` |  `object` |  SecretOrConfigMap allows to specify data as a Secret or ConfigMap. Fields are mutually exclusive.   
Show more

## 2.1.64. .spec.alertmanagerConfiguration.global

Description
     global defines the global parameters of the Alertmanager configuration. 
Type
     `object`

Property| Type| Description  
---|---|---  
`httpConfig` |  `object` |  httpConfig defines the default HTTP configuration.   
`jira` |  `object` |  jira defines the default configuration for Jira.   
`opsGenieApiKey` |  `object` |  opsGenieApiKey defines the default OpsGenie API Key.   
`opsGenieApiUrl` |  `object` |  opsGenieApiUrl defines the default OpsGenie API URL.   
`pagerdutyUrl` |  `string` |  pagerdutyUrl defines the default Pagerduty URL.   
`resolveTimeout` |  `string` |  resolveTimeout defines the default value used by alertmanager if the alert does not include EndsAt, after this time passes it can declare the alert as resolved if it has not been updated. This has no impact on alerts from Prometheus, as they always include EndsAt.   
`rocketChat` |  `object` |  rocketChat defines the default configuration for Rocket Chat.   
`slackApiUrl` |  `object` |  slackApiUrl defines the default Slack API URL.   
`smtp` |  `object` |  smtp defines global SMTP parameters.   
`telegram` |  `object` |  telegram defines the default Telegram config   
`victorops` |  `object` |  victorops defines the default configuration for VictorOps.   
`webex` |  `object` |  webex defines the default configuration for Webex.   
`wechat` |  `object` |  wechat defines the default WeChat Config   
Show more

## 2.1.65. .spec.alertmanagerConfiguration.global.httpConfig

Description
     httpConfig defines the default HTTP configuration. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authorization` |  `object` |  authorization configures the Authorization header credentials used by the client.  Cannot be set at the same time as `basicAuth`, `bearerTokenSecret` or `oauth2`.   
`basicAuth` |  `object` |  basicAuth defines the Basic Authentication credentials used by the client.  Cannot be set at the same time as `authorization`, `bearerTokenSecret` or `oauth2`.   
`bearerTokenSecret` |  `object` |  bearerTokenSecret defines a key of a Secret containing the bearer token used by the client for authentication. The secret needs to be in the same namespace as the custom resource and readable by the Prometheus Operator.  Cannot be set at the same time as `authorization`, `basicAuth` or `oauth2`.  Deprecated: use `authorization` instead.   
`enableHttp2` |  `boolean` |  enableHttp2 can be used to disable HTTP2.   
`followRedirects` |  `boolean` |  followRedirects defines whether the client should follow HTTP 3xx redirects.   
`noProxy` |  `string` |  noProxy defines a comma-separated string that can contain IPs, CIDR notation, domain names that should be excluded from proxying. IP and domain names can contain port numbers.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`oauth2` |  `object` |  oauth2 defines the OAuth2 settings used by the client.  It requires Prometheus >= 2.27.0.  Cannot be set at the same time as `authorization`, `basicAuth` or `bearerTokenSecret`.   
`proxyConnectHeader` |  `object` |  proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests.  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyConnectHeader{}` |  `array` |   
`proxyConnectHeader{}[]` |  `object` |  SecretKeySelector selects a key of a Secret.   
`proxyFromEnvironment` |  `boolean` |  proxyFromEnvironment defines whether to use the proxy configuration defined by environment variables (HTTP_PROXY, HTTPS_PROXY, and NO_PROXY).  It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0.   
`proxyUrl` |  `string` |  proxyUrl defines the HTTP proxy server to use.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS configuration used by the client.   
Show more

## 2.1.66. .spec.alertmanagerConfiguration.global.httpConfig.authorization

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

## 2.1.67. .spec.alertmanagerConfiguration.global.httpConfig.authorization.credentials

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

## 2.1.68. .spec.alertmanagerConfiguration.global.httpConfig.basicAuth

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

## 2.1.69. .spec.alertmanagerConfiguration.global.httpConfig.basicAuth.password

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

## 2.1.70. .spec.alertmanagerConfiguration.global.httpConfig.basicAuth.username

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

## 2.1.71. .spec.alertmanagerConfiguration.global.httpConfig.bearerTokenSecret

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

## 2.1.72. .spec.alertmanagerConfiguration.global.httpConfig.oauth2

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

## 2.1.73. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.clientId

Description
     clientId defines a key of a Secret or ConfigMap containing the OAuth2 client’s ID. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.74. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.clientId.configMap

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

## 2.1.75. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.clientId.secret

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

## 2.1.76. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.clientSecret

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

## 2.1.77. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 2.1.78. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.proxyConnectHeader{}

Description
    
Type
     `array`

## 2.1.79. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.proxyConnectHeader{}[]

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

## 2.1.80. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.tlsConfig

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

## 2.1.81. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.82. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.tlsConfig.ca.configMap

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

## 2.1.83. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.tlsConfig.ca.secret

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

## 2.1.84. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.85. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.tlsConfig.cert.configMap

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

## 2.1.86. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.tlsConfig.cert.secret

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

## 2.1.87. .spec.alertmanagerConfiguration.global.httpConfig.oauth2.tlsConfig.keySecret

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

## 2.1.88. .spec.alertmanagerConfiguration.global.httpConfig.proxyConnectHeader

Description
    

proxyConnectHeader optionally specifies headers to send to proxies during CONNECT requests. 

It requires Prometheus >= v2.43.0, Alertmanager >= v0.25.0 or Thanos >= v0.32.0. 

Type
     `object`

## 2.1.89. .spec.alertmanagerConfiguration.global.httpConfig.proxyConnectHeader{}

Description
    
Type
     `array`

## 2.1.90. .spec.alertmanagerConfiguration.global.httpConfig.proxyConnectHeader{}[]

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

## 2.1.91. .spec.alertmanagerConfiguration.global.httpConfig.tlsConfig

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

## 2.1.92. .spec.alertmanagerConfiguration.global.httpConfig.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.93. .spec.alertmanagerConfiguration.global.httpConfig.tlsConfig.ca.configMap

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

## 2.1.94. .spec.alertmanagerConfiguration.global.httpConfig.tlsConfig.ca.secret

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

## 2.1.95. .spec.alertmanagerConfiguration.global.httpConfig.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.96. .spec.alertmanagerConfiguration.global.httpConfig.tlsConfig.cert.configMap

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

## 2.1.97. .spec.alertmanagerConfiguration.global.httpConfig.tlsConfig.cert.secret

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

## 2.1.98. .spec.alertmanagerConfiguration.global.httpConfig.tlsConfig.keySecret

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

## 2.1.99. .spec.alertmanagerConfiguration.global.jira

Description
     jira defines the default configuration for Jira. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiURL` |  `string` |  apiURL defines the default Jira API URL.  It requires Alertmanager >= v0.28.0.   
Show more

## 2.1.100. .spec.alertmanagerConfiguration.global.opsGenieApiKey

Description
     opsGenieApiKey defines the default OpsGenie API Key. 
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

## 2.1.101. .spec.alertmanagerConfiguration.global.opsGenieApiUrl

Description
     opsGenieApiUrl defines the default OpsGenie API URL. 
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

## 2.1.102. .spec.alertmanagerConfiguration.global.rocketChat

Description
     rocketChat defines the default configuration for Rocket Chat. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiURL` |  `string` |  apiURL defines the default Rocket Chat API URL.  It requires Alertmanager >= v0.28.0.   
`token` |  `object` |  token defines the default Rocket Chat token.  It requires Alertmanager >= v0.28.0.   
`tokenID` |  `object` |  tokenID defines the default Rocket Chat Token ID.  It requires Alertmanager >= v0.28.0.   
Show more

## 2.1.103. .spec.alertmanagerConfiguration.global.rocketChat.token

Description
    

token defines the default Rocket Chat token. 

It requires Alertmanager >= v0.28.0. 

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

## 2.1.104. .spec.alertmanagerConfiguration.global.rocketChat.tokenID

Description
    

tokenID defines the default Rocket Chat Token ID. 

It requires Alertmanager >= v0.28.0. 

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

## 2.1.105. .spec.alertmanagerConfiguration.global.slackApiUrl

Description
     slackApiUrl defines the default Slack API URL. 
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

## 2.1.106. .spec.alertmanagerConfiguration.global.smtp

Description
     smtp defines global SMTP parameters. 
Type
     `object`

Property| Type| Description  
---|---|---  
`authIdentity` |  `string` |  authIdentity represents SMTP Auth using PLAIN   
`authPassword` |  `object` |  authPassword represents SMTP Auth using LOGIN and PLAIN.   
`authSecret` |  `object` |  authSecret represents SMTP Auth using CRAM-MD5.   
`authUsername` |  `string` |  authUsername represents SMTP Auth using CRAM-MD5, LOGIN and PLAIN. If empty, Alertmanager doesn’t authenticate to the SMTP server.   
`forceImplicitTLS` |  `boolean` |  forceImplicitTLS defines whether to force use of implicit TLS (direct TLS connection) for better security. true: force use of implicit TLS (direct TLS connection on any port) false: force disable implicit TLS (use explicit TLS/STARTTLS if required) nil (default): auto-detect based on port (465=implicit, other=explicit) for backward compatibility It requires Alertmanager >= v0.31.0.   
`from` |  `string` |  from defines the default SMTP From header field.   
`hello` |  `string` |  hello defines the default hostname to identify to the SMTP server.   
`requireTLS` |  `boolean` |  requireTLS defines the default SMTP TLS requirement. Note that Go does not support unencrypted connections to remote SMTP endpoints.   
`smartHost` |  `object` |  smartHost defines the default SMTP smarthost used for sending emails.   
`tlsConfig` |  `object` |  tlsConfig defines the default TLS configuration for SMTP receivers   
Show more

## 2.1.107. .spec.alertmanagerConfiguration.global.smtp.authPassword

Description
     authPassword represents SMTP Auth using LOGIN and PLAIN. 
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

## 2.1.108. .spec.alertmanagerConfiguration.global.smtp.authSecret

Description
     authSecret represents SMTP Auth using CRAM-MD5. 
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

## 2.1.109. .spec.alertmanagerConfiguration.global.smtp.smartHost

Description
     smartHost defines the default SMTP smarthost used for sending emails. 
Type
     `object`
Required
    

  * `host`
  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  host defines the host’s address, it can be a DNS name or a literal IP address.   
`port` |  `string` |  port defines the host’s port, it can be a literal port number or a port name.   
Show more

## 2.1.110. .spec.alertmanagerConfiguration.global.smtp.tlsConfig

Description
     tlsConfig defines the default TLS configuration for SMTP receivers 
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

## 2.1.111. .spec.alertmanagerConfiguration.global.smtp.tlsConfig.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.112. .spec.alertmanagerConfiguration.global.smtp.tlsConfig.ca.configMap

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

## 2.1.113. .spec.alertmanagerConfiguration.global.smtp.tlsConfig.ca.secret

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

## 2.1.114. .spec.alertmanagerConfiguration.global.smtp.tlsConfig.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.115. .spec.alertmanagerConfiguration.global.smtp.tlsConfig.cert.configMap

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

## 2.1.116. .spec.alertmanagerConfiguration.global.smtp.tlsConfig.cert.secret

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

## 2.1.117. .spec.alertmanagerConfiguration.global.smtp.tlsConfig.keySecret

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

## 2.1.118. .spec.alertmanagerConfiguration.global.telegram

Description
     telegram defines the default Telegram config 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiURL` |  `string` |  apiURL defines he default Telegram API URL.  It requires Alertmanager >= v0.24.0.   
Show more

## 2.1.119. .spec.alertmanagerConfiguration.global.victorops

Description
     victorops defines the default configuration for VictorOps. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiKey` |  `object` |  apiKey defines the default VictorOps API Key.   
`apiURL` |  `string` |  apiURL defines the default VictorOps API URL.   
Show more

## 2.1.120. .spec.alertmanagerConfiguration.global.victorops.apiKey

Description
     apiKey defines the default VictorOps API Key. 
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

## 2.1.121. .spec.alertmanagerConfiguration.global.webex

Description
     webex defines the default configuration for Webex. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiURL` |  `string` |  apiURL defines the is the default Webex API URL.  It requires Alertmanager >= v0.25.0.   
Show more

## 2.1.122. .spec.alertmanagerConfiguration.global.wechat

Description
     wechat defines the default WeChat Config 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiCorpID` |  `string` |  apiCorpID defines the default WeChat API Corporate ID.   
`apiSecret` |  `object` |  apiSecret defines the default WeChat API Secret.   
`apiURL` |  `string` |  apiURL defines he default WeChat API URL. The default value is "https://qyapi.weixin.qq.com/cgi-bin/"   
Show more

## 2.1.123. .spec.alertmanagerConfiguration.global.wechat.apiSecret

Description
     apiSecret defines the default WeChat API Secret. 
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

## 2.1.124. .spec.alertmanagerConfiguration.templates

Description
     templates defines the custom notification templates. 
Type
     `array`

## 2.1.125. .spec.alertmanagerConfiguration.templates[]

Description
     SecretOrConfigMap allows to specify data as a Secret or ConfigMap. Fields are mutually exclusive. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.126. .spec.alertmanagerConfiguration.templates[].configMap

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

## 2.1.127. .spec.alertmanagerConfiguration.templates[].secret

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

## 2.1.128. .spec.clusterTLS

Description
    

clusterTLS defines the mutual TLS configuration for the Alertmanager cluster’s gossip protocol. 

It requires Alertmanager >= 0.24.0. 

Type
     `object`
Required
    

  * `client`
  * `server`



Property| Type| Description  
---|---|---  
`client` |  `object` |  client defines the client-side configuration for mutual TLS.   
`server` |  `object` |  server defines the server-side configuration for mutual TLS.   
Show more

## 2.1.129. .spec.clusterTLS.client

Description
     client defines the client-side configuration for mutual TLS. 
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

## 2.1.130. .spec.clusterTLS.client.ca

Description
     ca defines the Certificate authority used when verifying server certificates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.131. .spec.clusterTLS.client.ca.configMap

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

## 2.1.132. .spec.clusterTLS.client.ca.secret

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

## 2.1.133. .spec.clusterTLS.client.cert

Description
     cert defines the Client certificate to present when doing client-authentication. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.134. .spec.clusterTLS.client.cert.configMap

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

## 2.1.135. .spec.clusterTLS.client.cert.secret

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

## 2.1.136. .spec.clusterTLS.client.keySecret

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

## 2.1.137. .spec.clusterTLS.server

Description
     server defines the server-side configuration for mutual TLS. 
Type
     `object`

Property| Type| Description  
---|---|---  
`cert` |  `object` |  cert defines the Secret or ConfigMap containing the TLS certificate for the web server.  Either `keySecret` or `keyFile` must be defined.  It is mutually exclusive with `certFile`.   
`certFile` |  `string` |  certFile defines the path to the TLS certificate file in the container for the web server.  Either `keySecret` or `keyFile` must be defined.  It is mutually exclusive with `cert`.   
`cipherSuites` |  `array (string)` |  cipherSuites defines the list of supported cipher suites for TLS versions up to TLS 1.2.  If not defined, the Go default cipher suites are used. Available cipher suites are documented in the Go documentation: <https://golang.org/pkg/crypto/tls/#pkg-constants>  
`clientAuthType` |  `string` |  clientAuthType defines the server policy for client TLS authentication.  For more detail on clientAuth options: <https://golang.org/pkg/crypto/tls/#ClientAuthType>  
`clientCAFile` |  `string` |  clientCAFile defines the path to the CA certificate file for client certificate authentication to the server.  It is mutually exclusive with `client_ca`.   
`client_ca` |  `object` |  client_ca defines the Secret or ConfigMap containing the CA certificate for client certificate authentication to the server.  It is mutually exclusive with `clientCAFile`.   
`curvePreferences` |  `array (string)` |  curvePreferences defines elliptic curves that will be used in an ECDHE handshake, in preference order.  Available curves are documented in the Go documentation: <https://golang.org/pkg/crypto/tls/#CurveID>  
`keyFile` |  `string` |  keyFile defines the path to the TLS private key file in the container for the web server.  If defined, either `cert` or `certFile` must be defined.  It is mutually exclusive with `keySecret`.   
`keySecret` |  `object` |  keySecret defines the secret containing the TLS private key for the web server.  Either `cert` or `certFile` must be defined.  It is mutually exclusive with `keyFile`.   
`maxVersion` |  `string` |  maxVersion defines the Maximum TLS version that is acceptable.   
`minVersion` |  `string` |  minVersion defines the minimum TLS version that is acceptable.   
`preferServerCipherSuites` |  `boolean` |  preferServerCipherSuites defines whether the server selects the client’s most preferred cipher suite, or the server’s most preferred cipher suite.  If true then the server’s preference, as expressed in the order of elements in cipherSuites, is used.   
Show more

## 2.1.138. .spec.clusterTLS.server.cert

Description
    

cert defines the Secret or ConfigMap containing the TLS certificate for the web server. 

Either `keySecret` or `keyFile` must be defined. 

It is mutually exclusive with `certFile`. 

Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.139. .spec.clusterTLS.server.cert.configMap

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

## 2.1.140. .spec.clusterTLS.server.cert.secret

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

## 2.1.141. .spec.clusterTLS.server.client_ca

Description
    

client_ca defines the Secret or ConfigMap containing the CA certificate for client certificate authentication to the server. 

It is mutually exclusive with `clientCAFile`. 

Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.142. .spec.clusterTLS.server.client_ca.configMap

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

## 2.1.143. .spec.clusterTLS.server.client_ca.secret

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

## 2.1.144. .spec.clusterTLS.server.keySecret

Description
    

keySecret defines the secret containing the TLS private key for the web server. 

Either `cert` or `certFile` must be defined. 

It is mutually exclusive with `keyFile`. 

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

## 2.1.145. .spec.containers

Description
    

containers allows injecting additional containers or modifying operator generated containers. This can be used to allow adding an authentication proxy to the Pods or to change the behavior of an operator generated container. Containers described here modify an operator generated container if they share the same name and modifications are done via a strategic merge patch. 

The names of containers managed by the operator are: * `alertmanager` * `config-reloader` * `thanos-sidecar`

Overriding containers which are managed by the operator require careful testing, especially when upgrading to a new version of the operator. 

Type
     `array`

## 2.1.146. .spec.containers[]

Description
     A single application container that you want to run within a pod. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`args` |  `array (string)` |  Arguments to the entrypoint. The container image’s CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell>  
`command` |  `array (string)` |  Entrypoint array. Not executed within a shell. The container image’s ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell>  
`env` |  `array` |  List of environment variables to set in the container. Cannot be updated.   
`env[]` |  `object` |  EnvVar represents an environment variable present in a Container.   
`envFrom` |  `array` |  List of sources to populate environment variables in the container. The keys defined within a source may consist of any printable ASCII characters except '='. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.   
`envFrom[]` |  `object` |  EnvFromSource represents the source of a set of ConfigMaps or Secrets   
`image` |  `string` |  Container image name. More info: <https://kubernetes.io/docs/concepts/containers/images> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.   
`imagePullPolicy` |  `string` |  Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/containers/images#updating-images>  
`lifecycle` |  `object` |  Actions that the management system should take in response to container lifecycle events. Cannot be updated.   
`livenessProbe` |  `object` |  Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`name` |  `string` |  Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.   
`ports` |  `array` |  List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated.   
`ports[]` |  `object` |  ContainerPort represents a network port in a single container.   
`readinessProbe` |  `object` |  Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`resizePolicy` |  `array` |  Resources resize policy for the container. This field cannot be set on ephemeral containers.   
`resizePolicy[]` |  `object` |  ContainerResizePolicy represents resource resize policy for the container.   
`resources` |  `object` |  Compute Resources required by this container. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
`restartPolicy` |  `string` |  RestartPolicy defines the restart behavior of individual containers in a pod. This overrides the pod-level restart policy. When this field is not specified, the restart behavior is defined by the Pod’s restart policy and the container type. Additionally, setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed.   
`restartPolicyRules` |  `array` |  Represents a list of rules to be checked to determine if the container should be restarted on exit. The rules are evaluated in order. Once a rule matches a container exit condition, the remaining rules are ignored. If no rule matches the container exit condition, the Container-level restart policy determines the whether the container is restarted or not. Constraints on the rules: - At most 20 rules are allowed. - Rules can have the same action. - Identical rules are not forbidden in validations. When rules are specified, container MUST set RestartPolicy explicitly even it if matches the Pod’s RestartPolicy.   
`restartPolicyRules[]` |  `object` |  ContainerRestartRule describes how a container exit is handled.   
`securityContext` |  `object` |  SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>  
`startupProbe` |  `object` |  StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod’s lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`stdin` |  `boolean` |  Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.   
`stdinOnce` |  `boolean` |  Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false   
`terminationMessagePath` |  `string` |  Optional: Path at which the file to which the container’s termination message will be written is mounted into the container’s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.   
`terminationMessagePolicy` |  `string` |  Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.   
`tty` |  `boolean` |  Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.   
`volumeDevices` |  `array` |  volumeDevices is the list of block devices to be used by the container.   
`volumeDevices[]` |  `object` |  volumeDevice describes a mapping of a raw block device within a container.   
`volumeMounts` |  `array` |  Pod volumes to mount into the container’s filesystem. Cannot be updated.   
`volumeMounts[]` |  `object` |  VolumeMount describes a mounting of a Volume within a container.   
`workingDir` |  `string` |  Container’s working directory. If not specified, the container runtime’s default will be used, which might be configured in the container image. Cannot be updated.   
Show more

## 2.1.147. .spec.containers[].env

Description
     List of environment variables to set in the container. Cannot be updated. 
Type
     `array`

## 2.1.148. .spec.containers[].env[]

Description
     EnvVar represents an environment variable present in a Container. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the environment variable. May consist of any printable ASCII characters except '='.   
`value` |  `string` |  Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".   
`valueFrom` |  `object` |  Source for the environment variable’s value. Cannot be used if value is not empty.   
Show more

## 2.1.149. .spec.containers[].env[].valueFrom

Description
     Source for the environment variable’s value. Cannot be used if value is not empty. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMapKeyRef` |  `object` |  Selects a key of a ConfigMap.   
`fieldRef` |  `object` |  Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.   
`fileKeyRef` |  `object` |  FileKeyRef selects a key of the env file. Requires the EnvFiles feature gate to be enabled.   
`resourceFieldRef` |  `object` |  Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.   
`secretKeyRef` |  `object` |  Selects a key of a secret in the pod’s namespace   
Show more

## 2.1.150. .spec.containers[].env[].valueFrom.configMapKeyRef

Description
     Selects a key of a ConfigMap. 
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

## 2.1.151. .spec.containers[].env[].valueFrom.fieldRef

Description
     Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. 
Type
     `object`
Required
    

  * `fieldPath`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  Version of the schema the FieldPath is written in terms of, defaults to "v1".   
`fieldPath` |  `string` |  Path of the field to select in the specified API version.   
Show more

## 2.1.152. .spec.containers[].env[].valueFrom.fileKeyRef

Description
     FileKeyRef selects a key of the env file. Requires the EnvFiles feature gate to be enabled. 
Type
     `object`
Required
    

  * `key`
  * `path`
  * `volumeName`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key within the env file. An invalid key will prevent the pod from starting. The keys defined within a source may consist of any printable ASCII characters except '='. During Alpha stage of the EnvFiles feature gate, the key size is limited to 128 characters.   
`optional` |  `boolean` |  Specify whether the file or its key must be defined. If the file or key does not exist, then the env var is not published. If optional is set to true and the specified key does not exist, the environment variable will not be set in the Pod’s containers.  If optional is set to false and the specified key does not exist, an error will be returned during Pod creation.   
`path` |  `string` |  The path within the volume from which to select the file. Must be relative and may not contain the '..' path or start with '..'.   
`volumeName` |  `string` |  The name of the volume mount containing the env file.   
Show more

## 2.1.153. .spec.containers[].env[].valueFrom.resourceFieldRef

Description
     Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. 
Type
     `object`
Required
    

  * `resource`



Property| Type| Description  
---|---|---  
`containerName` |  `string` |  Container name: required for volumes, optional for env vars   
`divisor` |  `integer-or-string` |  Specifies the output format of the exposed resources, defaults to "1"   
`resource` |  `string` |  Required: resource to select   
Show more

## 2.1.154. .spec.containers[].env[].valueFrom.secretKeyRef

Description
     Selects a key of a secret in the pod’s namespace 
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

## 2.1.155. .spec.containers[].envFrom

Description
     List of sources to populate environment variables in the container. The keys defined within a source may consist of any printable ASCII characters except '='. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. 
Type
     `array`

## 2.1.156. .spec.containers[].envFrom[]

Description
     EnvFromSource represents the source of a set of ConfigMaps or Secrets 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMapRef` |  `object` |  The ConfigMap to select from   
`prefix` |  `string` |  Optional text to prepend to the name of each environment variable. May consist of any printable ASCII characters except '='.   
`secretRef` |  `object` |  The Secret to select from   
Show more

## 2.1.157. .spec.containers[].envFrom[].configMapRef

Description
     The ConfigMap to select from 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the ConfigMap must be defined   
Show more

## 2.1.158. .spec.containers[].envFrom[].secretRef

Description
     The Secret to select from 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret must be defined   
Show more

## 2.1.159. .spec.containers[].lifecycle

Description
     Actions that the management system should take in response to container lifecycle events. Cannot be updated. 
Type
     `object`

Property| Type| Description  
---|---|---  
`postStart` |  `object` |  PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>  
`preStop` |  `object` |  PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod’s termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod’s termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>  
`stopSignal` |  `string` |  StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name   
Show more

## 2.1.160. .spec.containers[].lifecycle.postStart

Description
     PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>
Type
     `object`

Property| Type| Description  
---|---|---  
`exec` |  `object` |  Exec specifies a command to execute in the container.   
`httpGet` |  `object` |  HTTPGet specifies an HTTP GET request to perform.   
`sleep` |  `object` |  Sleep represents a duration that the container should sleep.   
`tcpSocket` |  `object` |  Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified.   
Show more

## 2.1.161. .spec.containers[].lifecycle.postStart.exec

Description
     Exec specifies a command to execute in the container. 
Type
     `object`

Property| Type| Description  
---|---|---  
`command` |  `array (string)` |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
Show more

## 2.1.162. .spec.containers[].lifecycle.postStart.httpGet

Description
     HTTPGet specifies an HTTP GET request to perform. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`httpHeaders` |  `array` |  Custom headers to set in the request. HTTP allows repeated headers.   
`httpHeaders[]` |  `object` |  HTTPHeader describes a custom header to be used in HTTP probes   
`path` |  `string` |  Path to access on the HTTP server.   
`port` |  `integer-or-string` |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`scheme` |  `string` |  Scheme to use for connecting to the host. Defaults to HTTP.   
Show more

## 2.1.163. .spec.containers[].lifecycle.postStart.httpGet.httpHeaders

Description
     Custom headers to set in the request. HTTP allows repeated headers. 
Type
     `array`

## 2.1.164. .spec.containers[].lifecycle.postStart.httpGet.httpHeaders[]

Description
     HTTPHeader describes a custom header to be used in HTTP probes 
Type
     `object`
Required
    

  * `name`
  * `value`



Property| Type| Description  
---|---|---  
`name` |  `string` |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`value` |  `string` |  The header field value   
Show more

## 2.1.165. .spec.containers[].lifecycle.postStart.sleep

Description
     Sleep represents a duration that the container should sleep. 
Type
     `object`
Required
    

  * `seconds`



Property| Type| Description  
---|---|---  
`seconds` |  `integer` |  Seconds is the number of seconds to sleep.   
Show more

## 2.1.166. .spec.containers[].lifecycle.postStart.tcpSocket

Description
     Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Optional: Host name to connect to, defaults to the pod IP.   
`port` |  `integer-or-string` |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
Show more

## 2.1.167. .spec.containers[].lifecycle.preStop

Description
     PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod’s termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod’s termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>
Type
     `object`

Property| Type| Description  
---|---|---  
`exec` |  `object` |  Exec specifies a command to execute in the container.   
`httpGet` |  `object` |  HTTPGet specifies an HTTP GET request to perform.   
`sleep` |  `object` |  Sleep represents a duration that the container should sleep.   
`tcpSocket` |  `object` |  Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified.   
Show more

## 2.1.168. .spec.containers[].lifecycle.preStop.exec

Description
     Exec specifies a command to execute in the container. 
Type
     `object`

Property| Type| Description  
---|---|---  
`command` |  `array (string)` |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
Show more

## 2.1.169. .spec.containers[].lifecycle.preStop.httpGet

Description
     HTTPGet specifies an HTTP GET request to perform. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`httpHeaders` |  `array` |  Custom headers to set in the request. HTTP allows repeated headers.   
`httpHeaders[]` |  `object` |  HTTPHeader describes a custom header to be used in HTTP probes   
`path` |  `string` |  Path to access on the HTTP server.   
`port` |  `integer-or-string` |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`scheme` |  `string` |  Scheme to use for connecting to the host. Defaults to HTTP.   
Show more

## 2.1.170. .spec.containers[].lifecycle.preStop.httpGet.httpHeaders

Description
     Custom headers to set in the request. HTTP allows repeated headers. 
Type
     `array`

## 2.1.171. .spec.containers[].lifecycle.preStop.httpGet.httpHeaders[]

Description
     HTTPHeader describes a custom header to be used in HTTP probes 
Type
     `object`
Required
    

  * `name`
  * `value`



Property| Type| Description  
---|---|---  
`name` |  `string` |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`value` |  `string` |  The header field value   
Show more

## 2.1.172. .spec.containers[].lifecycle.preStop.sleep

Description
     Sleep represents a duration that the container should sleep. 
Type
     `object`
Required
    

  * `seconds`



Property| Type| Description  
---|---|---  
`seconds` |  `integer` |  Seconds is the number of seconds to sleep.   
Show more

## 2.1.173. .spec.containers[].lifecycle.preStop.tcpSocket

Description
     Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Optional: Host name to connect to, defaults to the pod IP.   
`port` |  `integer-or-string` |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
Show more

## 2.1.174. .spec.containers[].livenessProbe

Description
     Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>
Type
     `object`

Property| Type| Description  
---|---|---  
`exec` |  `object` |  Exec specifies a command to execute in the container.   
`failureThreshold` |  `integer` |  Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.   
`grpc` |  `object` |  GRPC specifies a GRPC HealthCheckRequest.   
`httpGet` |  `object` |  HTTPGet specifies an HTTP GET request to perform.   
`initialDelaySeconds` |  `integer` |  Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`periodSeconds` |  `integer` |  How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.   
`successThreshold` |  `integer` |  Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.   
`tcpSocket` |  `object` |  TCPSocket specifies a connection to a TCP port.   
`terminationGracePeriodSeconds` |  `integer` |  Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.   
`timeoutSeconds` |  `integer` |  Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
Show more

## 2.1.175. .spec.containers[].livenessProbe.exec

Description
     Exec specifies a command to execute in the container. 
Type
     `object`

Property| Type| Description  
---|---|---  
`command` |  `array (string)` |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
Show more

## 2.1.176. .spec.containers[].livenessProbe.grpc

Description
     GRPC specifies a GRPC HealthCheckRequest. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`port` |  `integer` |  Port number of the gRPC service. Number must be in the range 1 to 65535.   
`service` |  `string` |  Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC.   
Show more

## 2.1.177. .spec.containers[].livenessProbe.httpGet

Description
     HTTPGet specifies an HTTP GET request to perform. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`httpHeaders` |  `array` |  Custom headers to set in the request. HTTP allows repeated headers.   
`httpHeaders[]` |  `object` |  HTTPHeader describes a custom header to be used in HTTP probes   
`path` |  `string` |  Path to access on the HTTP server.   
`port` |  `integer-or-string` |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`scheme` |  `string` |  Scheme to use for connecting to the host. Defaults to HTTP.   
Show more

## 2.1.178. .spec.containers[].livenessProbe.httpGet.httpHeaders

Description
     Custom headers to set in the request. HTTP allows repeated headers. 
Type
     `array`

## 2.1.179. .spec.containers[].livenessProbe.httpGet.httpHeaders[]

Description
     HTTPHeader describes a custom header to be used in HTTP probes 
Type
     `object`
Required
    

  * `name`
  * `value`



Property| Type| Description  
---|---|---  
`name` |  `string` |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`value` |  `string` |  The header field value   
Show more

## 2.1.180. .spec.containers[].livenessProbe.tcpSocket

Description
     TCPSocket specifies a connection to a TCP port. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Optional: Host name to connect to, defaults to the pod IP.   
`port` |  `integer-or-string` |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
Show more

## 2.1.181. .spec.containers[].ports

Description
     List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated. 
Type
     `array`

## 2.1.182. .spec.containers[].ports[]

Description
     ContainerPort represents a network port in a single container. 
Type
     `object`
Required
    

  * `containerPort`



Property| Type| Description  
---|---|---  
`containerPort` |  `integer` |  Number of port to expose on the pod’s IP address. This must be a valid port number, 0 < x < 65536\.   
`hostIP` |  `string` |  What host IP to bind the external port to.   
`hostPort` |  `integer` |  Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536\. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.   
`name` |  `string` |  If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.   
`protocol` |  `string` |  Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".   
Show more

## 2.1.183. .spec.containers[].readinessProbe

Description
     Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>
Type
     `object`

Property| Type| Description  
---|---|---  
`exec` |  `object` |  Exec specifies a command to execute in the container.   
`failureThreshold` |  `integer` |  Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.   
`grpc` |  `object` |  GRPC specifies a GRPC HealthCheckRequest.   
`httpGet` |  `object` |  HTTPGet specifies an HTTP GET request to perform.   
`initialDelaySeconds` |  `integer` |  Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`periodSeconds` |  `integer` |  How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.   
`successThreshold` |  `integer` |  Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.   
`tcpSocket` |  `object` |  TCPSocket specifies a connection to a TCP port.   
`terminationGracePeriodSeconds` |  `integer` |  Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.   
`timeoutSeconds` |  `integer` |  Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
Show more

## 2.1.184. .spec.containers[].readinessProbe.exec

Description
     Exec specifies a command to execute in the container. 
Type
     `object`

Property| Type| Description  
---|---|---  
`command` |  `array (string)` |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
Show more

## 2.1.185. .spec.containers[].readinessProbe.grpc

Description
     GRPC specifies a GRPC HealthCheckRequest. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`port` |  `integer` |  Port number of the gRPC service. Number must be in the range 1 to 65535.   
`service` |  `string` |  Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC.   
Show more

## 2.1.186. .spec.containers[].readinessProbe.httpGet

Description
     HTTPGet specifies an HTTP GET request to perform. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`httpHeaders` |  `array` |  Custom headers to set in the request. HTTP allows repeated headers.   
`httpHeaders[]` |  `object` |  HTTPHeader describes a custom header to be used in HTTP probes   
`path` |  `string` |  Path to access on the HTTP server.   
`port` |  `integer-or-string` |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`scheme` |  `string` |  Scheme to use for connecting to the host. Defaults to HTTP.   
Show more

## 2.1.187. .spec.containers[].readinessProbe.httpGet.httpHeaders

Description
     Custom headers to set in the request. HTTP allows repeated headers. 
Type
     `array`

## 2.1.188. .spec.containers[].readinessProbe.httpGet.httpHeaders[]

Description
     HTTPHeader describes a custom header to be used in HTTP probes 
Type
     `object`
Required
    

  * `name`
  * `value`



Property| Type| Description  
---|---|---  
`name` |  `string` |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`value` |  `string` |  The header field value   
Show more

## 2.1.189. .spec.containers[].readinessProbe.tcpSocket

Description
     TCPSocket specifies a connection to a TCP port. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Optional: Host name to connect to, defaults to the pod IP.   
`port` |  `integer-or-string` |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
Show more

## 2.1.190. .spec.containers[].resizePolicy

Description
     Resources resize policy for the container. This field cannot be set on ephemeral containers. 
Type
     `array`

## 2.1.191. .spec.containers[].resizePolicy[]

Description
     ContainerResizePolicy represents resource resize policy for the container. 
Type
     `object`
Required
    

  * `resourceName`
  * `restartPolicy`



Property| Type| Description  
---|---|---  
`resourceName` |  `string` |  Name of the resource to which this resource resize policy applies. Supported values: cpu, memory.   
`restartPolicy` |  `string` |  Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired.   
Show more

## 2.1.192. .spec.containers[].resources

Description
     Compute Resources required by this container. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>
Type
     `object`

Property| Type| Description  
---|---|---  
`claims` |  `array` |  Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This field depends on the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers.   
`claims[]` |  `object` |  ResourceClaim references one entry in PodSpec.ResourceClaims.   
`limits` |  `integer-or-string` |  Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
`requests` |  `integer-or-string` |  Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
Show more

## 2.1.193. .spec.containers[].resources.claims

Description
    

Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container. 

This field depends on the DynamicResourceAllocation feature gate. 

This field is immutable. It can only be set for containers. 

Type
     `array`

## 2.1.194. .spec.containers[].resources.claims[]

Description
     ResourceClaim references one entry in PodSpec.ResourceClaims. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container.   
`request` |  `string` |  Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request.   
Show more

## 2.1.195. .spec.containers[].restartPolicyRules

Description
     Represents a list of rules to be checked to determine if the container should be restarted on exit. The rules are evaluated in order. Once a rule matches a container exit condition, the remaining rules are ignored. If no rule matches the container exit condition, the Container-level restart policy determines the whether the container is restarted or not. Constraints on the rules: - At most 20 rules are allowed. - Rules can have the same action. - Identical rules are not forbidden in validations. When rules are specified, container MUST set RestartPolicy explicitly even it if matches the Pod’s RestartPolicy. 
Type
     `array`

## 2.1.196. .spec.containers[].restartPolicyRules[]

Description
     ContainerRestartRule describes how a container exit is handled. 
Type
     `object`
Required
    

  * `action`



Property| Type| Description  
---|---|---  
`action` |  `string` |  Specifies the action taken on a container exit if the requirements are satisfied. The only possible value is "Restart" to restart the container.   
`exitCodes` |  `object` |  Represents the exit codes to check on container exits.   
Show more

## 2.1.197. .spec.containers[].restartPolicyRules[].exitCodes

Description
     Represents the exit codes to check on container exits. 
Type
     `object`
Required
    

  * `operator`



Property| Type| Description  
---|---|---  
`operator` |  `string` |  Represents the relationship between the container exit code(s) and the specified values. Possible values are: - In: the requirement is satisfied if the container exit code is in the set of specified values. - NotIn: the requirement is satisfied if the container exit code is not in the set of specified values.   
`values` |  `array (integer)` |  Specifies the set of values to check for container exit codes. At most 255 elements are allowed.   
Show more

## 2.1.198. .spec.containers[].securityContext

Description
     SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>
Type
     `object`

Property| Type| Description  
---|---|---  
`allowPrivilegeEscalation` |  `boolean` |  AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.   
`appArmorProfile` |  `object` |  appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod’s appArmorProfile. Note that this field cannot be set when spec.os.name is windows.   
`capabilities` |  `object` |  The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.   
`privileged` |  `boolean` |  Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.   
`procMount` |  `string` |  procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.   
`readOnlyRootFilesystem` |  `boolean` |  Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows.   
`runAsGroup` |  `integer` |  The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.   
`runAsNonRoot` |  `boolean` |  Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.   
`runAsUser` |  `integer` |  The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.   
`seLinuxOptions` |  `object` |  The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.   
`seccompProfile` |  `object` |  The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.   
`windowsOptions` |  `object` |  The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.   
Show more

## 2.1.199. .spec.containers[].securityContext.appArmorProfile

Description
     appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod’s appArmorProfile. Note that this field cannot be set when spec.os.name is windows. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`localhostProfile` |  `string` |  localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost".   
`type` |  `string` |  type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement.   
Show more

## 2.1.200. .spec.containers[].securityContext.capabilities

Description
     The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows. 
Type
     `object`

Property| Type| Description  
---|---|---  
`add` |  `array (string)` |  Added capabilities   
`drop` |  `array (string)` |  Removed capabilities   
Show more

## 2.1.201. .spec.containers[].securityContext.seLinuxOptions

Description
     The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. 
Type
     `object`

Property| Type| Description  
---|---|---  
`level` |  `string` |  Level is SELinux level label that applies to the container.   
`role` |  `string` |  Role is a SELinux role label that applies to the container.   
`type` |  `string` |  Type is a SELinux type label that applies to the container.   
`user` |  `string` |  User is a SELinux user label that applies to the container.   
Show more

## 2.1.202. .spec.containers[].securityContext.seccompProfile

Description
     The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`localhostProfile` |  `string` |  localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.   
`type` |  `string` |  type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.   
Show more

## 2.1.203. .spec.containers[].securityContext.windowsOptions

Description
     The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. 
Type
     `object`

Property| Type| Description  
---|---|---  
`gmsaCredentialSpec` |  `string` |  GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.   
`gmsaCredentialSpecName` |  `string` |  GMSACredentialSpecName is the name of the GMSA credential spec to use.   
`hostProcess` |  `boolean` |  HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true.   
`runAsUserName` |  `string` |  The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.   
Show more

## 2.1.204. .spec.containers[].startupProbe

Description
     StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod’s lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>
Type
     `object`

Property| Type| Description  
---|---|---  
`exec` |  `object` |  Exec specifies a command to execute in the container.   
`failureThreshold` |  `integer` |  Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.   
`grpc` |  `object` |  GRPC specifies a GRPC HealthCheckRequest.   
`httpGet` |  `object` |  HTTPGet specifies an HTTP GET request to perform.   
`initialDelaySeconds` |  `integer` |  Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`periodSeconds` |  `integer` |  How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.   
`successThreshold` |  `integer` |  Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.   
`tcpSocket` |  `object` |  TCPSocket specifies a connection to a TCP port.   
`terminationGracePeriodSeconds` |  `integer` |  Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.   
`timeoutSeconds` |  `integer` |  Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
Show more

## 2.1.205. .spec.containers[].startupProbe.exec

Description
     Exec specifies a command to execute in the container. 
Type
     `object`

Property| Type| Description  
---|---|---  
`command` |  `array (string)` |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
Show more

## 2.1.206. .spec.containers[].startupProbe.grpc

Description
     GRPC specifies a GRPC HealthCheckRequest. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`port` |  `integer` |  Port number of the gRPC service. Number must be in the range 1 to 65535.   
`service` |  `string` |  Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC.   
Show more

## 2.1.207. .spec.containers[].startupProbe.httpGet

Description
     HTTPGet specifies an HTTP GET request to perform. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`httpHeaders` |  `array` |  Custom headers to set in the request. HTTP allows repeated headers.   
`httpHeaders[]` |  `object` |  HTTPHeader describes a custom header to be used in HTTP probes   
`path` |  `string` |  Path to access on the HTTP server.   
`port` |  `integer-or-string` |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`scheme` |  `string` |  Scheme to use for connecting to the host. Defaults to HTTP.   
Show more

## 2.1.208. .spec.containers[].startupProbe.httpGet.httpHeaders

Description
     Custom headers to set in the request. HTTP allows repeated headers. 
Type
     `array`

## 2.1.209. .spec.containers[].startupProbe.httpGet.httpHeaders[]

Description
     HTTPHeader describes a custom header to be used in HTTP probes 
Type
     `object`
Required
    

  * `name`
  * `value`



Property| Type| Description  
---|---|---  
`name` |  `string` |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`value` |  `string` |  The header field value   
Show more

## 2.1.210. .spec.containers[].startupProbe.tcpSocket

Description
     TCPSocket specifies a connection to a TCP port. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Optional: Host name to connect to, defaults to the pod IP.   
`port` |  `integer-or-string` |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
Show more

## 2.1.211. .spec.containers[].volumeDevices

Description
     volumeDevices is the list of block devices to be used by the container. 
Type
     `array`

## 2.1.212. .spec.containers[].volumeDevices[]

Description
     volumeDevice describes a mapping of a raw block device within a container. 
Type
     `object`
Required
    

  * `devicePath`
  * `name`



Property| Type| Description  
---|---|---  
`devicePath` |  `string` |  devicePath is the path inside of the container that the device will be mapped to.   
`name` |  `string` |  name must match the name of a persistentVolumeClaim in the pod   
Show more

## 2.1.213. .spec.containers[].volumeMounts

Description
     Pod volumes to mount into the container’s filesystem. Cannot be updated. 
Type
     `array`

## 2.1.214. .spec.containers[].volumeMounts[]

Description
     VolumeMount describes a mounting of a Volume within a container. 
Type
     `object`
Required
    

  * `mountPath`
  * `name`



Property| Type| Description  
---|---|---  
`mountPath` |  `string` |  Path within the container at which the volume should be mounted. Must not contain ':'.   
`mountPropagation` |  `string` |  mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).   
`name` |  `string` |  This must match the Name of a Volume.   
`readOnly` |  `boolean` |  Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.   
`recursiveReadOnly` |  `string` |  RecursiveReadOnly specifies whether read-only mounts should be handled recursively.  If ReadOnly is false, this field has no meaning and must be unspecified.  If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.  If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).  If this field is not specified, it is treated as an equivalent of Disabled.   
`subPath` |  `string` |  Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root).   
`subPathExpr` |  `string` |  Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive.   
Show more

## 2.1.215. .spec.dnsConfig

Description
     dnsConfig defines the DNS configuration for the pods. 
Type
     `object`

Property| Type| Description  
---|---|---  
`nameservers` |  `array (string)` |  nameservers defines the list of DNS name server IP addresses. This will be appended to the base nameservers generated from DNSPolicy.   
`options` |  `array` |  options defines the list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Resolution options given in Options will override those that appear in the base DNSPolicy.   
`options[]` |  `object` |  PodDNSConfigOption defines DNS resolver options of a pod.   
`searches` |  `array (string)` |  searches defines the list of DNS search domains for host-name lookup. This will be appended to the base search paths generated from DNSPolicy.   
Show more

## 2.1.216. .spec.dnsConfig.options

Description
     options defines the list of DNS resolver options. This will be merged with the base options generated from DNSPolicy. Resolution options given in Options will override those that appear in the base DNSPolicy. 
Type
     `array`

## 2.1.217. .spec.dnsConfig.options[]

Description
     PodDNSConfigOption defines DNS resolver options of a pod. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is required and must be unique.   
`value` |  `string` |  value is optional.   
Show more

## 2.1.218. .spec.hostAliases

Description
     hostAliases Pods configuration 
Type
     `array`

## 2.1.219. .spec.hostAliases[]

Description
     HostAlias holds the mapping between IP and hostnames that will be injected as an entry in the pod’s hosts file. 
Type
     `object`
Required
    

  * `hostnames`
  * `ip`



Property| Type| Description  
---|---|---  
`hostnames` |  `array (string)` |  hostnames defines hostnames for the above IP address.   
`ip` |  `string` |  ip defines the IP address of the host file entry.   
Show more

## 2.1.220. .spec.imagePullSecrets

Description
     imagePullSecrets An optional list of references to secrets in the same namespace to use for pulling prometheus and alertmanager images from registries see <https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/>
Type
     `array`

## 2.1.221. .spec.imagePullSecrets[]

Description
     LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 2.1.222. .spec.initContainers

Description
    

initContainers allows injecting initContainers to the Pod definition. Those can be used to e.g. fetch secrets for injection into the Prometheus configuration from external sources. Any errors during the execution of an initContainer will lead to a restart of the Pod. More info: <https://kubernetes.io/docs/concepts/workloads/pods/init-containers/> InitContainers described here modify an operator generated init containers if they share the same name and modifications are done via a strategic merge patch. 

The names of init container name managed by the operator are: * `init-config-reloader`. 

Overriding init containers which are managed by the operator require careful testing, especially when upgrading to a new version of the operator. 

Type
     `array`

## 2.1.223. .spec.initContainers[]

Description
     A single application container that you want to run within a pod. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`args` |  `array (string)` |  Arguments to the entrypoint. The container image’s CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell>  
`command` |  `array (string)` |  Entrypoint array. Not executed within a shell. The container image’s ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container’s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: <https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell>  
`env` |  `array` |  List of environment variables to set in the container. Cannot be updated.   
`env[]` |  `object` |  EnvVar represents an environment variable present in a Container.   
`envFrom` |  `array` |  List of sources to populate environment variables in the container. The keys defined within a source may consist of any printable ASCII characters except '='. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated.   
`envFrom[]` |  `object` |  EnvFromSource represents the source of a set of ConfigMaps or Secrets   
`image` |  `string` |  Container image name. More info: <https://kubernetes.io/docs/concepts/containers/images> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.   
`imagePullPolicy` |  `string` |  Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/containers/images#updating-images>  
`lifecycle` |  `object` |  Actions that the management system should take in response to container lifecycle events. Cannot be updated.   
`livenessProbe` |  `object` |  Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`name` |  `string` |  Name of the container specified as a DNS_LABEL. Each container in a pod must have a unique name (DNS_LABEL). Cannot be updated.   
`ports` |  `array` |  List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated.   
`ports[]` |  `object` |  ContainerPort represents a network port in a single container.   
`readinessProbe` |  `object` |  Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`resizePolicy` |  `array` |  Resources resize policy for the container. This field cannot be set on ephemeral containers.   
`resizePolicy[]` |  `object` |  ContainerResizePolicy represents resource resize policy for the container.   
`resources` |  `object` |  Compute Resources required by this container. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
`restartPolicy` |  `string` |  RestartPolicy defines the restart behavior of individual containers in a pod. This overrides the pod-level restart policy. When this field is not specified, the restart behavior is defined by the Pod’s restart policy and the container type. Additionally, setting the RestartPolicy as "Always" for the init container will have the following effect: this init container will be continually restarted on exit until all regular containers have terminated. Once all regular containers have completed, all init containers with restartPolicy "Always" will be shut down. This lifecycle differs from normal init containers and is often referred to as a "sidecar" container. Although this init container still starts in the init container sequence, it does not wait for the container to complete before proceeding to the next init container. Instead, the next init container starts immediately after this init container is started, or after any startupProbe has successfully completed.   
`restartPolicyRules` |  `array` |  Represents a list of rules to be checked to determine if the container should be restarted on exit. The rules are evaluated in order. Once a rule matches a container exit condition, the remaining rules are ignored. If no rule matches the container exit condition, the Container-level restart policy determines the whether the container is restarted or not. Constraints on the rules: - At most 20 rules are allowed. - Rules can have the same action. - Identical rules are not forbidden in validations. When rules are specified, container MUST set RestartPolicy explicitly even it if matches the Pod’s RestartPolicy.   
`restartPolicyRules[]` |  `object` |  ContainerRestartRule describes how a container exit is handled.   
`securityContext` |  `object` |  SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>  
`startupProbe` |  `object` |  StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod’s lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`stdin` |  `boolean` |  Whether this container should allocate a buffer for stdin in the container runtime. If this is not set, reads from stdin in the container will always result in EOF. Default is false.   
`stdinOnce` |  `boolean` |  Whether the container runtime should close the stdin channel after it has been opened by a single attach. When stdin is true the stdin stream will remain open across multiple attach sessions. If stdinOnce is set to true, stdin is opened on container start, is empty until the first client attaches to stdin, and then remains open and accepts data until the client disconnects, at which time stdin is closed and remains closed until the container is restarted. If this flag is false, a container processes that reads from stdin will never receive an EOF. Default is false   
`terminationMessagePath` |  `string` |  Optional: Path at which the file to which the container’s termination message will be written is mounted into the container’s filesystem. Message written is intended to be brief final status, such as an assertion failure message. Will be truncated by the node if greater than 4096 bytes. The total message length across all containers will be limited to 12kb. Defaults to /dev/termination-log. Cannot be updated.   
`terminationMessagePolicy` |  `string` |  Indicate how the termination message should be populated. File will use the contents of terminationMessagePath to populate the container status message on both success and failure. FallbackToLogsOnError will use the last chunk of container log output if the termination message file is empty and the container exited with an error. The log output is limited to 2048 bytes or 80 lines, whichever is smaller. Defaults to File. Cannot be updated.   
`tty` |  `boolean` |  Whether this container should allocate a TTY for itself, also requires 'stdin' to be true. Default is false.   
`volumeDevices` |  `array` |  volumeDevices is the list of block devices to be used by the container.   
`volumeDevices[]` |  `object` |  volumeDevice describes a mapping of a raw block device within a container.   
`volumeMounts` |  `array` |  Pod volumes to mount into the container’s filesystem. Cannot be updated.   
`volumeMounts[]` |  `object` |  VolumeMount describes a mounting of a Volume within a container.   
`workingDir` |  `string` |  Container’s working directory. If not specified, the container runtime’s default will be used, which might be configured in the container image. Cannot be updated.   
Show more

## 2.1.224. .spec.initContainers[].env

Description
     List of environment variables to set in the container. Cannot be updated. 
Type
     `array`

## 2.1.225. .spec.initContainers[].env[]

Description
     EnvVar represents an environment variable present in a Container. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the environment variable. May consist of any printable ASCII characters except '='.   
`value` |  `string` |  Variable references $(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "".   
`valueFrom` |  `object` |  Source for the environment variable’s value. Cannot be used if value is not empty.   
Show more

## 2.1.226. .spec.initContainers[].env[].valueFrom

Description
     Source for the environment variable’s value. Cannot be used if value is not empty. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMapKeyRef` |  `object` |  Selects a key of a ConfigMap.   
`fieldRef` |  `object` |  Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs.   
`fileKeyRef` |  `object` |  FileKeyRef selects a key of the env file. Requires the EnvFiles feature gate to be enabled.   
`resourceFieldRef` |  `object` |  Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported.   
`secretKeyRef` |  `object` |  Selects a key of a secret in the pod’s namespace   
Show more

## 2.1.227. .spec.initContainers[].env[].valueFrom.configMapKeyRef

Description
     Selects a key of a ConfigMap. 
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

## 2.1.228. .spec.initContainers[].env[].valueFrom.fieldRef

Description
     Selects a field of the pod: supports metadata.name, metadata.namespace, `metadata.labels['<KEY>']`, `metadata.annotations['<KEY>']`, spec.nodeName, spec.serviceAccountName, status.hostIP, status.podIP, status.podIPs. 
Type
     `object`
Required
    

  * `fieldPath`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  Version of the schema the FieldPath is written in terms of, defaults to "v1".   
`fieldPath` |  `string` |  Path of the field to select in the specified API version.   
Show more

## 2.1.229. .spec.initContainers[].env[].valueFrom.fileKeyRef

Description
     FileKeyRef selects a key of the env file. Requires the EnvFiles feature gate to be enabled. 
Type
     `object`
Required
    

  * `key`
  * `path`
  * `volumeName`



Property| Type| Description  
---|---|---  
`key` |  `string` |  The key within the env file. An invalid key will prevent the pod from starting. The keys defined within a source may consist of any printable ASCII characters except '='. During Alpha stage of the EnvFiles feature gate, the key size is limited to 128 characters.   
`optional` |  `boolean` |  Specify whether the file or its key must be defined. If the file or key does not exist, then the env var is not published. If optional is set to true and the specified key does not exist, the environment variable will not be set in the Pod’s containers.  If optional is set to false and the specified key does not exist, an error will be returned during Pod creation.   
`path` |  `string` |  The path within the volume from which to select the file. Must be relative and may not contain the '..' path or start with '..'.   
`volumeName` |  `string` |  The name of the volume mount containing the env file.   
Show more

## 2.1.230. .spec.initContainers[].env[].valueFrom.resourceFieldRef

Description
     Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, limits.ephemeral-storage, requests.cpu, requests.memory and requests.ephemeral-storage) are currently supported. 
Type
     `object`
Required
    

  * `resource`



Property| Type| Description  
---|---|---  
`containerName` |  `string` |  Container name: required for volumes, optional for env vars   
`divisor` |  `integer-or-string` |  Specifies the output format of the exposed resources, defaults to "1"   
`resource` |  `string` |  Required: resource to select   
Show more

## 2.1.231. .spec.initContainers[].env[].valueFrom.secretKeyRef

Description
     Selects a key of a secret in the pod’s namespace 
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

## 2.1.232. .spec.initContainers[].envFrom

Description
     List of sources to populate environment variables in the container. The keys defined within a source may consist of any printable ASCII characters except '='. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. 
Type
     `array`

## 2.1.233. .spec.initContainers[].envFrom[]

Description
     EnvFromSource represents the source of a set of ConfigMaps or Secrets 
Type
     `object`

Property| Type| Description  
---|---|---  
`configMapRef` |  `object` |  The ConfigMap to select from   
`prefix` |  `string` |  Optional text to prepend to the name of each environment variable. May consist of any printable ASCII characters except '='.   
`secretRef` |  `object` |  The Secret to select from   
Show more

## 2.1.234. .spec.initContainers[].envFrom[].configMapRef

Description
     The ConfigMap to select from 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the ConfigMap must be defined   
Show more

## 2.1.235. .spec.initContainers[].envFrom[].secretRef

Description
     The Secret to select from 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  Specify whether the Secret must be defined   
Show more

## 2.1.236. .spec.initContainers[].lifecycle

Description
     Actions that the management system should take in response to container lifecycle events. Cannot be updated. 
Type
     `object`

Property| Type| Description  
---|---|---  
`postStart` |  `object` |  PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>  
`preStop` |  `object` |  PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod’s termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod’s termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>  
`stopSignal` |  `string` |  StopSignal defines which signal will be sent to a container when it is being stopped. If not specified, the default is defined by the container runtime in use. StopSignal can only be set for Pods with a non-empty .spec.os.name   
Show more

## 2.1.237. .spec.initContainers[].lifecycle.postStart

Description
     PostStart is called immediately after a container is created. If the handler fails, the container is terminated and restarted according to its restart policy. Other management of the container blocks until the hook completes. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>
Type
     `object`

Property| Type| Description  
---|---|---  
`exec` |  `object` |  Exec specifies a command to execute in the container.   
`httpGet` |  `object` |  HTTPGet specifies an HTTP GET request to perform.   
`sleep` |  `object` |  Sleep represents a duration that the container should sleep.   
`tcpSocket` |  `object` |  Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified.   
Show more

## 2.1.238. .spec.initContainers[].lifecycle.postStart.exec

Description
     Exec specifies a command to execute in the container. 
Type
     `object`

Property| Type| Description  
---|---|---  
`command` |  `array (string)` |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
Show more

## 2.1.239. .spec.initContainers[].lifecycle.postStart.httpGet

Description
     HTTPGet specifies an HTTP GET request to perform. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`httpHeaders` |  `array` |  Custom headers to set in the request. HTTP allows repeated headers.   
`httpHeaders[]` |  `object` |  HTTPHeader describes a custom header to be used in HTTP probes   
`path` |  `string` |  Path to access on the HTTP server.   
`port` |  `integer-or-string` |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`scheme` |  `string` |  Scheme to use for connecting to the host. Defaults to HTTP.   
Show more

## 2.1.240. .spec.initContainers[].lifecycle.postStart.httpGet.httpHeaders

Description
     Custom headers to set in the request. HTTP allows repeated headers. 
Type
     `array`

## 2.1.241. .spec.initContainers[].lifecycle.postStart.httpGet.httpHeaders[]

Description
     HTTPHeader describes a custom header to be used in HTTP probes 
Type
     `object`
Required
    

  * `name`
  * `value`



Property| Type| Description  
---|---|---  
`name` |  `string` |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`value` |  `string` |  The header field value   
Show more

## 2.1.242. .spec.initContainers[].lifecycle.postStart.sleep

Description
     Sleep represents a duration that the container should sleep. 
Type
     `object`
Required
    

  * `seconds`



Property| Type| Description  
---|---|---  
`seconds` |  `integer` |  Seconds is the number of seconds to sleep.   
Show more

## 2.1.243. .spec.initContainers[].lifecycle.postStart.tcpSocket

Description
     Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Optional: Host name to connect to, defaults to the pod IP.   
`port` |  `integer-or-string` |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
Show more

## 2.1.244. .spec.initContainers[].lifecycle.preStop

Description
     PreStop is called immediately before a container is terminated due to an API request or management event such as liveness/startup probe failure, preemption, resource contention, etc. The handler is not called if the container crashes or exits. The Pod’s termination grace period countdown begins before the PreStop hook is executed. Regardless of the outcome of the handler, the container will eventually terminate within the Pod’s termination grace period (unless delayed by finalizers). Other management of the container blocks until the hook completes or until the termination grace period is reached. More info: <https://kubernetes.io/docs/concepts/containers/container-lifecycle-hooks/#container-hooks>
Type
     `object`

Property| Type| Description  
---|---|---  
`exec` |  `object` |  Exec specifies a command to execute in the container.   
`httpGet` |  `object` |  HTTPGet specifies an HTTP GET request to perform.   
`sleep` |  `object` |  Sleep represents a duration that the container should sleep.   
`tcpSocket` |  `object` |  Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified.   
Show more

## 2.1.245. .spec.initContainers[].lifecycle.preStop.exec

Description
     Exec specifies a command to execute in the container. 
Type
     `object`

Property| Type| Description  
---|---|---  
`command` |  `array (string)` |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
Show more

## 2.1.246. .spec.initContainers[].lifecycle.preStop.httpGet

Description
     HTTPGet specifies an HTTP GET request to perform. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`httpHeaders` |  `array` |  Custom headers to set in the request. HTTP allows repeated headers.   
`httpHeaders[]` |  `object` |  HTTPHeader describes a custom header to be used in HTTP probes   
`path` |  `string` |  Path to access on the HTTP server.   
`port` |  `integer-or-string` |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`scheme` |  `string` |  Scheme to use for connecting to the host. Defaults to HTTP.   
Show more

## 2.1.247. .spec.initContainers[].lifecycle.preStop.httpGet.httpHeaders

Description
     Custom headers to set in the request. HTTP allows repeated headers. 
Type
     `array`

## 2.1.248. .spec.initContainers[].lifecycle.preStop.httpGet.httpHeaders[]

Description
     HTTPHeader describes a custom header to be used in HTTP probes 
Type
     `object`
Required
    

  * `name`
  * `value`



Property| Type| Description  
---|---|---  
`name` |  `string` |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`value` |  `string` |  The header field value   
Show more

## 2.1.249. .spec.initContainers[].lifecycle.preStop.sleep

Description
     Sleep represents a duration that the container should sleep. 
Type
     `object`
Required
    

  * `seconds`



Property| Type| Description  
---|---|---  
`seconds` |  `integer` |  Seconds is the number of seconds to sleep.   
Show more

## 2.1.250. .spec.initContainers[].lifecycle.preStop.tcpSocket

Description
     Deprecated. TCPSocket is NOT supported as a LifecycleHandler and kept for backward compatibility. There is no validation of this field and lifecycle hooks will fail at runtime when it is specified. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Optional: Host name to connect to, defaults to the pod IP.   
`port` |  `integer-or-string` |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
Show more

## 2.1.251. .spec.initContainers[].livenessProbe

Description
     Periodic probe of container liveness. Container will be restarted if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>
Type
     `object`

Property| Type| Description  
---|---|---  
`exec` |  `object` |  Exec specifies a command to execute in the container.   
`failureThreshold` |  `integer` |  Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.   
`grpc` |  `object` |  GRPC specifies a GRPC HealthCheckRequest.   
`httpGet` |  `object` |  HTTPGet specifies an HTTP GET request to perform.   
`initialDelaySeconds` |  `integer` |  Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`periodSeconds` |  `integer` |  How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.   
`successThreshold` |  `integer` |  Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.   
`tcpSocket` |  `object` |  TCPSocket specifies a connection to a TCP port.   
`terminationGracePeriodSeconds` |  `integer` |  Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.   
`timeoutSeconds` |  `integer` |  Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
Show more

## 2.1.252. .spec.initContainers[].livenessProbe.exec

Description
     Exec specifies a command to execute in the container. 
Type
     `object`

Property| Type| Description  
---|---|---  
`command` |  `array (string)` |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
Show more

## 2.1.253. .spec.initContainers[].livenessProbe.grpc

Description
     GRPC specifies a GRPC HealthCheckRequest. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`port` |  `integer` |  Port number of the gRPC service. Number must be in the range 1 to 65535.   
`service` |  `string` |  Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC.   
Show more

## 2.1.254. .spec.initContainers[].livenessProbe.httpGet

Description
     HTTPGet specifies an HTTP GET request to perform. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`httpHeaders` |  `array` |  Custom headers to set in the request. HTTP allows repeated headers.   
`httpHeaders[]` |  `object` |  HTTPHeader describes a custom header to be used in HTTP probes   
`path` |  `string` |  Path to access on the HTTP server.   
`port` |  `integer-or-string` |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`scheme` |  `string` |  Scheme to use for connecting to the host. Defaults to HTTP.   
Show more

## 2.1.255. .spec.initContainers[].livenessProbe.httpGet.httpHeaders

Description
     Custom headers to set in the request. HTTP allows repeated headers. 
Type
     `array`

## 2.1.256. .spec.initContainers[].livenessProbe.httpGet.httpHeaders[]

Description
     HTTPHeader describes a custom header to be used in HTTP probes 
Type
     `object`
Required
    

  * `name`
  * `value`



Property| Type| Description  
---|---|---  
`name` |  `string` |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`value` |  `string` |  The header field value   
Show more

## 2.1.257. .spec.initContainers[].livenessProbe.tcpSocket

Description
     TCPSocket specifies a connection to a TCP port. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Optional: Host name to connect to, defaults to the pod IP.   
`port` |  `integer-or-string` |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
Show more

## 2.1.258. .spec.initContainers[].ports

Description
     List of ports to expose from the container. Not specifying a port here DOES NOT prevent that port from being exposed. Any port which is listening on the default "0.0.0.0" address inside a container will be accessible from the network. Modifying this array with strategic merge patch may corrupt the data. For more information See <https://github.com/kubernetes/kubernetes/issues/108255>. Cannot be updated. 
Type
     `array`

## 2.1.259. .spec.initContainers[].ports[]

Description
     ContainerPort represents a network port in a single container. 
Type
     `object`
Required
    

  * `containerPort`



Property| Type| Description  
---|---|---  
`containerPort` |  `integer` |  Number of port to expose on the pod’s IP address. This must be a valid port number, 0 < x < 65536\.   
`hostIP` |  `string` |  What host IP to bind the external port to.   
`hostPort` |  `integer` |  Number of port to expose on the host. If specified, this must be a valid port number, 0 < x < 65536\. If HostNetwork is specified, this must match ContainerPort. Most containers do not need this.   
`name` |  `string` |  If specified, this must be an IANA_SVC_NAME and unique within the pod. Each named port in a pod must have a unique name. Name for the port that can be referred to by services.   
`protocol` |  `string` |  Protocol for port. Must be UDP, TCP, or SCTP. Defaults to "TCP".   
Show more

## 2.1.260. .spec.initContainers[].readinessProbe

Description
     Periodic probe of container service readiness. Container will be removed from service endpoints if the probe fails. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>
Type
     `object`

Property| Type| Description  
---|---|---  
`exec` |  `object` |  Exec specifies a command to execute in the container.   
`failureThreshold` |  `integer` |  Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.   
`grpc` |  `object` |  GRPC specifies a GRPC HealthCheckRequest.   
`httpGet` |  `object` |  HTTPGet specifies an HTTP GET request to perform.   
`initialDelaySeconds` |  `integer` |  Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`periodSeconds` |  `integer` |  How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.   
`successThreshold` |  `integer` |  Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.   
`tcpSocket` |  `object` |  TCPSocket specifies a connection to a TCP port.   
`terminationGracePeriodSeconds` |  `integer` |  Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.   
`timeoutSeconds` |  `integer` |  Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
Show more

## 2.1.261. .spec.initContainers[].readinessProbe.exec

Description
     Exec specifies a command to execute in the container. 
Type
     `object`

Property| Type| Description  
---|---|---  
`command` |  `array (string)` |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
Show more

## 2.1.262. .spec.initContainers[].readinessProbe.grpc

Description
     GRPC specifies a GRPC HealthCheckRequest. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`port` |  `integer` |  Port number of the gRPC service. Number must be in the range 1 to 65535.   
`service` |  `string` |  Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC.   
Show more

## 2.1.263. .spec.initContainers[].readinessProbe.httpGet

Description
     HTTPGet specifies an HTTP GET request to perform. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`httpHeaders` |  `array` |  Custom headers to set in the request. HTTP allows repeated headers.   
`httpHeaders[]` |  `object` |  HTTPHeader describes a custom header to be used in HTTP probes   
`path` |  `string` |  Path to access on the HTTP server.   
`port` |  `integer-or-string` |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`scheme` |  `string` |  Scheme to use for connecting to the host. Defaults to HTTP.   
Show more

## 2.1.264. .spec.initContainers[].readinessProbe.httpGet.httpHeaders

Description
     Custom headers to set in the request. HTTP allows repeated headers. 
Type
     `array`

## 2.1.265. .spec.initContainers[].readinessProbe.httpGet.httpHeaders[]

Description
     HTTPHeader describes a custom header to be used in HTTP probes 
Type
     `object`
Required
    

  * `name`
  * `value`



Property| Type| Description  
---|---|---  
`name` |  `string` |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`value` |  `string` |  The header field value   
Show more

## 2.1.266. .spec.initContainers[].readinessProbe.tcpSocket

Description
     TCPSocket specifies a connection to a TCP port. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Optional: Host name to connect to, defaults to the pod IP.   
`port` |  `integer-or-string` |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
Show more

## 2.1.267. .spec.initContainers[].resizePolicy

Description
     Resources resize policy for the container. This field cannot be set on ephemeral containers. 
Type
     `array`

## 2.1.268. .spec.initContainers[].resizePolicy[]

Description
     ContainerResizePolicy represents resource resize policy for the container. 
Type
     `object`
Required
    

  * `resourceName`
  * `restartPolicy`



Property| Type| Description  
---|---|---  
`resourceName` |  `string` |  Name of the resource to which this resource resize policy applies. Supported values: cpu, memory.   
`restartPolicy` |  `string` |  Restart policy to apply when specified resource is resized. If not specified, it defaults to NotRequired.   
Show more

## 2.1.269. .spec.initContainers[].resources

Description
     Compute Resources required by this container. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>
Type
     `object`

Property| Type| Description  
---|---|---  
`claims` |  `array` |  Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This field depends on the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers.   
`claims[]` |  `object` |  ResourceClaim references one entry in PodSpec.ResourceClaims.   
`limits` |  `integer-or-string` |  Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
`requests` |  `integer-or-string` |  Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
Show more

## 2.1.270. .spec.initContainers[].resources.claims

Description
    

Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container. 

This field depends on the DynamicResourceAllocation feature gate. 

This field is immutable. It can only be set for containers. 

Type
     `array`

## 2.1.271. .spec.initContainers[].resources.claims[]

Description
     ResourceClaim references one entry in PodSpec.ResourceClaims. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container.   
`request` |  `string` |  Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request.   
Show more

## 2.1.272. .spec.initContainers[].restartPolicyRules

Description
     Represents a list of rules to be checked to determine if the container should be restarted on exit. The rules are evaluated in order. Once a rule matches a container exit condition, the remaining rules are ignored. If no rule matches the container exit condition, the Container-level restart policy determines the whether the container is restarted or not. Constraints on the rules: - At most 20 rules are allowed. - Rules can have the same action. - Identical rules are not forbidden in validations. When rules are specified, container MUST set RestartPolicy explicitly even it if matches the Pod’s RestartPolicy. 
Type
     `array`

## 2.1.273. .spec.initContainers[].restartPolicyRules[]

Description
     ContainerRestartRule describes how a container exit is handled. 
Type
     `object`
Required
    

  * `action`



Property| Type| Description  
---|---|---  
`action` |  `string` |  Specifies the action taken on a container exit if the requirements are satisfied. The only possible value is "Restart" to restart the container.   
`exitCodes` |  `object` |  Represents the exit codes to check on container exits.   
Show more

## 2.1.274. .spec.initContainers[].restartPolicyRules[].exitCodes

Description
     Represents the exit codes to check on container exits. 
Type
     `object`
Required
    

  * `operator`



Property| Type| Description  
---|---|---  
`operator` |  `string` |  Represents the relationship between the container exit code(s) and the specified values. Possible values are: - In: the requirement is satisfied if the container exit code is in the set of specified values. - NotIn: the requirement is satisfied if the container exit code is not in the set of specified values.   
`values` |  `array (integer)` |  Specifies the set of values to check for container exit codes. At most 255 elements are allowed.   
Show more

## 2.1.275. .spec.initContainers[].securityContext

Description
     SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>
Type
     `object`

Property| Type| Description  
---|---|---  
`allowPrivilegeEscalation` |  `boolean` |  AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no_new_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP_SYS_ADMIN Note that this field cannot be set when spec.os.name is windows.   
`appArmorProfile` |  `object` |  appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod’s appArmorProfile. Note that this field cannot be set when spec.os.name is windows.   
`capabilities` |  `object` |  The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.   
`privileged` |  `boolean` |  Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.   
`procMount` |  `string` |  procMount denotes the type of proc mount to use for the containers. The default value is Default which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.   
`readOnlyRootFilesystem` |  `boolean` |  Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows.   
`runAsGroup` |  `integer` |  The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.   
`runAsNonRoot` |  `boolean` |  Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.   
`runAsUser` |  `integer` |  The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.   
`seLinuxOptions` |  `object` |  The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.   
`seccompProfile` |  `object` |  The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.   
`windowsOptions` |  `object` |  The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.   
Show more

## 2.1.276. .spec.initContainers[].securityContext.appArmorProfile

Description
     appArmorProfile is the AppArmor options to use by this container. If set, this profile overrides the pod’s appArmorProfile. Note that this field cannot be set when spec.os.name is windows. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`localhostProfile` |  `string` |  localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost".   
`type` |  `string` |  type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement.   
Show more

## 2.1.277. .spec.initContainers[].securityContext.capabilities

Description
     The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows. 
Type
     `object`

Property| Type| Description  
---|---|---  
`add` |  `array (string)` |  Added capabilities   
`drop` |  `array (string)` |  Removed capabilities   
Show more

## 2.1.278. .spec.initContainers[].securityContext.seLinuxOptions

Description
     The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows. 
Type
     `object`

Property| Type| Description  
---|---|---  
`level` |  `string` |  Level is SELinux level label that applies to the container.   
`role` |  `string` |  Role is a SELinux role label that applies to the container.   
`type` |  `string` |  Type is a SELinux type label that applies to the container.   
`user` |  `string` |  User is a SELinux user label that applies to the container.   
Show more

## 2.1.279. .spec.initContainers[].securityContext.seccompProfile

Description
     The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`localhostProfile` |  `string` |  localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.   
`type` |  `string` |  type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.   
Show more

## 2.1.280. .spec.initContainers[].securityContext.windowsOptions

Description
     The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. 
Type
     `object`

Property| Type| Description  
---|---|---  
`gmsaCredentialSpec` |  `string` |  GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.   
`gmsaCredentialSpecName` |  `string` |  GMSACredentialSpecName is the name of the GMSA credential spec to use.   
`hostProcess` |  `boolean` |  HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true.   
`runAsUserName` |  `string` |  The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.   
Show more

## 2.1.281. .spec.initContainers[].startupProbe

Description
     StartupProbe indicates that the Pod has successfully initialized. If specified, no other probes are executed until this completes successfully. If this probe fails, the Pod will be restarted, just as if the livenessProbe failed. This can be used to provide different probe parameters at the beginning of a Pod’s lifecycle, when it might take a long time to load data or warm a cache, than during steady-state operation. This cannot be updated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>
Type
     `object`

Property| Type| Description  
---|---|---  
`exec` |  `object` |  Exec specifies a command to execute in the container.   
`failureThreshold` |  `integer` |  Minimum consecutive failures for the probe to be considered failed after having succeeded. Defaults to 3. Minimum value is 1.   
`grpc` |  `object` |  GRPC specifies a GRPC HealthCheckRequest.   
`httpGet` |  `object` |  HTTPGet specifies an HTTP GET request to perform.   
`initialDelaySeconds` |  `integer` |  Number of seconds after the container has started before liveness probes are initiated. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
`periodSeconds` |  `integer` |  How often (in seconds) to perform the probe. Default to 10 seconds. Minimum value is 1.   
`successThreshold` |  `integer` |  Minimum consecutive successes for the probe to be considered successful after having failed. Defaults to 1. Must be 1 for liveness and startup. Minimum value is 1.   
`tcpSocket` |  `object` |  TCPSocket specifies a connection to a TCP port.   
`terminationGracePeriodSeconds` |  `integer` |  Optional duration in seconds the pod needs to terminate gracefully upon probe failure. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. If this value is nil, the pod’s terminationGracePeriodSeconds will be used. Otherwise, this value overrides the value provided by the pod spec. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). This is a beta field and requires enabling ProbeTerminationGracePeriod feature gate. Minimum value is 1. spec.terminationGracePeriodSeconds is used if unset.   
`timeoutSeconds` |  `integer` |  Number of seconds after which the probe times out. Defaults to 1 second. Minimum value is 1. More info: <https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle#container-probes>  
Show more

## 2.1.282. .spec.initContainers[].startupProbe.exec

Description
     Exec specifies a command to execute in the container. 
Type
     `object`

Property| Type| Description  
---|---|---  
`command` |  `array (string)` |  Command is the command line to execute inside the container, the working directory for the command is root ('/') in the container’s filesystem. The command is simply exec’d, it is not run inside a shell, so traditional shell instructions ('|', etc) won’t work. To use a shell, you need to explicitly call out to that shell. Exit status of 0 is treated as live/healthy and non-zero is unhealthy.   
Show more

## 2.1.283. .spec.initContainers[].startupProbe.grpc

Description
     GRPC specifies a GRPC HealthCheckRequest. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`port` |  `integer` |  Port number of the gRPC service. Number must be in the range 1 to 65535.   
`service` |  `string` |  Service is the name of the service to place in the gRPC HealthCheckRequest (see <https://github.com/grpc/grpc/blob/master/doc/health-checking.md>).  If this is not specified, the default behavior is defined by gRPC.   
Show more

## 2.1.284. .spec.initContainers[].startupProbe.httpGet

Description
     HTTPGet specifies an HTTP GET request to perform. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Host name to connect to, defaults to the pod IP. You probably want to set "Host" in httpHeaders instead.   
`httpHeaders` |  `array` |  Custom headers to set in the request. HTTP allows repeated headers.   
`httpHeaders[]` |  `object` |  HTTPHeader describes a custom header to be used in HTTP probes   
`path` |  `string` |  Path to access on the HTTP server.   
`port` |  `integer-or-string` |  Name or number of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
`scheme` |  `string` |  Scheme to use for connecting to the host. Defaults to HTTP.   
Show more

## 2.1.285. .spec.initContainers[].startupProbe.httpGet.httpHeaders

Description
     Custom headers to set in the request. HTTP allows repeated headers. 
Type
     `array`

## 2.1.286. .spec.initContainers[].startupProbe.httpGet.httpHeaders[]

Description
     HTTPHeader describes a custom header to be used in HTTP probes 
Type
     `object`
Required
    

  * `name`
  * `value`



Property| Type| Description  
---|---|---  
`name` |  `string` |  The header field name. This will be canonicalized upon output, so case-variant names will be understood as the same header.   
`value` |  `string` |  The header field value   
Show more

## 2.1.287. .spec.initContainers[].startupProbe.tcpSocket

Description
     TCPSocket specifies a connection to a TCP port. 
Type
     `object`
Required
    

  * `port`



Property| Type| Description  
---|---|---  
`host` |  `string` |  Optional: Host name to connect to, defaults to the pod IP.   
`port` |  `integer-or-string` |  Number or name of the port to access on the container. Number must be in the range 1 to 65535. Name must be an IANA_SVC_NAME.   
Show more

## 2.1.288. .spec.initContainers[].volumeDevices

Description
     volumeDevices is the list of block devices to be used by the container. 
Type
     `array`

## 2.1.289. .spec.initContainers[].volumeDevices[]

Description
     volumeDevice describes a mapping of a raw block device within a container. 
Type
     `object`
Required
    

  * `devicePath`
  * `name`



Property| Type| Description  
---|---|---  
`devicePath` |  `string` |  devicePath is the path inside of the container that the device will be mapped to.   
`name` |  `string` |  name must match the name of a persistentVolumeClaim in the pod   
Show more

## 2.1.290. .spec.initContainers[].volumeMounts

Description
     Pod volumes to mount into the container’s filesystem. Cannot be updated. 
Type
     `array`

## 2.1.291. .spec.initContainers[].volumeMounts[]

Description
     VolumeMount describes a mounting of a Volume within a container. 
Type
     `object`
Required
    

  * `mountPath`
  * `name`



Property| Type| Description  
---|---|---  
`mountPath` |  `string` |  Path within the container at which the volume should be mounted. Must not contain ':'.   
`mountPropagation` |  `string` |  mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).   
`name` |  `string` |  This must match the Name of a Volume.   
`readOnly` |  `boolean` |  Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.   
`recursiveReadOnly` |  `string` |  RecursiveReadOnly specifies whether read-only mounts should be handled recursively.  If ReadOnly is false, this field has no meaning and must be unspecified.  If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.  If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).  If this field is not specified, it is treated as an equivalent of Disabled.   
`subPath` |  `string` |  Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root).   
`subPathExpr` |  `string` |  Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive.   
Show more

## 2.1.292. .spec.limits

Description
     limits defines the limits command line flags when starting Alertmanager. 
Type
     `object`

Property| Type| Description  
---|---|---  
`maxPerSilenceBytes` |  `string` |  maxPerSilenceBytes defines the maximum size of an individual silence as stored on disk. This corresponds to the Alertmanager’s `--silences.max-per-silence-bytes` flag. It requires Alertmanager >= v0.28.0.   
`maxSilences` |  `integer` |  maxSilences defines the maximum number active and pending silences. This corresponds to the Alertmanager’s `--silences.max-silences` flag. It requires Alertmanager >= v0.28.0.   
Show more

## 2.1.293. .spec.persistentVolumeClaimRetentionPolicy

Description
     persistentVolumeClaimRetentionPolicy controls if and how PVCs are deleted during the lifecycle of a StatefulSet. The default behavior is all PVCs are retained. This is an alpha field from kubernetes 1.23 until 1.26 and a beta field from 1.26. It requires enabling the StatefulSetAutoDeletePVC feature gate. 
Type
     `object`

Property| Type| Description  
---|---|---  
`whenDeleted` |  `string` |  WhenDeleted specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is deleted. The default policy of `Retain` causes PVCs to not be affected by StatefulSet deletion. The `Delete` policy causes those PVCs to be deleted.   
`whenScaled` |  `string` |  WhenScaled specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is scaled down. The default policy of `Retain` causes PVCs to not be affected by a scaledown. The `Delete` policy causes the associated PVCs for any excess pods above the replica count to be deleted.   
Show more

## 2.1.294. .spec.podMetadata

Description
    

podMetadata defines labels and annotations which are propagated to the Alertmanager pods. 

The following items are reserved and cannot be overridden: * "alertmanager" label, set to the name of the Alertmanager instance. * "app.kubernetes.io/instance" label, set to the name of the Alertmanager instance. * "app.kubernetes.io/managed-by" label, set to "prometheus-operator". * "app.kubernetes.io/name" label, set to "alertmanager". * "app.kubernetes.io/version" label, set to the Alertmanager version. * "kubectl.kubernetes.io/default-container" annotation, set to "alertmanager". 

Type
     `object`

Property| Type| Description  
---|---|---  
`annotations` |  `object (string)` |  annotations defines an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/>  
`labels` |  `object (string)` |  labels define the map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>  
`name` |  `string` |  name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/>  
Show more

## 2.1.295. .spec.resources

Description
     resources defines the resource requests and limits of the Pods. 
Type
     `object`

Property| Type| Description  
---|---|---  
`claims` |  `array` |  Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.  This field depends on the DynamicResourceAllocation feature gate.  This field is immutable. It can only be set for containers.   
`claims[]` |  `object` |  ResourceClaim references one entry in PodSpec.ResourceClaims.   
`limits` |  `integer-or-string` |  Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
`requests` |  `integer-or-string` |  Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
Show more

## 2.1.296. .spec.resources.claims

Description
    

Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container. 

This field depends on the DynamicResourceAllocation feature gate. 

This field is immutable. It can only be set for containers. 

Type
     `array`

## 2.1.297. .spec.resources.claims[]

Description
     ResourceClaim references one entry in PodSpec.ResourceClaims. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  Name must match the name of one entry in pod.spec.resourceClaims of the Pod where this field is used. It makes that resource available inside a container.   
`request` |  `string` |  Request is the name chosen for a request in the referenced claim. If empty, everything from the claim is made available, otherwise only the result of this request.   
Show more

## 2.1.298. .spec.securityContext

Description
     securityContext holds pod-level security attributes and common container settings. This defaults to the default PodSecurityContext. 
Type
     `object`

Property| Type| Description  
---|---|---  
`appArmorProfile` |  `object` |  appArmorProfile is the AppArmor options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.   
`fsGroup` |  `integer` |  A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:  1\. The owning GID will be the FSGroup 2. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3. The permission bits are OR’d with rw-rw----  If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.   
`fsGroupChangePolicy` |  `string` |  fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows.   
`runAsGroup` |  `integer` |  The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.   
`runAsNonRoot` |  `boolean` |  Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.   
`runAsUser` |  `integer` |  The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.   
`seLinuxChangePolicy` |  `string` |  seLinuxChangePolicy defines how the container’s SELinux label is applied to all volumes used by the Pod. It has no effect on nodes that do not support SELinux or to volumes does not support SELinux. Valid values are "MountOption" and "Recursive".  "Recursive" means relabeling of all files on all Pod volumes by the container runtime. This may be slow for large volumes, but allows mixing privileged and unprivileged Pods sharing the same volume on the same node.  "MountOption" mounts all eligible Pod volumes with `-o context` mount option. This requires all Pods that share the same volume to use the same SELinux label. It is not possible to share the same volume among privileged and unprivileged Pods. Eligible volumes are in-tree FibreChannel and iSCSI volumes, and all CSI volumes whose CSI driver announces SELinux support by setting spec.seLinuxMount: true in their CSIDriver instance. Other volumes are always re-labelled recursively. "MountOption" value is allowed only when SELinuxMount feature gate is enabled.  If not specified and SELinuxMount feature gate is enabled, "MountOption" is used. If not specified and SELinuxMount feature gate is disabled, "MountOption" is used for ReadWriteOncePod volumes and "Recursive" for all other volumes.  This field affects only Pods that have SELinux label set, either in PodSecurityContext or in SecurityContext of all containers.  All Pods that use the same volume should use the same seLinuxChangePolicy, otherwise some pods can get stuck in ContainerCreating state. Note that this field cannot be set when spec.os.name is windows.   
`seLinuxOptions` |  `object` |  The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.   
`seccompProfile` |  `object` |  The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.   
`supplementalGroups` |  `array (integer)` |  A list of groups applied to the first process run in each container, in addition to the container’s primary GID and fsGroup (if specified). If the SupplementalGroupsPolicy feature is enabled, the supplementalGroupsPolicy field determines whether these are in addition to or instead of any group memberships defined in the container image. If unspecified, no additional groups are added, though group memberships defined in the container image may still be used, depending on the supplementalGroupsPolicy field. Note that this field cannot be set when spec.os.name is windows.   
`supplementalGroupsPolicy` |  `string` |  Defines how supplemental groups of the first container processes are calculated. Valid values are "Merge" and "Strict". If not specified, "Merge" is used. (Alpha) Using the field requires the SupplementalGroupsPolicy feature gate to be enabled and the container runtime must implement support for this feature. Note that this field cannot be set when spec.os.name is windows.   
`sysctls` |  `array` |  Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.   
`sysctls[]` |  `object` |  Sysctl defines a kernel parameter to be set   
`windowsOptions` |  `object` |  The Windows specific settings applied to all containers. If unspecified, the options within a container’s SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.   
Show more

## 2.1.299. .spec.securityContext.appArmorProfile

Description
     appArmorProfile is the AppArmor options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`localhostProfile` |  `string` |  localhostProfile indicates a profile loaded on the node that should be used. The profile must be preconfigured on the node to work. Must match the loaded name of the profile. Must be set if and only if type is "Localhost".   
`type` |  `string` |  type indicates which kind of AppArmor profile will be applied. Valid options are: Localhost - a profile pre-loaded on the node. RuntimeDefault - the container runtime’s default profile. Unconfined - no AppArmor enforcement.   
Show more

## 2.1.300. .spec.securityContext.seLinuxOptions

Description
     The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows. 
Type
     `object`

Property| Type| Description  
---|---|---  
`level` |  `string` |  Level is SELinux level label that applies to the container.   
`role` |  `string` |  Role is a SELinux role label that applies to the container.   
`type` |  `string` |  Type is a SELinux type label that applies to the container.   
`user` |  `string` |  User is a SELinux user label that applies to the container.   
Show more

## 2.1.301. .spec.securityContext.seccompProfile

Description
     The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows. 
Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`localhostProfile` |  `string` |  localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.   
`type` |  `string` |  type indicates which kind of seccomp profile will be applied. Valid options are:  Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.   
Show more

## 2.1.302. .spec.securityContext.sysctls

Description
     Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows. 
Type
     `array`

## 2.1.303. .spec.securityContext.sysctls[]

Description
     Sysctl defines a kernel parameter to be set 
Type
     `object`
Required
    

  * `name`
  * `value`



Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of a property to set   
`value` |  `string` |  Value of a property to set   
Show more

## 2.1.304. .spec.securityContext.windowsOptions

Description
     The Windows specific settings applied to all containers. If unspecified, the options within a container’s SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux. 
Type
     `object`

Property| Type| Description  
---|---|---  
`gmsaCredentialSpec` |  `string` |  GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.   
`gmsaCredentialSpecName` |  `string` |  GMSACredentialSpecName is the name of the GMSA credential spec to use.   
`hostProcess` |  `boolean` |  HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true.   
`runAsUserName` |  `string` |  The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.   
Show more

## 2.1.305. .spec.storage

Description
     storage defines the definition of how storage will be used by the Alertmanager instances. 
Type
     `object`

Property| Type| Description  
---|---|---  
`disableMountSubPath` |  `boolean` |  disableMountSubPath deprecated: subPath usage will be removed in a future release.   
`emptyDir` |  `object` |  emptyDir to be used by the StatefulSet. If specified, it takes precedence over `ephemeral` and `volumeClaimTemplate`. More info: <https://kubernetes.io/docs/concepts/storage/volumes/#emptydir>  
`ephemeral` |  `object` |  ephemeral to be used by the StatefulSet. This is a beta field in k8s 1.21 and GA in 1.15. For lower versions, starting with k8s 1.19, it requires enabling the GenericEphemeralVolume feature gate. More info: <https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes>  
`volumeClaimTemplate` |  `object` |  volumeClaimTemplate defines the PVC spec to be used by the Prometheus StatefulSets. The easiest way to use a volume that cannot be automatically provisioned is to use a label selector alongside manually created PersistentVolumes.   
Show more

## 2.1.306. .spec.storage.emptyDir

Description
     emptyDir to be used by the StatefulSet. If specified, it takes precedence over `ephemeral` and `volumeClaimTemplate`. More info: <https://kubernetes.io/docs/concepts/storage/volumes/#emptydir>
Type
     `object`

Property| Type| Description  
---|---|---  
`medium` |  `string` |  medium represents what type of storage medium should back this directory. The default is "" which means to use the node’s default medium. Must be an empty string (default) or Memory. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir>  
`sizeLimit` |  `integer-or-string` |  sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir>  
Show more

## 2.1.307. .spec.storage.ephemeral

Description
     ephemeral to be used by the StatefulSet. This is a beta field in k8s 1.21 and GA in 1.15. For lower versions, starting with k8s 1.19, it requires enabling the GenericEphemeralVolume feature gate. More info: <https://kubernetes.io/docs/concepts/storage/ephemeral-volumes/#generic-ephemeral-volumes>
Type
     `object`

Property| Type| Description  
---|---|---  
`volumeClaimTemplate` |  `object` |  Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod. The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long).  An existing PVC with that name that is not owned by the pod will **not** be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster.  This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created.  Required, must not be nil.   
Show more

## 2.1.308. .spec.storage.ephemeral.volumeClaimTemplate

Description
    

Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod. The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long). 

An existing PVC with that name that is not owned by the pod will **not** be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster. 

This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created. 

Required, must not be nil. 

Type
     `object`
Required
    

  * `spec`



Property| Type| Description  
---|---|---  
`metadata` |  `object` |  May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation.   
`spec` |  `object` |  The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here.   
Show more

## 2.1.309. .spec.storage.ephemeral.volumeClaimTemplate.metadata

Description
     May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. 
Type
     `object`

## 2.1.310. .spec.storage.ephemeral.volumeClaimTemplate.spec

Description
     The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here. 
Type
     `object`

Property| Type| Description  
---|---|---  
`accessModes` |  `array (string)` |  accessModes contains the desired access modes the volume should have. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1>  
`dataSource` |  `object` |  dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource.   
`dataSourceRef` |  `object` |  dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn’t specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn’t set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef preserves all values, and generates an error if a disallowed value is specified. * While dataSource only allows local objects, dataSourceRef allows objects in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.   
`resources` |  `object` |  resources represents the minimum resources the volume should have. Users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources>  
`selector` |  `object` |  selector is a label query over volumes to consider for binding.   
`storageClassName` |  `string` |  storageClassName is the name of the StorageClass required by the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1>  
`volumeAttributesClassName` |  `string` |  volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string or nil value indicates that no VolumeAttributesClass will be applied to the claim. If the claim enters an Infeasible error state, this field can be reset to its previous value (including nil) to cancel the modification. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: <https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/>  
`volumeMode` |  `string` |  volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.   
`volumeName` |  `string` |  volumeName is the binding reference to the PersistentVolume backing this claim.   
Show more

## 2.1.311. .spec.storage.ephemeral.volumeClaimTemplate.spec.dataSource

Description
     dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  Kind is the type of resource being referenced   
`name` |  `string` |  Name is the name of resource being referenced   
Show more

## 2.1.312. .spec.storage.ephemeral.volumeClaimTemplate.spec.dataSourceRef

Description
     dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn’t specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn’t set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef preserves all values, and generates an error if a disallowed value is specified. * While dataSource only allows local objects, dataSourceRef allows objects in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  Kind is the type of resource being referenced   
`name` |  `string` |  Name is the name of resource being referenced   
`namespace` |  `string` |  Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled.   
Show more

## 2.1.313. .spec.storage.ephemeral.volumeClaimTemplate.spec.resources

Description
     resources represents the minimum resources the volume should have. Users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources>
Type
     `object`

Property| Type| Description  
---|---|---  
`limits` |  `integer-or-string` |  Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
`requests` |  `integer-or-string` |  Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
Show more

## 2.1.314. .spec.storage.ephemeral.volumeClaimTemplate.spec.selector

Description
     selector is a label query over volumes to consider for binding. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.315. .spec.storage.ephemeral.volumeClaimTemplate.spec.selector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.316. .spec.storage.ephemeral.volumeClaimTemplate.spec.selector.matchExpressions[]

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

## 2.1.317. .spec.storage.volumeClaimTemplate

Description
     volumeClaimTemplate defines the PVC spec to be used by the Prometheus StatefulSets. The easiest way to use a volume that cannot be automatically provisioned is to use a label selector alongside manually created PersistentVolumes. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  `object` |  metadata defines EmbeddedMetadata contains metadata relevant to an EmbeddedResource.   
`spec` |  `object` |  spec defines the specification of the characteristics of a volume requested by a pod author. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims>  
`status` |  `object` |  status is deprecated: this field is never set.   
Show more

## 2.1.318. .spec.storage.volumeClaimTemplate.metadata

Description
     metadata defines EmbeddedMetadata contains metadata relevant to an EmbeddedResource. 
Type
     `object`

Property| Type| Description  
---|---|---  
`annotations` |  `object (string)` |  annotations defines an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/>  
`labels` |  `object (string)` |  labels define the map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>  
`name` |  `string` |  name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/>  
Show more

## 2.1.319. .spec.storage.volumeClaimTemplate.spec

Description
     spec defines the specification of the characteristics of a volume requested by a pod author. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims>
Type
     `object`

Property| Type| Description  
---|---|---  
`accessModes` |  `array (string)` |  accessModes contains the desired access modes the volume should have. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1>  
`dataSource` |  `object` |  dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource.   
`dataSourceRef` |  `object` |  dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn’t specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn’t set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef preserves all values, and generates an error if a disallowed value is specified. * While dataSource only allows local objects, dataSourceRef allows objects in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.   
`resources` |  `object` |  resources represents the minimum resources the volume should have. Users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources>  
`selector` |  `object` |  selector is a label query over volumes to consider for binding.   
`storageClassName` |  `string` |  storageClassName is the name of the StorageClass required by the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1>  
`volumeAttributesClassName` |  `string` |  volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string or nil value indicates that no VolumeAttributesClass will be applied to the claim. If the claim enters an Infeasible error state, this field can be reset to its previous value (including nil) to cancel the modification. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: <https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/>  
`volumeMode` |  `string` |  volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.   
`volumeName` |  `string` |  volumeName is the binding reference to the PersistentVolume backing this claim.   
Show more

## 2.1.320. .spec.storage.volumeClaimTemplate.spec.dataSource

Description
     dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  Kind is the type of resource being referenced   
`name` |  `string` |  Name is the name of resource being referenced   
Show more

## 2.1.321. .spec.storage.volumeClaimTemplate.spec.dataSourceRef

Description
     dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn’t specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn’t set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef preserves all values, and generates an error if a disallowed value is specified. * While dataSource only allows local objects, dataSourceRef allows objects in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  Kind is the type of resource being referenced   
`name` |  `string` |  Name is the name of resource being referenced   
`namespace` |  `string` |  Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled.   
Show more

## 2.1.322. .spec.storage.volumeClaimTemplate.spec.resources

Description
     resources represents the minimum resources the volume should have. Users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources>
Type
     `object`

Property| Type| Description  
---|---|---  
`limits` |  `integer-or-string` |  Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
`requests` |  `integer-or-string` |  Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
Show more

## 2.1.323. .spec.storage.volumeClaimTemplate.spec.selector

Description
     selector is a label query over volumes to consider for binding. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.324. .spec.storage.volumeClaimTemplate.spec.selector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.325. .spec.storage.volumeClaimTemplate.spec.selector.matchExpressions[]

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

## 2.1.326. .spec.storage.volumeClaimTemplate.status

Description
     status is deprecated: this field is never set. 
Type
     `object`

Property| Type| Description  
---|---|---  
`accessModes` |  `array (string)` |  accessModes contains the actual access modes the volume backing the PVC has. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1>  
`allocatedResourceStatuses` |  `object (string)` |  allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either: * Un-prefixed keys: - storage - the capacity of the volume. * Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  ClaimResourceStatus can be in any of following states: - ControllerResizeInProgress: State set when resize controller starts resizing the volume in control-plane. - ControllerResizeFailed: State set when resize has failed in resize controller with a terminal error. - NodeResizePending: State set when resize controller has finished resizing the volume but further resizing of volume is needed on the node. - NodeResizeInProgress: State set when kubelet starts resizing the volume. - NodeResizeFailed: State set when resizing has failed in kubelet with a terminal error. Transient errors don’t set NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states: - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeFailed" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizePending" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeFailed" When this field is not set, it means that no resize operation is in progress for the given PVC.  A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.   
`allocatedResources` |  `integer-or-string` |  allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either: * Un-prefixed keys: - storage - the capacity of the volume. * Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.  Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.  A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.   
`capacity` |  `integer-or-string` |  capacity represents the actual resources of the underlying volume.   
`conditions` |  `array` |  conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'.   
`conditions[]` |  `object` |  PersistentVolumeClaimCondition contains details about state of pvc   
`currentVolumeAttributesClassName` |  `string` |  currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim   
`modifyVolumeStatus` |  `object` |  ModifyVolumeStatus represents the status object of ControllerModifyVolume operation. When this is unset, there is no ModifyVolume operation being attempted.   
`phase` |  `string` |  phase represents the current phase of PersistentVolumeClaim.   
Show more

## 2.1.327. .spec.storage.volumeClaimTemplate.status.conditions

Description
     conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'. 
Type
     `array`

## 2.1.328. .spec.storage.volumeClaimTemplate.status.conditions[]

Description
     PersistentVolumeClaimCondition contains details about state of pvc 
Type
     `object`
Required
    

  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastProbeTime` |  `string` |  lastProbeTime is the time we probed the condition.   
`lastTransitionTime` |  `string` |  lastTransitionTime is the time the condition transitioned from one status to another.   
`message` |  `string` |  message is the human-readable message indicating details about last transition.   
`reason` |  `string` |  reason is a unique, this should be a short, machine understandable string that gives the reason for condition’s last transition. If it reports "Resizing" that means the underlying persistent volume is being resized.   
`status` |  `string` |  Status is the status of the condition. Can be True, False, Unknown. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=state%20of%20pvc-,conditions.status,-(string)%2C%20required>  
`type` |  `string` |  Type is the type of the condition. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=set%20to%20%27ResizeStarted%27.-,PersistentVolumeClaimCondition,-contains%20details%20about>  
Show more

## 2.1.329. .spec.storage.volumeClaimTemplate.status.modifyVolumeStatus

Description
     ModifyVolumeStatus represents the status object of ControllerModifyVolume operation. When this is unset, there is no ModifyVolume operation being attempted. 
Type
     `object`
Required
    

  * `status`



Property| Type| Description  
---|---|---  
`status` |  `string` |  status is the status of the ControllerModifyVolume operation. It can be in any of following states: - Pending Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as the specified VolumeAttributesClass not existing. - InProgress InProgress indicates that the volume is being modified. - Infeasible Infeasible indicates that the request has been rejected as invalid by the CSI driver. To resolve the error, a valid VolumeAttributesClass needs to be specified. Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.   
`targetVolumeAttributesClassName` |  `string` |  targetVolumeAttributesClassName is the name of the VolumeAttributesClass the PVC currently being reconciled   
Show more

## 2.1.330. .spec.tolerations

Description
     tolerations defines the pod’s tolerations. 
Type
     `array`

## 2.1.331. .spec.tolerations[]

Description
     The pod this Toleration is attached to tolerates any taint that matches the triple <key,value,effect> using the matching operator <operator>. 
Type
     `object`

Property| Type| Description  
---|---|---  
`effect` |  `string` |  Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.   
`key` |  `string` |  Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.   
`operator` |  `string` |  Operator represents a key’s relationship to the value. Valid operators are Exists, Equal, Lt, and Gt. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category. Lt and Gt perform numeric comparisons (requires feature gate TaintTolerationComparisonOperators).   
`tolerationSeconds` |  `integer` |  TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.   
`value` |  `string` |  Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.   
Show more

## 2.1.332. .spec.topologySpreadConstraints

Description
     topologySpreadConstraints defines the Pod’s topology spread constraints. 
Type
     `array`

## 2.1.333. .spec.topologySpreadConstraints[]

Description
     TopologySpreadConstraint specifies how to spread matching pods among the given topology. 
Type
     `object`
Required
    

  * `maxSkew`
  * `topologyKey`
  * `whenUnsatisfiable`



Property| Type| Description  
---|---|---  
`labelSelector` |  `object` |  LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain.   
`matchLabelKeys` |  `array (string)` |  MatchLabelKeys is a set of pod label keys to select the pods over which spreading will be calculated. The keys are used to lookup values from the incoming pod labels, those key-value labels are ANDed with labelSelector to select the group of existing pods over which spreading will be calculated for the incoming pod. The same key is forbidden to exist in both MatchLabelKeys and LabelSelector. MatchLabelKeys cannot be set when LabelSelector isn’t set. Keys that don’t exist in the incoming pod labels will be ignored. A null or empty list means only match against labelSelector.  This is a beta field and requires the MatchLabelKeysInPodTopologySpread feature gate to be enabled (enabled by default).   
`maxSkew` |  `integer` |  MaxSkew describes the degree to which pods may be unevenly distributed. When `whenUnsatisfiable=DoNotSchedule`, it is the maximum permitted difference between the number of matching pods in the target topology and the global minimum. The global minimum is the minimum number of matching pods in an eligible domain or zero if the number of eligible domains is less than MinDomains. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 2/2/1: In this case, the global minimum is 1. | zone1 | zone2 | zone3 | | P P | P P | P | - if MaxSkew is 1, incoming pod can only be scheduled to zone3 to become 2/2/2; scheduling it onto zone1(zone2) would make the ActualSkew(3-1) on zone1(zone2) violate MaxSkew(1). - if MaxSkew is 2, incoming pod can be scheduled onto any zone. When `whenUnsatisfiable=ScheduleAnyway`, it is used to give higher precedence to topologies that satisfy it. It’s a required field. Default value is 1 and 0 is not allowed.   
`minDomains` |  `integer` |  MinDomains indicates a minimum number of eligible domains. When the number of eligible domains with matching topology keys is less than minDomains, Pod Topology Spread treats "global minimum" as 0, and then the calculation of Skew is performed. And when the number of eligible domains with matching topology keys equals or greater than minDomains, this value has no effect on scheduling. As a result, when the number of eligible domains is less than minDomains, scheduler won’t schedule more than maxSkew Pods to those domains. If value is nil, the constraint behaves as if MinDomains is equal to 1. Valid values are integers greater than 0. When value is not nil, WhenUnsatisfiable must be DoNotSchedule.  For example, in a 3-zone cluster, MaxSkew is set to 2, MinDomains is set to 5 and pods with the same labelSelector spread as 2/2/2: | zone1 | zone2 | zone3 | | P P | P P | P P | The number of domains is less than 5(MinDomains), so "global minimum" is treated as 0. In this situation, new pod with the same labelSelector cannot be scheduled, because computed skew will be 3(3 - 0) if new Pod is scheduled to any of the three zones, it will violate MaxSkew.   
`nodeAffinityPolicy` |  `string` |  NodeAffinityPolicy indicates how we will treat Pod’s nodeAffinity/nodeSelector when calculating pod topology spread skew. Options are: - Honor: only nodes matching nodeAffinity/nodeSelector are included in the calculations. - Ignore: nodeAffinity/nodeSelector are ignored. All nodes are included in the calculations.  If this value is nil, the behavior is equivalent to the Honor policy.   
`nodeTaintsPolicy` |  `string` |  NodeTaintsPolicy indicates how we will treat node taints when calculating pod topology spread skew. Options are: - Honor: nodes without taints, along with tainted nodes for which the incoming pod has a toleration, are included. - Ignore: node taints are ignored. All nodes are included.  If this value is nil, the behavior is equivalent to the Ignore policy.   
`topologyKey` |  `string` |  TopologyKey is the key of node labels. Nodes that have a label with this key and identical values are considered to be in the same topology. We consider each <key, value> as a "bucket", and try to put balanced number of pods into each bucket. We define a domain as a particular instance of a topology. Also, we define an eligible domain as a domain whose nodes meet the requirements of nodeAffinityPolicy and nodeTaintsPolicy. e.g. If TopologyKey is "kubernetes.io/hostname", each Node is a domain of that topology. And, if TopologyKey is "topology.kubernetes.io/zone", each zone is a domain of that topology. It’s a required field.   
`whenUnsatisfiable` |  `string` |  WhenUnsatisfiable indicates how to deal with a pod if it doesn’t satisfy the spread constraint. - DoNotSchedule (default) tells the scheduler not to schedule it. - ScheduleAnyway tells the scheduler to schedule the pod in any location, but giving higher precedence to topologies that would help reduce the skew. A constraint is considered "Unsatisfiable" for an incoming pod if and only if every possible node assignment for that pod would violate "MaxSkew" on some topology. For example, in a 3-zone cluster, MaxSkew is set to 1, and pods with the same labelSelector spread as 3/1/1: | zone1 | zone2 | zone3 | | P P P | P | P | If WhenUnsatisfiable is set to DoNotSchedule, incoming pod can only be scheduled to zone2(zone3) to become 3/2/1(3/1/2) as ActualSkew(2-1) on zone2(zone3) satisfies MaxSkew(1). In other words, the cluster can still be imbalanced, but scheduler won’t make it **more** imbalanced. It’s a required field.   
Show more

## 2.1.334. .spec.topologySpreadConstraints[].labelSelector

Description
     LabelSelector is used to find matching pods. Pods that match this label selector are counted to determine the number of pods in their corresponding topology domain. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.335. .spec.topologySpreadConstraints[].labelSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.336. .spec.topologySpreadConstraints[].labelSelector.matchExpressions[]

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

## 2.1.337. .spec.updateStrategy

Description
    

updateStrategy indicates the strategy that will be employed to update Pods in the StatefulSet when a revision is made to statefulset’s Pod Template. 

The default strategy is RollingUpdate. 

Type
     `object`
Required
    

  * `type`



Property| Type| Description  
---|---|---  
`rollingUpdate` |  `object` |  rollingUpdate is used to communicate parameters when type is RollingUpdate.   
`type` |  `string` |  type indicates the type of the StatefulSetUpdateStrategy.  Default is RollingUpdate.   
Show more

## 2.1.338. .spec.updateStrategy.rollingUpdate

Description
     rollingUpdate is used to communicate parameters when type is RollingUpdate. 
Type
     `object`

Property| Type| Description  
---|---|---  
`maxUnavailable` |  `integer-or-string` |  maxUnavailable is the maximum number of pods that can be unavailable during the update. The value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0. Defaults to 1. This field is alpha-level and is only honored by servers that enable the MaxUnavailableStatefulSet feature. The field applies to all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0 to Replicas-1, it will be counted towards MaxUnavailable.   
Show more

## 2.1.339. .spec.volumeMounts

Description
     volumeMounts allows configuration of additional VolumeMounts on the output StatefulSet definition. VolumeMounts specified will be appended to other VolumeMounts in the alertmanager container, that are generated as a result of StorageSpec objects. 
Type
     `array`

## 2.1.340. .spec.volumeMounts[]

Description
     VolumeMount describes a mounting of a Volume within a container. 
Type
     `object`
Required
    

  * `mountPath`
  * `name`



Property| Type| Description  
---|---|---  
`mountPath` |  `string` |  Path within the container at which the volume should be mounted. Must not contain ':'.   
`mountPropagation` |  `string` |  mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).   
`name` |  `string` |  This must match the Name of a Volume.   
`readOnly` |  `boolean` |  Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.   
`recursiveReadOnly` |  `string` |  RecursiveReadOnly specifies whether read-only mounts should be handled recursively.  If ReadOnly is false, this field has no meaning and must be unspecified.  If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only. If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime. If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.  If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).  If this field is not specified, it is treated as an equivalent of Disabled.   
`subPath` |  `string` |  Path within the volume from which the container’s volume should be mounted. Defaults to "" (volume’s root).   
`subPathExpr` |  `string` |  Expanded path within the volume from which the container’s volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container’s environment. Defaults to "" (volume’s root). SubPathExpr and SubPath are mutually exclusive.   
Show more

## 2.1.341. .spec.volumes

Description
     volumes allows configuration of additional volumes on the output StatefulSet definition. Volumes specified will be appended to other volumes that are generated as a result of StorageSpec objects. 
Type
     `array`

## 2.1.342. .spec.volumes[]

Description
     Volume represents a named volume in a pod that may be accessed by any container in the pod. 
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`awsElasticBlockStore` |  `object` |  awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Deprecated: AWSElasticBlockStore is deprecated. All operations for the in-tree awsElasticBlockStore type are redirected to the ebs.csi.aws.com CSI driver. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore>  
`azureDisk` |  `object` |  azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. Deprecated: AzureDisk is deprecated. All operations for the in-tree azureDisk type are redirected to the disk.csi.azure.com CSI driver.   
`azureFile` |  `object` |  azureFile represents an Azure File Service mount on the host and bind mount to the pod. Deprecated: AzureFile is deprecated. All operations for the in-tree azureFile type are redirected to the file.csi.azure.com CSI driver.   
`cephfs` |  `object` |  cephFS represents a Ceph FS mount on the host that shares a pod’s lifetime. Deprecated: CephFS is deprecated and the in-tree cephfs type is no longer supported.   
`cinder` |  `object` |  cinder represents a cinder volume attached and mounted on kubelets host machine. Deprecated: Cinder is deprecated. All operations for the in-tree cinder type are redirected to the cinder.csi.openstack.org CSI driver. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md>  
`configMap` |  `object` |  configMap represents a configMap that should populate this volume   
`csi` |  `object` |  csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers.   
`downwardAPI` |  `object` |  downwardAPI represents downward API about the pod that should populate this volume   
`emptyDir` |  `object` |  emptyDir represents a temporary directory that shares a pod’s lifetime. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir>  
`ephemeral` |  `object` |  ephemeral represents a volume that is handled by a cluster storage driver. The volume’s lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed.  Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity tracking are needed, c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through a PersistentVolumeClaim (see EphemeralVolumeSource for more information on the connection between this volume type and PersistentVolumeClaim).  Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod.  Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information.  A pod can use both types of ephemeral volumes and persistent volumes at the same time.   
`fc` |  `object` |  fc represents a Fibre Channel resource that is attached to a kubelet’s host machine and then exposed to the pod.   
`flexVolume` |  `object` |  flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. Deprecated: FlexVolume is deprecated. Consider using a CSIDriver instead.   
`flocker` |  `object` |  flocker represents a Flocker volume attached to a kubelet’s host machine. This depends on the Flocker control service being running. Deprecated: Flocker is deprecated and the in-tree flocker type is no longer supported.   
`gcePersistentDisk` |  `object` |  gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Deprecated: GCEPersistentDisk is deprecated. All operations for the in-tree gcePersistentDisk type are redirected to the pd.csi.storage.gke.io CSI driver. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk>  
`gitRepo` |  `object` |  gitRepo represents a git repository at a particular revision. Deprecated: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod’s container.   
`glusterfs` |  `object` |  glusterfs represents a Glusterfs mount on the host that shares a pod’s lifetime. Deprecated: Glusterfs is deprecated and the in-tree glusterfs type is no longer supported.   
`hostPath` |  `object` |  hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath>  
`image` |  `object` |  image represents an OCI object (a container image or artifact) pulled and mounted on the kubelet’s host machine. The volume is resolved at pod startup depending on which PullPolicy value is provided:  \- Always: the kubelet always attempts to pull the reference. Container creation will fail If the pull fails. - Never: the kubelet never pulls the reference and only uses a local image or artifact. Container creation will fail if the reference isn’t present. - IfNotPresent: the kubelet pulls if the reference isn’t already present on disk. Container creation will fail if the reference isn’t present and the pull fails.  The volume gets re-resolved if the pod gets deleted and recreated, which means that new remote content will become available on pod recreation. A failure to resolve or pull the image during pod startup will block containers from starting and may add significant latency. Failures will be retried using normal volume backoff and will be reported on the pod reason and message. The types of objects that may be mounted by this volume are defined by the container runtime implementation on a host machine and at minimum must include all valid types supported by the container image field. The OCI object gets mounted in a single directory (spec.containers[**].volumeMounts.mountPath) by merging the manifest layers in the same way as for container images. The volume will be mounted read-only (ro) and non-executable files (noexec). Sub path mounts for containers are not supported (spec.containers[**].volumeMounts.subpath) before 1.33. The field spec.securityContext.fsGroupChangePolicy has no effect on this volume type.   
`iscsi` |  `object` |  iscsi represents an ISCSI Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. More info: <https://kubernetes.io/docs/concepts/storage/volumes/#iscsi>  
`name` |  `string` |  name of the volume. Must be a DNS_LABEL and unique within the pod. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`nfs` |  `object` |  nfs represents an NFS mount on the host that shares a pod’s lifetime More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs>  
`persistentVolumeClaim` |  `object` |  persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims>  
`photonPersistentDisk` |  `object` |  photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine. Deprecated: PhotonPersistentDisk is deprecated and the in-tree photonPersistentDisk type is no longer supported.   
`portworxVolume` |  `object` |  portworxVolume represents a portworx volume attached and mounted on kubelets host machine. Deprecated: PortworxVolume is deprecated. All operations for the in-tree portworxVolume type are redirected to the pxd.portworx.com CSI driver when the CSIMigrationPortworx feature-gate is on.   
`projected` |  `object` |  projected items for all in one resources secrets, configmaps, and downward API   
`quobyte` |  `object` |  quobyte represents a Quobyte mount on the host that shares a pod’s lifetime. Deprecated: Quobyte is deprecated and the in-tree quobyte type is no longer supported.   
`rbd` |  `object` |  rbd represents a Rados Block Device mount on the host that shares a pod’s lifetime. Deprecated: RBD is deprecated and the in-tree rbd type is no longer supported.   
`scaleIO` |  `object` |  scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. Deprecated: ScaleIO is deprecated and the in-tree scaleIO type is no longer supported.   
`secret` |  `object` |  secret represents a secret that should populate this volume. More info: <https://kubernetes.io/docs/concepts/storage/volumes#secret>  
`storageos` |  `object` |  storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes. Deprecated: StorageOS is deprecated and the in-tree storageos type is no longer supported.   
`vsphereVolume` |  `object` |  vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine. Deprecated: VsphereVolume is deprecated. All operations for the in-tree vsphereVolume type are redirected to the csi.vsphere.vmware.com CSI driver.   
Show more

## 2.1.343. .spec.volumes[].awsElasticBlockStore

Description
     awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Deprecated: AWSElasticBlockStore is deprecated. All operations for the in-tree awsElasticBlockStore type are redirected to the ebs.csi.aws.com CSI driver. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore>
Type
     `object`
Required
    

  * `volumeID`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore>  
`partition` |  `integer` |  partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).   
`readOnly` |  `boolean` |  readOnly value true will force the readOnly setting in VolumeMounts. More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore>  
`volumeID` |  `string` |  volumeID is unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: <https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore>  
Show more

## 2.1.344. .spec.volumes[].azureDisk

Description
     azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. Deprecated: AzureDisk is deprecated. All operations for the in-tree azureDisk type are redirected to the disk.csi.azure.com CSI driver. 
Type
     `object`
Required
    

  * `diskName`
  * `diskURI`



Property| Type| Description  
---|---|---  
`cachingMode` |  `string` |  cachingMode is the Host Caching mode: None, Read Only, Read Write.   
`diskName` |  `string` |  diskName is the Name of the data disk in the blob storage   
`diskURI` |  `string` |  diskURI is the URI of data disk in the blob storage   
`fsType` |  `string` |  fsType is Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`kind` |  `string` |  kind expected values are Shared: multiple blob disks per storage account Dedicated: single blob disk per storage account Managed: azure managed data disk (only in managed availability set). defaults to shared   
`readOnly` |  `boolean` |  readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
Show more

## 2.1.345. .spec.volumes[].azureFile

Description
     azureFile represents an Azure File Service mount on the host and bind mount to the pod. Deprecated: AzureFile is deprecated. All operations for the in-tree azureFile type are redirected to the file.csi.azure.com CSI driver. 
Type
     `object`
Required
    

  * `secretName`
  * `shareName`



Property| Type| Description  
---|---|---  
`readOnly` |  `boolean` |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`secretName` |  `string` |  secretName is the name of secret that contains Azure Storage Account Name and Key   
`shareName` |  `string` |  shareName is the azure share Name   
Show more

## 2.1.346. .spec.volumes[].cephfs

Description
     cephFS represents a Ceph FS mount on the host that shares a pod’s lifetime. Deprecated: CephFS is deprecated and the in-tree cephfs type is no longer supported. 
Type
     `object`
Required
    

  * `monitors`



Property| Type| Description  
---|---|---  
`monitors` |  `array (string)` |  monitors is Required: Monitors is a collection of Ceph monitors More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it>  
`path` |  `string` |  path is Optional: Used as the mounted root, rather than the full Ceph tree, default is /   
`readOnly` |  `boolean` |  readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it>  
`secretFile` |  `string` |  secretFile is Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it>  
`secretRef` |  `object` |  secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it>  
`user` |  `string` |  user is optional: User is the rados user name, default is admin More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it>  
Show more

## 2.1.347. .spec.volumes[].cephfs.secretRef

Description
     secretRef is Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: <https://examples.k8s.io/volumes/cephfs/README.md#how-to-use-it>
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 2.1.348. .spec.volumes[].cinder

Description
     cinder represents a cinder volume attached and mounted on kubelets host machine. Deprecated: Cinder is deprecated. All operations for the in-tree cinder type are redirected to the cinder.csi.openstack.org CSI driver. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md>
Type
     `object`
Required
    

  * `volumeID`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md>  
`readOnly` |  `boolean` |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md>  
`secretRef` |  `object` |  secretRef is optional: points to a secret object containing parameters used to connect to OpenStack.   
`volumeID` |  `string` |  volumeID used to identify the volume in cinder. More info: <https://examples.k8s.io/mysql-cinder-pd/README.md>  
Show more

## 2.1.349. .spec.volumes[].cinder.secretRef

Description
     secretRef is optional: points to a secret object containing parameters used to connect to OpenStack. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 2.1.350. .spec.volumes[].configMap

Description
     configMap represents a configMap that should populate this volume 
Type
     `object`

Property| Type| Description  
---|---|---  
`defaultMode` |  `integer` |  defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`items` |  `array` |  items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.   
`items[]` |  `object` |  Maps a string key to a path within a volume.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  optional specify whether the ConfigMap or its keys must be defined   
Show more

## 2.1.351. .spec.volumes[].configMap.items

Description
     items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. 
Type
     `array`

## 2.1.352. .spec.volumes[].configMap.items[]

Description
     Maps a string key to a path within a volume. 
Type
     `object`
Required
    

  * `key`
  * `path`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key is the key to project.   
`mode` |  `integer` |  mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`path` |  `string` |  path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.   
Show more

## 2.1.353. .spec.volumes[].csi

Description
     csi (Container Storage Interface) represents ephemeral storage that is handled by certain external CSI drivers. 
Type
     `object`
Required
    

  * `driver`



Property| Type| Description  
---|---|---  
`driver` |  `string` |  driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster.   
`fsType` |  `string` |  fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply.   
`nodePublishSecretRef` |  `object` |  nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed.   
`readOnly` |  `boolean` |  readOnly specifies a read-only configuration for the volume. Defaults to false (read/write).   
`volumeAttributes` |  `object (string)` |  volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver’s documentation for supported values.   
Show more

## 2.1.354. .spec.volumes[].csi.nodePublishSecretRef

Description
     nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 2.1.355. .spec.volumes[].downwardAPI

Description
     downwardAPI represents downward API about the pod that should populate this volume 
Type
     `object`

Property| Type| Description  
---|---|---  
`defaultMode` |  `integer` |  Optional: mode bits to use on created files by default. Must be a Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`items` |  `array` |  Items is a list of downward API volume file   
`items[]` |  `object` |  DownwardAPIVolumeFile represents information to create the file containing the pod field   
Show more

## 2.1.356. .spec.volumes[].downwardAPI.items

Description
     Items is a list of downward API volume file 
Type
     `array`

## 2.1.357. .spec.volumes[].downwardAPI.items[]

Description
     DownwardAPIVolumeFile represents information to create the file containing the pod field 
Type
     `object`
Required
    

  * `path`



Property| Type| Description  
---|---|---  
`fieldRef` |  `object` |  Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported.   
`mode` |  `integer` |  Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`path` |  `string` |  Required: Path is the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'   
`resourceFieldRef` |  `object` |  Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.   
Show more

## 2.1.358. .spec.volumes[].downwardAPI.items[].fieldRef

Description
     Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported. 
Type
     `object`
Required
    

  * `fieldPath`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  Version of the schema the FieldPath is written in terms of, defaults to "v1".   
`fieldPath` |  `string` |  Path of the field to select in the specified API version.   
Show more

## 2.1.359. .spec.volumes[].downwardAPI.items[].resourceFieldRef

Description
     Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported. 
Type
     `object`
Required
    

  * `resource`



Property| Type| Description  
---|---|---  
`containerName` |  `string` |  Container name: required for volumes, optional for env vars   
`divisor` |  `integer-or-string` |  Specifies the output format of the exposed resources, defaults to "1"   
`resource` |  `string` |  Required: resource to select   
Show more

## 2.1.360. .spec.volumes[].emptyDir

Description
     emptyDir represents a temporary directory that shares a pod’s lifetime. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir>
Type
     `object`

Property| Type| Description  
---|---|---  
`medium` |  `string` |  medium represents what type of storage medium should back this directory. The default is "" which means to use the node’s default medium. Must be an empty string (default) or Memory. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir>  
`sizeLimit` |  `integer-or-string` |  sizeLimit is the total amount of local storage required for this EmptyDir volume. The size limit is also applicable for memory medium. The maximum usage on memory medium EmptyDir would be the minimum value between the SizeLimit specified here and the sum of memory limits of all containers in a pod. The default is nil which means that the limit is undefined. More info: <https://kubernetes.io/docs/concepts/storage/volumes#emptydir>  
Show more

## 2.1.361. .spec.volumes[].ephemeral

Description
    

ephemeral represents a volume that is handled by a cluster storage driver. The volume’s lifecycle is tied to the pod that defines it - it will be created before the pod starts, and deleted when the pod is removed. 

Use this if: a) the volume is only needed while the pod runs, b) features of normal volumes like restoring from snapshot or capacity tracking are needed, c) the storage driver is specified through a storage class, and d) the storage driver supports dynamic volume provisioning through a PersistentVolumeClaim (see EphemeralVolumeSource for more information on the connection between this volume type and PersistentVolumeClaim). 

Use PersistentVolumeClaim or one of the vendor-specific APIs for volumes that persist for longer than the lifecycle of an individual pod. 

Use CSI for light-weight local ephemeral volumes if the CSI driver is meant to be used that way - see the documentation of the driver for more information. 

A pod can use both types of ephemeral volumes and persistent volumes at the same time. 

Type
     `object`

Property| Type| Description  
---|---|---  
`volumeClaimTemplate` |  `object` |  Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod. The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long).  An existing PVC with that name that is not owned by the pod will **not** be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster.  This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created.  Required, must not be nil.   
Show more

## 2.1.362. .spec.volumes[].ephemeral.volumeClaimTemplate

Description
    

Will be used to create a stand-alone PVC to provision the volume. The pod in which this EphemeralVolumeSource is embedded will be the owner of the PVC, i.e. the PVC will be deleted together with the pod. The name of the PVC will be `<pod name>-<volume name>` where `<volume name>` is the name from the `PodSpec.Volumes` array entry. Pod validation will reject the pod if the concatenated name is not valid for a PVC (for example, too long). 

An existing PVC with that name that is not owned by the pod will **not** be used for the pod to avoid using an unrelated volume by mistake. Starting the pod is then blocked until the unrelated PVC is removed. If such a pre-created PVC is meant to be used by the pod, the PVC has to updated with an owner reference to the pod once the pod exists. Normally this should not be necessary, but it may be useful when manually reconstructing a broken cluster. 

This field is read-only and no changes will be made by Kubernetes to the PVC after it has been created. 

Required, must not be nil. 

Type
     `object`
Required
    

  * `spec`



Property| Type| Description  
---|---|---  
`metadata` |  `object` |  May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation.   
`spec` |  `object` |  The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here.   
Show more

## 2.1.363. .spec.volumes[].ephemeral.volumeClaimTemplate.metadata

Description
     May contain labels and annotations that will be copied into the PVC when creating it. No other fields are allowed and will be rejected during validation. 
Type
     `object`

## 2.1.364. .spec.volumes[].ephemeral.volumeClaimTemplate.spec

Description
     The specification for the PersistentVolumeClaim. The entire content is copied unchanged into the PVC that gets created from this template. The same fields as in a PersistentVolumeClaim are also valid here. 
Type
     `object`

Property| Type| Description  
---|---|---  
`accessModes` |  `array (string)` |  accessModes contains the desired access modes the volume should have. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1>  
`dataSource` |  `object` |  dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource.   
`dataSourceRef` |  `object` |  dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn’t specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn’t set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef preserves all values, and generates an error if a disallowed value is specified. * While dataSource only allows local objects, dataSourceRef allows objects in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled.   
`resources` |  `object` |  resources represents the minimum resources the volume should have. Users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources>  
`selector` |  `object` |  selector is a label query over volumes to consider for binding.   
`storageClassName` |  `string` |  storageClassName is the name of the StorageClass required by the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1>  
`volumeAttributesClassName` |  `string` |  volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string or nil value indicates that no VolumeAttributesClass will be applied to the claim. If the claim enters an Infeasible error state, this field can be reset to its previous value (including nil) to cancel the modification. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: <https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/>  
`volumeMode` |  `string` |  volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.   
`volumeName` |  `string` |  volumeName is the binding reference to the PersistentVolume backing this claim.   
Show more

## 2.1.365. .spec.volumes[].ephemeral.volumeClaimTemplate.spec.dataSource

Description
     dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  Kind is the type of resource being referenced   
`name` |  `string` |  Name is the name of resource being referenced   
Show more

## 2.1.366. .spec.volumes[].ephemeral.volumeClaimTemplate.spec.dataSourceRef

Description
     dataSourceRef specifies the object from which to populate the volume with data, if a non-empty volume is desired. This may be any object from a non-empty API group (non core object) or a PersistentVolumeClaim object. When this field is specified, volume binding will only succeed if the type of the specified object matches some installed volume populator or dynamic provisioner. This field will replace the functionality of the dataSource field and as such if both fields are non-empty, they must have the same value. For backwards compatibility, when namespace isn’t specified in dataSourceRef, both fields (dataSource and dataSourceRef) will be set to the same value automatically if one of them is empty and the other is non-empty. When namespace is specified in dataSourceRef, dataSource isn’t set to the same value and must be empty. There are three important differences between dataSource and dataSourceRef: * While dataSource only allows two specific types of objects, dataSourceRef allows any non-core object, as well as PersistentVolumeClaim objects. * While dataSource ignores disallowed values (dropping them), dataSourceRef preserves all values, and generates an error if a disallowed value is specified. * While dataSource only allows local objects, dataSourceRef allows objects in any namespaces. (Beta) Using this field requires the AnyVolumeDataSource feature gate to be enabled. (Alpha) Using the namespace field of dataSourceRef requires the CrossNamespaceVolumeDataSource feature gate to be enabled. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  Kind is the type of resource being referenced   
`name` |  `string` |  Name is the name of resource being referenced   
`namespace` |  `string` |  Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled.   
Show more

## 2.1.367. .spec.volumes[].ephemeral.volumeClaimTemplate.spec.resources

Description
     resources represents the minimum resources the volume should have. Users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#resources>
Type
     `object`

Property| Type| Description  
---|---|---  
`limits` |  `integer-or-string` |  Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
`requests` |  `integer-or-string` |  Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/>  
Show more

## 2.1.368. .spec.volumes[].ephemeral.volumeClaimTemplate.spec.selector

Description
     selector is a label query over volumes to consider for binding. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.369. .spec.volumes[].ephemeral.volumeClaimTemplate.spec.selector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.370. .spec.volumes[].ephemeral.volumeClaimTemplate.spec.selector.matchExpressions[]

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

## 2.1.371. .spec.volumes[].fc

Description
     fc represents a Fibre Channel resource that is attached to a kubelet’s host machine and then exposed to the pod. 
Type
     `object`

Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`lun` |  `integer` |  lun is Optional: FC target lun number   
`readOnly` |  `boolean` |  readOnly is Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`targetWWNs` |  `array (string)` |  targetWWNs is Optional: FC target worldwide names (WWNs)   
`wwids` |  `array (string)` |  wwids Optional: FC volume world wide identifiers (wwids) Either wwids or combination of targetWWNs and lun must be set, but not both simultaneously.   
Show more

## 2.1.372. .spec.volumes[].flexVolume

Description
     flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. Deprecated: FlexVolume is deprecated. Consider using a CSIDriver instead. 
Type
     `object`
Required
    

  * `driver`



Property| Type| Description  
---|---|---  
`driver` |  `string` |  driver is the name of the driver to use for this volume.   
`fsType` |  `string` |  fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.   
`options` |  `object (string)` |  options is Optional: this field holds extra command options if any.   
`readOnly` |  `boolean` |  readOnly is Optional: defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`secretRef` |  `object` |  secretRef is Optional: secretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts.   
Show more

## 2.1.373. .spec.volumes[].flexVolume.secretRef

Description
     secretRef is Optional: secretRef is reference to the secret object containing sensitive information to pass to the plugin scripts. This may be empty if no secret object is specified. If the secret object contains more than one secret, all secrets are passed to the plugin scripts. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 2.1.374. .spec.volumes[].flocker

Description
     flocker represents a Flocker volume attached to a kubelet’s host machine. This depends on the Flocker control service being running. Deprecated: Flocker is deprecated and the in-tree flocker type is no longer supported. 
Type
     `object`

Property| Type| Description  
---|---|---  
`datasetName` |  `string` |  datasetName is Name of the dataset stored as metadata  name on the dataset for Flocker should be considered as deprecated   
`datasetUUID` |  `string` |  datasetUUID is the UUID of the dataset. This is unique identifier of a Flocker dataset   
Show more

## 2.1.375. .spec.volumes[].gcePersistentDisk

Description
     gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Deprecated: GCEPersistentDisk is deprecated. All operations for the in-tree gcePersistentDisk type are redirected to the pd.csi.storage.gke.io CSI driver. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk>
Type
     `object`
Required
    

  * `pdName`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk>  
`partition` |  `integer` |  partition is the partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk>  
`pdName` |  `string` |  pdName is unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk>  
`readOnly` |  `boolean` |  readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk>  
Show more

## 2.1.376. .spec.volumes[].gitRepo

Description
     gitRepo represents a git repository at a particular revision. Deprecated: GitRepo is deprecated. To provision a container with a git repo, mount an EmptyDir into an InitContainer that clones the repo using git, then mount the EmptyDir into the Pod’s container. 
Type
     `object`
Required
    

  * `repository`



Property| Type| Description  
---|---|---  
`directory` |  `string` |  directory is the target directory name. Must not contain or start with '..'. If '.' is supplied, the volume directory will be the git repository. Otherwise, if specified, the volume will contain the git repository in the subdirectory with the given name.   
`repository` |  `string` |  repository is the URL   
`revision` |  `string` |  revision is the commit hash for the specified revision.   
Show more

## 2.1.377. .spec.volumes[].glusterfs

Description
     glusterfs represents a Glusterfs mount on the host that shares a pod’s lifetime. Deprecated: Glusterfs is deprecated and the in-tree glusterfs type is no longer supported. 
Type
     `object`
Required
    

  * `endpoints`
  * `path`



Property| Type| Description  
---|---|---  
`endpoints` |  `string` |  endpoints is the endpoint name that details Glusterfs topology.   
`path` |  `string` |  path is the Glusterfs volume path. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod>  
`readOnly` |  `boolean` |  readOnly here will force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: <https://examples.k8s.io/volumes/glusterfs/README.md#create-a-pod>  
Show more

## 2.1.378. .spec.volumes[].hostPath

Description
     hostPath represents a pre-existing file or directory on the host machine that is directly exposed to the container. This is generally used for system agents or other privileged things that are allowed to see the host machine. Most containers will NOT need this. More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath>
Type
     `object`
Required
    

  * `path`



Property| Type| Description  
---|---|---  
`path` |  `string` |  path of the directory on the host. If the path is a symlink, it will follow the link to the real path. More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath>  
`type` |  `string` |  type for HostPath Volume Defaults to "" More info: <https://kubernetes.io/docs/concepts/storage/volumes#hostpath>  
Show more

## 2.1.379. .spec.volumes[].image

Description
    

image represents an OCI object (a container image or artifact) pulled and mounted on the kubelet’s host machine. The volume is resolved at pod startup depending on which PullPolicy value is provided: 

  * Always: the kubelet always attempts to pull the reference. Container creation will fail If the pull fails. 
  * Never: the kubelet never pulls the reference and only uses a local image or artifact. Container creation will fail if the reference isn’t present. 
  * IfNotPresent: the kubelet pulls if the reference isn’t already present on disk. Container creation will fail if the reference isn’t present and the pull fails. 



The volume gets re-resolved if the pod gets deleted and recreated, which means that new remote content will become available on pod recreation. A failure to resolve or pull the image during pod startup will block containers from starting and may add significant latency. Failures will be retried using normal volume backoff and will be reported on the pod reason and message. The types of objects that may be mounted by this volume are defined by the container runtime implementation on a host machine and at minimum must include all valid types supported by the container image field. The OCI object gets mounted in a single directory (spec.containers[**].volumeMounts.mountPath) by merging the manifest layers in the same way as for container images. The volume will be mounted read-only (ro) and non-executable files (noexec). Sub path mounts for containers are not supported (spec.containers[**].volumeMounts.subpath) before 1.33. The field spec.securityContext.fsGroupChangePolicy has no effect on this volume type. 

Type
     `object`

Property| Type| Description  
---|---|---  
`pullPolicy` |  `string` |  Policy for pulling OCI objects. Possible values are: Always: the kubelet always attempts to pull the reference. Container creation will fail If the pull fails. Never: the kubelet never pulls the reference and only uses a local image or artifact. Container creation will fail if the reference isn’t present. IfNotPresent: the kubelet pulls if the reference isn’t already present on disk. Container creation will fail if the reference isn’t present and the pull fails. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise.   
`reference` |  `string` |  Required: Image or artifact reference to be used. Behaves in the same way as pod.spec.containers[*].image. Pull secrets will be assembled in the same way as for the container image by looking up node credentials, SA image pull secrets, and pod spec image pull secrets. More info: <https://kubernetes.io/docs/concepts/containers/images> This field is optional to allow higher level config management to default or override container images in workload controllers like Deployments and StatefulSets.   
Show more

## 2.1.380. .spec.volumes[].iscsi

Description
     iscsi represents an ISCSI Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. More info: <https://kubernetes.io/docs/concepts/storage/volumes/#iscsi>
Type
     `object`
Required
    

  * `iqn`
  * `lun`
  * `targetPortal`



Property| Type| Description  
---|---|---  
`chapAuthDiscovery` |  `boolean` |  chapAuthDiscovery defines whether support iSCSI Discovery CHAP authentication   
`chapAuthSession` |  `boolean` |  chapAuthSession defines whether support iSCSI Session CHAP authentication   
`fsType` |  `string` |  fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#iscsi>  
`initiatorName` |  `string` |  initiatorName is the custom iSCSI Initiator Name. If initiatorName is specified with iscsiInterface simultaneously, new iSCSI interface <target portal>:<volume name> will be created for the connection.   
`iqn` |  `string` |  iqn is the target iSCSI Qualified Name.   
`iscsiInterface` |  `string` |  iscsiInterface is the interface Name that uses an iSCSI transport. Defaults to 'default' (tcp).   
`lun` |  `integer` |  lun represents iSCSI Target Lun number.   
`portals` |  `array (string)` |  portals is the iSCSI Target Portal List. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).   
`readOnly` |  `boolean` |  readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false.   
`secretRef` |  `object` |  secretRef is the CHAP Secret for iSCSI target and initiator authentication   
`targetPortal` |  `string` |  targetPortal is iSCSI Target Portal. The Portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).   
Show more

## 2.1.381. .spec.volumes[].iscsi.secretRef

Description
     secretRef is the CHAP Secret for iSCSI target and initiator authentication 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 2.1.382. .spec.volumes[].nfs

Description
     nfs represents an NFS mount on the host that shares a pod’s lifetime More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs>
Type
     `object`
Required
    

  * `path`
  * `server`



Property| Type| Description  
---|---|---  
`path` |  `string` |  path that is exported by the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs>  
`readOnly` |  `boolean` |  readOnly here will force the NFS export to be mounted with read-only permissions. Defaults to false. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs>  
`server` |  `string` |  server is the hostname or IP address of the NFS server. More info: <https://kubernetes.io/docs/concepts/storage/volumes#nfs>  
Show more

## 2.1.383. .spec.volumes[].persistentVolumeClaim

Description
     persistentVolumeClaimVolumeSource represents a reference to a PersistentVolumeClaim in the same namespace. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims>
Type
     `object`
Required
    

  * `claimName`



Property| Type| Description  
---|---|---  
`claimName` |  `string` |  claimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims>  
`readOnly` |  `boolean` |  readOnly Will force the ReadOnly setting in VolumeMounts. Default false.   
Show more

## 2.1.384. .spec.volumes[].photonPersistentDisk

Description
     photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine. Deprecated: PhotonPersistentDisk is deprecated and the in-tree photonPersistentDisk type is no longer supported. 
Type
     `object`
Required
    

  * `pdID`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`pdID` |  `string` |  pdID is the ID that identifies Photon Controller persistent disk   
Show more

## 2.1.385. .spec.volumes[].portworxVolume

Description
     portworxVolume represents a portworx volume attached and mounted on kubelets host machine. Deprecated: PortworxVolume is deprecated. All operations for the in-tree portworxVolume type are redirected to the pxd.portworx.com CSI driver when the CSIMigrationPortworx feature-gate is on. 
Type
     `object`
Required
    

  * `volumeID`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fSType represents the filesystem type to mount Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs". Implicitly inferred to be "ext4" if unspecified.   
`readOnly` |  `boolean` |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`volumeID` |  `string` |  volumeID uniquely identifies a Portworx volume   
Show more

## 2.1.386. .spec.volumes[].projected

Description
     projected items for all in one resources secrets, configmaps, and downward API 
Type
     `object`

Property| Type| Description  
---|---|---  
`defaultMode` |  `integer` |  defaultMode are the mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`sources` |  `array` |  sources is the list of volume projections. Each entry in this list handles one source.   
`sources[]` |  `object` |  Projection that may be projected along with other supported volume types. Exactly one of these fields must be set.   
Show more

## 2.1.387. .spec.volumes[].projected.sources

Description
     sources is the list of volume projections. Each entry in this list handles one source. 
Type
     `array`

## 2.1.388. .spec.volumes[].projected.sources[]

Description
     Projection that may be projected along with other supported volume types. Exactly one of these fields must be set. 
Type
     `object`

Property| Type| Description  
---|---|---  
`clusterTrustBundle` |  `object` |  ClusterTrustBundle allows a pod to access the `.spec.trustBundle` field of ClusterTrustBundle objects in an auto-updating file.  Alpha, gated by the ClusterTrustBundleProjection feature gate.  ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector.  Kubelet performs aggressive normalization of the PEM contents written into the pod filesystem. Esoteric PEM features such as inter-block comments and block headers are stripped. Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time.   
`configMap` |  `object` |  configMap information about the configMap data to project   
`downwardAPI` |  `object` |  downwardAPI information about the downwardAPI data to project   
`podCertificate` |  `object` |  Projects an auto-rotating credential bundle (private key and certificate chain) that the pod can use either as a TLS client or server.  Kubelet generates a private key and uses it to send a PodCertificateRequest to the named signer. Once the signer approves the request and issues a certificate chain, Kubelet writes the key and certificate chain to the pod filesystem. The pod does not start until certificates have been issued for each podCertificate projected volume source in its spec.  Kubelet will begin trying to rotate the certificate at the time indicated by the signer using the PodCertificateRequest.Status.BeginRefreshAt timestamp.  Kubelet can write a single file, indicated by the credentialBundlePath field, or separate files, indicated by the keyPath and certificateChainPath fields.  The credential bundle is a single file in PEM format. The first PEM entry is the private key (in PKCS#8 format), and the remaining PEM entries are the certificate chain issued by the signer (typically, signers will return their certificate chain in leaf-to-root order).  Prefer using the credential bundle format, since your application code can read it atomically. If you use keyPath and certificateChainPath, your application must make two separate file reads. If these coincide with a certificate rotation, it is possible that the private key and leaf certificate you read may not correspond to each other. Your application will need to check for this condition, and re-read until they are consistent.  The named signer controls chooses the format of the certificate it issues; consult the signer implementation’s documentation to learn how to use the certificates it issues.   
`secret` |  `object` |  secret information about the secret data to project   
`serviceAccountToken` |  `object` |  serviceAccountToken is information about the serviceAccountToken data to project   
Show more

## 2.1.389. .spec.volumes[].projected.sources[].clusterTrustBundle

Description
    

ClusterTrustBundle allows a pod to access the `.spec.trustBundle` field of ClusterTrustBundle objects in an auto-updating file. 

Alpha, gated by the ClusterTrustBundleProjection feature gate. 

ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector. 

Kubelet performs aggressive normalization of the PEM contents written into the pod filesystem. Esoteric PEM features such as inter-block comments and block headers are stripped. Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time. 

Type
     `object`
Required
    

  * `path`



Property| Type| Description  
---|---|---  
`labelSelector` |  `object` |  Select all ClusterTrustBundles that match this label selector. Only has effect if signerName is set. Mutually-exclusive with name. If unset, interpreted as "match nothing". If set but empty, interpreted as "match everything".   
`name` |  `string` |  Select a single ClusterTrustBundle by object name. Mutually-exclusive with signerName and labelSelector.   
`optional` |  `boolean` |  If true, don’t block pod startup if the referenced ClusterTrustBundle(s) aren’t available. If using name, then the named ClusterTrustBundle is allowed not to exist. If using signerName, then the combination of signerName and labelSelector is allowed to match zero ClusterTrustBundles.   
`path` |  `string` |  Relative path from the volume root to write the bundle.   
`signerName` |  `string` |  Select all ClusterTrustBundles that match this signer name. Mutually-exclusive with name. The contents of all selected ClusterTrustBundles will be unified and deduplicated.   
Show more

## 2.1.390. .spec.volumes[].projected.sources[].clusterTrustBundle.labelSelector

Description
     Select all ClusterTrustBundles that match this label selector. Only has effect if signerName is set. Mutually-exclusive with name. If unset, interpreted as "match nothing". If set but empty, interpreted as "match everything". 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 2.1.391. .spec.volumes[].projected.sources[].clusterTrustBundle.labelSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 2.1.392. .spec.volumes[].projected.sources[].clusterTrustBundle.labelSelector.matchExpressions[]

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

## 2.1.393. .spec.volumes[].projected.sources[].configMap

Description
     configMap information about the configMap data to project 
Type
     `object`

Property| Type| Description  
---|---|---  
`items` |  `array` |  items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.   
`items[]` |  `object` |  Maps a string key to a path within a volume.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  optional specify whether the ConfigMap or its keys must be defined   
Show more

## 2.1.394. .spec.volumes[].projected.sources[].configMap.items

Description
     items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. 
Type
     `array`

## 2.1.395. .spec.volumes[].projected.sources[].configMap.items[]

Description
     Maps a string key to a path within a volume. 
Type
     `object`
Required
    

  * `key`
  * `path`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key is the key to project.   
`mode` |  `integer` |  mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`path` |  `string` |  path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.   
Show more

## 2.1.396. .spec.volumes[].projected.sources[].downwardAPI

Description
     downwardAPI information about the downwardAPI data to project 
Type
     `object`

Property| Type| Description  
---|---|---  
`items` |  `array` |  Items is a list of DownwardAPIVolume file   
`items[]` |  `object` |  DownwardAPIVolumeFile represents information to create the file containing the pod field   
Show more

## 2.1.397. .spec.volumes[].projected.sources[].downwardAPI.items

Description
     Items is a list of DownwardAPIVolume file 
Type
     `array`

## 2.1.398. .spec.volumes[].projected.sources[].downwardAPI.items[]

Description
     DownwardAPIVolumeFile represents information to create the file containing the pod field 
Type
     `object`
Required
    

  * `path`



Property| Type| Description  
---|---|---  
`fieldRef` |  `object` |  Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported.   
`mode` |  `integer` |  Optional: mode bits used to set permissions on this file, must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`path` |  `string` |  Required: Path is the relative path name of the file to be created. Must not be absolute or contain the '..' path. Must be utf-8 encoded. The first item of the relative path must not start with '..'   
`resourceFieldRef` |  `object` |  Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported.   
Show more

## 2.1.399. .spec.volumes[].projected.sources[].downwardAPI.items[].fieldRef

Description
     Required: Selects a field of the pod: only annotations, labels, name, namespace and uid are supported. 
Type
     `object`
Required
    

  * `fieldPath`



Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  Version of the schema the FieldPath is written in terms of, defaults to "v1".   
`fieldPath` |  `string` |  Path of the field to select in the specified API version.   
Show more

## 2.1.400. .spec.volumes[].projected.sources[].downwardAPI.items[].resourceFieldRef

Description
     Selects a resource of the container: only resources limits and requests (limits.cpu, limits.memory, requests.cpu and requests.memory) are currently supported. 
Type
     `object`
Required
    

  * `resource`



Property| Type| Description  
---|---|---  
`containerName` |  `string` |  Container name: required for volumes, optional for env vars   
`divisor` |  `integer-or-string` |  Specifies the output format of the exposed resources, defaults to "1"   
`resource` |  `string` |  Required: resource to select   
Show more

## 2.1.401. .spec.volumes[].projected.sources[].podCertificate

Description
    

Projects an auto-rotating credential bundle (private key and certificate chain) that the pod can use either as a TLS client or server. 

Kubelet generates a private key and uses it to send a PodCertificateRequest to the named signer. Once the signer approves the request and issues a certificate chain, Kubelet writes the key and certificate chain to the pod filesystem. The pod does not start until certificates have been issued for each podCertificate projected volume source in its spec. 

Kubelet will begin trying to rotate the certificate at the time indicated by the signer using the PodCertificateRequest.Status.BeginRefreshAt timestamp. 

Kubelet can write a single file, indicated by the credentialBundlePath field, or separate files, indicated by the keyPath and certificateChainPath fields. 

The credential bundle is a single file in PEM format. The first PEM entry is the private key (in PKCS#8 format), and the remaining PEM entries are the certificate chain issued by the signer (typically, signers will return their certificate chain in leaf-to-root order). 

Prefer using the credential bundle format, since your application code can read it atomically. If you use keyPath and certificateChainPath, your application must make two separate file reads. If these coincide with a certificate rotation, it is possible that the private key and leaf certificate you read may not correspond to each other. Your application will need to check for this condition, and re-read until they are consistent. 

The named signer controls chooses the format of the certificate it issues; consult the signer implementation’s documentation to learn how to use the certificates it issues. 

Type
     `object`
Required
    

  * `keyType`
  * `signerName`



Property| Type| Description  
---|---|---  
`certificateChainPath` |  `string` |  Write the certificate chain at this path in the projected volume.  Most applications should use credentialBundlePath. When using keyPath and certificateChainPath, your application needs to check that the key and leaf certificate are consistent, because it is possible to read the files mid-rotation.   
`credentialBundlePath` |  `string` |  Write the credential bundle at this path in the projected volume.  The credential bundle is a single file that contains multiple PEM blocks. The first PEM block is a PRIVATE KEY block, containing a PKCS#8 private key.  The remaining blocks are CERTIFICATE blocks, containing the issued certificate chain from the signer (leaf and any intermediates).  Using credentialBundlePath lets your Pod’s application code make a single atomic read that retrieves a consistent key and certificate chain. If you project them to separate files, your application code will need to additionally check that the leaf certificate was issued to the key.   
`keyPath` |  `string` |  Write the key at this path in the projected volume.  Most applications should use credentialBundlePath. When using keyPath and certificateChainPath, your application needs to check that the key and leaf certificate are consistent, because it is possible to read the files mid-rotation.   
`keyType` |  `string` |  The type of keypair Kubelet will generate for the pod.  Valid values are "RSA3072", "RSA4096", "ECDSAP256", "ECDSAP384", "ECDSAP521", and "ED25519".   
`maxExpirationSeconds` |  `integer` |  maxExpirationSeconds is the maximum lifetime permitted for the certificate.  Kubelet copies this value verbatim into the PodCertificateRequests it generates for this projection.  If omitted, kube-apiserver will set it to 86400(24 hours). kube-apiserver will reject values shorter than 3600 (1 hour). The maximum allowable value is 7862400 (91 days).  The signer implementation is then free to issue a certificate with any lifetime **shorter** than MaxExpirationSeconds, but no shorter than 3600 seconds (1 hour). This constraint is enforced by kube-apiserver. `kubernetes.io` signers will never issue certificates with a lifetime longer than 24 hours.   
`signerName` |  `string` |  Kubelet’s generated CSRs will be addressed to this signer.   
`userAnnotations` |  `object (string)` |  userAnnotations allow pod authors to pass additional information to the signer implementation. Kubernetes does not restrict or validate this metadata in any way.  These values are copied verbatim into the `spec.unverifiedUserAnnotations` field of the PodCertificateRequest objects that Kubelet creates.  Entries are subject to the same validation as object metadata annotations, with the addition that all keys must be domain-prefixed. No restrictions are placed on values, except an overall size limitation on the entire field.  Signers should document the keys and values they support. Signers should deny requests that contain keys they do not recognize.   
Show more

## 2.1.402. .spec.volumes[].projected.sources[].secret

Description
     secret information about the secret data to project 
Type
     `object`

Property| Type| Description  
---|---|---  
`items` |  `array` |  items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.   
`items[]` |  `object` |  Maps a string key to a path within a volume.   
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`optional` |  `boolean` |  optional field specify whether the Secret or its key must be defined   
Show more

## 2.1.403. .spec.volumes[].projected.sources[].secret.items

Description
     items if unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. 
Type
     `array`

## 2.1.404. .spec.volumes[].projected.sources[].secret.items[]

Description
     Maps a string key to a path within a volume. 
Type
     `object`
Required
    

  * `key`
  * `path`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key is the key to project.   
`mode` |  `integer` |  mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`path` |  `string` |  path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.   
Show more

## 2.1.405. .spec.volumes[].projected.sources[].serviceAccountToken

Description
     serviceAccountToken is information about the serviceAccountToken data to project 
Type
     `object`
Required
    

  * `path`



Property| Type| Description  
---|---|---  
`audience` |  `string` |  audience is the intended audience of the token. A recipient of a token must identify itself with an identifier specified in the audience of the token, and otherwise should reject the token. The audience defaults to the identifier of the apiserver.   
`expirationSeconds` |  `integer` |  expirationSeconds is the requested duration of validity of the service account token. As the token approaches expiration, the kubelet volume plugin will proactively rotate the service account token. The kubelet will start trying to rotate the token if the token is older than 80 percent of its time to live or if the token is older than 24 hours.Defaults to 1 hour and must be at least 10 minutes.   
`path` |  `string` |  path is the path relative to the mount point of the file to project the token into.   
Show more

## 2.1.406. .spec.volumes[].quobyte

Description
     quobyte represents a Quobyte mount on the host that shares a pod’s lifetime. Deprecated: Quobyte is deprecated and the in-tree quobyte type is no longer supported. 
Type
     `object`
Required
    

  * `registry`
  * `volume`



Property| Type| Description  
---|---|---  
`group` |  `string` |  group to map volume access to Default is no group   
`readOnly` |  `boolean` |  readOnly here will force the Quobyte volume to be mounted with read-only permissions. Defaults to false.   
`registry` |  `string` |  registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes   
`tenant` |  `string` |  tenant owning the given Quobyte volume in the Backend Used with dynamically provisioned Quobyte volumes, value is set by the plugin   
`user` |  `string` |  user to map volume access to Defaults to serivceaccount user   
`volume` |  `string` |  volume is a string that references an already created Quobyte volume by name.   
Show more

## 2.1.407. .spec.volumes[].rbd

Description
     rbd represents a Rados Block Device mount on the host that shares a pod’s lifetime. Deprecated: RBD is deprecated and the in-tree rbd type is no longer supported. 
Type
     `object`
Required
    

  * `image`
  * `monitors`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: <https://kubernetes.io/docs/concepts/storage/volumes#rbd>  
`image` |  `string` |  image is the rados image name. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
`keyring` |  `string` |  keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
`monitors` |  `array (string)` |  monitors is a collection of Ceph monitors. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
`pool` |  `string` |  pool is the rados pool name. Default is rbd. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
`readOnly` |  `boolean` |  readOnly here will force the ReadOnly setting in VolumeMounts. Defaults to false. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
`secretRef` |  `object` |  secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
`user` |  `string` |  user is the rados user name. Default is admin. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>  
Show more

## 2.1.408. .spec.volumes[].rbd.secretRef

Description
     secretRef is name of the authentication secret for RBDUser. If provided overrides keyring. Default is nil. More info: <https://examples.k8s.io/volumes/rbd/README.md#how-to-use-it>
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 2.1.409. .spec.volumes[].scaleIO

Description
     scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. Deprecated: ScaleIO is deprecated and the in-tree scaleIO type is no longer supported. 
Type
     `object`
Required
    

  * `gateway`
  * `secretRef`
  * `system`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Default is "xfs".   
`gateway` |  `string` |  gateway is the host address of the ScaleIO API Gateway.   
`protectionDomain` |  `string` |  protectionDomain is the name of the ScaleIO Protection Domain for the configured storage.   
`readOnly` |  `boolean` |  readOnly Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`secretRef` |  `object` |  secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail.   
`sslEnabled` |  `boolean` |  sslEnabled Flag enable/disable SSL communication with Gateway, default false   
`storageMode` |  `string` |  storageMode indicates whether the storage for a volume should be ThickProvisioned or ThinProvisioned. Default is ThinProvisioned.   
`storagePool` |  `string` |  storagePool is the ScaleIO Storage Pool associated with the protection domain.   
`system` |  `string` |  system is the name of the storage system as configured in ScaleIO.   
`volumeName` |  `string` |  volumeName is the name of a volume already created in the ScaleIO system that is associated with this volume source.   
Show more

## 2.1.410. .spec.volumes[].scaleIO.secretRef

Description
     secretRef references to the secret for ScaleIO user and other sensitive information. If this is not provided, Login operation will fail. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 2.1.411. .spec.volumes[].secret

Description
     secret represents a secret that should populate this volume. More info: <https://kubernetes.io/docs/concepts/storage/volumes#secret>
Type
     `object`

Property| Type| Description  
---|---|---  
`defaultMode` |  `integer` |  defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`items` |  `array` |  items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'.   
`items[]` |  `object` |  Maps a string key to a path within a volume.   
`optional` |  `boolean` |  optional field specify whether the Secret or its keys must be defined   
`secretName` |  `string` |  secretName is the name of the secret in the pod’s namespace to use. More info: <https://kubernetes.io/docs/concepts/storage/volumes#secret>  
Show more

## 2.1.412. .spec.volumes[].secret.items

Description
     items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. 
Type
     `array`

## 2.1.413. .spec.volumes[].secret.items[]

Description
     Maps a string key to a path within a volume. 
Type
     `object`
Required
    

  * `key`
  * `path`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key is the key to project.   
`mode` |  `integer` |  mode is Optional: mode bits used to set permissions on this file. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. If not specified, the volume defaultMode will be used. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set.   
`path` |  `string` |  path is the relative path of the file to map the key to. May not be an absolute path. May not contain the path element '..'. May not start with the string '..'.   
Show more

## 2.1.414. .spec.volumes[].storageos

Description
     storageOS represents a StorageOS volume attached and mounted on Kubernetes nodes. Deprecated: StorageOS is deprecated and the in-tree storageos type is no longer supported. 
Type
     `object`

Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is the filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`readOnly` |  `boolean` |  readOnly defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts.   
`secretRef` |  `object` |  secretRef specifies the secret to use for obtaining the StorageOS API credentials. If not specified, default values will be attempted.   
`volumeName` |  `string` |  volumeName is the human-readable name of the StorageOS volume. Volume names are only unique within a namespace.   
`volumeNamespace` |  `string` |  volumeNamespace specifies the scope of the volume within StorageOS. If no namespace is specified then the Pod’s namespace will be used. This allows the Kubernetes name scoping to be mirrored within StorageOS for tighter integration. Set VolumeName to any name to override the default behaviour. Set to "default" if you are not using namespaces within StorageOS. Namespaces that do not pre-exist within StorageOS will be created.   
Show more

## 2.1.415. .spec.volumes[].storageos.secretRef

Description
     secretRef specifies the secret to use for obtaining the StorageOS API credentials. If not specified, default values will be attempted. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 2.1.416. .spec.volumes[].vsphereVolume

Description
     vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine. Deprecated: VsphereVolume is deprecated. All operations for the in-tree vsphereVolume type are redirected to the csi.vsphere.vmware.com CSI driver. 
Type
     `object`
Required
    

  * `volumePath`



Property| Type| Description  
---|---|---  
`fsType` |  `string` |  fsType is filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.   
`storagePolicyID` |  `string` |  storagePolicyID is the storage Policy Based Management (SPBM) profile ID associated with the StoragePolicyName.   
`storagePolicyName` |  `string` |  storagePolicyName is the storage Policy Based Management (SPBM) profile name.   
`volumePath` |  `string` |  volumePath is the path that identifies vSphere volume vmdk   
Show more

## 2.1.417. .spec.web

Description
     web defines the web command line flags when starting Alertmanager. 
Type
     `object`

Property| Type| Description  
---|---|---  
`getConcurrency` |  `integer` |  getConcurrency defines the maximum number of GET requests processed concurrently. This corresponds to the Alertmanager’s `--web.get-concurrency` flag.   
`httpConfig` |  `object` |  httpConfig defines HTTP parameters for web server.   
`timeout` |  `integer` |  timeout for HTTP requests. This corresponds to the Alertmanager’s `--web.timeout` flag.   
`tlsConfig` |  `object` |  tlsConfig defines the TLS parameters for HTTPS.   
Show more

## 2.1.418. .spec.web.httpConfig

Description
     httpConfig defines HTTP parameters for web server. 
Type
     `object`

Property| Type| Description  
---|---|---  
`headers` |  `object` |  headers defines a list of headers that can be added to HTTP responses.   
`http2` |  `boolean` |  http2 enable HTTP/2 support. Note that HTTP/2 is only supported with TLS. When TLSConfig is not configured, HTTP/2 will be disabled. Whenever the value of the field changes, a rolling update will be triggered.   
Show more

## 2.1.419. .spec.web.httpConfig.headers

Description
     headers defines a list of headers that can be added to HTTP responses. 
Type
     `object`

Property| Type| Description  
---|---|---  
`contentSecurityPolicy` |  `string` |  contentSecurityPolicy defines the Content-Security-Policy header to HTTP responses. Unset if blank.   
`strictTransportSecurity` |  `string` |  strictTransportSecurity defines the Strict-Transport-Security header to HTTP responses. Unset if blank. Please make sure that you use this with care as this header might force browsers to load Prometheus and the other applications hosted on the same domain and subdomains over HTTPS. <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security>  
`xContentTypeOptions` |  `string` |  xContentTypeOptions defines the X-Content-Type-Options header to HTTP responses. Unset if blank. Accepted value is nosniff. <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options>  
`xFrameOptions` |  `string` |  xFrameOptions defines the X-Frame-Options header to HTTP responses. Unset if blank. Accepted values are deny and sameorigin. <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options>  
`xXSSProtection` |  `string` |  xXSSProtection defines the X-XSS-Protection header to all responses. Unset if blank. <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection>  
Show more

## 2.1.420. .spec.web.tlsConfig

Description
     tlsConfig defines the TLS parameters for HTTPS. 
Type
     `object`

Property| Type| Description  
---|---|---  
`cert` |  `object` |  cert defines the Secret or ConfigMap containing the TLS certificate for the web server.  Either `keySecret` or `keyFile` must be defined.  It is mutually exclusive with `certFile`.   
`certFile` |  `string` |  certFile defines the path to the TLS certificate file in the container for the web server.  Either `keySecret` or `keyFile` must be defined.  It is mutually exclusive with `cert`.   
`cipherSuites` |  `array (string)` |  cipherSuites defines the list of supported cipher suites for TLS versions up to TLS 1.2.  If not defined, the Go default cipher suites are used. Available cipher suites are documented in the Go documentation: <https://golang.org/pkg/crypto/tls/#pkg-constants>  
`clientAuthType` |  `string` |  clientAuthType defines the server policy for client TLS authentication.  For more detail on clientAuth options: <https://golang.org/pkg/crypto/tls/#ClientAuthType>  
`clientCAFile` |  `string` |  clientCAFile defines the path to the CA certificate file for client certificate authentication to the server.  It is mutually exclusive with `client_ca`.   
`client_ca` |  `object` |  client_ca defines the Secret or ConfigMap containing the CA certificate for client certificate authentication to the server.  It is mutually exclusive with `clientCAFile`.   
`curvePreferences` |  `array (string)` |  curvePreferences defines elliptic curves that will be used in an ECDHE handshake, in preference order.  Available curves are documented in the Go documentation: <https://golang.org/pkg/crypto/tls/#CurveID>  
`keyFile` |  `string` |  keyFile defines the path to the TLS private key file in the container for the web server.  If defined, either `cert` or `certFile` must be defined.  It is mutually exclusive with `keySecret`.   
`keySecret` |  `object` |  keySecret defines the secret containing the TLS private key for the web server.  Either `cert` or `certFile` must be defined.  It is mutually exclusive with `keyFile`.   
`maxVersion` |  `string` |  maxVersion defines the Maximum TLS version that is acceptable.   
`minVersion` |  `string` |  minVersion defines the minimum TLS version that is acceptable.   
`preferServerCipherSuites` |  `boolean` |  preferServerCipherSuites defines whether the server selects the client’s most preferred cipher suite, or the server’s most preferred cipher suite.  If true then the server’s preference, as expressed in the order of elements in cipherSuites, is used.   
Show more

## 2.1.421. .spec.web.tlsConfig.cert

Description
    

cert defines the Secret or ConfigMap containing the TLS certificate for the web server. 

Either `keySecret` or `keyFile` must be defined. 

It is mutually exclusive with `certFile`. 

Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.422. .spec.web.tlsConfig.cert.configMap

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

## 2.1.423. .spec.web.tlsConfig.cert.secret

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

## 2.1.424. .spec.web.tlsConfig.client_ca

Description
    

client_ca defines the Secret or ConfigMap containing the CA certificate for client certificate authentication to the server. 

It is mutually exclusive with `clientCAFile`. 

Type
     `object`

Property| Type| Description  
---|---|---  
`configMap` |  `object` |  configMap defines the ConfigMap containing data to use for the targets.   
`secret` |  `object` |  secret defines the Secret containing data to use for the targets.   
Show more

## 2.1.425. .spec.web.tlsConfig.client_ca.configMap

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

## 2.1.426. .spec.web.tlsConfig.client_ca.secret

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

## 2.1.427. .spec.web.tlsConfig.keySecret

Description
    

keySecret defines the secret containing the TLS private key for the web server. 

Either `cert` or `certFile` must be defined. 

It is mutually exclusive with `keyFile`. 

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

## 2.1.428. .status

Description
     status defines the most recent observed status of the Alertmanager cluster. Read-only. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#spec-and-status>
Type
     `object`

Property| Type| Description  
---|---|---  
`availableReplicas` |  `integer` |  availableReplicas defines the total number of available pods (ready for at least minReadySeconds) targeted by this Alertmanager cluster.   
`conditions` |  `array` |  conditions defines the current state of the Alertmanager object.   
`conditions[]` |  `object` |  Condition represents the state of the resources associated with the Prometheus, Alertmanager or ThanosRuler resource.   
`paused` |  `boolean` |  paused defines whether any actions on the underlying managed objects are being performed. Only delete actions will be performed.   
`replicas` |  `integer` |  replicas defines the total number of non-terminated pods targeted by this Alertmanager object (their labels match the selector).   
`selector` |  `string` |  selector used to match the pods targeted by this Alertmanager object.   
`unavailableReplicas` |  `integer` |  unavailableReplicas defines the total number of unavailable pods targeted by this Alertmanager object.   
`updatedReplicas` |  `integer` |  updatedReplicas defines the total number of non-terminated pods targeted by this Alertmanager object that have the desired version spec.   
Show more

## 2.1.429. .status.conditions

Description
     conditions defines the current state of the Alertmanager object. 
Type
     `array`

## 2.1.430. .status.conditions[]

Description
     Condition represents the state of the resources associated with the Prometheus, Alertmanager or ThanosRuler resource. 
Type
     `object`
Required
    

  * `lastTransitionTime`
  * `status`
  * `type`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  `string` |  lastTransitionTime is the time of the last update to the current status property.   
`message` |  `string` |  message defines human-readable message indicating details for the condition’s last transition.   
`observedGeneration` |  `integer` |  observedGeneration defines the .metadata.generation that the condition was set based upon. For instance, if `.metadata.generation` is currently 12, but the `.status.conditions[].observedGeneration` is 9, the condition is out of date with respect to the current state of the instance.   
`reason` |  `string` |  reason for the condition’s last transition.   
`status` |  `string` |  status of the condition.   
`type` |  `string` |  type of the condition being reported.   
Show more
