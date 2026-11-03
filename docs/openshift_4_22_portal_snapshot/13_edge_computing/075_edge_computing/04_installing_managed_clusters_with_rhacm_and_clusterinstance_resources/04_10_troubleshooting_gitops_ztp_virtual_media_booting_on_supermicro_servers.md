# 4.10. Troubleshooting GitOps ZTP virtual media booting on SuperMicro servers

SuperMicro X11 servers do not support virtual media installations when the image is served using the `https` protocol. 

As a result, single-node OpenShift deployments for this environment fail to boot on the target node. To avoid this issue, log in to the hub cluster and disable Transport Layer Security (TLS) in the `Provisioning` resource. This ensures the image is not served with TLS even though the image address uses the `https` scheme. 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`). 
  * You have logged in to the hub cluster as a user with `cluster-admin` privileges. 



**Procedure**

  1. Disable TLS in the `Provisioning` resource by running the following command: 

```shell-session
$ oc patch provisioning provisioning-configuration --type merge -p '{"spec":{"disableVirtualMediaTLS": true}}'
```


  2. Continue the steps to deploy your single-node OpenShift cluster.
