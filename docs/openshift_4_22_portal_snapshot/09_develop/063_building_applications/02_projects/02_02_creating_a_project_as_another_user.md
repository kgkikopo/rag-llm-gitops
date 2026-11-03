# 2.2. Creating a project as another user

You can use impersonation to create a project on behalf of a different user account. 

## 2.2.1. API impersonation

You can configure API requests in OpenShift Container Platform to act as another user. Impersonation allows you to perform actions on behalf of another account without switching credentials. 

## 2.2.2. Impersonating a user when you create a project

You can impersonate a different user when you create a project request. Because `system:authenticated:oauth` is the only bootstrap group that can create project requests, you must impersonate that group. 

**Procedure**

  * To create a project request on behalf of a different user: 

```shell-session
$ oc new-project <project> --as=<user> \
    --as-group=system:authenticated --as-group=system:authenticated:oauth
```


## 2.2.3. Additional resources

  * [User impersonation (Kubernetes documentation)](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation)
