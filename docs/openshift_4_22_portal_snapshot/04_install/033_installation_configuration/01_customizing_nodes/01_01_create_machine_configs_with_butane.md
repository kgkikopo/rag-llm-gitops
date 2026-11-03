# 1.1. Create machine configs with Butane

Machine configs are used to configure control plane and compute machines by instructing machines how to create users and file systems, set up the network, install systemd units, and more. 

Because modifying machine configs can be difficult, you can use Butane configs to create machine configs for you, thereby making node configuration much easier. 

## 1.1.1. About Butane

Butane is a command-line utility that OpenShift Container Platform uses to provide convenient, short-hand syntax for writing machine configs, and for performing additional validation of machine configs. The format of the Butane config file that Butane accepts is defined in the Butane config specification. 

**Additional resources**

  * [Butane config specification](https://coreos.github.io/butane/specs/)



## 1.1.2. Installing Butane

You can install the Butane tool (`butane`) to create OpenShift Container Platform machine configs from a command-line interface. You can install `butane` on Linux, Windows, or macOS by downloading the corresponding binary file. 

Tip

Butane releases are backwards-compatible with older releases and with the Fedora CoreOS Config Transpiler (FCCT). 

**Procedure**

  1. Navigate to the Butane image download page at <https://mirror.openshift.com/pub/openshift-v4/clients/butane/>. 
  2. Get the `butane` binary: 

     1. To save the latest version of Butane, save the `butane` image to your current directory: 

```shell-session
$ curl https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane --output butane
```


     2. Optional: For a specific architecture, such as aarch64 or ppc64le, indicate the appropriate URL: 

```shell-session
$ curl https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane-aarch64 --output butane
```


  3. Make the downloaded binary file executable: 

```shell-session
$ chmod +x butane
```


  4. Move the `butane` binary file to a directory on your `PATH`. 

To check your `PATH`, open a terminal and execute the following command: 

```shell-session
$ echo $PATH
```


**Verification**

  * You can now use the Butane tool by running the `butane` command: 

```shell-session
$ butane <butane_file>
```


## 1.1.3. Creating a MachineConfig object by using Butane

You can use Butane to produce a `MachineConfig` object so that you can configure compute or control plane nodes at installation time or through the Machine Config Operator. 

**Prerequisites**

  * You have installed the `butane` utility. 



**Procedure**

  1. Create a Butane config file. The following example creates a file named `99-worker-custom.bu` that configures kernel debug messages and specifies custom settings for the chrony time service: 

```yaml
variant: openshift
version: 4.22.0
metadata:
  name: 99-worker-custom
  labels:
    machineconfiguration.openshift.io/role: worker
openshift:
  kernel_arguments:
    - loglevel=7
storage:
  files:
    - path: /etc/chrony.conf
      mode: 0644
      overwrite: true
      contents:
        inline: |
          pool 0.rhel.pool.ntp.org iburst
          driftfile /var/lib/chrony/drift
          makestep 1.0 3
          rtcsync
          logdir /var/log/chrony
```


Note

The `99-worker-custom.bu` file is set to create a machine config for compute nodes. To deploy on control plane nodes, change the role from `worker` to `master`. To configure both node types, repeat the procedure and specify different file names and roles for each node type. 

  2. Create a `MachineConfig` object by giving Butane the file that you created in the previous step: 

```shell-session
$ butane 99-worker-custom.bu -o ./99-worker-custom.yaml
```


A `MachineConfig` object YAML file is created for you to finish configuring your machines. 

  3. Save the Butane config in case you need to update the `MachineConfig` object in the future. 
  4. Choose one of the following options: 

     * If the cluster is not running yet, generate manifest files and add the `MachineConfig` object YAML file to the `openshift` directory. 
     * If the cluster is already running, apply the file as follows: 

```shell-session
$ oc create -f 99-worker-custom.yaml
```
