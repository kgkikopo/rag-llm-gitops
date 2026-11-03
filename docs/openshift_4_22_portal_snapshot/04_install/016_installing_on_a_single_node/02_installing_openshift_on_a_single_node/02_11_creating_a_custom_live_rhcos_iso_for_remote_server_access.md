# 2.11. Creating a custom live RHCOS ISO for remote server access

In some cases, you cannot attach an external disk drive to a server, however, you need to access the server remotely to provision a node. It is recommended to enable SSH access to the server. 

You can create a live RHCOS ISO with SSHd enabled and with predefined credentials so that you can access the server after it boots. 

**Prerequisites**

  * You installed the `butane` utility. 



**Procedure**

  1. Download the `coreos-installer` binary from the `coreos-installer` image [mirror](https://mirror.openshift.com/pub/openshift-v4/clients/coreos-installer/latest/) page. 
  2. Download the latest live RHCOS ISO from [mirror.openshift.com](https://mirror.openshift.com/pub/openshift-v4/x86_64/dependencies/rhcos/4.12/latest/). 
  3. Create the `embedded.yaml` file that the `butane` utility uses to create the Ignition file: 

```yaml
variant: openshift
version: 4.22.0
metadata:
  name: sshd
  labels:
    machineconfiguration.openshift.io/role: worker
passwd:
  users:
    - name: core
      ssh_authorized_keys:
        - '<ssh_key>'
```


For the `passwd.users.name` parameter, the `core` user has sudo privileges. 

  4. Run the `butane` utility to create the Ignition file using the following command: 

```shell-session
$ butane -pr embedded.yaml -o embedded.ign
```


  5. After the Ignition file is created, you can include the configuration in a new live RHCOS ISO, which is named `rhcos-sshd-4.22.0-x86_64-live.x86_64.iso`, with the `coreos-installer` utility: 

```shell-session
$ coreos-installer iso ignition embed -i embedded.ign rhcos-4.22.0-x86_64-live.x86_64.iso -o rhcos-sshd-4.22.0-x86_64-live.x86_64.iso
```


**Verification**

  * Check that the custom live ISO can be used to boot the server by running the following command: 

```shell-session
# coreos-installer iso ignition show rhcos-sshd-4.22.0-x86_64-live.x86_64.iso
```


**Example output**

```plaintext
{
  "ignition": {
    "version": "3.2.0"
  },
  "passwd": {
    "users": [
      {
        "name": "core",
        "sshAuthorizedKeys": [
          "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCZnG8AIzlDAhpyENpK2qKiTT8EbRWOrz7NXjRzopbPu215mocaJgjjwJjh1cYhgPhpAp6M/ttTk7I4OI7g4588Apx4bwJep6oWTU35LkY8ZxkGVPAJL8kVlTdKQviDv3XX12l4QfnDom4tm4gVbRH0gNT1wzhnLP+LKYm2Ohr9D7p9NBnAdro6k++XWgkDeijLRUTwdEyWunIdW1f8G0Mg8Y1Xzr13BUo3+8aey7HLKJMDtobkz/C8ESYA/f7HJc5FxF0XbapWWovSSDJrr9OmlL9f4TfE+cQk3s+eoKiz2bgNPRgEEwihVbGsCN4grA+RzLCAOpec+2dTJrQvFqsD alosadag@sonnelicht.local"
        ]
      }
    ]
  }
}
```
