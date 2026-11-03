# 12.2. Create service accounts

You can create a service account in a project and grant it permissions by binding it to a role. 

**Procedure**

  1. Optional: To view the service accounts in the current project: 

```shell-session
$ oc get sa
```


**Example output**

```shell-session
NAME       SECRETS   AGE
builder    1         2d
default    1         2d
deployer   1         2d
```


  2. To create a new service account in the current project: 

```shell-session
$ oc create sa <service_account_name>
```


To create a service account in a different project, specify `-n <project_name>`. 

**Example output**

```shell-session
serviceaccount "robot" created
```


Tip

You can alternatively apply the following YAML to create the service account: 

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: <service_account_name>
  namespace: <current_project>
```


  3. Optional: View the secrets for the service account: 

```shell-session
$ oc describe sa robot
```


**Example output**

```shell-session
Name:                robot
Namespace:           project1
Labels:              <none>
Annotations:         openshift.io/internal-registry-pull-secret-ref: robot-dockercfg-qzbhb
Image pull secrets:  robot-dockercfg-qzbhb
Mountable secrets:   robot-dockercfg-qzbhb
Tokens:              <none>
Events:              <none>
```
