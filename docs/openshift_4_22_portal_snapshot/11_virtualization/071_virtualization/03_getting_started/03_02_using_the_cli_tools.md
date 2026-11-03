# 3.2. Using the CLI tools

You can manage OpenShift Virtualization resources by using the `virtctl` command-line tool. Virtual machine (VM) commands can also be used to manage virtual machine instances (VMIs) unless otherwise specified. 

Note

You can access and change VM disk images by using the `libguestfs` command-line tool. You deploy `libguestfs` by using the `virtctl libguestfs` command. 

## 3.2.1. Install the virtctl binary

Download and install the `virtctl` binary that is available from the OpenShift Container Platform web console. You can run `virtctl` on Red Hat Enterprise Linux (RHEL) 9 or later, other Linux operating systems, Windows, or macOS. 

**Procedure**

  1. Navigate to the **Virtualization** page in the web console. 
  2. Click the **Question Mark (?)** icon in the top right corner of screen. 
  3. Select **Command Line Tools** from the menu. 
  4. Locate the **virtctl - KubeVirt command line interface** section of the page. 
  5. Click the **Download virtctl** link to download the `virtctl` binary for your operating system. 
  6. Install `virtctl`: 

     * For RHEL and other Linux operating systems: 

       1. Decompress the archive file: 

```shell-session
$ tar -xvf <virtctl-version-distribution.arch>.tar.gz
```


       2. Run the following command to make the `virtctl` binary executable: 

```shell-session
$ chmod +x <path/virtctl-file-name>
```


       3. Move the `virtctl` binary to a directory in your `PATH` environment variable. 

You can check your path by running the following command: 

```shell-session
$ echo $PATH
```


       4. Set the `KUBECONFIG` environment variable: 

```shell-session
$ export KUBECONFIG=/home/<user>/clusters/current/auth/kubeconfig
```


     * For Windows: 

       1. Decompress the archive file. 
       2. Navigate the extracted folder hierarchy and double-click the `virtctl` executable file to install the client. 
       3. Move the `virtctl` binary to a directory in your `PATH` environment variable. 

You can check your path by running the following command: 

```shell-session
C:\> path
```


     * For macOS: 

       1. Decompress the archive file. 
       2. Move the `virtctl` binary to a directory in your `PATH` environment variable. 

You can check your path by running the following command: 

```shell-session
echo $PATH
```


## 3.2.2. virtctl information commands

You can use the following `virtctl` commands to view the client and server versions and to list the commands and options that are available. 

Table 3.1. Information commandsCommand| Description  
---|---  
`virtctl version` |  View the `virtctl` client and server versions.   
`virtctl help` |  View a list of `virtctl` commands.   
`virtctl <command> -h|--help` |  View a list of options for a specific command.   
`virtctl options` |  View a list of global command options for any `virtctl` command.   
Show more

## 3.2.3. VM information commands

You can use the following `virtctl` commands to view the file systems, operating systems, and logged-in users of a guest machine. 

Table 3.2. VM information commandsCommand| Description  
---|---  
`virtctl fslist <vm_name>` |  View the file systems available on a guest machine.   
`virtctl guestosinfo <vm_name>` |  View information about the operating systems on a guest machine.   
`virtctl userlist <vm_name>` |  View the logged-in users on a guest machine.   
Show more

## 3.2.4. VM manifest creation commands

You can use the following `virtctl create` commands to create manifests for virtual machines (VMs), instance types, and preferences. 

