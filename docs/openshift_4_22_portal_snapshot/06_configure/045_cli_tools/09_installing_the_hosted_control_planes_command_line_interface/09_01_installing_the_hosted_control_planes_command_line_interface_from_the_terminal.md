# 9.1. Installing the hosted control planes command-line interface from the terminal

You can install the hosted control planes command-line interface (CLI), `hcp`, from the terminal. 

**Prerequisites**

  * On an OpenShift Container Platform cluster, you have installed multicluster engine for Kubernetes Operator 2.5 or later. The multicluster engine Operator is automatically installed when you install Red Hat Advanced Cluster Management. You can also install multicluster engine Operator without Red Hat Advanced Management as an Operator from the OpenShift Container Platform software catalog. 



**Procedure**

  1. Get the URL to download the `hcp` binary by running the following command: 

```shell-session
$ oc get ConsoleCLIDownload hcp-cli-download -o json | jq -r ".spec"
```


  2. Download the `hcp` binary by running the following command: 

```shell-session
$ wget <hcp_cli_download_url>
```


Replace `hcp_cli_download_url` with the URL that you obtained from the previous step. 

  3. Unpack the downloaded archive by running the following command: 

```shell-session
$ tar xvzf hcp.tar.gz
```


  4. Make the `hcp` binary file executable by running the following command: 

```shell-session
$ chmod +x hcp
```


  5. Move the `hcp` binary file to a directory in your path by running the following command: 

```shell-session
$ sudo mv hcp /usr/local/bin/.
```


Note

If you download the CLI on a Mac computer, you might see a warning about the `hcp` binary file. You need to adjust your security settings to allow the binary file to be run. 




**Verification**

  * Verify that you see the list of available parameters by running the following command: 

```shell-session
$ hcp create cluster <platform> --help
```


You can use the `hcp create cluster` command to create and manage hosted clusters. The supported platforms are `agent`, `aws`, and `kubevirt`. The `azure` and `openstack` platforms are also available as Technology Preview features.
