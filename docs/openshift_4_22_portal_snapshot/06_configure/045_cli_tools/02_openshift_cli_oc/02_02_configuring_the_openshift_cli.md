# 2.2. Configuring the OpenShift CLI

You can customize your command-line environment after installing the OpenShift CLI (`oc`). 

## 2.2.1. Enabling tab completion

You can enable tab completion for the Bash or Zsh shells. 

### 2.2.1.1. Enable tab completion for Bash

After you install the OpenShift CLI (`oc`), you can enable tab completion to automatically complete `oc` commands or suggest options when you press Tab. The following procedure enables tab completion for the Bash shell. 

**Prerequisites**

  * You must have the OpenShift CLI (`oc`) installed. 
  * You must have the package `bash-completion` installed. 



**Procedure**

  1. Save the Bash completion code to a file: 

```shell-session
$ oc completion bash > oc_bash_completion
```


  2. Copy the file to `/etc/bash_completion.d/`: 

```shell-session
$ sudo cp oc_bash_completion /etc/bash_completion.d/
```


You can also save the file to a local directory and source it from your `.bashrc` file instead. Tab completion is enabled when you open a new terminal. 




### 2.2.1.2. Enable tab completion for Zsh

After you install the OpenShift CLI (`oc`), you can enable tab completion to automatically complete `oc` commands or suggest options when you press Tab. The following procedure enables tab completion for the Zsh shell. 

**Prerequisites**

  * You must have the OpenShift CLI (`oc`) installed. 



**Procedure**

  * To add tab completion for `oc` to your `.zshrc` file, run the following command: 

```shell-session
$ cat >>~/.zshrc<<EOF
autoload -Uz compinit
compinit
if [ $commands[oc] ]; then
  source <(oc completion zsh)
  compdef _oc oc
fi
EOF
```


Tab completion is enabled when you open a new terminal. 




## 2.2.2. Access kubeconfig by using the oc CLI

You can use the `oc` CLI to log in to your OpenShift cluster and retrieve a kubeconfig file for accessing the cluster from the command line. 

Important

If you plan to reuse the exported `kubeconfig` file across sessions or machines, store it securely and avoid committing it to source control. 

**Prerequisites**

  * You have access to the OpenShift Container Platform web console or API server endpoint. 



**Procedure**

  1. Log in to your OpenShift cluster by running the following command: 

```shell-session
$ oc login <api_server_url> -u <username> -p <password>
```


where: 

`<api_server_url>`
     Specifies the full API server URL; for example, `<https://api.my-cluster.example.com:6443>`. 
`<username>`
     Specifies a valid username; for example, `kubeadmin`. 
`<password>`
     Specifies the password for the specified user; for example, the `kubeadmin` password generated during cluster installation. 

  2. Save the cluster configuration to a local file by running the following command: 

```shell-session
$ oc config view --raw > kubeconfig
```


  3. Set the `KUBECONFIG` environment variable to point to the exported file by running the following command: 

```shell-session
$ export KUBECONFIG=./kubeconfig
```


  4. Use `oc` to interact with your OpenShift cluster by running the following command: 

```shell-session
$ oc get nodes
```
