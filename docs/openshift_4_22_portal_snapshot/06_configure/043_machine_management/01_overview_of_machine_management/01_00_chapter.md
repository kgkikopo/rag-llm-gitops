# Chapter 1. Overview of machine management

You can use machine management to flexibly work with underlying infrastructure such as Amazon Web Services (AWS), Microsoft Azure, Google Cloud, Red Hat OpenStack Platform (RHOSP), and VMware vSphere to manage the OpenShift Container Platform cluster. You can control the cluster and perform auto-scaling, such as scaling up and down the cluster based on specific workload policies. 

It is important to have a cluster that adapts to changing workloads. The OpenShift Container Platform cluster can horizontally scale up and down when the load increases or decreases. 

Machine management is implemented as a custom resource definition (CRD). A CRD object defines a new unique object `Kind` in the cluster and enables the Kubernetes API server to handle the object’s entire lifecycle. 

The Machine API Operator provisions the following resources: 

  * `MachineSet`
  * `Machine`
  * `ClusterAutoscaler`
  * `MachineAutoscaler`
  * `MachineHealthCheck`

- [1.1. Machine API overview](01_01_machine_api_overview.md)
- [1.2. Compute machine management](01_02_compute_machine_management.md)
- [1.3. Control plane machine management](01_03_control_plane_machine_management.md)
- [1.4. Cluster autoscaling](01_04_cluster_autoscaling.md)
- [1.5. Compute machine creation on user-provisioned infrastructure](01_05_compute_machine_creation_on_user_provisioned_infrastructure.md)
