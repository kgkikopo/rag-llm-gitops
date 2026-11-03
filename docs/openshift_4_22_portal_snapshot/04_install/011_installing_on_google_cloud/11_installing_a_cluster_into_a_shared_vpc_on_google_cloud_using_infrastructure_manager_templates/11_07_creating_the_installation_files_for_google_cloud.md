# 11.7. Creating the installation files for Google Cloud

To install OpenShift Container Platform on Google Cloud by using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use. 

You generate and customize the `install-config.yaml` file, Kubernetes manifests, and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation. 

## 11.7.1. Manually creating the installation configuration file

Installing the cluster requires that you manually create the installation configuration file. 

**Prerequisites**

  * You have an SSH public key on your local machine for use with the installation program. You can use the key for SSH authentication onto your cluster nodes for debugging and disaster recovery. 
  * You have obtained the OpenShift Container Platform installation program and the pull secret for your cluster. 



**Procedure**

  1. Create an installation directory to store your required installation assets in: 

```shell-session
$ mkdir <installation_directory>
```


Important

You must create a directory. Some installation assets, such as bootstrap X.509 certificates have short expiration intervals, so you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version. 

  2. Customize the provided sample `install-config.yaml` file template and save the file in the `<installation_directory>`. 

Note

You must name this configuration file `install-config.yaml`. 

  3. Back up the `install-config.yaml` file so that you can use it to install many clusters. 

Important

Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step. 




**Additional resources**

  * [Installation configuration parameters for Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_google_cloud/installation-config-parameters-gcp "Chapter 14. Installation configuration parameters for Google Cloud")



## 11.7.2. Enabling Shielded VMs

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


## 11.7.3. Enable Confidential VMs

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



## 11.7.4. Sample customized install-config.yaml file for Google Cloud

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters. 

Important

This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it. 

```yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    gcp:
      type: n2-standard-4
      zones:
      - us-central1-a
      - us-central1-c
      tags:
      - control-plane-tag1
      - control-plane-tag2
  replicas: 3
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    gcp:
      type: n2-standard-4
      zones:
      - us-central1-a
      - us-central1-c
      tags:
      - compute-tag1
      - compute-tag2
  replicas: 0
metadata:
  name: test-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  networkType: OVNKubernetes
  serviceNetwork:
  - 172.30.0.0/16
platform:
  gcp:
    defaultMachinePlatform:
      tags:
      - global-tag1
      - global-tag2
    projectID: openshift-production
    region: us-central1
pullSecret: '{"auths": ...}'
fips: false
sshKey: ssh-ed25519 AAAA...
publish: Internal
```


where: 

`baseDomain`
     Specifies the public DNS on the host project. 
`controlPlane`
     Specifies the parameters that apply to control plane machines. The `controlPlane` section is a single mapping. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`, and the first line of the `controlPlane` section must not. Only one control plane pool is used. If you do not provide these parameters and values, the installation program provides the default value. 
`compute`
     Specifies the parameters that apply to compute machines. The `compute` section is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`, and the first line of the `controlPlane` section must not. Although both sections currently define a single machine pool, it is possible that future versions of OpenShift Container Platform will support defining multiple compute pools during installation. If you do not provide these parameters and values, the installation program provides the default value. 
`hyperthreading`
    

Specifies whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines. 

Important

If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance. Use larger machine types, such as `n1-standard-8`, for your machines if you disable simultaneous multithreading. 

`tags`
     Specifies a set of network tags to apply to the control plane or compute machine sets. The `platform.gcp.defaultMachinePlatform.tags` parameter applies to both control plane and compute machines. If the `compute.platform.gcp.tags` or `controlPlane.platform.gcp.tags` parameters are set, they override the `platform.gcp.defaultMachinePlatform.tags` parameter. This parameter is optional. 
`networkType`
     Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value. 
`projectID`
     Specifies the main project where the VM instances reside. 
`region`
     Specifies the region that your VPC network is in. 
`fips`
    

Specifies whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead. 

Important

To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening). 

When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures. 

`sshKey`
    

Specifies the `sshKey` value that you use to access the machines in your cluster. This parameter is optional. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses. 

`publish`
     Specifies how to publish the user-facing endpoints of your cluster. Set `publish` to `Internal` to deploy a private cluster, which cannot be accessed from the internet. The default value is `External`. To use a shared VPC in a cluster that uses infrastructure that you provision, you must set `publish` to `Internal`. The installation program can no longer access the public DNS zone for the base domain in the host project. 

## 11.7.5. Configuring the cluster-wide proxy during installation

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




## 11.7.6. Creating the Kubernetes manifest and Ignition config files

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


  4. Remove the Kubernetes manifest files that define the worker machines: 

```shell-session
$ rm -f <installation_directory>/openshift/99_openshift-cluster-api_worker-machineset-*.yaml
```


Because you create and manage the worker machines yourself, you do not need to initialize these machines. 

  5. Verify that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines: 

     1. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file. 
     2. Locate the `mastersSchedulable` parameter and verify that it is set to `false`. 
     3. Save and exit the file. 

  6. Remove the `privateZone` sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file: 

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
status: {}
```


`spec.privateZone`: Remove this section completely. 

  7. Configure the cloud provider for your VPC. 

     1. Open the `<installation_directory>/manifests/cloud-provider-config.yaml` file. 
     2. Add the `network-project-id` parameter and set its value to the ID of project that hosts the shared VPC network. 
     3. Add the `network-name` parameter and set its value to the name of the shared VPC network that hosts the OpenShift Container Platform cluster. 
     4. Replace the value of the `subnetwork-name` parameter with the value of the shared VPC subnet that hosts your compute machines. 

The contents of the `<installation_directory>/manifests/cloud-provider-config.yaml` resemble the following example: 

```yaml
config: |+
  [global]
  project-id      = example-project
  regional        = true
  multizone       = true
  node-tags       = opensh-ptzzx-master
  node-tags       = opensh-ptzzx-worker
  node-instance-prefix = opensh-ptzzx
  external-instance-groups-prefix = opensh-ptzzx
  network-project-id = example-shared-vpc
  network-name    = example-network
  subnetwork-name = example-worker-subnet
```


  8. If you deploy a cluster that is not on a private network, open the `<installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml` file and replace the value of the `scope` parameter with `External`. The contents of the file resemble the following example: 

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: null
  name: default
  namespace: openshift-ingress-operator
spec:
  endpointPublishingStrategy:
    loadBalancer:
      scope: External
    type: LoadBalancerService
status:
  availableReplicas: 0
  domain: ''
  selector: ''
```


  9. To create the Ignition configuration files, run the following command from the directory that contains the installation program: 

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
