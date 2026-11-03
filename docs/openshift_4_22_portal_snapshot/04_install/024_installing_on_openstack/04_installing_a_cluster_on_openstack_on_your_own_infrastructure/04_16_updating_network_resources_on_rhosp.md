# 4.16. Updating network resources on RHOSP

Update the network resources that an OpenShift Container Platform on Red Hat OpenStack Platform (RHOSP) installation on your own infrastructure requires. 

**Prerequisites**

  * Python 3 is installed on your machine. 
  * You downloaded the modules in "Downloading playbook dependencies". 
  * You downloaded the playbooks in "Downloading the installation playbooks". 



**Procedure**

  1. Optional: Add an external network value to the `inventory.yaml` playbook: 

**Example external network value in the`inventory.yaml` Ansible Playbook**

```yaml
...
      # The public network providing connectivity to the cluster. If not
      # provided, the cluster external connectivity must be provided in another
      # way.

      # Required for os_api_fip, os_ingress_fip, os_bootstrap_fip.
      os_external_network: 'external'
...
```


Important

If you did not provide a value for `os_external_network` in the `inventory.yaml` file, you must ensure that VMs can access Glance and an external connection yourself. 

  2. Optional: Add external network and floating IP (FIP) address values to the `inventory.yaml` playbook: 

**Example FIP values in the`inventory.yaml` Ansible Playbook**

```yaml
...
      # OpenShift API floating IP address. If this value is non-empty, the
      # corresponding floating IP will be attached to the Control Plane to
      # serve the OpenShift API.
      os_api_fip: '203.0.113.23'

      # OpenShift Ingress floating IP address. If this value is non-empty, the
      # corresponding floating IP will be attached to the worker nodes to serve
      # the applications.
      os_ingress_fip: '203.0.113.19'

      # If this value is non-empty, the corresponding floating IP will be
      # attached to the bootstrap machine. This is needed for collecting logs
      # in case of install failure.
      os_bootstrap_fip: '203.0.113.20'
```


Important

If you do not define values for `os_api_fip` and `os_ingress_fip`, you must perform postinstallation network configuration. 

If you do not define a value for `os_bootstrap_fip`, the installation program cannot download debugging information from failed installations. 

See "Enabling access to the environment" for more information. 

  3. On a command line, create security groups by running the `security-groups.yaml` playbook: 

```shell-session
$ ansible-playbook -i inventory.yaml security-groups.yaml
```


  4. On a command line, update the network resources by running the `update-network-resources.yaml` playbook: 

```shell-session
$ ansible-playbook -i inventory.yaml update-network-resources.yaml
```


     * The playbook adds tags to the network, subnets, ports, and router. The playbook also attaches floating IP addresses to the API and Ingress ports and sets the security groups for those ports. 

  5. Optional: If you want to control the default resolvers that Nova servers use, run the RHOSP CLI command: 

```shell-session
$ openstack subnet set --dns-nameserver <server_1> --dns-nameserver <server_2> "$INFRA_ID-nodes"
```


  6. Optional: You can use the `inventory.yaml` file that you created to customize your installation. For example, you can deploy a cluster that uses bare-metal machines. 



## 4.16.1. Deploying a cluster with bare-metal machines

If you want your cluster to use bare-metal machines, modify the `inventory.yaml` file. Your cluster can have compute machines running on bare metal. 

Note

Be sure that your `install-config.yaml` file reflects whether the RHOSP network that you use for bare-metal workers supports floating IP addresses or not. 

**Prerequisites**

  * The Bare Metal service (Ironic) is enabled and accessible via the RHOSP Compute API. 
  * Bare metal is available as a RHOSP flavor. 
  * If your cluster runs on an RHOSP version that is more than 16.1.6 and less than 16.2.4, bare-metal workers do not function due to a [known issue](https://bugzilla.redhat.com/show_bug.cgi?id=2033953) that causes the metadata service to be unavailable for services on OpenShift Container Platform nodes. 
  * The RHOSP network supports both VM and bare-metal server attachment. 
  * If you want to deploy the machines on a pre-existing network, a RHOSP subnet is provisioned. 
  * If you want to deploy the machines on an installer-provisioned network, the RHOSP Bare Metal service (Ironic) is able to listen for and interact with Preboot eXecution Environment (PXE) boot machines that run on tenant networks. 
  * You created an `inventory.yaml` file as part of the OpenShift Container Platform installation process. 



**Procedure**

  1. In the `inventory.yaml` file, edit the flavors for machines: 

     1. Change the value of `os_flavor_worker` to a bare-metal flavor. 

**An example bare metal`inventory.yaml` file**

```yaml
all:
  hosts:
    localhost:
      ansible_connection: local
      ansible_python_interpreter: "{{ansible_playbook_python}}"

      # User-provided values
      os_subnet_range: '10.0.0.0/16'
      os_flavor_master: 'my-vm-flavor'
      os_flavor_worker: 'my-bare-metal-flavor'
      os_image_rhcos: 'rhcos'
      os_external_network: 'external'
...
```


where: 

`all.hosts.localhost.os_flavor_worker`
    

Specifies a bare-metal flavor to use for compute machines. 

Use the updated `inventory.yaml` file to complete the installation process. Machines that are created during deployment use the flavor that you added to the file. 

Note

The installation program may time out while waiting for bare-metal machines to boot. 

If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example: 

```shell-session
$ ./openshift-install wait-for install-complete --log-level debug
```


**Additional resources**

  * [Bare Metal service (Ironic)](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/bare_metal_provisioning/index)
  * [A RHOSP flavor](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/17.1/html/configuring_the_bare_metal_provisioning_service/assembly_configuring-the-bare-metal-provisioning-service-after-deployment#proc_creating-flavors-for-launching-bare-metal-instances_bare-metal-post-deployment)
