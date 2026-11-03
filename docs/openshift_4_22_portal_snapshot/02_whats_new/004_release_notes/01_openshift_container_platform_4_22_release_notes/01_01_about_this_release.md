# 1.1. About this release

OpenShift Container Platform 4.22 release uses [Kubernetes 1.35](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.35.md) with CRI-O runtime. New features, changes, and known issues that pertain to OpenShift Container Platform 4.22 are included in this topic. 

OpenShift Container Platform 4.22 clusters are available at <https://console.redhat.com/openshift>. From the Red Hat Hybrid Cloud Console, you can deploy OpenShift Container Platform clusters to either on-premises or cloud environments. 

You must use RHCOS machines for the control plane and for the compute machines. 

Starting from OpenShift Container Platform 4.14, the Extended Update Support (EUS) phase for even-numbered releases increases the total available lifecycle to 24 months on all supported architectures, including `x86_64`, 64-bit ARM (`aarch64`), IBM Power® (`ppc64le`), and IBM Z® (`s390x`) architectures. Beyond this, Red Hat also offers a 12-month additional EUS add-on, denoted as _Additional EUS Term 2_ , that extends the total available lifecycle from 24 months to 36 months. The Additional EUS Term 2 is available on all architecture variants of OpenShift Container Platform. For more information about support for all versions, see the [Red Hat OpenShift Container Platform Life Cycle Policy](https://access.redhat.com/support/policy/updates/openshift). 

## 1.1.1. About FIPS compliance

OpenShift Container Platform is designed for FIPS. When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the `x86_64`, `ppc64le`, and `s390x` architectures. 

For more information about the NIST validation program, see [Cryptographic Module Validation Program](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/validated-modules). For the latest NIST status for the individual versions of RHEL cryptographic libraries that have been submitted for validation, see [Compliance Activities and Government Standards](https://access.redhat.com/articles/2918071#fips-140-2-and-fips-140-3-2). 

## 1.1.2. About PQC compliance

OpenShift Container Platform supports post-quantum cryptography (PQC) readiness for secure cluster communication. When running on Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS), core OpenShift Container Platform components use the cryptographic capabilities provided by the platform operating system and TLS 1.3 security profiles, including hybrid Module-Lattice-Based Key-Encapsulation Mechanism (ML-KEM) key exchange where enabled by the configured TLS security profile and supported by the component. 

For more information about NIST post-quantum cryptography standards, see [Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography). For the latest compliance information for OpenShift Container Platform, RHEL, and Red Hat Enterprise Linux CoreOS (RHCOS), see [Compliance Activities and Government Standards](https://access.redhat.com/articles/2918071).
