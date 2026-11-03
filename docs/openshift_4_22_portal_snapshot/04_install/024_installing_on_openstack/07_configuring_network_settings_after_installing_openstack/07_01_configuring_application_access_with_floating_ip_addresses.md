# 7.1. Configuring application access with floating IP addresses

After you install OpenShift Container Platform, configure Red Hat OpenStack Platform (RHOSP) to allow application network traffic by attaching a floating IP address to the ingress port. 

Note

You do not need to perform this procedure if you provided values for `platform.openstack.apiFloatingIP` and `platform.openstack.ingressFloatingIP` in the `install-config.yaml` file, or `os_api_fip` and `os_ingress_fip` in the `inventory.yaml` playbook, during installation. The floating IP addresses are already set. 

**Prerequisites**

  * OpenShift Container Platform cluster must be installed 
  * Floating IP addresses are enabled as described in the OpenShift Container Platform on RHOSP installation documentation. 



**Procedure**

  1. Attach a floating IP address to the ingress port by completing the following commands: 

     1. Show the port by entering the following command: 

```shell-session
$ openstack port show <cluster_name>-<cluster_ID>-ingress-port
```


     2. Attach the port to the IP address by entering the following command: 

```shell-session
$ openstack floating ip set --port <ingress_port_ID> <apps_FIP>
```


  2. Add a wildcard `A` record for `*apps.` to your DNS file: 

```plaintext
*.apps.<cluster_name>.<base_domain>  IN  A  <apps_FIP>
```


Note

If you do not control the DNS server but want to enable application access for non-production purposes, you can add these hostnames to the `/etc/hosts` file: 

```plaintext
<apps_FIP> console-openshift-console.apps.<cluster name>.<base domain>
<apps_FIP> integrated-oauth-server-openshift-authentication.apps.<cluster name>.<base domain>
<apps_FIP> oauth-openshift.apps.<cluster name>.<base domain>
<apps_FIP> prometheus-k8s-openshift-monitoring.apps.<cluster name>.<base domain>
<apps_FIP> <app name>.apps.<cluster name>.<base domain>
```
