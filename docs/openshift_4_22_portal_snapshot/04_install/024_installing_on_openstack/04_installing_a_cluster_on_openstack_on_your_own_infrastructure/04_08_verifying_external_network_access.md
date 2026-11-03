# 4.8. Verifying external network access

The OpenShift Container Platform installation process requires external network access. You must provide an external network value to it, or deployment fails. Before you begin the process, verify that a network with the external router type exists in Red Hat OpenStack Platform (RHOSP). 

**Prerequisites**

  * [Configure OpenStack’s networking service to have DHCP agents forward instances' DNS queries](https://docs.openstack.org/neutron/rocky/admin/config-dns-res.html#case-2-dhcp-agents-forward-dns-queries-from-instances)



**Procedure**

  * Using the RHOSP CLI, verify the name and ID of the 'External' network: 

```shell-session
$ openstack network list --long -c ID -c Name -c "Router Type"
```


**Example output**

```shell-session
+--------------------------------------+----------------+-------------+
| ID                                   | Name           | Router Type |
+--------------------------------------+----------------+-------------+
| 148a8023-62a7-4672-b018-003462f8d7dc | public_network | External    |
+--------------------------------------+----------------+-------------+
```


A network with an external router type appears in the network list. If at least one does not, see [Creating a default floating IP network](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.0/html/director_installation_and_usage/performing-overcloud-post-installation-tasks#creating-a-default-floating-ip-network) and [Creating a default provider network](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.0/html/director_installation_and_usage/performing-overcloud-post-installation-tasks#creating-a-default-provider-network). 

Note

If the Neutron trunk service plugin is enabled, a trunk port is created by default. For more information, see [Neutron trunk port](https://wiki.openstack.org/wiki/Neutron/TrunkPort).
