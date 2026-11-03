# 2.4. Installing the commatrix plugin

You can install the `commatrix` plugin from the Red Hat Ecosystem Catalog. 

Note

  * You can also install the `commatrix` plugin by using Krew. For more information, see "CLI Manager Operator overview". 
  * The communication matrix does not include ports from non-core Operators or other software that do not expose a `Service` object. For a complete view of listening ports, run the `generate` command with the `--host-open-ports` flag. 



**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * You installed Podman. 



**Procedure**

  1. Log in to the Red Hat Ecosystem Catalog registry by running the following command and entering your credentials: 

```bash
$ podman login registry.redhat.io
```


  2. Extract the `commatrix` binary from the plugin image by running the following commands: 

```bash
$ podman create --name oc-commatrix registry.redhat.io/openshift-kni/commatrix:v4.22
$ podman cp oc-commatrix:/oc-commatrix .
$ podman rm oc-commatrix
```


  3. Move the extracted binary to a directory in your system `PATH`, such as `/usr/local/bin/`, by running the following command: 

```bash
sudo mv oc-commatrix /usr/local/bin/
```


**Verification**

  * Run the following command to verify that the plugin is available locally: 

```bash
$ oc commatrix
```


```bash
Generate an up-to-date communication flows matrix for all ingress flows of openshift (multi-node and single-node in OpenShift) and Operators.

 Optionally, generate a host open ports matrix and the difference with the communication matrix.

 For additional details, please refer to the communication matrix documentation(https://github.com/openshift-kni/commatrix/blob/main/README.md).

Usage:
  commatrix [command]

Available Commands:
  completion  Generate the autocompletion script for the specified shell
  generate    Generate an up-to-date communication flows matrix for all ingress flows.
  help        Help about any command

Flags:
  -h, --help   help for commatrix

Use "commatrix [command] --help" for more information about a command.
```


**Additional resources**

  * [CLI Manager Operator overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/cli_tools/#cli-manager-overview)
