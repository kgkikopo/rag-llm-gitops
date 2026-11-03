# 4.6. Installation of a cluster in FIPS mode

To install a cluster in FIPS mode, follow the instructions to install a customized cluster on your preferred infrastructure. Ensure that you set `fips: true` in the `install-config.yaml` file before you deploy your cluster. 

Important

To enable FIPS mode for your cluster, you must run the installation program from a RHEL computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Installing the system in FIPS mode](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/security_hardening/assembly_installing-the-system-in-fips-mode_security-hardening). 

  * [Amazon Web Services](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-customizations)
  * [Microsoft Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-customizations)
  * [Bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal)
  * [Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-customizations)
  * [IBM Cloud®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_cloud/#installing-ibm-cloud-customizations)
  * [IBM Power®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power/#installing-ibm-power)
  * [IBM Z® and IBM® LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z)
  * [IBM Z® and IBM® LinuxONE with RHEL KVM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z-kvm)
  * [IBM Z® and IBM® LinuxONE in an LPAR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z-lpar)
  * [Red Hat OpenStack Platform (RHOSP)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_openstack/#installing-openstack-installer-custom)
  * [VMware vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere)



Note

If you are using Azure File storage, you cannot enable FIPS mode. 

To apply `AES CBC` encryption to your etcd data store, follow the "Encrypting etcd data" process after you install your cluster. 

**Additional resources**

  * [Encrypting etcd data](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/etcd/#etcd-encrypt)
