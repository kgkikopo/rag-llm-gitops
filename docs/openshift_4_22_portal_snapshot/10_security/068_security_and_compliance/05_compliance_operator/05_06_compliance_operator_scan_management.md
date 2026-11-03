# 5.6. Compliance Operator scan management

## 5.6.1. Supported compliance profiles

There are several profiles available as part of the Compliance Operator (CO) installation. Although you can use these profiles to assess gaps in a cluster, usage alone does not infer or guarantee compliance with a particular profile and is not an auditor. 

To be compliant or certified under these various standards, you need to engage an authorized auditor such as a Qualified Security Assessor (QSA), Joint Authorization Board (JAB), or other industry recognized regulatory authority to assess your environment. You are required to work with an authorized auditor to achieve compliance with a standard. 

Important

The Compliance Operator might report incorrect results on some managed platforms, such as OpenShift Dedicated and Azure Red Hat OpenShift. For more information, see Red Hat Knowledgebase Solution #6983418. 

### 5.6.1.1. Compliance profiles

When working with the Compliance Operator (CO), you can use the profiles provided by the Operator to meet industry standard benchmarks. 

Note

The following tables reflect the latest available profiles in the Compliance Operator. The only supported versions of CIS and DISA STIG profiles will be the latest. Our recommendation to customers is to use `ocp4-cis` and `ocp4-cis-node`, `ocp4-stig`, and `ocp4-stig-node`, which always point to the latest version. 

#### 5.6.1.1.1. CIS compliance profiles