Table 3.3. VM manifest creation commandsCommand| Description  
---|---  
`virtctl create vm` |  Create a `VirtualMachine` (VM) manifest.   
`virtctl create vm --name <vm_name>` |  Create a VM manifest, specifying a name for the VM.   
`virtctl create vm --user <user_name> --ssh-key|password-file=<value>` |  Create a VM manifest with a cloud-init configuration to create the selected user and either add an SSH public key from the supplied string, or a password from a file.   
`virtctl create vm --access-cred type:password,src:<secret>` |  Create a VM manifest with a user and password combination injected from the selected secret.   
`virtctl create vm --access-cred type:ssh,src:<secret>,user:<user_name>` |  Create a VM manifest with an SSH public key injected from the selected secret.   
`virtctl create vm --volume-sysprep src:<config_map>` |  Create a VM manifest, specifying a config map to use as the sysprep volume. The config map must contain a valid answer file named `unattend.xml` or `autounattend.xml`.   
`virtctl create vm --instancetype <instancetype_name>` |  Create a VM manifest that uses an existing cluster-wide instance type.   
`virtctl create vm --instancetype=virtualmachineinstancetype/<instancetype_name>` |  Create a VM manifest that uses an existing namespaced instance type.   
`virtctl create instancetype --cpu <cpu_value> --memory <memory_value> --name <instancetype_name>` |  Create a manifest for a cluster-wide instance type.   
`virtctl create instancetype --cpu <cpu_value> --memory <memory_value> --name <instancetype_name> --namespace <namespace_value>` |  Create a manifest for a namespaced instance type.   
`virtctl create preference --name <preference_name>` |  Create a manifest for a cluster-wide VM preference, specifying a name for the preference.   
`virtctl create preference --namespace <namespace_value>` |  Create a manifest for a namespaced VM preference.   
Show more

## 3.2.5. VM management commands

You can use the following `virtctl` commands to start, stop, pause, restart, and migrate virtual machines (VMs). 

Table 3.4. VM management commandsCommand| Description  
---|---  
`virtctl start <vm_name>` |  Start a VM.   
`virtctl start --paused <vm_name>` |  Start a VM in a paused state. This option enables you to interrupt the boot process from the VNC console.   
`virtctl stop <vm_name>` |  Stop a VM.   
`virtctl stop <vm_name> --grace-period 0 --force` |  Force stop a VM. This option might cause data inconsistency or data loss.   
`virtctl pause vm <vm_name>` |  Pause a VM. The machine state is kept in memory.   
`virtctl unpause vm <vm_name>` |  Unpause a VM.   
`virtctl migrate <vm_name>` |  Migrate a VM.   
`virtctl migrate-cancel <vm_name>` |  Cancel a VM migration.   
`virtctl restart <vm_name>` |  Restart a VM.   
Show more

## 3.2.6. VM connection commands

You can use the following `virtctl` commands to connect to the console of a virtual machine (VM), open an SSH connection, copy files, and expose a port as a service. 

Table 3.5. VM connection commandsCommand| Description  
---|---  
`virtctl console <vm_name>` |  Connect to the serial console of a VM.   
`virtctl expose vm <vm_name> --name <service_name> --type <ClusterIP|NodePort|LoadBalancer> --port <port>` |  Create a service that forwards a designated port of a VM and expose the service on the specified port of the node.  Example: `virtctl expose vm rhel9_vm --name rhel9-ssh --type NodePort --port 22`  
`virtctl scp -i <ssh_key> <file_name> <user_name>@vm/<vm_name>` |  Copy a file from your machine to a VM. This command uses the private key of an SSH key pair. The VM must be configured with the public key.   
`virtctl scp -i <ssh_key> <user_name@vm/<vm_name>:<file_name> .` |  Copy a file from a VM to your machine. This command uses the private key of an SSH key pair. The VM must be configured with the public key.   
`virtctl ssh -i <ssh_key> <user_name>@vm/<vm_name>` |  Open an SSH connection with a VM. This command uses the private key of an SSH key pair. The VM must be configured with the public key.   
`virtctl vnc <vm_name>` |  Connect to the VNC console of a VM.  You must have `virt-viewer` installed.   
`virtctl vnc --proxy-only=true <vm_name>` |  Display the port number and connect manually to a VM by using any viewer through the VNC connection.   
`virtctl vnc --port=<port-number> <vm_name>` |  Specify a port number to run the proxy on the specified port, if that port is available.  If a port number is not specified, the proxy runs on a random port.   
Show more

