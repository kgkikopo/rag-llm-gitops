# 11.1. Configure node pools for hosted control planes

In hosted control planes, you can configure node pools by creating a `MachineConfig` object inside of a config map in the management cluster. 

**Procedure**

  1. To create a `MachineConfig` object inside of a config map in the management cluster, enter the following information: 

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: <configmap_name>
  namespace: clusters
data:
  config: |
    apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineConfig
    metadata:
      labels:
        machineconfiguration.openshift.io/role: worker
      name: <machineconfig_name>
    spec:
      config:
        ignition:
          version: 3.2.0
        storage:
          files:
          - contents:
              source: data:...
            mode: 420
            overwrite: true
            path: ${PATH}
```


The `path` field specifies the path on the node where the `MachineConfig` object is stored. 

  2. After you add the object to the config map, you can apply the config map to the node pool as follows: 

```yaml
$ oc edit nodepool <nodepool_name> --namespace <hosted_cluster_namespace>
```


  3. Edit the `NodePool` resource to include the config map: 

```yaml
apiVersion: hypershift.openshift.io/v1alpha1
kind: NodePool
metadata:
# ...
  name: nodepool-1
  namespace: clusters
# ...
spec:
  config:
  - name: <configmap_name>
# ...
```


Replace `<configmap_name>` with the name of your config map.
