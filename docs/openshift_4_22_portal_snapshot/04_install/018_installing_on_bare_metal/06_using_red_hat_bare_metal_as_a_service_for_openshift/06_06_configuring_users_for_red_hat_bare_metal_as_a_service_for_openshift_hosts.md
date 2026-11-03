# 6.6. Configuring users for Red Hat Bare-Metal-as-a-Service for OpenShift hosts

Configure bare-metal host users and add them to a Kubernetes secret. Then, create and apply the secret to customize the host. With configured users you can access or manage the bare-metal host after it is provisioned. 

**Procedure**

  1. Create a file named `<hostname>-user-data.yaml`, where `<hostname>` is the name of the bare-metal host, with the following content: 

```yaml
users:
  - name: <name>
    sudo: [<sudo_config>]
    ssh_authorized_keys:
      - <key_type>
      <key>
    shell: <shell_path>
    groups: [<groups>]
    lock_passwd: true|false
```


`users.name`
     The user name. 
`users.sudo`
     The sudo configuration for the user. 
`users.ssh_authorized_keys.<key_type>`
     The SSH key type. 
`users.ssh_authorized_keys.<key>`
     The public SSH key to use when accessing this host as the `<name>` user. 
`users.shell`
     The shell to use when accessing the host. 
`users.groups`
     The groups the user belongs to. 
`users.lock_passwd`
     Whether the user password is locked. If `true`, the user cannot log in by using the password, but can still use SSH. 

**Example user**

```yaml
users:
  - name: sysadmin
    sudo: ["ALL=(ALL) NOPASSWD:ALL"]
    ssh_authorized_keys:
      - ssh-rsa AAAAB3NzaC1yc2E... sysadmin@workstation.example.com
    shell: /bin/bash
    groups: [adm, sudo]
    lock_passwd: true
```


  2. Create a secret from the `<hostname>-user-data.yaml` file by running the following command: 

```shell-session
$ oc create secret generic <hostname>-user-data \
  --from-file=userData=<hostname>-user-data.yaml -n bmaas
```


`<hostname>`
     The name of the bare-metal host. 

  3. Configure the `BareMetalHost` to use the `<hostname>-user-data.yaml` file by running the following command: 

```shell-session
$ oc patch baremetalhost <hostname> -n bmaas \
     --type merge -p '{"spec":{"userData":{"name":"<hostname>-user-data"}}}'
```


`<hostname>`
     The name of the bare-metal host.
