# 3.6. Customize the internal OAuth server URL

Customize the internal OAuth server URL to use a custom hostname and TLS certificate by configuring the cluster Ingress component routes. 

Warning

If you update the internal OAuth server URL, you might break trust from components in the cluster that need to communicate with the OpenShift Container Platform OAuth server to retrieve OAuth access tokens. Components that need to trust the OAuth server will need to include the proper CA bundle when calling OAuth endpoints. For example: 

```shell-session
$ oc login -u <username> -p <password> --certificate-authority=<path_to_ca.crt>
```


\+ For self-signed certificates, the `ca.crt` file must contain the custom CA certificate, otherwise the login will not succeed. 

The Cluster Authentication Operator publishes the OAuth server’s serving certificate in the `oauth-serving-cert` config map in the `openshift-config-managed` namespace. You can find the certificate in the `data.ca-bundle.crt` key of the config map. 

**Prerequisites**

  * You have logged in to the cluster as a user with administrative privileges. 
  * You have created a secret in the `openshift-config` namespace containing the TLS certificate and key. This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches. 

Tip

You can create a TLS secret by using the `oc create secret tls` command. 




**Procedure**

  1. Edit the cluster `Ingress` configuration: 

```shell-session
$ oc edit ingress.config.openshift.io cluster
```


  2. Set the custom hostname and optionally the serving certificate and key: 

```yaml
apiVersion: config.openshift.io/v1
kind: Ingress
metadata:
  name: cluster
spec:
  componentRoutes:
    - name: oauth-openshift
      namespace: openshift-authentication
      hostname: <custom_hostname>
      servingCertKeyPairSecret:
        name: <secret_name>
```


where: 

`spec.componentRoutes.hostname`
     Specifies the custom hostname for the OAuth server. 
`spec.componentRoutes.servingCertKeyPairSecret.name`
     Specifies the name of a secret in the `openshift-config` namespace that contains a TLS certificate (`tls.crt`) and key (`tls.key`). This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches. 

  3. Save the file to apply the changes.
