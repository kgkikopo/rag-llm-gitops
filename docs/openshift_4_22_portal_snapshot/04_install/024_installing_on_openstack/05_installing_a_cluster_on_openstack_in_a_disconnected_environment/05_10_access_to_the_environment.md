# 5.10. Access to the environment

At deployment, all OpenShift Container Platform machines are created in a Red Hat OpenStack Platform (RHOSP)-tenant network. Therefore, they are not accessible directly in most RHOSP deployments. 

You can configure OpenShift Container Platform API and application access by using floating IP addresses (FIPs) during installation. You can also complete an installation without configuring FIPs, but the installer will not configure a way to reach the API or applications externally. 

## 5.10.1. Enabling access with floating IP addresses

Create floating IP (FIP) addresses for external access to the OpenShift Container Platform API and cluster applications. 

**Procedure**

  1. Using the Red Hat OpenStack Platform (RHOSP) CLI, create the API FIP: 

```shell-session
$ openstack floating ip create --description "API <cluster_name>.<base_domain>" <external_network>
```


  2. Using the Red Hat OpenStack Platform (RHOSP) CLI, create the apps, or Ingress, FIP: 

```shell-session
$ openstack floating ip create --description "Ingress <cluster_name>.<base_domain>" <external_network>
```


  3. Add records that follow these patterns to your DNS server for the API and Ingress FIPs: 

```plaintext
api.<cluster_name>.<base_domain>.  IN  A  <API_FIP>
*.apps.<cluster_name>.<base_domain>. IN  A <apps_FIP>
```


Note

If you do not control the DNS server, you can access the cluster by adding the cluster domain names such as the following to your `/etc/hosts` file: 

     * `<api_floating_ip> api.<cluster_name>.<base_domain>`
     * `<application_floating_ip> grafana-openshift-monitoring.apps.<cluster_name>.<base_domain>`
     * `<application_floating_ip> prometheus-k8s-openshift-monitoring.apps.<cluster_name>.<base_domain>`
     * `<application_floating_ip> oauth-openshift.apps.<cluster_name>.<base_domain>`
     * `<application_floating_ip> console-openshift-console.apps.<cluster_name>.<base_domain>`
     * `application_floating_ip integrated-oauth-server-openshift-authentication.apps.<cluster_name>.<base_domain>`

The cluster domain names in the `/etc/hosts` file grant access to the web console and the monitoring interface of your cluster locally. You can also use the `kubectl` or `oc`. You can access the user applications by using the additional entries pointing to the <application_floating_ip>. This action makes the API and applications accessible to only you, which is not suitable for production deployment, but does allow installation for development and testing. 

  4. Add the FIPs to the `install-config.yaml` file as the values of the following parameters: 

     * `platform.openstack.ingressFloatingIP`
     * `platform.openstack.apiFloatingIP`

If you use these values, you must also enter an external network as the value of the `platform.openstack.externalNetwork` parameter in the `install-config.yaml` file. 

Tip

You can make OpenShift Container Platform resources available outside of the cluster by assigning a floating IP address and updating your firewall configuration. 




## 5.10.2. Completing installation without floating IP addresses

You can install OpenShift Container Platform on Red Hat OpenStack Platform (RHOSP) without providing floating IP addresses. 

**Procedure**

  1. In the `install-config.yaml` file, do not define the following parameters: 

     * `platform.openstack.ingressFloatingIP`
     * `platform.openstack.apiFloatingIP`

  2. If you cannot provide an external network, you can also leave `platform.openstack.externalNetwork` blank. If you do not provide a value for `platform.openstack.externalNetwork`, a router is not created for you, and, without additional action, the installer will fail to retrieve an image from Glance. You must configure external connectivity on your own. 
  3. If you run the installer from a system that cannot reach the cluster API due to a lack of floating IP addresses or name resolution, installation fails. To prevent installation failure in these cases, you can use a proxy network or run the installer from a system that is on the same network as your machines. 

Note

You can enable name resolution by creating DNS records for the API and Ingress ports. For example: 

```plaintext
api.<cluster_name>.<base_domain>.  IN  A  <api_port_IP>
*.apps.<cluster_name>.<base_domain>. IN  A <ingress_port_IP>
```


If you do not control the DNS server, you can add the record to your `/etc/hosts` file. This action makes the API accessible to only you, which is not suitable for production deployment but does allow installation for development and testing.
