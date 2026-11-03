# 4.8. Using in-tree modules with the device plugin

You can configure a KMM `Module` custom resource on OpenShift Container Platform to use an in-tree kernel module and run only the device plugin. Omit the `moduleLoader` section and specify only `devicePlugin` in the CR. 

**Example 4.1. Example`Module` CR**

```yaml
apiVersion: kmm.sigs.x-k8s.io/v1beta1
kind: Module
metadata:
  name: my-kmod
spec:
  selector:
    node-role.kubernetes.io/worker: ""
  devicePlugin:
    container:
      image: some.registry/org/my-device-plugin:latest
```
