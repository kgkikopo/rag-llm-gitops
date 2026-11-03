# 5.1. Adding RHCOS compute machines to an OpenShift Container Platform cluster

You can add more Red Hat Enterprise Linux CoreOS (RHCOS) compute machines to your OpenShift Container Platform cluster on bare metal. 

Before you add more compute machines to a cluster that you installed on bare metal infrastructure, you must create RHCOS machines for it to use. You can either use an ISO image or network PXE booting to create the machines. 

**Prerequisites**

  * You installed a cluster on bare metal. 
  * You have installation media and Red Hat Enterprise Linux CoreOS (RHCOS) images that you used to create your cluster. If you do not have these files, you must obtain them by following the instructions in the installation procedure. 



## 5.1.1. Create RHCOS machines by using an ISO image

To scale your OpenShift Container Platform bare metal cluster, you can create more Red Hat Enterprise Linux CoreOS (RHCOS) compute machines by using an ISO image. 

**Prerequisites**

  * You have obtained the URL of the Ignition config file for the compute machines for your cluster. You uploaded this file to your HTTP server during installation. 
  * You must have the OpenShift CLI (`oc`) installed. 



**Procedure**

  1. Extract the Ignition config file from the cluster by running the following command: 

```shell-session
$ oc extract -n openshift-machine-api secret/worker-user-data-managed --keys=userData --to=- > worker.ign
```


  2. Upload the `worker.ign` Ignition config file you exported from your cluster to your HTTP server. Note the URLs of these files. 
  3. You can validate that the ignition files are available on the URLs. The following example gets the Ignition config files for the compute node: 

```shell-session
$ curl -k http://<HTTP_server>/worker.ign
```


  4. You can access the ISO image for booting your new machine by running the following command: 

```shell-session
RHCOS_VHD_ORIGIN_URL=$(oc -n openshift-machine-config-operator get configmap/coreos-bootimages -o jsonpath='{.data.stream}' | jq -r '.architectures.<architecture>.artifacts.metal.formats.iso.disk.location')
```


  5. Use the ISO file to install RHCOS on more compute machines. Use the same method that you used when you created machines before you installed the cluster: 

     * Burn the ISO image to a disk and boot it directly. 
     * Use ISO redirection with a LOM interface. 

  6. Boot the RHCOS ISO image without specifying any options, or interrupting the live boot sequence. Wait for the installer to boot into a shell prompt in the RHCOS live environment. 

Note

You can interrupt the RHCOS installation boot process to add kernel arguments. However, for this ISO procedure you must use the `coreos-installer` command as outlined in the following steps, instead of adding kernel arguments. 

  7. Run the `coreos-installer` command by using `sudo`. The `core` user does not have the root privileges required to perform the installation. Specify the options that meet your installation requirements. At a minimum, you must specify the URL that points to the Ignition config file for the node type, and the device that you are installing to. 

```shell-session
$ sudo coreos-installer install --ignition-url=http://<HTTP_server>/<node_type>.ign <device> --ignition-hash=sha512-<digest>
```


where: 

`<digest>`
    

Specifies the Ignition config file SHA512 digest obtained through an HTTP URL to validate the authenticity of the Ignition config file on the cluster node. 

Note

If you want to provide your Ignition config files through an HTTPS server that uses TLS, you can add the internal certificate authority (CA) to the system trust store before running `coreos-installer`. 

The following example initializes a compute node installation to the `/dev/sda` device. The Ignition config file for the compute node is obtained from an HTTP web server with the IP address 192.168.1.2: 

```shell-session
$ sudo coreos-installer install --ignition-url=http://192.168.1.2:80/installation_directory/worker.ign /dev/sda --ignition-hash=sha512-a5a2d43879223273c9b60af66b44202a1d1248fc01cf156c46d4a79f552b6bad47bc8cc78ddf0116e80c59d2ea9e32ba53bc807afbca581aa059311def2c3e3b
```


  8. Monitor the progress of the RHCOS installation on the console of the machine. 

Important

Ensure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of RHCOS installation issues that might arise. 

  9. Continue to create more compute machines for your cluster. 



