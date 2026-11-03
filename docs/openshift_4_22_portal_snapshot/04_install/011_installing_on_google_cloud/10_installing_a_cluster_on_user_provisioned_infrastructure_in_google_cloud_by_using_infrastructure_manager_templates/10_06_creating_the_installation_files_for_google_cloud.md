# 10.6. Creating the installation files for Google Cloud

To install OpenShift Container Platform on Google Cloud by using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use. 

You generate and customize the `install-config.yaml` file, Kubernetes manifests, and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation. 

## 10.6.1. Creating a separate /var partition

To isolate growing storage for containers, etcd, or logs, you can optionally create a separate `/var` partition on worker nodes before you generate Ignition configs. 

It is recommended that disk partitioning for OpenShift Container Platform be left to the installation program. However, there are cases where you might want to create separate partitions in a part of the filesystem that you expect to grow. 

OpenShift Container Platform supports the addition of a single partition to attach storage to either the `/var` partition or a subdirectory of `/var`. For example: 

  * `/var/lib/containers`: Holds container-related content that can grow as more images and containers are added to a system. 
  * `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage. 
  * `/var`: Holds data that you might want to keep separate for purposes such as auditing. 



Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date and keep that data intact. With this method, you will not have to pull all your containers again, nor will you have to copy massive log files when you update systems. 

Because `/var` must be in place before a fresh installation of Red Hat Enterprise Linux CoreOS (RHCOS), the following procedure sets up the separate `/var` partition by creating a machine config manifest that is inserted during the `openshift-install` preparation phases of an OpenShift Container Platform installation. 

Important

If you follow the steps to create a separate `/var` partition in this procedure, it is not necessary to create the Kubernetes manifest and Ignition config files again as described later in this section. 

**Procedure**

  1. Create a directory to hold the OpenShift Container Platform installation files: 

```shell-session
$ mkdir $HOME/clusterconfig
```


  2. Run `openshift-install` to create a set of files in the `manifest` and `openshift` subdirectories. Answer the system questions as you are prompted: 

```shell-session
$ openshift-install create manifests --dir $HOME/clusterconfig
```


**Example output**

```shell-session
? SSH Public Key ...
INFO Credentials loaded from the "myprofile" profile in file "/home/myuser/.aws/credentials"
INFO Consuming Install Config from target directory
INFO Manifests created in: $HOME/clusterconfig/manifests and $HOME/clusterconfig/openshift
```


  3. Optional: Confirm that the installation program created manifests in the `clusterconfig/openshift` directory: 

```shell-session
$ ls $HOME/clusterconfig/openshift/
```


**Example output**

```shell-session
99_kubeadmin-password-secret.yaml
99_openshift-cluster-api_master-machines-0.yaml
99_openshift-cluster-api_master-machines-1.yaml
99_openshift-cluster-api_master-machines-2.yaml
...
```


  4. Create a Butane config that configures the additional partition. For example, name the file `$HOME/clusterconfig/98-var-partition.bu`, change the disk device name to the name of the storage device on the `worker` systems, and set the storage size as appropriate. This example places the `/var` directory on a separate partition: 

```yaml
variant: openshift
version: 4.22.0
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 98-var-partition
storage:
  disks:
  - device: /dev/disk/by-id/<device_name>
    partitions:
    - label: var
      start_mib: <partition_start_offset>
      size_mib: <partition_size>
      number: 5
  filesystems:
    - device: /dev/disk/by-partlabel/var
      path: /var
      format: xfs
      mount_options: [defaults, prjquota]
      with_mount_unit: true
