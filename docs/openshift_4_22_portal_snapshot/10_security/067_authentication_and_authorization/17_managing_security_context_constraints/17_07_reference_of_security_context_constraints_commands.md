# 17.7. Reference of security context constraints commands

You can manage security context constraints (SCCs) in your instance as normal API objects by using the OpenShift CLI (`oc`). 

Note

You must have `cluster-admin` privileges to manage SCCs. 

## 17.7.1. Listing security context constraints

To get a current list of SCCs: 

```shell-session
$ oc get scc
```


**Example output**

```shell-session
NAME                              PRIV    CAPS                   SELINUX     RUNASUSER          FSGROUP     SUPGROUP    PRIORITY     READONLYROOTFS   VOLUMES
anyuid                            false   <no value>             MustRunAs   RunAsAny           RunAsAny    RunAsAny    10           false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
hostaccess                        false   <no value>             MustRunAs   MustRunAsRange     MustRunAs   RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","hostPath","persistentVolumeClaim","projected","secret"]
hostmount-anyuid                  false   <no value>             MustRunAs   RunAsAny           RunAsAny    RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","hostPath","nfs","persistentVolumeClaim","projected","secret"]
hostnetwork                       false   <no value>             MustRunAs   MustRunAsRange     MustRunAs   MustRunAs   <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
hostnetwork-v2                    false   ["NET_BIND_SERVICE"]   MustRunAs   MustRunAsRange     MustRunAs   MustRunAs   <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
node-exporter                     true    <no value>             RunAsAny    RunAsAny           RunAsAny    RunAsAny    <no value>   false            ["*"]
nonroot                           false   <no value>             MustRunAs   MustRunAsNonRoot   RunAsAny    RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
nonroot-v2                        false   ["NET_BIND_SERVICE"]   MustRunAs   MustRunAsNonRoot   RunAsAny    RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
privileged                        true    ["*"]                  RunAsAny    RunAsAny           RunAsAny    RunAsAny    <no value>   false            ["*"]
restricted                        false   <no value>             MustRunAs   MustRunAsRange     MustRunAs   RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
restricted-v2                     false   ["NET_BIND_SERVICE"]   MustRunAs   MustRunAsRange     MustRunAs   RunAsAny    <no value>   false            ["configMap","downwardAPI","emptyDir","persistentVolumeClaim","projected","secret"]
```


## 17.7.2. Examining security context constraints

You can view information about a particular SCC, including which users, service accounts, and groups the SCC is applied to. 

For example, to examine the `restricted` SCC: 

```shell-session
$ oc describe scc restricted
```


**Example output**

```shell-session
Name:                                  restricted
Priority:                              <none>
Access:
  Users:                               <none>
  Groups:                              <none>
Settings:
  Allow Privileged:                    false
  Allow Privilege Escalation:          true
  Default Add Capabilities:            <none>
  Required Drop Capabilities:          KILL,MKNOD,SETUID,SETGID
  Allowed Capabilities:                <none>
  Allowed Seccomp Profiles:            <none>
  Allowed Volume Types:                configMap,downwardAPI,emptyDir,persistentVolumeClaim,projected,secret
  Allowed Flexvolumes:                 <all>
  Allowed Unsafe Sysctls:              <none>
  Forbidden Sysctls:                   <none>
  Allow Host Network:                  false
  Allow Host Ports:                    false
  Allow Host PID:                      false
  Allow Host IPC:                      false
  Read Only Root Filesystem:           false
  Run As User Strategy: MustRunAsRange
    UID:                               <none>
    UID Range Min:                     <none>
    UID Range Max:                     <none>
  SELinux Context Strategy: MustRunAs
    User:                              <none>
    Role:                              <none>
    Type:                              <none>
    Level:                             <none>
  FSGroup Strategy: MustRunAs
    Ranges:                            <none>
  Supplemental Groups Strategy: RunAsAny
    Ranges:                            <none>
```


where, `Users`
     Lists which users and service accounts the SCC is applied to. 
`Groups`
     Lists which groups the SCC is applied to. 

Note

To preserve customized SCCs during upgrades, do not edit settings on the default SCCs. 

## 17.7.3. Updating security context constraints

If your custom SCC no longer satisfies your application workloads requirements, you can update your SCC by using the OpenShift CLI (`oc`). 

To update an existing SCC: 

```shell-session
$ oc edit scc <scc_name>
```


Important

To preserve customized SCCs during upgrades, do not edit settings on the default SCCs. 

## 17.7.4. Deleting security context constraints

If you no longer require your custom SCC, you can delete the SCC by using the OpenShift CLI (`oc`). 

To delete an SCC: 

```shell-session
$ oc delete scc <scc_name>
```


Important

Do not delete default SCCs. If you delete a default SCC, it is regenerated by the Cluster Version Operator.
