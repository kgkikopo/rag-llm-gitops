# 3.7. Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on Nutanix. 

**Prerequisites**

  * You have the OpenShift Container Platform installation program and the pull secret for your cluster. 
  * You have verified that you have met the Nutanix networking requirements. For more information, see "Preparing to install on Nutanix". 



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

        2. Select **nutanix** as the platform to target. 
        3. Enter the Prism Central domain name or IP address. 
        4. Enter the port that is used to log into Prism Central. 
        5. Enter the credentials that are used to log into Prism Central. 

The installation program connects to Prism Central. 

        6. Select the Prism Element that will manage the OpenShift Container Platform cluster. 
        7. Select the network subnet to use. 
        8. Enter the virtual IP address that you configured for control plane API access. 
        9. Enter the virtual IP address that you configured for cluster ingress. 
        10. Enter the base domain. This base domain must be the same one that you configured in the DNS records. 
        11. Enter a descriptive name for your cluster. 

The cluster name you enter must match the cluster name you specified when configuring the DNS records. 

  2. Optional: Update one or more of the default configuration parameters in the `install.config.yaml` file to customize the installation. 

For more information about the parameters, see "Installation configuration parameters". 

Note

If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that cluster’s control planes are schedulable. For more information, see "Installing a three-node cluster on Nutanix". 

  3. Back up the `install-config.yaml` file so that you can use it to install multiple clusters. 

Important

The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now. 




**Additional resources**

  * [Installation configuration parameters for Nutanix](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_nutanix/installation-config-parameters-nutanix "Chapter 7. Installation configuration parameters for Nutanix")



## 3.7.1. Sample customized install-config.yaml file for Nutanix

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters. 

Important

This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it. 

```yaml
apiVersion: v1
baseDomain: example.com
compute:
- hyperthreading: Enabled
  name: worker
  replicas: 3
  platform:
    nutanix:
      cpus: 2
      coresPerSocket: 2
      memoryMiB: 8196
      osDisk:
        diskSizeGiB: 120
      categories:
      - key: <category_key_name>
        value: <category_value>
controlPlane:
  hyperthreading: Enabled
  name: master
  replicas: 3
  platform:
    nutanix:
      cpus: 4
      coresPerSocket: 2
      memoryMiB: 16384
      osDisk:
        diskSizeGiB: 120
      categories:
      - key: <category_key_name>
        value: <category_value>
metadata:
  creationTimestamp: null
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
  nutanix:
    apiVIPs:
      - 10.40.142.7
    defaultMachinePlatform:
      bootType: Legacy
      categories:
      - key: <category_key_name>
        value: <category_value>
      project:
        type: name
        name: <project_name>
    ingressVIPs:
      - 10.40.142.8
    prismCentral:
      endpoint:
        address: your.prismcentral.domainname
        port: 9440
      password: <password>
      username: <username>
    prismElements:
    - endpoint:
        address: your.prismelement.domainname
        port: 9440
      uuid: 0005b0f1-8f43-a0f2-02b7-3cecef193712
    subnetUUIDs:
    - c7938dc6-7659-453e-a688-e26020c68e43
    clusterOSImage: http://example.com/images/rhcos-47.83.202103221318-0-nutanix.x86_64.qcow2
credentialsMode: Manual
publish: External
pullSecret: '{"auths": ...}'
fips: false
sshKey: ssh-ed25519 AAAA...
```


The installation program prompts you for the values of `baseDomain`, `metadata.name`, `platform.nutanix.apiVIPs`, `platform.nutanix.ingressVIPs`, `platform.nutanix.prismCentral.endpoint.address`, `platform.nutanix.prismCentral.endpoint.port`, `platform.nutanix.prismCentral.password`, `platform.nutanix.prismCentral.username`, and `pullSecret`. 

where: 

`compute`
     The `compute` section is a sequence of mappings. The first line of the `compute` section must begin with a hyphen, `-`. Although this section currently defines a single machine pool, it is possible that future versions of OpenShift Container Platform will support defining multiple compute pools during installation. 
`hyperthreading`
    

Whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines. 

Important

If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance. 

