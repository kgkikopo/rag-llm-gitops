# 3.9. Creating the installation configuration file

You can customize the OpenShift Container Platform cluster you install on Red Hat OpenStack Platform (RHOSP). 

**Prerequisites**

  * You have the OpenShift Container Platform installation program and the pull secret for your cluster. 



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

  2. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section. 
  3. Back up the `install-config.yaml` file so that you can use it to install multiple clusters. 

Important

The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now. 




**Additional resources**

  * [Installation configuration parameters for RHOSP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_openstack/installation-config-parameters-openstack "Chapter 12. Installation configuration parameters for OpenStack")



## 3.9.1. Configuring the cluster-wide proxy during installation

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




## 3.9.2. Custom subnets in RHOSP deployments

Optionally, you can deploy a cluster on a Red Hat OpenStack Platform (RHOSP) subnet of your choice. The GUID of a subnet is passed as the value of `platform.openstack.machinesSubnet` in the `install-config.yaml` file. 

This subnet is used as the cluster’s primary subnet. By default, nodes and ports are created on the subnet. You can create nodes and ports on a different RHOSP subnet by setting the value of the `platform.openstack.machinesSubnet` property to the subnet’s UUID. 

Before you run the OpenShift Container Platform installer with a custom subnet, verify that your configuration meets the following requirements: 

  * The subnet that is used by `platform.openstack.machinesSubnet` has DHCP enabled. 
  * The CIDR of `platform.openstack.machinesSubnet` matches the CIDR of `networking.machineNetwork`. 
  * The installation program user has permission to create ports on this network, including ports with fixed IP addresses. 



Clusters that use custom subnets have the following limitations: 

  * If you plan to install a cluster that uses floating IP addresses, the `platform.openstack.machinesSubnet` subnet must be attached to a router that is connected to the `externalNetwork` network. 
  * If the `platform.openstack.machinesSubnet` value is set in the `install-config.yaml` file, the installation program does not create a private network or subnet for your RHOSP machines. 
  * You cannot use the `platform.openstack.externalDNS` property at the same time as a custom subnet. To add DNS to a cluster that uses a custom subnet, configure DNS on the RHOSP network. 



Note

By default, the API VIP takes x.x.x.5 and the Ingress VIP takes x.x.x.7 from your network’s CIDR block. To override these default values, set values for `platform.openstack.apiVIPs` and `platform.openstack.ingressVIPs` that are outside of the DHCP allocation pool. 

Important

The CIDR ranges for networks are not adjustable after cluster installation. Red Hat does not provide direct guidance on determining the range during cluster installation because it requires careful consideration of the number of created pods per namespace. 

## 3.9.3. Deploying a cluster with bare-metal machines

If you want your cluster to use bare-metal machines, modify the `install-config.yaml` file. Your cluster can have compute machines running on bare metal. 

Note

Be sure that your `install-config.yaml` file reflects whether the RHOSP network that you use for bare-metal workers supports floating IP addresses or not. 

