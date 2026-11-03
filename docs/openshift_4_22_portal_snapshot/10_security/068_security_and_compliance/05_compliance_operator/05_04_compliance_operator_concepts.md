# 5.4. Compliance Operator concepts

## 5.4.1. About the Compliance Operator

The Compliance Operator evaluates your OpenShift Container Platform cluster against compliance benchmarks and identifies gaps so you can remediate them. The Operator uses profiles that target platform components, node configurations, or both depending on the compliance standard you need to meet. 

The Compliance Operator lets OpenShift Container Platform administrators describe the required compliance state of a cluster and provides them with an overview of gaps and ways to remediate them. The Compliance Operator assesses compliance of both the Kubernetes API resources of OpenShift Container Platform, and the nodes running the cluster. The Compliance Operator uses OpenSCAP, a NIST-certified tool, to scan and enforce security policies provided by the content. 

As of Compliance Operator 1.10.0, Common Expression Language (CEL) `Rule` and `CustomRule` objects are generally available (GA). CEL works alongside OpenSCAP as a scanning engine and does not replace Extensible Configuration Checklist Description Format (XCCDF) profiles. 

Important

The Compliance Operator is available for Red Hat Enterprise Linux CoreOS (RHCOS) deployments only. 

### 5.4.1.1. Compliance Operator profiles

There are several profiles available as part of the Compliance Operator installation. You can use the `oc get` command to view available profiles, profile details, and specific rules. 

  * View the available profiles: 

```shell-session
$ oc get profile.compliance -n openshift-compliance
```


**Example output**

```shell-session
NAME                       AGE     VERSION
ocp4-cis                   3h49m   1.9.0
ocp4-cis-1-9               3h49m   1.9.0
ocp4-cis-node              3h49m   1.9.0
ocp4-cis-node-1-9          3h49m   1.9.0
ocp4-e8                    3h49m
ocp4-high                  3h49m   Revision 4
ocp4-high-node             3h49m   Revision 4
ocp4-high-node-rev-4       3h49m   Revision 4
ocp4-high-rev-4            3h49m   Revision 4
ocp4-moderate              3h49m   Revision 4
ocp4-moderate-node         3h49m   Revision 4
ocp4-moderate-node-rev-4   3h49m   Revision 4
ocp4-moderate-rev-4        3h49m   Revision 4
ocp4-nerc-cip              3h49m
ocp4-nerc-cip-node         3h49m
ocp4-pci-dss               3h49m   4.0.0
ocp4-pci-dss-3-2           3h49m   3.2.1
ocp4-pci-dss-4-0           3h49m   4.0.0
ocp4-pci-dss-node          3h49m   4.0.0
ocp4-pci-dss-node-3-2      3h49m   3.2.1
ocp4-pci-dss-node-4-0      3h49m   4.0.0
ocp4-stig                  3h49m   V2R3
ocp4-stig-node             3h49m   V2R3
ocp4-stig-node-v2r3        3h49m   V2R3
ocp4-stig-v2r3             3h49m   V2R3
rhcos4-e8                  3h49m
rhcos4-high                3h49m   Revision 4
rhcos4-high-rev-4          3h49m   Revision 4
rhcos4-moderate            3h49m   Revision 4
rhcos4-moderate-rev-4      3h49m   Revision 4
rhcos4-nerc-cip            3h49m
rhcos4-stig                3h49m   V2R3
rhcos4-stig-v2r3           3h49m   V2R3
```


These profiles represent different compliance benchmarks. Each profile has the product name that it applies to added as a prefix to the name of the profile. `ocp4-e8` applies the Essential 8 benchmark to the OpenShift Container Platform product, while `rhcos4-e8` applies the Essential 8 benchmark to the Red Hat Enterprise Linux CoreOS (RHCOS) product. 

  * Run the following command to view the details of the `rhcos4-e8` profile: 

```shell-session
$ oc get -n openshift-compliance -oyaml profiles.compliance rhcos4-e8
```


**Example output**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
description: 'This profile contains configuration checks for Red Hat Enterprise Linux
  CoreOS that align to the Australian Cyber Security Centre (ACSC) Essential Eight.
  A copy of the Essential Eight in Linux Environments guide can be found at the ACSC
  website: https://www.cyber.gov.au/acsc/view-all-content/publications/hardening-linux-workstations-and-servers'
