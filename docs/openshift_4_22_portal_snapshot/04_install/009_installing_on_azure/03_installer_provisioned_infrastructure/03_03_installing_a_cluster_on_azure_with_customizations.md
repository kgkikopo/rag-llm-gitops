# 3.3. Installing a cluster on Azure with customizations

In OpenShift Container Platform version 4.22, you can install a cluster with a customized configuration or a customized network configuration on infrastructure that the installation program provisions on Microsoft Azure. To install a cluster with customizations or with network customizations, modify parameters in the `install-config.yaml` file before you install the cluster. By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations. You must set most of the network configuration parameters during installation, and you can modify only the `kubeProxy` configuration parameters in a running cluster. 

## 3.3.1. Using the Azure Marketplace offering

You can use the Azure Marketplace offering to deploy an OpenShift Container Platform cluster, which is billed on pay-per-use basis (hourly, per core) through Azure, while still being supported directly by Red Hat. 

To deploy an OpenShift Container Platform cluster using the Azure Marketplace offering, you must first obtain the Azure Marketplace image. The installation program uses this image to deploy worker or control plane nodes. When obtaining your image, consider the following: 

  * While the images are the same, the Azure Marketplace publisher is different depending on your region. If you are located in North America, specify `redhat` as the publisher. If you are located in EMEA, specify `redhat-limited` as the publisher. 
  * The offer includes a `rh-ocp-worker` SKU and a `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker` SKU represents a Hyper-V generation version 2 VM image. The default instance types used in OpenShift Container Platform are version 2 compatible. If you plan to use an instance type that is only version 1 compatible, use the image associated with the `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker-gen1` SKU represents a Hyper-V version 1 VM image. 



Important

Installing images with the Azure marketplace is not supported on clusters with 64-bit ARM instances. 

You should only modify the RHCOS image for compute machines to use an Azure Marketplace image. Control plane machines and infrastructure nodes do not require an OpenShift Container Platform subscription and use the public RHCOS default image by default, which does not incur subscription costs on your Azure bill. Therefore, you should not modify the cluster default boot image or the control plane boot images. Applying the Azure Marketplace image to them will incur additional licensing costs that cannot be recovered. 

**Prerequisites**

  * You have installed the Azure CLI client `(az)`. 
  * Your Azure account is entitled for the offer and you have logged into this account with the Azure CLI client. 



**Procedure**

  1. Display all of the available OpenShift Container Platform images by running one of the following commands: 

     * North America: 

```shell-session
$  az vm image list --all --offer rh-ocp-worker --publisher redhat -o table
```


**Example output**

```shell-session
Offer          Publisher       Sku                 Urn                                                             Version
-------------  --------------  ------------------  --------------------------------------------------------------  -----------------
rh-ocp-worker  RedHat          rh-ocp-worker       RedHat:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
rh-ocp-worker  RedHat          rh-ocp-worker-gen1  RedHat:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
```


     * EMEA: 

```shell-session
$  az vm image list --all --offer rh-ocp-worker --publisher redhat-limited -o table
```


**Example output**

```shell-session
Offer          Publisher       Sku                 Urn                                                                     Version
-------------  --------------  ------------------  --------------------------------------------------------------          -----------------
rh-ocp-worker  redhat-limited  rh-ocp-worker       redhat-limited:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
rh-ocp-worker  redhat-limited  rh-ocp-worker-gen1  redhat-limited:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
```


Note

Use the latest image that is available for compute and control plane nodes. If required, your VMs are automatically upgraded as part of the installation process. 

  2. Inspect the image for your offer by running one of the following commands: 

     * North America: 

```shell-session
$ az vm image show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
```


     * EMEA: 

```shell-session
$ az vm image show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
```


  3. Review the terms of the offer by running one of the following commands: 

     * North America: 

```shell-session
$ az vm image terms show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
```


     * EMEA: 

```shell-session
$ az vm image terms show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
```


  4. Accept the terms of the offering by running one of the following commands: 

     * North America: 

```shell-session
$ az vm image terms accept --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
```


     * EMEA: 

```shell-session
$ az vm image terms accept --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
```


  5. Record the image details of your offer. You must update the `compute` section in the `install-config.yaml` file with values for `publisher`, `offer`, `sku`, and `version` before deploying the cluster. You may also update the `controlPlane` section to deploy control plane machines with the specified image details, or the `defaultMachinePlatform` section to deploy both control plane and compute machines with the specified image details. Use the latest available image for control plane and compute nodes. 

**Sample`install-config.yaml` file with the Azure Marketplace compute nodes**

```yaml
apiVersion: v1
baseDomain: example.com
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    azure:
      type: Standard_D4s_v5
      osImage:
        publisher: redhat
        offer: rh-ocp-worker
        sku: rh-ocp-worker
        version: 413.92.2023101700
  replicas: 3
```


## 3.3.2. Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on Microsoft Azure. 

Important

Do not specify `windows`, `microsoft`, or other variants of these words in the `metadata.name` parameter of the `install-config.yaml` file. Specifying one of these words for the cluster name causes the installation program to generate an error message like the following example message: 

```shell-session
The resource name 'windows-xxxx-identity' or a part of the name is a trademarked or reserved word.
```


Additionally, specifying `login` at the beginning of the name in the `metadata.name` parameter of the `install-config.yaml` file results in the generation of an error message. You can specify `login` in the middle or end of the name. 

**Prerequisites**

  * You have the OpenShift Container Platform installation program and the pull secret for your cluster. 
  * You have an Azure subscription ID and tenant ID. 
  * If you are installing the cluster using a service principal, you have its application ID and password. 
  * If you are installing the cluster using a system-assigned managed identity, you have enabled it on the virtual machine that you will run the installation program from. 
  * If you are installing the cluster using a user-assigned managed identity, you have met these prerequisites: 

    * You have its client ID. 
    * You have assigned it to the virtual machine that you will run the installation program from. 




**Procedure**

  1. Optional: If you have run the installation program on this computer before, and want to use an alternative service principal or managed identity, go to the `~/.azure/` directory and delete the `osServicePrincipal.json` configuration file. 

Deleting this file prevents the installation program from automatically reusing subscription and authentication values from a previous installation. 

  2. Create the `install-config.yaml` file. 

     1. Change to the directory that contains the installation program and run the following command: 

```shell-session
$ ./openshift-install create install-config --dir <installation_directory>
```


        * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates. 

When specifying the directory: 

        * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory. 
        * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version. 

     2. At the prompts, provide the configuration details for your cloud: 

        1. Optional: Select an SSH key to use to access your cluster machines. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses. 

        2. Select **azure** as the platform to target. 

If the installation program cannot locate the `osServicePrincipal.json` configuration file from a previous installation, you are prompted for Azure subscription and authentication values. 

        3. Enter the following Azure parameter values for your subscription: 

           * **azure subscription id** : Enter the subscription ID to use for the cluster. 
           * **azure tenant id** : Enter the tenant ID. 

        4. Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the **azure service principal client id** : 

           * If you are using a service principal, enter its application ID. 
           * If you are using a system-assigned managed identity, leave this value blank. 
           * If you are using a user-assigned managed identity, specify its client ID. 

        5. Depending on the Azure identity you are using to deploy the cluster, do one of the following when prompted for the **azure service principal client secret** : 

           * If you are using a service principal, enter its password. 
           * If you are using a system-assigned managed identity, leave this value blank. 
           * If you are using a user-assigned managed identity, leave this value blank. 

        6. Select the region to deploy the cluster to. 
        7. Select the base domain to deploy the cluster to. The base domain corresponds to the Azure DNS Zone that you created for your cluster. 
        8. Enter a descriptive name for your cluster. 

Important

All Azure resources that are available through public endpoints are subject to resource name restrictions, and you cannot create resources that use certain terms. For a list of terms that Azure restricts, see [Resolve reserved resource name errors](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-reserved-resource-name) in the Azure documentation. 

  3. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section. 

Note

If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that the cluster’s control planes are schedulable. For more information, see "Installing a three-node cluster on Azure". 

  4. Back up the `install-config.yaml` file so that you can use it to install multiple clusters. 

Important

The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now. 

