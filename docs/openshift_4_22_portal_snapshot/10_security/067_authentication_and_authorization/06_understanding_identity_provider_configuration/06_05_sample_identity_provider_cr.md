# 6.5. Sample identity provider CR

You can use a custom resource (CR) to see the parameters and default values that you use to configure an identity provider. 

The following example uses the htpasswd identity provider. 

**Sample identity provider CR**

```yaml
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: my_identity_provider
    mappingMethod: claim
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpass-secret
```


where: 

`spec.identityProviders.name`
     Specifies the provider name, which is prefixed to provider user names to form an identity name. 
`spec.identityProviders.mappingMethod`
     Specifies how mappings are established between this provider’s identities and `User` objects. 
`spec.identityProviders.htpasswd.fileData.name`
     Specifies an existing secret containing a file generated using [`htpasswd`](http://httpd.apache.org/docs/2.4/programs/htpasswd.html).
