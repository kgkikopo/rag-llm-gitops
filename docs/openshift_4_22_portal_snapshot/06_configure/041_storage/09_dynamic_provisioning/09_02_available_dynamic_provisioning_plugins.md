# 9.2. Available dynamic provisioning plugins

Provisioner plugins automatically create storage resources on-demand by connecting to your cloud provider’s API. This lets you dynamically provision persistent volumes (PVs) without manual intervention, adapting to your cluster’s storage needs as they arise. 

Important

Any chosen provisioner plugin also requires configuration for the relevant cloud, host, or third-party provider as in the relevant documentation. 

Storage type| Provisioner plugin name| Notes  
---|---|---  
Red Hat OpenStack Platform (RHOSP) Cinder  |  `kubernetes.io/cinder` |   
RHOSP Manila Container Storage Interface (CSI)  |  `manila.csi.openstack.org` |  After being installed, the OpenStack Manila CSI Driver Operator and ManilaDriver automatically create the required storage classes for all available Manila share types needed for dynamic provisioning.   
Amazon Elastic Block Store (Amazon EBS)  |  `ebs.csi.aws.com` |  For dynamic provisioning when using multiple clusters in different zones, tag each node with `Key=kubernetes.io/cluster/<cluster_name>,Value=<cluster_id>` where `<cluster_name>` and `<cluster_id>` are unique per cluster.   
Azure Disk  |  `kubernetes.io/azure-disk` |   
Azure File  |  `kubernetes.io/azure-file` |  The `persistent-volume-binder` service account requires permissions to create and get secrets to store the Azure storage account and keys.   
GCE Persistent Disk (gcePD)  |  `kubernetes.io/gce-pd` |  In multi-zone configurations, it is advisable to run one OpenShift Container Platform cluster per GCE project to avoid persistent volumes (PVs) from being created in zones where no node exists in the current cluster.   
IBM Power® Virtual Server Block  |  `powervs.csi.ibm.com` |  After installation, the IBM Power® Virtual Server Block CSI Driver Operator and IBM Power® Virtual Server Block CSI Driver automatically create the required storage classes for dynamic provisioning.   
VMware vSphere  |  `kubernetes.io/vsphere-volume` |   
Show more
