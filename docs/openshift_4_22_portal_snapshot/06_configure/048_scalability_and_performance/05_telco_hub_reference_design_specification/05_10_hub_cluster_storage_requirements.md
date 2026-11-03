# 5.10. Hub cluster storage requirements

The total amount of storage required by the management hub cluster is dependant on the storage requirements for each of the applications deployed on the cluster. The main components that require storage through highly available `PersistentVolume` resources are described in the following sections. 

Note

The storage required for the underlying OpenShift Container Platform installation is separate to these requirements. 

## 5.10.1. Assisted Service

The Assisted Service is deployed with the multicluster engine and Red Hat Advanced Cluster Management (RHACM). 

Note

The following numbers are estimates. Tune the values for more accurate results. Add an engineering margin, for example +20%, to the results to account for potential estimation inaccuracies. 

Table 5.2. Assisted Service storage requirementsPersistent volume resource| Size (GB)  
---|---  
`imageStorage`[1] |  30   
`filesystemStorage`[2] |  709   
`dataBaseStorage`[3] |  0.7   
Show more

[1][2] For more information, refer to the multicluster engine Operator documentation [About enabling central infrastructure management](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/clusters/cluster_mce_overview#enable-cim). 

[3] The `databaseStorage` value is an empirical estimate based on cluster topology, number of installation events, hardware profile, and configuration complexity. Based on empirical testing, estimate approximately 200 KB per host. 

**Additional resources**

  * [Enabling central infrastructure management in disconnected environments](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15/html/clusters/cluster_mce_overview#enable-cim-disconnected)



## 5.10.2. RHACM Observability

Cluster Observability is provided by the multicluster engine and Red Hat Advanced Cluster Management (RHACM). 

  * Observability storage needs several `PV` resources and an S3 compatible bucket storage for long-term retention of the metrics. 
  * Storage requirements calculation is complex and dependent on the specific workloads and characteristics of managed clusters. Requirements for `PV` resources and the S3 bucket depend on many aspects including data retention, the number of managed clusters, managed cluster workloads, and so on. 
  * Estimate the required storage for observability by using the observability sizing calculator in the RHACM capacity planning repository. See the Red Hat Knowledgebase article [Calculating storage need for MultiClusterHub Observability on telco environments](https://access.redhat.com/articles/7103886) for an explanation of using the calculator to estimate observability storage requirements. The below table uses inputs derived from the telco RAN DU RDS and the hub cluster RDS as representative values. 



The following numbers are estimates. Tune the values for more accurate results. Add an engineering margin, for example +20%, to the results to account for potential estimation inaccuracies. 

Storage resources depend on the number of replicas for each component. You can configure the sizing for the Observability stack in the `MultiClusterObservability` custom resource. The number of replicas scales with the sizing configuration. The sizing values in this specification use the default size. 

Table 5.3. Cluster requirementsCapacity planner input| Data source| Example value  
---|---|---  
Number of control plane nodes  |  Hub cluster RDS (scale) and telco RAN DU RDS (topology)  |  3500   
Number of additional worker nodes  |  Hub cluster RDS (scale) and telco RAN DU RDS (topology)  |  0   
Days for storage of data  |  Hub cluster RDS  |  15   
Total number of pods per cluster  |  Telco RAN DU RDS  |  120   
Number of namespaces (excluding OpenShift Container Platform)  |  Telco RAN DU RDS  |  4   
Number of metric samples per hour  |  Default value  |  12   
Number of hours of retention in receiver persistent volume (PV)  |  Default value  |  24   
Show more

With these input values, the sizing calculator as described in the Red Hat Knowledgebase article [Calculating storage need for MultiClusterHub Observability on telco environments](https://access.redhat.com/articles/7103886) indicates the following storage needs: 

Table 5.4. Storage requirements`alertmanager` PV| `thanos receive` PV| `thanos compact` PV  
---|---|---  
**Per replica** |  **Total** |  **Per replica** |  **Total** |  **Total**  
10 GiB  |  30 GiB  |  10 GiB  |  30 GiB  |  100 GiB   
Show more

Table 5.5. Storage requirements`thanos rule` PV| `thanos store` PV| Object bucket[1]  
---|---|---  
**Per replica** |  **Total** |  **Per replica** |  **Total** |  **Total**  
30 GiB  |  90 GiB  |  100 GiB  |  300 GiB  |  310 GiB   
Show more

[1] This value assumes downsampling is enabled. You cannot configure the object bucket size in the `MultiClusterObservability` CR. Ensure this storage capacity is available in your environment. 

## 5.10.3. Storage considerations

Storage in the OpenShift Container Platform telco hub cluster reference configuration must meet high availability, performance, and capacity requirements. 

The reference configuration uses Red Hat OpenShift Data Foundation, backed by the Local Storage Operator, for block, file, and object storage. 

Limits and requirements
    

  * Minimum OpenShift Container Platform and Red Hat Advanced Cluster Management (RHACM) limits apply 
  * High availability should be provided through a storage backend. The hub cluster reference configuration provides storage through Red Hat OpenShift Data Foundation. 
  * Object bucket storage is provided through OpenShift Data Foundation. 



Engineering considerations
    

  * Use SSD or NVMe disks with low latency and high throughput for etcd storage. 
  * You must use clean storage disks with OpenShift Data Foundation, including before a re-install procedure. See "ODF disks cleaning procedure" for further information. 
  * The storage solution for telco hub clusters is OpenShift Data Foundation. 

    * Local Storage Operator supports the storage class used by OpenShift Data Foundation to provide block, file, and object storage as needed by other components on the hub cluster. 

  * The Local Storage Operator `LocalVolume` configuration includes setting `forceWipeDevicesAndDestroyAllData: true` to support the reinstallation of hub cluster nodes where OpenShift Data Foundation has previously been used. 



**Additional resources**

  * [ODF disks cleaning procedure](https://access.redhat.com/solutions/7114870)
  * [Persistent storage overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-overview_understanding-persistent-storage)
  * [OpenShift Data Foundation architecture](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/latest/html/red_hat_openshift_data_foundation_architecture/index)
  * [Persistent storage using local volumes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-local-volume)
  * [Recommended etcd practices](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/etcd/#recommended-etcd-practices)