```


where: 

`<device_name>`
     Specifies the storage device name of the disk that you want to partition. 
`<partition_start_offset>`
     Specifies the `start_mib` parameter. When adding a data partition to the boot disk, a minimum value of 25000 MiB (Mebibytes) is recommended. The root file system is automatically resized to fill all available space up to the specified offset. If no value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of RHCOS might overwrite the beginning of the data partition. 
`<partition_size>`
     Specifies the size of the data partition in mebibytes. 
`storage.filesystems.mount_options`
    

The `prjquota` mount option must be enabled for filesystems used for container storage. 

Note

When creating a separate `/var` partition, you cannot use different instance types for worker nodes, if the different instance types do not have the same device name. 

  5. Create a manifest from the Butane config and save it to the `clusterconfig/openshift` directory. For example, run the following command: 

```shell-session
$ butane $HOME/clusterconfig/98-var-partition.bu -o $HOME/clusterconfig/openshift/98-var-partition.yaml
```


  6. Run `openshift-install` again to create Ignition configs from a set of files in the `manifest` and `openshift` subdirectories: 

```shell-session
$ openshift-install create ignition-configs --dir $HOME/clusterconfig
```


```shell-session
$ ls $HOME/clusterconfig/
auth  bootstrap.ign  master.ign  metadata.json  worker.ign
```


You can now use the Ignition config files as input to the installation procedures to install Red Hat Enterprise Linux CoreOS (RHCOS) systems. 




## 10.6.2. Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on Google Cloud. 

**Prerequisites**

  * You have the OpenShift Container Platform installation program and the pull secret for your cluster. 
  * Configure a Google Cloud account. 



**Procedure**

  1. Create the `install-config.yaml` file. 

     1. Change to the directory that contains the installation program and run the following command: 

```shell-session
$ ./openshift-install create install-config --dir <installation_directory>
```


        * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates. 

When specifying the directory: 

        * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory. 
        * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version. 

     2. At the prompts, provide the configuration details for your cloud: 

        1. Optional: Select an SSH key to use to access your cluster machines. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses. 

        2. Select **gcp** as the platform to target. 
        3. If you have not configured the service account key for your Google Cloud account on your computer, you must obtain it from Google Cloud and paste the contents of the file or enter the absolute path to the file. 
        4. Select the project ID to provision the cluster in. The default value is specified by the service account that you configured. 
        5. Select the region to deploy the cluster to. 
        6. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster. 
        7. Enter a descriptive name for your cluster. 

  2. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section. 

Note

If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that the cluster’s control planes are schedulable. For more information, see "Installing a three-node cluster on Google Cloud". 

  3. Back up the `install-config.yaml` file so that you can use it to install multiple clusters. 

Important

The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now. 




**Additional resources**

  * [Installation configuration parameters for Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installation-config-parameters-gcp "Chapter 14. Installation configuration parameters for Google Cloud")



## 10.6.3. Enabling Shielded VMs

You can use Shielded VMs when installing your OpenShift Container Platform cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. 

For more information, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm). 

Note

Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures. 

**Procedure**

  * Use a text editor to edit the `install-config.yaml` file before deploying your cluster and add one of the following stanzas: 

    1. To use shielded VMs for only control plane machines: 

```yaml
controlPlane:
  platform:
    gcp:
       secureBoot: Enabled
```


    2. To use shielded VMs for only compute machines: 

```yaml
compute:
- platform:
    gcp:
       secureBoot: Enabled
```


    3. To use shielded VMs for all machines: 

```yaml
platform:
  gcp:
    defaultMachinePlatform:
       secureBoot: Enabled
```


## 10.6.4. Enable Confidential VMs

You can use Confidential VMs when installing your OpenShift Container Platform cluster. Confidential VMs encrypt data during processing. 

For more information, see Google’s documentation on [Confidential Computing](https://cloud.google.com/confidential-computing). You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other. 

Note

Confidential VMs are currently not supported on 64-bit ARM architectures. 

**Procedure**

  * Use a text editor to edit the `install-config.yaml` file before deploying your cluster and add one of the following stanzas: 

    1. To use confidential VMs for only control plane machines: 

```yaml
controlPlane:
  platform:
    gcp:
       confidentialCompute: AMDEncryptedVirtualizationNestedPaging
       type: n2d-standard-8
       onHostMaintenance: Terminate
```


where: 

`confidentialCompute`
     Enables confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional Google Cloud configuration parameters". 
`type`
     Specifies a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see [Supported operating systems and machine types](https://cloud.google.com/compute/confidential-vm/docs/os-and-machine-type#machine-type). 
`onHostMaintenance`
     Specifies the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration. 

    2. To use confidential VMs for only compute machines: 

```yaml
compute:
- platform:
    gcp:
       confidentialCompute: AMDEncryptedVirtualizationNestedPaging
       type: n2d-standard-8
       onHostMaintenance: Terminate
```


    3. To use confidential VMs for all machines: 

```yaml
platform:
  gcp:
    defaultMachinePlatform:
       confidentialCompute: AMDEncryptedVirtualizationNestedPaging
       type: n2d-standard-8
       onHostMaintenance: Terminate
```


**Additional resources**

  * [Additional Google Cloud configuration parameters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installation-config-parameters-gcp#installation-configuration-parameters-additional-gcp_installation-config-parameters-gcp "14.1.4. Additional Google Cloud configuration parameters")



## 10.6.5. Configuring the cluster-wide proxy during installation

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file. 

**Prerequisites**

  * You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, the proxy handles all cluster egress traffic, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object’s `spec.noProxy` field to bypass the proxy if necessary. 

Note

The `Proxy` object `status.noProxy` field includes the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration. 

For installations on Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Red Hat OpenStack Platform (RHOSP), the `Proxy` object `status.noProxy` field also includes the instance metadata endpoint (`169.254.169.254`). 




**Procedure**

  1. Edit your `install-config.yaml` file and add the proxy settings. For example: 

```yaml
apiVersion: v1
baseDomain: my.domain.com
proxy:
  httpProxy: http://<username>:<pswd>@<ip>:<port>
  httpsProxy: https://<username>:<pswd>@<ip>:<port>
  noProxy: example.com
