# 3.2. Persistent kubelet log level configuration

**Procedure**

  * Use the following `MachineConfig` object for persistent kubelet log level configuration: 

```yaml
 apiVersion: machineconfiguration.openshift.io/v1
 kind: MachineConfig
 metadata:
   labels:
     machineconfiguration.openshift.io/role: master
   name: 99-master-kubelet-loglevel
 spec:
   config:
     ignition:
       version: 3.2.0
     systemd:
       units:
         - name: kubelet.service
           enabled: true
           dropins:
             - name: 30-logging.conf
               contents: |
                 [Service]
                 Environment="KUBELET_LOG_LEVEL=2"
```


Generally, it is recommended to apply `0-4` as debug-level logs and `5-8` as trace-level logs.
