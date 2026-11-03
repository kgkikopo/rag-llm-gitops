# 5.8. Creating the machine configuration

Before you create the resource pods, you need to create the `machineconfig.yaml` custom resource (CR) that provides access to the GPU and networking resources without the need for user privileges. 

**Procedure**

  1. Generate a `Machineconfig` CR: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 02-worker-container-runtime
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=utf-8;base64,W2NyaW8ucnVudGltZV0KZGVmYXVsdF91bGltaXRzID0gWwoibWVtbG9jaz0tMTotMSIKXQo=
        mode: 420
        overwrite: true
        path: /etc/crio/crio.conf.d/10-custom
```