Table 5.1. Supported CIS compliance profilesProfile| Profile title| Application| Industry compliance benchmark| Supported architectures| Supported platforms  
---|---|---|---|---|---  
ocp4-cis [1] |  CIS Red Hat OpenShift Container Platform Benchmark v2.0.0  |  Platform  |  [CIS Benchmarks ™](https://www.cisecurity.org/cis-benchmarks/) [4] |  `x86_64` `ppc64le` `s390x` `aarch64` |   
ocp4-cis-1-9[3] |  CIS Red Hat OpenShift Container Platform Benchmark v1.9.0  |  Platform  |  [CIS Benchmarks ™](https://www.cisecurity.org/cis-benchmarks/) [4] |  `x86_64` `ppc64le` `s390x` `aarch64` |   
ocp4-cis-node [1] |  CIS Red Hat OpenShift Container Platform Benchmark v2.0.0  |  Node [2] |  [CIS Benchmarks ™](https://www.cisecurity.org/cis-benchmarks/) [4] |  `x86_64` `ppc64le` `s390x` `aarch64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
ocp4-cis-node-1-9[3] |  CIS Red Hat OpenShift Container Platform Benchmark v1.9.0  |  Node [2] |  [CIS Benchmarks ™](https://www.cisecurity.org/cis-benchmarks/) [4] |  `x86_64` `ppc64le` `s390x` `aarch64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
ocp4-cis-vm-extension  |  CIS Red Hat OpenShift Virtual Machine Extension Benchmark v1.0.0  |  Platform  |  [CIS Benchmarks ™](https://www.cisecurity.org/cis-benchmarks/) [4] |  `x86_64` `ppc64le` `s390x` `aarch64` |   
ocp4-cis-vm-extension-node  |  CIS Red Hat OpenShift Virtual Machine Extension Benchmark v1.0.0  |  Node [2] |  [CIS Benchmarks ™](https://www.cisecurity.org/cis-benchmarks/) [4] |  `x86_64` `ppc64le` `s390x` `aarch64` |   
Show more

  1. The `ocp4-cis` and `ocp4-cis-node` profiles maintain the most up-to-date version of the CIS benchmark as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as CIS v1.9.0, use the `ocp4-cis-1-9` and `ocp4-cis-node-1-9` profiles. 
  2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_. 
  3. CIS v1.9.0 is superceded by CIS v2.0.0. It is recommended to apply the latest profile to your environment. 
  4. To locate the CIS OpenShift Container Platform v4 Benchmark, go to [CIS Benchmarks](https://www.cisecurity.org/benchmark/kubernetes) and click **Download Latest CIS Benchmark** , where you can then register to download the benchmark. 



#### 5.6.1.1.2. BSI Profile Support

Table 5.2. Supported BSI compliance profilesProfile| Profile title| Application| Industry compliance benchmark| Supported architectures| Supported platforms  
---|---|---|---|---|---  
ocp4-bsi [1] |  BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4  |  Platform  |  [BSI Basic Protection Compendium](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/International/bsi_it_gs_comp_2022.pdf) |  `x86_64` |   
ocp4-bsi-node [1] |  BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4  |  Node [2] |  [BSI Basic Protection Compendium](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/International/bsi_it_gs_comp_2022.pdf) |  `x86_64` |   
rhcos4-bsi [1] |  BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4  |  Node [2] |  [BSI Basic Protection Compendium](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/International/bsi_it_gs_comp_2022.pdf) |  `x86_64` |   
ocp4-bsi-2022 [3] |  BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4  |  Platform  |  [BSI Basic Protection Compendium](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/International/bsi_it_gs_comp_2022.pdf) |  `x86_64` |   
ocp4-bsi-node-2022 [3] |  BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4  |  Node [2] |  [BSI Basic Protection Compendium](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/International/bsi_it_gs_comp_2022.pdf) |  `x86_64` |   
rhcos4-bsi-2022 [3] |  BSI IT-Grundschutz (Basic Protection) Building Block SYS.1.6 and APP.4.4  |  Node [2] |  [BSI Basic Protection Compendium](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/International/bsi_it_gs_comp_2022.pdf) |  `x86_64` |   
Show more

  1. The `ocp4-bsi`, `ocp4-bsi-node`, and `rhcos4-bsi` profiles maintain the most up-to-date version of the BSI Basic Protection Profile as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as BSI 2022, use the `ocp4-bsi-2022`, `ocp4-bsi-node-2022` or `rhcos4-bsi-2022` profiles. 
  2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_. 
  3. Edition 2022 is the latest available English edition of the BSI IT-Grundschutz (Basic Protection) compendium. There were no changes for Building Blocks SYS.1.6 and APP.4.4, SYS.1.1, and SYS.1.3 in the latest published German compendium (edition 2023). 



For more information, see [**BSI Quick Check**](https://access.redhat.com/articles/7045834). 

#### 5.6.1.1.3. Essential Eight compliance profiles

Table 5.3. Supported Essential Eight compliance profilesProfile| Profile title| Application| Industry compliance benchmark| Supported architectures| Supported platforms  
---|---|---|---|---|---  
ocp4-e8  |  Australian Cyber Security Centre (ACSC) Essential Eight  |  Platform  |  [ACSC Hardening Linux Workstations and Servers](https://www.cyber.gov.au/acsc/view-all-content/publications/hardening-linux-workstations-and-servers) |  `x86_64` |   
rhcos4-e8  |  Australian Cyber Security Centre (ACSC) Essential Eight  |  Node  |  [ACSC Hardening Linux Workstations and Servers](https://www.cyber.gov.au/acsc/view-all-content/publications/hardening-linux-workstations-and-servers) |  `x86_64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
Show more

#### 5.6.1.1.4. FedRAMP High compliance profiles

Important

Applying automatic remediations to any profile, such as `rhcos4-stig`, that uses the `service-sshd-disabled` rule, automatically disables the `sshd` service. This situation blocks SSH access to control plane nodes and compute nodes. To keep the SSH access enabled, create a `TailoredProfile` object and set the `rhcos4-service-sshd-disabled` rule value for the `disableRules` parameter. 

Table 5.4. Supported FedRAMP High compliance profilesProfile| Profile title| Application| Industry compliance benchmark| Supported architectures| Supported platforms  
---|---|---|---|---|---  
ocp4-high [1] |  NIST 800-53 High-Impact Baseline for Red Hat OpenShift - Platform level  |  Platform  |  [NIST SP-800-53 Release Search](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#!/800-53) |  `x86_64` |   
ocp4-high-node [1] |  NIST 800-53 High-Impact Baseline for Red Hat OpenShift - Node level  |  Node [2] |  [NIST SP-800-53 Release Search](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#!/800-53) |  `x86_64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
ocp4-high-node-rev-4  |  NIST 800-53 High-Impact Baseline for Red Hat OpenShift - Node level  |  Node [2] |  [NIST SP-800-53 Release Search](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#!/800-53) |  `x86_64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
ocp4-high-rev-4  |  NIST 800-53 High-Impact Baseline for Red Hat OpenShift - Platform level  |  Platform  |  [NIST SP-800-53 Release Search](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#!/800-53) |  `x86_64` |   
rhcos4-high [1] |  NIST 800-53 High-Impact Baseline for Red Hat Enterprise Linux CoreOS  |  Node  |  [NIST SP-800-53 Release Search](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#!/800-53) |  `x86_64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
rhcos4-high-rev-4  |  NIST 800-53 High-Impact Baseline for Red Hat Enterprise Linux CoreOS  |  Node  |  [NIST SP-800-53 Release Search](https://csrc.nist.gov/Projects/risk-management/sp800-53-controls/release-search#!/800-53) |  `x86_64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
Show more

  1. The `ocp4-high`, `ocp4-high-node` and `rhcos4-high` profiles maintain the most up-to-date version of the FedRAMP High standard as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as FedRAMP high R4, use the `ocp4-high-rev-4` and `ocp4-high-node-rev-4` profiles. 
  2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_. 



#### 5.6.1.1.5. FedRAMP Moderate compliance profiles

Table 5.5. Supported FedRAMP Moderate compliance profilesProfile| Profile title| Application| Industry compliance benchmark| Supported architectures| Supported platforms  
---|---|---|---|---|---  
ocp4-moderate [1] |  NIST 800-53 Moderate-Impact Baseline for Red Hat OpenShift - Platform level  |  Platform  |  [NIST SP-800-53 Release Search](https://nvd.nist.gov/800-53/Rev4/impact/moderate) |  `x86_64` `ppc64le` `s390x` `aarch64` |   
ocp4-moderate-node [1] |  NIST 800-53 Moderate-Impact Baseline for Red Hat OpenShift - Node level  |  Node [2] |  [NIST SP-800-53 Release Search](https://nvd.nist.gov/800-53/Rev4/impact/moderate) |  `x86_64` `ppc64le` `s390x` `aarch64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
ocp4-moderate-node-rev-4  |  NIST 800-53 Moderate-Impact Baseline for Red Hat OpenShift - Node level  |  Node [2] |  [NIST SP-800-53 Release Search](https://nvd.nist.gov/800-53/Rev4/impact/moderate) |  `x86_64` `ppc64le` `s390x` `aarch64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
ocp4-moderate-rev-4  |  NIST 800-53 Moderate-Impact Baseline for Red Hat OpenShift - Platform level  |  Platform  |  [NIST SP-800-53 Release Search](https://nvd.nist.gov/800-53/Rev4/impact/moderate) |  `x86_64` `ppc64le` `s390x` `aarch64` |   
rhcos4-moderate [1] |  NIST 800-53 Moderate-Impact Baseline for Red Hat Enterprise Linux CoreOS  |  Node  |  [NIST SP-800-53 Release Search](https://nvd.nist.gov/800-53/Rev4/impact/moderate) |  `x86_64` `aarch64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
rhcos4-moderate-rev-4  |  NIST 800-53 Moderate-Impact Baseline for Red Hat Enterprise Linux CoreOS  |  Node  |  [NIST SP-800-53 Release Search](https://nvd.nist.gov/800-53/Rev4/impact/moderate) |  `x86_64` `aarch64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
Show more

  1. The `ocp4-moderate`, `ocp4-moderate-node` and `rhcos4-moderate` profiles maintain the most up-to-date version of the FedRAMP Moderate standard as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as FedRAMP Moderate R4, use the `ocp4-moderate-rev-4` and `ocp4-moderate-node-rev-4` profiles. 
  2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_. 



#### 5.6.1.1.6. NERC-CIP compliance profiles

Table 5.6. Supported NERC-CIP compliance profilesProfile| Profile title| Application| Industry compliance benchmark| Supported architectures| Supported platforms  
---|---|---|---|---|---  
ocp4-nerc-cip  |  North American Electric Reliability Corporation (NERC) Critical Infrastructure Protection (CIP) cybersecurity standards profile for the OpenShift Container Platform - Platform level  |  Platform  |  [NERC CIP Standards](https://www.nerc.com/pa/Stand/Pages/USRelStand.aspx) |  `x86_64` |   
ocp4-nerc-cip-node  |  North American Electric Reliability Corporation (NERC) Critical Infrastructure Protection (CIP) cybersecurity standards profile for the OpenShift Container Platform - Node level  |  Node [1] |  [NERC CIP Standards](https://www.nerc.com/pa/Stand/Pages/USRelStand.aspx) |  `x86_64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
rhcos4-nerc-cip  |  North American Electric Reliability Corporation (NERC) Critical Infrastructure Protection (CIP) cybersecurity standards profile for Red Hat Enterprise Linux CoreOS  |  Node  |  [NERC CIP Standards](https://www.nerc.com/pa/Stand/Pages/USRelStand.aspx) |  `x86_64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
Show more

  1. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_. 



#### 5.6.1.1.7. PCI-DSS compliance profiles

Table 5.7. Supported PCI-DSS compliance profilesProfile| Profile title| Application| Industry compliance benchmark| Supported architectures| Supported platforms  
---|---|---|---|---|---  
ocp4-pci-dss [1] |  PCI-DSS v4 Control Baseline for OpenShift Container Platform 4  |  Platform  |  [PCI Security Standards ® Council Document Library](https://www.pcisecuritystandards.org/document_library?document=pci_dss) |  `x86_64` `ppc64le` `aarch64` |   
ocp4-pci-dss-3-2 [3] |  PCI-DSS v3.2.1 Control Baseline for OpenShift Container Platform 4  |  Platform  |  [PCI Security Standards ® Council Document Library](https://www.pcisecuritystandards.org/document_library?document=pci_dss) |  `x86_64` `ppc64le` `s390x` `aarch64` |   
ocp4-pci-dss-4-0  |  PCI-DSS v4 Control Baseline for OpenShift Container Platform 4  |  Platform  |  [PCI Security Standards ® Council Document Library](https://www.pcisecuritystandards.org/document_library?document=pci_dss) |  `x86_64` `ppc64le` `aarch64` |   
ocp4-pci-dss-node [1] |  PCI-DSS v4 Control Baseline for OpenShift Container Platform 4  |  Node [2] |  [PCI Security Standards ® Council Document Library](https://www.pcisecuritystandards.org/document_library?document=pci_dss) |  `x86_64` `ppc64le` `aarch64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
ocp4-pci-dss-node-3-2 [3] |  PCI-DSS v3.2.1 Control Baseline for OpenShift Container Platform 4  |  Node [2] |  [PCI Security Standards ® Council Document Library](https://www.pcisecuritystandards.org/document_library?document=pci_dss) |  `x86_64` `ppc64le` `s390x` `aarch64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
ocp4-pci-dss-node-4-0  |  PCI-DSS v4 Control Baseline for OpenShift Container Platform 4  |  Node [2] |  [PCI Security Standards ® Council Document Library](https://www.pcisecuritystandards.org/document_library?document=pci_dss) |  `x86_64` `ppc64le` `aarch64` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
Show more

  1. The `ocp4-pci-dss` and `ocp4-pci-dss-node` profiles maintain the most up-to-date version of the PCI-DSS standard as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as PCI-DSS v3.2.1, use the `ocp4-pci-dss-3-2` and `ocp4-pci-dss-node-3-2` profiles. 
  2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_. 
  3. PCI-DSS v3.2.1 is superceded by PCI-DSS v4. It is recommended to apply the latest profile to your environment. 



#### 5.6.1.1.8. STIG compliance profiles

Important

Applying automatic remediations to any profile, such as `rhcos4-stig`, that uses the `service-sshd-disabled` rule, automatically disables the `sshd` service. This situation blocks SSH access to control plane nodes and compute nodes. To keep the SSH access enabled, create a `TailoredProfile` object and set the `rhcos4-service-sshd-disabled` rule value for the `disableRules` parameter. 

Table 5.8. Supported STIG compliance profilesProfile| Profile title| Application| Industry compliance benchmark| Supported architectures| Supported platforms  
---|---|---|---|---|---  
ocp4-stig [1] |  Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red Hat OpenShift V2R6[3] |  Platform  |  [DISA-STIG](https://public.cyber.mil/stigs/downloads/) |  `x86_64` `ppc64le` |   
ocp4-stig-node [1] |  Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red Hat OpenShift V2R6[3] |  Node [2] |  [DISA-STIG](https://public.cyber.mil/stigs/downloads/) |  `x86_64` `ppc64le` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
ocp4-stig-vm-extension  |  Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red Hat OpenShift V2R6 - OpenShift Virtualization  |  Platform  |  [DISA-STIG](https://public.cyber.mil/stigs/downloads/) |  `x86_64` `ppc64le` |   
ocp4-stig-v2r3  |  Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red Hat OpenShift V2R3  |  Platform  |  [DISA-STIG](https://public.cyber.mil/stigs/downloads/) |  `x86_64` `ppc64le` |   
ocp4-stig-node-v2r3 [1] |  Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red Hat OpenShift V2R3  |  Node  |  [DISA-STIG](https://public.cyber.mil/stigs/downloads/) |  `x86_64` `ppc64le` |   
rhcos4-stig[1] |  Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red Hat OpenShift V2R6[3] |  Node  |  [DISA-STIG](https://public.cyber.mil/stigs/downloads/) |  `x86_64` `ppc64le` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
rhcos4-stig-v2r3  |  Defense Information Systems Agency Security Technical Implementation Guide (DISA STIG) for Red Hat OpenShift V2R3  |  Node  |  [DISA-STIG](https://public.cyber.mil/stigs/downloads/) |  `x86_64` `ppc64le` |  Red Hat OpenShift Service on AWS with hosted control planes (ROSA HCP)   
Show more

  1. The `ocp4-stig`, `ocp4-stig-node` and `rhcos4-stig` profiles maintain the most up-to-date version of the DISA-STIG benchmark as it becomes available in the Compliance Operator. If you want to adhere to a specific version, such as DISA-STIG V2R3, use the `ocp4-stig-v2r3` and `ocp4-stig-node-v2r3` profiles. 
  2. Node profiles must be used with the relevant Platform profile. For more information, see _Compliance Operator profile types_. 
  3. DISA-STIG V2R3 is superceded by DISA-STIG V2R6. It is recommended to apply the latest profile to your environment. 



#### 5.6.1.1.9. About extended compliance profiles

Some compliance profiles have controls that require following industry best practices, resulting in some profiles extending others. Combining the Center for Internet Security (CIS) best practices with National Institute of Standards and Technology (NIST) security frameworks establishes a path to a secure and compliant environment. 

For example, the NIST High-Impact and Moderate-Impact profiles extend the CIS profile to achieve compliance. As a result, extended compliance profiles eliminate the need to run both profiles in a single cluster. 

Table 5.9. Profile extensionsProfile| Extends  
---|---  
ocp4-pci-dss  |  ocp4-cis   
ocp4-pci-dss-node  |  ocp4-cis-node   
ocp4-high  |  ocp4-cis   
ocp4-high-node  |  ocp4-cis-node   
ocp4-moderate  |  ocp4-cis   
ocp4-moderate-node  |  ocp4-cis-node   
ocp4-nerc-cip  |  ocp4-moderate   
ocp4-nerc-cip-node  |  ocp4-moderate-node   
Show more

#### 5.6.1.1.10. Compliance Operator profile types

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

### 5.6.1.2. Additional resources

  * [Red Hat Knowledgebase Solution #6983418](https://access.redhat.com/solutions/6983418)
  * [Product Compliance](https://access.redhat.com/compliance)



## 5.6.2. Compliance Operator scans

You can use the `ScanSetting` and `ScanSettingBinding` APIs to run compliance scans with the Compliance Operator. 

For more information on these API objects, run the following command: 

```shell-session
$ oc explain scansettings
```


or 

```shell-session
$ oc explain scansettingbindings
```


### 5.6.2.1. Run compliance scans

You can run a scan using the Center for Internet Security (CIS) profiles to evaluate cluster compliance against CIS benchmarks. For convenience, the Compliance Operator creates a `ScanSetting` object with reasonable defaults on startup. This `ScanSetting` object is named `default`. 

Note

For all-in-one control plane and worker nodes, the compliance scan runs twice on the worker and control plane nodes. The compliance scan might generate inconsistent scan results. You can avoid inconsistent results by defining only a single role in the `ScanSetting` object. 

Important

Compliance Operator scans report `INCONSISTENT` on clusters with multi-architecture compute machines whether the control plane uses `aarch64` or `x86` CPUs. This is due to the same rule behaving differently on different architectures. This applies only to node scans, where the Compliance Operator aggregates results from multiple nodes into a single result. 

For more information about inconsistent scan results, see Compliance Operator shows INCONSISTENT scan result with worker node. 

**Procedure**

  1. Inspect the `ScanSetting` object by running the following command: 

```shell-session
$ oc describe scansettings default -n openshift-compliance
```


**Example output**

```yaml
Name:                  default
Namespace:             openshift-compliance
Labels:                <none>
Annotations:           <none>
API Version:           compliance.openshift.io/v1alpha1
Kind:                  ScanSetting
Max Retry On Timeout:  3
Metadata:
  Creation Timestamp:  2024-07-16T14:56:42Z
  Generation:          2
  Resource Version:    91655682
  UID:                 50358cf1-57a8-4f69-ac50-5c7a5938e402
Raw Result Storage:
  Node Selector:
    node-role.kubernetes.io/master:
  Pv Access Modes:
    ReadWriteOnce
  Rotation:            3
  Size:                1Gi
  Storage Class Name:  standard
  Tolerations:
    Effect:              NoSchedule
    Key:                 node-role.kubernetes.io/master
    Operator:            Exists
    Effect:              NoExecute
    Key:                 node.kubernetes.io/not-ready
    Operator:            Exists
    Toleration Seconds:  300
    Effect:              NoExecute
    Key:                 node.kubernetes.io/unreachable
    Operator:            Exists
    Toleration Seconds:  300
    Effect:              NoSchedule
    Key:                 node.kubernetes.io/memory-pressure
    Operator:            Exists
Roles:
  master
  worker
Scan Tolerations:
  Operator:           Exists
Schedule:             0 1 * * *
Show Not Applicable:  false
Strict Node Scan:     true
Suspend:              false
Timeout:              30m
Events:               <none>
```


where: 

`Raw Result Storage.pvAccessModes.ReadWriteOnce`
     Specifies access mode for the PV created by the Compliance Operator with the results of the scans. By default, the PV will use access mode `ReadWriteOnce` because the Compliance Operator cannot make any assumptions about the storage classes configured on the cluster. Additionally, `ReadWriteOnce` access mode is available on most clusters. If you need to fetch the scan results, you can do so by using a helper pod, which also binds the volume. Volumes that use the `ReadWriteOnce` access mode can be mounted by only one pod at time, so it is important to remember to delete the helper pods. Otherwise, the Compliance Operator will not be able to reuse the volume for subsequent scans. 
`Raw Result Storage.Rotation`
     Specifies that the Compliance Operator keeps the results of three subsequent scans in the volume; older scans are rotated. 
`Raw Result Storage.size`
     Specifies that the Compliance Operator will allocate one GB of storage for the scan results. 
`Raw Result Storage.Storage Class Name`
     Specifies the `storageClassName` value to use when creating the `PersistentVolumeClaim` object to store the raw results. The default value is null, which will attempt to use the default storage class configured in the cluster. If there is no default class specified, then you must set a default class. 
`Roles`
     If the scan setting uses any profiles that scan cluster nodes, scan these node roles. 
`Scan Tolerations`
     The default scan setting object scans all the nodes. 
`Schedule`
    

The default scan setting object runs scans at 01:00 each day. 

As an alternative to the default scan setting, you can use `default-auto-apply`, which has the following settings: 

```yaml
Name:                      default-auto-apply
Namespace:                 openshift-compliance
Labels:                    <none>
Annotations:               <none>
API Version:               compliance.openshift.io/v1alpha1
Auto Apply Remediations:   true
Auto Update Remediations:  true
Kind:                      ScanSetting
Metadata:
  Creation Timestamp:  2022-10-18T20:21:00Z
  Generation:          1
  Managed Fields:
    API Version:  compliance.openshift.io/v1alpha1
    Fields Type:  FieldsV1
    fieldsV1:
      f:autoApplyRemediations:
      f:autoUpdateRemediations:
      f:rawResultStorage:
        .:
        f:nodeSelector:
          .:
          f:node-role.kubernetes.io/master:
        f:pvAccessModes:
        f:rotation:
        f:size:
        f:tolerations:
      f:roles:
      f:scanTolerations:
      f:schedule:
      f:showNotApplicable:
      f:strictNodeScan:
    Manager:         compliance-operator
    Operation:       Update
    Time:            2022-10-18T20:21:00Z
  Resource Version:  38840
  UID:               8cb0967d-05e0-4d7a-ac1c-08a7f7e89e84
Raw Result Storage:
  Node Selector:
    node-role.kubernetes.io/master:
  Pv Access Modes:
    ReadWriteOnce
  Rotation:  3
  Size:      1Gi
  Tolerations:
    Effect:              NoSchedule
    Key:                 node-role.kubernetes.io/master
    Operator:            Exists
    Effect:              NoExecute
    Key:                 node.kubernetes.io/not-ready
    Operator:            Exists
    Toleration Seconds:  300
    Effect:              NoExecute
    Key:                 node.kubernetes.io/unreachable
    Operator:            Exists
    Toleration Seconds:  300
    Effect:              NoSchedule
    Key:                 node.kubernetes.io/memory-pressure
    Operator:            Exists
Roles:
  master
  worker
Scan Tolerations:
  Operator:           Exists
Schedule:             0 1 * * *
Show Not Applicable:  false
Strict Node Scan:     true
Events:               <none>
```


     * Setting `autoUpdateRemediations` and `autoApplyRemediations` flags to `true` allows you to easily create `ScanSetting` objects that auto-remediate without extra steps. 

  2. Create a `ScanSettingBinding` object that binds to the default `ScanSetting` object and scans the cluster using the `cis` and `cis-node` profiles. For example: 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSettingBinding
metadata:
  name: cis-compliance
  namespace: openshift-compliance
profiles:
  - name: ocp4-cis-node
    kind: Profile
    apiGroup: compliance.openshift.io/v1alpha1
  - name: ocp4-cis
    kind: Profile
    apiGroup: compliance.openshift.io/v1alpha1
settingsRef:
  name: default
  kind: ScanSetting
  apiGroup: compliance.openshift.io/v1alpha1
```


  3. Create the `ScanSettingBinding` object by running: 

```shell-session
$ oc create -f <file-name>.yaml -n openshift-compliance
```


At this point in the process, the `ScanSettingBinding` object is reconciled and based on the `Binding` and the `Bound` settings. The Compliance Operator creates a `ComplianceSuite` object and the associated `ComplianceScan` objects. 

  4. Follow the compliance scan progress by running: 

```shell-session
$ oc get compliancescan -w -n openshift-compliance
```


The scans progress through the scanning phases and eventually reach the `DONE` phase when complete. In most cases, the result of the scan is `NON-COMPLIANT`. You can review the scan results and start applying remediations to make the cluster compliant. 




### 5.6.2.2. Set custom storage size for results

Although `ComplianceCheckResult` custom resources summarize one check across all scanned nodes, raw scanner results in ARF format are too large to store in etcd-backed Kubernetes resources. 

You can store them on a per-scan persistent volume and increase the default 1 GiB size by setting the `rawResultStorage.size` value in a `ScanSetting` or `ComplianceScan` resource. 

A related parameter is `rawResultStorage.rotation` which controls how many scans are retained in the PV before the older scans are rotated. The default value is 3, setting the rotation policy to 0 disables the rotation. Given the default rotation policy and an estimate of 100MB per a raw ARF scan report, you can calculate the right PV size for your environment. 

Because OpenShift Container Platform can be deployed in a variety of public clouds or bare metal, the Compliance Operator cannot determine available storage configurations. By default, the Compliance Operator will try to create the PV for storing results by using the default storage class of the cluster, but a custom storage class can be configured using the `rawResultStorage.StorageClassName` attribute. 

Important

If your cluster does not specify a default storage class, this attribute must be set. 

  * Configure the `ScanSetting` custom resource to use a standard storage class and create persistent volumes that are 10GB in size and keep the last 10 results: 

**Example`ScanSetting` CR**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSetting
metadata:
  name: default
  namespace: openshift-compliance
rawResultStorage:
  storageClassName: standard
  rotation: 10
  size: 10Gi
roles:
- worker
- master
scanTolerations:
- effect: NoSchedule
  key: node-role.kubernetes.io/master
  operator: Exists
schedule: '0 1 * * *'
```


### 5.6.2.3. Schedule the result server pod on a worker node

The result server pod mounts the persistent volume (PV) that stores the raw Asset Reporting Format (ARF) scan results. You can use the `nodeSelector` and `tolerations` attributes to configure the location of the result server pod to meet your organization’s requirements. 

This is helpful for those environments where control plane nodes are not permitted to mount persistent volumes. 

**Procedure**

  * Create a `ScanSetting` custom resource (CR) for the Compliance Operator: 

    1. Define the `ScanSetting` CR, and save the YAML file, for example, `rs-workers.yaml`: 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSetting
metadata:
  name: rs-on-workers
  namespace: openshift-compliance
rawResultStorage:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  pvAccessModes:
  - ReadWriteOnce
  rotation: 3
  size: 1Gi
  tolerations:
  - operator: Exists
roles:
- worker
- master
scanTolerations:
  - operator: Exists
schedule: 0 1 * * *
```


where: 

`rawResultStorage.nodeSelector.node-role.kubernetes.io/worker`
     Specifies the Compliance Operator uses this node to store scan results in ARF format. 
`rawResultStorage.tolerations.operator`
     Specifies the result server pod tolerates all taints. 

    2. To create the `ScanSetting` CR, run the following command: 

```shell-session
$ oc create -f rs-workers.yaml
```


**Verification**

  * To verify that the `ScanSetting` object is created, run the following command: 

```shell-session
$ oc get scansettings rs-on-workers -n openshift-compliance -o yaml
```


**Example output**

```shell-session
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSetting
metadata:
  creationTimestamp: "2021-11-19T19:36:36Z"
  generation: 1
  name: rs-on-workers
  namespace: openshift-compliance
  resourceVersion: "48305"
  uid: 43fdfc5f-15a7-445a-8bbc-0e4a160cd46e
rawResultStorage:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  pvAccessModes:
  - ReadWriteOnce
  rotation: 3
  size: 1Gi
  tolerations:
  - operator: Exists
roles:
- worker
- master
scanTolerations:
- operator: Exists
schedule: 0 1 * * *
strictNodeScan: true
```


### 5.6.2.4. ScanSetting Custom Resource

You can configure the scan limits attribute of the `ScanSetting` custom resource to override the default CPU and memory limits of scanner pods to meet your environment’s resource requirements. 

The Compliance Operator uses defaults of 500Mi memory and 100m CPU for the scanner container, and 200Mi memory and 100m CPU for the `api-resource-collector` container. To set the memory limits of the Operator, modify the `Subscription` object if installed through OLM or the Operator deployment itself. 

Important

Increasing the memory limit for the Compliance Operator or the scanner pods is needed if the default limits are not sufficient and the Operator or scanner pods are ended by the Out Of Memory (OOM) process. For more information, see Increasing Compliance Operator resource limits. 

### 5.6.2.5. Configure the hosted control planes management cluster

If you are hosting your own Hosted control planes or Hypershift environment and want to scan a Hosted Cluster from the management cluster, you will need to set the name and prefix namespace for the target Hosted Cluster. You can achieve this by creating a `TailoredProfile`. 

Important

This procedure only applies to users managing their own hosted control planes environment. 

Note

Only `ocp4-cis` and `ocp4-pci-dss` profiles are supported in hosted control planes management clusters. 

**Prerequisites**

  * The Compliance Operator is installed in the management cluster. 



**Procedure**

  1. Obtain the `name` and `namespace` of the hosted cluster to be scanned by running the following command: 

```shell-session
$ oc get hostedcluster -A
```


**Example output**

```shell-session
NAMESPACE       NAME                   VERSION   KUBECONFIG                              PROGRESS    AVAILABLE   PROGRESSING   MESSAGE
local-cluster   79136a1bdb84b3c13217   4.13.5    79136a1bdb84b3c13217-admin-kubeconfig   Completed   True        False         The hosted control plane is available
```


  2. In the management cluster, create a `TailoredProfile` extending the scan Profile and define the name and namespace of the Hosted Cluster to be scanned: 

**Example`management-tailoredprofile.yaml`**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: TailoredProfile
metadata:
  name: hypershift-cisk57aw88gry
  namespace: openshift-compliance
spec:
  description: This profile test required rules
  extends: ocp4-cis
  title: Management namespace profile
  setValues:
  - name: ocp4-hypershift-cluster
    rationale: This value is used for HyperShift version detection
    value: 79136a1bdb84b3c13217
  - name: ocp4-hypershift-namespace-prefix
    rationale: This value is used for HyperShift control plane namespace detection
    value: local-cluster
```


where: 

`spec.extends`
     Specifies the name of the `Profile` object upon which the `TailoredProfile` is built. Only `ocp4-cis` and `ocp4-pci-dss` profiles are supported in hosted control planes management clusters. 
`spec.setValues.value`
     Specifies the output in the previous step. 
`spec.setValues.value`
     Specifies the `NAMESPACE` from the output in the previous step. 

  3. Create the `TailoredProfile`: 

```shell-session
$ oc create -n openshift-compliance -f mgmt-tp.yaml
```


### 5.6.2.6. Apply resource requests and limits

You can configure a container’s requests and limits for memory and CPU to define how much CPU time and memory that the container can use. 

When the kubelet starts a container as part of a Pod, the kubelet passes that container’s requests and limits for memory and CPU to the container runtime. In Linux, the container runtime configures the kernel cgroups that apply and enforce the limits you defined. 

The CPU limit defines how much CPU time the container can use. During each scheduling interval, the Linux kernel checks to see if this limit is exceeded. If so, the kernel waits before allowing the cgroup to resume execution. 

If several different containers (cgroups) want to run on a contended system, workloads with larger CPU requests are allocated more CPU time than workloads with small requests. The memory request is used during Pod scheduling. On a node that uses cgroups v2, the container runtime might use the memory request as a hint to set `memory.min` and `memory.low` values. 

If a container attempts to allocate more memory than this limit, the Linux kernel out-of-memory subsystem activates and intervenes by stopping one of the processes in the container that tried to allocate memory. The memory limit for the Pod or container can also apply to pages in memory-backed volumes, such as an emptyDir. 

The kubelet tracks `tmpfs` `emptyDir` volumes as container memory is used, rather than as local ephemeral storage. If a container exceeds its memory request and the node that it runs on becomes short of memory overall, the Pod’s container might be evicted. 

Important

A container might not exceed its CPU limit for extended periods. Container run times do not stop Pods or containers for excessive CPU usage. To determine whether a container cannot be scheduled or is being killed due to resource limits, see _Troubleshooting the Compliance Operator_. 

### 5.6.2.7. Schedule Pods with container resource requests

You can specify CPU and memory resource requests and limits for containers to ensure that pods are placed on nodes with sufficient capacity, preventing resource shortages. 

Although memory or CPU resource usage on nodes is very low, the scheduler might still refuse to place a Pod on a node if the capacity check fails to protect against a resource shortage on a node. 

For each container, you can specify the following resource limits and request: 

```shell-session
spec.containers[].resources.limits.cpu
spec.containers[].resources.limits.memory
spec.containers[].resources.limits.hugepages-<size>
spec.containers[].resources.requests.cpu
spec.containers[].resources.requests.memory
spec.containers[].resources.requests.hugepages-<size>
```


Although you can specify requests and limits for only individual containers, it is also useful to consider the overall resource requests and limits for a pod. For a particular resource, a container resource request or limit is the sum of the resource requests or limits of that type for each container in the pod. 

**Example container resource requests and limits**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: images.my-company.example/app:v4
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
  - name: log-aggregator
    image: images.my-company.example/log-aggregator:v6
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
```


where: 

`spec.containers.resources.requests`
     Specifies that the container is requesting 64 Mi of memory and 250 m CPU. 
`spec.containers.resources.limits`
     Specifies the container’s limits are 128 Mi of memory and 500 m CPU. 

### 5.6.2.8. Additional resources

  * [Increasing Compliance Operator resource limits](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/compliance-operator#compliance-increasing-operator-limits_compliance-troubleshooting "5.6.8.2. Increasing Compliance Operator resource limits")
  * [Compliance Operator shows INCONSISTENT scan result with worker node](https://access.redhat.com/solutions/6970861)
  * [Managing Compliance Operator result and remediation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/compliance-operator#compliance-operator-remediation "5.6.6. Managing Compliance Operator result and remediation")



## 5.6.3. Propagating custom metadata to ComplianceCheckResult objects

Starting in Compliance Operator 1.9.0, add labels and annotations to `Rule` and `CustomRule` objects so matching metadata is displayed on `ComplianceCheckResult` objects after a scan. Downstream tools, dashboards, and ticketing workflows can use this metadata without maintaining a separate mapping. 

### 5.6.3.1. Understanding custom metadata on rules and check results

When the Compliance Operator creates or updates a `ComplianceCheckResult` object for a check that Open Security Content Automation Protocol (OpenSCAP) evaluates, it copies custom labels and annotations from the corresponding `Rule` object in the same namespace. 

For checks that the Common Expression Language (CEL) scanner evaluates from a `CustomRule`, the Operator copies custom metadata from that `CustomRule` instead. 

Custom metadata is any label or annotation whose name is not managed by the Compliance Operator or core Kubernetes namespaces. Some keys are reserved, so user-supplied values never replace the Operator values for those keys. Examples include the following: 

  * Keys starting with `compliance.openshift.io/`
  * Keys starting with `complianceoperator.openshift.io/`
  * Keys starting with `complianceascode.io/`
  * Keys where the domain contains `kubernetes.io/` (such as `kubernetes.io/name` or `app.kubernetes.io/`) 
  * Keys where the domain contains `k8s.io/` (such as `k8s.io/component` or `node.k8s.io/instance-type`) 



Note

Metadata that you set on `TailoredProfile`, `ScanSettingBinding`, or other orchestration resources is not propagated to individual `ComplianceCheckResult` objects. Attach metadata on the `Rule` or `CustomRule` that owns the check. 

Note

Custom metadata on `ComplianceRemediation` objects is not covered by this feature. 

Profile bundle updates
     When a `ProfileBundle` refreshes profile content, the Operator merges user-defined annotations on `Rule` objects with parser-managed annotations so your keys remain while Operator and content fields stay current. 
Failure behavior
     If the Operator cannot build its in-memory index of `Rule` objects during aggregation, it logs a warning and still creates scan results without your custom metadata. If a label value violates Kubernetes length or syntax rules, the Operator can fail to create that specific `ComplianceCheckResult` while other results continue. 

For more background on the enhancement, see Additional resources. 

### 5.6.3.2. Adding custom labels and annotations to a Rule object

You can attach custom labels and annotations to a `Rule` that Open Security Content Automation Protocol (OpenSCAP) evaluates, and verify that they are displayed on the aggregated `ComplianceCheckResult` after the next scan. 

**Prerequisites**

  * You have installed Compliance Operator 1.9.0 or later. 
  * You have access to the `openshift-compliance` namespace (or the namespace where your rules and scans run). 
  * You identified the `Rule` object name and the `ComplianceScan` that evaluates it. 



**Procedure**

  1. Add custom labels to the rule. Replace `<rule_name>` with your `Rule` object name, and adjust labels as needed with the following command: 

```shell-session
$ oc label rule.compliance/<rule_name> \
  business-unit=payments \
  risk-tier=critical \
  -n openshift-compliance
```


  2. Add custom annotations with the following command: 

```shell-session
$ oc annotate rule.compliance/<rule_name> \
  internal-id=SEC-4021 \
  exception-ticket=JIRA-123 \
  -n openshift-compliance
```


Long or free-form values are better suited to annotations than labels because of Kubernetes label length limits. 

  3. Trigger a new scan or wait for the next scheduled run. For example, to request a rescan of an existing `ComplianceScan` named `ocp4-cis` use the following command: 

```shell-session
$ oc annotate compliancescan ocp4-cis \
  compliance.openshift.io/rescan= \
  -n openshift-compliance
```


  4. After the scan finishes, list `ComplianceCheckResult` objects that carry your label using the following command: 

```shell-session
$ oc get compliancecheckresults \
  -l business-unit=payments \
  -n openshift-compliance
```


  5. Confirm an annotation on a specific result with the following command: 

```shell-session
$ oc get compliancecheckresult <result_name> \
  -o jsonpath='{.metadata.annotations.internal-id}' \
  -n openshift-compliance
```


Replace `<result_name>` with the `ComplianceCheckResult` name for your rule. 

  6. Optional: Verify that a user annotation survives a `ProfileBundle` content image update using the following command. 

```shell-session
$ oc get rule.compliance/<rule_name> \
  -o jsonpath='{.metadata.annotations.exception-ticket}' \
  -n openshift-compliance
```


After the profile parser reconciles the `Rule`, your key should still be present. 




### 5.6.3.3. Adding custom labels and annotations to a CustomRule object

For platform checks implemented as a `CustomRule` object and evaluated by the Common Expression Language (CEL) scanner, define labels and annotations on the `CustomRule` metadata. The Compliance Operator copies non-reserved entries onto each generated `ComplianceCheckResult`. 

**Prerequisites**

  * You have installed Compliance Operator 1.9.0 or later. 
  * You use a `TailoredProfile` (or equivalent workflow) that enables your `CustomRule` for a CEL profile scan. 



**Procedure**

  1. Create a `CustomRule` object that includes your metadata in `metadata.labels` and `metadata.annotations`. The following example defines a platform CEL check; replace names, expressions, and metadata with values appropriate for your environment: 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: CustomRule
metadata:
  name: check-pod-security-standard
  namespace: openshift-compliance
  labels:
    break_severity: critical
    weakness_score: "9.5"
  annotations:
    internal-id: SEC-5500
    audit-contact: platform-security-team
spec:
  id: check-pod-security-standard
  title: "Ensure Pod Security Standards are enforced"
  severity: high
  checkType: Platform
  scannerType: CEL
  expression: |
    namespaces.items.all(ns,
      has(ns.metadata.labels) &&
      "pod-security.kubernetes.io/enforce" in ns.metadata.labels
    )
  failureReason: "One or more namespaces do not enforce Pod Security Standards"
  inputs:
    - name: namespaces
      kubernetesInputSpec:
        apiVersion: v1
        resource: namespaces
```


  2. Apply the manifest by running the following command: 

```shell-session
$ oc apply -f custom-rule.yaml
```


  3. Reference the `CustomRule` object from a `TailoredProfile`, for example: 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: TailoredProfile
metadata:
  name: custom-cel-profile
  namespace: openshift-compliance
spec:
  title: "Custom CEL profile"
  description: "Profile with custom CEL rules"
  enableRules:
    - name: check-pod-security-standard
      rationale: "Enforce pod security standards"
      kind: CustomRule
```


  4. Bind the tailored profile with a `ScanSettingBinding` and run the scan using your normal workflow. 
  5. After the scan completes, query results by a custom label by running the following command: 

```shell-session
$ oc get compliancecheckresults \
  -l break_severity=critical \
  -n openshift-compliance
```


  6. Identify the `ComplianceCheckResult` name for your `CustomRule` object in the scan output, for example by listing results in the namespace and filtering by labels or name. 
  7. Read a propagated annotation from that object by running the following command: 

```shell-session
$ oc get compliancecheckresult <result_name> \
  -o jsonpath='{.metadata.annotations.internal-id}' \
  -n openshift-compliance
```


## 5.6.4. Tailoring the Compliance Operator

Although the Compliance Operator includes ready-to-use profiles, you must modify the profiles to fit your organization’s requirements. The process of modifying a profile is called _tailoring_. 

The Compliance Operator provides the `TailoredProfile` object to help tailor profiles. 

### 5.6.4.1. Create a new tailored profile

You can write a tailored profile from scratch by using the `TailoredProfile` object. Set an appropriate `title` and `description` and leave the `extends` field empty. 

Indicate to the Compliance Operator what type of scan this custom profile will generate: 

  * Node scan: Scans the operating system. 
  * Platform scan: Scans the OpenShift Container Platform configuration. 



**Procedure**

  * Set the following annotation on the `TailoredProfile` object: 

**Example`new-profile.yaml`**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: TailoredProfile
metadata:
  name: new-profile
  annotations:
    compliance.openshift.io/product-type: Node
spec:
  extends: ocp4-cis-node
  description: My custom profile
  title: Custom profile
  enableRules:
    - name: ocp4-etcd-unique-ca
      rationale: We really need to enable this
  disableRules:
    - name: ocp4-file-groupowner-cni-conf
      rationale: This does not apply to the cluster
```


where: 

`metadata.annotations.compliance.openshift.io/product-type`
     Sets `Node` or `Platform` accordingly. 
`spec.extends`
     Optional field to specify the base profile. 
`spec.description`
     Specifies the function of the new `TailoredProfile` object. 
`spec.title`
    

Specifies a title for the `TailoredProfile` object. 

Note

Adding the `-node` suffix to the `name` field of the `TailoredProfile` object is similar to adding the `Node` product type annotation and generates an operating system scan. 




### 5.6.4.2. Use tailored profiles to extend existing ProfileBundles

Although the `TailoredProfile` CR enables the most common tailoring operations, you can use the XCCDF (Extensible Configuration Checklist Description Format) standard for even more flexibility in tailoring OpenSCAP profiles. 

In addition, if your organization has been using OpenScap previously, you might have an existing XCCDF tailoring file and can reuse it. 

The `ComplianceSuite` object has an optional `TailoringConfigMap` attribute that you can point to a custom tailoring file. The value of the `TailoringConfigMap` attribute is a name of a config map, which must contain a key called `tailoring.xml` and the value of this key is the tailoring contents. 

**Procedure**

  1. Browse the available rules for the Red Hat Enterprise Linux CoreOS (RHCOS) `ProfileBundle`: 

```shell-session
$ oc get rules.compliance -n openshift-compliance -l compliance.openshift.io/profile-bundle=rhcos4
```


  2. Browse the available variables in the same `ProfileBundle`: 

```shell-session
$ oc get variables.compliance -n openshift-compliance -l compliance.openshift.io/profile-bundle=rhcos4
```


  3. Create a tailored profile named `nist-moderate-modified`: 

     1. Choose which rules you want to add to the `nist-moderate-modified` tailored profile. This example extends the `rhcos4-moderate` profile by disabling two rules and changing one value. Use the `rationale` value to describe why these changes were made: 

**Example`new-profile-node.yaml`**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: TailoredProfile
metadata:
  name: nist-moderate-modified
spec:
  extends: rhcos4-moderate
  description: NIST moderate profile
  title: My modified NIST moderate profile
  disableRules:
  - name: rhcos4-file-permissions-var-log-messages
    rationale: The file contains logs of error messages in the system
  - name: rhcos4-account-disable-post-pw-expiration
    rationale: No need to check this as it comes from the IdP
  setValues:
  - name: rhcos4-var-selinux-state
    rationale: Organizational requirements
    value: permissive
```


Table 5.10. Attributes for spec variablesAttribute| Description  
---|---  
`extends` |  Name of the `Profile` object upon which this `TailoredProfile` is built.   
`title` |  Human-readable title of the `TailoredProfile`.   
`disableRules` |  A list of name and rationale pairs. Each name refers to a name of a rule object that is to be disabled. The rationale value is human-readable text describing why the rule is disabled.   
`manualRules` |  A list of name and rationale pairs. When a manual rule is added, the check result status will always be `manual` and remediation will not be generated. This attribute is automatic and by default has no values when set as a manual rule.   
`enableRules` |  A list of name and rationale pairs. Each name refers to a name of a rule object that is to be enabled. The rationale value is human-readable text describing why the rule is enabled.   
`description` |  Human-readable text describing the `TailoredProfile`.   
`setValues` |  A list of name, rationale, and value groupings. Each name refers to a name of the value set. The rationale is human-readable text describing the set. The value is the actual setting.   
Show more

     2. Add the `tailoredProfile.spec.manualRules` attribute: 

**Example`tailoredProfile.spec.manualRules.yaml`**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: TailoredProfile
metadata:
  name: ocp4-manual-scc-check
spec:
  extends: ocp4-cis
  description: This profile extends ocp4-cis by forcing the SCC check to always return MANUAL
  title: OCP4 CIS profile with manual SCC check
  manualRules:
    - name: ocp4-scc-limit-container-allowed-capabilities
      rationale: We use third party software that installs its own SCC with extra privileges
```


     3. Create the `TailoredProfile` object: 

```shell-session
$ oc create -n openshift-compliance -f new-profile-node.yaml
```


        * The `TailoredProfile` object is created in the default `openshift-compliance` namespace. 

**Example output**

```shell-session
tailoredprofile.compliance.openshift.io/nist-moderate-modified created
```


  4. Define the `ScanSettingBinding` object to bind the new `nist-moderate-modified` tailored profile to the default `ScanSetting` object. 

**Example`new-scansettingbinding.yaml`**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSettingBinding
metadata:
  name: nist-moderate-modified
profiles:
  - apiGroup: compliance.openshift.io/v1alpha1
    kind: Profile
    name: ocp4-moderate
  - apiGroup: compliance.openshift.io/v1alpha1
    kind: TailoredProfile
    name: nist-moderate-modified
settingsRef:
  apiGroup: compliance.openshift.io/v1alpha1
  kind: ScanSetting
  name: default
```


  5. Create the `ScanSettingBinding` object: 

```shell-session
$ oc create -n openshift-compliance -f new-scansettingbinding.yaml
```


**Example output**

```shell-session
scansettingbinding.compliance.openshift.io/nist-moderate-modified created
```


## 5.6.5. Retrieving Compliance Operator raw results

When proving compliance for your OpenShift Container Platform cluster, you might need to provide the scan results for auditing purposes. 

### 5.6.5.1. Obtain Compliance Operator raw results from a persistent volume

You can view the results of Compliance Operator scans for auditing purposes. The Operator stores the raw results in a persistent volume in Asset Reporting Format (ARF). 

**Procedure**

  1. Explore the `ComplianceSuite` object: 

```shell-session
$ oc get compliancesuites nist-moderate-modified \
-o json -n openshift-compliance | jq '.status.scanStatuses[].resultsStorage'
```


**Example output**

```plaintext
{
     "name": "ocp4-moderate",
     "namespace": "openshift-compliance"
}
{
     "name": "nist-moderate-modified-master",
     "namespace": "openshift-compliance"
}
{
     "name": "nist-moderate-modified-worker",
     "namespace": "openshift-compliance"
}
```


This shows the persistent volume claims where the raw results are accessible. 

  2. Verify the raw data location by using the name and namespace of one of the results: 

```shell-session
$ oc get pvc -n openshift-compliance rhcos4-moderate-worker
```


**Example output**

```shell-session
NAME                 	STATUS   VOLUME                                 	CAPACITY   ACCESS MODES   STORAGECLASS   AGE
rhcos4-moderate-worker   Bound	pvc-548f6cfe-164b-42fe-ba13-a07cfbc77f3a   1Gi    	RWO        	gp2        	92m
```


  3. Fetch the raw results by spawning a pod that mounts the volume and copying the results: 

```shell-session
$ oc create -n openshift-compliance -f pod.yaml
```


**Example pod.yaml**

```yaml
apiVersion: "v1"
kind: Pod
metadata:
  name: pv-extract
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: pv-extract-pod
      image: registry.access.redhat.com/ubi9/ubi
      command: ["sleep", "3000"]
      volumeMounts:
      - mountPath: "/workers-scan-results"
        name: workers-scan-vol
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
  volumes:
    - name: workers-scan-vol
      persistentVolumeClaim:
        claimName: rhcos4-moderate-worker
```


  4. After the pod is running, download the results: 

```shell-session
$ oc cp pv-extract:/workers-scan-results -n openshift-compliance .
```


Important

Spawning a pod that mounts the persistent volume will keep the claim as `Bound`. If the volume’s storage class in use has permissions set to `ReadWriteOnce`, the volume is only mountable by one pod at a time. You must delete the pod upon completion, or it will not be possible for the Operator to schedule a pod and continue storing results in this location. 

  5. After the extraction is complete, the pod can be deleted: 

```shell-session
$ oc delete pod pv-extract -n openshift-compliance
```


## 5.6.6. Managing Compliance Operator result and remediation

You can review compliance scan results and apply remediations to resolve failing rules. Remediations are not applied automatically, so you can verify each change before applying it to your cluster. 

Important

Full remediation for Federal Information Processing Standards (FIPS) compliance requires enabling FIPS mode for the cluster. To enable FIPS mode, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see Installing the system in FIPS mode. 

FIPS mode is supported on the following architectures: 

  * `x86_64`
  * `ppc64le`
  * `s390x`



### 5.6.6.1. Filters for compliance check results

You can use the labels in the `ComplianceCheckResult` objects to query the checks and decide on the next steps after the results are generated. 

List checks that belong to a specific suite: 

```shell-session
$ oc get -n openshift-compliance compliancecheckresults \
  -l compliance.openshift.io/suite=workers-compliancesuite
```


List checks that belong to a specific scan: 

```shell-session
$ oc get -n openshift-compliance compliancecheckresults \
-l compliance.openshift.io/scan-name=workers-scan
```


Not all `ComplianceCheckResult` objects create `ComplianceRemediation` objects. Only `ComplianceCheckResult` objects that can be remediated automatically do. A `ComplianceCheckResult` object has a related remediation if it is labeled with the `compliance.openshift.io/automated-remediation` label. The name of the remediation is the same as the name of the check. 

List all failing checks that can be remediated automatically: 

```shell-session
$ oc get -n openshift-compliance compliancecheckresults \
-l 'compliance.openshift.io/check-status=FAIL,compliance.openshift.io/automated-remediation'
```


List all failing checks sorted by severity: 

```shell-session
$ oc get compliancecheckresults -n openshift-compliance \
-l 'compliance.openshift.io/check-status=FAIL,compliance.openshift.io/check-severity=high'
```


**Example output**

```shell-session
NAME                                                           STATUS   SEVERITY
nist-moderate-modified-master-configure-crypto-policy          FAIL     high
nist-moderate-modified-master-coreos-pti-kernel-argument       FAIL     high
nist-moderate-modified-master-disable-ctrlaltdel-burstaction   FAIL     high
nist-moderate-modified-master-disable-ctrlaltdel-reboot        FAIL     high
nist-moderate-modified-master-enable-fips-mode                 FAIL     high
nist-moderate-modified-master-no-empty-passwords               FAIL     high
nist-moderate-modified-master-selinux-state                    FAIL     high
nist-moderate-modified-worker-configure-crypto-policy          FAIL     high
nist-moderate-modified-worker-coreos-pti-kernel-argument       FAIL     high
nist-moderate-modified-worker-disable-ctrlaltdel-burstaction   FAIL     high
nist-moderate-modified-worker-disable-ctrlaltdel-reboot        FAIL     high
nist-moderate-modified-worker-enable-fips-mode                 FAIL     high
nist-moderate-modified-worker-no-empty-passwords               FAIL     high
nist-moderate-modified-worker-selinux-state                    FAIL     high
ocp4-moderate-configure-network-policies-namespaces            FAIL     high
ocp4-moderate-fips-mode-enabled-on-all-nodes                   FAIL     high
```


List all failing checks that must be remediated manually: 

```shell-session
$ oc get -n openshift-compliance compliancecheckresults \
-l 'compliance.openshift.io/check-status=FAIL,!compliance.openshift.io/automated-remediation'
```


The manual remediation steps are typically stored in the `description` attribute in the `ComplianceCheckResult` object. 

Table 5.11. ComplianceCheckResult StatusComplianceCheckResult Status| Description  
---|---  
PASS  |  Compliance check ran to completion and passed.   
FAIL  |  Compliance check ran to completion and failed.   
INFO  |  Compliance check ran to completion and found something not severe enough to be considered an error.   
MANUAL  |  Compliance check does not have a way to automatically assess the success or failure and must be checked manually.   
INCONSISTENT  |  Compliance check reports different results from different sources, typically cluster nodes.   
ERROR  |  Compliance check ran, but could not complete properly.   
NOT-APPLICABLE  |  Compliance check did not run because it is not applicable or not selected.   
Show more

### 5.6.6.2. Review a remediation

You can review a `ComplianceRemediation` object and the `ComplianceCheckResult` object to understand what a check verifies, its severity and security controls, and how the remediation fixes the issue. After the first scan, check for remediations with the state `MissingDependencies`. 

The `ComplianceCheckResult` object includes human-readable descriptions of what the check does and what security hardening it enforces. 

The remediation payload is stored in the `spec.current` attribute. The payload can be any Kubernetes object, but because this remediation was produced by a node scan, the remediation payload in the following example is a `MachineConfig` object. For Platform scans, the remediation payload is often a different kind of an object (for example, a `ConfigMap` or `Secret` object). Typically, applying that remediation is up to the administrator. Otherwise, the Compliance Operator would have required a very broad set of permissions to manipulate any generic Kubernetes object. An example of remediating a Platform check is provided later in the text. 

To see exactly what the remediation does when applied, the `MachineConfig` object contents use the Ignition objects for the configuration. See the link to "Ignition specification" in Additional resources for further information about the format. In the following example, the `spec.config.storage.files[0].path` attribute specifies the file that is being created by this remediation (`/etc/sysctl.d/75-sysctl_net_ipv4_conf_all_accept_redirects.conf`) and the `spec.config.storage.files[0].contents.source` attribute specifies the contents of that file. 

**Procedure**

  1. Review the example of a check and a remediation called `sysctl-net-ipv4-conf-all-accept-redirects`. This example is redacted to only show `spec` and `status` and omits `metadata`: 

```yaml
spec:
  apply: false
  current:
  object:
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfig
    spec:
      config:
        ignition:
          version: 3.2.0
        storage:
          files:
            - path: /etc/sysctl.d/75-sysctl_net_ipv4_conf_all_accept_redirects.conf
              mode: 0644
              contents:
                source: data:,net.ipv4.conf.all.accept_redirects%3D0
  outdated: {}
status:
  applicationState: NotApplied
```


  2. Use the following Python script to view the contents: 

Note

The contents of the files are URL-encoded. 

```shell-session
$ echo "net.ipv4.conf.all.accept_redirects%3D0" | python3 -c "import sys, urllib.parse; print(urllib.parse.unquote(''.join(sys.stdin.readlines())))"
```


**Example output**

```shell-session
net.ipv4.conf.all.accept_redirects=0
```


Important

The Compliance Operator does not automatically resolve dependency issues that can occur between remediations. Users should perform a rescan after remediations are applied to ensure accurate results. 




### 5.6.6.3. Apply remediation when using customized machine config pools

When you create a custom `MachineConfigPool`, add a label to the `MachineConfigPool` so that `machineConfigPoolSelector` present in the `KubeletConfig` can match the label with `MachineConfigPool`. 

Important

Do not set `protectKernelDefaults: false` in the `KubeletConfig` file, because the `MachineConfigPool` object might fail to unpause unexpectedly after the Compliance Operator finishes applying remediation. 

**Procedure**

  1. List the nodes. 

```shell-session
$ oc get nodes -n openshift-compliance
```


**Example output**

```shell-session
NAME                                       STATUS  ROLES  AGE    VERSION
ip-10-0-128-92.us-east-2.compute.internal  Ready   master 5h21m  v1.35.4
ip-10-0-158-32.us-east-2.compute.internal  Ready   worker 5h17m  v1.35.4
ip-10-0-166-81.us-east-2.compute.internal  Ready   worker 5h17m  v1.35.4
ip-10-0-171-170.us-east-2.compute.internal Ready   master 5h21m  v1.35.4
ip-10-0-197-35.us-east-2.compute.internal  Ready   master 5h22m  v1.35.4
```


  2. Add a label to nodes. 

```shell-session
$ oc -n openshift-compliance \
label node ip-10-0-166-81.us-east-2.compute.internal \
node-role.kubernetes.io/<machine_config_pool_name>=
```


**Example output**

```shell-session
node/ip-10-0-166-81.us-east-2.compute.internal labeled
```


  3. Create custom `MachineConfigPool` CR. 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: <machine_config_pool_name>
  labels:
    pools.operator.machineconfiguration.openshift.io/<machine_config_pool_name>: ''
spec:
  machineConfigSelector:
  matchExpressions:
  - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,<machine_config_pool_name>]}
  nodeSelector:
  matchLabels:
    node-role.kubernetes.io/<machine_config_pool_name>: ""
```


where: 

`metadata.labels.pools.operator.machineconfiguration.openshift.io/<machine_config_pool_name>`
     The `labels` field defines the label name to add for the machine config pool (MCP). 

  4. Verify MCP created successfully. 

```shell-session
$ oc get mcp -w
```


### 5.6.6.4. Evaluate KubeletConfig rules against default configuration values

The Compliance Operator uses the Node/Proxy API to evaluate `KubeletConfig` object rules against actual node configurations, preventing inaccurate results caused by incomplete configuration files and default values for missing options. 

OpenShift Container Platform infrastructure might contain incomplete configuration files at run time, and nodes assume default configuration values for missing configuration options. Some configuration options can be passed as command-line arguments. As a result, the Compliance Operator cannot verify if the configuration file on the node is complete because it might be missing options used in the rule checks. 

To prevent false negative results where the default configuration value passes a check, the Compliance Operator uses the Node/Proxy API to fetch the configuration for each node in a node pool, then all configuration options that are consistent across nodes in the node pool are stored in a file that represents the configuration for all nodes within that node pool. This increases the accuracy of the scan results. 

No additional configuration changes are required to use this feature with default `master` and `worker` node pools configurations. 

### 5.6.6.5. Scan custom node pools

The Compliance Operator does not maintain a copy of each node pool configuration. 

The Compliance Operator aggregates consistent configuration options for all nodes within a single node pool into one copy of the configuration file. The Compliance Operator then uses the configuration file for a particular node pool to evaluate rules against nodes within that pool. 

**Procedure**

  1. Add the `example` role to the `ScanSetting` object that will be stored in the `ScanSettingBinding` CR: 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSetting
metadata:
  name: default
  namespace: openshift-compliance
rawResultStorage:
  rotation: 3
  size: 1Gi
roles:
- worker
- master
- example
scanTolerations:
- effect: NoSchedule
  key: node-role.kubernetes.io/master
  operator: Exists
schedule: '0 1 * * *'
```


  2. Create a scan that uses the `ScanSettingBinding` CR: 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSettingBinding
metadata:
  name: cis
  namespace: openshift-compliance
profiles:
- apiGroup: compliance.openshift.io/v1alpha1
  kind: Profile
  name: ocp4-cis
- apiGroup: compliance.openshift.io/v1alpha1
  kind: Profile
  name: ocp4-cis-node
settingsRef:
  apiGroup: compliance.openshift.io/v1alpha1
  kind: ScanSetting
  name: default
```


**Verification**

  * The Platform KubeletConfig rules are checked through the `Node/Proxy` object. You can find those rules by running the following command: 

```shell-session
$ oc get rules -o json | jq '.items[] | select(.checkType == "Platform") | select(.metadata.name | contains("ocp4-kubelet-")) | .metadata.name'
```


### 5.6.6.6. Remediate KubeletConfig sub pools

You can apply `KubeletConfig` remediation labels to `MachineConfigPool` sub-pools. 

**Procedure**

  * Add a label to the sub-pool `MachineConfigPool` CR: 

```shell-session
$ oc label mcp <sub-pool-name> pools.operator.machineconfiguration.openshift.io/<sub-pool-name>=
```


### 5.6.6.7. Apply a remediation

The boolean attribute `spec.apply` controls whether the remediation should be applied by the Compliance Operator. You can apply the remediation by setting the attribute to `true`. 

**Procedure**

  1. Apply the remediation by setting the attribute to `true`: 

```shell-session
$ oc -n openshift-compliance \
patch complianceremediations/<scan-name>-sysctl-net-ipv4-conf-all-accept-redirects \
--patch '{"spec":{"apply":true}}' --type=merge
```


After the Compliance Operator processes the applied remediation, the `status.ApplicationState` attribute would change to **Applied** or to **Error** if incorrect. When a machine config remediation is applied, that remediation along with all other applied remediations are rendered into a `MachineConfig` object named `75-$scan-name-$suite-name`. That `MachineConfig` object is subsequently rendered by the Machine Config Operator and finally applied to all the nodes in a machine config pool by an instance of the machine control daemon running on each node. 

Note that when the Machine Config Operator applies a new `MachineConfig` object to nodes in a pool, all the nodes belonging to the pool are rebooted. This might be inconvenient when applying multiple remediations, each of which re-renders the composite `75-$scan-name-$suite-name` `MachineConfig` object. To prevent applying the remediation immediately, you can pause the machine config pool by setting the `.spec.paused` attribute of a `MachineConfigPool` object to `true`. 

  2. Optionally, the Compliance Operator can apply remediations automatically. Set `autoApplyRemediations: true` in the `ScanSetting` top-level object. 

Warning

Applying remediations automatically should only be done with careful consideration. 

Important

The Compliance Operator does not automatically resolve dependency issues that can occur between remediations. Users should perform a rescan after remediations are applied to ensure accurate results. 




### 5.6.6.8. Remediate a platform check manually

You must manually remediate checks from Platform scans so you can fix findings that the Compliance Operator cannot apply automatically. 

Manual remediations are necessary for the following reasons: 

  * It is not always possible to automatically determine the value that must be set. One of the checks requires that a list of allowed registries is provided, but the scanner has no way of knowing which registries the organization wants to allow. 
  * Different checks modify different API objects, requiring automated remediation to possess `root` or superuser access to modify objects in the cluster, which is not advised. 



**Procedure**

  1. The example below uses the `ocp4-ocp-allowed-registries-for-import` rule, which would fail on a default OpenShift Container Platform installation. Inspect the rule `oc get rule.compliance/ocp4-ocp-allowed-registries-for-import -oyaml`, the rule is to limit the registries the users are allowed to import images from by setting the `allowedRegistriesForImport` attribute, The _warning_ attribute of the rule also shows the API object checked, so it can be modified and remediate the issue: 

```shell-session
$ oc edit image.config.openshift.io/cluster
```


**Example output**

```yaml
apiVersion: config.openshift.io/v1
kind: Image
metadata:
  annotations:
    release.openshift.io/create-only: "true"
  creationTimestamp: "2020-09-10T10:12:54Z"
  generation: 2
  name: cluster
  resourceVersion: "363096"
  selfLink: /apis/config.openshift.io/v1/images/cluster
  uid: 2dcb614e-2f8a-4a23-ba9a-8e33cd0ff77e
spec:
  allowedRegistriesForImport:
  - domainName: registry.redhat.io
status:
  externalRegistryHostnames:
  - default-route-openshift-image-registry.apps.user-cluster-09-10-12-07.devcluster.openshift.com
  internalRegistryHostname: image-registry.openshift-image-registry.svc:5000
```


  2. Re-run the scan: 

```shell-session
$ oc -n openshift-compliance \
annotate compliancescans/rhcos4-e8-worker compliance.openshift.io/rescan=
```


### 5.6.6.9. Update remediations

When you update compliance content to a newer version, the Compliance Operator marks previously applied remediations as **Outdated**. Review these remediations and apply the updated versions to ensure your nodes use the latest configuration. 

The previously applied remediation contents would then be stored in the `spec.outdated` attribute of a `ComplianceRemediation` object and the new updated contents would be stored in the `spec.current` attribute. After updating the content to a newer version, the administrator then needs to review the remediation. If the `spec.outdated` attribute exists, it would be used to render the resulting `MachineConfig` object. After the `spec.outdated` attribute is removed, the Compliance Operator re-renders the resulting `MachineConfig` object, which causes the Operator to push the configuration to the nodes. 

Important

The Compliance Operator does not automatically resolve dependency issues that can occur between remediations. Users should perform a rescan after remediations are applied to ensure accurate results. 

**Procedure**

  1. Search for any outdated remediations: 

```shell-session
$ oc -n openshift-compliance get complianceremediations \
-l complianceoperator.openshift.io/outdated-remediation=
```


**Example output**

```shell-session
NAME                              STATE
workers-scan-no-empty-passwords   Outdated
```


Note

The currently applied remediation is stored in the `Outdated` attribute and the new, unapplied remediation is stored in the `Current` attribute. If you are satisfied with the new version, remove the `Outdated` field. If you want to keep the updated content, remove the `Current` and `Outdated` attributes. 

  2. Apply the newer version of the remediation: 

```shell-session
$ oc -n openshift-compliance patch complianceremediations workers-scan-no-empty-passwords \
--type json -p '[{"op":"remove", "path":/spec/outdated}]'
```


  3. The remediation state will switch from `Outdated` to `Applied`: 

```shell-session
$ oc get -n openshift-compliance complianceremediations workers-scan-no-empty-passwords
```


**Example output**

```shell-session
NAME                              STATE
workers-scan-no-empty-passwords   Applied
```


  4. Verify that the nodes apply the newer remediation version and reboot. 



### 5.6.6.10. Unapply a remediation

You can unapply a remediation that was previously applied to roll back a change when you need to revert it. 

Important

The Compliance Operator does not automatically resolve dependency issues that can occur between remediations. Users should perform a rescan after remediations are applied to ensure accurate results. 

**Procedure**

  1. Set the `apply` flag to `false`: 

```shell-session
$ oc -n openshift-compliance \
patch complianceremediations/rhcos4-moderate-worker-sysctl-net-ipv4-conf-all-accept-redirects \
--patch '{"spec":{"apply":false}}' --type=merge
```


  2. Verify that the remediation status has changed to `NotApplied` and the composite `MachineConfig` object is re-rendered to not include the remediation. 

Important

All affected nodes with the remediation will be rebooted. 




### 5.6.6.11. Remove a KubeletConfig remediation

`KubeletConfig` remediations are included in node-level profiles. To remove a `KubeletConfig` remediation, you must manually remove it from the `KubeletConfig` objects. 

**Procedure**

  1. Locate the `scan-name` and compliance check for the `one-rule-tp-node-master-kubelet-eviction-thresholds-set-hard-imagefs-available` remediation: 

```shell-session
$ oc -n openshift-compliance get remediation \ one-rule-tp-node-master-kubelet-eviction-thresholds-set-hard-imagefs-available -o yaml
```


**Example output**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ComplianceRemediation
metadata:
  annotations:
    compliance.openshift.io/xccdf-value-used: var-kubelet-evictionhard-imagefs-available
  creationTimestamp: "2022-01-05T19:52:27Z"
  generation: 1
  labels:
    compliance.openshift.io/scan-name: one-rule-tp-node-master
    compliance.openshift.io/suite: one-rule-ssb-node
  name: one-rule-tp-node-master-kubelet-eviction-thresholds-set-hard-imagefs-available
  namespace: openshift-compliance
  ownerReferences:
  - apiVersion: compliance.openshift.io/v1alpha1
    blockOwnerDeletion: true
    controller: true
    kind: ComplianceCheckResult
    name: one-rule-tp-node-master-kubelet-eviction-thresholds-set-hard-imagefs-available
    uid: fe8e1577-9060-4c59-95b2-3e2c51709adc
  resourceVersion: "84820"
  uid: 5339d21a-24d7-40cb-84d2-7a2ebb015355
spec:
  apply: true
  current:
    object:
      apiVersion: machineconfiguration.openshift.io/v1
      kind: KubeletConfig
      spec:
        kubeletConfig:
          evictionHard:
            imagefs.available: 10%
  outdated: {}
  type: Configuration
status:
  applicationState: Applied
```


where: 

     * `metadata.labels.compliance.openshift.io/scan-name` specifies the scan name of the remediation. 
     * `spec.current.object.spec.kubeletConfig.evictionHard.imagefs.available` specifies the remediation that was added to the `KubeletConfig` objects. 

Note

If the remediation invokes an `evictionHard` kubelet configuration, you must specify all of the `evictionHard` parameters: `memory.available`, `nodefs.available`, `nodefs.inodesFree`, `imagefs.available`, and `imagefs.inodesFree`. If you do not specify all parameters, only the specified parameters are applied and the remediation will not function properly. 

  2. Remove the remediation: 

     1. Set `apply` to false for the remediation object: 

```shell-session
$ oc -n openshift-compliance patch \
complianceremediations/one-rule-tp-node-master-kubelet-eviction-thresholds-set-hard-imagefs-available \
-p '{"spec":{"apply":false}}' --type=merge
```


     2. Using the `scan-name`, find the `KubeletConfig` object that the remediation was applied to: 

```shell-session
$ oc -n openshift-compliance get kubeletconfig \
--selector compliance.openshift.io/scan-name=one-rule-tp-node-master
```


**Example output**

```shell-session
NAME                                 AGE
compliance-operator-kubelet-master   2m34s
```


     3. Manually remove the remediation, `imagefs.available: 10%`, from the `KubeletConfig` object: 

```shell-session
$ oc edit -n openshift-compliance KubeletConfig compliance-operator-kubelet-master
```


Important

All affected nodes with the remediation will be rebooted. 

Note

You must also exclude the rule from any scheduled scans in your tailored profiles that auto-applies the remediation, otherwise, the remediation will be re-applied during the next scheduled scan. 




### 5.6.6.12. Inconsistent ComplianceScan

The `ScanSetting` object lists the node roles that the compliance scans generated from the `ScanSetting` or `ScanSettingBinding` objects would scan. Each node role usually maps to a machine config pool. 

Important

All machines in a machine config pool are expected to be identical and all scan results from the nodes in a pool should be identical. 

If a compliance scan results in an `INCONSISTENT` result, re-run the compliance scan to get a consistent result by annotating the scan with the `compliance.openshift.io/rescan=` option. 

The `ScanSetting` object lists the node roles that the compliance scans generated from the `ScanSetting` or `ScanSettingBinding` objects would scan. Each node role usually maps to a machine config pool. 

Because the number of machines in a pool might be quite large, the Compliance Operator attempts to find the most common state and list the nodes that differ from the common state. The most common state is stored in the `compliance.openshift.io/most-common-status` annotation and the annotation `compliance.openshift.io/inconsistent-source` contains pairs of `hostname:status` of check statuses that differ from the most common status. If no common state can be found, all the `hostname:status` pairs are listed in the `compliance.openshift.io/inconsistent-source annotation`. 

If possible, a remediation is still created so that the cluster can converge to a compliant status. However, this might not always be possible and correcting the difference between nodes must be done manually. 

**Procedure**

  * Re-run the compliance scan to get a consistent result by annotating the scan with the `compliance.openshift.io/rescan=` option: 

```shell-session
$ oc -n openshift-compliance \
annotate compliancescans/rhcos4-e8-worker compliance.openshift.io/rescan=
```


### 5.6.6.13. Additional resources

  * [Modifying nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-nodes-managing-about_nodes-nodes-managing)
  * [Ignition specification](https://coreos.github.io/ignition/specs/)
  * [Installing the system in FIPS mode](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/security_hardening/assembly_installing-the-system-in-fips-mode_security-hardening)



## 5.6.7. Performing advanced Compliance Operator tasks

As an advanced user, you can use options in the Compliance Operator for the purpose of debugging or integrating with existing tooling. 

### 5.6.7.1. Using the ComplianceSuite and ComplianceScan objects directly

You can define a `ComplianceSuite` object directly rather than using the `ScanSetting` and `ScanSettingBinding` objects to define the suites and scans. 

There following use cases are valid reasons to define a `ComplianceSuite` object: 

  * Specifying only a single rule to scan. This can be useful for debugging together with the `debug: true` attribute which increases the OpenSCAP scanner verbosity, as the debug mode tends to get quite verbose otherwise. Limiting the test to one rule helps to lower the amount of debug information. 
  * Providing a custom nodeSelector. In order for a remediation to be applicable, the nodeSelector must match a pool. 
  * Pointing the Scan to a bespoke config map with a tailoring file. 
  * For testing or development when the overhead of parsing profiles from bundles is not required. 



The following example shows a `ComplianceSuite` that scans the worker machines with only a single rule: 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ComplianceSuite
metadata:
  name: workers-compliancesuite
spec:
  scans:
    - name: workers-scan
      profile: xccdf_org.ssgproject.content_profile_moderate
      content: ssg-rhcos4-ds.xml
      contentImage: registry.redhat.io/compliance/openshift-compliance-content-rhel8@sha256:45dc...
      debug: true
      rule: xccdf_org.ssgproject.content_rule_no_direct_root_logins
      nodeSelector:
      node-role.kubernetes.io/worker: ""
```


The `ComplianceSuite` object and the `ComplianceScan` objects referred to above specify several attributes in a format that OpenSCAP expects. 

To discover the profile, content, or rule values, you can start by creating a similar Suite from `ScanSetting` and `ScanSettingBinding` or inspect the objects parsed from the `ProfileBundle` objects such as rules or profiles. Those objects contain the `xccdf_org` identifiers you can use to refer to them from a `ComplianceSuite`. 

### 5.6.7.2. Setting PriorityClass for ScanSetting scans

In some clusters, the default `PriorityClass` object can be too low to guarantee pods execute scans on time. To maintain compliance or guarantee automated scanning, you can set the `PriorityClass` variable to ensure the Compliance Operator is always given priority in resource constrained situations. 

**Prerequisites**

  * Optional: You have created a `PriorityClass` object. For more information, see "Configuring priority and preemption" in the _Additional resources_. 



**Procedure**

  * Set the `PriorityClass` variable: 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
strictNodeScan: true
metadata:
  name: default
  namespace: openshift-compliance
priorityClass: compliance-high-priority
kind: ScanSetting
showNotApplicable: false
rawResultStorage:
  nodeSelector:
    node-role.kubernetes.io/master: ''
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
schedule: 0 1 * * *
roles:
  - master
  - worker
scanTolerations:
  - operator: Exists
```


where: 

`PriorityClass`
     If the `PriorityClass` referenced in the `ScanSetting` cannot be found, the Operator will leave the `PriorityClass` empty, issue a warning, and continue scheduling scans without a `PriorityClass`. 




### 5.6.7.3. Using raw tailored profiles

Although the `TailoredProfile` CR enables the most common tailoring operations, you can use the XCCDF standard for more flexibility in tailoring OpenSCAP profiles. 

In addition, if your organization has been using OpenScap previously, you might have an existing XCCDF tailoring file and can reuse it. 

The `ComplianceSuite` object contains an optional `TailoringConfigMap` attribute that you can point to a custom tailoring file. The value of the `TailoringConfigMap` attribute is a name of a config map which must contain a key called `tailoring.xml` and the value of this key is the tailoring contents. 

**Procedure**

  1. Create the `ConfigMap` object from a file: 

```shell-session
$ oc -n openshift-compliance \
create configmap nist-moderate-modified \
--from-file=tailoring.xml=/path/to/the/tailoringFile.xml
```


  2. Reference the tailoring file in a scan that belongs to a suite: 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ComplianceSuite
metadata:
  name: workers-compliancesuite
spec:
  debug: true
  scans:
    - name: workers-scan
      profile: xccdf_org.ssgproject.content_profile_moderate
      content: ssg-rhcos4-ds.xml
      contentImage: registry.redhat.io/compliance/openshift-compliance-content-rhel8@sha256:45dc...
      debug: true
  tailoringConfigMap:
      name: nist-moderate-modified
  nodeSelector:
    node-role.kubernetes.io/worker: ""
```


### 5.6.7.4. Performing a rescan

You can re-run a scan on a defined schedule, such as every Monday or daily. It can also be useful to re-run a scan once after fixing a problem on a node. 

To perform a single scan, annotate the scan with the `compliance.openshift.io/rescan=` option: 

**Procedure**

  1. Annotate the scan to trigger a rescan: 

```shell-session
$ oc -n openshift-compliance \
annotate compliancescans/rhcos4-e8-worker compliance.openshift.io/rescan=
```


A rescan generates four additional `mc` for `rhcos-moderate` profile: 

  2. Verify the rescan generated machine configs: 

```shell-session
$ oc get mc
```


**Example output**

```shell-session
75-worker-scan-chronyd-or-ntpd-specify-remote-server
75-worker-scan-configure-usbguard-auditbackend
75-worker-scan-service-usbguard-enabled
75-worker-scan-usbguard-allow-hid-and-hub
```


Important

When the scan setting `default-auto-apply` label is applied, remediations are applied automatically and outdated remediations automatically update. If there are remediations that were not applied due to dependencies, or remediations that had been outdated, rescanning applies the remediations and might trigger a reboot. Only remediations that use `MachineConfig` objects trigger reboots. If there are no updates or dependencies to be applied, no reboot occurs. 




### 5.6.7.5. Set custom storage size for results

Although `ComplianceCheckResult` custom resources summarize one check across all scanned nodes, raw scanner results in ARF format are too large to store in etcd-backed Kubernetes resources. 

You can store them on a per-scan persistent volume and increase the default 1 GiB size by setting the `rawResultStorage.size` value in a `ScanSetting` or `ComplianceScan` resource. 

A related parameter is `rawResultStorage.rotation` which controls how many scans are retained in the PV before the older scans are rotated. The default value is 3, setting the rotation policy to 0 disables the rotation. Given the default rotation policy and an estimate of 100MB per a raw ARF scan report, you can calculate the right PV size for your environment. 

Because OpenShift Container Platform can be deployed in a variety of public clouds or bare metal, the Compliance Operator cannot determine available storage configurations. By default, the Compliance Operator will try to create the PV for storing results by using the default storage class of the cluster, but a custom storage class can be configured using the `rawResultStorage.StorageClassName` attribute. 

Important

If your cluster does not specify a default storage class, this attribute must be set. 

  * Configure the `ScanSetting` custom resource to use a standard storage class and create persistent volumes that are 10GB in size and keep the last 10 results: 

**Example`ScanSetting` CR**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSetting
metadata:
  name: default
  namespace: openshift-compliance
rawResultStorage:
  storageClassName: standard
  rotation: 10
  size: 10Gi
roles:
- worker
- master
scanTolerations:
- effect: NoSchedule
  key: node-role.kubernetes.io/master
  operator: Exists
schedule: '0 1 * * *'
```


### 5.6.7.6. Applying remediations generated by suite scans

Although you can use the `autoApplyRemediations` boolean parameter in a `ComplianceSuite` object, you can alternatively annotate the object with `compliance.openshift.io/apply-remediations`. This allows the Operator to apply all of the created remediations. 

**Procedure**

  * Apply the `compliance.openshift.io/apply-remediations` annotation by running the following command: 

```shell-session
$ oc -n openshift-compliance \
annotate compliancesuites/workers-compliancesuite compliance.openshift.io/apply-remediations=
```


### 5.6.7.7. Automatically update remediations

In some cases, a scan with newer content might mark remediations as `OUTDATED`. As an administrator, you can apply the `compliance.openshift.io/remove-outdated` annotation to apply new remediations and remove the outdated ones. 

Alternatively, set the `autoUpdateRemediations` flag in a `ScanSetting` or `ComplianceSuite` object to update the remediations automatically. 

**Procedure**

  * Apply the `compliance.openshift.io/remove-outdated` annotation: 

```shell-session
$ oc -n openshift-compliance \
annotate compliancesuites/workers-compliancesuite compliance.openshift.io/remove-outdated=
```


### 5.6.7.8. Creating a custom SCC for the Compliance Operator

In some environments, you must create a custom Security Context Constraints (SCC) file to ensure the correct permissions are available to the Compliance Operator `api-resource-collector`. 

**Prerequisites**

  * You must have `admin` privileges. 



**Procedure**

  1. Define the SCC in a YAML file named `restricted-adjusted-compliance.yaml`: 

**`SecurityContextConstraints` object definition**

```yaml
  allowHostDirVolumePlugin: false
  allowHostIPC: false
  allowHostNetwork: false
  allowHostPID: false
  allowHostPorts: false
  allowPrivilegeEscalation: true
  allowPrivilegedContainer: false
  allowedCapabilities: null
  apiVersion: security.openshift.io/v1
  defaultAddCapabilities: null
  fsGroup:
    type: MustRunAs
  kind: SecurityContextConstraints
  metadata:
    name: restricted-adjusted-compliance
  priority: 30
  readOnlyRootFilesystem: false
  requiredDropCapabilities:
  - KILL
  - SETUID
  - SETGID
  - MKNOD
  runAsUser:
    type: MustRunAsRange
  seLinuxContext:
    type: MustRunAs
  supplementalGroups:
    type: RunAsAny
  users:
  - system:serviceaccount:openshift-compliance:api-resource-collector
  volumes:
  - configMap
  - downwardAPI
  - emptyDir
  - persistentVolumeClaim
  - projected
  - secret
```


where: 

`priority`
     Specifies the priority of this SCC. This value must be higher than any other SCC that applies to the `system:authenticated` group. 
`system:serviceaccount:openshift-compliance:api-resource-collector`
     Specifies the Service Account used by Compliance Operator Scanner pod. 

  2. Create the SCC: 

```shell-session
$ oc create -n openshift-compliance  -f restricted-adjusted-compliance.yaml
```


**Example output**

```shell-session
securitycontextconstraints.security.openshift.io/restricted-adjusted-compliance created
```


**Verification**

  1. Verify the SCC was created: 

```shell-session
$ oc get -n openshift-compliance scc restricted-adjusted-compliance
```


**Example output**

```shell-session
NAME                             PRIV    CAPS         SELINUX     RUNASUSER        FSGROUP     SUPGROUP   PRIORITY   READONLYROOTFS   VOLUMES
restricted-adjusted-compliance   false   <no value>   MustRunAs   MustRunAsRange   MustRunAs   RunAsAny   30         false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
```


### 5.6.7.9. Additional resources

  * [Configuring priority and preemption](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-pods-priority-configuring_nodes-pods-priority)
  * [Managing security context constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#managing-pod-security-policies)



## 5.6.8. Troubleshooting Compliance Operator scans

You can use the information on how to troubleshoot the Compliance Operator to learn how to diagnose a problem or provide information in a bug report. 

When troubleshooting, review the following general tips: 

  * The Compliance Operator emits Kubernetes events when something important happens. You can either view all events in the cluster using the command: 

```shell-session
 $ oc get events -n openshift-compliance
```


Or view events for an object such as a scan using the command: 

```shell-session
$ oc describe -n openshift-compliance compliancescan/cis-compliance
```


  * The Compliance Operator consists of several controllers, approximately one per API object. It could be useful to filter only those controllers that correspond to the API object having issues. If a `ComplianceRemediation` cannot be applied, view the messages from the `remediationctrl` controller. You can filter the messages from a single controller by parsing with `jq`: 

```shell-session
$ oc -n openshift-compliance logs compliance-operator-775d7bddbd-gj58f \
    | jq -c 'select(.logger == "profilebundlectrl")'
```


  * The timestamps are logged as seconds since UNIX epoch in UTC. To convert them to a human-readable date, use `date -d @timestamp --utc`, for example: 

```shell-session
$ date -d @1596184628.955853 --utc
```


  * Many custom resources, most importantly `ComplianceSuite` and `ScanSetting`, allow the `debug` option to be set. Enabling this option increases verbosity of the OpenSCAP scanner pods, and some other helper pods. 
  * If a single rule is passing or failing unexpectedly, it could be helpful to run a single scan or a suite with only that rule to find the rule ID from the corresponding `ComplianceCheckResult` object and use it as the `rule` attribute value in a `Scan` CR. Then, together with the `debug` option enabled, the `scanner` container logs in the scanner pod would show the raw OpenSCAP logs. 



### 5.6.8.1. Anatomy of a scan

Before troubleshooting Compliance Operator scans, familiarize yourself with the components and stages of Compliance Operator scans. 

#### 5.6.8.1.1. Compliance sources

The compliance content is stored in `Profile` objects that are generated from a `ProfileBundle` object. The Compliance Operator creates a `ProfileBundle` object for the cluster and another for the cluster nodes. 

```shell-session
$ oc get -n openshift-compliance profilebundle.compliance
```


```shell-session
$ oc get -n openshift-compliance profile.compliance
```


The `ProfileBundle` objects are processed by deployments labeled with the `Bundle` name. To troubleshoot an issue with the `Bundle`, you can find the deployment and view logs of the pods in a deployment: 

```shell-session
$ oc logs -n openshift-compliance -lprofile-bundle=ocp4 -c profileparser
```


```shell-session
$ oc get -n openshift-compliance deployments,pods -lprofile-bundle=ocp4
```


```shell-session
$ oc logs -n openshift-compliance pods/<pod-name>
```


```shell-session
$ oc describe -n openshift-compliance pod/<pod-name> -c profileparser
```


#### 5.6.8.1.2. The ScanSetting and ScanSettingBinding objects lifecycle and debugging

With valid compliance content sources, the high-level `ScanSetting` and `ScanSettingBinding` objects can be used to generate `ComplianceSuite` and `ComplianceScan` objects: 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSetting
metadata:
  name: my-companys-constraints
debug: true
# For each role, a separate scan will be created pointing
# to a node-role specified in roles
roles:
  - worker
---
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSettingBinding
metadata:
  name: my-companys-compliance-requirements
profiles:
  # Node checks
  - name: rhcos4-e8
    kind: Profile
    apiGroup: compliance.openshift.io/v1alpha1
  # Cluster checks
  - name: ocp4-e8
    kind: Profile
    apiGroup: compliance.openshift.io/v1alpha1
settingsRef:
  name: my-companys-constraints
  kind: ScanSetting
  apiGroup: compliance.openshift.io/v1alpha1
```


Both `ScanSetting` and `ScanSettingBinding` objects are handled by the same controller tagged with `logger=scansettingbindingctrl`. These objects have no status. Any issues are communicated in form of events: 

```shell-session
Events:
  Type     Reason        Age    From                    Message
  ----     ------        ----   ----                    -------
  Normal   SuiteCreated  9m52s  scansettingbindingctrl  ComplianceSuite openshift-compliance/my-companys-compliance-requirements created
```


Now a `ComplianceSuite` object is created. The flow continues to reconcile the newly created `ComplianceSuite`. 

#### 5.6.8.1.3. ComplianceSuite custom resource lifecycle and debugging

The `ComplianceSuite` CR is a wrapper around `ComplianceScan` CRs. The `ComplianceSuite` CR is handled by controller tagged with `logger=suitectrl`. This controller handles creating scans from a suite, reconciling and aggregating individual Scan statuses into a single Suite status. If a suite is set to run periodically, the `suitectrl` also handles creating a `CronJob` CR that re-runs the scans in the suite after the initial run is done: 

```shell-session
$ oc get cronjobs
```


**Example output**

```shell-session
NAME                                           SCHEDULE    SUSPEND   ACTIVE   LAST SCHEDULE   AGE
<cron_name>                                    0 1 * * *   False     0        <none>          151m
```


For the most important issues, events are emitted. View them with `oc describe compliancesuites/<name>`. The `Suite` objects also have a `Status` subresource that is updated when any of `Scan` objects that belong to this suite update their `Status` subresource. After all expected scans are created, control is passed to the scan controller. 

#### 5.6.8.1.4. ComplianceScan custom resource lifecycle and debugging

The `ComplianceScan` CRs are handled by the `scanctrl` controller. This is also where the actual scans happen and the scan results are created. Each scan goes through several phases: 

#### 5.6.8.1.5. Pending phase

The scan is validated for correctness in this phase. If some parameters such as storage size are invalid, the scan transitions to DONE with ERROR result, otherwise proceeds to the Launching phase. 

#### 5.6.8.1.6. Launching phase

In this phase, several config maps that contain either environment for the scanner pods or directly the script that the scanner pods will be evaluating. List the config maps: 

```shell-session
$ oc -n openshift-compliance get cm \
-l compliance.openshift.io/scan-name=rhcos4-e8-worker,complianceoperator.openshift.io/scan-script=
```


These config maps will be used by the scanner pods. If you ever needed to modify the scanner behavior, change the scanner debug level or print the raw results, modifying the config maps is the way to go. Afterwards, a persistent volume claim is created per scan to store the raw ARF results: 

```shell-session
$ oc get pvc -n openshift-compliance -lcompliance.openshift.io/scan-name=rhcos4-e8-worker
```


The PVCs are mounted by a per-scan `ResultServer` deployment. A `ResultServer` is a simple HTTP server where the individual scanner pods upload the full ARF results to. Each server can run on a different node. The full ARF results might be very large and you cannot presume that it would be possible to create a volume that could be mounted from multiple nodes at the same time. After the scan is finished, the `ResultServer` deployment is scaled down. The PVC with the raw results can be mounted from another custom pod and the results can be fetched or inspected. The traffic between the scanner pods and the `ResultServer` is protected by mutual TLS protocols. 

Finally, the scanner pods are launched in this phase; one scanner pod for a `Platform` scan instance and one scanner pod per matching node for a `node` scan instance. The per-node pods are labeled with the node name. Each pod is always labeled with the `ComplianceScan` name: 

```shell-session
$ oc get pods -lcompliance.openshift.io/scan-name=rhcos4-e8-worker,workload=scanner --show-labels
```


**Example output**

```shell-session
NAME                                                              READY   STATUS      RESTARTS   AGE   LABELS
rhcos4-e8-worker-ip-10-0-169-90.eu-north-1.compute.internal-pod   0/2     Completed   0          39m   compliance.openshift.io/scan-name=rhcos4-e8-worker,targetNode=ip-10-0-169-90.eu-north-1.compute.internal,workload=scanner
```


The scan then proceeds to the Running phase. 

#### 5.6.8.1.7. Running phase

The running phase waits until the scanner pods finish. The following terms and processes are in use in the running phase: 

  * **init container** : There is one init container called `content-container`. It runs the **contentImage** container and executes a single command that copies the **contentFile** to the `/content` directory shared with the other containers in this pod. 
  * **scanner** : This container runs the scan. For node scans, the container mounts the node filesystem as `/host` and mounts the content delivered by the init container. The container also mounts the `entrypoint` `ConfigMap` created in the Launching phase and executes it. The default script in the entrypoint `ConfigMap` executes OpenSCAP and stores the result files in the `/results` directory shared between the containers in the pod. Logs from this pod can be viewed to determine what the OpenSCAP scanner checked. More verbose output can be viewed with the `debug` flag. 
  * **logcollector** : The logcollector container waits until the scanner container finishes. Then, it uploads the full ARF results to the `ResultServer` and separately uploads the XCCDF results along with scan result and OpenSCAP result code as a `ConfigMap.` These result config maps are labeled with the scan name (`compliance.openshift.io/scan-name=rhcos4-e8-worker`): 

```shell-session
$ oc describe cm/rhcos4-e8-worker-ip-10-0-169-90.eu-north-1.compute.internal-pod
```


**Example output**

```shell-session
      Name:         rhcos4-e8-worker-ip-10-0-169-90.eu-north-1.compute.internal-pod
      Namespace:    openshift-compliance
      Labels:       compliance.openshift.io/scan-name-scan=rhcos4-e8-worker
                    complianceoperator.openshift.io/scan-result=
      Annotations:  compliance-remediations/processed:
                    compliance.openshift.io/scan-error-msg:
                    compliance.openshift.io/scan-result: NON-COMPLIANT
                    OpenSCAP-scan-result/node: ip-10-0-169-90.eu-north-1.compute.internal

      Data
      ====
      exit-code:
      ----
      2
      results:
      ----
      <?xml version="1.0" encoding="UTF-8"?>
      ...
```


Scanner pods for `Platform` scans are similar, except: 

  * There is one extra init container called `api-resource-collector` that reads the OpenSCAP content provided by the content-container init, container, figures out which API resources the content needs to examine and stores those API resources to a shared directory where the `scanner` container would read them from. 
  * The `scanner` container does not need to mount the host file system. 



When the scanner pods are done, the scans move on to the Aggregating phase. 

#### 5.6.8.1.8. Aggregating phase

In the aggregating phase, the scan controller spawns yet another pod called the aggregator pod. Its purpose is to take the result `ConfigMap` objects, read the results and for each check result create the corresponding Kubernetes object. If the check failure can be automatically remediated, a `ComplianceRemediation` object is created. To provide human-readable metadata for the checks and remediations, the aggregator pod also mounts the OpenSCAP content by using an init container. 

When a config map is processed by an aggregator pod, it is labeled the `compliance-remediations/processed` label. The result of this phase are `ComplianceCheckResult` objects: 

```shell-session
$ oc get compliancecheckresults -lcompliance.openshift.io/scan-name=rhcos4-e8-worker
```


**Example output**

```shell-session
NAME                                                       STATUS   SEVERITY
rhcos4-e8-worker-accounts-no-uid-except-zero               PASS     high
rhcos4-e8-worker-audit-rules-dac-modification-chmod        FAIL     medium
```


and `ComplianceRemediation` objects: 

```shell-session
$ oc get complianceremediations -lcompliance.openshift.io/scan-name=rhcos4-e8-worker
```


**Example output**

```shell-session
NAME                                                       STATE
rhcos4-e8-worker-audit-rules-dac-modification-chmod        NotApplied
rhcos4-e8-worker-audit-rules-dac-modification-chown        NotApplied
rhcos4-e8-worker-audit-rules-execution-chcon               NotApplied
rhcos4-e8-worker-audit-rules-execution-restorecon          NotApplied
rhcos4-e8-worker-audit-rules-execution-semanage            NotApplied
rhcos4-e8-worker-audit-rules-execution-setfiles            NotApplied
```


After these CRs are created, the aggregator pod exits and the scan moves on to the Done phase. 

#### 5.6.8.1.9. Done phase

In the final scan phase, the scan resources are cleaned up if needed and the `ResultServer` deployment is either scaled down (if the scan was one-time) or deleted if the scan is continuous; the next scan instance would then re-create the deployment again. 

It is also possible to trigger a re-run of a scan in the Done phase by annotating it: 

```shell-session
$ oc -n openshift-compliance \
annotate compliancescans/rhcos4-e8-worker compliance.openshift.io/rescan=
```


After the scan reaches the Done phase, nothing else happens on its own unless the remediations are set to be applied automatically with `autoApplyRemediations: true`. The OpenShift Container Platform administrator would now review the remediations and apply them as needed. If the remediations are set to be applied automatically, the `ComplianceSuite` controller takes over in the Done phase, pauses the machine config pool to which the scan maps to and applies all the remediations in one go. If a remediation is applied, the `ComplianceRemediation` controller takes over. 

#### 5.6.8.1.10. ComplianceRemediation controller lifecycle and debugging

The example scan has reported some findings. One of the remediations can be enabled by toggling its `apply` attribute to `true`: 

```shell-session
$ oc patch complianceremediations/rhcos4-e8-worker-audit-rules-dac-modification-chmod --patch '{"spec":{"apply":true}}' --type=merge
```


The `ComplianceRemediation` controller (`logger=remediationctrl`) reconciles the modified object. The result of the reconciliation is change of status of the remediation object that is reconciled, but also a change of the rendered per-suite `MachineConfig` object that contains all the applied remediations. 

The `MachineConfig` object always begins with `75-` and is named after the scan and the suite: 

```shell-session
$ oc get mc | grep 75-
```


**Example output**

```shell-session
75-rhcos4-e8-worker-my-companys-compliance-requirements                                                3.2.0             2m46s
```


The remediations the `mc` currently consists of are listed in the annotations of the machine config: 

```shell-session
$ oc describe mc/75-rhcos4-e8-worker-my-companys-compliance-requirements
```


**Example output**

```shell-session
Name:         75-rhcos4-e8-worker-my-companys-compliance-requirements
Labels:       machineconfiguration.openshift.io/role=worker
Annotations:  remediation/rhcos4-e8-worker-audit-rules-dac-modification-chmod:
```


The `ComplianceRemediation` controller algorithm works like this: 

  * All currently applied remediations are read into an initial remediation set. 
  * If the reconciled remediation is supposed to be applied, it is added to the set. 
  * A `MachineConfig` object is rendered from the set and annotated with names of remediations in the set. If the set is empty (the last remediation was unapplied), the rendered `MachineConfig` object is removed. 
  * If and only if the rendered machine config is different from the one already applied in the cluster, the applied MC is updated (or created, or deleted). 
  * Creating or modifying a `MachineConfig` object triggers a reboot of nodes that match the `machineconfiguration.openshift.io/role` label - see the Machine Config Operator documentation for more details. 



The remediation loop ends once the rendered machine config is updated, if needed, and the reconciled remediation object status is updated. In our case, applying the remediation would trigger a reboot. After the reboot, annotate the scan to re-run it: 

```shell-session
$ oc -n openshift-compliance \
annotate compliancescans/rhcos4-e8-worker compliance.openshift.io/rescan=
```


The scan will run and finish. Check for the remediation to pass: 

```shell-session
$ oc -n openshift-compliance \
get compliancecheckresults/rhcos4-e8-worker-audit-rules-dac-modification-chmod
```


**Example output**

```shell-session
NAME                                                  STATUS   SEVERITY
rhcos4-e8-worker-audit-rules-dac-modification-chmod   PASS     medium
```


#### 5.6.8.1.11. Useful labels

Each pod that is spawned by the Compliance Operator is labeled specifically with the scan it belongs to and the work it does. The scan identifier is labeled with the `compliance.openshift.io/scan-name` label. The workload identifier is labeled with the `workload` label. 

The Compliance Operator schedules the following workloads: 

  * **scanner** : Performs the compliance scan. 
  * **resultserver** : Stores the raw results for the compliance scan. 
  * **aggregator** : Aggregates the results, detects inconsistencies and outputs result objects (checkresults and remediations). 
  * **suitererunner** : Will tag a suite to be re-run (when a schedule is set). 
  * **profileparser** : Parses a datastream and creates the appropriate profiles, rules and variables. 



When debugging and logs are required for a certain workload, run: 

```shell-session
$ oc logs -l workload=<workload_name> -c <container_name>
```


### 5.6.8.2. Increasing Compliance Operator resource limits

In some cases, the Compliance Operator might require more memory than the default limits allow. You can mitigate this issue by setting custom resource limits. 

To increase the default memory and CPU limits of scanner pods, see _`ScanSetting` Custom resource_. 

**Procedure**

  1. To increase the Operator memory limits to 500 Mi, create the following patch file named `co-memlimit-patch.yaml`: 

```yaml
spec:
  config:
    resources:
      limits:
        memory: 500Mi
```


  2. Apply the patch file: 

```shell-session
$ oc patch sub compliance-operator -nopenshift-compliance --patch-file co-memlimit-patch.yaml --type=merge
```


### 5.6.8.3. Configuring Operator resource constraints

You can configure the `resources` field in the `compliance-operator` subscription object to define resource constraints for all the containers in the pod created by the Operator Lifecycle Manager (OLM), so the Operator pods have enough CPU and memory. 

Note

Resource Constraints applied in this process overwrites the existing resource constraints. 

**Procedure**

  * Inject a request of 0.25 cpu and 64 Mi of memory, and a limit of 0.5 cpu and 128 Mi of memory in each container by editing the `Subscription` object: 

```yaml
kind: Subscription
metadata:
  name: compliance-operator
  namespace: openshift-compliance
spec:
  package: package-name
  channel: stable
  config:
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```


### 5.6.8.4. Configuring ScanSetting resources

When using the Compliance Operator in a cluster that contains more than 500 MachineConfigs, the `ocp4-pci-dss-api-checks-pod` pod might pause in the `init` phase when performing a `Platform` scan. 

Note

Resource constraints applied in this process overwrites the existing resource constraints. 

**Procedure**

  1. Confirm the `ocp4-pci-dss-api-checks-pod` pod is stuck in the `Init:OOMKilled` status: 

```shell-session
$ oc get pod ocp4-pci-dss-api-checks-pod -w
```


**Example output**

```shell-session
NAME                          READY   STATUS     RESTARTS        AGE
ocp4-pci-dss-api-checks-pod   0/2     Init:1/2   8 (5m56s ago)   25m
ocp4-pci-dss-api-checks-pod   0/2     Init:OOMKilled   8 (6m19s ago)   26m
```


  2. Edit the `scanLimits` attribute in the `ScanSetting` CR to increase the available memory for the `ocp4-pci-dss-api-checks-pod` pod: 

```yaml
timeout: 30m
strictNodeScan: true
metadata:
  name: default
  namespace: openshift-compliance
kind: ScanSetting
showNotApplicable: false
rawResultStorage:
  nodeSelector:
    node-role.kubernetes.io/master: ''
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
schedule: 0 1 * * *
roles:
  - master
  - worker
apiVersion: compliance.openshift.io/v1alpha1
maxRetryOnTimeout: 3
scanTolerations:
  - operator: Exists
scanLimits:
  memory: 1024Mi
```


where: 

`scanLimits.memory`
     Specifies the default setting is `500Mi`. 

  3. Apply the `ScanSetting` CR to your cluster: 

```shell-session
$ oc apply -f scansetting.yaml
```


### 5.6.8.5. Configuring ScanSetting timeout

The `ScanSetting` object has a timeout option that you can specify in the `ComplianceScanSetting` object as a duration string, such as `1h30m`. If the scan does not finish within the specified timeout, the scan reattempts until the `maxRetryOnTimeout` limit is reached. 

**Procedure**

  * To set a `timeout` and `maxRetryOnTimeout` in ScanSetting, modify an existing `ScanSetting` object: 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ScanSetting
metadata:
  name: default
  namespace: openshift-compliance
rawResultStorage:
  rotation: 3
  size: 1Gi
roles:
- worker
- master
scanTolerations:
- effect: NoSchedule
  key: node-role.kubernetes.io/master
  operator: Exists
schedule: '0 1 * * *'
timeout: '10m0s'
maxRetryOnTimeout: 3
```


where: 

`timeout`
     Specifies a duration string, such as `1h30m`. The default value is `30m`. To disable the timeout, set the value to `0s`. 
`maxRetryOnTimeout`
     Specifies the `maxRetryOnTimeout` variable defines how many times a retry is attempted. The default value is `3`. 




### 5.6.8.6. Get support

Red Hat offers several support channels to help you troubleshoot issues and get the most from OpenShift Container Platform. 

From the Red Hat Customer Portal, you can: 

  * Search or browse through the Red Hat Knowledgebase of articles and solutions about Red Hat products. 
  * Submit a support case to Red Hat Support. 
  * Access other product documentation. 



To identify issues with your cluster, you can use Red Hat Lightspeed in [OpenShift Cluster Manager](https://console.redhat.com/openshift). Red Hat Lightspeed provides details about issues and, if available, information about how to solve a problem. 

To suggest improvements or report errors, give specific details such as the section name and OpenShift Container Platform version. 

## 5.6.9. Using the oc-compliance plugin

Although the Compliance Operator automates many of the checks and remediations for the cluster, an administrator can use the `oc-compliance` plugin to perform the full process of bringing a cluster into compliance by interacting with the Compliance Operator API and other components. 

### 5.6.9.1. Install the oc-compliance plugin

You can install the `oc-compliance` plugin to simplify compliance operations from the command line. 

**Procedure**

  * Extract the `oc-compliance` image to get the `oc-compliance` binary: 

```shell-session
$ podman run --rm -v ~/.local/bin:/mnt/out:Z registry.redhat.io/compliance/oc-compliance-rhel8:stable /bin/cp /usr/bin/oc-compliance /mnt/out/
```


**Example output**

```shell-session
W0611 20:35:46.486903   11354 manifest.go:440] Chose linux/amd64 manifest from the manifest list.
```


You can now run `oc-compliance`. 




### 5.6.9.2. Fetch raw results

An administrator or auditor can review the complete detailed results of a scan as created by the OpenSCAP tool. These results contain more details than what is contained in the `ComplianceCheckResult` custom resource (CR). 

When a compliance scan finishes, the results of the individual checks are listed in the resulting `ComplianceCheckResult` custom resource (CR). However, an administrator or auditor might require the complete details of the scan. The OpenSCAP tool creates an Advanced Recording Format (ARF) formatted file with the detailed results. This ARF file is too large to store in a config map or other standard Kubernetes resource, so a persistent volume (PV) is created to contain it. 

**Procedure**

  1. Fetch the results from the PV by running the following command: 

```shell-session
$ oc compliance fetch-raw <object-type> <object-name> -o <output-path>
```


where: 

     * `<object-type>` can be either `scansettingbinding`, `compliancescan` or `compliancesuite`, depending on which of these objects the scans were launched with. 
     * `<object-name>` is the name of the binding, suite, or scan object to gather the ARF file for, and `<output-path>` is the local directory to place the results. 

For example: 

```shell-session
$ oc compliance fetch-raw scansettingbindings my-binding -o /tmp/
```


**Example output**

```shell-session
Fetching results for my-binding scans: ocp4-cis, ocp4-cis-node-worker, ocp4-cis-node-master
Fetching raw compliance results for scan 'ocp4-cis'.......
The raw compliance results are available in the following directory: /tmp/ocp4-cis
Fetching raw compliance results for scan 'ocp4-cis-node-worker'...........
The raw compliance results are available in the following directory: /tmp/ocp4-cis-node-worker
Fetching raw compliance results for scan 'ocp4-cis-node-master'......
The raw compliance results are available in the following directory: /tmp/ocp4-cis-node-master
```


  2. View the list of files in the directory: 

```shell-session
$ ls /tmp/ocp4-cis-node-master/
```


**Example output**

```shell-session
ocp4-cis-node-master-ip-10-0-128-89.ec2.internal-pod.xml.bzip2  ocp4-cis-node-master-ip-10-0-150-5.ec2.internal-pod.xml.bzip2  ocp4-cis-node-master-ip-10-0-163-32.ec2.internal-pod.xml.bzip2
```


  3. Extract the results: 

```shell-session
$ bunzip2 -c resultsdir/worker-scan/worker-scan-stage-459-tqkg7-compute-0-pod.xml.bzip2 > resultsdir/worker-scan/worker-scan-ip-10-0-170-231.us-east-2.compute.internal-pod.xml
```


  4. View the extracted results: 

```shell-session
$ ls resultsdir/worker-scan/
```


**Example output**

```shell-session
worker-scan-ip-10-0-170-231.us-east-2.compute.internal-pod.xml
worker-scan-stage-459-tqkg7-compute-0-pod.xml.bzip2
worker-scan-stage-459-tqkg7-compute-1-pod.xml.bzip2
```


### 5.6.9.3. Re-running scans

Although it is possible to run scans as scheduled jobs, you must often re-run a scan on demand, particularly after remediations are applied or when other changes to the cluster are made. 

Rerunning a scan with the Compliance Operator requires the use of an annotation on the scan object. However, with the `oc-compliance` plugin you can rerun a scan with a single command. 

**Procedure**

  * Rerun the scans for the `ScanSettingBinding` object named `my-binding` by running the following command: 

```shell-session
$ oc compliance rerun-now scansettingbindings my-binding
```


**Example output**

```shell-session
Rerunning scans from 'my-binding': ocp4-cis
Re-running scan 'openshift-compliance/ocp4-cis'
```


### 5.6.9.4. Use ScanSettingBinding custom resources

When using the `ScanSetting` and `ScanSettingBinding` custom resources (CRs) that the Compliance Operator provides, it is possible to run scans for multiple profiles while using a common set of scan options, such as `schedule`, `machine roles`, `tolerations`, and so on. 

Although that is easier than working with multiple `ComplianceSuite` or `ComplianceScan` objects, it can confuse new users. 

The `oc compliance bind` subcommand helps you create a `ScanSettingBinding` CR. 

**Procedure**

  1. Run: 

```shell-session
$ oc compliance bind [--dry-run] -N <binding name> [-S <scansetting name>] <objtype/objname> [..<objtype/objname>]
```


     * If you omit the `-S` flag, the `default` scan setting provided by the Compliance Operator is used. 
     * The object type is the Kubernetes object type, which can be `profile` or `tailoredprofile`. More than one object can be provided. 
     * The object name is the name of the Kubernetes resource, such as `.metadata.name`. 
     * Add the `--dry-run` option to display the YAML file of the objects that are created. 

For example, given the following profiles and scan settings: 

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


```shell-session
$ oc get scansettings -n openshift-compliance
```


**Example output**

```shell-session
NAME                 AGE
default              10m
default-auto-apply   10m
```


  2. To apply the `default` settings to the `ocp4-cis` and `ocp4-cis-node` profiles, run: 

```shell-session
$ oc compliance bind -N my-binding profile/ocp4-cis profile/ocp4-cis-node
```


**Example output**

```shell-session
Creating ScanSettingBinding my-binding
```


After the `ScanSettingBinding` CR is created, the bound profile begins scanning for both profiles with the related settings. Overall, this is the fastest way to begin scanning with the Compliance Operator. 




### 5.6.9.5. Print controls

You can view a report of the compliance standards and controls that a given profile satisfies. 

Compliance standards are generally organized into a the following hierarchy: 

  * A benchmark is the top-level definition of a set of controls for a particular standard. For example, FedRAMP Moderate or Center for Internet Security (CIS) v.1.6.0. 
  * A control describes a family of requirements that must be met to be in compliance with the benchmark. For example, FedRAMP AC-01 (access control policy and procedures). 
  * A rule is a single check that is specific for the system being brought into compliance, and one or more of these rules map to a control. 
  * The Compliance Operator handles the grouping of rules into a profile for a single benchmark. It can be difficult to determine which controls that the set of rules in a profile satisfy. 



**Procedure**

  * The `oc compliance` `controls` subcommand provides a report of the standards and controls that a given profile satisfies: 

```shell-session
$ oc compliance controls profile ocp4-cis-node
```


**Example output**

```shell-session
+-----------+----------+
| FRAMEWORK | CONTROLS |
+-----------+----------+
| CIS-OCP   | 1.1.1    |
+           +----------+
|           | 1.1.10   |
+           +----------+
|           | 1.1.11   |
+           +----------+
...
```


### 5.6.9.6. Fetch compliance remediation details

The Compliance Operator provides remediation objects that are used to automate the changes required to make the cluster compliant. You can use the `fetch-fixes` subcommand to help you understand exactly which configuration remediations are used. 

The `fetch-fixes` extracts the remediation objects from a profile, rule, or `ComplianceRemediation` object into a directory for you to inspect. 

Warning

Use caution before applying remediations directly. Some remediations might not be applicable in bulk, such as the usbguard rules in the moderate profile. In these cases, allow the Compliance Operator to apply the rules because it addresses the dependencies and ensures that the cluster remains in a good state. 

**Procedure**

  1. View the remediations for a profile: 

```shell-session
$ oc compliance fetch-fixes profile ocp4-cis -o /tmp
```


**Example output**

```shell-session
No fixes to persist for rule 'ocp4-api-server-api-priority-flowschema-catch-all'
No fixes to persist for rule 'ocp4-api-server-api-priority-gate-enabled'
No fixes to persist for rule 'ocp4-api-server-audit-log-maxbackup'
Persisted rule fix to /tmp/ocp4-api-server-audit-log-maxsize.yaml
No fixes to persist for rule 'ocp4-api-server-audit-log-path'
No fixes to persist for rule 'ocp4-api-server-auth-mode-no-aa'
No fixes to persist for rule 'ocp4-api-server-auth-mode-node'
No fixes to persist for rule 'ocp4-api-server-auth-mode-rbac'
No fixes to persist for rule 'ocp4-api-server-basic-auth'
No fixes to persist for rule 'ocp4-api-server-bind-address'
No fixes to persist for rule 'ocp4-api-server-client-ca'
Persisted rule fix to /tmp/ocp4-api-server-encryption-provider-cipher.yaml
Persisted rule fix to /tmp/ocp4-api-server-encryption-provider-config.yaml
```


Note

The `No fixes to persist` warning is expected whenever there are rules in a profile that do not have a corresponding remediation, because either the rule cannot be remediated automatically or a remediation was not provided. 

  2. You can view a sample of the YAML file. The `head` command will show you the first 10 lines: 

```shell-session
$ head /tmp/ocp4-api-server-audit-log-maxsize.yaml
```


**Example output**

```shell-session
apiVersion: config.openshift.io/v1
kind: APIServer
metadata:
  name: cluster
spec:
  maximumFileSizeMegabytes: 100
```


  3. View the remediation from a `ComplianceRemediation` object created after a scan: 

```shell-session
$ oc get complianceremediations -n openshift-compliance
```


**Example output**

```shell-session
NAME                                             STATE
ocp4-cis-api-server-encryption-provider-cipher   NotApplied
ocp4-cis-api-server-encryption-provider-config   NotApplied
```


```shell-session
$ oc compliance fetch-fixes complianceremediations ocp4-cis-api-server-encryption-provider-cipher -o /tmp
```


**Example output**

```shell-session
Persisted compliance remediation fix to /tmp/ocp4-cis-api-server-encryption-provider-cipher.yaml
```


  4. You can view a sample of the YAML file. The `head` command will show you the first 10 lines: 

```shell-session
$ head /tmp/ocp4-cis-api-server-encryption-provider-cipher.yaml
```


**Example output**

```shell-session
apiVersion: config.openshift.io/v1
kind: APIServer
metadata:
  name: cluster
spec:
  encryption:
    type: aescbc
```


### 5.6.9.7. View ComplianceCheckResult object details

When scans are finished running, `ComplianceCheckResult` objects are created for the individual scan rules. You can use the `view-result` subcommand to provide a human-readable output of the `ComplianceCheckResult` object details. 

**Procedure**

  * Run: 

```shell-session
$ oc compliance view-result ocp4-cis-scheduler-no-bind-address
```


### 5.6.9.8. Additional resources

  * [About the Compliance Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/compliance-operator#understanding-compliance-operator "5.4.1. About the Compliance Operator")
