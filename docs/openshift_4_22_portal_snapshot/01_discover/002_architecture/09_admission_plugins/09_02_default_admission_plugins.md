# 9.2. Default admission plugins

Default validating and mutating admission plugins are enabled in OpenShift Container Platform. These default plugins contribute to fundamental control plane functionality, such as ingress policy, cluster resource limit override, and quota policy. 

Important

Do not run workloads in or share access to default projects. Default projects are reserved for running core cluster components. 

The following default projects are considered highly privileged: `default`, `kube-public`, `kube-system`, `openshift`, `openshift-infra`, `openshift-node`, and other system-created projects that have the `openshift.io/run-level` label set to `0` or `1`. Functionality that relies on admission plugins, such as pod security admission, security context constraints, cluster resource quotas, and image reference resolution, does not work in highly privileged projects. 

The following list includes the default validating admission plugins: 

  * `LimitRanger`
  * `ServiceAccount`
  * `PodNodeSelector`
  * `Priority`
  * `PodTolerationRestriction`
  * `OwnerReferencesPermissionEnforcement`
  * `PersistentVolumeClaimResize`
  * `RuntimeClass`
  * `CertificateApproval`
  * `CertificateSigning`
  * `CertificateSubjectRestriction`
  * `autoscaling.openshift.io/ManagementCPUsOverride`
  * `authorization.openshift.io/RestrictSubjectBindings`
  * `scheduling.openshift.io/OriginPodNodeEnvironment`
  * `network.openshift.io/ExternalIPRanger`
  * `network.openshift.io/RestrictedEndpointsAdmission`
  * `image.openshift.io/ImagePolicy`
  * `security.openshift.io/SecurityContextConstraint`
  * `security.openshift.io/SCCExecRestrictions`
  * `route.openshift.io/IngressAdmission`
  * `config.openshift.io/ValidateAPIServer`
  * `config.openshift.io/ValidateAuthentication`
  * `config.openshift.io/ValidateFeatureGate`
  * `config.openshift.io/ValidateConsole`
  * `operator.openshift.io/ValidateDNS`
  * `config.openshift.io/ValidateImage`
  * `config.openshift.io/ValidateOAuth`
  * `config.openshift.io/ValidateProject`
  * `config.openshift.io/DenyDeleteClusterConfiguration`
  * `config.openshift.io/ValidateScheduler`
  * `quota.openshift.io/ValidateClusterResourceQuota`
  * `security.openshift.io/ValidateSecurityContextConstraints`
  * `authorization.openshift.io/ValidateRoleBindingRestriction`
  * `config.openshift.io/ValidateNetwork`
  * `operator.openshift.io/ValidateKubeControllerManager`
  * `ValidatingAdmissionWebhook`
  * `ResourceQuota`
  * `quota.openshift.io/ClusterResourceQuota`



The following list includes the default mutating admission plugins: 

  * `NamespaceLifecycle`
  * `LimitRanger`
  * `ServiceAccount`
  * `NodeRestriction`
  * `TaintNodesByCondition`
  * `PodNodeSelector`
  * `Priority`
  * `DefaultTolerationSeconds`
  * `PodTolerationRestriction`
  * `DefaultStorageClass`
  * `StorageObjectInUseProtection`
  * `RuntimeClass`
  * `DefaultIngressClass`
  * `autoscaling.openshift.io/ManagementCPUsOverride`
  * `scheduling.openshift.io/OriginPodNodeEnvironment`
  * `image.openshift.io/ImagePolicy`
  * `security.openshift.io/SecurityContextConstraint`
  * `security.openshift.io/DefaultSecurityContextConstraints`
  * `MutatingAdmissionWebhook`
