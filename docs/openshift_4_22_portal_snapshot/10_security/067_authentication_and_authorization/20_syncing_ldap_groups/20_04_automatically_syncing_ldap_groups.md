# 20.4. Automatically syncing LDAP groups

Configure a cron job to automatically sync LDAP groups with OpenShift Container Platform so you can keep group membership up to date without running manual sync commands. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You configured an LDAP identity provider (IDP). 
  * You created an LDAP secret named `ldap-secret` and a config map named `ca-config-map`. 



**Procedure**

  1. Create a project where the cron job runs by running the following command: 

```shell-session
$ oc new-project ldap-sync
```


This procedure uses a project called `ldap-sync`. 

  2. Locate the secret and config map that you created when configuring the LDAP identity provider and copy them to this new project. 

The secret and config map exist in the `openshift-config` project and must be copied to the new `ldap-sync` project. 

  3. Define a service account: 

```yaml
kind: ServiceAccount
apiVersion: v1
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync
```


  4. Create the service account by running the following command: 

```shell-session
$ oc create -f ldap-sync-service-account.yaml
```


  5. Define a cluster role: 

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: ldap-group-syncer
rules:
  - apiGroups:
      - user.openshift.io
    resources:
      - groups
    verbs:
      - get
      - list
      - create
      - update
```


  6. Create the cluster role by running the following command: 

```shell-session
$ oc create -f ldap-sync-cluster-role.yaml
```


  7. Define a cluster role binding to bind the cluster role to the service account: 

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: ldap-group-syncer
subjects:
  - kind: ServiceAccount
    name: ldap-group-syncer
    namespace: ldap-sync
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: ldap-group-syncer
```


where: 

`subjects.name`
     Specifies the service account created earlier in this procedure. 
`roleRef.name`
     Specifies the cluster role created earlier in this procedure. 

  8. Create the cluster role binding by running the following command: 

```shell-session
$ oc create -f ldap-sync-cluster-role-binding.yaml
```


  9. Define a config map that specifies the sync configuration file: 

```yaml
kind: ConfigMap
apiVersion: v1
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync
data:
  sync.yaml:
    kind: LDAPSyncConfig
    apiVersion: v1
    url: ldaps://10.0.0.0:636
    insecure: false
    bindDN: cn=admin,dc=example,dc=com
    bindPassword:
      file: "/etc/secrets/bindPassword"
    ca: /etc/ldap-ca/ca.crt
    rfc2307:
      groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        filter: "(objectClass=groupOfMembers)"
        derefAliases: never
        pageSize: 0
      groupUIDAttribute: dn
      groupNameAttributes: [ cn ]
      groupMembershipAttributes: [ member ]
      usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
      userUIDAttribute: dn
      userNameAttributes: [ uid ]
      tolerateMemberNotFoundErrors: false
      tolerateMemberOutOfScopeErrors: false
```


where: 

`data.sync.yaml`
     Specifies the sync configuration file. 
`data.sync.yaml.url`
     Specifies the URL. 
`data.sync.yaml.bindDN`
     Specifies the `bindDN`. 
`data.sync.yaml.rfc2307`
     Specifies the RFC 2307 schema. Adjust the values as necessary. You can also use a different schema. 
`data.sync.yaml.rfc2307.groupsQuery.baseDN`
     Specifies the `baseDN` for `groupsQuery`. 
`data.sync.yaml.rfc2307.usersQuery.baseDN`
     Specifies the `baseDN` for `usersQuery`. 

  10. Create the config map by running the following command: 

```shell-session
$ oc create -f ldap-sync-config-map.yaml
```


  11. Define a cron job: 

```yaml
kind: CronJob
apiVersion: batch/v1
metadata:
  name: ldap-group-syncer
  namespace: ldap-sync
spec:
  schedule: "*/30 * * * *"
  concurrencyPolicy: Forbid
  jobTemplate:
    spec:
      backoffLimit: 0
      ttlSecondsAfterFinished: 1800
      template:
        spec:
          containers:
            - name: ldap-group-sync
              image: "registry.redhat.io/openshift4/ose-cli:latest"
              command:
                - "/bin/bash"
                - "-c"
                - "oc adm groups sync --sync-config=/etc/config/sync.yaml --confirm"
              volumeMounts:
                - mountPath: "/etc/config"
                  name: "ldap-sync-volume"
                - mountPath: "/etc/secrets"
                  name: "ldap-bind-password"
                - mountPath: "/etc/ldap-ca"
                  name: "ldap-ca"
          volumes:
            - name: "ldap-sync-volume"
              configMap:
                name: "ldap-group-syncer"
            - name: "ldap-bind-password"
              secret:
                secretName: "ldap-secret"
            - name: "ldap-ca"
              configMap:
                name: "ca-config-map"
          restartPolicy: "Never"
          terminationGracePeriodSeconds: 30
          activeDeadlineSeconds: 500
          dnsPolicy: "ClusterFirst"
          serviceAccountName: "ldap-group-syncer"
```


where: 

`spec`
     Specifies the configuration settings for the cron job. See "Creating cron jobs" for more information on cron job settings. 
`spec.schedule`
     Specifies the schedule for the job specified in [cron format](https://en.wikipedia.org/wiki/Cron). This example cron job runs every 30 minutes. Adjust the frequency as necessary, making sure to take into account how long the sync takes to run. 
`spec.jobTemplate.spec.ttlSecondsAfterFinished`
     Specifies how long, in seconds, to keep finished jobs. This should match the period of the job schedule in order to clean old failed jobs and prevent unnecessary alerts. For more information, see [Automatic Cleanup for Finished Jobs (Kubernetes documentation)](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished). 
`spec.jobTemplate.spec.template.spec.containers.command`
     Specifies the LDAP sync command for the cron job to run. Passes in the sync configuration file that was defined in the config map. 
`spec.jobTemplate.spec.template.spec.volumes.secret.secretName`
     Specifies the name of the secret that you created when the LDAP IDP was configured. 
`spec.jobTemplate.spec.template.spec.volumes.configMap.name`
     Specifies the name of the config map that you created when the LDAP IDP was configured. 

  12. Create the cron job by running the following command: 

```shell-session
$ oc create -f ldap-sync-cron-job.yaml
```


**Additional resources**

  * [Configuring an LDAP identity provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/configuring-identity-providers#configuring-ldap-identity-provider "7.3. Configuring an LDAP identity provider")
  * [Creating cron jobs](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-nodes-jobs-creating-cron_nodes-nodes-jobs)
