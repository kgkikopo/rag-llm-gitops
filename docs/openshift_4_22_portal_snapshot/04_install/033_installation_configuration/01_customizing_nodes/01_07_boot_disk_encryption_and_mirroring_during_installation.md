# 1.7. Boot disk encryption and mirroring during installation

You can configure the OpenShift Container Platform installation to enable boot disk encryption and mirroring on the cluster nodes. 

OpenShift Container Platform supports the Trusted Platform Module (TPM) v2 and Tang encryption modes. 

TPM v2
     This is the preferred mode. TPM v2 stores passphrases in a secure cryptoprocessor on the server. You can use this mode to prevent decryption of the boot disk data on a cluster node if the disk is removed from the server. 
Tang
     Tang and Clevis are server and client components that enable network-bound disk encryption (NBDE). You can bind the boot disk data on your cluster nodes to one or more Tang servers. This prevents decryption of the data unless the nodes are on a secure network where the Tang servers are accessible. Clevis is an automated decryption framework used to implement decryption on the client side. 

Important

The use of the Tang encryption mode to encrypt your disks is only supported for bare metal and vSphere installations on user-provisioned infrastructure. 

In earlier versions of Red Hat Enterprise Linux CoreOS (RHCOS), disk encryption was configured by specifying `/etc/clevis.json` in the Ignition config. The file is not supported in clusters created with OpenShift Container Platform 4.7 or later. 

When the TPM v2 or Tang encryption modes are enabled, the RHCOS boot disks are encrypted using the LUKS2 format. 

Note the following points about the boot disk encryption and mirroring feature: 

  * Is available for installer-provisioned infrastructure, user-provisioned infrastructure, and Assisted Installer deployments 
  * For Assisted Installer deployments: 

    * Each cluster can only have a single encryption method, Tang or TPM 
    * Encryption can be enabled on some or all nodes 
    * There is no Tang threshold; all servers must be valid and operational 
    * Encryption applies to the installation disks only, not to the workload disks 

  * Is supported on Red Hat Enterprise Linux CoreOS (RHCOS) systems only 
  * Sets up disk encryption during the manifest installation phase, encrypting all data written to disk, from first boot forward 
  * Requires no user intervention for providing passphrases 
  * Uses AES-256-XTS encryption 



## 1.7.1. Configuring an encryption threshold

In OpenShift Container Platform, define an encryption threshold to require more than one Tang server for boot disk decryption. 

You can also configure the TPM v2 and Tang encryption modes simultaneously. Configuring both modes enables boot disk data decryption only if the TPM secure cryptoprocessor is present and the Tang servers are accessible over a secure network. 

You can use the `threshold` attribute in your Butane configuration to define the minimum number of TPM v2 and Tang encryption conditions required for decryption to occur. 

The threshold is met when the stated value is reached through any combination of the declared conditions. In the case of offline provisioning, the offline server is accessed by using an included advertisement, and only uses that supplied advertisement if the number of online servers does not meet the set threshold. 

**Procedure**

  * Create the Butane configuration file and define a disk encryption configuration in the file. For example, the `threshold` value of `2` in the following configuration can be reached by accessing two Tang servers, where the offline server is available as a backup, or by accessing the TPM secure cryptoprocessor and one of the Tang servers. 

**Example Butane configuration for disk encryption**

```yaml
variant: openshift
version: 4.22.0
metadata:
  name: worker-storage
  labels:
    machineconfiguration.openshift.io/role: worker
boot_device:
  layout: x86_64
  luks:
    tpm2: true
    tang:
      - url: http://tang1.example.com:7500
        thumbprint: jwGN5tRFK-kF6pIX89ssF3khxxX
      - url: http://tang2.example.com:7500
        thumbprint: VCJsvZFjBSIHSldw78rOrq7h2ZF
      - url: http://tang3.example.com:7500
        thumbprint: PLjNyRdGw03zlRoGjQYMahSZGu9
        advertisement: "{\"payload\": \"...\", \"protected\": \"...\", \"signature\": \"...\"}"
    threshold: 2
openshift:
  fips: true
```


where: 

`boot_device.layout`
     Specifies the instruction set architecture of the cluster nodes. Some examples include, `x86_64`, `aarch64`, or `ppc64le`. 
`boot_device.luks.tpm2`
     When `true`, specifies that you want to use a Trusted Platform Module (TPM) to encrypt the root file system. 
`boot_device.luks.tang`
     Specifies that you want to use the listed Tang servers. 
`boot_device.luks.tang.advertisement`
     Optional parameter. Specifies offline provisioning. Ignition provisions the Tang server binding rather than fetching the advertisement from the server at runtime. This lets the server be unavailable at provisioning time. 
`boot_device.luks.threshold`
    

Specifies the minimum number of TPM v2 and Tang encryption conditions required for decryption to occur. 

Important

The default `threshold` value is `1`. If you include multiple encryption conditions in your configuration but do not specify a threshold, decryption can occur if any of the conditions are met. 

Note

If you require TPM v2 _and_ Tang for decryption, the value of the `threshold` attribute must equal the total number of stated Tang servers plus one. If the `threshold` value is lower, you can reach the threshold value by using a single encryption mode. 

For example, if you set `tpm2` to `true` and specify two Tang servers, a threshold of `2` can be met by accessing the two Tang servers, even if the TPM secure cryptoprocessor is not available.
