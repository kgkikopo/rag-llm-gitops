# 2.9. Change the core user password for node access

You can use the default `core` user to access a node through a cloud provider serial console or a bare metal baseboard controller manager (BMC) if a node is down and you cannot access that node by using SSH or the `oc debug node` command. 

By default, Red Hat Enterprise Linux CoreOS (RHCOS) creates a user named `core` on the nodes in your cluster. However, there is no password for this user. As such, you cannot log in with this user without creating a password by using a machine config. The Machine Config Operator (MCO) assigns the password and injects the password into the `/etc/shadow` file, allowing you to log in with the `core` user. The MCO does not examine the password hash. As such, the MCO cannot report if there is a problem with the password. 

Note

  * The password works only through a cloud provider serial console or a BMC. It does not work with SSH. 
  * If you have a machine config that includes an `/etc/shadow` file or a systemd unit that sets a password, it takes precedence over the password hash. 



You can change the password, if needed, by editing the machine config you used to create the password. Also, you can remove the password by deleting the machine config. Deleting the machine config does not remove the user account. 

**Procedure**

  1. Using a tool that is supported by your operating system, create a hashed password. For example, create a hashed password using `mkpasswd` by running the following command: 

```shell-session
$ mkpasswd -m SHA-512 testpass
```


**Example output**

```shell-session
$ $6$CBZwA6s6AVFOtiZe$aUKDWpthhJEyR3nnhM02NM1sKCpHn9XN.NPrJNQ3HYewioaorpwL3mKGLxvW0AOb4pJxqoqP4nFX77y0p00.8.
```


  2. Create a machine config file that contains the `core` username and the hashed password: 

```shell-session
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: set-core-user-password
spec:
  config:
    ignition:
      version: 3.5.0
    passwd:
      users:
      - name: core
        passwordHash: <password>
```


where: 

`spec.config.passwd.users.name`
     Specifies the user name. This must be `core`. 
`spec.config.passwd.users.passwordHash`
     Specifies the hashed password to use with the `core` account. 

  3. Create the machine config by running the following command: 

```shell-session
$ oc create -f <file-name>.yaml
```


The nodes do not reboot and should become available in a few moments. You can use the `oc get mcp` to watch for the machine config pools to be updated, as shown in the following example: 

```plaintext
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master   rendered-master-d686a3ffc8fdec47280afec446fce8dd   True      False      False      3              3                   3                     0                      64m
worker   rendered-worker-4605605a5b1f9de1d061e9d350f251e5   False     True       False      3              0                   0                     0                      64m
```


**Verification**

  1. After the nodes return to the `UPDATED=True` state, start a debug session for a node by running the following command: 

```shell-session
$ oc debug node/<node_name>
```


  2. Set `/host` as the root directory within the debug shell by running the following command: 

```shell-session
sh-4.4# chroot /host
```


  3. Check the contents of the `/etc/shadow` file: 

**Example output**

```shell-session
...
core:$6$2sE/010goDuRSxxv$o18K52wor.wIwZp:19418:0:99999:7:::
...
```


The hashed password is assigned to the `core` user.
