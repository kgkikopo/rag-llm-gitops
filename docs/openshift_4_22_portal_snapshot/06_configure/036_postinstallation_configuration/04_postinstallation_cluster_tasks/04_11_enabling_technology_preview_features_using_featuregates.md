# 4.11. Enabling Technology Preview features using FeatureGates

Enable Technology Preview features cluster-wide by editing the `FeatureGate` custom resource. 

You can turn on a subset of the current Technology Preview features on for all nodes in the cluster by editing the `FeatureGate` custom resource (CR). 

## 4.11.1. Understanding feature gates

You can use the `FeatureGate` custom resource (CR) to enable specific feature sets so that you can use specific non-default features in your cluster. 

A feature set is a collection of OpenShift Container Platform features that are not enabled by default. 

You can activate the following feature set by using the `FeatureGate` CR: 

  * `TechPreviewNoUpgrade`. This feature set is a subset of the current Technology Preview features. This feature set allows you to enable these Technology Preview features on test clusters, where you can fully test them, while leaving the features disabled on production clusters. 

Warning

Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters. 

The following Technology Preview features are enabled by this feature set: 

    * `AdditionalStorageConfig`
    * `AutomatedEtcdBackup`
    * `AWSClusterHostedDNS`
    * `AWSClusterHostedDNSInstall`
    * `AWSDedicatedHosts`
    * `AWSDualStackInstall`
    * `AWSEuropeanSovereignCloudInstall`
    * `AWSServiceLBNetworkSecurityGroup`
    * `AzureClusterHostedDNSInstall`
    * `AzureDedicatedHosts`
    * `AzureDualStackInstall`
    * `AzureMultiDisk`
    * `AzureWorkloadIdentity`
    * `BootcNodeManagement`
    * `BootImageSkewEnforcement`
    * `BuildCSIVolumes`
    * `CBORServingAndStorage`
    * `ClientsPreferCBOR`
    * `ClusterAPIInstallIBMCloud`
    * `ClusterAPIMachineManagement`
    * `ClusterAPIMachineManagementAWS`
    * `ClusterAPIMachineManagementAzure`
    * `ClusterAPIMachineManagementBareMetal`
    * `ClusterAPIMachineManagementGCP`
    * `ClusterAPIMachineManagementOpenStack`
    * `ClusterAPIMachineManagementPowerVS`
    * `ClusterAPIMachineManagementVSphere`
    * `ClusterMonitoringConfig`
    * `ClusterUpdateAcceptRisks`
    * `ClusterVersionOperatorConfiguration`
    * `ConfigurablePKI`
    * `ConsolePluginContentSecurityPolicy`
    * `CRDCompatibilityRequirementOperator`
    * `CRIOCredentialProviderConfig`
    * `DNSNameResolver`
    * `DRAPartitionableDevices`
    * `DualReplica`
    * `DynamicServiceEndpointIBMCloud`
    * `EtcdBackendQuota`
    * `EventTTL`
    * `Example`
    * `ExternalOIDC`
    * `ExternalOIDCWithUIDAndExtraClaimMappings`
    * `ExternalOIDCWithUpstreamParity`
    * `GatewayAPIWithoutOLM`
    * `GCPCustomAPIEndpoints`
    * `GCPCustomAPIEndpointsInstall`
    * `GCPDualStackInstall`
    * `HyperShiftOnlyDynamicResourceAllocation`
    * `ImageModeStatusReporting`
    * `ImageStreamImportMode`
    * `IngressControllerDynamicConfigurationManager`
    * `InsightsConfig`
    * `InsightsOnDemandDataGather`
    * `IrreconcilableMachineConfig`
    * `KMSEncryption`
    * `KMSv1`
    * `MachineAPIMigration`
    * `MachineAPIMigrationAWS`
    * `MachineAPIMigrationOpenStack`
    * `ManagedBootImagesCPMS`
    * `MaxUnavailableStatefulSet`
    * `MetricsCollectionProfiles`
    * `MinimumKubeletVersion`
    * `MixedCPUsAllocation`
    * `MultiDiskSetup`
    * `MutableCSINodeAllocatableCount`
    * `MutatingAdmissionPolicy`
    * `NewOLM`
    * `NewOLMBoxCutterRuntime`
    * `NewOLMCatalogdAPIV1Metas`
    * `NewOLMConfigAPI`
    * `NewOLMOwnSingleNamespace`
    * `NewOLMPreflightPermissionChecks`
    * `NewOLMWebhookProviderOpenshiftServiceCA`
    * `NoOverlayMode`
    * `NoRegistryClusterInstall`
    * `NutanixMultiSubnets`
    * `OnPremDNSRecords`
    * `OpenShiftPodSecurityAdmission`
    * `OSStreams`
    * `OVNObservability`
    * `RouteExternalCertificate`
    * `SELinuxMount`
    * `ServiceAccountTokenNodeBinding`
    * `SignatureStores`
    * `SigstoreImageVerification`
    * `SigstoreImageVerificationPKI`
    * `StoragePerformantSecurityPolicy`
    * `TLSAdherence`
    * `UpgradeStatus`
    * `UserNamespacesPodSecurityStandards`
    * `UserNamespacesSupport`
    * `VolumeGroupSnapshot`
    * `VSphereConfigurableMaxAllowedBlockVolumesPerNode`
    * `VSphereHostVMGroupZonal`
    * `VSphereMixedNodeEnv`
    * `VSphereMultiDisk`
    * `VSphereMultiNetworks`




