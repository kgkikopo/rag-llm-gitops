# Chapter 4. Support for FIPS cryptography

You can install an OpenShift Container Platform cluster in FIPS mode. 

OpenShift Container Platform is designed for FIPS. When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures. 

For more information about the NIST validation program, see "Cryptographic Module Validation Program" in the _Additional resources_ section. For the latest NIST status for the individual versions of RHEL cryptographic libraries that have been submitted for validation, see "Compliance Activities and Government Standards" in the _Additional resources_ section. 

Important

To enable FIPS mode for your cluster, you must run the installation program from a RHEL 9 computer that is configured to operate in FIPS mode, and you must use a FIPS-capable version of the installation program. See the section titled _Obtaining a FIPS-capable installation program using `oc adm extract`_. 

For more information about configuring FIPS mode on RHEL, see "Installing the system in FIPS mode" in the _Additional resources_ section. 

For the Red Hat Enterprise Linux CoreOS (RHCOS) machines in your cluster, this change is applied when the machines are deployed based on the status of an option in the `install-config.yaml` file, which governs the cluster options that a user can change during cluster deployment. With Red Hat Enterprise Linux (RHEL) machines, you must enable FIPS mode when you install the operating system on the machines that you plan to use as worker machines. 

Because FIPS must be enabled before the operating system that your cluster uses boots for the first time, you cannot enable FIPS after you deploy a cluster.

- [4.1. Obtain a FIPS-capable installation program using oc adm extract](04_01_obtain_a_fips_capable_installation_program_using_oc_adm_extract.md)
- [4.2. Additional resources](04_02_additional_resources.md)
- [4.3. Obtain a FIPS-capable installation program using the public OpenShift mirror](04_03_obtain_a_fips_capable_installation_program_using_the_public_openshift_mirror.md)
- [4.4. FIPS validation in OpenShift Container Platform](04_04_fips_validation_in_openshift_container_platform.md)
- [4.5. FIPS support in components that the cluster uses](04_05_fips_support_in_components_that_the_cluster_uses.md)
- [4.6. Installation of a cluster in FIPS mode](04_06_installation_of_a_cluster_in_fips_mode.md)
