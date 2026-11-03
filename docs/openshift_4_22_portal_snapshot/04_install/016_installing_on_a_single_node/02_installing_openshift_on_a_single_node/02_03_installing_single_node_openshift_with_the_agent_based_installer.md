# 2.3. Installing single-node OpenShift with the Agent-based Installer

You can use the Agent-based Installer to deploy single-node OpenShift on bare-metal servers running ARM (`aarch64`) architecture. The Agent-based Installer generates a self-contained bootable ISO image by using the OpenShift Container Platform installer for offline and automated deployments. 

The following procedure describes how to create the required configuration files, generate the agent ISO image, and boot the target ARM server to install single-node OpenShift. 

**Additional resources**

  * [Preparing to install with the Agent-based Installer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/#preparing-to-install-with-agent-based-installer)



## 2.3.1. Installing single-node OpenShift with the Agent-based Installer on ARM architecture

You can use the Agent-based Installer to install single-node OpenShift on an `aarch64` (ARM) server. The Agent-based Installer generates a bootable ISO image that you use to boot the target machine and deploy the cluster. 

**Prerequisites**

  * You downloaded the `openshift-install` binary for your installation host architecture from the [Red Hat Hybrid Cloud Console](https://console.redhat.com). When you select the architecture on the console, ensure that it matches your installation host and that you select `ARM64` (`aarch64`) as the target cluster architecture. 
  * You have a valid pull secret from the [Red Hat Hybrid Cloud Console](https://console.redhat.com). 
  * You have an SSH public key on the administration host. 
  * You configured DNS records for `api.<cluster_name>.<base_domain>` and `*.apps.<cluster_name>.<base_domain>` to point to the node IP address. 



Note

See "Requirements for installing OpenShift on a single node" for networking requirements, including DNS records. 

**Procedure**

  1. Create a directory to store the installation configuration by running the following command: 

```shell-session
$ mkdir ~/<install_directory>
```


  2. Create the `install-config.yaml` file in the installation directory as in the following example: 

```yaml
apiVersion: v1
baseDomain: <domain>
compute:
- architecture: arm64
  hyperthreading: Enabled
  name: worker
  replicas: 0
controlPlane:
  architecture: arm64
  hyperthreading: Enabled
  name: master
  replicas: 1
metadata:
  name: <cluster_name>
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: <machine_network_cidr>
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
pullSecret: '<pull_secret>'
sshKey: '<ssh_pub_key>'
```


The following table describes the required parameters: 

Table 2.1. Required install-config.yaml parametersParameter| Description  
---|---  
`baseDomain` |  Specify the cluster base domain name.   
`compute[].architecture` |  Set to `arm64` for ARM-based deployments. Must match the `controlPlane` architecture.   
`compute[].replicas` |  Set to `0` to make the control plane node schedulable.   
`controlPlane.architecture` |  Set to `arm64` for ARM-based deployments. Must match the `compute` architecture.   
`controlPlane.replicas` |  Set to `1` to ensure the cluster runs on a single node.   
`metadata.name` |  Specify the cluster name.   
`machineNetwork[].cidr` |  Set the CIDR value to match the subnet of the single-node OpenShift cluster.   
`networkType` |  Set to `OVNKubernetes`. This is the only supported network plugin for single-node clusters.   
`pullSecret` |  Copy the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) and add the contents to this configuration setting.   
`sshKey` |  Provide the public SSH key from the administration host so that you can log in to the cluster after installation.   
Show more

  3. Create the `agent-config.yaml` file in the same installation directory as in the following example: 

```yaml
apiVersion: v1beta1
kind: AgentConfig
metadata:
  name: <cluster_name>
rendezvousIP: <node_ip>
```


Replace `<cluster_name>` with the cluster name. This value must match the `metadata.name` value in `install-config.yaml`. Replace `<node_ip>` with the IP address of the node. For single-node OpenShift, this is the IP address of the single node. 

  4. Generate the agent ISO image by running the following command: 

```shell-session
$ openshift-install --dir ~/<install_directory> agent create image
```


The command creates the `agent.aarch64.iso` image in the installation directory. 

  5. Transfer the `agent.aarch64.iso` image to the target ARM server and boot from it. You can use one of the following methods: 

     * Attach the ISO image by using a virtual media interface such as Redfish or a BMC console. 
     * Write the ISO image to a USB drive and boot from it. 
     * Host the ISO image on an HTTP server and boot from it by using the Redfish API. 

The ISO image writes the system configuration to the target installation disk and installs OpenShift Container Platform. 

  6. Monitor the installation progress from the administration host by running the following command: 

```shell-session
$ openshift-install --dir ~/<install_directory> agent wait-for install-complete --log-level=info
```


**Example output**

```shell-session
...................................................................
INFO Cluster is installed
INFO Install complete!
INFO To access the cluster as the system:admin user when using 'oc', run
INFO     export KUBECONFIG=~/<install_directory>/auth/kubeconfig
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.<cluster_name>.<domain>
```


**Verification**

  * After the installation is complete, verify the cluster by running the following commands: 

```shell-session
$ export KUBECONFIG=~/<install_directory>/auth/kubeconfig
```


```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME                    STATUS   ROLES                         AGE     VERSION
<node_name>             Ready    control-plane,master,worker   10m     v1.34.2
```
