# 5.8. Hub cluster networking

The reference hub cluster is designed to operate in a disconnected networking environment where direct access to the internet is not possible. 

As with all OpenShift Container Platform clusters, the hub cluster requires access to an image registry hosting all OpenShift and Day 2 Operator Lifecycle Manager (OLM) images. 

The hub cluster supports dual-stack networking support for IPv6 and IPv4 networks. IPv6 is typical in edge or far-edge network segments, while IPv4 is more prevalent for use with legacy equipment in the data center. 

Limits and requirements
    

  * Regardless of the installation method, you must configure the following network types for the hub cluster: 

    * `clusterNetwork`
    * `serviceNetwork`
    * `machineNetwork`

  * You must configure the following IP addresses for the hub cluster: 

    * `apiVIP`
    * `ingressVIP`




Note

For the above networking configurations, some values are required, or can be auto-assigned, depending on the chosen architecture and DHCP configuration. 

  * You must use the default OpenShift Container Platform network provider OVN-Kubernetes. 
  * Networking between the managed cluster and hub cluster must meet the networking requirements in the Red Hat Advanced Cluster Management (RHACM) documentation, for example: 

    * Hub cluster access to managed cluster API service, Ironic Python agent, and baseboard management controller (BMC) port. 
    * Managed cluster access to hub cluster API service, ingress IP and control plane node IP addresses. 
    * Managed cluster BMC access to hub cluster control plane node IP addresses. 

  * An image registry must be accessible throughout the lifetime of the hub cluster. 

    * All required container images must be mirrored to the disconnected registry. All OpenShift Container Platform releases and OLM Operator release images needed in your deployment must be mirrored to the registry. You can see example mirroring configuration in the `imageset-config.yaml` resource. You must update this example YAML to include your required versions. For deploying clusters, you can only use `ClusterImageSet` CRs that reference mirrored versions. 
    * The hub cluster must be configured to use a disconnected registry. 
    * The hub cluster cannot host its own image registry. For example, the registry must be available in a scenario where a power failure affects all cluster nodes. 




Engineering considerations
    

  * When deploying a hub cluster, ensure you define appropriately sized CIDR range definitions. 
  * In OpenShift Container Platform 4.22 and later, pulling OpenShift images from a disconnected mirror registry requires copying the image signatures into that registry during the mirroring process. The `oc adm mirror` command does not mirror signatures and must not be used. Instead, use the `oc mirror` plugin v2 to ensure signatures are properly mirrored. 



**Additional resources**

  * [Mirroring images for a disconnected installation by using the oc-mirror plugin v2](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#about-installing-oc-mirror-v2)
  * [Installing a cluster in a disconnected environment](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installing-disconnected-environments)
  * [Using Operator Lifecycle Manager on restricted networks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#olm-restricted-networks)
  * [Configuring the hub cluster to use a disconnected mirror registry](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/edge_computing/#ztp-configuring-the-cluster-for-a-disconnected-environment_ztp-preparing-the-hub-cluster)
  * [CIDR range definitions](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_overview/#cidr-range-definitions)
  * [Installing OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#ocp-installation-overview)
  * [Networking in OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_overview/#understanding-networking)
  * [Networking in RHACM](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html-single/networking/index)
  * [Network configuration in RHACM](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/clusters/cluster_mce_overview#mce-network-configuration)
