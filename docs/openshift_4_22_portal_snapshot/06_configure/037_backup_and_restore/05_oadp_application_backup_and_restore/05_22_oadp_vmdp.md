# 5.22. OADP VMDP

## 5.22.1. OADP virtual machine data protection

Use OpenShift API for Data Protection virtual machine data protection (VMDP) to back up and restore user data from within VMs on OpenShift Virtualization. This helps you to protect files and directories without relying on cluster administrators. 

### 5.22.1.1. About OADP virtual machine data protection

You can independently back up and restore your own data from within a virtual machine (VM) by using the OADP VM data protection (VMDP) command-line tool. This approach helps you secure specific files and directories in your encrypted repository without requiring cluster administrator privileges. 

#### 5.22.1.1.1. What problem is VMDP solving

Cluster administrators manage traditional OADP backups. The administrator owns the backup storage location, controls what to back up, and manages the restore process. This means that VM users must rely on an administrator to recover their data, and the backup scope is limited to the persistent volume claims (PVCs) attached to the VM at the time of backup. 

VMDP addresses this gap by shifting data ownership to the VM user. The user creates their own encrypted backup repository, chooses what data to protect, and restores data without administrator involvement. This follows zero-trust architecture principles where the user owns the data, the backup, and the encryption keys. Administrators cannot access or restore the user’s backup data. 

#### 5.22.1.1.2. What VMDP does

VMDP is a command-line tool that runs inside virtual machines on OpenShift Virtualization. With VMDP, you can complete the following tasks: 

  * Back up and restore files and directories from within the VM by using a single command. 
  * Protect data accessible over network file systems such as Common Internet File System (CIFS) and Network File System (NFS) shares, which standard OADP backups typically exclude. 
  * Create a personal encrypted repository in S3-compatible or file system storage. 
  * Use data deduplication for efficient storage and fast incremental backups. 



VMDP is based on Kopia and uses the same repository format. 

#### 5.22.1.1.3. Who uses VMDP

VMDP is designed for VM users who need to manage their own backups independently. The user is responsible for: 

  * Providing their own credentials to create an encrypted backup repository. 
  * Choosing what data to back up and restore. 
  * Managing backup lifecycle operations such as listing, deleting, and restoring backups. 



Cluster administrators are not involved in the backup and restore process. Their role is limited to deploying the OADP Operator. The OADP Operator has the VMDP CLI available for download. 

#### 5.22.1.1.4. VMDP and VMFR comparison

OADP provides two complementary features for VM data recovery: 

VMDP (VM data protection)
     The VM user, without `cluster-admin` privileges, owns the data. The user creates encrypted backups of selected files and directories from within the VM. The user holds the encryption keys and manages the backup lifecycle independently. 
VMFR (VM file restore)
     The cluster administrator manages the backups and file recovery. VMFR enables file-level recovery from admin-created Velero backups of entire VMs, including all PVCs. The administrator controls the backup and restore process. 

### 5.22.1.2. Supported platforms for OADP virtual machine data protection

Review the supported guest operating systems and architectures for the OpenShift API for Data Protection virtual machine data protection (VMDP) command-line interface. This helps you to verify that your VM environment is compatible. 

