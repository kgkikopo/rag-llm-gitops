# 2.2. Creating SR-IOV networks for compute machines

If your Red Hat OpenStack Platform (RHOSP) deployment supports single root I/O virtualization (SR-IOV), you can provision SR-IOV networks that compute machines run on. 

You must configure your RHOSP platform before you install a cluster that uses SR-IOV on the platform. 

Note

The procedure uses an example of creating an external flat network and an external VLAN-based network that can be attached to a compute machine. Depending on your RHOSP deployment, other network types might be required. 

**Prerequisites**

  * Your cluster supports SR-IOV. 

Note

If you are unsure about what your cluster supports, review the OpenShift Container Platform SR-IOV hardware networks documentation. 

  * You created radio and uplink provider networks as part of your RHOSP deployment. The names `radio` and `uplink` are used in all example commands to represent these networks. 



**Procedure**

  1. On a command line, create a radio RHOSP network: 

```shell-session
$ openstack network create radio --provider-physical-network radio --provider-network-type flat --external
```


  2. Create an uplink RHOSP network: 

```shell-session
$ openstack network create uplink --provider-physical-network uplink --provider-network-type vlan --external
```


  3. Create a subnet for the radio network: 

```shell-session
$ openstack subnet create --network radio --subnet-range <radio_network_subnet_range> radio
```


  4. Create a subnet for the uplink network: 

```shell-session
$ openstack subnet create --network uplink --subnet-range <uplink_network_subnet_range> uplink
```


**Additional resources**

  * [Planning an SR-IOV deployment](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html-single/network_functions_virtualization_planning_and_configuration_guide/index#assembly_sriov_parameters)
