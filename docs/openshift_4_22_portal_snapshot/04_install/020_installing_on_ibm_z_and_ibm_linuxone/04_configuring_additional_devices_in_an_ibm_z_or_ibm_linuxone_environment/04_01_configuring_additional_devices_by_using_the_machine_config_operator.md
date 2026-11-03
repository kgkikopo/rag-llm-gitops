# 4.1. Configuring additional devices by using the Machine Config Operator

You can use the Machine Config Operator (MCO) to configure additional devices in an IBM Z® or IBM® LinuxONE environment. Configuring devices with the MCO is persistent but only allows specific configurations for compute nodes. MCO does not allow control plane nodes to have different configurations. 

**Prerequisites**

  * You are logged in to the cluster as a user with administrative privileges. 
  * The device must be available to the z/VM guest. 
  * The device is already attached. 
  * The device is not included in the `cio_ignore` list, which can be set in the kernel parameters. 
  * You have created a `MachineConfig` object file with the following YAML: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: worker0
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,worker0]}
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/worker0: ""
```


**Procedure**

  1. To configure an FCP host adapter with N_Port Identifier Virtualization (NPIV) by adding a udev rule, complete the following steps: 

     1. Take the following sample udev rule `441-zfcp-host-0.0.8000.rules`: 

```shell-session
ACTION=="add", SUBSYSTEM=="ccw", KERNEL=="0.0.8000", DRIVER=="zfcp", GOTO="cfg_zfcp_host_0.0.8000"
ACTION=="add", SUBSYSTEM=="drivers", KERNEL=="zfcp", TEST=="[ccw/0.0.8000]", GOTO="cfg_zfcp_host_0.0.8000"
GOTO="end_zfcp_host_0.0.8000"

LABEL="cfg_zfcp_host_0.0.8000"
ATTR{[ccw/0.0.8000]online}="1"

LABEL="end_zfcp_host_0.0.8000"
```


     2. Convert the rule to Base64 encoded by running the following command: 

```shell-session
$ base64 /path/to/file/
```


     3. Copy the following MCO sample profile into a YAML file: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
   labels:
     machineconfiguration.openshift.io/role: worker0
   name: 99-worker0-devices
spec:
   config:
     ignition:
       version: 3.2.0
     storage:
       files:
       - contents:
           source: <base64_data_uri>
         filesystem: root
         mode: 420
         path: /etc/udev/rules.d/41-zfcp-host-0.0.8000.rules
```


where: 

`metadata.labels.machineconfiguration.openshift.io/role`
     Specifies the role you have defined in the machine config file. 
`spec.config.storage.files.contents.source`
     Specifies the data URI for the Base64 encoded udev rule. The value is the Base64 encoded string that you generated in the previous step, formatted as an Ignition data URI. 
`spec.config.storage.files.path`
     Specifies the path where the udev rule is located. 

  2. To configure an FCP LUN by adding a udev rule, complete the following steps. You can add new FCP LUNs or add additional paths to LUNs that are already configured with multipathing. 

     1. Take the following sample udev rule `41-zfcp-lun-0.0.8000:0x500507680d760026:0x00bc000000000000.rules`: 

```shell-session
ACTION=="add", SUBSYSTEMS=="ccw", KERNELS=="0.0.8000", GOTO="start_zfcp_lun_0.0.8207"
GOTO="end_zfcp_lun_0.0.8000"

LABEL="start_zfcp_lun_0.0.8000"
SUBSYSTEM=="fc_remote_ports", ATTR{port_name}=="0x500507680d760026", GOTO="cfg_fc_0.0.8000_0x500507680d760026"
GOTO="end_zfcp_lun_0.0.8000"

LABEL="cfg_fc_0.0.8000_0x500507680d760026"
ATTR{[ccw/0.0.8000]0x500507680d760026/unit_add}="0x00bc000000000000"
GOTO="end_zfcp_lun_0.0.8000"

LABEL="end_zfcp_lun_0.0.8000"
```


     2. Convert the rule to Base64 encoded by running the following command: 

```shell-session
$ base64 /path/to/file/
```


     3. Copy the following MCO sample profile into a YAML file: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
   labels:
     machineconfiguration.openshift.io/role: worker0
   name: 99-worker0-devices
spec:
   config:
     ignition:
       version: 3.2.0
     storage:
       files:
       - contents:
           source: <base64_data_uri>
         filesystem: root
         mode: 420
         path: /etc/udev/rules.d/41-zfcp-lun-0.0.8000:0x500507680d760026:0x00bc000000000000.rules
