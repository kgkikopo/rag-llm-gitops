# 7.1. About boot image skew enforcement

Using boot image skew enforcement, you can ensure that the boot images in a cluster are up-to-date with the OpenShift Container Platform and RHCOS version being used in the cluster. Making sure that your boot images are current can help you avoid the problems associated with running older images. 

When boot image skew enforcement is active in a cluster, the Machine Config Operator (MCO) examines the boot image version reported in the `MachineConfiguration` object to determine if that boot image is appropriate for the cluster. If the boot image version is too old, the Operator reports that _boot image version skew_ is detected and blocks cluster updates until you manually update the boot image or disable boot image skew enforcement by setting the `None` mode, as described in this section. 

The limit for boot image version skew is set within the MCO and cannot be modified. 

For information on manually configuring the boot image in your cluster, see "Manually updating the boot image". 

## 7.1.1. About boot image skew enforcement modes

Review the following information to learn about the boot image skew enforcement modes. Use the information to determine the best method for your cluster. 

Boot image skew enforcement operates in one of the following modes: 

Automatic
    

When set to `Automatic`, with boot image management also enabled, if the cluster is updated from one OpenShift Container Platform version to the next, the MCO automatically updates the boot image version in the `MachineConfiguration` object and tests the boot image version for skew. 

Note

In OpenShift Container Platform 4.22, the automatic mode is available only for AWS, Google Cloud, Azure, and vSphere clusters and is the default for these platforms. 

The MCO automatically configures this mode when the following conditions are met: 

  * Boot image management is available for the platform that your cluster uses. Currently boot image management is available for only AWS, Google Cloud, Azure, and vSphere clusters. 
  * You have enabled boot image management for compute machine sets. 
  * You have not set skew enforcement to the manual or none mode. 



For information on boot image management, see "Boot image management". 

**Example`MachineConfiguration` object with automatic skew enforcement**

```yaml
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
status:
# ...
  bootImageSkewEnforcementStatus:
    automatic:
      ocpVersion: 4.22.0
    mode: Automatic
```


The MCO examines the boot image reported in the `ocpVersion` parameter to determine if the cluster is violating the boot image version skew limits. 

Manual
    

When set to `Manual`, if the boot image version is updated, a cluster administrator is responsible for manually updating the `MachineConfiguration` object with the RHCOS version of the new boot image or the OpenShift Container Platform version associated with the new boot image. The MCO then tests the boot image version for skew. 

**Example`MachineConfiguration` object with skew enforcement based on an RHCOS version**

```yaml
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  bootImageSkewEnforcement:
    mode: Manual
    manual:
      mode: RHCOSVersion
      rhcosVersion: 9.2.20251023-0
# ...
status:
  bootImageSkewEnforcementStatus:
    manual:
      mode: RHCOSVersion
      rhcosVersion: 9.2.20251023-0
    mode: Manual
```


**Example`MachineConfiguration` object with skew enforcement based on an OpenShift Container Platform version**

```yaml
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  bootImageSkewEnforcement:
    manual:
      mode: OCPVersion
      ocpVersion: 4.22.0
    mode: Manual
# ...
status:
  bootImageSkewEnforcementStatus:
    manual:
      mode: OCPVersion
      ocpVersion: 4.22.0
    mode: Manual
```


The MCO examines the boot image reported in the `rhcosVersion` or `ocpVersion` parameter to determine if the cluster is violating the boot image version skew limits. 

None
    

When set to `None`, boot image skew enforcement is disabled. When disabled, the MCO does not monitor for boot image skew and does not report if new nodes are provisioned with older boot images, which could introduce issues when scaling new nodes. 

**Example`MachineConfiguration` object with skew enforcement disabled**

```yaml
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  bootImageSkewEnforcement:
    mode: None
# ...
status:
  bootImageSkewEnforcementStatus:
    mode: None
```


When in the none mode, the MCO reports a Prometheus alert that skew enforcement is disabled and that scale-up might run into issues due to old boot images. The alert does not cause any functional issues for the cluster. 

Single-node OpenShift clusters default to the none mode regardless of platform, because they do not scale. The skew enforcement Prometheus alert is not reported for single-node OpenShift clusters. 

Bare-metal clusters running OpenShift Container Platform version 4.10 and later do not use the MCO to keep their boot images up-to-date. Skew enforcement defaults to the none mode and the skew enforcement Prometheus alert mentioned is not reported. For bare-metal clusters running OpenShift Container Platform version 4.9 and earlier, you need to perform a one-time action to migrate to the 4.10 system, this is explained further in the bare metal boot image update docs. For information, see "Manually updating the boot image".
