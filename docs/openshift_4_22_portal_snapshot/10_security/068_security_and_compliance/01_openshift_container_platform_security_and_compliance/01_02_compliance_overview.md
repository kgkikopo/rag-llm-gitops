# 1.2. Compliance overview

For many OpenShift Container Platform customers, regulatory readiness, or compliance, on some level is required before any systems can be put into production. That regulatory readiness can be imposed by national standards, industry standards, or the organization’s corporate governance framework. 

## 1.2.1. Compliance checking

Administrators can use the [Compliance Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/compliance-operator#understanding-compliance-operator "5.4.1. About the Compliance Operator") to run compliance scans and recommend remediations for any issues found. The [`oc-compliance` plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/compliance-operator#using-oc-compliance-plug-in "5.6.9. Using the oc-compliance plugin") is an OpenShift CLI (`oc`) plugin that provides a set of utilities to easily interact with the Compliance Operator. 

## 1.2.2. File integrity checking

Administrators can use the [File Integrity Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/file-integrity-operator#understanding-file-integrity-operator "6.6. Understanding the File Integrity Operator") to continually run file integrity checks on cluster nodes and provide a log of files that have been modified.