additionalTrustBundle: |
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
additionalTrustBundlePolicy: <policy_to_add_additionalTrustBundle>
# ...
```


where: 

`proxy.httpProxy`
     Specifies a proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`. 
`proxy.httpsProxy`
     Specifies a proxy URL to use for creating HTTPS connections outside the cluster. 
`proxy.noProxy`
     Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations. 
`additionalTrustBundle`
     If you specify this value, the installation program generates a config map named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you specify `additionalTrustBundle` and at least one proxy setting, the `Proxy` object references the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the RHCOS trust bundle. You must set the `additionalTrustBundle` field unless an authority from the RHCOS trust bundle signs the proxy’s identity certificate. 
`additionalTrustBundlePolicy`
    

Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when you configure an `http/https` proxy. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter. 

Note

The installation program does not support the proxy `readinessEndpoints` field. 

Note

If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example: 

```shell-session
$ ./openshift-install wait-for install-complete --log-level debug
```


  2. Save the file and reference it when installing OpenShift Container Platform. 

The installation program creates a cluster-wide proxy named `cluster` that uses the proxy settings in the `install-config.yaml` file. If you do not give proxy settings, the installation program still creates a `cluster` `Proxy` object, but it has a nil `spec`. 

Note

Only the `Proxy` object named `cluster` is supported, and you cannot create additional proxies. 




## 10.6.6. Creating the Kubernetes manifest and Ignition config files

Because you manually provision infrastructure, you must generate the Kubernetes manifest and Ignition config files that the cluster requires. 

The installation program converts the installation configuration into Kubernetes manifests and then wraps them into Ignition configuration files. You use these Ignition files to configure the cluster machines. 

Important

  * The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which the system then renews. If you shut down the cluster before the system renews the certificates and you later restart the cluster after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for _Recovering from expired control plane certificates_ for more information. 
  * Use Ignition config files within 12 hours after you generate them, because the 24-hour certificate rotates from 16 to 22 hours after you install the cluster. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation. 



**Procedure**

  1. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster: 

```shell-session
$ ./openshift-install create manifests --dir <installation_directory>
```


where: 

`<installation_directory>`
     Specifies the installation directory that contains the `install-config.yaml` file you created. 

  2. Remove the Kubernetes manifest files that define the control plane machines: 

```shell-session
$ rm -f <installation_directory>/openshift/99_openshift-cluster-api_master-machines-*.yaml
```


By removing these files, you prevent the cluster from automatically generating control plane machines. 

  3. Remove the Kubernetes manifest files that define the control plane machine set: 

```shell-session
$ rm -f <installation_directory>/openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
```


  4. Optional: If you do not want the cluster to provision compute machines, remove the Kubernetes manifest files that define the worker machines: 

```shell-session
$ rm -f <installation_directory>/openshift/99_openshift-cluster-api_worker-machineset-*.yaml
```


Important

If you disabled the `MachineAPI` capability when installing a cluster on user-provisioned infrastructure, you must remove the Kubernetes manifest files that define the worker machines. Otherwise, your cluster fails to install. 

Because you create and manage the worker machines yourself, you do not need to initialize these machines. 

Warning

If you are installing a three-node cluster, skip the following step to allow the control plane nodes to be schedulable. 

Important

When you configure control plane nodes from the default unschedulable to schedulable, you require additional subscriptions because control plane nodes then become compute nodes. 

  5. Verify that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines: 

     1. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file. 
     2. Locate the `mastersSchedulable` parameter and verify that it is set to `false`. 
     3. Save and exit the file. 

  6. Optional: If you do not want [the Ingress Operator](https://github.com/openshift/cluster-ingress-operator) to create DNS records on your behalf, remove the `privateZone` and `publicZone` sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file: 

```yaml
apiVersion: config.openshift.io/v1
kind: DNS
metadata:
  creationTimestamp: null
  name: cluster
spec:
  baseDomain: example.openshift.com
  privateZone:
    id: mycluster-100419-private-zone
  publicZone:
    id: example.openshift.com
status: {}
```


`spec.privateZone`: Remove this section completely. 

If you do so, you must add ingress DNS records manually in a later step. 

  7. To create the Ignition configuration files, run the following command from the directory that contains the installation program: 

```shell-session
$ ./openshift-install create ignition-configs --dir <installation_directory>
```


where: 

`<installation_directory>`
    

Specifies the same installation directory. 

The installation program creates Ignition config files for the bootstrap, control plane, and compute nodes in the installation directory. The program also creates the `kubeadmin-password` and `kubeconfig` files in the `./<installation_directory>/auth` directory: 

```plaintext
.
├── auth
│   ├── kubeadmin-password
│   └── kubeconfig
├── bootstrap.ign
├── master.ign
├── metadata.json
└── worker.ign
```


**Additional resources**

  * [Adding the ingress DNS records](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installing-gcp-user-infra#installation-gcp-user-infra-adding-ingress_installing-gcp-user-infra "10.25. Adding the ingress DNS records")
