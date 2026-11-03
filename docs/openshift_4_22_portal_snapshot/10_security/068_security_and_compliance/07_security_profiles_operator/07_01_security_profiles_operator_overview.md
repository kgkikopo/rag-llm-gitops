# 7.1. Security Profiles Operator overview

With the OpenShift Container Platform Security Profiles Operator (SPO), you can define seccomp and SELinux profiles as custom resources and keep them synchronized across every node in a namespace. 

The SPO distributes seccomp and SELinux profile custom resources to each node and keeps them up to date when profiles change. You can also bind policies to pods and record workloads. See Additional resources for advanced tasks such as enabling the log enricher, configuring webhooks and metrics, or restricting profiles to a single namespace, and for advanced audit logging that correlates cluster users with actions during `oc exec`, `oc rsh`, and `oc debug` sessions. 

## 7.1.1. Additional resources

  * [Security Profiles Operator release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/security-profiles-operator#spo-release-notes "7.2. Release notes for the Security Profiles Operator")
  * [Security Profiles Operator support](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/security-profiles-operator#spo-support "7.3. Security Profiles Operator support")
  * [Understanding the Security Profiles Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/security-profiles-operator#spo-understanding "7.4. Understanding the Security Profiles Operator")
  * [Enabling the Security Profiles Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/security-profiles-operator#spo-enabling "7.5. Enabling the Security Profiles Operator")
  * [Managing seccomp profiles](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/security-profiles-operator#spo-seccomp "7.6. Managing seccomp profiles")
  * [Managing SELinux profiles](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/security-profiles-operator#spo-selinux "7.7. Managing SELinux profiles")
  * [Advanced Security Profiles Operator tasks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/security-profiles-operator#spo-advanced "7.8. Advanced Security Profiles Operator tasks")
  * [Advanced Audit Logging Framework](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/security-profiles-operator#spo-audit-logging "7.9. Advanced Audit Logging Framework")
  * [Troubleshooting the Security Profiles Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/security-profiles-operator#spo-inspecting-seccomp-profiles_spo-troubleshooting "7.10.1. Inspecting seccomp profiles")
  * [Uninstalling the Security Profiles Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/security-profiles-operator#spo-uninstalling "7.11. Uninstalling the Security Profiles Operator")
  * [seccomp](https://kubernetes.io/docs/tutorials/security/seccomp/)