```


where: 

`metadata.labels.machineconfiguration.openshift.io/role`
     Specifies the role you have defined in the machine config file. 
`spec.config.storage.files.contents.source`
     Specifies the data URI for the Base64 encoded udev rule. The value is the Base64 encoded string that you generated in the previous step, formatted as an Ignition data URI. 
`spec.config.storage.files.path`
     Specifies the path where the udev rule is located. 

  3. To configure a DASD device by adding a udev rule, complete the following steps: 

     1. Take the following sample udev rule `41-dasd-eckd-0.0.4444.rules`: 

```shell-session
ACTION=="add", SUBSYSTEM=="ccw", KERNEL=="0.0.4444", DRIVER=="dasd-eckd", GOTO="cfg_dasd_eckd_0.0.4444"
ACTION=="add", SUBSYSTEM=="drivers", KERNEL=="dasd-eckd", TEST=="[ccw/0.0.4444]", GOTO="cfg_dasd_eckd_0.0.4444"
GOTO="end_dasd_eckd_0.0.4444"

LABEL="cfg_dasd_eckd_0.0.4444"
ATTR{[ccw/0.0.4444]online}="1"

LABEL="end_dasd_eckd_0.0.4444"
```


     2. Convert the rule to Base64 encoded by running the following command: 

```shell-session
$ base64 /path/to/file/
```


     3. Copy the following MCO sample profile into a YAML file: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
   labels:
     machineconfiguration.openshift.io/role: worker0
   name: 99-worker0-devices
spec:
   config:
     ignition:
       version: 3.2.0
     storage:
       files:
       - contents:
           source: <base64_data_uri>
         filesystem: root
         mode: 420
         path: /etc/udev/rules.d/41-dasd-eckd-0.0.4444.rules
```


where: 

`metadata.labels.machineconfiguration.openshift.io/role`
     Specifies the role you have defined in the machine config file. 
`spec.config.storage.files.contents.source`
     Specifies the data URI for the Base64 encoded udev rule. The value is the Base64 encoded string that you generated in the previous step, formatted as an Ignition data URI. 
`spec.config.storage.files.path`
     Specifies the path where the udev rule is located. 

  4. To configure a qeth device by adding a udev rule, complete the following steps: 

     1. Take the following sample udev rule `41-qeth-0.0.1000.rules`: 

```shell-session
ACTION=="add", SUBSYSTEM=="drivers", KERNEL=="qeth", GOTO="group_qeth_0.0.1000"
ACTION=="add", SUBSYSTEM=="ccw", KERNEL=="0.0.1000", DRIVER=="qeth", GOTO="group_qeth_0.0.1000"
ACTION=="add", SUBSYSTEM=="ccw", KERNEL=="0.0.1001", DRIVER=="qeth", GOTO="group_qeth_0.0.1000"
ACTION=="add", SUBSYSTEM=="ccw", KERNEL=="0.0.1002", DRIVER=="qeth", GOTO="group_qeth_0.0.1000"
ACTION=="add", SUBSYSTEM=="ccwgroup", KERNEL=="0.0.1000", DRIVER=="qeth", GOTO="cfg_qeth_0.0.1000"
GOTO="end_qeth_0.0.1000"

LABEL="group_qeth_0.0.1000"
TEST=="[ccwgroup/0.0.1000]", GOTO="end_qeth_0.0.1000"
TEST!="[ccw/0.0.1000]", GOTO="end_qeth_0.0.1000"
TEST!="[ccw/0.0.1001]", GOTO="end_qeth_0.0.1000"
TEST!="[ccw/0.0.1002]", GOTO="end_qeth_0.0.1000"
ATTR{[drivers/ccwgroup:qeth]group}="0.0.1000,0.0.1001,0.0.1002"
GOTO="end_qeth_0.0.1000"

LABEL="cfg_qeth_0.0.1000"
ATTR{[ccwgroup/0.0.1000]online}="1"

LABEL="end_qeth_0.0.1000"
```


     2. Convert the rule to Base64 encoded by running the following command: 

```shell-session
$ base64 /path/to/file/
```


     3. Copy the following MCO sample profile into a YAML file: 

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
   labels:
     machineconfiguration.openshift.io/role: worker0
   name: 99-worker0-devices
spec:
   config:
     ignition:
       version: 3.2.0
     storage:
       files:
       - contents:
           source: <base64_data_uri>
         filesystem: root
         mode: 420
         path: /etc/udev/rules.d/41-dasd-eckd-0.0.4444.rules
```


where: 

`metadata.labels.machineconfiguration.openshift.io/role`
     Specifies the role you have defined in the machine config file. 
`spec.config.storage.files.contents.source`
     Specifies the data URI for the Base64 encoded udev rule. The value is the Base64 encoded string that you generated in the previous step, formatted as an Ignition data URI. 
`spec.config.storage.files.path`
     Specifies the path where the udev rule is located. 




**Additional resources**

  * [Install and configure the Local Storage Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-local-volume)
  * [Observing and updating the node network state and configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/kubernetes_nmstate/#k8s-nmstate-updating-node-network-config)
