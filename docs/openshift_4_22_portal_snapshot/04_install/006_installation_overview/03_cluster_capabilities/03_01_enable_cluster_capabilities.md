# 3.1. Enable cluster capabilities

If you are using an installation method that includes customizing your cluster by creating an `install-config.yaml` file, you can select which cluster capabilities you want to make available on the cluster. 

Note

If you customize your cluster by enabling or disabling specific cluster capabilities, you must manually maintain your `install-config.yaml` file. New OpenShift Container Platform updates might declare new capability handles for existing components, or introduce new components altogether. Users who customize their `install-config.yaml` file should consider periodically updating their `install-config.yaml` file as OpenShift Container Platform is updated. 

You can use the following configuration parameters to select cluster capabilities: 

```yaml
capabilities:
  baselineCapabilitySet: v4.11
  additionalEnabledCapabilities:
  - CSISnapshot
  - Console
  - Storage
```


`capabilities.baselineCapabilitySet`
     Specifies a baseline set of capabilities to install. Valid values are `None`, `vCurrent` and `v4.x`. If you select `None`, all optional capabilities are disabled. The default value is `vCurrent`, which enables all optional capabilities. 

Note

`v4.x` refers to any value up to and including the current cluster version. For example, valid values for a OpenShift Container Platform 4.12 cluster are `v4.11` and `v4.12`. 

`capabilities.additionalEnabledCapabilities`
     Specifies a list of capabilities to explicitly enable. These capabilities are enabled in addition to the capabilities specified in `baselineCapabilitySet`. 

Note

In this example, the default capability is set to `v4.11`. The `additionalEnabledCapabilities` field enables additional capabilities over the default `v4.11` capability set. 

The following table describes the `baselineCapabilitySet` values. 

Table 3.1. Cluster capabilities baselineCapabilitySet values descriptionValue| Description  
---|---  
`vCurrent` |  Specify this option when you want to automatically add new, default capabilities that are introduced in new releases.   
`v4.11` |  Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.11. By specifying `v4.11`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.11 are `baremetal`, `MachineAPI`, `marketplace`, and `openshift-samples`.   
`v4.12` |  Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.12. By specifying `v4.12`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.12 are `baremetal`, `MachineAPI`, `marketplace`, `openshift-samples`, `Console`, `Insights`, `Storage`, and `CSISnapshot`.   
`v4.13` |  Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.13. By specifying `v4.13`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.13 are `baremetal`, `MachineAPI`, `marketplace`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, and `NodeTuning`.   
`v4.14` |  Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.14. By specifying `v4.14`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.14 are `baremetal`, `MachineAPI`, `marketplace`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, and `DeploymentConfig`.   
`v4.15` |  Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.15. By specifying `v4.15`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.15 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, and `DeploymentConfig`.   
`v4.16` |  Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.16. By specifying `v4.16`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.16 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, `DeploymentConfig`, and `CloudControllerManager`.   
`v4.17` |  Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.17. By specifying `v4.17`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.17 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, `DeploymentConfig`, and `CloudControllerManager`.   
`v4.18` |  Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.18. By specifying `v4.18`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.18 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `OperatorLifecycleManagerV1`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, `DeploymentConfig`, and `CloudControllerManager`.   
`None` |  Specify when the other sets are too large, and you do not need any capabilities or want to fine-tune via `additionalEnabledCapabilities`.   
Show more

**Additional resources**

  * [Installing a cluster on AWS with customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-customizations)
  * [Installing a cluster on Google Cloud with customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-customizations)
