# 4.1. Audit configuration

Audit logging configuration in OpenShift Container Platform is defined in the `policyAuditConfig` section of the cluster `Network` custom resource for OVN-Kubernetes. You can review these default settings to plan log destinations, file size limits, and rate limits before you enable logging. 

The following YAML illustrates the default values for the audit logging: 

**Audit logging configuration**

```yaml
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  defaultNetwork:
    ovnKubernetesConfig:
      policyAuditConfig:
        destination: "null"
        maxFileSize: 50
        rateLimit: 20
        syslogFacility: local0
```


The following table describes the configuration fields for audit logging. 

Table 4.1. policyAuditConfig objectField| Type| Description  
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
