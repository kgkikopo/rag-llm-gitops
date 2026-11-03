# Chapter 3. Using node disruption policies to minimize disruption from machine config changes

You can create a _node disruption policy_ to define the configuration changes that cause a disruption to your cluster, and which changes do not. 

Note

Node disruption policies are not supported for on-cluster custom layered images. 

By default, when you make certain changes to the Ignition config objects fields by using a `MachineConfig` object, the Machine Config Operator (MCO) drains and reboots the nodes associated with that machine config. 

By using a node disruption policy, you can define the configuration changes that require actions such as node reboots, node drains, or service restarts, and which changes do not. This reduces node downtime when making small machine configuration changes in your cluster. To configure the policy, you modify the `MachineConfiguration` object, which is in the `openshift-machine-config-operator` namespace. See the example node disruption policies in the `MachineConfiguration` objects in "Example node disruption policies". 

Note

There are machine configuration changes that always require a reboot, regardless of any node disruption policies. For more information, see _About the Machine Config Operator_. 

After you create the node disruption policy, the MCO validates the policy to search for potential issues in the file, such as problems with formatting. The MCO then merges the policy with the cluster defaults and populates the `status.nodeDisruptionPolicyStatus` fields in the machine config with the actions to be performed upon future changes to the machine config. The configurations in your policy always overwrite the cluster defaults. 

Important

The MCO does not validate whether a change can be successfully applied by your node disruption policy. Therefore, you are responsible to ensure the accuracy of your node disruption policies. 

For example, you can configure a node disruption policy so that sudo configurations do not require a node drain and reboot. Or, you can configure your cluster so that updates to `sshd` are applied with only a reload of that one service. 

You can control the behavior of the MCO when making the changes to the following Ignition configuration objects: 

  * **configuration files** : You add to or update the files in the `/var` or `/etc` directory. You can configure a policy for a specific file anywhere in the directory or for a path to a specific directory. For a path, a change or addition to any file in that directory triggers the policy. 

Note

If a file is included in more than one policy, only the policy with the best match to that file is applied. 

For example, if you have a policy for the `/etc/` directory and a policy for the `/etc/pki/` directory, a change to the `/etc/pki/tls/certs/ca-bundle.crt` file would apply the `etc/pki` policy. 

  * **systemd units** : You create and set the status of a systemd service or modify a systemd service. 
  * **users and groups** : You change SSH keys in the `passwd` section postinstallation. 
  * **ICSP** , **ITMS** , **IDMS** objects: You can remove mirroring rules from an `ImageContentSourcePolicy` (ICSP), `ImageTagMirrorSet` (ITMS), and `ImageDigestMirrorSet` (IDMS) object. 



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

- [3.1. Example node disruption policies](03_01_example_node_disruption_policies.md)
- [3.2. Configure node restart behaviors upon machine config changes](03_02_configure_node_restart_behaviors_upon_machine_config_changes.md)
