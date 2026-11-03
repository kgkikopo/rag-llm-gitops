# 13.4. Set the SR-IOV Network Operator into systemd mode

To support hardware offloading, you must first set the SR-IOV Network Operator into `systemd` mode. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You have access to the cluster as a user that has the `cluster-admin` role. 



**Procedure**

  1. Create a `SriovOperatorConfig` custom resource (CR) to deploy all the SR-IOV Operator components: 

     1. Create a file named `sriovOperatorConfig.yaml` that contains the following YAML: 

```yaml
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
spec:
  enableInjector: true
  enableOperatorWebhook: true
  configurationMode: "systemd"
  logLevel: 2
```


        * The only valid name for the `SriovOperatorConfig` resource is `default` and it must be in the namespace where the Operator is deployed. 
        * Setting the SR-IOV Network Operator into `systemd` mode is only relevant for Open vSwitch hardware offloading. 

     2. Create the resource by running the following command: 

```shell-session
$ oc apply -f sriovOperatorConfig.yaml
```
