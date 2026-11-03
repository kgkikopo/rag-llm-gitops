# 3.2. Configure node restart behaviors upon machine config changes

You can create a node disruption policy to define the machine configuration changes that cause a disruption to your cluster, and which changes do not. 

You can control how your nodes respond to changes in the files in the `/var` or `/etc` directory, the systemd units, the SSH keys, and the `registries.conf` file. 

When you make any of these changes, the node disruption policy determines which of the following actions are required when the MCO implements the changes: 

  * **Reboot** : The MCO drains and reboots the nodes. This is the default behavior. 
  * **None** : The MCO does not drain or reboot the nodes. The MCO applies the changes with no further action. 
  * **Drain** : The MCO cordons and drains the nodes of their workloads. The workloads restart with the new configurations. 
  * **Reload** : For services, the MCO reloads the specified services without restarting the service. 
  * **Restart** : For services, the MCO fully restarts the specified services. 
  * **DaemonReload** : The MCO reloads the systemd manager configuration. 
  * **Special** : This is an internal MCO-only action and cannot be set by the user. 



Note

  * The `Reboot` and `None` actions cannot be used with any other actions, as the `Reboot` and `None` actions override the others. 
  * Actions are applied in the order that they are set in the node disruption policy list. 
  * If you make other machine config changes that do require a reboot or other disruption to the nodes, that reboot supercedes the node disruption policy actions. 



**Procedure**

  1. Edit the `machineconfigurations.operator.openshift.io` object to define the node disruption policy: 

```shell-session
$ oc edit MachineConfiguration cluster -n openshift-machine-config-operator
```


  2. Add a node disruption policy similar to the following: 

```yaml
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  nodeDisruptionPolicy:
    files:
    - actions:
      - restart:
          serviceName: chronyd.service
        type: Restart
      path: /etc/chrony.conf
    sshkey:
      actions:
      - type: Drain
      - reload:
          serviceName: crio.service
        type: Reload
      - type: DaemonReload
      - restart:
          serviceName: crio.service
        type: Restart
    units:
    - actions:
      - type: Drain
      - reload:
          serviceName: crio.service
        type: Reload
      - type: DaemonReload
      - restart:
          serviceName: crio.service
        type: Restart
      name: test.service
```


where: 

`spec.nodeDisruptionPolicy`
     Specifies the node disruption policy. 
`spec.nodeDisruptionPolicy.files`
     Specifies a list of machine config file definitions and actions to take to changes on those paths. This list supports a maximum of 50 entries. 
`spec.nodeDisruptionPolicy.files.actions`
    

Specifies the series of actions to be executed upon changes to the specified files. Actions are applied in the order that they are set in this list. This list supports a maximum of 10 entries. Specify the following parameters: 

`restart`. Specifies that the listed service is to be reloaded upon changes to the specified files. `restart.serviceName`. Specifies the full name of the service to be acted upon. 

`spec.nodeDisruptionPolicy.files.path`
     Specifies the location of a file that is managed by a machine config. The actions in the policy apply when changes are made to the file in `path`. 
`spec.nodeDisruptionPolicy.sshkey`
     Specifies a list of service names and actions to take upon changes to the SSH keys in the cluster. 
`spec.nodeDisruptionPolicy.units`
     Specifies a list of systemd unit names and actions to take upon changes to those units. 




**Verification**

  * View the `MachineConfiguration` object file that you created: 

```plaintext
$ oc get MachineConfiguration/cluster -o yaml
```


**Example output**

```yaml
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: cluster
# ...
status:
  nodeDisruptionPolicyStatus:
    clusterPolicies:
      files:
# ...
      - actions:
        - restart:
            serviceName: chronyd.service
          type: Restart
        path: /etc/chrony.conf
      sshkey:
        actions:
        - type: Drain
        - reload:
            serviceName: crio.service
          type: Reload
        - type: DaemonReload
        - restart:
            serviceName: crio.service
          type: Restart
      units:
      - actions:
        - type: Drain
        - reload:
            serviceName: crio.service
          type: Reload
        - type: DaemonReload
        - restart:
            serviceName: crio.service
          type: Restart
        name: test.se
# ...
```


The `nodeDisruptionPolicyStatus` parameter specifies the current cluster-validated policies.
