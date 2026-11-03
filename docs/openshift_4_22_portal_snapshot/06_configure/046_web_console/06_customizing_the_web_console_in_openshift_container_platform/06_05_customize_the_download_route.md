# 6.5. Customize the download route

You can customize the download route by setting the custom hostname and TLS certificate in the `spec.componentRoutes` field of the cluster `Ingress` configuration. 

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
    - name: downloads
      namespace: openshift-console
      hostname: <custom_hostname>
      servingCertKeyPairSecret:
        name: <secret_name>
```


The `hostname` field specifies the custom hostname. The `servingCertKeyPairSecret.name` field references a secret in the `openshift-config` namespace that contains a TLS certificate (`tls.crt`) and key (`tls.key`). This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches. 

  3. Save the file to apply the changes. 

Note

Add a DNS record for the custom downloads route that points to the application ingress load balancer.
