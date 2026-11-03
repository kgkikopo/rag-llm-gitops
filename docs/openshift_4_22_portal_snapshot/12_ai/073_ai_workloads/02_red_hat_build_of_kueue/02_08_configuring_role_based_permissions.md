# 2.8. Configuring role-based permissions

You can configure role-based access control (RBAC) for your Red Hat build of Kueue deployment to control which users can create specific Red Hat build of Kueue objects. 

## 2.8.1. Red Hat build of Kueue cluster roles

The Red Hat build of Kueue Operator deploys the `kueue-batch-admin-role` and `kueue-batch-user-role` cluster roles by default. Bind these cluster roles to your own users and groups to grant Red Hat build of Kueue permissions. 

kueue-batch-admin-role
     This cluster role includes the permissions to manage cluster queues, local queues, workloads, and resource flavors. 
kueue-batch-user-role
     This cluster role includes the permissions to manage jobs and to view local queues and workloads. 

## 2.8.2. Configuring permissions for batch administrators

You can configure permissions for batch administrators by binding the `kueue-batch-admin-role` cluster role to a user or group of users. 

**Prerequisites**

  * The Red Hat build of Kueue Operator is installed on your cluster. 
  * You have cluster administrator permissions. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a `ClusterRoleBinding` object as a YAML file: 

**Example`ClusterRoleBinding` object**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kueue-admins
subjects:
- kind: User
  name: admin@example.com
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: kueue-batch-admin-role
  apiGroup: rbac.authorization.k8s.io
```


where: 

`metadata.name`
     Specifies the name of the `ClusterRoleBinding` object. 
`subjects`
     Specifies the user or group of users you want to provide user permissions for. 
`roleRef`
     Specifies the `kueue-batch-admin-role` cluster role. 

  2. Apply the `ClusterRoleBinding` object: 

```shell-session
$ oc apply -f <filename>.yaml
```


**Verification**

  * You can verify that the `ClusterRoleBinding` object was applied correctly by running the following command and verifying that the output contains the correct information for the `kueue-batch-admin-role` cluster role: 

```yaml
$ oc describe clusterrolebinding.rbac
```


**Example output**

```shell-session
...
Name:         kueue-batch-admin-role
Labels:       app.kubernetes.io/name=kueue
Annotations:  <none>
Role:
  Kind:  ClusterRole
  Name:  kueue-batch-admin-role
Subjects:
  Kind            Name                      Namespace
  ----            ----                      ---------
  User            admin@example.com         admin-namespace
...
```


## 2.8.3. Configuring permissions for users

You can configure permissions for Red Hat build of Kueue users by binding the `kueue-batch-user-role` cluster role to a user or group of users. 

**Prerequisites**

  * The Red Hat build of Kueue Operator is installed on your cluster. 
  * You have cluster administrator permissions. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Create a `RoleBinding` object as a YAML file: 

**Example`ClusterRoleBinding` object**

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: kueue-users
  namespace: user-namespace
subjects:
- kind: Group
  name: team-a@example.com
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: kueue-batch-user-role
  apiGroup: rbac.authorization.k8s.io
```


where: 

`metadata.name`
     Specifies the name of the `RoleBinding` object. 
`metadata.namespace`
     Specifies the namespace the `RoleBinding` object applies to. 
`subjects`
     Specifies the user or group of users you want to provide user permissions for. 
`roleRef`
     Specifies the `kueue-batch-user-role` cluster role. 

  2. Apply the `RoleBinding` object: 

```shell-session
$ oc apply -f <filename>.yaml
```


**Verification**

  * You can verify that the `RoleBinding` object was applied correctly by running the following command and verifying that the output contains the correct information for the `kueue-batch-user-role` cluster role: 

```yaml
$ oc describe rolebinding.rbac
```


**Example output**

```shell-session
...
Name:         kueue-users
Labels:       app.kubernetes.io/name=kueue
Annotations:  <none>
Role:
  Kind:  ClusterRole
  Name:  kueue-batch-user-role
Subjects:
  Kind            Name                      Namespace
  ----            ----                      ---------
  Group           team-a@example.com        user-namespace
...
```


## 2.8.4. Additional resources

  * [Using RBAC to define and apply permissions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#using-rbac)
  * [Glossary of common terms for OpenShift Container Platform authentication and authorization](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#openshift-auth-common-terms_overview-of-authentication-authorization)
