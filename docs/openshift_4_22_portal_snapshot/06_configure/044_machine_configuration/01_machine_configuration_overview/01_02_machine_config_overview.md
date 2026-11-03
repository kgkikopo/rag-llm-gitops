# 1.2. Machine config overview

You should understand what the Machine Config Operator (MCO) does and how it interacts with other components before making advanced, system-level changes to an OpenShift Container Platform cluster. 

The Machine Config Operator (MCO) manages updates to systemd, CRI-O and Kubelet, the kernel, Network Manager, and other system features. It also offers a `MachineConfig` CRD that can write configuration files onto the host. 

You should know the following details about the MCO, machine configs, and how they are used: 

  * A machine config can make a specific change to a file or service on the operating system of each system representing a pool of OpenShift Container Platform nodes. 
  * MCO applies changes to operating systems in pools of machines. All OpenShift Container Platform clusters start with worker and control plane node pools. By adding more role labels, you can configure custom pools of nodes. For example, you can set up a custom pool of worker nodes that includes particular hardware features needed by an application. However, examples in this section focus on changes to the default pool types. 

Important

A node can have multiple labels applied that indicate its type, such as `master` or `worker`, however it can be a member of only a **single** machine config pool. 

  * Machine configs are processed alphabetically, in lexicographically increasing order, by their name. The render controller uses the first machine config in the list as the base and appends the rest to the base machine config into a rendered machine config, which is then applied to the appropriate nodes. 
  * When you create a machine config for the worker nodes, the changes are also applied to the nodes in all custom pools. 

However, as of OpenShift Container Platform 4.15, any machine configs that target custom pools always override worker machine configs if the worker machine configs contain definitions for the same fields. 

  * After a machine config change, the MCO updates the affected nodes alphabetically by zone, based on the `topology.kubernetes.io/zone` label. If a zone has more than one node, the oldest nodes are updated first. For nodes that do not use zones, such as in bare metal deployments, the nodes are upgraded by age, with the oldest nodes updated first. The MCO updates the number of nodes as specified by the `maxUnavailable` field on the machine configuration pool at a time. 
  * Some machine configuration must be in place before OpenShift Container Platform is installed to disk. In most cases, this can be accomplished by creating a machine config that is injected directly into the OpenShift Container Platform installer process, instead of running as a postinstallation machine config. In other cases, you might need to do bare metal installation where you pass kernel arguments at OpenShift Container Platform installer startup, to do such things as setting per-node individual IP addresses or advanced disk partitioning. 
  * MCO manages items that are set in machine configs. Manual changes you do to your systems will not be overwritten by MCO, unless MCO is explicitly told to manage a conflicting file. In other words, MCO only makes specific updates you request, it does not claim control over the whole node. 
  * Manual changes to nodes are strongly discouraged. If you need to decommission a node and start a new one, those direct changes would be lost. 
  * MCO is only supported for writing to files in `/etc` and `/var` directories, although there are symbolic links to some directories that can be writeable by being symbolically linked to one of those areas. The `/opt` and `/usr/local` directories are examples. 
  * Ignition is the configuration format used in MachineConfigs. For details, see "Configuration Specification v3.5.0 (Ignition documentation)". 
  * Although Ignition config settings can be delivered directly at OpenShift Container Platform installation time, and are formatted in the same way that MCO delivers Ignition configs, MCO has no way of seeing what those original Ignition configs are. Therefore, you should wrap Ignition config settings into a machine config before deploying them. 
  * When a file managed by MCO changes outside of MCO, the Machine Config Daemon (MCD) sets the node as `degraded`. It will not overwrite the offending file, however, and should continue to operate in a `degraded` state. 
  * A key reason for using a machine config is that it will be applied when you spin up new nodes for a pool in your OpenShift Container Platform cluster. The `machine-api-operator` provisions a new machine and MCO configures it. 



MCO uses Ignition as the configuration format. OpenShift Container Platform 4.6 moved from Ignition config specification version 2 to version 3. For more information, see the "Configuration Specification v3.5.0 (Ignition documentation)" in the _Additional resources_ section. 

## 1.2.1. What can you change with machine configs?

The kinds of components that MCO can change include: 

  * **config** : Create Ignition config objects to do things like modify files, systemd services, and other features on OpenShift Container Platform machines, including: 

    * **Configuration files** : Create or overwrite files in the `/var` or `/etc` directory. 
    * **systemd units** : Create and set the status of a systemd service or add to an existing systemd service by dropping in additional settings. 
    * **users and groups** : Change SSH keys in the passwd section postinstallation. 

Important

      * Changing SSH keys by using a machine config is supported only for the `core` user. 
      * Adding new users by using a machine config is not supported. 

  * **kernelArguments** : Add arguments to the kernel command line when OpenShift Container Platform nodes boot. 
  * **kernelType** : Optionally identify a non-standard kernel to use instead of the standard kernel. Use `realtime` to use the RT kernel (for RAN). This is only supported on select platforms. Use the `64k-pages` parameter to enable the 64k page size kernel. This setting is exclusive to machines with 64-bit ARM architectures. 
  * **fips** : Enable FIPS mode. FIPS should be set at installation-time setting and not a postinstallation procedure. For more information, see "Using system-wide cryptographic policies". 

Important

To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening). 