## 3.2.7. VM export commands

You can use the following `virtctl vmexport` commands to export a volume from a virtual machine (VM), a VM snapshot, or a persistent volume claim (PVC). These commands create the export, download the volume, and retrieve the manifest. 

Table 3.6. VM export commandsCommand| Description  
---|---  
`virtctl vmexport create <vmexport_name> --vm|snapshot|pvc=<object_name>` |  Create a `VirtualMachineExport` custom resource (CR) to export a volume from a VM, VM snapshot, or PVC. 

  * `--vm`: Exports the PVCs of a VM. 
  * `--snapshot`: Exports the PVCs contained in a `VirtualMachineSnapshot` CR. 
  * `--pvc`: Exports a PVC. 
  * Optional: `--ttl=1h` specifies the time to live. The default duration is 2 hours. 

  
`virtctl vmexport delete <vmexport_name>` |  Delete a `VirtualMachineExport` CR manually.   
`virtctl vmexport download <vmexport_name> --output=<output_file> --volume=<volume_name>` |  Download the volume defined in a `VirtualMachineExport` CR. 

  * `--output` specifies the file format. Example: `disk.img.gz`. 
  * `--volume` specifies the volume to download. This flag is optional if only one volume is available. 

Optional: 

  * `--keep-vme` retains the `VirtualMachineExport` CR after download. The default behavior is to delete the `VirtualMachineExport` CR after download. 
  * `--insecure` enables an insecure HTTP connection. 

  
`virtctl vmexport download <vmexport_name> --vm|snapshot|pvc=<object_name> --output=<output_file> --volume=<volume_name>` |  Create a `VirtualMachineExport` CR and then download the volume defined in the CR.   
`virtctl vmexport download export --manifest` |  Retrieve the manifest for an existing export. The manifest does not include the header secret.   
`virtctl vmexport download export --manifest --vm=example` |  Create a VM export for a VM example, and retrieve the manifest. The manifest does not include the header secret.   
`virtctl vmexport download export --manifest --snap=example` |  Create a VM export for a VM snapshot example, and retrieve the manifest. The manifest does not include the header secret.   
`virtctl vmexport download export --manifest --include-secret` |  Retrieve the manifest for an existing export. The manifest includes the header secret.   
`virtctl vmexport download export --manifest --manifest-output-format=json` |  Retrieve the manifest for an existing export in json format. The manifest does not include the header secret.   
`virtctl vmexport download export --manifest --include-secret --output=manifest.yaml` |  Retrieve the manifest for an existing export. The manifest includes the header secret and writes it to the file specified.   
Show more

## 3.2.8. Hot plug and hot unplug commands

You can use the following `virtctl` commands to add or remove a virtual disk while a virtual machine (VM) or virtual machine instance (VMI) is running. 

Table 3.7. Hot plug and hot unplug commandsCommand| Description  
---|---  
`virtctl addvolume <vm_name> --volume-name=<datavolume_or_PVC> [--bus=<bus_type>] [--persist] [--serial=<label>]` |  Hot plug a data volume or persistent volume claim (PVC).  Optional: 

  * `--bus=<bus_type>` specifies the bus type of the added disk. Supported values are `virtio` and `scsi`. The default bus type is `virtio`. 
  * `--persist` mounts the virtual disk permanently on a VM. **This flag does not apply to VMIs.**
  * `--serial=<label>` adds a label to the VM. If you do not specify a label, the default label is the data volume or PVC name. 

  
`virtctl removevolume <vm_name> --volume-name=<virtual_disk>` |  Hot unplug a virtual disk.   
Show more

## 3.2.9. Image upload commands

You can use the following `virtctl image-upload` commands to upload a virtual machine (VM) image to a new or existing data volume. 

