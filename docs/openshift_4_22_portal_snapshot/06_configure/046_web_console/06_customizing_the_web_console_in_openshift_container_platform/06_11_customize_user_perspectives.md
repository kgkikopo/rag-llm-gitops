# 6.11. Customize user perspectives

As a cluster administrator, you can show or hide web console perspectives for all users or for a specific user role, ensuring users see only the perspectives relevant to their role and tasks. For example, you can hide the **Administrator** perspective from users without administrative access. 

You can also customize the perspective visibility for users based on role-based access control (RBAC). For example, if you customize a perspective for monitoring purposes, which requires specific permissions, you can define that the perspective is visible only to users with required permissions. 

Each perspective includes the following mandatory parameters, which you can edit in the YAML view: 

  * `id`: Defines the ID of the perspective to show or hide 
  * `visibility`: Defines the state of the perspective along with access review checks, if needed 
  * `state`: Defines whether the perspective is enabled, disabled, or needs an access review check 



Note

By default, all perspectives are enabled. When you customize the user perspective, your changes are applicable to the entire cluster. 

## 6.11.1. Customize a perspective using YAML view

You can customize a perspective by editing the console resource YAML content. 

**Prerequisites**

  * You must have administrator privileges. 



**Procedure**

  1. In the **Administrator** perspective, navigate to **Administration** **Cluster Settings**. 
  2. Select the **Configuration** tab and click the **Console (operator.openshift.io)** resource. 
  3. Click the **YAML** tab and make your customization: 

     1. To enable or disable a perspective, insert the snippet for **Add user perspectives** and edit the YAML code as needed: 

```yaml
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  customization:
    perspectives:
      - id: admin
        visibility:
          state: Enabled
      - id: dev
        visibility:
          state: Enabled
```


     2. To hide a perspective based on RBAC permissions, insert the snippet for **Hide user perspectives** and edit the YAML code as needed: 

```yaml
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  customization:
    perspectives:
      - id: admin
        requiresAccessReview:
          - group: rbac.authorization.k8s.io
            resource: clusterroles
            verb: list
      - id: dev
        state: Enabled
```


     3. To customize a perspective based on your needs, create your own YAML snippet: 

```yaml
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  customization:
    perspectives:
      - id: admin
        visibility:
          state: AccessReview
          accessReview:
            missing:
              - resource: deployment
                verb: list
            required:
              - resource: namespaces
                verb: list
      - id: dev
        visibility:
          state: Enabled
```


  4. Click **Save**. 



## 6.11.2. Customize a perspective using form view

You can customize a perspective by using the form view of the console resource. 

**Prerequisites**

  * You must have administrator privileges. 



**Procedure**

  1. In the **Administrator** perspective, navigate to **Administration** **Cluster Settings**. 
  2. Select the **Configuration** tab and click the **Console (operator.openshift.io)** resource. 
  3. Click **Actions** **Customize** on the right side of the page. 
  4. In the **General** settings, customize the perspective by selecting one of the following options from the dropdown list: 

     * **Enabled** : Enables the perspective for all users 
     * **Only visible for privileged users** : Enables the perspective for users who can list all namespaces 
     * **Only visible for unprivileged users** : Enables the perspective for users who cannot list all namespaces 
     * **Disabled** : Disables the perspective for all users 

A notification opens to confirm that your changes are saved. 

Note

When you customize the user perspective, your changes are automatically saved and take effect after a browser refresh.
