# 6.2. Configuring the OpenShift Pipelines tkn CLI

Configure the Red Hat OpenShift Pipelines `tkn` CLI to enable tab completion. 

## 6.2.1. Enabling tab completion

After you install the `tkn` CLI, you can enable tab completion to automatically complete `tkn` commands or suggest options when you press Tab. 

**Prerequisites**

  * You must have the `tkn` CLI tool installed. 
  * You must have `bash-completion` installed on your local system. 



**Procedure**

The following procedure enables tab completion for Bash. 

  1. Save the Bash completion code to a file: 

```shell-session
$ tkn completion bash > tkn_bash_completion
```


  2. Copy the file to `/etc/bash_completion.d/`: 

```shell-session
$ sudo cp tkn_bash_completion /etc/bash_completion.d/
```


Alternatively, you can save the file to a local directory and source it from your `.bashrc` file instead. 




Tab completion is enabled when you open a new terminal.
