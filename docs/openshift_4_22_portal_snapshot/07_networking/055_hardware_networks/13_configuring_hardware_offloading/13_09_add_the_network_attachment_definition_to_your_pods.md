# 13.9. Add the network attachment definition to your pods

After you create the machine config pool, the `SriovNetworkPoolConfig` and `SriovNetworkNodePolicy` custom resources, and the network attachment definition, you can apply these configurations to your pods by adding the network attachment definition to your pod specifications. 

**Procedure**

  * In the pod specification, add the `.metadata.annotations.k8s.v1.cni.cncf.io/networks` field and specify the network attachment definition you created for hardware offloading: 

```yaml
....
metadata:
  annotations:
    v1.multus-cni.io/default-network: <namespace>/<net_attach_def_name>
```


    * `<namespace>/<net_attach_def_name>` specifies the namespace and name of the network attachment definition you created for hardware offloading.
