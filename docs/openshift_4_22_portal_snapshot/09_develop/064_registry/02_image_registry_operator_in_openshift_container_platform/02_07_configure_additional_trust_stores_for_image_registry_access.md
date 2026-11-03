# 2.7. Configure additional trust stores for image registry access

You can add references to a config map that has additional certificate authorities (CAs) to be trusted during image registry access to the `image.config.openshift.io/cluster` custom resource (CR). 

**Prerequisites**

  * The certificate authorities (CAs) must be PEM-encoded. 



**Procedure**

  1. Create a config map in the `openshift-config` namespace, then and use the config map name in the `AdditionalTrustedCA` parameter of the `image.config.openshift.io` CR. This adds CAs that should be trusted when the cluster contacts external image registries. 

**Image registry CA config map example**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-registry-ca
data:
  registry.example.com: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
  registry-with-port.example.com..5000: |
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
```


where: 

`data:registry.example.com:`
     An example hostname of a registry for which this CA is to be trusted. 
`data:registry-with-port.example.com..5000:`
    

An example hostname of a registry with the port for which this CA is to be trusted. If the registry has a port, such as `registry-with-port.example.com:5000`, `:` must be replaced with `..`. 

The PEM certificate content is the value for each additional registry CA to trust. 

  2. Optional. Configure an additional CA by running the following command: 

```shell-session
$ oc create configmap registry-config --from-file=<external_registry_address>=ca.crt -n openshift-config
```


```shell-session
$ oc edit image.config.openshift.io cluster
```


```yaml
spec:
  additionalTrustedCA:
    name: registry-config
```
