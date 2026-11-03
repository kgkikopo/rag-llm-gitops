# 4.5. Creating the installation configuration file

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



## 4.5.1. Minimum resource requirements for cluster installation

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements. 

Table 4.1. Minimum resource requirementsMachine| Operating system| vCPU| Virtual RAM| Storage| Input/Output Per Second (IOPS)  
---|---|---|---|---|---  
Bootstrap  |  RHCOS  |  4  |  16 GB  |  100 GB  |  300   
Control plane  |  RHCOS  |  4  |  16 GB  |  100 GB  |  300   
Compute  |  RHCOS  |  2  |  8 GB  |  100 GB  |  300   
Show more

  * One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs. 
  * OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance. 
  * As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines. 



Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA): 

  * x86-64 architecture requires x86-64-v2 ISA 
  * ARM64 architecture requires ARMv8.0-A ISA 
  * ppc64le architecture requires IBM® Power9 ISA 
  * s390x architecture requires IBM® z14 ISA 



For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation. 

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform. 

**Additional resources**

  * [Optimizing storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#optimizing-storage)



## 4.5.2. Tested instance types for Google Cloud

OpenShift Container Platform supports specific Google Cloud instance types that have been validated for cluster deployment. 

Note

Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) (Google documentation). 

Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see [machine series support for Hyperdisk](https://cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in _Storage_. 

See the following machine series: 

  * `A2`
  * `A3`
  * `C2`
  * `C2D`
  * `C3`
  * `C3D`
  * `C4`
  * `E2`
  * `M1`
  * `N1`
  * `N2`
  * `N2D`
  * `N4`
  * `Tau T2D`



## 4.5.3. Tested instance types for Google Cloud on 64-bit ARM infrastructures

OpenShift Container Platform supports specific Google Cloud 64-bit ARM instance types that have been validated for cluster deployment. 

See the following machine series for 64-bit ARM machines: 

  * `C4A`
  * `N4A`
  * `Tau T2A`



## 4.5.4. Using custom machine types

If the predefined Google Cloud machine types do not meet your workload requirements, you can configure a custom machine type in the `install-config.yaml` file during OpenShift Container Platform installation. 

Consider the following when using a custom machine type: 

  * Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation". 
  * The name of the custom machine type must adhere to the following syntax: 

`custom-<number_of_cpus>-<amount_of_memory_in_mb>`

For example, `custom-6-20480`. 




As part of the installation process, you specify the custom machine type in the `install-config.yaml` file. 

**Sample`install-config.yaml` file with a custom machine type**

```yaml
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  platform:
    gcp:
      type: custom-6-20480
  replicas: 2
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform:
    gcp:
      type: custom-6-20480
  replicas: 3
```


## 4.5.5. Enabling Shielded VMs

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


## 4.5.6. Enable Confidential VMs

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



## 4.5.7. Enabling a user-managed DNS

You can install a cluster with a domain name server (DNS) solution that you manage instead of the default cluster-provisioned DNS solution. As a result, you can manage the API and Ingress DNS records in your own system rather than adding the records to the DNS of the cloud. 

For example, your organization’s security policies might not allow the use of public DNS services such as Google Cloud DNS. In such scenarios, you can use your own DNS service to bypass the public DNS service and manage your own DNS for the IP addresses of the API and Ingress services. 

If you enable user-managed DNS during installation, the installation program provisions DNS records for the API and Ingress services only within the cluster. To ensure access from outside the cluster, you must provision the DNS records in an external DNS service of your choice for the API and Ingress services after installation. 

For information about provisioning your DNS records for the API server and the Ingress services, see "Provisioning your own DNS records". 

**Prerequisites**

  * You installed the `jq` package. 



**Procedure**

  * Before you deploy your cluster, use a text editor to open the `install-config.yaml` file and add the following stanza: 

    * To enable user-managed DNS: 

```yaml
platform:
  gcp:
    userProvisionedDNS: Enabled
```


where: 

`Enabled`
     Enables user-provisioned DNS management. 




**Additional resources**

  * [Additional Google Cloud configuration parameters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installation-config-parameters-gcp#installation-configuration-parameters-additional-gcp_installation-config-parameters-gcp "14.1.4. Additional Google Cloud configuration parameters")



## 4.5.8. Sample customized install-config.yaml file for Google Cloud

To specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters, you can customize the `install-config.yaml` file. 

Important

This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it. 

```yaml
apiVersion: v1
baseDomain: example.com
pullSecret: '{"auths": ...}'
controlPlane:
  name: master
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
compute:
- name: worker
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
metadata:
  name: test-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  gcp:
    projectID: sample-project
    region: us-east1
```


where: 

`controlPlane`
     Specifies parameters that apply to control plane machines. 
`compute`
     Specifies parameters that apply to compute machines. 
`networking`
     Specifies parameters that apply to the cluster networking configuration. If you do not provide networking values, the installation program provides default values. 
`platform`
     Specifies parameters that apply to the infrastructure platform that hosts the cluster. 

**Additional resources**

  * [Installation configuration parameters for GCP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installation-config-parameters-gcp "Chapter 14. Installation configuration parameters for Google Cloud")
  * [Enabling customer-managed encryption keys for a compute machine set](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/#machineset-enabling-customer-managed-encryption_creating-machineset-gcp)



## 4.5.9. Configuring the cluster-wide proxy during installation

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file. 

**Prerequisites**

  * You have an existing `install-config.yaml` file. 
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