**Additional resources**

  * [Installing a cluster on bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal)



## 5.1.2. Create RHCOS machines by PXE or iPXE booting

To scale your OpenShift Container Platform bare metal cluster, you can create more Red Hat Enterprise Linux CoreOS (RHCOS) compute machines by using PXE or iPXE booting. 

**Prerequisites**

  * You have obtained the URL of the Ignition config file for the compute machines for your cluster. You uploaded this file to your HTTP server during installation. 
  * You have obtained the URLs of the RHCOS ISO image, compressed metal BIOS, `kernel`, and `initramfs` files that you uploaded to your HTTP server during cluster installation. 
  * You have access to the PXE booting infrastructure that you used to create the machines for your OpenShift Container Platform cluster during installation. The machines must boot from their local disks after RHCOS is installed on them. 
  * If you use UEFI, you have access to the `grub.conf` file that you modified during OpenShift Container Platform installation. 



**Procedure**

  1. Confirm that your PXE or iPXE installation for the RHCOS images is correct. 

     * For PXE: 

```plaintext
DEFAULT pxeboot
TIMEOUT 20
PROMPT 0
LABEL pxeboot
    KERNEL http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture>
    APPEND initrd=http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/worker.ign coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img
```


where: 

`KERNEL`
     Specifies the location of the live `kernel` file that you uploaded to your HTTP server. 
`APPEND`
     Specifies the locations of the RHCOS files that you uploaded to your HTTP server: 
`initrd`
     Specifies the location of the live `initramfs` file. 
`coreos.inst.ignition_url`
     Specifies the location of the worker Ignition config file. This parameter supports only HTTP and HTTPS. 
`coreos.live.rootfs_url`
    

Specifies the location of the live `rootfs` file. This parameter supports only HTTP and HTTPS. 

Note

This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `APPEND` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information on setting up a serial terminal and/or console in RHCOS, see "How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?". 

     * For iPXE (`x86_64` \+ `aarch64`): 

```plaintext
kernel http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture> initrd=main coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/worker.ign
initrd --name main http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img
boot
```


where: 

`kernel`
     Specifies the location of the `kernel` file that you uploaded to your HTTP server. 
`initrd=main`
     Specifies an argument that is required for booting on UEFI systems. 
`coreos.live.rootfs_url`
     Specifies the location of the `rootfs` file that you uploaded to your HTTP server. 
`coreos.inst.ignition_url`
     Specifies the location of the worker Ignition config file that you uploaded to your HTTP server. 
`initrd --name main`
    

Specifies the location of the `initramfs` file that you uploaded to your HTTP server. 

Note

       * If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC named `eno1`, set `ip=eno1:dhcp`. 
       * This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `kernel` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information on setting up a serial terminal and/or console in RHCOS, see "How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?" in the Additional resources section and "Enabling the serial console for PXE and ISO installation" in the "Advanced RHCOS installation configuration" section. 

Note

To network boot the CoreOS `kernel` on `aarch64` architecture, you need to use a version of iPXE build with the `IMAGE_GZIP` option enabled. For more information, see "IMAGE_GZIP option in iPXE". 

     * For PXE (with UEFI and GRUB as second stage) on `aarch64`: 

```plaintext
menuentry 'Install CoreOS' {
    linux rhcos-<version>-live-kernel-<architecture>  coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/worker.ign
    initrd rhcos-<version>-live-initramfs.<architecture>.img
}
```


where: 

`linux`
     Specifies the location of the live `kernel` file on your TFTP server. 
`coreos.live.rootfs_url`
     Specifies the location of the live `rootfs` file. 
`coreos.inst.ignition_url`
     Specifies the location of the worker Ignition config file. 
`initrd`
    

Specifies the location of the live `initramfs` file on your TFTP server. 

Note

If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC named `eno1`, set `ip=eno1:dhcp`. 

  2. Use the PXE or iPXE infrastructure to create the required compute machines for your cluster. 



