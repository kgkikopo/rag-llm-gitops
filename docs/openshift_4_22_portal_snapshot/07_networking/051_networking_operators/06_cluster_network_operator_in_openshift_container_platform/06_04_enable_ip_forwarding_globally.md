# 6.4. Enable IP forwarding globally

From OpenShift Container Platform 4.14 onward, OVN-Kubernetes disables global IP forwarding by default. By setting the Cluster Network Operator `gatewayConfig.ipForwarding` spec to `Global`, you can enable cluster-wide forwarding. 

**Procedure**

  1. Backup the existing network configuration by running the following command: 

```shell-session
$ oc get network.operator cluster -o yaml > network-config-backup.yaml
```


  2. Run the following command to modify the existing network configuration: 

```shell-session
$ oc edit network.operator cluster
```


     1. Add or update the following block under `spec` as illustrated in the following example: 

```yaml
spec:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  serviceNetwork:
  - 172.30.0.0/16
  networkType: OVNKubernetes
  clusterNetworkMTU: 8900
  defaultNetwork:
    ovnKubernetesConfig:
      gatewayConfig:
        ipForwarding: Global
```


     2. Save and close the file. 

  3. After applying the changes, the OpenShift Cluster Network Operator (CNO) applies the update across the cluster. You can monitor the progress by using the following command: 

```shell-session
$ oc get clusteroperators network
```


The status should eventually report as `Available`, `Progressing=False`, and `Degraded=False`. 

  4. Alternatively, you can enable IP forwarding globally by running the following command: 

```shell-session
$ oc patch network.operator cluster -p '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig":{"ipForwarding": "Global"}}}}}' --type=merge
```


Note

The other valid option for this parameter is `Restricted` in case you want to revert this change. `Restricted` is the default and with that setting global IP address forwarding is disabled.
