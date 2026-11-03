# 4.2. Enabling Stream Control Transmission Protocol (SCTP)

As a cluster administrator, you can load and enable the blacklisted SCTP kernel module on worker nodes in your cluster. 

**Prerequisites**

  * Install the OpenShift CLI (`oc`). 
  * Access to the cluster as a user with the `cluster-admin` role. 



**Procedure**

  1. Create a file named `load-sctp-module.yaml` that contains the following YAML definition: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  name: load-sctp-module
  labels:
    machineconfiguration.openshift.io/role: worker
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
        - path: /etc/modprobe.d/sctp-blacklist.conf
          mode: 0644
          overwrite: true
          contents:
            source: data:,
        - path: /etc/modules-load.d/sctp-load.conf
          mode: 0644
          overwrite: true
          contents:
            source: data:,sctp
```


  2. To create the `MachineConfig` object, enter the following command: 

```shell-session
$ oc create -f load-sctp-module.yaml
```


  3. Optional: To watch the status of the nodes while the MachineConfig Operator applies the configuration change, enter the following command. When the status of a node transitions to `Ready`, the configuration update is applied. 

```shell-session
$ oc get nodes
```
