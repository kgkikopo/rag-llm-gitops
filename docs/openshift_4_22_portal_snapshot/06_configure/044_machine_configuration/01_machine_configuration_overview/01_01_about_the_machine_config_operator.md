# 1.1. About the Machine Config Operator

The Machine Config Operator (MCO) manages the lifecycle of your cluster nodes by coordinating operating system updates and configuration changes. You can use the MCO to simplify node upgrades and ensures consistent host environments across your cluster. 

OpenShift Container Platform 4.22 integrates both operating system and cluster management. Because the cluster manages its own updates, including updates to Red Hat Enterprise Linux CoreOS (RHCOS) on cluster nodes, OpenShift Container Platform provides an opinionated lifecycle management experience that simplifies the orchestration of node upgrades. 

OpenShift Container Platform employs three daemon sets and controllers to simplify node management. These daemon sets orchestrate operating system updates and configuration changes to the hosts by using standard Kubernetes-style constructs. They include: 

  * The `machine-config-controller`, which coordinates machine upgrades from the control plane. It monitors all of the cluster nodes and orchestrates their configuration updates. 
  * The `machine-config-daemon` daemon set, which runs on each node in the cluster and updates a machine to configuration as defined by machine config and as instructed by the MachineConfigController. When the node detects a change, it drains off its pods, applies the update, and reboots. These changes come in the form of Ignition configuration files that apply the specified machine configuration and control kubelet configuration. The update itself is delivered in a container. This process is key to the success of managing OpenShift Container Platform and RHCOS updates together. 
  * The `machine-config-server` daemon set, which provides the Ignition config files to control plane nodes as they join the cluster. 



The machine configuration is a subset of the Ignition configuration. The `machine-config-daemon` reads the machine configuration to see if it needs to do an OSTree update or if it must apply a series of systemd kubelet file changes, configuration changes, or other changes to the operating system or OpenShift Container Platform configuration. 

When you perform node management operations, you create or modify a `KubeletConfig` custom resource (CR). 

Important

When changes are made to a machine configuration, the Machine Config Operator (MCO) automatically reboots all corresponding nodes in order for the changes to take effect. 

You can mitigate the disruption caused by some machine config changes by using a node disruption policy. See _Understanding node restart behaviors after machine config changes_. 

Alternatively, you can prevent the nodes from automatically rebooting after machine configuration changes before making the changes. Pause the autoreboot process by setting the `spec.paused` field to `true` in the corresponding machine config pool. When paused, machine configuration changes are not applied until you set the `spec.paused` field to `false` and the nodes have rebooted into the new configuration. 

  * When the MCO detects any of the following changes, it applies the update without draining or rebooting the node: 

    * Changes to the SSH key in the `spec.config.passwd.users.sshAuthorizedKeys` parameter of a machine config. 
    * Changes to the global pull secret or pull secret in the `openshift-config` namespace. 
    * Automatic rotation of the `/etc/kubernetes/kubelet-ca.crt` certificate authority (CA) by the Kubernetes API Server Operator. 

  * When the MCO detects changes to the `/etc/containers/registries.conf` file, such as editing an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object, it drains the corresponding nodes, applies the changes, and uncordons the nodes. The node drain does not happen for the following changes: 

    * The addition of a registry with the `pull-from-mirror = "digest-only"` parameter set for each mirror. 
    * The addition of a mirror with the `pull-from-mirror = "digest-only"` parameter set in a registry. 
    * The addition of items to the `unqualified-search-registries` list. 




There might be situations where the configuration on a node does not fully match what the currently-applied machine config specifies. This state is called _configuration drift_. The Machine Config Daemon (MCD) regularly checks the nodes for configuration drift. If the MCD detects configuration drift, the MCO marks the node `degraded` until an administrator corrects the node configuration. A degraded node is online and operational, but, it cannot be updated.
