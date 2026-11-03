# 4.12. Creating the installation configuration file

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




You now have the file `install-config.yaml` in the directory that you specified. 

**Additional resources**

  * [Installation configuration parameters for OpenStack](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_openstack/installation-config-parameters-openstack "Chapter 12. Installation configuration parameters for OpenStack")



## 4.12.1. Custom subnets in RHOSP deployments

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

## 4.12.2. Sample customized install-config.yaml file for RHOSP

The example `install-config.yaml` files demonstrate all of the possible Red Hat OpenStack Platform (RHOSP) customization options. 

Important

This sample file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program. 

**Example 4.1. Example single stack`install-config.yaml` file**

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


**Example 4.2. Example dual stack`install-config.yaml` file**

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


## 4.12.3. Setting a custom subnet for machines

The IP range that the installation program uses by default might not match the Neutron subnet that you create when you install OpenShift Container Platform. If necessary, update the CIDR value for new machines by editing the installation configuration file. 

**Prerequisites**

  * You have the `install-config.yaml` file that was generated by the OpenShift Container Platform installation program. 
  * You have Python 3 installed. 



**Procedure**

  1. On a command line, browse to the directory that contains the `install-config.yaml` and `inventory.yaml` files. 
  2. From that directory, either run a script to edit the `install-config.yaml` file or update the file manually: 

     * To set the value by using a script, run the following command: 

```shell-session
$ python -c 'import os
import sys
import yaml
import re
re_os_net_id = re.compile(r"{{\s*os_net_id\s*}}")
os_net_id = os.getenv("OS_NET_ID")
path = "common.yaml"
facts = None
for _dict in yaml.safe_load(open(path))[0]["tasks"]:
    if "os_network" in _dict.get("set_fact", {}):
        facts = _dict["set_fact"]
        break
if not facts:
    print("Cannot find `os_network` in common.yaml file. Make sure OpenStack resource names are defined in one of the tasks.")
    sys.exit(1)
os_network = re_os_net_id.sub(os_net_id, facts["os_network"])
os_subnet = re_os_net_id.sub(os_net_id, facts["os_subnet"])
path = "install-config.yaml"
data = yaml.safe_load(open(path))
inventory = yaml.safe_load(open("inventory.yaml"))["all"]["hosts"]["localhost"]
machine_net = [{"cidr": inventory["os_subnet_range"]}]
api_vips = [inventory["os_apiVIP"]]
ingress_vips = [inventory["os_ingressVIP"]]
ctrl_plane_port = {"network": {"name": os_network}, "fixedIPs": [{"subnet": {"name": os_subnet}}]}
if inventory.get("os_subnet6_range"):
    os_subnet6 = re_os_net_id.sub(os_net_id, facts["os_subnet6"])
    machine_net.append({"cidr": inventory["os_subnet6_range"]})
    api_vips.append(inventory["os_apiVIP6"])
    ingress_vips.append(inventory["os_ingressVIP6"])
    data["networking"]["networkType"] = "OVNKubernetes"
    data["networking"]["clusterNetwork"].append({"cidr": inventory["cluster_network6_cidr"], "hostPrefix": inventory["cluster_network6_prefix"]})
    data["networking"]["serviceNetwork"].append(inventory["service_subnet6_range"])
    ctrl_plane_port["fixedIPs"].append({"subnet": {"name": os_subnet6}})
data["networking"]["machineNetwork"] = machine_net
data["platform"]["openstack"]["apiVIPs"] = api_vips
data["platform"]["openstack"]["ingressVIPs"] = ingress_vips
data["platform"]["openstack"]["controlPlanePort"] = ctrl_plane_port
del data["platform"]["openstack"]["externalDNS"]
open(path, "w").write(yaml.dump(data, default_flow_style=False))'
```


     * Where `if inventory.get("os_subnet6_range")` applies to dual stack (IPv4/IPv6) environments. 




## 4.12.4. Emptying compute machine pools

To proceed with an installation that uses your own infrastructure, set the number of compute machines in the installation configuration file to zero. Later, you create these machines manually. 

**Prerequisites**

  * You have the `install-config.yaml` file that was generated by the OpenShift Container Platform installation program. 



**Procedure**

  1. On a command line, browse to the directory that contains `install-config.yaml`. 
  2. From that directory, either run a script to edit the `install-config.yaml` file or update the file manually: 

     * To set the value by using a script, run: 

```shell-session
$ python -c '
import yaml;
path = "install-config.yaml";
data = yaml.safe_load(open(path));
data["compute"][0]["replicas"] = 0;
open(path, "w").write(yaml.dump(data, default_flow_style=False))'
```


     * To set the value manually, open the file and set the value of `compute.<first entry>.replicas` to `0`. 




## 4.12.5. Cluster deployment on RHOSP provider networks

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

**Additional resources**

  * [The RHOSP documentation](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/networking-overview_rhosp-network#tenant-provider-networks_network-overview)



### 4.12.5.1. RHOSP provider network requirements for cluster installation

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



**Additional resources**

  * [The provider networks documentation](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/networking-overview_rhosp-network#tenant-provider-networks_network-overview)
  * [role-based access control (RBAC)](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/networking_guide/config-rbac-policies_rhosp-network#proc_create-rbac-policies_config-rbac-policies)



### 4.12.5.2. Deploying a cluster that has a primary interface on a provider network

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
