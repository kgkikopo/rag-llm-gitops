# 18.5. About pod security admission alerts

If your pods violate the configured pod security standards, you receive a `PodSecurityViolation` alert. This alert persists for one day so that you can investigate and resolve compliance issues. 

You can view the Kubernetes API server audit logs to investigate alerts that were triggered. As an example, a workload is likely to fail admission if global enforcement is set to the `restricted` pod security level. 

To identify pod security admission violation audit events, see "Audit annotations" in the Kubernetes documentation. 

## 18.5.1. Identify pod security violations

To identify which workloads are causing pod security violations, you can review the Kubernetes API server audit logs by using the `must-gather` tool. 

The `PodSecurityViolation` alert does not provide details on which workloads are causing pod security violations. 

**Prerequisites**

  * You have installed `jq`. 
  * You have access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. To gather the audit logs, enter the following command: 

```shell-session
$ oc adm must-gather -- /usr/bin/gather_audit_logs
```


  2. To output the affected workload details, enter the following command: 

```shell-session
$ zgrep -h pod-security.kubernetes.io/audit-violations must-gather.local.<archive_id>/<image_digest_id>/audit_logs/kube-apiserver/*log.gz \
  | jq -r 'select((.annotations["pod-security.kubernetes.io/audit-violations"] != null) and (.objectRef.resource=="pods")) | .objectRef.namespace + " " + .objectRef.name' \
  | sort | uniq -c
```


Replace `<archive_id>` and `<image_digest_id>` with the actual path names. 

**Example output**

```plaintext
1 test-namespace my-pod
```