`platform.nutanix`
     Optional: Provide additional configuration for the machine pool parameters for the compute and control plane machines. 
`categories`
     Optional: Provide one or more pairs of a prism category key and a prism category value. These category key-value pairs must exist in Prism Central. You can provide separate categories to compute machines, control plane machines, or all machines. 
`controlPlane`
     The `controlPlane` section is a single mapping. The first line of the `controlPlane` section must not begin with a hyphen. Only one control plane pool is used. 
`networkType`
     The cluster network plugin to install. The default value `OVNKubernetes` is the only supported value. 
`project`
     Optional: Specify a project with which VMs are associated. Specify either `name` or `uuid` for the project type, and then provide the corresponding UUID or project name. You can associate projects to compute machines, control plane machines, or all machines. 
`<password>`
     Required. The installation program prompts you for this value. 
`<username>`
     Required. The installation program prompts you for this value. 
`clusterOSImage`
     Optional: By default, the installation program downloads and installs the Red Hat Enterprise Linux CoreOS (RHCOS) image. If Prism Central does not have internet access, you can override the default behavior by hosting the RHCOS image on any HTTP server and pointing the installation program to the image. 
`fips`
    

Whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead. 

Important

When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86_64, ppc64le, and s390x architectures. 

`sshKey`
    

Optional: You can provide the `sshKey` value that you use to access the machines in your cluster. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses. 

## 3.7.2. Configuring failure domains

Failure domains improve the fault tolerance of an OpenShift Container Platform cluster by distributing control plane and compute machines across multiple Nutanix Prism Elements (clusters). 

Tip

It is recommended that you configure three failure domains to ensure high-availability. 

**Prerequisites**

  * You have an installation configuration file (`install-config.yaml`). 



**Procedure**

  1. Edit the `install-config.yaml` file and add the following stanza to configure the first failure domain: 

```yaml
apiVersion: v1
baseDomain: example.com
compute:
# ...
platform:
  nutanix:
    failureDomains:
    - name: <failure_domain_name>
      prismElement:
        name: <prism_element_name>
        uuid: <prism_element_uuid>
      subnetUUIDs:
      - <network_uuid>
# ...
```


where: 

`<failure_domain_name>`
     Specifies a unique name for the failure domain. The name is limited to 64 or fewer characters, which can include lower-case letters, digits, and a dash (`-`). The dash cannot be in the leading or ending position of the name. 
`<prism_element_name>`
     Optional. Specifies the name of the Prism Element. 
`<prism_element_uuid`>
     Specifies the UUID of the Prism Element. 
`<network_uuid`>
     Specifies the one or more UUIDs of the Prism Element subnet objects. Among them, one of the subnet’s IP address prefixes (CIDRs) must contain the virtual IP addresses that the OpenShift Container Platform cluster uses. A maximum of 32 subnets for each failure domain (Prism Element) in an OpenShift Container Platform cluster is supported. All `subnetUUID` values must be unique. 

  2. As required, configure additional failure domains. 
  3. To distribute control plane and compute machines across the failure domains, do one of the following: 

     * If compute and control plane machines can share the same set of failure domains, add the failure domain names under the cluster’s default machine configuration. 

**Example of control plane and compute machines sharing a set of failure domains**

```yaml
apiVersion: v1
baseDomain: example.com
compute:
# ...
platform:
  nutanix:
    defaultMachinePlatform:
      failureDomains:
        - failure-domain-1
        - failure-domain-2
        - failure-domain-3
# ...
```


     * If compute and control plane machines must use different failure domains, add the failure domain names under the respective machine pools. 

**Example of control plane and compute machines using different failure domains**

```yaml
apiVersion: v1
baseDomain: example.com
compute:
# ...
controlPlane:
  platform:
    nutanix:
      failureDomains:
        - failure-domain-1
        - failure-domain-2
        - failure-domain-3
# ...
compute:
  platform:
    nutanix:
      failureDomains:
        - failure-domain-1
        - failure-domain-2
# ...
```


  4. Save the file. 



## 3.7.3. Configuring the cluster-wide proxy during installation

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
