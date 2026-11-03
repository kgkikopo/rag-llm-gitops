# 6.10. Disable IPsec encryption for an external IPsec endpoint

To stop encrypting traffic to an external host in OpenShift Container Platform, you can remove the IPsec tunnel configuration from your cluster nodes. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * You are logged in to the cluster as a user with `cluster-admin` privileges. 
  * You enabled IPsec in either `Full` or `External` mode on your cluster. 



**Procedure**

  1. Create a file named `remove-ipsec-tunnel.yaml` with the following YAML: 

```yaml
kind: NodeNetworkConfigurationPolicy
apiVersion: nmstate.io/v1
metadata:
  name: <name>
spec:
  nodeSelector:
    kubernetes.io/hostname: <node_name>
  desiredState:
    interfaces:
    - name: <tunnel_name>
      type: ipsec
      state: absent
```


where: 

`name`
     Specifies a name for the node network configuration policy. 
`node_name`
     Specifies the name of the node where the IPsec tunnel that you want to remove exists. 
`tunnel_name`
     Specifies the interface name for the existing IPsec tunnel. 

  2. To remove the IPsec tunnel, enter the following command: 

```shell-session
$ oc apply -f remove-ipsec-tunnel.yaml
```
