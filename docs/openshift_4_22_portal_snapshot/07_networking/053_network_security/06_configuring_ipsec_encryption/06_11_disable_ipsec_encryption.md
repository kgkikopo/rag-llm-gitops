# 6.11. Disable IPsec encryption

To disable IPsec encryption in OpenShift Container Platform, you can patch the cluster `Network` custom resource and set `ipsecConfig` mode to `Disabled`. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You logged in to the cluster with a user with `cluster-admin` privileges. 



**Procedure**

  1. Choose one of the following options to disable IPsec encryption: 

     1. Where the `ipsecConfig.mode` parameter is set to either `External` or `Full` and the `ipsecConfig.full` schema is not added to `networks.operator.openshift.io`, enter the following command: 

```shell-session
$ oc patch networks.operator.openshift.io cluster --type=merge -p \
  '{
  "spec":{
    "defaultNetwork":{
      "ovnKubernetesConfig":{
        "ipsecConfig":{
          "mode":"Disabled"
        }}}}}'
```


     2. Where the `ipsecConfig.mode` parameter is set to `Full` and the `ipsecConfig.full` configuration is added to `networks.operator.openshift.io`, enter the following command: 

```shell-session
$ oc patch networks.operator.openshift.io cluster --type='json' -p \
      '[{"op": "remove", "path": "/spec/defaultNetwork/ovnKubernetesConfig/ipsecConfig/full"},
      {"op": "replace", "path": "/spec/defaultNetwork/ovnKubernetesConfig/ipsecConfig/mode", "value": "Disabled"}]'
```


  2. Optional: You can increase the size of your cluster MTU by `46` bytes because there is no longer any overhead from the IPsec Encapsulating Security Payload (ESP) header in IP packets.
