# 19.2. Impersonate the system:admin user

You can use the OpenShift web console to impersonate a user and select multiple group memberships at the same time to reproduce that user’s effective permissions. 

**Procedure**

  * To grant a user permission to impersonate `system:admin`, run the following command: 

```shell-session
$ oc create clusterrolebinding <any_valid_name> --clusterrole=sudoer --user=<username>
```


Tip

You can alternatively apply the following YAML to grant permission to impersonate `system:admin`: 

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: <any_valid_name>
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: sudoer
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: User
  name: <username>
```