Table 3.8. Image upload commandsCommand| Description  
---|---  
`virtctl image-upload dv <datavolume_name> --image-path=</path/to/image> --no-create` |  Upload a VM image to a data volume that already exists.   
`virtctl image-upload dv <datavolume_name> --size=<datavolume_size> --image-path=</path/to/image>` |  Upload a VM image to a new data volume of a specified requested size.   
`virtctl image-upload dv <datavolume_name> --datasource --size=<datavolume_size> --image-path=</path/to/image>` |  Upload a VM image to a new data volume and create an associated `DataSource` object for it.   
Show more

## 3.2.10. Deploy libguestfs by using virtctl

You can use the `virtctl guestfs` command to deploy an interactive container that has `libguestfs-tools` installed and a persistent volume claim (PVC) attached. Use the container to inspect and modify the VM disk on the PVC. 

**Procedure**

  * To deploy a container with `libguestfs-tools`, mount the PVC, and attach a shell to it, run the following command: 

```shell-session
$ virtctl guestfs -n <namespace> <pvc_name>
```


Important

The `<pvc_name>` argument is required. If you do not include it, an error message appears. 




## 3.2.11. Libguestfs and virtctl guestfs commands

The `libguestfs` tools let you access and modify virtual machine (VM) disk images. You can run them in the container that `virtctl guestfs` deploys to view and edit files in a guest, clone VMs, and resize disks. 

You can also use the `virtctl guestfs` command and its sub-commands to modify, inspect, and debug VM disks on a PVC. To see a complete list of possible sub-commands, enter `virt-` on the command line and press the Tab key. For example: 

Command| Description  
---|---  
`virt-edit -a /dev/vda /etc/motd` |  Edit a file interactively in your terminal.   
`virt-customize -a /dev/vda --ssh-inject root:string:<public key example>` |  Inject an ssh key into the guest and create a login.   
`virt-df -a /dev/vda -h` |  See how much disk space is used by a VM.   
`virt-customize -a /dev/vda --run-command 'rpm -qa > /rpm-list'` |  See the full list of all RPMs installed on a guest by creating an output file containing the full list.   
`virt-cat -a /dev/vda /rpm-list` |  Display the output file list of all RPMs created using the `virt-customize -a /dev/vda --run-command 'rpm -qa > /rpm-list'` command in your terminal.   
`virt-sysprep -a /dev/vda` |  Seal a virtual machine disk image to be used as a template.   
Show more

By default, `virtctl guestfs` creates a session with everything needed to manage a VM disk. However, the command also supports several flag options if you want to customize the behavior: 

Flag Option| Description  
---|---  
`--h` or `--help` |  Provides help for `guestfs`.   
`-n <namespace>` option with a `<pvc_name>` argument  |  To use a PVC from a specific namespace.  If you do not use the `-n <namespace>` option, your current project is used. To change projects, use `oc project <namespace>`.  If you do not include a `<pvc_name>` argument, an error message appears.   
`--image string` |  Lists the `libguestfs-tools` container image.  You can configure the container to use a custom image by using the `--image` option.   
`--kvm` |  Indicates that `kvm` is used by the `libguestfs-tools` container.  By default, `virtctl guestfs` sets up `kvm` for the interactive container, which greatly speeds up the `libguest-tools` execution because it uses QEMU.  If a cluster does not have any `kvm` supporting nodes, you must disable `kvm` by setting the option `--kvm=false`.  If not set, the `libguestfs-tools` pod remains pending because it cannot be scheduled on any node.   
`--pull-policy string` |  Shows the pull policy for the `libguestfs` image.  You can also overwrite the image’s pull policy by setting the `pull-policy` option.   
Show more

The command also checks if a PVC is in use by another pod, in which case an error message appears. However, once the `libguestfs-tools` process starts, the setup cannot avoid a new pod using the same PVC. You must verify that there are no active `virtctl guestfs` pods before starting the VM that accesses the same PVC. 

Note

The `virtctl guestfs` command accepts only a single PVC attached to the interactive pod. 

## 3.2.12. Additional resources

  * [Red Hat Ansible Automation Hub](https://console.redhat.com/ansible/automation-hub)
  * [`libguestfs`](https://libguestfs.org)
