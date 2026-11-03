# 4.7. Migrating a configured br-ex bridge to NMState

If you used the `configure-ovs.sh` shell script to set a `br-ex` bridge during cluster installation, you can migrate the `br-ex` bridge to NMState as a postinstallation task. NMState provides a declarative and idempotent way to handle configuring the `br-ex` bridge. 

Note

The initial steps in the procedure do not show example configurations. For detailed example configurations that would represent objects to create during cluster installation, see the "Creating a manifest object that includes a customized br-ex bridge" link in the _Additional resources_ section. 

After you migrate your configured `br-ex` bridge to NMState, you cannot reverse the operation. This means that you cannot migrate back to the shell script version of the `br-ex` bridge. 

Important

Misconfiguring any files that form part of the migration operation can cause disruptive changes to your cluster. Reverting these changes might not always be possible. 

**Prerequisites**

  * You used the `configure-ovs.sh` shell script to set a `br-ex` bridge for your cluster. 



**Procedure**

  1. Create an NMState configuration file for your customized `br-ex` bridge network. In a later step, the `MachineConfig` object saves the NMState configuration file in the `/etc/nmstate/openshift` directory path. 
  2. Use the `cat` command to base64-encode the contents of the NMState configuration file: 

```shell-session
$ cat <nmstate_configuration>.yaml | base64
```


Replace `<nmstate_configuration>` with the name of your NMState resource YAML file. 

  3. Create a `MachineConfig` manifest file and define a customized `br-ex` bridge network configuration in the file. Specify the path to the `base64-encoded` NMState configuration file. This embeds the file contents in the `MachineConfig` manifest file. 

Important

To ensure network stability and performance, you must explicitly declare the MTU in the manifest for every interface. Do not rely on automatic MTU configuration. The MTU configured on a bridge port or VLAN-tagged interface must not exceed the maximum frame size supported by the attached physical medium. A mismatch causes packet fragmentation or connectivity loss. 

You can use NMState to apply various network settings across cluster nodes. As an example, the following configuration sets the MTU to `9000` for both a physical device and a bridge interface. You must encode the file in base64 format and then embed the output in a `MachineConfig` manifest file. The `MachineConfig` manifest file writes to `/etc/nmstate/openshift/cluster.yml` or a per-node path under `/etc/nmstate/openshift/`. 

**NMState file before encoding**

```yaml
# ...
interfaces:
# ...
- name: enp2s0
  type: ethernet
  state: up
  mtu: 9000
# ...
- name: br-ex
  type: ovs-interface
  state: up
  copy-mac-from: enp2s0
  mtu: 9000
# ...
```


**MachineConfig embeds the encoded file**

```yaml
# ...
  kind: MachineConfig
  metadata:
# ...
spec:
  config:
# ...
    storage:
      files:
      - contents:
          source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
# ...
        path: /etc/nmstate/openshift/cluster.yml
# ...
```


  4. Apply the updates from the `MachineConfig` object to your cluster by entering the following command: 

```shell-session
$ oc apply -f <machine_config>.yml
```


  5. Create a bare `MachineConfig` object but do not make any configuration changes to the file: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: master
  name: 10-force-reboot-master
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=utf-8;base64,
        mode: 0644
        overwrite: true
        path: /etc/force-reboot
---
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 10-force-reboot-worker
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=utf-8;base64,
        mode: 0644
        overwrite: true
        path: /etc/force-reboot
# ...
```


  6. Start a reboot operation by applying the bare `MachineConfig` object configuration to your cluster by entering the following command: 

```shell-session
$ oc apply -f <bare_machine_config>.yml
```


  7. Delete the bare `MachineConfig` object by entering the following command: 

```shell-session
$ oc delete machineconfig <machine_config_name>
```


**Verification**

  * Use the `nmstatectl` tool to check the configuration for the `br-ex` bridge interface by running the following command. The tool checks a node that runs the `br-ex` bridge interface. The tool does not check the location where you deployed the `MachineConfig` objects. 

```shell-session
$ sudo nmstatectl show br-ex
```


**Additional resources**

  * [Installer-provisioned infrastructure: Creating a manifest object that includes a customized `br-ex` bridge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_bare_metal/installer-provisioned-infrastructure#creating-manifest-file-customized-br-ex-bridge_ipi-install-installation-workflow "3.3.6. Creating a manifest object that includes a customized br-ex bridge")
  * [User-provisioned infrastructure: Creating a manifest object that includes a customized `br-ex` bridge](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_bare_metal/user-provisioned-infrastructure#creating-manifest-file-customized-br-ex-bridge_installing-bare-metal "2.1.3. Creating a manifest object that includes a customized br-ex bridge")
