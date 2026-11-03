# 6.1. File Integrity Operator overview

The File Integrity Operator continually runs file integrity checks on the cluster nodes. It deploys a DaemonSet that initializes and runs privileged Advanced Intrusion Detection Environment (AIDE) containers on each node, providing a log of files that have been modified since the initial run of the DaemonSet pods. 

Note

File Integrity Operator is not supported on HCP clusters. 

  * [File Integrity Operator release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/file-integrity-operator#file-integrity-operator-release-notes "6.2. Release notes for the File Integrity Operator")
  * [File Integrity Operator support](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/file-integrity-operator#fio-support "6.3. File Integrity Operator support")
  * [Installing the File Integrity Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/file-integrity-operator#installing-file-integrity-operator "6.4. Installing the File Integrity Operator")
  * [Updating the File Integrity Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/file-integrity-operator#file-integrity-operator-updating "6.5. Updating the File Integrity Operator")
  * [Understanding the File Integrity Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/file-integrity-operator#understanding-file-integrity-operator "6.6. Understanding the File Integrity Operator")
  * [Configuring the Custom File Integrity Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/file-integrity-operator#configuring-file-integrity-operator "6.7. Configuring the Custom File Integrity Operator")
  * [Performing advanced Custom File Integrity Operator tasks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/file-integrity-operator#file-integrity-operator-advanced-usage "6.8. Performing advanced Custom File Integrity Operator tasks")
  * [Troubleshooting the File Integrity Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/file-integrity-operator#troubleshooting-file-integrity-operator "6.9. Troubleshooting the File Integrity Operator")
  * [Uninstalling the File Integrity Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/file-integrity-operator#fio-uninstalling "6.10. Uninstalling the File Integrity Operator")
