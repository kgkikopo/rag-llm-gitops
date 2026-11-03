# 6.6. Customize the login page

You can customize the login page to display Terms of Service information or apply custom branding for third-party login providers. 

Custom login pages can also be helpful if you use a third-party login provider, such as GitHub or Google, to show users a branded page that they trust and expect before being redirected to the authentication provider. You can also render custom error pages during the authentication process. 

Note

Customizing the error template is limited to identity providers (IDPs) that use redirects, such as request header and OIDC-based IDPs. It does not have an effect on IDPs that use direct password authentication, such as LDAP and htpasswd. 

**Prerequisites**

  * You must have administrator privileges. 



**Procedure**

  1. Run the following commands to create templates you can modify: 

```shell-session
$ oc adm create-login-template > login.html
```


```shell-session
$ oc adm create-provider-selection-template > providers.html
```


```shell-session
$ oc adm create-error-template > errors.html
```


  2. Create the secrets: 

```shell-session
$ oc create secret generic login-template --from-file=login.html -n openshift-config
```


```shell-session
$ oc create secret generic providers-template --from-file=providers.html -n openshift-config
```


```shell-session
$ oc create secret generic error-template --from-file=errors.html -n openshift-config
```


  3. Run: 

```shell-session
$ oc edit oauths cluster
```


  4. Update the specification: 

```yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
# ...
spec:
  templates:
    error:
        name: error-template
    login:
        name: login-template
    providerSelection:
        name: providers-template
```


Run `oc explain oauths.spec.templates` to understand the options.