If previously not detected, the installation program creates an `osServicePrincipal.json` configuration file and stores this file in the `~/.azure/` directory on your computer. This ensures that the installation program can load the profile when it is creating an OpenShift Container Platform cluster on the target platform. 




**Additional resources**

  * [Installation configuration parameters for Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_azure/installation-config-parameters-azure "Chapter 7. Installation configuration parameters for Azure")



### 3.3.2.1. Minimum resource requirements for cluster installation

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements. 

Table 3.1. Minimum resource requirementsMachine| Operating system| vCPU| Virtual RAM| Storage| Input/Output Per Second (IOPS)  
---|---|---|---|---|---  
Bootstrap  |  RHCOS  |  4  |  16 GB  |  100 GB  |  300   
Control plane  |  RHCOS  |  4  |  16 GB  |  100 GB  |  300   
Compute  |  RHCOS  |  2  |  8 GB  |  100 GB  |  300   
Show more

  * One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs. 
  * OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance. 
  * As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines. 



Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA): 

  * x86-64 architecture requires x86-64-v2 ISA 
  * ARM64 architecture requires ARMv8.0-A ISA 
  * ppc64le architecture requires IBM® Power9 ISA 
  * s390x architecture requires IBM® z14 ISA 



For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation. 

Important

You must use Azure virtual machines that have the `premiumIO` parameter set to `true`. 

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform. 