id: xccdf_org.ssgproject.content_profile_e8
kind: Profile
metadata:
  annotations:
    compliance.openshift.io/image-digest: pb-rhcos4hrdkm
    compliance.openshift.io/product: redhat_enterprise_linux_coreos_4
    compliance.openshift.io/product-type: Node
  creationTimestamp: "2022-10-19T12:06:49Z"
  generation: 1
  labels:
    compliance.openshift.io/profile-bundle: rhcos4
  name: rhcos4-e8
  namespace: openshift-compliance
  ownerReferences:
  - apiVersion: compliance.openshift.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: ProfileBundle
    name: rhcos4
    uid: 22350850-af4a-4f5c-9a42-5e7b68b82d7d
  resourceVersion: "43699"
  uid: 86353f70-28f7-40b4-bf0e-6289ec33675b
rules:
- rhcos4-accounts-no-uid-except-zero
- rhcos4-audit-rules-dac-modification-chmod
- rhcos4-audit-rules-dac-modification-chown
- rhcos4-audit-rules-execution-chcon
- rhcos4-audit-rules-execution-restorecon
- rhcos4-audit-rules-execution-semanage
- rhcos4-audit-rules-execution-setfiles
- rhcos4-audit-rules-execution-setsebool
- rhcos4-audit-rules-execution-seunshare
- rhcos4-audit-rules-kernel-module-loading-delete
- rhcos4-audit-rules-kernel-module-loading-finit
- rhcos4-audit-rules-kernel-module-loading-init
- rhcos4-audit-rules-login-events
- rhcos4-audit-rules-login-events-faillock
- rhcos4-audit-rules-login-events-lastlog
- rhcos4-audit-rules-login-events-tallylog
- rhcos4-audit-rules-networkconfig-modification
- rhcos4-audit-rules-sysadmin-actions
- rhcos4-audit-rules-time-adjtimex
- rhcos4-audit-rules-time-clock-settime
- rhcos4-audit-rules-time-settimeofday
- rhcos4-audit-rules-time-stime
- rhcos4-audit-rules-time-watch-localtime
- rhcos4-audit-rules-usergroup-modification
- rhcos4-auditd-data-retention-flush
- rhcos4-auditd-freq
- rhcos4-auditd-local-events
- rhcos4-auditd-log-format
- rhcos4-auditd-name-format
- rhcos4-auditd-write-logs
- rhcos4-configure-crypto-policy
- rhcos4-configure-ssh-crypto-policy
- rhcos4-no-empty-passwords
- rhcos4-selinux-policytype
- rhcos4-selinux-state
- rhcos4-service-auditd-enabled
- rhcos4-sshd-disable-empty-passwords
- rhcos4-sshd-disable-gssapi-auth
- rhcos4-sshd-disable-rhosts
- rhcos4-sshd-disable-root-login
- rhcos4-sshd-disable-user-known-hosts
- rhcos4-sshd-do-not-permit-user-env
- rhcos4-sshd-enable-strictmodes
- rhcos4-sshd-print-last-log
- rhcos4-sshd-set-loglevel-info
- rhcos4-sysctl-kernel-dmesg-restrict
- rhcos4-sysctl-kernel-kptr-restrict
- rhcos4-sysctl-kernel-randomize-va-space
- rhcos4-sysctl-kernel-unprivileged-bpf-disabled
- rhcos4-sysctl-kernel-yama-ptrace-scope
- rhcos4-sysctl-net-core-bpf-jit-harden
title: Australian Cyber Security Centre (ACSC) Essential Eight
```


  * Run the following command to view the details of the `rhcos4-audit-rules-login-events` rule: 

```shell-session
$ oc get -n openshift-compliance -oyaml rules rhcos4-audit-rules-login-events
```


**Example output**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
checkType: Node
description: |-
  The audit system already collects login information for all users and root. If the auditd daemon is configured to use the augenrules program to read audit rules during daemon startup (the default), add the following lines to a file with suffix.rules in the directory /etc/audit/rules.d in order to watch for attempted manual edits of files involved in storing logon events:

  -w /var/log/tallylog -p wa -k logins
  -w /var/run/faillock -p wa -k logins
  -w /var/log/lastlog -p wa -k logins

  If the auditd daemon is configured to use the auditctl utility to read audit rules during daemon startup, add the following lines to /etc/audit/audit.rules file in order to watch for unattempted manual edits of files involved in storing logon events:

  -w /var/log/tallylog -p wa -k logins
  -w /var/run/faillock -p wa -k logins
  -w /var/log/lastlog -p wa -k logins
id: xccdf_org.ssgproject.content_rule_audit_rules_login_events
kind: Rule
metadata:
  annotations:
    compliance.openshift.io/image-digest: pb-rhcos4hrdkm
    compliance.openshift.io/rule: audit-rules-login-events
    control.compliance.openshift.io/NIST-800-53: AU-2(d);AU-12(c);AC-6(9);CM-6(a)
    control.compliance.openshift.io/PCI-DSS: Req-10.2.3
    policies.open-cluster-management.io/controls: AU-2(d),AU-12(c),AC-6(9),CM-6(a),Req-10.2.3
    policies.open-cluster-management.io/standards: NIST-800-53,PCI-DSS
  creationTimestamp: "2022-10-19T12:07:08Z"
  generation: 1
  labels:
    compliance.openshift.io/profile-bundle: rhcos4
  name: rhcos4-audit-rules-login-events
  namespace: openshift-compliance
  ownerReferences:
  - apiVersion: compliance.openshift.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: ProfileBundle
    name: rhcos4
    uid: 22350850-af4a-4f5c-9a42-5e7b68b82d7d
  resourceVersion: "44819"
  uid: 75872f1f-3c93-40ca-a69d-44e5438824a4
rationale: Manual editing of these files may indicate nefarious activity, such as
  an attacker attempting to remove evidence of an intrusion.
severity: medium
title: Record Attempts to Alter Logon and Logout Events
warning: Manual editing of these files may indicate nefarious activity, such as an
  attacker attempting to remove evidence of an intrusion.
```


