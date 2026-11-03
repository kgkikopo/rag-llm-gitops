# 4.4. Create the managed bare-metal host secrets

Add the required `Secret` custom resources (CRs) for the managed bare-metal host to the hub cluster. You need a secret for the GitOps Zero Touch Provisioning (ZTP) pipeline to access the Baseboard Management Controller (BMC) and a pull secret for the Assisted Installer service. 

Note

The secrets are referenced from the `ClusterInstance` CR by name. The namespace must match the `ClusterInstance` namespace. 

**Procedure**

  1. Create a YAML secret file containing credentials for the host Baseboard Management Controller (BMC) and a pull secret required for installing OpenShift and all add-on cluster Operators: 

     1. Save the following YAML as the file `example-sno-secret.yaml`: 

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: example-sno-bmc-secret
  namespace: example-sno
data:
  password: <base64_password>
  username: <base64_username>
type: Opaque
---
apiVersion: v1
kind: Secret
metadata:
  name: pull-secret
  namespace: example-sno
data:
  .dockerconfigjson: <pull_secret>
type: kubernetes.io/dockerconfigjson
```


where: 

`namespace`
     Must match the namespace configured in the related `ClusterInstance` CR. 
`password`, `username`
     Base64-encoded values for `password` and `username`. 
`.dockerconfigjson`
     Base64-encoded pull secret. 

  2. Add the relative path to `example-sno-secret.yaml` to the `kustomization.yaml` file that you use to install the cluster.