VMDP is built for [OpenShift Virtualization certified guest operating systems](https://access.redhat.com/articles/4234591) on the following platforms: 

Table 5.48. Supported guest operating systemsGuest operating system| Architectures  
---|---  
Red Hat Enterprise Linux  |  x86_64, AArch64   
Microsoft Windows  |  x86_64, AArch64   
Show more

Each binary is statically linked and includes a SHA256 checksum for integrity verification. 

### 5.22.1.3. OADP virtual machine data protection backend storage

Review the backend storage options for OpenShift API for Data Protection virtual machine data protection (VMDP) backup storage locations. This helps you to configure S3-compatible or file system storage for your backup repository. 

#### 5.22.1.3.1. S3-compatible storage

Table 5.49. S3 storage optionsOption| Description| Default  
---|---|---  
`--bucket` |  Name of the S3 bucket.  |  (required)   
`--access-key` |  Access key ID.  |  (required)   
`--secret-access-key` |  Secret access key.  |  (required)   
`--endpoint` |  S3 endpoint URL.  |  `s3.amazonaws.com`  
`--region` |  S3 region.  |  Auto-detect   
`--prefix` |  Object prefix in the bucket.  |  None   
`--session-token` |  Session token for temporary credentials.  |  None   
`--disable-tls` |  Disable HTTPS.  |  `false`  
`--disable-tls-verification` |  Skip TLS certificate verification.  |  `false`  
`--root-ca-pem-path` |  Path to a custom CA certificate file.  |  None   
`--root-ca-pem-base64` |  Base64-encoded CA certificate.  |  None   
Show more

Note

VMDP automatically prepends `oadp-vmdp/` to your prefix. 

#### 5.22.1.3.2. Filesystem storage

Table 5.50. Filesystem storage optionsOption| Description| Default  
---|---|---  
`--path` |  Absolute path to the storage directory.  |  (required)   
`--owner-uid` |  User ID for new files.  |  Current user   
`--owner-gid` |  Group ID for new files.  |  Current group   
`--file-mode` |  Permission mode for files.  |  `0600`  
`--dir-mode` |  Permission mode for directories.  |  `0700`  
Show more

### 5.22.1.4. OADP virtual machine data protection configuration

Review the environment variables and file locations for the OpenShift API for Data Protection virtual machine data protection (VMDP) command-line interface (CLI). This helps you to configure credentials, logging, and behavioral settings. 

#### 5.22.1.4.1. Environment variables

Table 5.51. Credential environment variablesVariable| Description  
---|---  
`BSLS_PASSWORD` |  BSL encryption password. Set this variable to avoid interactive prompts.   
`AWS_ACCESS_KEY_ID` |  Access key for S3 storage   
`AWS_SECRET_ACCESS_KEY` |  Secret key for S3 storage   
`AWS_SESSION_TOKEN` |  Session token for temporary credentials   
Show more

Table 5.52. Configuration environment variablesVariable| Description| Default  
---|---|---  
`OADP_CONFIG_PATH` |  Path to the configuration file  |  `~/.config/oadp/repository.config`  
`OADP_CACHE_DIRECTORY` |  Path to the cache directory  |  System-dependent   
`OADP_LOG_DIR` |  Directory for log files  |  `~/.cache/oadp/`  
Show more

Table 5.53. Behavior environment variablesVariable| Description| Default  
---|---|---  
`OADP_CHECK_FOR_UPDATES` |  Enable or disable update checks  |  `true`  
`OADP_PERSIST_CREDENTIALS_ON_CONNECT` |  Save credentials after connecting  |  `true`  
`OADP_USE_KEYRING` |  Use the system keyring for password storage  |  `false`  
`OADP_BACKUP_FAIL_FAST` |  Fail immediately on the first error  |  `false`  
Show more

Table 5.54. Logging environment variablesVariable| Description| Default  
---|---|---  
`OADP_LOG_DIR_MAX_FILES` |  Maximum number of log files  |  `1000`  
`OADP_LOG_DIR_MAX_AGE` |  Maximum age of log files  |  `720h`  
`OADP_LOG_DIR_MAX_SIZE_MB` |  Maximum total size of log files in MB  |  `1000`  
Show more

#### 5.22.1.4.2. File locations

Table 5.55. Default file locationsType| Linux| Windows  
---|---|---  
Configuration  |  `~/.config/oadp/repository.config` |  `%APPDATA%\oadp\repository.config`  
Logs  |  `~/.cache/oadp/` |  `%LOCALAPPDATA%\oadp\`  
Show more

#### 5.22.1.4.3. Kopia compatibility

VMDP is based on Kopia and uses the same repository format. Repositories are fully compatible between the two tools. 

Table 5.56. Command mapping between VMDP and KopiaVMDP command| Kopia equivalent  
---|---  
`bsl` |  `repository`  
`backup` |  `snapshot`  
Show more

When you connect to a VMDP repository by using the Kopia CLI, include the `oadp-vmdp/` prefix that VMDP adds automatically. For example: 

```shell-session
$ kopia repository connect s3 \
  --bucket <bucket_name> \
  --prefix oadp-vmdp/<your_prefix>/ \
  ...
```


## 5.22.2. Using OADP virtual machine data protection

Install the OpenShift API for Data Protection virtual machine data protection (VMDP) command-line interface (CLI), configure a backup storage location, and back up and restore data from within your VM. This helps you to manage your own VM backups independently. 

### 5.22.2.1. Install the OADP virtual machine data protection CLI

Install the OpenShift API for Data Protection virtual machine data protection (VMDP) command-line interface (CLI) inside your VM to back up and restore data. This helps you to download the correct binary for your VM guest operating system. 

The OADP Operator deploys a download server in the cluster as the `openshift-adp-vmdp-server` service in the `openshift-adp` namespace. A `ConsoleCLIDownload` resource links to the download server routes, and users can access the download links from the OpenShift Container Platform web console or by using HTTP directly. 

**Prerequisites**

  * You have installed the OADP Operator. 
  * You have a running VM on OpenShift Virtualization with a supported guest operating system. 
  * You have installed the `virtctl` CLI tool. 



**Procedure**

  1. Get the cluster IP of the VMDP download server by running the following command: 

```shell-session
$ oc get svc -n openshift-adp openshift-adp-vmdp-server
```


Make a note of the `CLUSTER-IP` value from the output. 

  2. Install the VMDP CLI: 

     * For Linux VMs, download the VMDP binary and make it executable inside the VM by running the following command: 

```shell-session
$ virtctl ssh <vm_user>@<vm_name> -n <vm_namespace> \
  --command "curl -kLf 'http://<cluster_ip>:80/download/oadp-vmdp_linux_amd64' \
  -o oadp-vmdp_linux_amd64 && chmod +x oadp-vmdp_linux_amd64"
```


where: 

`<vm_user>`
     Specifies the username for the VM. For example, `fedora`. 
`<vm_name>`
     Specifies the name of the VM. 
`<vm_namespace>`
     Specifies the namespace of the VM. 
`<cluster_ip>`
     Specifies the `CLUSTER-IP` value of the `openshift-adp-vmdp-server` service. 

     * For Microsoft Windows VMs, access the VM by using Remote Desktop Protocol (RDP) or the VNC console, open PowerShell, and download the VMDP binary by running the following command: 

```plaintext
PS> curl.exe -L -o oadp-vmdp.exe "http://<cluster_ip>:80/download/oadp-vmdp_windows_amd64.exe"
```


Replace `<cluster_ip>` with the `CLUSTER-IP` value of the `openshift-adp-vmdp-server` service. 




**Verification**

  * Depending on your operating system, use one of the following steps to verify the installation: 

    * For Linux VMs, verify that the binary is installed and working by running the following command: 

```shell-session
$ virtctl ssh <vm_user>@<vm_name> -n <vm_namespace> \
  --command "./oadp-vmdp_linux_amd64 --help"
```


```shell-session
usage: oadp-vmdp [<flags>] <command> [<args> ...]
OADP VM Data Protection - Virtual Machine Data Protection for OpenShift
    Virtualization

Flags:
  --[no-]help                Show context-sensitive help (also try --help-long
                             and --help-man).
  --[no-]version             Show application version.
  --log-file=LOG-FILE        Override log file.
  --[no-]disable-file-logging
                             Disable file-based logging.
  ....
```


    * For Microsoft Windows VMs, open PowerShell and verify the binary by running the following command: 

```plaintext
PS> .\oadp-vmdp.exe --help
```


### 5.22.2.2. Create a backup storage location with S3-compatible storage by using the VMDP CLI

Create a backup storage location (BSL) with S3-compatible storage to set up an encrypted repository for storing your virtual machine (VM) backups. This helps you to configure remote S3-compatible storage for your data. 

When you create a BSL, the virtual machine data protection (VMDP) command-line interface (CLI) creates a personal encrypted repository in the specified storage backend. You provide the encryption password, which is used to encrypt all backup data. Only users with this password can access the backup data. 

**Prerequisites**

  * You have installed the VMDP CLI inside your VM. 
  * You have the storage credentials for your S3-compatible storage. 



**Procedure**

  1. To create a BSL with S3-compatible storage, run the following command: 

```shell-session
$ sshpass -p <vm_password> virtctl ssh vm/<vm_name> -n <vm_namespace> \
  --username <vm_username> \
  --local-ssh-opts=-oUserKnownHostsFile=/dev/null \
  --local-ssh-opts=-oStrictHostKeyChecking=no \
  --local-ssh-opts=-oPreferredAuthentications=password \
  --local-ssh-opts=-oPubkeyAuthentication=no \
  --command "./oadp-vmdp_linux_amd64 bsl create s3 --bucket <bucket_name> --endpoint <s3_endpoint> --access-key <access_key> --secret-access-key <secret_access_key> --disable-tls"
```


where: 

`<vm_password>`
     Specifies the password for the VM user. 
`<vm_name>`
     Specifies the name of the VM. 
`<vm_namespace>`
     Specifies the namespace of the VM. 
`<vm_username>`
     Specifies the username for the VM. For example, `fedora`. 
`<bucket_name>`
     Specifies the name of the S3 bucket. 
`<s3_endpoint>`
     Specifies the S3 endpoint URL. 
`<access_key>`
     Specifies the access key ID. 
`<secret_access_key>`
     Specifies the secret access key. 

You should see an output similar to the following example: 

\+ 

```shell-session
Initializing repository with:
  block hash:          BLAKE2B-256-128
  encryption:          AES256-GCM-HMAC-SHA256
  key derivation:      scrypt-65536-8-1
  splitter:            DYNAMIC-4M-BUZHASH
```


  2. Create an alias for the VMDP binary and name it `oadp-vmdp`. 



**Verification**

  * To verify the BSL connection status, run the following command: 

```shell-session
$ oadp-vmdp bsl status
```


### 5.22.2.3. Create a backup storage location with file system storage by using the VMDP CLI

Create a backup storage location (BSL) with file system storage to set up an encrypted repository for storing your virtual machine (VM) backups. This helps you to configure local file system storage for your data. 

When you create a BSL, the virtual machine data protection (VMDP) command-line interface (CLI) creates a personal encrypted repository in the specified storage backend. You provide the encryption password, which is used to encrypt all backup data. Only users with this password can access the backup data. 

**Prerequisites**

  * You have installed the VMDP CLI inside your VM. 
  * You have created an alias called `oadp-vmdp` for the VMDP CLI binary. 
  * You have access to a local file system path for backup storage. 



**Procedure**

  * To create a BSL with file system storage, run the following command: 

```shell-session
$ oadp-vmdp bsl create filesystem \
  --path <storage_directory_path>
```


Replace `<storage_directory_path>` with the absolute path to the storage directory. 




**Verification**

  * To verify the BSL connection status, run the following command: 

```shell-session
$ oadp-vmdp bsl status
```


### 5.22.2.4. Back up data from a virtual machine by using the VMDP CLI

Back up files and directories from within your virtual machine (VM) by using the OpenShift API for Data Protection VM data protection (VMDP) command-line interface (CLI). This helps you to protect user data, including data accessible over network file systems such as CIFS and NFS shares. 

VMDP uses data deduplication to store data efficiently. If the same data exists in multiple locations, subsequent backups complete faster because only unique data blocks are stored. 

**Prerequisites**

  * You are connected to your virtual machine (VM) by using SSH. 
  * You have installed the VMDP CLI inside your VM. 
  * You have created an alias called `oadp-vmdp` for the VMDP CLI binary. 
  * You have created and connected to a backup storage location. 



**Procedure**

  1. To create a backup of a directory, run the following command: 

```shell-session
$ oadp-vmdp backup create <path_to_data>
```


Replace `<path_to_data>` with the path to the directory or files to back up. 

  2. To list all available backups, run the following command: 

```shell-session
$ oadp-vmdp backup list
```


  3. To delete a specific backup, run the following command: 

```shell-session
$ oadp-vmdp backup delete <backup_id>
```


Replace `<backup_id>` with the ID of the backup to delete. 

Important

After you delete backups, orphaned data objects such as pack blobs are not automatically cleaned up from the underlying storage backend. You must manually remove these orphaned objects directly from your storage backend, for example, by deleting them from your S3 bucket. 




### 5.22.2.5. Restore data to a virtual machine by using the VMDP CLI

Restore data from a backup to your virtual machine (VM) by using the OpenShift API for Data Protection VM data protection (VMDP) command-line interface (CLI). This helps you to recover files to the original location or to a different directory. 

You can restore from the most recent backup or from a specific backup by specifying its ID. You can also restore to a different VM by connecting to the BSL of the new VM. 

**Prerequisites**

  * You are connected to your VM by using SSH. 
  * You have installed the VMDP CLI inside your VM. 
  * You have created an alias called `oadp-vmdp` for the VMDP CLI binary. 
  * You have connected to the backup storage location that contains the backup. 



**Procedure**

  * Depending on your specific use case, use one of the following steps to restore data: 

    * To restore data from the most recent backup, run the following command: 

```shell-session
$ oadp-vmdp restore <path_to_restore>
```


Replace `<path_to_restore>` with the path to restore. 

    * To restore a specific backup to a custom location, run the following commands: 

      1. Retrieve the source backup ID: 

```shell-session
$ oadp-vmdp backup list
```


      2. Restore the backup by running the following command: 

```shell-session
$ oadp-vmdp restore <source_id> <restore_path>
```


where: 

`<source_id>`
     Specifies the ID of the backup to restore. 
`<restore_path>`
     Specifies the directory path where the data is restored. 

    * To restore data from a different VM, run the following commands: 

      1. To connect to the existing BSL from the new VM, run the following command: 

```shell-session
$ oadp-vmdp bsl connect s3 \
  --bucket <bucket_name> \
  --endpoint <s3_endpoint> \
  --access-key <access_key> \
  --secret-access-key <secret_access_key>
```


      2. Restore from the BSL by running the following command: 

```shell-session
$ oadp-vmdp restore <path_to_data>
```


### 5.22.2.6. OADP VMDP BSL management commands

Review the available commands for managing backup storage locations (BSL) with the virtual machine data protection (VMDP) command-line interface (CLI). This helps you to connect, disconnect, and manage your BSL connections. 

Table 5.57. BSL management commandsCommand| Description  
---|---  
`oadp-vmdp bsl create` |  Create and connect to a new BSL.   
`oadp-vmdp bsl connect` |  Connect to an existing BSL.   
`oadp-vmdp bsl disconnect` |  Disconnect from the current BSL.   
`oadp-vmdp bsl status` |  Show the current BSL connection status.   
`oadp-vmdp bsl change-password` |  Change the BSL encryption password.   
Show more

### 5.22.2.7. Troubleshoot OADP virtual machine data protection

Troubleshoot common issues and solutions for the OpenShift API for Data Protection virtual machine data protection (VMDP) command-line interface (CLI). This helps you to resolve connection and configuration problems. 

#### 5.22.2.7.1. Not connected to a backup storage location

If you receive a `Not connected to a Backup Storage Location` error message, check the connection status and reconnect: 

```shell-session
$ oadp-vmdp bsl status
```


```shell-session
$ oadp-vmdp bsl connect s3 \
  --bucket <bucket_name> \
  --endpoint <s3_endpoint> \
  --access-key <access_key> \
  --secret-access-key <secret_access_key>
```


#### 5.22.2.7.2. Prefix must not contain oadp-vmdp

The `oadp-vmdp/` prefix is added automatically. Do not include `oadp-vmdp` as a path segment in the `--prefix` option. Ensure that the `--prefix` value does not start or end with whitespace. 

#### 5.22.2.7.3. S3 connection issues

For S3-compatible services, you might need to use the following options: 

  * `--disable-tls` for non-HTTPS endpoints. 
  * `--disable-tls-verification` for self-signed certificates. 
  * `--root-ca-pem-path` to specify a custom CA certificate. 



#### 5.22.2.7.4. Getting help

  * To view available commands and options, run the following command: 



```shell-session
$ oadp-vmdp --help
```


  * To view help for a specific command, run the following command: 



```shell-session
$ oadp-vmdp <command> --help
```
