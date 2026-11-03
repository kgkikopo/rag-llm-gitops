# 7.7. Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on 

**Prerequisites**

  * You have the OpenShift Container Platform installation program and the pull secret for your cluster. For a restricted network installation, these files are on your mirror host. 
  * You have the `imageContentSources` values that were generated during mirror registry creation. 
  * You have obtained the contents of the certificate for your mirror registry. 
  * You have retrieved a Red Hat Enterprise Linux CoreOS (RHCOS) image and uploaded it to an accessible location. 



**Procedure**

  1. Create the `install-config.yaml` file. 

     1. Change to the directory that contains the installation program and run the following command: 

```shell-session
$ ./openshift-install create install-config --dir <installation_directory>
```


        * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates. 

When specifying the directory: 

        * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version. 

Note

Always delete the `~/.powervs` directory to avoid reusing a stale configuration. Run the following command: 

```shell-session
$ rm -rf ~/.powervs
```


     2. At the prompts, provide the configuration details for your cloud: 

        1. Optional: Select an SSH key to use to access your cluster machines. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses. 

        2. Select **powervs** as the platform to target. 
        3. Select the region to deploy the cluster to. 
        4. Select the zone to deploy the cluster to. 
        5. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster. 
        6. Enter a descriptive name for your cluster. 

  2. Edit the `install-config.yaml` file to give the additional information that is required for an installation in a restricted network. 

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

     3. Define the network for the VPC to install the cluster in under the parent `platform.powervs` field: 

```yaml
vpcName: <existing_vpc>
```


For `platform.powervs.vpcName`, specify the name for the existing IBM Cloud® VPC. 

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


For these values, use the `imageContentSources` that you recorded during mirror registry creation. 

     5. Optionally, set the publishing strategy to `Internal`: 

```yaml
publish: Internal
```


By setting this option, you create an internal Ingress Controller and a private load balancer. 

  3. Make any other modifications to the `install-config.yaml` file that you require. 

For more information about the parameters, see "Installation configuration parameters". 

  4. Back up the `install-config.yaml` file so that you can use it to install multiple clusters. 

Important

The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now. 




**Additional resources**

  * [Installation configuration parameters for IBM Power® Virtual Server](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_ibm_power_virtual_server/installation-config-parameters-ibm-power-vs "Chapter 9. Installation configuration parameters for IBM Power Virtual Server")



## 7.7.1. Minimum resource requirements for cluster installation

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements. 

Table 7.1. Minimum resource requirementsMachine| Operating system| vCPU| Virtual RAM| Storage| Input/Output Per Second (IOPS)  
---|---|---|---|---|---  
Bootstrap  |  RHCOS  |  2  |  16 GB  |  100 GB  |  300   
Control plane  |  RHCOS  |  2  |  16 GB  |  100 GB  |  300   
Compute  |  RHCOS  |  2  |  8 GB  |  100 GB  |  300   
Show more

  * One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs. 
  * OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance. 



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



## 7.7.2. Sample customized install-config.yaml file for IBM Power Virtual Server

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or change the values of the required parameters. 

Important

This sample YAML file is for reference only. You must obtain your `install-config.yaml` file by using the installation program and change it. 

```yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
  hyperthreading: Enabled
  name: master
  platform:
    powervs:
      smtLevel: 8
  replicas: 3
compute:
- hyperthreading: Enabled
  name: worker
  platform:
    powervs:
      smtLevel: 8
    ibmcloud: {}
  replicas: 3
metadata:
  name: example-restricted-cluster-name
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  networkType: OVNKubernetes
  serviceNetwork:
  - 192.168.0.0/24
platform:
  powervs:
    userid: ibm-user-id
    powervsResourceGroup: "ibmcloud-resource-group"
    region: "powervs-region"
    vpcRegion: "vpc-region"
    vpcName: name-of-existing-vpc
    zone: "powervs-zone"
    serviceInstanceID: "service-instance-id"
publish: Internal
credentialsMode: Manual
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
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
     Specifies the base domain of the cluster. This value is required. 
`metadata.name`
     Specifies the name of the cluster. This value is required. 
`compute`
     Specifies parameters where, if you do not provide values, the installation program provides the default value. The first line of the `compute` section must begin with a hyphen, `-`. 
`compute.hyperthreading`
     Specifies whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines. 
`compute.platform.powervs.smtLevel`
     Specifies the level of SMT to set to the compute machines. The supported values are 1, 2, 4, 8, `'off'`, and `'on'`. The default value is 8. The smtLevel `'off'` sets SMT to off, and smtLevel `'on'` sets SMT to the default value 8 on the cluster nodes. 
`controlPlane`
     Specifies parameters where, if you do not provide values, the installation program provides the default value. The `controlPlane` section is a single mapping, and its first line must not begin with a hyphen. Only one control plane pool is used. 
`controlPlane.hyperthreading`
    

Specifies whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines. 

Important

When multithreading (SMT) is disabled, each vCPU is equivalent to one physical core. Disable SMT only if you have specific requirements. 

`controlPlane.platform.powervs.smtLevel`
    

Specifies the level of SMT to set to the control plane. The supported values are 1, 2, 4, 8, `'off'`, and `'on'`. The default value is 8. The smtLevel `'off'` sets SMT to off, and smtLevel `'on'` sets SMT to the default value 8 on the cluster nodes. 

Note

When simultaneous multithreading (SMT) is not enabled, one vCPU is equivalent to one physical core. When enabled, total vCPUs is computed as (Thread(s) per core * Core(s) per socket) * Socket(s). The smtLevel controls the threads per core. Lower SMT levels may require additional assigned cores when deploying the cluster nodes. You can do this by setting the `'processors'` parameter in the `install-config.yaml` file to an appropriate value to meet the requirements for deploying OpenShift Container Platform successfully. 

`networking.clusterNetwork.cidr`
     Specifies the CIDR. The machine CIDR must contain the subnets for the compute machines and control plane machines. 
`networking.machineNetwork.cidr`
     Specifies the CIDR. The CIDR must contain the subnets defined in `platform.ibmcloud.controlPlaneSubnets` and `platform.ibmcloud.computeSubnets`. 
`networking.networkType`
     Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value. 
`platform.powervs.powervsResourceGroup`
     Specifies the name of an existing resource group. The existing VPC and subnets should be in this resource group. The cluster is deployed to this resource group. 
`platform.powervs.vpcName`
     Specifies the name of an existing VPC. 
`pullSecret`
     Specifies the pull secret for your mirror registry. For `<local_registry>`, specify the registry domain name, and optionally the port, that your mirror registry uses to serve content. For example, registry.example.com or registry.example.com:5000. For `<credentials>`, specify the base64-encoded user name and password for your mirror registry. 
`sshKey`
    

Specifies the SSH key to use to access the machines in your cluster. This value is optional. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses. 

`additionalTrustBundle`
     Specifies the contents of the certificate file that you used for your mirror registry. 
`imageContentSources`
     Specifies the `imageContentSources` section from the output of the command to mirror the repository. 

## 7.7.3. Configuring the cluster-wide proxy during installation

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
