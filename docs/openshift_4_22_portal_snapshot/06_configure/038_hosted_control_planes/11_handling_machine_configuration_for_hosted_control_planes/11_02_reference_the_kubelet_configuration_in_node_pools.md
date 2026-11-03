# 11.2. Reference the kubelet configuration in node pools

To reference your kubelet configuration in node pools, you add the kubelet configuration in a config map and then apply the config map in the `NodePool` resource. 

**Procedure**

  1. Add the kubelet configuration inside of a config map in the management cluster by entering the following information: 

**Example`ConfigMap` object with the kubelet configuration**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: <configmap_name>
  namespace: clusters
data:
  config: |
    apiVersion: machineconfiguration.openshift.io/v1
    kind: KubeletConfig
    metadata:
      name: <kubeletconfig_name>
    spec:
      kubeletConfig:
        registerWithTaints:
        - key: "example.sh/unregistered"
          value: "true"
          effect: "NoExecute"
```


     * `<configmap_name>` specifies the name of your config map. 
     * `<kubeletconfig_name>` specifies the name of the `KubeletConfig` resource. 

  2. Apply the config map to the node pool by entering the following command: 

```yaml
$ oc edit nodepool <nodepool_name> --namespace clusters
```


Replace `<nodepool_name>` with the name of your node pool. 

**Example`NodePool` resource configuration**

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
  - name: example-configmap-1
# ...
```
