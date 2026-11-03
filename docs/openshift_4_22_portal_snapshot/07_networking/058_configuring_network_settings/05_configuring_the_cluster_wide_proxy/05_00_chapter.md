# Chapter 5. Configuring the cluster-wide proxy

To enable your OpenShift Container Platform cluster to use an HTTP or HTTPS proxy when direct internet access is denied, you can configure cluster-wide proxy settings by modifying the `Proxy` object for existing clusters or by configuring proxy settings in the `install-config.yaml` file for new clusters. 

After you enable a cluster-wide egress proxy for your cluster on a supported platform, Red Hat Enterprise Linux CoreOS (RHCOS) populates the `status.noProxy` parameter with the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your `install-config.yaml` file that exists on the supported platform. 

Note

As a postinstallation task, you can change the `networking.clusterNetwork[].cidr` value, but not the `networking.machineNetwork[].cidr` and the `networking.serviceNetwork[]` values. For more information, see "Configuring the cluster network range". 

For installations on Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Red Hat OpenStack Platform (RHOSP), the `status.noProxy` parameter is also populated with the instance metadata endpoint, `169.254.169.254`. 

**Example of values added to the`status:` segment of a `Proxy` object by RHCOS**

```yaml
apiVersion: config.openshift.io/v1
kind: Proxy
metadata:
  name: cluster
# ...
networking:
  clusterNetwork:
  - cidr: <ip_address_from_cidr>
    hostPrefix: 23
  network type: OVNKubernetes
  machineNetwork:
  - cidr: <ip_address_from_cidr>
  serviceNetwork:
  - 172.30.0.0/16
# ...
status:
  noProxy:
  - localhost
  - .cluster.local
  - .svc
  - 127.0.0.1
  - <api_server_internal_url>
# ...
```


where: 

`<ip_address_from_cidr>`
     Specifies IP address blocks from which pod IP addresses are allocated. The default value is `10.128.0.0/14` with a host prefix of `/23`. 
`<ip_address_from_cidr>`
     Specifies IP address blocks for machines. The default value is `10.0.0.0/16`. 
`<ip_address_from_cidr>`
     Specifies IP address block for services. The default value is `172.30.0.0/16`. 
`<api_server_internal_url>`
     You can find the URL of the internal API server by running the `oc get infrastructures.config.openshift.io cluster -o jsonpath='{.status.etcdDiscoveryDomain}'` command. 

Important

If node IP addresses fall outside the specified `networking.machineNetwork[].cidr` range, you must add the IP addresses to the `noProxy` field. This configuration ensures that traffic between nodes can bypass the proxy.

- [5.1. Prerequisites](05_01_prerequisites.md)
- [5.2. Enabling the cluster-wide proxy](05_02_enabling_the_cluster_wide_proxy.md)
- [5.3. Removing the cluster-wide proxy](05_03_removing_the_cluster_wide_proxy.md)
- [5.4. Verifying the cluster-wide proxy configuration](05_04_verifying_the_cluster_wide_proxy_configuration.md)
- [5.5. Additional resources](05_05_additional_resources.md)
