# 8.5. Generating a key pair for cluster node SSH access

During an OpenShift Container Platform installation, you can provide an SSH public key to the installation program. The key is passed to Red Hat Enterprise Linux CoreOS (RHCOS) nodes through their Ignition config files and is added to `~/.ssh/authorized_keys` for the `core` user on each node. 

The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication. After the key is passed to the nodes, you can use the key pair to SSH in to the RHCOS nodes as the user `core`. To access the nodes through SSH, the private key identity must be managed by SSH for your local user. 

If you want to SSH in to your cluster nodes to perform installation debugging or disaster recovery, you must provide the SSH public key during the installation process. The `./openshift-install gather` command also requires the SSH public key to be in place on the cluster nodes. 

Important

Do not skip this procedure in production environments, where disaster recovery and debugging is required. 

Note

You must use a local key, not one that you configured with platform-specific approaches. 

**Procedure**

  1. If you do not have an existing SSH key pair on your local machine to use for authentication onto your cluster nodes, create one. For example, on a computer that uses a Linux operating system, run the following command: 

```shell-session
$ ssh-keygen -t ed25519 -N '' -f <path>/<file_name>
```


Specifies the path and file name, such as `~/.ssh/id_ed25519`, of the new SSH key. If you have an existing key pair, ensure your public key is in the your `~/.ssh` directory. 

Note

If you plan to install an OpenShift Container Platform cluster that uses the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the `x86_64`, `ppc64le`, and `s390x` architectures, do not create a key that uses the `ed25519` algorithm. Instead, create a key that uses the `rsa` or `ecdsa` algorithm. 

  2. View the public SSH key: 

```shell-session
$ cat <path>/<file_name>.pub
```


For example, run the following to view the `~/.ssh/id_ed25519.pub` public key: 

```shell-session
$ cat ~/.ssh/id_ed25519.pub
```


  3. Add the SSH private key identity to the SSH agent for your local user, if it has not already been added. SSH agent management of the key is required for password-less SSH authentication onto your cluster nodes, or if you want to use the `./openshift-install gather` command. 

Note

On some distributions, default SSH private key identities such as `~/.ssh/id_rsa` and `~/.ssh/id_dsa` are managed automatically. 

     1. If the `ssh-agent` process is not already running for your local user, start it as a background task: 

```shell-session
$ eval "$(ssh-agent -s)"
```


**Example output**

```shell-session
Agent pid 31874
```


Note

If your cluster is in FIPS mode, only use FIPS-compliant algorithms to generate the SSH key. The key must be either RSA or ECDSA. 

  4. Add your SSH private key to the `ssh-agent`: 

```shell-session
$ ssh-add <path>/<file_name>
```


Specify the path and file name for your SSH private key, such as `~/.ssh/id_ed25519`. 

**Example output**

```shell-session
Identity added: /home/<you>/<path>/<file_name> (<computer_name>)
```


**Next steps**

  * When you install OpenShift Container Platform, provide the SSH public key to the installation program.
