# 18.1. Installing the Network Observability CLI

The Network Observability CLI (oc netobserv) is a standalone OpenShift CLI (`oc`) plugin used to debug and troubleshoot cluster network traffic. It operates independently of the Network Observability Operator to gather immediate network performance diagnostics. 

## 18.1.1. Network Observability CLI overview

Use the Network Observability CLI (`oc netobserv`) to quickly debug and troubleshoot networking issues. This tool provides instant, live insight into flows and packets without installing the Network Observability Operator. 

The Network Observability CLI is a flow and packet visualization tool that relies on eBPF agents to stream collected data to an ephemeral collector pod. It requires no persistent storage during the capture. After the run, the output is transferred to your local machine. 

Important

CLI capture is meant to run only for short durations, such as 8-10 minutes. If it runs for too long, it can be difficult to delete the running process. 

## 18.1.2. Install the Network Observability CLI

The Network Observability CLI gives you a lightweight way to quickly debug and troubleshoot network observability. It must be installed separately. 

Installing the Network Observability CLI (`oc netobserv`) is a separate procedure from the Network Observability Operator installation. This means that, even if the Operator is installed from the software catalog, the `CLI` must be installed separately. 

Note

Users can optionally use Krew to install the `netobserv` CLI plugin. For more information, see "Installing a CLI plugin with Krew". 

**Prerequisites**

  * You must install the OpenShift CLI (`oc`). 
  * You must have a macOS or Linux operating system. 
  * You must install either `docker` or `podman`. 



Note

You can use `podman` or `docker` to run the installation commands. This procedure uses `podman`. 

**Procedure**

  1. Log in to the **Red Hat registry** by running the following command: 

```shell-session
$ podman login registry.redhat.io
```


  2. Extract the `oc-netobserv` file from the image by running the following commands: 

```shell-session
$ podman create --name netobserv-cli registry.redhat.io/network-observability/network-observability-cli-rhel9:1.11
$ podman cp netobserv-cli:/oc-netobserv .
$ podman rm netobserv-cli
```


  3. Move the extracted file to a directory that is on the system’s `PATH`, such as `/usr/local/bin/`, by running the following command: 

```shell-session
$ sudo mv oc-netobserv /usr/local/bin/
```


**Verification**

  1. Verify that `oc netobserv` is available: 

```shell-session
$ oc netobserv version
```


This command should produce an outcome similar to the following example: 




```plaintext
Netobserv CLI version <version>
```


**Additional resources**

  * [Installing and using CLI plugins](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#cli-installing-plugins_cli-extend-plugins)
  * [Installing the CLI Manager Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#installing-cli-manager)
