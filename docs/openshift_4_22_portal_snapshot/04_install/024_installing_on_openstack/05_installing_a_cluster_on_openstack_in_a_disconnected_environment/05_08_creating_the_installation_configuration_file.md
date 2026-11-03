# 5.8. Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on Red Hat OpenStack Platform (RHOSP). 

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

        * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory. 
        * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version. 

     2. At the prompts, provide the configuration details for your cloud: 

        1. Optional: Select an SSH key to use to access your cluster machines. 

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses. 

        2. Select **openstack** as the platform to target. 
        3. Specify the Red Hat OpenStack Platform (RHOSP) external network name to use for installing the cluster. 
        4. Specify the floating IP address to use for external access to the OpenShift API. 
        5. Specify a RHOSP flavor with at least 16 GB RAM to use for control plane nodes and 8 GB RAM for compute nodes. 
        6. Select the base domain to deploy the cluster to. All DNS records will be sub-domains of this base and will also include the cluster name. 
        7. Enter a name for your cluster. The name must be 14 or fewer characters long. 

  2. In the `install-config.yaml` file, set the value of `platform.openstack.clusterOSImage` to the image location or name. For example: 

```yaml
platform:
  openstack:
      clusterOSImage: http://mirror.example.com/images/rhcos-43.81.201912131630.0-openstack.x86_64.qcow2.gz?sha256=ffebbd68e8a1f2a245ca19522c16c86f67f9ac8e4e0c1f0a812b068b16f7265d
```


  3. Edit the `install-config.yaml` file to give the additional information that is required for an installation in a restricted network. 

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

     3. Add the image content resources, which resemble the following YAML excerpt: 

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

  4. Make any other modifications to the `install-config.yaml` file that you require. 

For more information about the parameters, see "Installation configuration parameters". 

  5. Back up the `install-config.yaml` file so that you can use it to install multiple clusters. 

Important

The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now. 




**Additional resources**

  * [Installation configuration parameters for RHOSP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_openstack/installation-config-parameters-openstack "Chapter 12. Installation configuration parameters for OpenStack")



## 5.8.1. Configuring the cluster-wide proxy during installation

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




## 5.8.2. Sample customized install-config.yaml file for restricted OpenStack installations

This sample `install-config.yaml` demonstrates all of the possible Red Hat OpenStack Platform (RHOSP) customization options. 

Important

This sample file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program. 

```yaml
apiVersion: v1
baseDomain: example.com
controlPlane:
  name: master
  platform: {}
  replicas: 3
compute:
- name: worker
  platform:
    openstack:
      type: ml.large
  replicas: 3
metadata:
  name: example
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  serviceNetwork:
  - 172.30.0.0/16
  networkType: OVNKubernetes
platform:
  openstack:
    region: region1
    cloud: mycloud
    externalNetwork: external
    computeFlavor: m1.xlarge
    apiFloatingIP: 128.0.0.1
fips: false
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
additionalTrustBundle: |

  -----BEGIN CERTIFICATE-----

  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ

  -----END CERTIFICATE-----

imageContentSources:
- mirrors:
  - <mirror_registry>/<repo_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <mirror_registry>/<repo_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
```