**Additional resources**

  * [Optimizing storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#optimizing-storage)



### 3.3.2.2. Tested instance types for Azure

There are several Microsoft Azure instance types tested with OpenShift Container Platform. Choose a listed instance type when you install a cluster on 64-bit x86 infrastructure. 

See the following machine types based on 64-bit x86 architecture: 

#### 3.3.2.2.1. General Purpose

| Azure VM Series | Family Name | |-----------------|-------------| | Basv2-series | `standardBasv2Family` | | BS-series | `standardBSFamily` | | Bsv2-series | `standardBsv2Family` | | Dadsv5-series | `standardDADSv5Family` | | Dadsv6-series | `standardDadv6Family` | | Daldsv6-series | `standardDaldv6Family` | | Dalsv6-series | `standardDalv6Family` | | Dasv4-series | `standardDASv4Family` | | Dasv5-series | `standardDASv5Family` | | Dasv6-series | `standardDav6Family` | | DCas_cc_v5-series | `standardDCACCV5Family` | | DCads_cc_v5-series | `standardDCADCCV5Family` | | DCadsv5-series | `standardDCADSv5Family` | | DCasv5-series | `standardDCASv5Family` | | DCsv2-series | `standardDCSv2Family` | | DCsv3-series | `standardDCSv3Family` | | DCdsv3-series | `standardDDCSv3Family` | | DCedsv5-series | `standardDCEDV5Family` | | DCesv5-series | `standardDCEV5Family` | | Ddsv4-series | `standardDDSv4Family` | | Ddsv5-series | `standardDDSv5Family` | | Ddsv6-series | `StandardDdsv6Family` | | Dldsv5-series | `standardDLDSv5Family` | | Dldsv6-series | `StandardDldsv6Family` | | Dlsv5-series | `standardDLSv5Family` | | Dlsv6-series | `StandardDlsv6Family` | | DS-series | `standardDSFamily` | | Dsv2-series | `standardDSv2Family` | | Dsv3-series | `standardDSv3Family` | | Dsv4-series | `standardDSv4Family` | | Dsv5-series | `standardDSv5Family` | | Dsv6-series | `StandardDsv6Family` | 

#### 3.3.2.2.2. Memory Optimized

| Azure VM Series | Family Name | |-----------------|-------------| | Eadsv5-series | `standardEADSv5Family`, `standardEIADSv5Family` | | Eadsv6-series | `standardEadv6Family` | | Easv4-series | `standardEASv4Family`, `standardEIASv4Family` | | Easv5-series | `standardEASv5Family`, `standardEIASv5Family` | | Easv6-series | `standardEav6Family` | | Ebdsv5-series | `standardEBDSv5Family`, `standardEIBDSv5Family` | | Ebsv5-series | `standardEBSv5Family`, `standardEIBSv5Family` | | ECas_cc_v5-series | `standardECACCV5Family` | | ECads_cc_v5-series | `standardECADCCV5Family` | | ECadsv5-series | `standardECADSv5Family` | | ECasv5-series | `standardECASv5Family` | | ECedsv5-series | `standardECEDV5Family` | | ECesv5-series | `standardECEV5Family` | | Edsv4-series | `standardEDSv4Family` | | Edsv5-series | `standardEDSv5Family`, `standardEIDSv5Family` | | Edsv6-series | `StandardEdsv6Family` | | Esv3-series | `standardESv3Family`, `standardEISv3Family` | | Esv4-series | `standardESv4Family`, `standardXEISv4Family` | | Esv5-series | `standardESv5Family`, `standardEISv5Family` | | Esv6-series | `StandardEsv6Family` | | M-series | `standardMSFamily` | | Mbdsv3-series | `StandardMBDSMediumMemoryv3Family` | | Mbsv3-series | `StandardMBSMediumMemoryv3Family` | | Mdsv3 High Memory-series | `standardMDSHighMemoryv3Family`, `standardMIDSHighMemoryv3Family` | | Mdsv2 Medium Memory-series | `standardMDSMediumMemoryv2Family`, `standardMIDSMediumMemoryv2Family` | | Mdsv3 Medium Memory-series | `standardMDSMediumMemoryv3Family` | | Msv3 High Memory-series | `standardMISHighMemoryv3Family`, `standardMSHighMemoryv3Family` | | Msv2 Medium Memory-series | `standardMISMediumMemoryv2Family`, `standardMSMediumMemoryv2Family` | | Msv3 Medium Memory-series | `standardMSMediumMemoryv3Family` | 

#### 3.3.2.2.3. Compute Optimized

| Azure VM Series | Family Name | |-----------------|-------------| | Falsv6-series | `StandardFalsv6Family` | | Famsv6-series | `StandardFamsv6Family` | | Fasv6-series | `StandardFasv6Family` | | FS-series | `standardFSFamily` | | Fsv2-series | `standardFSv2Family` | | FXmdsv2-series | `StandardFXmdsv2Family` | | FX-series | `standardFXMDVSFamily` | | FXmsv2-series | `StandardFXmsv2Family` | 

#### 3.3.2.2.4. Storage Optimized

| Azure VM Series | Family Name | |-----------------|-------------| | GS-series | `standardGSFamily` | | Laosv4-series | `standardLaosv4Family` | | Lasv3-series | `standardLASv3Family` | | Lasv4-series | `standardLasv4Family` | | Ls-series | `standardLSFamily` | | Lsv2-series | `standardLSv2Family` | | Lsv3-series | `standardLSv3Family` | | Lsv4-series | `standardLsv4Family` | 

#### 3.3.2.2.5. GPU Accelerated

| Azure VM Series | Family Name | |-----------------|-------------| | NC_A100_v4-series | `StandardNCADSA100v4Family` | | NCads_H100_v5-series | `StandardNCadsH100v5Family` | | NCCads_H100_v5-series | `StandardNCCads2023Family` | | NCasT4_v3-series | `Standard NCASv3_T4 Family` | | NCv3-series | `standardNCSv3Family` | | NDasrA100_v4-series | `Standard NDASv4_A100 Family` | | ND-H200-v5-series | `standardNDISRH200V5Family` | | ND-H100-v5-series | `standardNDSH100v5Family` | | NDv2-series | `standardNDSv2Family` | | NGads_V620-series | `StandardNGADSV620v1Family` | | NVadsA10_v5-series | `StandardNVADSA10v5Family` | | NVads V710 v5-series | `StandardNVadsV710v5Family` | | NVv3-series | `standardNVSv3Family` | 

#### 3.3.2.2.6. FPGA Accelerated

| Azure VM Series | Family Name | |-----------------|-------------| | NPS-series | `standardNPSFamily` | 

#### 3.3.2.2.7. High Performance Compute

| Azure VM Series | Family Name | |-----------------|-------------| | HBv2-series | `standardHBrsv2Family` | | HBv4-series | `standardHBv4Family` | | HBv5-series | `standardHBv5Family` | | HC-series | `standardHCSFamily` | | HX-series | `standardHXFamily` | 

### 3.3.2.3. Tested instance types for Azure on 64-bit ARM infrastructures

There are several Microsoft Azure ARM64 instance types tested with OpenShift Container Platform. Choose a listed instance type when you install a cluster on 64-bit ARM infrastructure. 

See the following machine types based on 64-bit ARM architecture: 

#### 3.3.2.3.1. General Purpose (ARM64)

| Azure VM Series | Family Name | |-----------------|-------------| | Bpsv2-series | `standardBpsv2Family` | | Dpdsv5-series | `standardDPDSv5Family` | | Dpldsv5-series | `standardDPLDSv5Family` | | Dplsv5-series | `standardDPLSv5Family` | | Dpsv5-series | `standardDPSv5Family` | | Dpdsv6-series | `StandardDpdsv6Family` | | Dpldsv6-series | `StandardDpldsv6Family` | | Dplsv6-series | `StandardDplsv6Family` | | Dpsv6-series | `StandardDpsv6Family` | 

#### 3.3.2.3.2. Memory Optimized (ARM64)

| Azure VM Series | Family Name | |-----------------|-------------| | Epdsv5-series | `standardEPDSv5Family` | | Epsv5-series | `standardEPSv5Family` | | Epdsv6-series | `StandardEpdsv6Family` | | Epsv6-series | `StandardEpsv6Family` | 

### 3.3.2.4. Enabling trusted launch for Azure VMs

To enable trusted launch on Azure virtual machines for your OpenShift Container Platform cluster, you can configure secure boot and virtualized Trusted Platform Modules in the `install-config.yaml` file. Apply the settings to control plane nodes, compute nodes, or all nodes as needed. 

For more information about the sizes of virtual machines that support the trusted launch features, secure boot, and virtualized Trusted Platform Modules, see the Additional resources section. 

Important

Trusted launch is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Prerequisites**

  * You have created an `install-config.yaml` file. 



**Procedure**

  * Edit the `install-config.yaml` file before deploying your cluster: 

    * Enable trusted launch only on control plane by adding the following stanza: 

```yaml
controlPlane:
  platform:
    azure:
      settings:
        securityType: TrustedLaunch
        trustedLaunch:
          uefiSettings:
            secureBoot: Enabled
            virtualizedTrustedPlatformModule: Enabled
```


    * Enable trusted launch only on compute node by adding the following stanza: 

```yaml
compute:
  platform:
    azure:
      settings:
        securityType: TrustedLaunch
        trustedLaunch:
          uefiSettings:
            secureBoot: Enabled
            virtualizedTrustedPlatformModule: Enabled
```


    * Enable trusted launch on all nodes by adding the following stanza: 

```yaml
platform:
  azure:
    settings:
      securityType: TrustedLaunch
      trustedLaunch:
        uefiSettings:
          secureBoot: Enabled
          virtualizedTrustedPlatformModule: Enabled
```


**Additional resources**

  * [Secure Boot (Microsoft Azure documentation)](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch#secure-boot)
  * [virtualized Trusted Platform Modules (Microsoft Azure documentation)](https://learn.microsoft.com/en-us/windows/security/hardware-security/tpm/trusted-platform-module-overview)
  * [Virtual machine sizes (Microsoft Azure documentation)](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch#virtual-machines-sizes)



### 3.3.2.5. Enable confidential VMs

To enable confidential VMs on Azure for your OpenShift Container Platform cluster, you can configure the `install-config.yaml` file before deployment. Apply the settings to control plane nodes, compute nodes, or all nodes as needed. 

You can use confidential VMs with the following VM sizes: 

  * DCasv5-series 
  * DCadsv5-series 
  * ECasv5-series 
  * ECadsv5-series 
  * DCesv5-series 
  * DCedsv5-series 
  * ECesv5-series 
  * ECedsv5-series 
  * NCCads_H100_v5 



Important

Confidential VMs are currently not supported on 64-bit ARM architectures. 

**Prerequisites**

  * You have created an `install-config.yaml` file. 



**Procedure**

  * Edit the `install-config.yaml` file before deploying your cluster: 

    * Enable confidential VMs only on control plane by adding the following stanza: 

```yaml
controlPlane:
  platform:
    azure:
      settings:
        securityType: ConfidentialVM
        confidentialVM:
          uefiSettings:
            secureBoot: Enabled
            virtualizedTrustedPlatformModule: Enabled
      osDisk:
        securityProfile:
          securityEncryptionType: VMGuestStateOnly
```


    * Enable confidential VMs only on compute nodes by adding the following stanza: 

```yaml
compute:
  platform:
    azure:
      settings:
        securityType: ConfidentialVM
        confidentialVM:
          uefiSettings:
            secureBoot: Enabled
            virtualizedTrustedPlatformModule: Enabled
      osDisk:
        securityProfile:
          securityEncryptionType: VMGuestStateOnly
```


    * Enable confidential VMs on all nodes by adding the following stanza: 

```yaml
platform:
  azure:
    defaultMachinePlatform:
      settings:
        securityType: ConfidentialVM
        confidentialVM:
          uefiSettings:
            secureBoot: Enabled
            virtualizedTrustedPlatformModule: Enabled
      osDisk:
        securityProfile:
          securityEncryptionType: VMGuestStateOnly
```


### 3.3.2.6. Configuring a dedicated disk for etcd

You can install your OpenShift Container Platform cluster on Microsoft Azure with a dedicated data disk for `etcd`. This configuration attaches a separate managed disk to each control plane node and uses it only for `etcd` data, which can improve cluster performance and stability. 

Important

Dedicated disk for etcd is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Prerequisites**

  * You have created an `install-config.yaml` file. 



**Procedure**

  * To configure a dedicated `etcd` disk, edit the `install-config.yaml` file and add the `diskSetup` and `dataDisks` parameters to the `controlPlane` stanza: 

```yaml
# ...
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform:
    azure:
      type: Standard_D4s_v5
      dataDisks:
      - nameSuffix: etcddisk
        cachingType: None
        diskSizeGB: 20
        lun: 0
  diskSetup:
  - type: etcd
    etcd:
      platformDiskID: etcddisk
  replicas: 3
# ...
```


where: 

`controlPlane.platform.azure.dataDisks.nameSuffix`
     Specifies the same value you defined for `platformDiskID`. 
`controlPlane.platform.azure.dataDisks.cachingType`
     Specifies `None`. Other caching requirements are not currently supported. 
`controlPlane.platform.azure.dataDisks.diskSizeGB`
    

Specifies a disk size in GB. This value can be any integer greater than `0`. 

Note

A minimum of 20 GB ensures enough space is available for defragmentation operations. 

`controlPlane.platform.azure.dataDisks.lun`
     Specifies a logical unit number (LUN). This can be any integer from `0` through `63` that is not used by another disk. 
`controlPlane.diskSetup.type`
     Specifies `etcd`. This identifies `etcd` as the node component type to receive a dedicated disk. 
`controlPlane.diskSetup.etcd.platformDiskID`
     Specifies a name to identify the disk. This value must not exceed 12 characters. 




### 3.3.2.7. Enabling a user-managed DNS

To manage API and Ingress DNS records in your own system, install your cluster with a DNS solution that you manage. 

This solution replaces the default cluster-provisioned DNS solution. For example, your organization’s security policies might not allow the use of public DNS services such as Microsoft Azure. In such scenarios, you can use your own DNS service to bypass the public DNS service and manage your own DNS for the IP addresses of the API and Ingress services. 

If you enable user-managed DNS during installation, the installation program provisions DNS records for the API and Ingress services only within the cluster. To ensure access from outside the cluster, you must provision the DNS records in an external DNS service of your choice for the API and Ingress services after installation. 

**Prerequisites**

  * You installed the `jq` package. 



**Procedure**

  * Before you deploy your cluster, use a text editor to open the `install-config.yaml` file and add the following stanza: 

    * To enable user-managed DNS: 

```yaml
# ...

platform:
  azure:
    userProvisionedDNS: Enabled
```


where: 

`userProvisionedDNS`
     Enables user-provisioned DNS management. 




**Next steps**

For information about provisioning your DNS records for the API server and the Ingress services, see "Provisioning your own DNS records". 

### 3.3.2.8. Sample customized install-config.yaml file for Azure

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters. 

Important

This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it. For a full list and description of all installation configuration parameters, see _Installation configuration parameters for Azure_. 

**Sample`install-config.yaml` file for Azure**

```yaml
apiVersion: v1
baseDomain: example.com
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
metadata:
  name: example-cluster
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    azure:
      type: Standard_D8s_v3
  replicas: 3
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    azure:
      type: Standard_D2s_v3
  replicas: 3
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  azure:
    baseDomainResourceGroupName: example-basedomain-resourcegroup-name
    region: centralus
```


where: 

`controlPlane`
     Specifies parameters that apply to control plane machines. 
`compute`
     Specifies parameters that apply to compute machines. 
`networking`
     Specifies parameters that apply to the cluster networking configuration. If you do not provide networking values, the installation program provides default values. 
`platform`
     Specifies parameters that apply to the infrastructure platform that hosts the cluster. 

**Additional resources**

  * [Installation configuration parameters for Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_azure/installation-config-parameters-azure "Chapter 7. Installation configuration parameters for Azure")



### 3.3.2.9. Configuring the cluster-wide proxy during installation

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file. 

**Prerequisites**

  * You have an existing `install-config.yaml` file. 
  * You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, the proxy handles all cluster egress traffic, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object’s `spec.noProxy` field to bypass the proxy if necessary. 

Note

The `Proxy` object `status.noProxy` field includes the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration. 

For installations on Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Red Hat OpenStack Platform (RHOSP), the `Proxy` object `status.noProxy` field also includes the instance metadata endpoint (`169.254.169.254`). 




**Procedure**

  1. Edit your `install-config.yaml` file and add the proxy settings. For example: 

```yaml
apiVersion: v1
baseDomain: my.domain.com
proxy:
  httpProxy: http://<username>:<pswd>@<ip>:<port>
  httpsProxy: https://<username>:<pswd>@<ip>:<port>
  noProxy: example.com
additionalTrustBundle: |
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
additionalTrustBundlePolicy: <policy_to_add_additionalTrustBundle>
# ...
```


where: 

`proxy.httpProxy`
     Specifies a proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`. 
`proxy.httpsProxy`
     Specifies a proxy URL to use for creating HTTPS connections outside the cluster. 
`proxy.noProxy`
     Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations. 
`additionalTrustBundle`
     If you specify this value, the installation program generates a config map named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you specify `additionalTrustBundle` and at least one proxy setting, the `Proxy` object references the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the RHCOS trust bundle. You must set the `additionalTrustBundle` field unless an authority from the RHCOS trust bundle signs the proxy’s identity certificate. 
`additionalTrustBundlePolicy`
    

Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when you configure an `http/https` proxy. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter. 

Note

The installation program does not support the proxy `readinessEndpoints` field. 

Note

If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example: 

```shell-session
$ ./openshift-install wait-for install-complete --log-level debug
```


  2. Save the file and reference it when installing OpenShift Container Platform. 

The installation program creates a cluster-wide proxy named `cluster` that uses the proxy settings in the `install-config.yaml` file. If you do not give proxy settings, the installation program still creates a `cluster` `Proxy` object, but it has a nil `spec`. 

Note

Only the `Proxy` object named `cluster` is supported, and you cannot create additional proxies. 




**Additional resources**

  * For more details about Accelerated Networking, see [Accelerated Networking for Microsoft Azure VMs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#machineset-azure-accelerated-networking_creating-machineset-azure). 



## 3.3.3. Network configuration phases

You can customize your OpenShift Container Platform network plugin configuration, such as cluster network CIDR and service network ranges, during two phases before installation to integrate with your existing network environment. 

Phase 1
    

You can customize the following network-related fields in the `install-config.yaml` file before you create the manifest files: 

  * `networking.networkType`
  * `networking.clusterNetwork`
  * `networking.serviceNetwork`
  * `networking.machineNetwork`
  * `nodeNetworking`

For more information, see "Installation configuration parameters". 

Note

Set the `networking.machineNetwork` to match the Classless Inter-Domain Routing (CIDR) where the preferred subnet is located. 

Important

The CIDR range `172.17.0.0/16` is reserved by `libVirt`. You cannot use any other CIDR range that overlaps with the `172.17.0.0/16` CIDR range for networks in your cluster. 




Phase 2
     After creating the manifest files by running `openshift-install create manifests`, you can define a customized Cluster Network Operator manifest with only the fields you want to modify. You can use the manifest to specify an advanced network configuration. 

During phase 2, you cannot override the values that you specified in phase 1 in the `install-config.yaml` file. However, you can customize the network plugin during phase 2. 

## 3.3.4. Specifying advanced network configuration

You can use advanced network configuration for your OpenShift Container Platform network plugin to integrate your cluster into your existing network environment. 

You can specify advanced network configuration only before you install the cluster. 

Important

Customizing your network configuration by modifying the OpenShift Container Platform manifest files created by the installation program is not supported. Applying a manifest file that you create, as in the following procedure, is supported. 

**Prerequisites**

  * You have created the `install-config.yaml` file and completed any modifications to it. 



**Procedure**

  1. Change to the directory that contains the installation program and create the manifests: 

```shell-session
$ ./openshift-install create manifests --dir <installation_directory>
```


where `<installation_directory>` specifies the name of the directory that contains the `install-config.yaml` file for your cluster. 

  2. Create a stub manifest file for the advanced network configuration that is named `cluster-network-03-config.yml` in the `<installation_directory>/manifests/` directory: 

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
```


  3. Specify the advanced network configuration for your cluster in the `cluster-network-03-config.yml` file, such as in the following example: 

The following example enables IPsec for the OVN-Kubernetes network provider: 

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      ipsecConfig:
        mode: Full
```


  4. Optional: Back up the `manifests/cluster-network-03-config.yml` file. The installation program consumes the `manifests/` directory when you create the Ignition config files. 
  5. Remove the Kubernetes manifest files that define the control plane machines and compute `MachineSets`: 

```shell-session
$ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml
```


Because you create and manage these resources yourself, you do not have to initialize them. 

     * You can preserve the `MachineSet` files to create compute machines by using the machine API, but you must update references to them to match your environment. 




## 3.3.5. Cluster Network Operator configuration

To manage cluster networking, configure the Cluster Network Operator (CNO) `Network` custom resource (CR) named `cluster` so the cluster uses the correct IP ranges and network plugin settings for reliable pod and service connectivity. 

Some settings and fields are inherited at the time of install or by the `default.Network.type` plugin, OVN-Kubernetes. 

The CNO configuration inherits the following fields during cluster installation from the `Network` API in the `Network.config.openshift.io` API group: 

`clusterNetwork`
     IP address pools from which pod IP addresses are allocated. 
`serviceNetwork`
     IP address pool for services. 
`defaultNetwork.type`
     Cluster network plugin. `OVNKubernetes` is the only supported plugin during installation. 

You can specify the cluster network plugin configuration for your cluster by setting the fields for the `defaultNetwork` object in the CNO object named `cluster`. 

### 3.3.5.1. Cluster Network Operator configuration object

The fields for the Cluster Network Operator (CNO) are described in the following table: 

Table 3.2. Cluster Network Operator configuration objectField| Type| Description  
---|---|---  
`metadata.name` |  `string` |  The name of the CNO object. This name is always `cluster`.   
`spec.clusterNetwork` |  `array` |  A list specifying the blocks of IP addresses from which pod IP addresses are allocated and the subnet prefix length assigned to each individual node in the cluster. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:  `spec: clusterNetwork: - cidr: 10.128.0.0/19 hostPrefix: 23 - cidr: fd01::/48 hostPrefix: 64` If you install a cluster on AWS with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first.   
`spec.serviceNetwork` |  `array` |  A block of IP addresses for services. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:  `spec: serviceNetwork: - 172.30.0.0/14 - fd02::/112` If you install a cluster on AWS with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first.  You can customize this field only in the `install-config.yaml` file before you create the manifests. The value is read-only in the manifest file.   
`spec.defaultNetwork` |  `object` |  Configures the network plugin for the cluster network.   
`spec.additionalRoutingCapabilities.providers` |  `array` |  This setting enables a dynamic routing provider. The FRR routing capability provider is required for the route advertisement feature. The only supported value is `FRR`. 

  * `FRR`: The FRR routing provider 

`spec: additionalRoutingCapabilities: providers: - FRR`  
Show more

Important

For a cluster that needs to deploy objects across multiple networks, ensure that you specify the same value for the `clusterNetwork.hostPrefix` parameter for each network type that is defined in the `install-config.yaml` file. Setting a different value for each `clusterNetwork.hostPrefix` parameter can impact the OVN-Kubernetes network plugin, where the plugin cannot effectively route object traffic among different nodes. 

### 3.3.5.2. defaultNetwork object configuration

The values for the `defaultNetwork` object are defined in the following table: 

Table 3.3. defaultNetwork objectField| Type| Description  
---|---|---  
`type` |  `string` |  `OVNKubernetes`. The Red Hat OpenShift Networking network plugin is selected during installation. This value cannot be changed after cluster installation.  Note OpenShift Container Platform uses the OVN-Kubernetes network plugin by default.   
`ovnKubernetesConfig` |  `object` |  This object is only valid for the OVN-Kubernetes network plugin.   
Show more

### 3.3.5.3. Configuration for the OVN-Kubernetes network plugin

The following table describes the configuration fields for the OVN-Kubernetes network plugin: 

Table 3.4. ovnKubernetesConfig objectField| Type| Description  
---|---|---  
`mtu` |  `integer` |  The maximum transmission unit (MTU) for the Geneve (Generic Network Virtualization Encapsulation) overlay network. This is detected automatically based on the MTU of the primary network interface. You do not normally need to override the detected MTU.  If the auto-detected value is not what you expect it to be, confirm that the MTU on the primary network interface on your nodes is correct. You cannot use this option to change the MTU value of the primary network interface on the nodes.  If your cluster requires different MTU values for different nodes, you must set this value to `100` less than the lowest MTU value in your cluster. For example, if some nodes in your cluster have an MTU of `9001`, and some have an MTU of `1500`, you must set this value to `1400`.   
`genevePort` |  `integer` |  The port to use for all Geneve packets. The default value is `6081`. This value cannot be changed after cluster installation.   
`ipsecConfig` |  `object` |  Specify a configuration object for customizing the IPsec configuration.   
`ipv4` |  `object` |  Specifies a configuration object for IPv4 settings.   
`ipv6` |  `object` |  Specifies a configuration object for IPv6 settings.   
`policyAuditConfig` |  `object` |  Specify a configuration object for customizing network policy audit logging. If unset, the defaults audit log settings are used.   
`routeAdvertisements` |  `string` |  Specifies whether to advertise cluster network routes. The default value is `Disabled`. 

  * `Enabled`: Import routes to the cluster network and advertise cluster network routes as configured in `RouteAdvertisements` objects. 
  * `Disabled`: Do not import routes to the cluster network or advertise cluster network routes. 

  
`gatewayConfig` |  `object` |  Optional: Specify a configuration object for customizing how egress traffic is sent to the node gateway. Valid values are `Shared` and `Local`. The default value is `Shared`. In the default setting, the Open vSwitch (OVS) outputs traffic directly to the node IP interface. If you are using hardware offloading, Red Hat recommends to use the default `Shared` gateway mode to bypass the host routing plane. In the `Local` setting, it traverses the host network; consequently, it gets applied to the routing table of the host.  Note While migrating egress traffic, you can expect some disruption to workloads and service traffic until the Cluster Network Operator (CNO) successfully rolls out the changes.   
Show more

Table 3.5. ovnKubernetesConfig.ipv4 objectField| Type| Description  
---|---|---  
`internalTransitSwitchSubnet` |  string  |  If your existing network infrastructure overlaps with the `100.88.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.  The default value is `100.88.0.0/16`.   
`internalJoinSubnet` |  string  |  If your existing network infrastructure overlaps with the `100.64.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster. For example, if the `clusterNetwork.cidr` value is `10.128.0.0/14` and the `clusterNetwork.hostPrefix` value is `/23`, then the maximum number of nodes is `2^(23-14)=512`.  The default value is `100.64.0.0/16`.   
Show more

Table 3.6. ovnKubernetesConfig.ipv6 objectField| Type| Description  
---|---|---  
`internalTransitSwitchSubnet` |  string  |  If your existing network infrastructure overlaps with the `fd97::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.  The default value is `fd97::/64`.   
`internalJoinSubnet` |  string  |  If your existing network infrastructure overlaps with the `fd98::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster.  The default value is `fd98::/64`.   
Show more

Table 3.7. policyAuditConfig objectField| Type| Description  
---|---|---  
`rateLimit` |  integer  |  The maximum number of messages to generate every second per node. The default value is `20` messages per second.   
`maxFileSize` |  integer  |  The maximum size for the audit log in bytes. The default value is `50000000` or 50 MB.   
`maxLogFiles` |  integer  |  The maximum number of log files that are retained.   
`destination` |  string  |  One of the following additional audit log targets: 

`libc`
     The libc `syslog()` function of the journald process on the host. 
`udp:<host>:<port>`
     A syslog server. Replace `<host>:<port>` with the host and port of the syslog server. 
`unix:<file>`
     A UNIX Domain Socket file specified by `<file>`. 
`null`
     Do not send the audit logs to any additional target.   
`syslogFacility` |  string  |  The syslog facility, such as `kern`, as defined by RFC5424. The default value is `local0`.   
Show more

Table 3.8. gatewayConfig objectField| Type| Description  
---|---|---  
`routingViaHost` |  `boolean` |  Set this field to `true` to send egress traffic from pods to the host networking stack. For highly-specialized installations and applications that rely on manually configured routes in the kernel routing table, you might want to route egress traffic to the host networking stack. By default, egress traffic is processed in OVN to exit the cluster and is not affected by specialized routes in the kernel routing table. The default value is `false`.  This field has an interaction with the Open vSwitch hardware offloading feature. If you set this field to `true`, you do not receive the performance benefits of the offloading because egress traffic is processed by the host networking stack.   
`ipForwarding` |  `object` |  You can control IP forwarding for all traffic on OVN-Kubernetes managed interfaces by using the `ipForwarding` specification in the `Network` resource. Specify `Restricted` to only allow IP forwarding for Kubernetes related traffic. Specify `Global` to allow forwarding of all IP traffic. For new installations, the default is `Restricted`. For updates to OpenShift Container Platform 4.14 or later, the default is `Global`.  Note The default value of `Restricted` sets the IP forwarding to drop.   
`ipv4` |  `object` |  Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv4 addresses.   
`ipv6` |  `object` |  Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv6 addresses.   
Show more

Table 3.9. gatewayConfig.ipv4 objectField| Type| Description  
---|---|---  
`internalMasqueradeSubnet` |  `string` |  The masquerade IPv4 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses and the shared gateway bridge interface. The default value is `169.254.169.0/29`.  Important For OpenShift Container Platform 4.17 and later versions, clusters use `169.254.0.0/17` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.   
Show more

Table 3.10. gatewayConfig.ipv6 objectField| Type| Description  
---|---|---  
`internalMasqueradeSubnet` |  `string` |  The masquerade IPv6 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses and the shared gateway bridge interface. The default value is `fd69::/125`.  Important For OpenShift Container Platform 4.17 and later versions, clusters use `fd69::/112` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet.   
Show more

Table 3.11. ipsecConfig objectField| Type| Description  
---|---|---  
`mode` |  `string` |  Specifies the behavior of the IPsec implementation. Must be one of the following values: 

  * `Disabled`: IPsec is not enabled on cluster nodes. 
  * `External`: IPsec is enabled for network traffic with external hosts. 
  * `Full`: IPsec is enabled for pod traffic and network traffic with external hosts. 

  
Show more

**Example OVN-Kubernetes configuration with IPsec enabled**

```yaml
defaultNetwork:
  type: OVNKubernetes
  ovnKubernetesConfig:
    mtu: 1400
    genevePort: 6081
    ipsecConfig:
      mode: Full
```


## 3.3.6. Configure hybrid networking with OVN-Kubernetes

To configure hybrid networking with OVN-Kubernetes, you can set `hybridOverlayConfig` during installation or patch the Cluster Network Operator (CNO) after installation. 

Note

This configuration is necessary to run both Linux and Windows nodes in the same cluster. 

**Prerequisites**

  * You defined `OVNKubernetes` for the `networking.networkType` parameter in the `install-config.yaml` file. See the installation documentation for configuring OpenShift Container Platform network customizations on your chosen cloud provider for more information. 



**Procedure**

  1. Change to the directory that contains the installation program and create the manifests: 

```shell-session
$ ./openshift-install create manifests --dir <installation_directory>
```


For the `<installation_directory>`, specify the name of the directory that contains the `install-config.yaml` file for your cluster. 

  2. Create a stub manifest file for the advanced network configuration that is named `cluster-network-03-config.yml` in the `<installation_directory>/manifests/` directory: 

```shell-session
$ cat <<EOF > <installation_directory>/manifests/cluster-network-03-config.yml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
EOF
```


For `<installation_directory>`, specify the directory name that contains the `manifests/` directory for your cluster. 

  3. Open the `cluster-network-03-config.yml` file in an editor and specify a hybrid networking configuration similar to the following example: 

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      hybridOverlayConfig:
        hybridClusterNetwork:
        - cidr: 10.132.0.0/14
          hostPrefix: 23
        hybridOverlayVXLANPort: 9898
```


where: 

`spec.defaultNetwork.ovnKubernetesConfig.hybridOverlayConfig.hybridClusterNetwork`
     Specifies the CIDR configuration used for nodes on the additional overlay network. The `hybridClusterNetwork` CIDR must not overlap with the `clusterNetwork` CIDR. 
`spec.defaultNetwork.ovnKubernetesConfig.hybridOverlayConfig.hybridOverlayVXLANPort`
    

Specifies a custom VXLAN port for the additional overlay network. This is required for running Windows nodes in a cluster installed on vSphere, and must not be configured for any other cloud provider. The custom port can be any open port excluding the default `6081` port. For more information on this requirement, see [Pod-to-pod connectivity between hosts is broken](https://docs.microsoft.com/en-us/virtualization/windowscontainers/kubernetes/common-problems#pod-to-pod-connectivity-between-hosts-is-broken-on-my-kubernetes-cluster-running-on-vsphere) in the Microsoft documentation. 

Note

Windows Server Long-Term Servicing Channel (LTSC): Windows Server 2019 is not supported on clusters with a custom `hybridOverlayVXLANPort` value because this Windows server version does not support selecting a custom VXLAN port. 

  4. Save the `cluster-network-03-config.yml` file and quit the text editor. 
  5. Optional: Back up the `manifests/cluster-network-03-config.yml` file. The installation program deletes the `manifests/` directory when creating the cluster. 



Note

For more information about using Linux and Windows nodes in the same cluster, see [Understanding Windows container workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/windows_container_support_for_openshift/#understanding-windows-container-workloads). 

**Additional resources**

  * For more details about Accelerated Networking, see [Accelerated Networking for Microsoft Azure VMs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#machineset-azure-accelerated-networking_creating-machineset-azure). 



## 3.3.7. Configuring user-defined tags for Azure

In OpenShift Container Platform, you can use tags for grouping resources and for managing resource access and cost. 

Tags are applied only to the resources created by the OpenShift Container Platform installation program and its core Operators such as Machine API Operator, Cluster Ingress Operator, Cluster Image Registry Operator. The OpenShift Container Platform consists of the following types of tags: 

OpenShift Container Platform tags
     By default, OpenShift Container Platform installation program attaches the OpenShift Container Platform tags to the Azure resources. These OpenShift Container Platform tags are not accessible to the users. The format of the OpenShift Container Platform tags is `kubernetes.io_cluster.<cluster_id>:owned`, where `<cluster_id>` is the value of `.status.infrastructureName` in the infrastructure resource for the cluster. 
User-defined tags
    

User-defined tags are manually created in `install-config.yaml` file during installation. When creating the user-defined tags, you must consider the following points: 

  * User-defined tags on Azure resources can only be defined during OpenShift Container Platform cluster creation, and cannot be modified after the cluster is created. 
  * Support for user-defined tags is available only for the resources created in the Azure Public Cloud. 
  * User-defined tags are not supported for the OpenShift Container Platform clusters upgraded to OpenShift Container Platform 4.22. 



### 3.3.7.1. Creating user-defined tags for Azure

To define the list of user-defined tags, edit the `.platform.azure.userTags` field in the `install-config.yaml` file. 

**Procedure**

  * Specify the `.platform.azure.userTags` field as shown in the following `install-config.yaml` file: 

```yaml
apiVersion: v1
baseDomain: example.com
#...
platform:
  azure:
    userTags:
      <key>: <value>
#...
```


where: 

`.platform.azure.userTags`
     Specifies the additional keys and values that the installation program adds as tags to all Azure resources that it creates. 
`<key>: <value>`
    

Specifies the key and value. You can configure a maximum of 10 tags for resource group and resources. Tag keys are case-insensitive. For more information on requirements for specifying user-defined tags, see "User-defined tags requirements" section. 

**Example`install-config.yaml` file**

```yaml
apiVersion: v1
baseDomain: example.com
#...
platform:
  azure:
    userTags:
      createdBy: user
      environment: dev
#...
```


**Verification**

  * Access the list of created user-defined tags for the Azure resources by running the following command: 

```shell-session
$ oc get infrastructures.config.openshift.io cluster -o=jsonpath-as-json='{.status.platformStatus.azure.resourceTags}'
```


**Example output**

```plaintext
[
    [
        {
            "key": "createdBy",
            "value": "user"
        },
        {
            "key": "environment",
            "value": "dev"
        }
    ]
]
```


### 3.3.7.2. User-defined tags requirements

The user-defined tags have the following requirements: 

  * A tag key must have a maximum of 128 characters. 
  * A tag key must begin with a letter. 
  * A tag key must end with a letter, number or underscore. 
  * A tag key must contain only letters, numbers, underscores(`_`), periods(`.`), and hyphens(`-`). 
  * A tag key must not be specified as `name`. 
  * A tag key must not have the following prefixes: 

    * `kubernetes.io`
    * `openshift.io`
    * `microsoft`
    * `azure`
    * `windows`

  * A tag value must have a maximum of 256 characters. 



For more information about Azure tags, see [Azure user-defined tags](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources?tabs=json). 

## 3.3.8. Alternatives to storing administrator-level secrets in the kube-system project

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must use one of the following alternatives: 

  * To manage long-term cloud credentials manually, follow the procedure in [Manually creating long-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_azure/installer-provisioned-infrastructure#manually-create-iam_installing-azure-customizations "3.3.8.1. Manually creating long-term credentials"). 
  * To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in [Configuring an Azure cluster to use short-term credentials](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_azure/installer-provisioned-infrastructure#installing-azure-with-short-term-creds_installing-azure-customizations "3.3.8.2. Configuring an Azure cluster to use short-term credentials"). 



### 3.3.8.1. Manually creating long-term credentials

You can put the Cloud Credential Operator (CCO) into manual mode before OpenShift Container Platform installation if the cloud identity and access management (IAM) APIs are not reachable, or if you prefer not to store an administrator-level credential secret in the cluster `kube-system` namespace. 

**Procedure**

  1. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown: 

**Sample configuration file snippet**

```yaml
apiVersion: v1
baseDomain: example.com
credentialsMode: Manual
# ...
```


  2. If you have not previously created installation manifest files, do so by running the following command: 

```shell-session
$ openshift-install create manifests --dir <installation_directory>
```


where `<installation_directory>` is the directory in which the installation program creates files. 

  3. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command: 

```shell-session
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
```


  4. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command: 

```shell-session
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
  --to=<path_to_directory_for_credentials_requests>
```


where: 

`--included`
     Specifies only the manifests that your specific cluster configuration requires. 
`<path_to_directory_with_installation_configuration>`
     Specifies the location of the `install-config.yaml` file. 
`<path_to_directory_for_credentials_requests>`
    

Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it. 

This command creates a YAML file for each `CredentialsRequest` object. 

**Sample`CredentialsRequest` object**

```yaml
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: <component_credentials_request>
  namespace: openshift-cloud-credential-operator
  ...
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AzureProviderSpec
    roleBindings:
    - role: Contributor
  ...
```


  5. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object. 

**Sample`CredentialsRequest` object with secrets**

```yaml
apiVersion: cloudcredential.openshift.io/v1
kind: CredentialsRequest
metadata:
  name: <component_credentials_request>
  namespace: openshift-cloud-credential-operator
  ...
spec:
  providerSpec:
    apiVersion: cloudcredential.openshift.io/v1
    kind: AzureProviderSpec
    roleBindings:
    - role: Contributor
      ...
  secretRef:
    name: <component_secret>
    namespace: <component_namespace>
  ...
```


**Sample`Secret` object**

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: <component_secret>
  namespace: <component_namespace>
data:
  azure_subscription_id: <base64_encoded_azure_subscription_id>
  azure_client_id: <base64_encoded_azure_client_id>
  azure_client_secret: <base64_encoded_azure_client_secret>
  azure_tenant_id: <base64_encoded_azure_tenant_id>
  azure_resource_prefix: <base64_encoded_azure_resource_prefix>
  azure_resourcegroup: <base64_encoded_azure_resourcegroup>
  azure_region: <base64_encoded_azure_region>
```


Important

Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state. 




### 3.3.8.2. Configuring an Azure cluster to use short-term credentials

To install a cluster that uses Microsoft Entra Workload ID, you must configure the Cloud Credential Operator utility and create the required Azure resources for your cluster. 

#### 3.3.8.2.1. Configuring the Cloud Credential Operator utility

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary. 

Note

The `ccoctl` utility is a Linux binary that must run in a Linux environment. 

**Prerequisites**

  * You have access to an OpenShift Container Platform account with cluster administrator access. 
  * You have installed the OpenShift CLI (`oc`). 



  * You have created a global Azure account for the `ccoctl` utility to use with the following permissions: 

    * `Microsoft.Resources/subscriptions/resourceGroups/read`
    * `Microsoft.Resources/subscriptions/resourceGroups/write`
    * `Microsoft.Resources/subscriptions/resourceGroups/delete`
    * `Microsoft.Authorization/roleAssignments/read`
    * `Microsoft.Authorization/roleAssignments/delete`
    * `Microsoft.Authorization/roleAssignments/write`
    * `Microsoft.Authorization/roleDefinitions/read`
    * `Microsoft.Authorization/roleDefinitions/write`
    * `Microsoft.Authorization/roleDefinitions/delete`
    * `Microsoft.Storage/storageAccounts/listkeys/action`
    * `Microsoft.Storage/storageAccounts/delete`
    * `Microsoft.Storage/storageAccounts/read`
    * `Microsoft.Storage/storageAccounts/write`
    * `Microsoft.Storage/storageAccounts/blobServices/containers/delete`
    * `Microsoft.Storage/storageAccounts/blobServices/containers/read`
    * `Microsoft.Storage/storageAccounts/blobServices/containers/write`
    * `Microsoft.ManagedIdentity/userAssignedIdentities/delete`
    * `Microsoft.ManagedIdentity/userAssignedIdentities/read`
    * `Microsoft.ManagedIdentity/userAssignedIdentities/write`
    * `Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentials/read`
    * `Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentials/write`
    * `Microsoft.ManagedIdentity/userAssignedIdentities/federatedIdentityCredentials/delete`
    * `Microsoft.Storage/register/action`
    * `Microsoft.ManagedIdentity/register/action`




**Procedure**

  1. Set a variable for the OpenShift Container Platform release image by running the following command: 

```shell-session
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
```


  2. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command: 

```shell-session
$ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
```


Note

Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool. 

  3. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command: 

```shell-session
$ oc image extract $CCO_IMAGE \
  --file="/usr/bin/ccoctl.<rhel_version>" \
  -a ~/.pull-secret
```


For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid: 

     * `rhel8`: Specify this value for hosts that use RHEL 8. 
     * `rhel9`: Specify this value for hosts that use RHEL 9. 

Note

The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`. 

  4. Change the permissions to make `ccoctl` executable by running the following command: 

```shell-session
$ chmod 775 ccoctl
```


**Verification**

  * To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example: 

```shell-session
$ ./ccoctl
```


**Example output**

```shell-session
OpenShift credentials provisioning tool

Usage:
  ccoctl [command]

Available Commands:
  aws          Manage credentials objects for AWS cloud
  azure        Manage credentials objects for Azure
  gcp          Manage credentials objects for Google cloud
  help         Help about any command
  ibmcloud     Manage credentials objects for IBM Cloud
  nutanix      Manage credentials objects for Nutanix

Flags:
  -h, --help   help for ccoctl

Use "ccoctl [command] --help" for more information about a command.
```


#### 3.3.8.2.2. Creating Azure resources with the Cloud Credential Operator utility

You can use the `ccoctl azure create-all` command to automate the creation of Azure resources. 

Note

By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory. 

**Prerequisites**

You must have: 

  * Extracted and prepared the `ccoctl` binary. 
  * Access to your Microsoft Azure account by using the Azure CLI. 



**Procedure**

  1. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command: 

```shell-session
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
```


  2. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command: 

```shell-session
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \
  --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
  --to=<path_to_directory_for_credentials_requests>
```


where: 

`--included`
     Specifies to include only the manifests that your specific cluster configuration requires. 
`<path_to_directory_with_installation_configuration>`
     Specifies the location of the `install-config.yaml` file. 
`<path_to_directory_for_credentials_requests>`
    

Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it. 

Note

This command might take a few moments to run. 

  3. To enable the `ccoctl` utility to detect your Azure credentials automatically, log in to the Azure CLI by running the following command: 

```shell-session
$ az login
```


  4. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command: 

```shell-session
$ ccoctl azure create-all \
  --name=<azure_infra_name> \
  --output-dir=<ccoctl_output_dir> \
  --region=<azure_region> \
  --subscription-id=<azure_subscription_id> \
  --credentials-requests-dir=<path_to_credentials_requests_directory> \
  --dnszone-resource-group-name=<azure_dns_zone_resource_group_name> \
  --tenant-id=<azure_tenant_id> \
  --network-resource-group-name <azure_resource_group> \
  --preserve-existing-roles
```


where: 

`<azure_infra_name>`
     Specifies the user-defined name for all created Azure resources used for tracking. 
`<ccoctl_output_dir>`
     Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run. This parameter is optional. 
`<azure_region>`
     Specifies the Azure region in which cloud resources will be created. 
`<azure_subscription_id>`
     Specifies the Azure subscription ID to use. 
`<path_to_credentials_requests_directory>`
     Specifies the directory containing the files for the component `CredentialsRequest` objects. 
`<azure_dns_zone_resource_group_name>`
     Specifies the name of the resource group containing the cluster’s base domain Azure DNS zone. 
`<azure_tenant_id>`
     Specifies the Azure tenant ID to use. 
`<azure_resource_group>`
     Specifies the virtual network resource group if it is different from the cluster resource group. This parameter is optional. 
`--preserve-existing-roles`
    

Specifies that any custom role assignments you define on managed identities are not removed during OpenShift Container Platform updates. This parameter is optional. 

Note

If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter. 

To see additional optional parameters and explanations of how to use them, run the `azure create-all --help` command. 




**Verification**

  * To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory: 

```shell-session
$ ls <path_to_ccoctl_output_dir>/manifests
```


**Example output**

```plaintext
azure-ad-pod-identity-webhook-config.yaml
cluster-authentication-02-config.yaml
openshift-cloud-controller-manager-azure-cloud-credentials-credentials.yaml
openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
openshift-cluster-api-capz-manager-bootstrap-credentials-credentials.yaml
openshift-cluster-csi-drivers-azure-disk-credentials-credentials.yaml
openshift-cluster-csi-drivers-azure-file-credentials-credentials.yaml
openshift-image-registry-installer-cloud-credentials-credentials.yaml
openshift-ingress-operator-cloud-credentials-credentials.yaml
openshift-machine-api-azure-cloud-credentials-credentials.yaml
```


You can verify that the Microsoft Entra ID service accounts are created by querying Azure. For more information, refer to Azure documentation on listing Entra ID service accounts. 




#### 3.3.8.2.3. Incorporating the Cloud Credential Operator utility manifests

To implement short-term security credentials managed outside the cluster for individual OpenShift Container Platform components, you must move the manifest files that the Cloud Credential Operator utility (`ccoctl`) created to the correct directories for the installation program. 

**Prerequisites**

  * You have configured an account with the cloud platform that hosts your cluster. 
  * You have configured the Cloud Credential Operator utility (`ccoctl`). 
  * You have created the cloud provider resources that are required for your cluster with the `ccoctl` utility. 



**Procedure**

  1. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown: 

**Sample configuration file snippet**

```yaml
apiVersion: v1
baseDomain: example.com
credentialsMode: Manual
# ...
```


  2. If you used the `ccoctl` utility to create a new Azure resource group instead of using an existing resource group, modify the `resourceGroupName` parameter in the `install-config.yaml` as shown: 

**Sample configuration file snippet**

```yaml
apiVersion: v1
baseDomain: example.com
# ...
platform:
  azure:
    resourceGroupName: <azure_infra_name>
# ...
```


The `<azure_infra_name>` value must match the user-defined name for Azure resources that was specified with the `--name` argument of the `ccoctl azure create-all` command. 

  3. If you have not previously created installation manifest files, do so by running the following command: 

```shell-session
$ openshift-install create manifests --dir <installation_directory>
```


where `<installation_directory>` is the directory in which the installation program creates files. 

  4. Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command: 

```shell-session
$ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
```


  5. Copy the `tls` directory that contains the private key to the installation directory: 

```shell-session
$ cp -a /<path_to_ccoctl_output_dir>/tls .
```


## 3.3.9. Deploying the cluster

To deploy your OpenShift Container Platform cluster, you initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions the required infrastructure and completes the cluster setup. 

Important

You can run the `create cluster` command of the installation program only once, during initial installation. 

**Prerequisites**

  * You have configured an account with the cloud platform that hosts your cluster. 
  * You have the OpenShift Container Platform installation program and the pull secret for your cluster. 
  * You have an Azure subscription ID and tenant ID. 



**Procedure**

  * In the directory that contains the installation program, initialize the cluster deployment by running the following command: 

```shell-session
$ ./openshift-install create cluster --dir <installation_directory> \
    --log-level=info
```


where: 

    * `<installation_directory>`: Specifies the location of your customized `./install-config.yaml` file. 
    * `--log-level`: Specifies the log level. To view different installation details, specify `warn`, `debug`, or `error` instead of `info`. 




**Verification**

When the cluster deployment completes successfully: 

  * The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user. 
  * Credential information also outputs to `<installation_directory>/.openshift_install.log`. 

Important

Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster. 

The following example shows the expected output: 

```shell-session
...
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
INFO Login to the console with user: "kubeadmin", and password: "password"
INFO Time elapsed: 36m22s
```


Important

    * The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information. 
    * It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation. 




## 3.3.10. Provisioning your own DNS records

Use the IP address of the API server to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. 

Use the IP address of the Ingress service to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. 

**Prerequisite**

  * You have installed the Azure CLI client `(az)`. 



**Procedure**

  1. Add the `userProvisionedDNS` parameter to the `install-config.yaml` file and enable the parameter. For more information, see "Enabling a user-managed DNS". 
  2. Install your cluster. 
  3. If you are installing a private cluster, set the `lb_name` variable by running the following command: 

```shell-session
$ lb_name="${infra_id}-internal"
```


     1. Set the `frontendipconfig_id` variable by running the following command: 

```shell-session
$ frontendipconfig_id=$(az network lb show -n ${lb_name} -g ${cluster_resource_group_name} -ojson | jq -r ".loadBalancingRules[] | select(.frontendPort == 6443) | .frontendIPConfiguration.id")
```


     2. Set the `frontendipconfig_name` variable by running the following command: 

```shell-session
$ frontendipconfig_name=${frontendipconfig_id##*/}
```


     3. To retrieve the IP address of the API service, run the following command: 

```shell-session
$ az network lb frontend-ip show -n ${frontendipconfig_name} --lb-name ${lb_name} -g ${cluster_resource_group_name} --query "privateIPAddress" -otsv
```


  4. If you are installing a public cluster, set the `lb_name` variable by running the following command: 

```shell-session
$ lb_name="${infra_id}"
```


     1. Set the `frontendipconfig_id` variable by running the following command: 

```shell-session
$ frontendipconfig_id=$(az network lb show -n ${lb_name} -g ${cluster_resource_group_name} -ojson | jq -r ".loadBalancingRules[] | select(.frontendPort == 6443) | .frontendIPConfiguration.id")
```


     2. Set the `frontendipconfig_name` variable by running the following command: 

```shell-session
$ frontendipconfig_name=${frontendipconfig_id##*/}
```


     3. Set the `frontendpublicip_id` variable by running the following command: 

```shell-session
$ frontendpublicip_id=$(az network lb frontend-ip show -n ${frontendipconfig_name} --lb-name ${lb_name} -g ${cluster_resource_group_name} --query "publicIPAddress.id" -otsv)
```


     4. To retrieve the IP address of the API service, run the following command: 

```shell-session
$ az network public-ip show --ids ${frontendpublicip_id} --query 'ipAddress' -otsv
```


  5. Use the IP address and your cluster name and base cluster domain to configure your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname. 
  6. If you are installing a private cluster, set the `lb_name` variable by running the following command: 

```shell-session
$ lb_name="${infra_id}-internal"
```


     1. Set the `frontendipconfig_id` variable by running the following command: 

```shell-session
$ frontendipconfig_id=$(az network lb show -n ${lb_name} -g ${cluster_resource_group_name} -ojson | jq -r ".loadBalancingRules[] | select(.frontendPort == 443) | .frontendIPConfiguration.id")
```


     2. Set the `frontendipconfig_name` variable by running the following command: 

```shell-session
$ frontendipconfig_name=${frontendipconfig_id##*/}
```


     3. To retrieve the IP address of the Ingress service, run the following command: 

```shell-session
$ az network lb frontend-ip show -n ${frontendipconfig_name} --lb-name ${lb_name} -g ${cluster_resource_group_name} --query "privateIPAddress" -otsv
```


  7. If you are installing a public cluster, set the `lb_name` variable by running the following command: 

```shell-session
$ lb_name="${infra_id}"
```


     1. Set the `frontendipconfig_id` variable by running the following command: 

```shell-session
$ frontendipconfig_id=$(az network lb show -n ${lb_name} -g ${cluster_resource_group_name} -ojson | jq -r ".loadBalancingRules[] | select(.frontendPort == 443) | .frontendIPConfiguration.id")
```


     2. Set the `frontendipconfig_name` variable by running the following command: 

```shell-session
$ frontendipconfig_name=${frontendipconfig_id##*/}
```


     3. Set the `frontendpublicip_id` variable by running the following command: 

```shell-session
$ frontendpublicip_id=$(az network lb frontend-ip show -n ${frontendipconfig_name} --lb-name ${lb_name} -g ${cluster_resource_group_name} --query "publicIPAddress.id" -otsv)
```


     4. To retrieve the IP address of the Ingress service, run the following command: 

```shell-session
$ az network public-ip show --ids ${frontendpublicip_id} --query 'ipAddress' -otsv
```


  8. Use the IP address and your cluster name and base cluster domain to configure your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname. 



## 3.3.11. Logging in to the cluster by using the CLI

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation. 

The `kubeconfig` file is specific to a cluster and OpenShift Container Platform generates it during installation. 

**Prerequisites**

  * You deployed an OpenShift Container Platform cluster. 
  * You installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Export the `kubeadmin` credentials by running the following command: 

```shell-session
$ export KUBECONFIG=<installation_directory>/auth/kubeconfig
```


where: 

`<installation_directory>`
     Specifies the path to the directory that stores the installation files. 

  2. Verify you can run `oc` commands successfully using the exported configuration by running the following command: 

```shell-session
$ oc whoami
```


**Example output**

```shell-session
system:admin
```


**Next steps**

  * "Customize your cluster" 
  * "Remote health reporting" 



**Additional resources**

  * [Accessing the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/web_console/#web-console)



## 3.3.12. Next steps

  * [Customize your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations). 
  * If necessary, you can [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting).
