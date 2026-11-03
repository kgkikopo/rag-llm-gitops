# 7.9. Manually creating the installation configuration file

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

  * [Installation configuration parameters for IBM Cloud®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_ibm_cloud/installation-config-parameters-ibm-cloud-vpc "Chapter 10. Installation configuration parameters for IBM Cloud")



## 7.9.1. Minimum resource requirements for cluster installation

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements. 

Table 7.1. Minimum resource requirementsMachine| Operating system| vCPU| Virtual RAM| Storage| Input/Output Per Second (IOPS)  
---|---|---|---|---|---  
Bootstrap  |  RHCOS  |  4  |  16 GB  |  100 GB  |  300   
Control plane  |  RHCOS  |  4  |  16 GB  |  100 GB  |  300   
Compute  |  RHCOS  |  2  |  8 GB  |  100 GB  |  300   
Show more

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



## 7.9.2. Tested instance types for IBM Cloud

Use these tested IBM Cloud® instance types to ensure compatibility when selecting machine types for your OpenShift Container Platform cluster. 

See the following machine series: 

  * `bx2-8x32`
  * `bx2d-4x16`
  * `bx3d-4x20`
  * `bx3dc-8x40`
  * `cx2-8x16`
  * `cx2d-4x8`
  * `cx3d-8x20`
  * `cx3dc-4x10`
  * `gx2-8x64x1v100`
  * `gx3-16x80x1l4`
  * `gx3d-160x1792x8h100`
  * `mx2-8x64`
  * `mx2d-4x32`
  * `mx3d-4x40`
  * `ox2-8x64`
  * `ux2d-2x56`
  * `vx2d-4x56`



## 7.9.3. Sample customized install-config.yaml file for IBM Cloud

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or change the values of the required parameters. 

Important

This sample YAML file is for reference only. You must obtain your `install-config.yaml` file by using the installation program and then change it. 

```yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    ibmcloud: {}
  replicas: 3
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    ibmcloud: {}
  replicas: 3
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
  ibmcloud:
    region: eu-gb
    resourceGroupName: eu-gb-example-cluster-rg
    networkResourceGroupName: eu-gb-example-existing-network-rg
    vpcName: eu-gb-example-network-1
    controlPlaneSubnets:
      - eu-gb-example-network-1-cp-eu-gb-1
      - eu-gb-example-network-1-cp-eu-gb-2
      - eu-gb-example-network-1-cp-eu-gb-3
    computeSubnets:
      - eu-gb-example-network-1-compute-eu-gb-1
      - eu-gb-example-network-1-compute-eu-gb-2
      - eu-gb-example-network-1-compute-eu-gb-3
credentialsMode: Manual
publish: Internal
pullSecret: '{"auths": ...}'
fips: false
sshKey: ssh-ed25519 AAAA...
```


where: 

`baseDomain`
     Specifies the base domain of your cluster. This value is required. 
`metadata.name`
     Specifies the name of your cluster. This value is required. 
`platform.ibmcloud.region`
     Specifies the IBM Cloud® region to deploy the cluster to. This value is required. 
`pullSecret`
     Specifies your pull secret. This value is required. 
`compute`
     Specifies parameters where, if you do not supply values, the installation program uses the default value. The first line of the `compute` section must begin with a hyphen, `-`. Both sections currently define a single machine pool. 
`compute.hyperthreading`
     Specifies whether to enable or disable simultaneous multithreading, also known as Hyper-Threading. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines. 
`controlPlane`
     Specifies parameters where, if you do not supply values, the installation program uses the default value. The `controlPlane` section is a single mapping, and its first line must not begin with a hyphen. Only one control plane pool is used. 
`controlPlane.hyperthreading`
    

Specifies whether to enable or disable simultaneous multithreading, also known as Hyper-Threading. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines. 

Important

If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance. Use larger machine types, such as `n1-standard-8`, for your machines if you disable simultaneous multithreading. 

`networking.clusterNetwork.cidr`
     Specifies the CIDR. The machine CIDR must contain the subnets for the compute machines and control plane machines. 
`networking.machineNetwork.cidr`
     Specifies the CIDR. The CIDR must contain the subnets defined in `platform.ibmcloud.controlPlaneSubnets` and `platform.ibmcloud.computeSubnets`. 
`networking.networkType`
     Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value. 
`platform.ibmcloud.resourceGroupName`
     Specifies the name of an existing resource group. All installer-provisioned cluster resources are deployed to this resource group. If undefined, a new resource group is created for the cluster. 
`platform.ibmcloud.networkResourceGroupName`
     Specifies the name of the resource group that contains the existing virtual private cloud (VPC). The existing VPC and subnets must be in this resource group. The cluster is installed to this VPC. 
`platform.ibmcloud.vpcName`
     Specifies the name of an existing VPC. 
`platform.ibmcloud.controlPlaneSubnets`
     Specifies the name of the existing subnets to which to deploy the control plane machines. The subnets must belong to the VPC that you specified. Specify a subnet for each availability zone in the region. 
`platform.ibmcloud.computeSubnets`
     Specifies the name of the existing subnets to which to deploy the compute machines. The subnets must belong to the VPC that you specified. Specify a subnet for each availability zone in the region. 
`publish`
     Specifies how to publish the user-facing endpoints of your cluster. Set `publish` to `Internal` to deploy a private cluster. The default value is `External`. 
`fips`
    

Specifies whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead. 

Important

When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures. 

`sshKey`
    

Specifies the SSH key to use to access the machines in your cluster. This value is optional. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses. 

## 7.9.4. Configuring the cluster-wide proxy during installation

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