When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures. 

  * **extensions** : Extend RHCOS features by adding selected pre-packaged software. For this feature, available extensions include usbguard and kernel modules. For more information, see "Protecting systems against intrusive USB devices" in the _Additional resources_ section. 
  * **Custom resources (for`ContainerRuntime` and `Kubelet`)**: Outside of machine configs, MCO manages two special custom resources for modifying CRI-O container runtime settings (`ContainerRuntime` CR) and the Kubelet service (`Kubelet` CR). 



The MCO is not the only Operator that can change operating system components on OpenShift Container Platform nodes. Other Operators can modify operating system-level features as well. One example is the Node Tuning Operator, which allows you to do node-level tuning through Tuned daemon profiles. 

Tasks for the MCO configuration that can be done after installation are included in the following procedures. See descriptions of RHCOS bare metal installation for system configuration tasks that must be done during or before OpenShift Container Platform installation. By default, many of the changes you make with the MCO require a reboot. 

  * When the MCO detects any of the following changes, it applies the update without draining or rebooting the node: 

    * Changes to the SSH key in the `spec.config.passwd.users.sshAuthorizedKeys` parameter of a machine config. 
    * Changes to the global pull secret or pull secret in the `openshift-config` namespace. 
    * Automatic rotation of the `/etc/kubernetes/kubelet-ca.crt` certificate authority (CA) by the Kubernetes API Server Operator. 

  * When the MCO detects changes to the `/etc/containers/registries.conf` file, such as editing an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object, it drains the corresponding nodes, applies the changes, and uncordons the nodes. The node drain does not happen for the following changes: 

    * The addition of a registry with the `pull-from-mirror = "digest-only"` parameter set for each mirror. 
    * The addition of a mirror with the `pull-from-mirror = "digest-only"` parameter set in a registry. 
    * The addition of items to the `unqualified-search-registries` list. 




In other cases, you can mitigate the disruption to your workload when the MCO makes changes by using _node disruption policies_. For information, see _Understanding node restart behaviors after machine config changes_. 

There might be situations where the configuration on a node does not fully match what the currently-applied machine config specifies. This state is called _configuration drift_. The Machine Config Daemon (MCD) regularly checks the nodes for configuration drift. If the MCD detects configuration drift, the MCO marks the node `degraded` until an administrator corrects the node configuration. A degraded node is online and operational, but, it cannot be updated. For more information on configuration drift, see _Understanding configuration drift detection_. 

## 1.2.2. Node configuration management with machine config pools

When making changes to nodes, you can modify groups of nodes by applying the changes to all of the nodes in the same machine config pool (MCP). 

Machines that run control plane components or user workloads are divided into groups based on the types of resources they handle. These groups of machines are called machine config pools (MCP). Each MCP manages a set of nodes and its corresponding machine configs. The role of the node determines which MCP it belongs to; the MCP governs nodes based on its assigned node role label. Nodes in an MCP have the same configuration; this means nodes can be scaled up and torn down in response to increased or decreased workloads. 

By default, there are two MCPs created by the cluster when it is installed: `master` and `worker`. Each default MCP has a defined configuration applied by the Machine Config Operator (MCO), which is responsible for managing MCPs and facilitating MCP updates. 

For worker nodes, you can create additional MCPs, or custom pools, to manage nodes with custom use cases that extend outside of the default node types. Custom MCPs for the control plane nodes are not supported. 

Custom pools are pools that inherit their configurations from the worker pool. They use any machine config targeted for the worker pool, but add the ability to deploy changes only targeted at the custom pool. Since a custom pool inherits its configuration from the worker pool, any change to the worker pool is applied to the custom pool as well. Custom pools that do not inherit their configurations from the worker pool are not supported by the MCO. 

Note

A node can only be included in one MCP. If a node has multiple labels that correspond to several MCPs, like `worker,infra`, it is managed by the infra custom pool, not the worker pool. Custom pools take priority on selecting nodes to manage based on node labels; nodes that do not belong to a custom pool are managed by the worker pool. 

It is recommended to have a custom pool for every node role you want to manage in your cluster. For example, if you create infra nodes to handle infra workloads, it is recommended to create a custom infra MCP to group those nodes together. If you apply an `infra` role label to a worker node so it has the `worker,infra` dual label, but do not have a custom infra MCP, the MCO considers it a worker node. If you remove the `worker` label from a node and apply the `infra` label without grouping it in a custom pool, the node is not recognized by the MCO and is unmanaged by the cluster. 

Important

Any node labeled with the `infra` role that is only running infra workloads is not counted toward the total number of subscriptions. The MCP managing an infra node is mutually exclusive from how the cluster determines subscription charges; tagging a node with the appropriate `infra` role and using taints to prevent user workloads from being scheduled on that node are the only requirements for avoiding subscription charges for infra workloads. 

The MCO applies updates for pools independently; for example, if there is an update that affects all pools, nodes from each pool update in parallel with each other. If you add a custom pool, nodes from that pool also attempt to update concurrently with the master and worker nodes. 

There might be situations where the configuration on a node does not fully match what the currently-applied machine config specifies. This state is called _configuration drift_. The Machine Config Daemon (MCD) regularly checks the nodes for configuration drift. If the MCD detects configuration drift, the MCO marks the node `degraded` until an administrator corrects the node configuration. A degraded node is online and operational, but, it cannot be updated.