## 4.11.2. Enabling feature sets using the web console

You can use the OpenShift Container Platform web console to enable feature sets for all of the nodes in a cluster by editing the `FeatureGate` custom resource (CR). Completing this task enables non-default features in your cluster. 

**Procedure**

  1. In the OpenShift Container Platform web console, switch to the **Administration** **Custom Resource Definitions** page. 
  2. On the **Custom Resource Definitions** page, click **FeatureGate**. 
  3. On the **Custom Resource Definition Details** page, click the **Instances** tab. 
  4. Click the **cluster** feature gate, then click the **YAML** tab. 
  5. Edit the **cluster** instance to add specific feature sets: 

Warning

Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters. 

**Sample Feature Gate custom resource**

```yaml
apiVersion: config.openshift.io/v1
kind: FeatureGate
metadata:
  name: cluster 
```


1

```yaml
# ...
spec:
  featureSet: TechPreviewNoUpgrade 
```


2

```yaml

```


where: 

`metadata.name`
     Specifies the name of the `FeatureGate` CR. You must specify `cluster` for the name. 
`spec.featureSet`
    

Specifies the feature set that you want to enable: 

     * `TechPreviewNoUpgrade` enables specific Technology Preview features. 

After you save the changes, new machine configs are created, the machine config pools are updated, and scheduling on each node is disabled while the change is being applied. 




**Verification**

You can verify that the feature gates are enabled by looking at the `kubelet.conf` file on a node after the nodes return to the ready state. 

  1. From the **Administrator** perspective in the web console, navigate to **Compute** **Nodes**. 
  2. Select a node. 
  3. In the **Node details** page, click **Terminal**. 
  4. In the terminal window, change your root directory to `/host`: 

```shell-session
sh-4.2# chroot /host
```


  5. View the `kubelet.conf` file: 

```shell-session
sh-4.2# cat /etc/kubernetes/kubelet.conf
```


**Sample output**

```shell-session
# ...
featureGates:
  InsightsOperatorPullingSCA: true,
  LegacyNodeRoleBehavior: false
# ...
```


The features that are listed as `true` are enabled on your cluster. 

Note

The features listed vary depending upon the OpenShift Container Platform version. 




## 4.11.3. Enabling feature sets using the CLI

You can use the OpenShift CLI (`oc`) to enable feature sets for all of the nodes in a cluster by editing the `FeatureGate` custom resource (CR). Completing this task enables non-default features in your cluster. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  * Edit the `FeatureGate` CR named `cluster`: 

```shell-session
$ oc edit featuregate cluster
```


Warning

Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. You should not enable this feature set on production clusters. 

**Sample FeatureGate custom resource**

```yaml
apiVersion: config.openshift.io/v1
kind: FeatureGate
metadata:
  name: cluster
# ...
spec:
  featureSet: TechPreviewNoUpgrade
```


where: 

`metadata.name`
     Specifies the name of the `FeatureGate` CR. This must be `cluster`. 
`spec.featureSet`
    

Specifies the feature set that you want to enable: 

    * `TechPreviewNoUpgrade` enables specific Technology Preview features. 

After you save the changes, new machine configs are created, the machine config pools are updated, and scheduling on each node is disabled while the change is being applied. 




**Verification**

You can verify that the feature gates are enabled by looking at the `kubelet.conf` file on a node after the nodes return to the ready state. 

  1. From the **Administrator** perspective in the web console, navigate to **Compute** **Nodes**. 
  2. Select a node. 
  3. In the **Node details** page, click **Terminal**. 
  4. In the terminal window, change your root directory to `/host`: 

```shell-session
sh-4.2# chroot /host
```


  5. View the `kubelet.conf` file: 

```shell-session
sh-4.2# cat /etc/kubernetes/kubelet.conf
```


**Sample output**

```shell-session
# ...
featureGates:
  InsightsOperatorPullingSCA: true,
  LegacyNodeRoleBehavior: false
# ...
```


The features that are listed as `true` are enabled on your cluster. 

Note

The features listed vary depending upon the OpenShift Container Platform version.
