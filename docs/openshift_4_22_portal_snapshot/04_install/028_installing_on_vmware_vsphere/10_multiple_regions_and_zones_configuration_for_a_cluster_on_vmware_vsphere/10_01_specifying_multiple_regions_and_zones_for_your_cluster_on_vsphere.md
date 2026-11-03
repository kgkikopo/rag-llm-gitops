# 10.1. Specifying multiple regions and zones for your cluster on vSphere

You can configure the `infrastructures.config.openshift.io` configuration resource to specify multiple regions and zones for your OpenShift Container Platform cluster that runs on a VMware vSphere instance. 

Topology-aware features for the cloud controller manager and the vSphere Container Storage Interface (CSI) Operator Driver require information about the vSphere topology where you host your OpenShift Container Platform cluster. This topology information exists in the `infrastructures.config.openshift.io` configuration resource. 

Before you specify regions and zones for your cluster, you must ensure that all data centers and compute clusters contain tags, so that the cloud provider can add labels to your node. For example, if `data-center-1` represents `region-a` and `compute-cluster-1` represents `zone-1`, the cloud provider adds an `openshift-region` category label with a value of `region-a` to `data-center-1`. Additionally, the cloud provider adds an `openshift-zone` category tag with a value of `zone-1` to `compute-cluster-1`. 

Note

You can migrate control plane nodes with vMotion capabilities to a failure domain. After you add these nodes to a failure domain, the cloud provider adds `topology.kubernetes.io/zone` and `topology.kubernetes.io/region` labels to these nodes. 

**Prerequisites**

  * You created the `openshift-region` and `openshift-zone` tag categories on the vCenter server. 
  * You ensured that each data center and compute cluster contains tags that represent the name of their associated region or zone, or both. 
  * Optional: If you defined **API** and **Ingress** static IP addresses to the installation program, you must ensure that all regions and zones share a common layer 2 network. This configuration ensures that API and Ingress Virtual IP (VIP) addresses can interact with your cluster. 



Important

If you do not supply tags to all data centers and compute clusters before you create a node or migrate a node, the cloud provider cannot add the `topology.kubernetes.io/zone` and `topology.kubernetes.io/region` labels to the node. This means that services cannot route traffic to your node. 

**Procedure**

  1. Edit the `infrastructures.config.openshift.io` custom resource definition (CRD) of your cluster to specify multiple regions and zones in the `failureDomains` section of the resource by running the following command: 

```shell-session
$ oc edit infrastructures.config.openshift.io cluster
```


The following example shows an `infrastructures.config.openshift.io` CRD for an instance named `cluster` with multiple regions and zones defined in its configuration: 

```yaml
spec:
  cloudConfig:
    key: config
    name: cloud-provider-config
  platformSpec:
    type: vSphere
    vsphere:
      vcenters:
        - datacenters:
            - <region_a_data_center>
            - <region_b_data_center>
          port: 443
          server: <your_vcenter_server>
      failureDomains:
        - name: <failure_domain_1>
          region: <region_a>
          zone: <zone_a>
          server: <your_vcenter_server>
          topology:
            datacenter: <region_a_dc>
            computeCluster: "</region_a_dc/host/zone_a_cluster>"
            resourcePool: "</region_a_dc/host/zone_a_cluster/Resources/resource_pool>"
            datastore: "</region_a_dc/datastore/datastore_a>"
            networks:
            - port-group
        - name: <failure_domain_2>
          region: <region_a>
          zone: <zone_b>
          server: <your_vcenter_server>
          topology:
            computeCluster: </region_a_dc/host/zone_b_cluster>
            datacenter: <region_a_dc>
            datastore: </region_a_dc/datastore/datastore_a>
            networks:
            - port-group
        - name: <failure_domain_3>
          region: <region_b>
          zone: <zone_a>
          server: <your_vcenter_server>
          topology:
            computeCluster: </region_b_dc/host/zone_a_cluster>
            datacenter: <region_b_dc>
            datastore: </region_b_dc/datastore/datastore_b>
            networks:
            - port-group
      nodeNetworking:
        external: {}
        internal: {}
```


Important

After you create a failure domain and you define it in a CRD for a VMware vSphere cluster, you must not modify or delete the failure domain. Doing any of these actions with this configuration can impact the availability and fault tolerance of a control plane machine. 

  2. Save the resource file to apply the changes. 



**Additional resources**

  * [Parameters for the cluster-wide infrastructure CRD](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_vmware_vsphere/post-install-vsphere-zones-regions-configuration#references-regions-zones-infrastructure-vsphere_post-install-vsphere-zones-regions-configuration "10.3. Parameters for the cluster-wide infrastructure CRD")
