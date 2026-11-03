# 4.11. Use signing with Kernel Module Management (KMM)

On Secure Boot-enabled OpenShift Container Platform systems, out-of-tree kernel modules must be signed with keys enrolled in the Machine Owner’s Key (MOK) database. For kernel modules built out of tree, KMM supports signing kmods through the `sign` section of the kernel mapping in a `Module` custom resource. 

For more details on using Secure Boot, see "Generating a public and private key pair". 

## 4.11.1. Prerequisites

  * A public private key pair in the correct (DER) format. 
  * At least one secure-boot enabled node with the public key enrolled in its MOK database. 
  * Either a pre-built driver container image, or the source code and Dockerfile needed to build one in-cluster. 



**Additional resources**

  * [Generating a public and private key pair](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/managing_monitoring_and_updating_the_kernel/signing-a-kernel-and-modules-for-secure-boot_managing-monitoring-and-updating-the-kernel#generating-a-public-and-private-key-pair_signing-a-kernel-and-modules-for-secure-boot)
