# 19.7. Add unauthenticated groups to cluster roles

Grant unauthenticated users access to specific cluster roles to enable features that require cluster access without authentication, such as external webhooks or automated token management. 

You can add unauthenticated users to the following cluster roles: 

  * `system:scope-impersonation`
  * `system:webhook`
  * `system:oauth-token-deleter`
  * `self-access-reviewer`



Important

Always verify compliance with your organization’s security standards when modifying unauthenticated access. 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a YAML file named `add-<cluster_role>-unauth.yaml` and add the following content: 

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
 annotations:
   rbac.authorization.kubernetes.io/autoupdate: "true"
 name: <cluster_role>access-unauthenticated
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: ClusterRole
 name: <cluster_role>
subjects:
 - apiGroup: rbac.authorization.k8s.io
   kind: Group
   name: system:unauthenticated
```


  2. Apply the configuration by running the following command: 

```shell-session
$ oc apply -f add-<cluster_role>.yaml
```