**Prerequisites**

  * The Bare Metal service (Ironic) is enabled and accessible via the RHOSP Compute API. 
  * Bare metal is available as a RHOSP flavor. 
  * If your cluster runs on an RHOSP version that is more than 16.1.6 and less than 16.2.4, bare-metal workers do not function due to a [known issue](https://bugzilla.redhat.com/show_bug.cgi?id=2033953) that causes the metadata service to be unavailable for services on OpenShift Container Platform nodes. 
  * The RHOSP network supports both VM and bare-metal server attachment. 
  * If you want to deploy the machines on a pre-existing network, a RHOSP subnet is provisioned. 
  * If you want to deploy the machines on an installer-provisioned network, the RHOSP Bare Metal service (Ironic) is able to listen for and interact with Preboot eXecution Environment (PXE) boot machines that run on tenant networks. 
  * You created an `install-config.yaml` file as part of the OpenShift Container Platform installation process. 



**Procedure**

  1. In the `install-config.yaml` file, edit the flavors for machines: 

     1. Change the value of `compute.platform.openstack.type` to a bare-metal flavor. 
     2. If you want to deploy your machines on a pre-existing network, change the value of `platform.openstack.machinesSubnet` to the RHOSP subnet UUID of the network. 

**An example bare metal`install-config.yaml` file**

```yaml
compute:
  - architecture: amd64
    hyperthreading: Enabled
    name: worker
    platform:
      openstack:
        type: <bare_metal_compute_flavor>
    replicas: 3
...

platform:
    openstack:
      machinesSubnet: <subnet_UUID>
...
```


where: 

`compute.platform.openstack.type`
     Specifies a bare-metal flavor to use for compute machines. 
`platform.openstack.machinesSubnet`
    

If you want to use a pre-existing network, change this value to the UUID of the RHOSP subnet. 

Use the updated `install-config.yaml` file to complete the installation process. The compute machines that are created during deployment use the flavor that you added to the file. 

Note

The installation program may time out while waiting for bare-metal machines to boot. 

If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example: 

```shell-session
$ ./openshift-install wait-for install-complete --log-level debug
```


## 3.9.4. Cluster deployment on RHOSP provider networks

You can deploy your OpenShift Container Platform clusters on Red Hat OpenStack Platform (RHOSP) with a primary network interface on a provider network. 

Provider networks are commonly used to give projects direct access to a public network that can be used to reach the internet. You can also share provider networks among projects as part of the network creation process. 

RHOSP provider networks map directly to an existing physical network in the data center. A RHOSP administrator must create them. 

In the following example, OpenShift Container Platform workloads are connected to a data center by using a provider network: 

![A diagram that depicts four OpenShift workloads on OpenStack. Each workload is connected by its NIC to an external data center by using a provider network.](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_OpenStack-en-US/images/b49712cae2810b6700081476367769dc/openshift-on-openstack-provider-network.png) ![A diagram that depicts four OpenShift workloads on OpenStack. Each workload is connected by its NIC to an external data center by using a provider network.](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_OpenStack-en-US/images/b49712cae2810b6700081476367769dc/openshift-on-openstack-provider-network.png)

OpenShift Container Platform clusters that are installed on provider networks do not require tenant networks or floating IP addresses. The installer does not create these resources during installation. 

Example provider network types include flat (untagged) and VLAN (802.1Q tagged). 

Note

A cluster can support as many provider network connections as the network type allows. For example, VLAN networks typically support up to 4096 connections. 

You can learn more about provider and tenant networks in the RHOSP documentation. 

### 3.9.4.1. RHOSP provider network requirements for cluster installation

Before you install an OpenShift Container Platform cluster, your Red Hat OpenStack Platform (RHOSP) deployment and provider network must meet several conditions. 

These conditions are listed as follows: 

  * The [RHOSP networking service (Neutron) is enabled](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/networking-overview_rhosp-network#install-networking_network-overview) and accessible through the RHOSP networking API. 
  * The RHOSP networking service has the [port security and allowed address pairs extensions enabled](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/config-allowed-address-pairs_rhosp-network#overview-allow-addr-pairs_config-allowed-address-pairs). 
  * The provider network can be shared with other tenants. 

Tip

Use the `openstack network create` command with the `--share` flag to create a network that can be shared. 

  * The RHOSP project that you use to install the cluster must own the provider network and an appropriate subnet. 



To learn more about creating networks on RHOSP, read the provider networks documentation. 

**Procedure**

  1. To create a network for a project that is named "openshift," enter the following command: 

```shell-session
$ openstack network create --project openshift
```


  2. To create a subnet for a project that is named "openshift," enter the following command: 

```shell-session
$ openstack subnet create --project openshift
```


  3. If the cluster is owned by the `admin` user, you must run the installation program as that user to create ports on the network. 

Important

Provider networks must be owned by the RHOSP project that is used to create the cluster. If they are not, the RHOSP Compute service (Nova) cannot request a port from that network. 

  4. Verify that the provider network can reach the RHOSP metadata service IP address, which is `169.254.169.254` by default. 

Depending on your RHOSP SDN and networking service configuration, you might need to provide the route when you create the subnet. For example: 

```shell-session
$ openstack subnet create --dhcp --host-route destination=169.254.169.254/32,gateway=192.0.2.2 ...
```


  5. Optional: To secure the network, create role-based access control (RBAC) rules that limit network access to a single project. 



### 3.9.4.2. Deploying a cluster that has a primary interface on a provider network

You can deploy an OpenShift Container Platform cluster that has its primary network interface on an Red Hat OpenStack Platform (RHOSP) provider network. 

Tip

You can add additional networks, including provider networks, to the `platform.openstack.additionalNetworkIDs` list. 

After you deploy your cluster, you can attach pods to additional networks. For more information, see "Understanding multiple networks". 

**Prerequisites**

  * Your Red Hat OpenStack Platform (RHOSP) deployment is configured as described by "RHOSP provider network requirements for cluster installation". 



**Procedure**

  1. In a text editor, open the `install-config.yaml` file. 
  2. Set the value of the `platform.openstack.apiVIPs` property to the IP address for the API VIP. 
  3. Set the value of the `platform.openstack.ingressVIPs` property to the IP address for the Ingress VIP. 
  4. Set the value of the `platform.openstack.machinesSubnet` property to the UUID of the provider network subnet. 
  5. Set the value of the `networking.machineNetwork.cidr` property to the CIDR block of the provider network subnet. 

Important

The `platform.openstack.apiVIPs` and `platform.openstack.ingressVIPs` properties must both be unassigned IP addresses from the `networking.machineNetwork.cidr` block. 

**Section of an installation configuration file for a cluster that relies on a RHOSP provider network**

```yaml
        ...
        platform:
          openstack:
            apiVIPs:
              - 192.0.2.13
            ingressVIPs:
              - 192.0.2.23
            machinesSubnet: fa806b2f-ac49-4bce-b9db-124bc64209bf
            # ...
        networking:
          machineNetwork:
          - cidr: 192.0.2.0/24
```


     * In OpenShift Container Platform 4.12 and later, the `apiVIP` and `ingressVIP` configuration settings are deprecated. Instead, use a list format to enter values in the `apiVIPs` and `ingressVIPs` configuration settings. 

Warning

You cannot set the `platform.openstack.externalNetwork` or `platform.openstack.externalDNS` parameters while using a provider network for the primary network interface. 

When you deploy the cluster, the installer uses the `install-config.yaml` file to deploy the cluster on the provider network. 




**Additional resources**

  * [Understanding multiple networks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/multiple_networks/#understanding-multiple-networks)



## 3.9.5. Sample customized install-config.yaml file for RHOSP

The example `install-config.yaml` files demonstrate all of the possible Red Hat OpenStack Platform (RHOSP) customization options. 

Important

This sample file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program. 

**Example 3.1. Example single stack`install-config.yaml` file**

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
    cloud: mycloud
    externalNetwork: external
    computeFlavor: m1.xlarge
    apiFloatingIP: 128.0.0.1
fips: false
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
```


**Example 3.2. Example dual stack`install-config.yaml` file**

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
  - cidr: fd01::/48
    hostPrefix: 64
  machineNetwork:
  - cidr: 192.168.25.0/24
  - cidr: fd2e:6f44:5dd8:c956::/64
  serviceNetwork:
  - 172.30.0.0/16
  - fd02::/112
  networkType: OVNKubernetes
platform:
  openstack:
    cloud: mycloud
    externalNetwork: external
    computeFlavor: m1.xlarge
    apiVIPs:
    - 192.168.25.10
    - fd2e:6f44:5dd8:c956:f816:3eff:fec3:5955
    ingressVIPs:
    - 192.168.25.132
    - fd2e:6f44:5dd8:c956:f816:3eff:fe40:aecb
    controlPlanePort:
      fixedIPs:
      - subnet:
          name: openshift-dual4
      - subnet:
          name: openshift-dual6
      network:
        name: openshift-dual
fips: false
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
```


## 3.9.6. Configuring a cluster with dual-stack networking

Deploy a cluster with both IPv4 and IPv6 addressing on Red Hat OpenStack Platform (RHOSP). From RHOSP 17.1, you can use single-stack IPv6 infrastructure while the cluster provides internal IPv4 connectivity. 

You can create a dual-stack cluster on RHOSP. 

For RHOSP 17.1, you can deploy a dual-stack OpenShift Container Platform cluster on a single-stack IPv6 RHOSP infrastructure. The OpenShift Container Platform cluster offers IPv4 connectivity internally, even when the underlying RHOSP network only has IPv6 subnets. 

For earlier versions of RHOSP, you can enable the dual-stack configuration only if you are using an RHOSP network with IPv4 and IPv6 subnets. 

Note

RHOSP does not support the conversion of an IPv4 single-stack cluster to a dual-stack cluster network. 

### 3.9.6.1. Deploying the dual-stack cluster

Create dual-stack networks and VIPs, then edit the `install-config.yaml` file to deploy an cluster with both IPv4 and IPv6 addressing on Red Hat OpenStack Platform (RHOSP). 

**Procedure**

  1. Create a network with the required subnets: 

     * For RHOSP 17.1, you can create a network with an IPv6 subnet. The OpenShift Container Platform cluster offers IPv4 connectivity internally. In the `install-config.yaml` file, you specify both IPv4 and IPv6 subnets in the `controlPlanePort.fixedIPs` section. 
     * For earlier versions of RHOSP, create a network with both IPv4 and IPv6 subnets. 

The available address modes for the `ipv6-ra-mode` and `ipv6-address-mode` fields are: `dhcpv6-stateful`, `dhcpv6-stateless`, and `slaac`. 

Note

The dual-stack network MTU must accommodate both the minimum MTU for IPv6, which is 1280, and the OVN-Kubernetes encapsulation requirement, which is 100 bytes. 

Note

DHCP must be enabled on the subnets. 

  2. Create the API and Ingress VIPs ports. 
  3. Add the IPv6 subnet to the router to enable router advertisements. If you are using a provider network, you can enable router advertisements by adding the network as an external gateway, which also enables external connectivity. 
  4. To configure IPv4 and IPv6 address endpoints for cluster nodes, edit the `install-config.yaml` file. The following is an example of an `install-config.yaml` file: 

**Example`install-config.yaml`**

```yaml
apiVersion: v1
baseDomain: mydomain.test
compute:
- name: worker
  platform:
    openstack:
      type: m1.xlarge
  replicas: 3
controlPlane:
  name: master
  platform:
    openstack:
      type: m1.xlarge
  replicas: 3
metadata:
  name: mycluster
networking:
  machineNetwork:
  - cidr: "192.168.25.0/24"
  - cidr: "fd2e:6f44:5dd8:c956::/64"
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  - cidr: fd01::/48
    hostPrefix: 64
  serviceNetwork:
  - 172.30.0.0/16
  - fd02::/112
platform:
  openstack:
    ingressVIPs: ['192.168.25.79', 'fd2e:6f44:5dd8:c956:f816:3eff:fef1:1bad']
    apiVIPs: ['192.168.25.199', 'fd2e:6f44:5dd8:c956:f816:3eff:fe78:cf36']
    controlPlanePort:
      fixedIPs:
      - subnet:
          name: subnet-v4
          id: subnet-v4-id
      - subnet:
          name: subnet-v6
          id: subnet-v6-id
      network:
        name: dualstack
        id: network-id
```


     * `networking.machineNetwork`, `networking.clusterNetwork`, and `networking.serviceNetwork` specify IP address ranges for both the IPv4 and IPv6 address families. For RHOSP 17.1 deployments on single-stack IPv6 infrastructure, the OpenShift Container Platform cluster offers IPv4 connectivity internally. 
     * `platform.openstack.ingressVIPs` specifies the virtual IP (VIP) address endpoints for the Ingress VIP services to give an interface to the cluster. 
     * `platform.openstack.apiVIPs` specifies the virtual IP (VIP) address endpoints for the API VIP services to give an interface to the cluster. 
     * `platform.openstack.controlPlanePort` specifies the dual-stack network details that all the nodes across the cluster use. 
     * `platform.openstack.controlPlanePort.fixedIPs` specifies the subnets for the control plane port. The CIDR of any subnet specified in this field must match the CIDRs listed on `networking.machineNetwork`. 
     * `platform.openstack.controlPlanePort.fixedIPs[].subnet` specifies each subnet. You can specify a value for either `name` or `id`, or both. 
     * `platform.openstack.controlPlanePort.network` specifies the network. Specifying the `network` under the `controlPlanePort` field is optional. 

Note

For RHOSP 17.1 deployments on single-stack IPv6 infrastructure, you can deploy a dual-stack OpenShift Container Platform cluster. In the `install-config.yaml` file, specify both IPv4 and IPv6 address ranges for the cluster and service networks. The OpenShift Container Platform cluster offers IPv4 connectivity internally, even though the underlying RHOSP network only has IPv6 subnets. In the `controlPlanePort.fixedIPs` section, specify both the IPv4 and IPv6 subnets. 

Alternatively, if you want an IPv6 primary dual-stack cluster, edit the `install-config.yaml` file following the example below: 

**Example`install-config.yaml`**

```yaml
apiVersion: v1
baseDomain: mydomain.test
compute:
- name: worker
  platform:
    openstack:
      type: m1.xlarge
  replicas: 3
controlPlane:
  name: master
  platform:
    openstack:
      type: m1.xlarge
  replicas: 3
metadata:
  name: mycluster
networking:
  machineNetwork:
  - cidr: "fd2e:6f44:5dd8:c956::/64"
  - cidr: "192.168.25.0/24"
  clusterNetwork:
  - cidr: fd01::/48
    hostPrefix: 64
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  serviceNetwork:
  - fd02::/112
  - 172.30.0.0/16
platform:
  openstack:
    ingressVIPs: ['fd2e:6f44:5dd8:c956:f816:3eff:fef1:1bad', '192.168.25.79']
    apiVIPs: ['fd2e:6f44:5dd8:c956:f816:3eff:fe78:cf36', '192.168.25.199']
    controlPlanePort:
      fixedIPs:
      - subnet:
          name: subnet-v6
          id: subnet-v6-id
      - subnet:
          name: subnet-v4
          id: subnet-v4-id
      network:
        name: dualstack
        id: network-id
```


     * `networking.machineNetwork`, `networking.clusterNetwork`, and `networking.serviceNetwork` specify IP address ranges for both the IPv4 and IPv6 address families. For RHOSP 17.1 deployments on single-stack IPv6 infrastructure, the OpenShift Container Platform cluster offers IPv4 connectivity internally. 
     * `platform.openstack.ingressVIPs` specifies the virtual IP (VIP) address endpoints for the Ingress VIP services to give an interface to the cluster. 
     * `platform.openstack.apiVIPs` specifies the virtual IP (VIP) address endpoints for the API VIP services to give an interface to the cluster. 
     * `platform.openstack.controlPlanePort` specifies the dual-stack network details that all the nodes across the cluster use. 
     * `platform.openstack.controlPlanePort.fixedIPs` specifies the subnets for the control plane port. The CIDR of any subnet specified in this field must match the CIDRs listed on `networking.machineNetwork`. 
     * `platform.openstack.controlPlanePort.fixedIPs[].subnet` specifies each subnet. You can specify a value for either `name` or `id`, or both. 
     * `platform.openstack.controlPlanePort.network` specifies the network. Specifying the `network` under the `controlPlanePort` field is optional. 

Note

When using an installation host in an isolated dual-stack network, the IPv6 address might not be reassigned correctly upon reboot. 

To resolve this problem on Red Hat Enterprise Linux (RHEL) 8, create a file called `/etc/NetworkManager/system-connections/required-rhel8-ipv6.conf` that has the following configuration: 

```plaintext
[connection]
type=ethernet
[ipv6]
addr-gen-mode=eui64
method=auto
```


To resolve this problem on RHEL 9, create a file called `/etc/NetworkManager/conf.d/required-rhel9-ipv6.conf` that has the following configuration: 

```plaintext
[connection]
ipv6.addr-gen-mode=0
```


After you create and edit the file, reboot the installation host. 

Note

The `ip=dhcp,dhcp6` kernel argument, which is set on all of the nodes, results in a single Network Manager connection profile that activates on many interfaces simultaneously. Because of this behavior, any additional network has the same connection enforced with the same UUID. If you need an interface-specific configuration, create a new connection profile for that interface so that the default connection is no longer enforced on it. 




## 3.9.7. Configuring a cluster with single-stack IPv6 networking

Create API and Ingress VIP ports and configure the `install-config.yaml` file to deploy a cluster with IPv6-only networking on Red Hat OpenStack Platform (RHOSP). 

You can create a single-stack IPv6 cluster on Red Hat OpenStack Platform (RHOSP) after you configure your RHOSP deployment. 

Note

For RHOSP 17.1, you can also deploy a dual-stack OpenShift Container Platform cluster on a single-stack IPv6 RHOSP infrastructure. The OpenShift Container Platform cluster offers IPv4 connectivity internally, even when the underlying RHOSP network only has IPv6 subnets. 

Important

You cannot convert a dual-stack cluster into a single-stack IPv6 cluster. 

**Prerequisites**

  * Your RHOSP deployment has an existing network with a DHCPv6-stateful IPv6 subnet to use as the machine network. 
  * DNS is configured for the existing IPv6 subnet. 
  * The IPv6 subnet is added to a RHOSP router, and the router is configured to send router advertisements (RAs). 
  * You added any additional IPv6 subnets that are used in the cluster to an RHOSP router to enable router advertisements. 

Note

Using an IPv6 SLAAC subnet is not supported because any `dns_nameservers` addresses are not enforced by RHOSP Neutron. 

  * You have a mirror registry with an IPv6 interface. 
  * The RHOSP network accepts a minimum MTU size of 1442 bytes. 
  * You created API and ingress virtual IP addresses (VIPs) as RHOSP ports on the machine network and included those addresses in the `install-config.yaml` file. 



**Procedure**

  1. Create the API VIP port on the network by running the following command: 

```bash
$ openstack port create api --network <v6_machine_network>
```


  2. Create the Ingress VIP port on the network by running the following command: 

```bash
$ openstack port create ingress --network <v6_machine_network>
```


  3. After the networking resources are pre-created, deploy a cluster by using an `install-config.yaml` file that reflects your IPv6 network configuration. As an example: 

```yaml
apiVersion: v1
baseDomain: mydomain.test
compute:
- name: worker
  platform:
    openstack:
      type: m1.xlarge
  replicas: 3
controlPlane:
  name: master
  platform:
    openstack:
      type: m1.xlarge
  replicas: 3
metadata:
  name: mycluster
networking:
  machineNetwork:
  - cidr: "fd2e:6f44:5dd8:c956::/64"
  clusterNetwork:
  - cidr: fd01::/48
    hostPrefix: 64
  serviceNetwork:
  - fd02::/112
platform:
  openstack:
    ingressVIPs: ['fd2e:6f44:5dd8:c956::383']
    apiVIPs: ['fd2e:6f44:5dd8:c956::9a']
    controlPlanePort:
      fixedIPs:
      - subnet:
          name: subnet-v6
      network:
        name: v6-network
imageContentSources:
- mirrors:
  - <mirror>
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
- mirrors:
  - <mirror>
  source: registry.ci.openshift.org/ocp/release
additionalTrustBundle: |
<certificate_of_the_mirror>
```


     * `networking.machineNetwork` specifies the CIDR of the subnet. The CIDR of the subnet specified in this field must match the CIDR of the subnet that is specified in the `controlPlanePort` section. 
     * `platform.openstack.ingressVIPs` and `platform.openstack.apiVIPs` specify the virtual IP addresses. Use the address from the ports you generated in the earlier steps as the values for these parameters. 
     * `platform.openstack.controlPlanePort.fixedIPs` and `platform.openstack.controlPlanePort.network` specify the control plane port configuration. Items under these keys can contain an ID, a name, or both. 
     * `imageContentSources` specifies the mirror details. For more information on configuring a local image registry, see "Creating a mirror registry with mirror registry for Red Hat OpenShift". 




**Additional resources**

  * [Creating a mirror registry with mirror registry for Red Hat OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installing-mirroring-creating-registry)



## 3.9.8. Installation configuration for a cluster on OpenStack with a user-managed load balancer

The example `install-config.yaml` file demonstrates how to configure a cluster that uses an external, user-managed load balancer rather than the default internal load balancer. 

```yaml
apiVersion: v1
baseDomain: mydomain.test
compute:
- name: worker
  platform:
    openstack:
      type: m1.xlarge
  replicas: 3
controlPlane:
  name: master
  platform:
    openstack:
      type: m1.xlarge
  replicas: 3
metadata:
  name: mycluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 192.168.10.0/24
platform:
  openstack:
    cloud: mycloud
    machinesSubnet: 8586bf1a-cc3c-4d40-bdf6-c243decc603a
    apiVIPs:
    - 192.168.10.5
    ingressVIPs:
    - 192.168.10.7
    loadBalancer:
      type: UserManaged
```


where: 

`platform.openstack.machineSubnet`
     Regardless of which load balancer you use, the load balancer is deployed to this subnet. 
`platform.openstack.loadBalancer.type`
     Specifies the `UserManaged` value, which indicates that you are using a user-managed load balancer.