### 5.4.1.2. Compliance Operator profile types

To assess both platform and node compliance for your required benchmarks, you can select from different Compliance Operator profile types. 

Platform
     Platform profiles evaluate your OpenShift Container Platform cluster components. For example, a Platform-level rule can confirm whether APIServer configurations are using strong encryption cyphers. 
Node
     Node profiles evaluate the OpenShift or RHCOS configuration of each host. You can use two node profiles: `ocp4` node profiles and `rhcos4` node profiles. The `ocp4` node profiles evaluate the OpenShift configuration of each host. For example, they can confirm whether `kubeconfig` files have the correct permissions to meet a compliance standard. The `rhcos4` node profiles evaluate the Red Hat Enterprise Linux CoreOS (RHCOS) configuration of each host. For example, they can confirm whether the SSHD service is configured to disable password logins. 

Important

For benchmarks that have Node and Platform profiles, such as PCI-DSS, you must run both profiles in your OpenShift Container Platform environment. 

For benchmarks that have `ocp4` Platform, `ocp4` Node, and `rhcos4` node profiles, such as FedRAMP High, you must run all three profiles in your OpenShift Container Platform environment. 

Note

In a cluster with many Nodes, both `ocp4` Node and `rhcos4` Node scans might take a long time to complete. 

### 5.4.1.3. Additional resources

  * [ACSC Essential Eight - Hardening Linux Workstations and Servers](https://www.cyber.gov.au/acsc/view-all-content/publications/hardening-linux-workstations-and-servers)
  * [OpenSCAP project](https://www.open-scap.org/)
  * [NIST Security Content Automation Protocol (SCAP)](https://csrc.nist.gov/projects/security-content-automation-protocol)



## 5.4.2. About the Compliance Operator custom resource definitions

You can use the Custom Resource Definitions (CRDs) provided by the Compliance Operator to run compliance scans and get remediation for the issues found. 

The Compliance Operator in the OpenShift Container Platform provides you with several Custom Resource Definitions (CRDs) to run the compliance scans. The Compliance Operator converts security policies into CRDs, which you can use. 

The CRD workflow uses these objects: 

  * `ProfileBundle`, `Profile`, and `TailoredProfile` to define scan requirements 
  * `ScanSetting` to configure the scan type, occurrence, and location 
  * `ScanSettingBinding` to process requirements with those settings 
  * `ComplianceSuite` to monitor deployed scans 
  * Scan results and remediation after the suite reaches the `DONE` phase 



### 5.4.2.1. Compliance Operator custom resource definition workflow

You can use the Compliance Operator Custom Resource Definition (CRD) workflow to define requirements, configure settings, process scans, monitor compliance checks, and review results. 

The CRD workflow includes the following steps: 

  1. Define your compliance scan requirements. 
  2. Configure the compliance scan settings. 
  3. Process compliance requirements with compliance scans settings. 
  4. Monitor the compliance scans. 
  5. Check the compliance scan results. 



### 5.4.2.2. ProfileBundle object

When you install the Compliance Operator, it includes ready-to-run `ProfileBundle` objects. The Compliance Operator parses the `ProfileBundle` object and creates a `Profile` object for each profile in the bundle. It also parses `Rule` and `Variable` objects, which are used by the `Profile` object. 

**Example`ProfileBundle` object**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ProfileBundle
  name: <profile bundle name>
  namespace: openshift-compliance
status:
  dataStreamStatus: VALID
```


where: 

`status.dataStreamStatus`
     Specifies whether the Compliance Operator was able to parse the content files. Value is `VALID` when parsing succeeds. 

Note

When the `contentFile` fails, an `errorMessage` attribute is displayed, which provides details of the error that occurred. 

Note

When you roll back to a known content image from an invalid image, the `ProfileBundle` object stops responding and displays `PENDING` state. As a workaround, you can move to a different image than the earlier one or you can delete and re-create the `ProfileBundle` object to return to the working state. 

### 5.4.2.3. Profile object

You can use the `Profile` object to review parsed out details about an OpenSCAP profile, such as its XCCDF identifier and profile checks for a `Node` or `Platform` type. 

The `Profile` object defines the rules and variables that can be evaluated for a certain compliance standard. You can either directly use the `Profile` object or further customize it using a `TailorProfile` object. 

Note

You cannot create or modify the `Profile` object manually because it is derived from a single `ProfileBundle` object. Typically, a single `ProfileBundle` object can include several `Profile` objects. 

**Example`Profile` object**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
description: <description of the profile>
id: xccdf_org.ssgproject.content_profile_moderate
kind: Profile
metadata:
  annotations:
    compliance.openshift.io/product: <product name>
    compliance.openshift.io/product-type: Node
  creationTimestamp: "YYYY-MM-DDTMM:HH:SSZ"
  generation: 1
  labels:
    compliance.openshift.io/profile-bundle: <profile bundle name>
  name: rhcos4-moderate
  namespace: openshift-compliance
  ownerReferences:
  - apiVersion: compliance.openshift.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: ProfileBundle
    name: <profile bundle name>
    uid: <uid string>
  resourceVersion: "<version number>"
  selfLink: /apis/compliance.openshift.io/v1alpha1/namespaces/openshift-compliance/profiles/rhcos4-moderate
  uid: <uid string>
rules:
- rhcos4-account-disable-post-pw-expiration
- rhcos4-accounts-no-uid-except-zero
- rhcos4-audit-rules-dac-modification-chmod
- rhcos4-audit-rules-dac-modification-chown
title: <title of the profile>
```


where: 

`id`
     Specifies the XCCDF name of the profile. Use this identifier when you define a `ComplianceScan` object as the value of the profile attribute of the scan. 
`metadata.annotations.compliance.openshift.io/product-type`
     Specifies either a `Node` or `Platform`. Node profiles scan the cluster nodes and platform profiles scan the Kubernetes platform. 
`rules`
     Specifies the list of rules for the profile. Each rule corresponds to a single check. 

### 5.4.2.4. Rule object

You can use the `Rule` object, which represents an individual compliance check, to view check details and understand why a scan result passed or failed. 

The `Rule` objects, which form the profiles, are also exposed as objects. You can use the `Rule` object to define your compliance check requirements and specify how a failed compliance check can be remediated. 

**Example`Rule` object**

```yaml
    apiVersion: compliance.openshift.io/v1alpha1
    checkType: Platform
    description: <description of the rule>
    id: xccdf_org.ssgproject.content_rule_configure_network_policies_namespaces
    instructions: <manual instructions for the scan>
    kind: Rule
    metadata:
      annotations:
        compliance.openshift.io/rule: configure-network-policies-namespaces
        control.compliance.openshift.io/CIS-OCP: 5.3.2
        control.compliance.openshift.io/NERC-CIP: CIP-003-3 R4;CIP-003-3 R4.2;CIP-003-3
          R5;CIP-003-3 R6;CIP-004-3 R2.2.4;CIP-004-3 R3;CIP-007-3 R2;CIP-007-3 R2.1;CIP-007-3
          R2.2;CIP-007-3 R2.3;CIP-007-3 R5.1;CIP-007-3 R6.1
        control.compliance.openshift.io/NIST-800-53: AC-4;AC-4(21);CA-3(5);CM-6;CM-6(1);CM-7;CM-7(1);SC-7;SC-7(3);SC-7(5);SC-7(8);SC-7(12);SC-7(13);SC-7(18)
      labels:
        compliance.openshift.io/profile-bundle: ocp4
      name: ocp4-configure-network-policies-namespaces
      namespace: openshift-compliance
    rationale: <description of why this rule is checked>
    severity: high
    title: <summary of the rule>
```


where: 

`checkType`
     Specifies the type of check this rule executes. `Node` profiles scan the cluster nodes and `Platform` profiles scan the Kubernetes platform. An empty value indicates there is no automated check. 
`id`
     Specifies the XCCDF name of the rule, which is parsed directly from the datastream. 
`severity`
    

Specifies the severity of the rule when it fails. 

Note

The `Rule` object gets an appropriate label for an easy identification of the associated `ProfileBundle` object. The `ProfileBundle` also gets specified in the `OwnerReferences` of this object. 

### 5.4.2.5. TailoredProfile object

You can use the `TailoredProfile` object to modify the default `Profile` object based on your organization requirements. You can enable or disable rules, set variable values, and provide justification for the customization. 

After validation, the `TailoredProfile` object creates a `ConfigMap`, which can be referenced by a `ComplianceScan` object. 

Tip

You can use the `TailoredProfile` object by referencing it in a `ScanSettingBinding` object. For more information about `ScanSettingBinding`, see ScanSettingBinding object. 

**Example`TailoredProfile` object**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: TailoredProfile
metadata:
  name: rhcos4-with-usb
spec:
  extends: rhcos4-moderate
  title: <title of the tailored profile>
  disableRules:
    - name: <name of a rule object to be disabled>
      rationale: <description of why this rule is checked>
status:
  id: xccdf_compliance.openshift.io_profile_rhcos4-with-usb
  outputRef:
    name: rhcos4-with-usb-tp
    namespace: openshift-compliance
  state: READY
```


where: 

`spec.extends`
     Optional parameter. Specifies the name of the `Profile` object upon which the `TailoredProfile` is built. If no value is set, a new profile is created from the `enableRules` list. 
`status.id`
     Specifies the XCCDF name of the tailored profile. 
`status.outputRef.name`
     Specifies the `ConfigMap` name, which can be used as the value of the `tailoringConfigMap.name` attribute of a `ComplianceScan`. 
`status.state`
     Specifies the state of the object such as `READY`, `PENDING`, and `FAILURE`. If the state of the object is `ERROR`, then the attribute `status.errorMessage` provides the reason for the failure. 

With the `TailoredProfile` object, you can create a new `Profile` object by using the `TailoredProfile` construct. To create a new `Profile`, set the following configuration parameters: 

  * an appropriate title 
  * `extends` value must be empty 
  * scan type annotation on the `TailoredProfile` object: 

```yaml
compliance.openshift.io/product-type: Platform/Node
```


Note

If you have not set the `product-type` annotation, the Compliance Operator defaults to `Platform` scan type. Adding the `-node` suffix to the name of the `TailoredProfile` object results in `node` scan type. 




### 5.4.2.6. ScanSetting object

You can use the `ScanSetting` object to define and reuse the operational policies to run your scans, reducing configuration repetition across many scan bindings. 

By default, the Compliance Operator creates the following `ScanSetting` objects: 

  * **default** \- Runs a scan every day at 1 AM on both control plane and worker nodes by using a 1Gi Persistent Volume (PV) and keeps the last three results. Remediation is neither applied nor updated automatically. 
  * **default-auto-apply** \- Runs a scan every day at 1 AM on both control plane and worker nodes by using a 1Gi Persistent Volume (PV) and keeps the last three results. Both `autoApplyRemediations` and `autoUpdateRemediations` are set to `true`. 



**Example`ScanSetting` object**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
autoApplyRemediations: true
autoUpdateRemediations: true
kind: ScanSetting
maxRetryOnTimeout: 3
metadata:
  creationTimestamp: "2022-10-18T20:21:00Z"
  generation: 1
  name: default-auto-apply
  namespace: openshift-compliance
  resourceVersion: "38840"
  uid: 8cb0967d-05e0-4d7a-ac1c-08a7f7e89e84
rawResultStorage:
  nodeSelector:
    node-role.kubernetes.io/master: ""
  pvAccessModes:
  - ReadWriteOnce
  rotation: 3
  size: 1Gi
  tolerations:
  - effect: NoSchedule
    key: node-role.kubernetes.io/master
    operator: Exists
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  - effect: NoSchedule
    key: node.kubernetes.io/memory-pressure
    operator: Exists
roles:
- master
- worker
scanTolerations:
- operator: Exists
schedule: 0 1 * * *
showNotApplicable: false
strictNodeScan: true
timeout: 30m
```


where: 

`autoApplyRemediations`
     Set to `true` to enable auto remediations. Set to `false` to disable auto remediations. 
`autoUpdateRemediations`
     Set to `true` to enable auto remediations for content updates. Set to `false` to disable auto remediations for content updates. 
`rawResultStorage.rotation`
     Specifies the number of stored scans in the raw result format. The default value is `3`. As the older results get rotated, the administrator must store the results elsewhere before the rotation happens. To disable the rotation policy, set the value to `0`. 
`rawResultStorage.size`
     Specifies the storage size that must be created for the scan to store the raw results. The default value is `1Gi`. 
`schedule`
    

Specifies how often the scan must be run in cron format. 

Note

To disable the rotation policy, set the value to `0`. 

`roles`
     Specifies the `node-role.kubernetes.io` label value to schedule the scan for `Node` type. This value must match the name of a `MachineConfigPool`. 

#### 5.4.2.6.1. ScanSettingBinding object

You can use the `ScanSettingBinding` object to specify your compliance requirements with reference to the `Profile` or `TailoredProfile` object. 

The `ScanSettingBinding` object is linked to a `ScanSetting` object, which provides the operational constraints for the scan. Then the Compliance Operator generates the `ComplianceSuite` object based on the `ScanSetting` and `ScanSettingBinding` objects. 

**Example`ScanSettingBinding` object**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSettingBinding
metadata:
  name: <name of the scan>
profiles:
  # Node checks
  - name: rhcos4-with-usb
    kind: TailoredProfile
    apiGroup: compliance.openshift.io/v1alpha1
  # Cluster checks
  - name: ocp4-moderate
    kind: Profile
    apiGroup: compliance.openshift.io/v1alpha1
settingsRef:
  name: my-companys-constraints
  kind: ScanSetting
  apiGroup: compliance.openshift.io/v1alpha1
```


where: 

`profiles`
     Specifies the details of `Profile` or `TailoredProfile` object to scan your environment. 
`settingsRef`
     Specifies the operational constraints, such as schedule and storage size. 

The creation of `ScanSetting` and `ScanSettingBinding` objects results in the compliance suite. To get the list of compliance suite, run the following command: 

```shell-session
$ oc get compliancesuites
```


Important

If you delete `ScanSettingBinding`, then compliance suite also is deleted. 

#### 5.4.2.6.2. ComplianceSuite object

You can review a `ComplianceSuite` object to keep track of the state of the scans. The object has the raw settings to create scans and an overall result. 

For `Node` type scans, map the scan to the `MachineConfigPool`, because the scan has the remediation for any issues. If you specify a label, ensure the label directly applies to a pool. 

**Example`ComplianceSuite` object**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ComplianceSuite
metadata:
  name: <name_of_the_suite>
spec:
  autoApplyRemediations: false
  schedule: "0 1 * * *"
  scans:
    - name: workers-scan
      scanType: Node
      profile: xccdf_org.ssgproject.content_profile_moderate
      content: ssg-rhcos4-ds.xml
      contentImage: registry.redhat.io/compliance/openshift-compliance-content-rhel8@sha256:45dc...
      rule: "xccdf_org.ssgproject.content_rule_no_netrc_files"
      nodeSelector:
        node-role.kubernetes.io/worker: ""
status:
  Phase: DONE
  Result: NON-COMPLIANT
  scanStatuses:
  - name: workers-scan
    phase: DONE
    result: NON-COMPLIANT
```


where: 

`spec.autoApplyRemediations`
     Set to `true` to enable auto remediations. Set to `false` to disable auto remediations. 
`spec.schedule`
     Specifies how often the scan should be run in cron format. 
`spec.scans`
     Specifies a list of scan specifications to run in the cluster. 
`status.Phase`
     Specifies the progress of the scans. 
`status.Result`
     Specifies the overall verdict of the suite. 

The suite in the background creates the `ComplianceScan` object based on the `scans` parameter. You can programmatically fetch the `ComplianceSuites` events. To get the events for the suite, run the following command: 

```shell-session
$ oc get events --field-selector involvedObject.kind=ComplianceSuite,involvedObject.name=<name of the suite>
```


Important

You might create errors when you manually define the `ComplianceSuite`, since it contains the XCCDF attributes. 

#### 5.4.2.6.3. Advanced ComplianceScan Object

You can use the `ComplianceScan` object to configure advanced options such as custom result storage, debug pods, and scan suspension for troubleshooting and tool integration. 

The Compliance Operator includes options for advanced users for debugging or integrating with existing tool. While Red Hat recommends that you should not create a `ComplianceScan` object directly, you can instead manage the object by using a `ComplianceSuite` object. 

**Example Advanced`ComplianceScan` object**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ComplianceScan
metadata:
  name: <name_of_the_compliance_scan>
spec:
  scanType: Node
  profile: xccdf_org.ssgproject.content_profile_moderate
  content: ssg-ocp4-ds.xml
  contentImage: registry.redhat.io/compliance/openshift-compliance-content-rhel8@sha256:45dc...
  rule: "xccdf_org.ssgproject.content_rule_no_netrc_files"
  nodeSelector:
    node-role.kubernetes.io/worker: ""
status:
  phase: DONE
  result: NON-COMPLIANT
```


where: 

`spec.scanType`
     Specifies either `Node` or `Platform`. Node profiles scan the cluster nodes and platform profiles scan the Kubernetes platform. 
`spec.profile`
     Specifies the XCCDF (Extensible Configuration Checklist Description Format) identifier of the profile that you want to run. 
`spec.contentImage`
     Specifies the container image that encapsulates the profile files. 
`spec.rule`
    

Specifies the scan to run a single rule. This rule must be identified with the XCCDF ID, and must belong to the specified profile. 

Note

If you skip the `rule` parameter, then scan runs for all the available rules of the specified profile. 

`spec.nodeSelector`
    

If you are on the OpenShift Container Platform and wants to generate a remediation, the `nodeSelector` label must match the `MachineConfigPool` label. 

Note

If you do not specify `nodeSelector` parameter or match the `MachineConfig` label, scan will still run, but it will not create remediation. 

`status.phase`
     Specifies the current phase of the scan. 
`status.result`
     Specifies the verdict of the scan. 

Important

If you delete a `ComplianceSuite` object, then all the associated scans get deleted. 

When the scan is complete, it generates the result as Custom Resources of the `ComplianceCheckResult` object. However, the raw results are available in ARF format. These results are stored in a Persistent Volume (PV), which has a Persistent Volume Claim (PVC) associated with the name of the scan. You can programmatically fetch the `ComplianceScans` events. To generate events for the suite, run the following command: 

```shell-session
$ oc get events --field-selector involvedObject.kind=ComplianceScan,involvedObject.name=<name_of_the_compliance_scan>
```


#### 5.4.2.6.4. ComplianceCheckResult object

When you run a scan with a specific profile, several rules in the profiles are verified. For each of these rules, a `ComplianceCheckResult` object is created, which provides the state of the cluster for a specific rule. 

**Example`ComplianceCheckResult` object**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ComplianceCheckResult
metadata:
  labels:
    compliance.openshift.io/check-severity: medium
    compliance.openshift.io/check-status: FAIL
    compliance.openshift.io/suite: example-compliancesuite
    compliance.openshift.io/scan-name: workers-scan
  name: workers-scan-no-direct-root-logins
  namespace: openshift-compliance
  ownerReferences:
  - apiVersion: compliance.openshift.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: ComplianceScan
    name: workers-scan
description: <description of scan check>
instructions: <manual instructions for the scan>
id: xccdf_org.ssgproject.content_rule_no_direct_root_logins
severity: medium
status: FAIL
```


where: 

`severity`
     Specifies the severity of the scan check. 
`status`
    

Specifies the result of the check. The possible values are: 

  * `PASS`: Specifies if the check was successful. 
  * `FAIL`: Specifies if the check was unsuccessful. 
  * `INFO`: Specifies if the check was successful and found something not severe enough to be considered an error. 
  * `MANUAL`: Specifies if the check cannot automatically assess the status and manual check is required. 
  * `INCONSISTENT`: Specifies that the different nodes are reporting different results. 
  * `ERROR`: Specifies if the check ran successfully, but could not complete. 
  * `NOTAPPLICABLE`: Specifies if the check did not run as it is not applicable. 

To get all the check results from a suite, run the following command: 




```shell-session
$ oc get compliancecheckresults \
-l compliance.openshift.io/suite=workers-compliancesuite
```


#### 5.4.2.6.5. ComplianceRemediation object

If a Kubernetes fix is available, the Compliance Operator creates a `ComplianceRemediation` object, which you can use to determine a way to fix a problem described in a `ComplianceCheckResult` object. 

For a specific check you can have a datastream specified fix. However, if a Kubernetes fix is available, then the Compliance Operator creates a `ComplianceRemediation` object. 

**Example`ComplianceRemediation` object**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ComplianceRemediation
metadata:
  labels:
    compliance.openshift.io/suite: example-compliancesuite
    compliance.openshift.io/scan-name: workers-scan
    machineconfiguration.openshift.io/role: worker
  name: workers-scan-disable-users-coredumps
  namespace: openshift-compliance
  ownerReferences:
  - apiVersion: compliance.openshift.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: ComplianceCheckResult
    name: workers-scan-disable-users-coredumps
    uid: <UID>
spec:
  apply: false
  object:
    current:
       apiVersion: machineconfiguration.openshift.io/v1
       kind: MachineConfig
       spec:
         config:
           ignition:
             version: 2.2.0
           storage:
             files:
             - contents:
                 source: data:,%2A%20%20%20%20%20hard%20%20%20core%20%20%20%200
               filesystem: root
               mode: 420
               path: /etc/security/limits.d/75-disable_users_coredumps.conf
    outdated: {}
```


where: 

`spec.apply`
     A `true` value specifies the remediation was applied. A `false` value indicates the remediation was not applied. 
`spec.object.current`
     Specifies the definition of the remediation. 
`spec.object.outdated`
     Specifies remediation that was before parsed from an earlier version of the content. The Compliance Operator still retains the outdated objects to give the administrator a chance to review the new remediations before applying them. 

To get all the remediations from a suite, run the following command: 

```shell-session
$ oc get complianceremediations \
-l compliance.openshift.io/suite=workers-compliancesuite
```


To list all failing checks that can be remediated automatically, run the following command: 

```shell-session
$ oc get compliancecheckresults \
-l 'compliance.openshift.io/check-status in (FAIL),compliance.openshift.io/automated-remediation'
```


To list all failing checks that can be remediated manually, run the following command: 

```shell-session
$ oc get compliancecheckresults \
-l 'compliance.openshift.io/check-status in (FAIL),!compliance.openshift.io/automated-remediation'
```
