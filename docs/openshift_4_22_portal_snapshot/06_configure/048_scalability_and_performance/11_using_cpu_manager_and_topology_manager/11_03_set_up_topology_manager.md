# 11.3. Set up Topology Manager

To use Topology Manager, you must configure an allocation policy in the `KubeletConfig` custom resource (CR) named `cpumanager-enabled`. This file might exist if you have set up CPU Manager. If the file does not exist, you can create the file. 

**Prerequisites**

  * Configure the CPU Manager policy to be `static`. 



**Procedure**

  1. To activate Topology Manager, configure the Topology Manager allocation policy in the custom resource. 

```shell-session
$ oc edit KubeletConfig cpumanager-enabled
```


```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: cpumanager-enabled
spec:
  machineConfigPoolSelector:
    matchLabels:
      custom-kubelet: cpumanager-enabled
  kubeletConfig:
     cpuManagerPolicy: static
     cpuManagerReconcilePeriod: 5s
     topologyManagerPolicy: single-numa-node
```


     * `cpuManagerPolicy` must be `static` with a lowercase `s`. 
     * `topologyManagerPolicy` specifies your selected Topology Manager allocation policy. In this example, the policy is `single-numa-node`. Acceptable values are: `default`, `best-effort`, `restricted`, `single-numa-node`.