**Additional resources**

  * [How does one set up a serial terminal and/or console in Red Hat Enterprise Linux? (Red Hat Knowledgebase article)](https://access.redhat.com/articles/7212)
  * [`IMAGE_GZIP` option in iPXE (iPXE documentation)](https://ipxe.org/buildcfg/image_gzip)



## 5.1.3. Approve the certificate signing requests for your machines

To allow newly added machines to join your OpenShift Container Platform cluster, confirm that the cluster approves pending certificate signing requests (CSRs), or approve them yourself. Approve client requests first, then server requests. 

**Prerequisites**

  * You added machines to your cluster. 



**Procedure**

  1. Confirm that the cluster recognizes the machines: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME      STATUS    ROLES   AGE  VERSION
master-0  Ready     master  63m  v1.35.4
master-1  Ready     master  63m  v1.35.4
master-2  Ready     master  64m  v1.35.4
```


The output lists all of the machines that you created. 

Note

The preceding output might not include the compute nodes until you approve some CSRs. 

  2. Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster: 

```shell-session
$ oc get csr
```


**Example output**

```shell-session
NAME        AGE     REQUESTOR                                                                   CONDITION
csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
...
```


In this example, two machines are joining the cluster. You might see more approved CSRs in the list. 

  3. If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines: 

Note

You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates rotate, and more than two certificates are present for each node. You must approve all of these certificates. After you approve the client CSR, the kubelet creates a secondary CSR for the serving certificate, which requires manual approval. The `machine-approver` then automatically approves later serving certificate renewal requests if the kubelet requests a new certificate with the same parameters. 

Note

For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If you do not approve a request, the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because the API server requires a serving certificate when it connects to the kubelet. Any operation that contacts the kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the `node-bootstrapper` service account in the `system:node` or `system:admin` groups submitted the CSR, and confirm the identity of the node. 

     * To approve them individually, run the following command for each valid CSR: 

```shell-session
$ oc adm certificate approve <csr_name>
```


where: 

`<csr_name>`
     Specifies the name of a CSR from the list of current CSRs. 

     * To approve all pending CSRs, run the following command: 

```shell-session
$ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
```


Note

Some Operators might not become available until you approve some CSRs. Each node submits two CSRs, so you might need to run the command to approve CSRs many times. 

  4. After you approve your client requests, review the server requests for each machine that you added to the cluster: 

```shell-session
$ oc get csr
```


**Example output**

```shell-session
NAME        AGE     REQUESTOR                                                                   CONDITION
csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
...
```


  5. If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines: 

     * To approve them individually, run the following command for each valid CSR: 

```shell-session
$ oc adm certificate approve <csr_name>
```


where: 

`<csr_name>`
     Specifies the name of a CSR from the list of current CSRs. 

     * To approve all pending CSRs, run the following command: 

```shell-session
$ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
```


  6. After you approve all client and server CSRs, the machines have the `Ready` status. Verify this by running the following command: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME      STATUS    ROLES   AGE  VERSION
master-0  Ready     master  73m  v1.35.4
master-1  Ready     master  73m  v1.35.4
master-2  Ready     master  74m  v1.35.4
worker-0  Ready     worker  11m  v1.35.4
worker-1  Ready     worker  11m  v1.35.4
```


Note

You might need to wait a few minutes after approval of the server CSRs for the machines to reach the `Ready` status. 




## 5.1.4. Adding a new RHCOS worker node with a custom /var partition in AWS

You can add an RHCOS worker node with a custom `/var` partition in AWS by creating a user data secret and a compute machine set that use the required device naming schema. 

OpenShift Container Platform supports partitioning devices during installation by using machine configs that are processed during the bootstrap. However, if you use `/var` partitioning, the device name must be determined at installation and cannot be changed. You cannot add different instance types as nodes if they have a different device naming schema. For example, if you configured the `/var` partition with the default AWS device name for `m4.large` instances, `dev/xvdb`, you cannot directly add an AWS `m5.large` instance, as `m5.large` instances use a `/dev/nvme1n1` device by default. The device might fail to partition due to the different naming schema. 

The procedure in this section shows how to add a new Red Hat Enterprise Linux CoreOS (RHCOS) compute node with an instance that uses a different device name from what was configured at installation. You create a custom user data secret and configure a new compute machine set. These steps are specific to an AWS cluster. The principles apply to other cloud deployments also. However, the device naming schema is different for other deployments and should be determined on a per-case basis. 

**Procedure**

  1. On a command line, change to the `openshift-machine-api` namespace: 

```shell-session
$ oc project openshift-machine-api
```


  2. Create a new secret from the `worker-user-data` secret: 

     1. Export the `userData` section of the secret to a text file: 

```shell-session
$ oc get secret worker-user-data --template='{{index .data.userData | base64decode}}' | jq > userData.txt
```


     2. Edit the text file to add the `storage`, `filesystems`, and `systemd` stanzas for the partitions you want to use for the new node. You can specify any [Ignition configuration parameters](https://coreos.github.io/ignition/configuration-v3_2/) as needed. 

Note

Do not change the values in the `ignition` stanza. 

```shell-session
{
  "ignition": {
    "config": {
      "merge": [
        {
          "source": "https:...."
        }
      ]
    },
    "security": {
      "tls": {
        "certificateAuthorities": [
          {
            "source": "data:text/plain;charset=utf-8;base64,.....=="
          }
        ]
      }
    },
    "version": "3.2.0"
  },
  "storage": {
    "disks": [
      {
        "device": "/dev/nvme1n1",
        "partitions": [
          {
            "label": "var",
            "sizeMiB": 50000,
            "startMiB": 0
          }
        ]
      }
    ],
    "filesystems": [
      {
        "device": "/dev/disk/by-partlabel/var",
        "format": "xfs",
        "path": "/var"
      }
    ]
  },
  "systemd": {
    "units": [
      {
        "contents": "[Unit]\nBefore=local-fs.target\n[Mount]\nWhere=/var\nWhat=/dev/disk/by-partlabel/var\nOptions=defaults,pquota\n[Install]\nWantedBy=local-fs.target\n",
        "enabled": true,
        "name": "var.mount"
      }
    ]
  }
}
```


where: 

`device` (under `disks`)
     Specifies an absolute path to the AWS block device. 
`sizeMiB`
     Specifies the size of the data partition in Mebibytes. 
`startMiB`
     Specifies the start of the partition in Mebibytes. When adding a data partition to the boot disk, a minimum value of 25000 MB (Mebibytes) is recommended. The root file system is automatically resized to fill all available space up to the specified offset. If no value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of RHCOS might overwrite the beginning of the data partition. 
`device` (under `filesystems`)
     Specifies an absolute path to the `/var` partition. 
`format`
     Specifies the filesystem format. 
`path`
     Specifies the mount-point of the filesystem while Ignition is running relative to where the root filesystem will be mounted. This is not necessarily the same as where it should be mounted in the real root, but it is encouraged to make it the same. 
`units`
     Defines a systemd mount unit that mounts the `/dev/disk/by-partlabel/var` device to the `/var` partition. 

     3. Extract the `disableTemplating` section from the `work-user-data` secret to a text file: 

```shell-session
$ oc get secret worker-user-data --template='{{index .data.disableTemplating | base64decode}}' | jq > disableTemplating.txt
```


     4. Create the new user data secret file from the two text files. This user data secret passes the additional node partition information in the `userData.txt` file to the newly created node. 

```shell-session
$ oc create secret generic worker-user-data-x5 --from-file=userData=userData.txt --from-file=disableTemplating=disableTemplating.txt
```


  3. Create a new compute machine set for the new node: 

     1. Create a new compute machine set YAML file, similar to the following, which is configured for AWS. Add the required partitions and the newly-created user data secret: 

Tip

Use an existing compute machine set as a template and change the parameters as needed for the new node. 

```shell-session
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: auto-52-92tf4
  name: worker-us-east-2-nvme1n1
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: auto-52-92tf4
      machine.openshift.io/cluster-api-machineset: auto-52-92tf4-worker-us-east-2b
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: auto-52-92tf4
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: auto-52-92tf4-worker-us-east-2b
    spec:
      metadata: {}
      providerSpec:
        value:
          ami:
            id: ami-0c2dbd95931a
          apiVersion: awsproviderconfig.openshift.io/v1beta1
          blockDevices:
          - DeviceName: /dev/nvme1n1
            ebs:
              encrypted: true
              iops: 0
              volumeSize: 120
              volumeType: gp2
          - DeviceName: /dev/nvme1n2
            ebs:
              encrypted: true
              iops: 0
              volumeSize: 50
              volumeType: gp2
          credentialsSecret:
            name: aws-cloud-credentials
          deviceIndex: 0
          iamInstanceProfile:
            id: auto-52-92tf4-worker-profile
          instanceType: m6i.large
          kind: AWSMachineProviderConfig
          metadata:
            creationTimestamp: null
          placement:
            availabilityZone: us-east-2b
            region: us-east-2
          securityGroups:
          - filters:
            - name: tag:Name
              values:
              - auto-52-92tf4-worker-sg
          subnet:
            id: subnet-07a90e5db1
          tags:
          - name: kubernetes.io/cluster/auto-52-92tf4
            value: owned
          userDataSecret:
            name: worker-user-data-x5
```


where: 

`name`
     Specifies a name for the new node. 
`DeviceName: /dev/nvme1n1`
     Specifies an absolute path to the AWS block device, here an encrypted EBS volume. 
`DeviceName: /dev/nvme1n2`
     Optional. Specifies an additional EBS volume. 
`userDataSecret.name`
     Specifies the user data secret file. 

     2. Create the compute machine set: 

```yaml
$ oc create -f <file-name>.yaml
```


The machines might take a few moments to become available. 

  4. Verify that the new partition and nodes are created: 

     1. Verify that the compute machine set is created: 

```shell-session
$ oc get machineset
```


**Example output**

```shell-session
NAME                                               DESIRED   CURRENT   READY   AVAILABLE   AGE
ci-ln-2675bt2-76ef8-bdgsc-worker-us-east-1a        1         1         1       1           124m
ci-ln-2675bt2-76ef8-bdgsc-worker-us-east-1b        2         2         2       2           124m
worker-us-east-2-nvme1n1                           1         1         1       1           2m35s
```


The `worker-us-east-2-nvme1n1` compute machine set is the new compute machine set. 

     2. Verify that the new node is created: 

```shell-session
$ oc get nodes
```


**Example output**

```shell-session
NAME                           STATUS   ROLES    AGE     VERSION
ip-10-0-128-78.ec2.internal    Ready    worker   117m    v1.35.4
ip-10-0-146-113.ec2.internal   Ready    master   127m    v1.35.4
ip-10-0-153-35.ec2.internal    Ready    worker   118m    v1.35.4
ip-10-0-176-58.ec2.internal    Ready    master   126m    v1.35.4
ip-10-0-217-135.ec2.internal   Ready    worker   2m57s   v1.35.4
ip-10-0-225-248.ec2.internal   Ready    master   127m    v1.35.4
ip-10-0-245-59.ec2.internal    Ready    worker   116m    v1.35.4
```


The `ip-10-0-217-135.ec2.internal` node is the new node. 

     3. Verify that the custom `/var` partition is created on the new node: 

```shell-session
$ oc debug node/<node-name> -- chroot /host lsblk
```


For example: 

```shell-session
$ oc debug node/ip-10-0-217-135.ec2.internal -- chroot /host lsblk
```


**Example output**

```shell-session
NAME        MAJ:MIN  RM  SIZE RO TYPE MOUNTPOINT
nvme0n1     202:0    0   120G  0 disk
|-nvme0n1p1 202:1    0     1M  0 part
|-nvme0n1p2 202:2    0   127M  0 part
|-nvme0n1p3 202:3    0   384M  0 part /boot
`-nvme0n1p4 202:4    0 119.5G  0 part /sysroot
nvme1n1     202:16   0    50G  0 disk
`-nvme1n1p1 202:17   0  48.8G  0 part /var
```


The `nvme1n1` device is mounted to the `/var` partition. 




**Additional resources**

  * [Disk partitioning for OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installation-user-infra-machines-advanced_disk_installing-bare-metal)



Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API. 

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation. 

To view the platform type for your cluster, run the following command: 

```shell-session
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```
