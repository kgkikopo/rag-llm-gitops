# 8.7. Manually creating the installation configuration file

Installing the cluster requires that you manually create the installation configuration file. 

**Prerequisites**

  * You have obtained the OpenShift Container Platform installation program and the pull secret for your cluster. 
  * You have the `imageContentSourcePolicy.yaml` file that was created when you mirrored your registry. 
  * You have obtained the contents of the certificate for your mirror registry. 



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

When customizing the sample template, be sure to provide the information that is required for an installation in a restricted network: 

     1. Update the `pullSecret` value to contain the authentication information for your registry: 

```yaml
pullSecret: '{"auths":{"<mirror_host_name>:5000": {"auth": "<credentials>","email": "you@example.com"}}}'
```


For `<mirror_host_name>`, specify the registry domain name that you specified in the certificate for your mirror registry, and for `<credentials>`, specify the base64-encoded user name and password for your mirror registry. 

     2. Add the `additionalTrustBundle` parameter and value. 

```yaml
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
```


The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority, or the self-signed certificate that you generated for the mirror registry. 

     3. Define the network and subnets for the VPC to install the cluster in under the parent `platform.ibmcloud` field: 

```yaml
vpcName: <existing_vpc>
controlPlaneSubnets: <control_plane_subnet>
computeSubnets: <compute_subnet>
```


For `platform.ibmcloud.vpcName`, specify the name for the existing IBM Cloud Virtual Private Cloud (VPC) network. For `platform.ibmcloud.controlPlaneSubnets` and `platform.ibmcloud.computeSubnets`, specify the existing subnets to deploy the control plane machines and compute machines, respectively. 

     4. Add the image content resources, which resemble the following YAML excerpt: 

```yaml
imageContentSources:
- mirrors:
  - <mirror_host_name>:5000/<repo_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <mirror_host_name>:5000/<repo_name>/release
  source: registry.redhat.io/ocp/release
```


For these values, use the `imageContentSourcePolicy.yaml` file that was created when you mirrored the registry. 

     5. If network restrictions limit the use of public endpoints to access the required IBM Cloud® services, add the `serviceEndpoints` stanza to `platform.ibmcloud` to specify an alternate service endpoint. 

Note

You can specify only one alternate service endpoint for each service. 

**Example of using alternate services endpoints**

```yaml
# ...
serviceEndpoints:
  - name: IAM
    url: <iam_alternate_endpoint_url>
  - name: VPC
    url: <vpc_alternate_endpoint_url>
  - name: ResourceController
    url: <resource_controller_alternate_endpoint_url>
  - name: ResourceManager
    url: <resource_manager_alternate_endpoint_url>
  - name: DNSServices
    url: <dns_services_alternate_endpoint_url>
  - name: COS
    url: <cos_alternate_endpoint_url>
  - name: GlobalSearch
    url: <global_search_alternate_endpoint_url>
  - name: GlobalTagging
    url: <global_tagging_alternate_endpoint_url>
# ...
```


     6. Optional: Set the publishing strategy to `Internal`: 

```yaml
publish: Internal
```


By setting this option, you create an internal Ingress Controller and a private load balancer. 

Note

If you use the default value of `External`, your network must be able to access the public endpoint for IBM Cloud® Internet Services (CIS). CIS is not enabled for Virtual Private Endpoints. 

  3. Back up the `install-config.yaml` file so that you can use it to install many clusters. 

Important

Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step. 




## 8.7.1. Configuring the cluster-wide proxy during installation

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




**Additional resources**

  * [Installation configuration parameters for IBM Cloud®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_ibm_cloud/installation-config-parameters-ibm-cloud-vpc "Chapter 10. Installation configuration parameters for IBM Cloud")



## 8.7.2. Minimum resource requirements for cluster installation

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements. 

Table 8.1. Minimum resource requirementsMachine| Operating system| vCPU| Virtual RAM| Storage| Input/Output Per Second (IOPS)  
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

## 8.7.3. Tested instance types for IBM Cloud

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



## 8.7.4. Sample customized install-config.yaml file for IBM Cloud

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
    region: us-east
    resourceGroupName: us-east-example-cluster-rg
    serviceEndpoints:
      - name: IAM
        url: https://private.us-east.iam.cloud.ibm.com
      - name: VPC
        url: https://us-east.private.iaas.cloud.ibm.com/v1
      - name: ResourceController
        url: https://private.us-east.resource-controller.cloud.ibm.com
      - name: ResourceManager
        url: https://private.us-east.resource-controller.cloud.ibm.com
      - name: DNSServices
        url: https://api.private.dns-svcs.cloud.ibm.com/v1
      - name: COS
        url: https://s3.direct.us-east.cloud-object-storage.appdomain.cloud
      - name: GlobalSearch
        url: https://api.private.global-search-tagging.cloud.ibm.com
      - name: GlobalTagging
        url: https://tags.private.global-search-tagging.cloud.ibm.com
    networkResourceGroupName: us-east-example-existing-network-rg
    vpcName: us-east-example-network-1
    controlPlaneSubnets:
      - us-east-example-network-1-cp-us-east-1
      - us-east-example-network-1-cp-us-east-2
      - us-east-example-network-1-cp-us-east-3
    computeSubnets:
      - us-east-example-network-1-compute-us-east-1
      - us-east-example-network-1-compute-us-east-2
      - us-east-example-network-1-compute-us-east-3
credentialsMode: Manual
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
fips: false
sshKey: ssh-ed25519 AAAA...
additionalTrustBundle: |
    -----BEGIN CERTIFICATE-----
    <MY_TRUSTED_CA_CERT>
    -----END CERTIFICATE-----
imageContentSources:
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
```


where: 

`baseDomain`
     Specifies the base domain of your cluster. This value is required. 
`metadata.name`
     Specifies the name of your cluster. This value is required. 
`platform.ibmcloud.region`
     Specifies the IBM Cloud® region to deploy the cluster to. This value is required. 
`pullSecret`
     Specifies the pull secret for your mirror registry. For `<local_registry>`, specify the registry domain name, and optionally the port, that your mirror registry uses to serve content. For example, `registry.example.com` or `registry.example.com:5000`. For `<credentials>`, specify the base64-encoded user name and password for your mirror registry. 
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
`platform.ibmcloud.serviceEndpoints`
     Specifies alternate service endpoints based on the network restrictions of the VPC. This overrides the default public endpoint for the service. 
`platform.ibmcloud.networkResourceGroupName`
     Specifies the name of the resource group that contains the existing virtual private cloud (VPC). The existing VPC and subnets must be in this resource group. The cluster is installed to this VPC. 
`platform.ibmcloud.vpcName`
     Specifies the name of an existing VPC. 
`platform.ibmcloud.controlPlaneSubnets`
     Specifies the name of the existing subnets to which to deploy the control plane machines. The subnets must belong to the VPC that you specified. Specify a subnet for each availability zone in the region. 
`platform.ibmcloud.computeSubnets`
     Specifies the name of the existing subnets to which to deploy the compute machines. The subnets must belong to the VPC that you specified. Specify a subnet for each availability zone in the region. 
`fips`
    

Specifies whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead. 

Important

The use of FIPS Validated or Modules in Process cryptographic libraries is only supported on OpenShift Container Platform deployments on the `x86_64` architecture. 

`sshKey`
     Specifies the SSH key to use to access the machines in your cluster. This value is optional. 
`additionalTrustBundle`
     Specifies the contents of the certificate file that you used for your mirror registry. 
`imageContentSources`
    

Specifies the values from the `metadata.name: release-0` section of the `imageContentSourcePolicy.yaml` file that was created when you mirrored the registry. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
